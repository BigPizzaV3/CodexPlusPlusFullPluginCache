// Puppeteer helpers for Browserless. No live HA connection or browser launch here.
export function createBrowserHelpers(page) {
  const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
  // A path is CSS at each successive open shadow root, ending at one element.
  const inspect = async (path, scroll = false) => page.evaluate(({path,scroll}) => {
    let root = document, el;
    for (let i = 0; i < path.length; i++) {
      const matches = root.querySelectorAll(path[i]);
      if (matches.length !== 1) throw new Error('Target must be unique: '+path[i]);
      el = matches[0];
      if (i < path.length-1) {
        root = el.shadowRoot;
        if (!root) throw new Error('Missing open shadow root: '+path[i]);
      }
    }
    if (!el) throw new Error('Empty target path');
    let rect = el.getBoundingClientRect();
    if (scroll && (rect.top < 0 || rect.bottom > innerHeight || rect.left < 0 || rect.right > innerWidth)) {
      el.scrollIntoView({block:'center',inline:'center',behavior:'instant'});
      rect = el.getBoundingClientRect();
    }
    const x = rect.left+rect.width/2, y = rect.top+rect.height/2;
    let hit = document.elementFromPoint(x,y);
    while (hit?.shadowRoot) {
      const next = hit.shadowRoot.elementFromPoint(x,y);
      if (!next || next === hit) break;
      hit = next;
    }
    let node = hit, receives = false;
    while (node) {
      if (node === el) { receives = true; break; }
      node = node.parentElement || node.getRootNode()?.host;
    }
    let active = document.activeElement;
    while (active?.shadowRoot?.activeElement) active = active.shadowRoot.activeElement;
    const css = getComputedStyle(el);
    let ancestor=el, ancestorsVisible=true, inert=false;
    while(ancestor) {
      const style=getComputedStyle(ancestor);
      if(style.display==='none' || ['hidden','collapse'].includes(style.visibility) || Number(style.opacity)===0) ancestorsVisible=false;
      inert ||= ancestor.hasAttribute('inert');
      ancestor=ancestor.parentElement || ancestor.getRootNode()?.host;
    }
    const viewport={left:window.visualViewport?.offsetLeft??0,top:window.visualViewport?.offsetTop??0,
      width:window.visualViewport?.width??innerWidth,height:window.visualViewport?.height??innerHeight};
    const clipped={left:Math.max(rect.left,viewport.left),top:Math.max(rect.top,viewport.top),
      right:Math.min(rect.right,viewport.left+viewport.width),bottom:Math.min(rect.bottom,viewport.top+viewport.height)};
    const area=Math.max(0,clipped.right-clipped.left)*Math.max(0,clipped.bottom-clipped.top);
    const viewportFraction=rect.width*rect.height>0?area/(rect.width*rect.height):0;
    const hitSamples=[];
    if(area>0) for(const [fx,fy] of [[.5,.5],[.2,.2],[.8,.2],[.2,.8],[.8,.8]]) {
      const px=clipped.left+(clipped.right-clipped.left)*fx,py=clipped.top+(clipped.bottom-clipped.top)*fy;
      let candidate=document.elementFromPoint(px,py);
      while(candidate?.shadowRoot) {
        const next=candidate.shadowRoot.elementFromPoint(px,py);
        if(!next || next===candidate) break;
        candidate=next;
      }
      let cursor=candidate,matched=false;
      while(cursor) {
        if(cursor===el) {matched=true;break;}
        cursor=cursor.parentElement || cursor.getRootNode()?.host;
      }
      hitSamples.push({x:px,y:py,receives:matched});
    }
    const cssVisible=ancestorsVisible && (typeof el.checkVisibility!=='function' ||
      el.checkVisibility({checkOpacity:true,checkVisibilityCSS:true,contentVisibilityAuto:true}));
    return {x,y,top:rect.top,bottom:rect.bottom,left:rect.left,right:rect.right,
      width:rect.width,height:rect.height,receives,disabled:inert||el.matches(':disabled,[aria-disabled="true"]'),
      visible:cssVisible&&css.display!=='none'&&rect.width>0&&rect.height>0,
      viewport,viewportFraction,hitSamples,inert,
      sampledHitFraction:hitSamples.length?hitSamples.filter(s=>s.receives).length/hitSamples.length:0,
      inViewport:x>=0&&y>=0&&x<innerWidth&&y<innerHeight,
      focused:active===el,value:'value' in el?el.value:null,
      selectionStart:el.selectionStart??null,selectionEnd:el.selectionEnd??null,
      selectionDirection:el.selectionDirection??null,scrollY,scrollTop:el.scrollTop,
      tag:el.tagName,id:el.id};
  },{path,scroll});
  return {
    inspect,
    async sample(path,{durationMs=1000,intervalMs=100}={}) {
      if(!Number.isFinite(durationMs) || durationMs<=0 || durationMs>30000 ||
        !Number.isFinite(intervalMs) || intervalMs<=0 || intervalMs>durationMs)
        throw new Error('Use a bounded sample window and positive interval');
      const samples=[],start=performance.now();
      do {
        let observation;
        try {observation=await inspect(path);}
        catch(error) {error.auditSamples=samples; throw error;}
        samples.push({at:performance.now()-start,observation});
        const elapsed=samples.at(-1).at-samples[0].at;
        if(elapsed>=durationMs) break;
        await pause(Math.min(intervalMs,durationMs-elapsed));
      } while(true);
      return {samples,timeDomain:'monotonic-real',requestedDurationMs:durationMs,
        scope:'Sampled geometry and hit tests; inspect screenshots and device-specific gaps separately'};
    },
    async tap(path,{timeoutMs=2500,stableMs=80}={}) {
      await inspect(path,true);
      const started = Date.now(); let prior, stableAt = Date.now();
      while (Date.now()-started < timeoutMs) {
        const now = await inspect(path);
        if (!prior || ['top','left','width','height'].some(k=>Math.abs(now[k]-prior[k])>.5)) stableAt=Date.now();
        if (now.visible && now.inViewport && now.receives && !now.disabled && Date.now()-stableAt>=stableMs) {
          await page.touchscreen.tap(now.x,now.y);
          return {input:'browser-touch',point:{x:now.x,y:now.y},target:now};
        }
        prior=now; await pause(20);
      }
      throw new Error('Target did not become stable, visible and actionable');
    },
    async type(text,{delay=20}={}) { await page.keyboard.type(text,{delay}); },
    async until(fn,{timeoutMs=2500,intervalMs=25}={}) {
      const start=Date.now(); let value;
      do { value=await fn(); if(value) return value; await pause(intervalMs); } while(Date.now()-start<timeoutMs);
      throw new Error('Expected condition did not settle before deadline');
    },
    async swipe({x,y,toX,toY,durationMs=220,steps=12}) {
      const session = await page.target().createCDPSession();
      try {
        await session.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y}]});
        for(let i=1;i<=steps;i++) {
          await session.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:x+(toX-x)*i/steps,y:y+(toY-y)*i/steps}]});
          await pause(durationMs/steps);
        }
      } finally {
        try { await session.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]}); }
        finally { await session.detach(); }
      }
    }
  };
}
