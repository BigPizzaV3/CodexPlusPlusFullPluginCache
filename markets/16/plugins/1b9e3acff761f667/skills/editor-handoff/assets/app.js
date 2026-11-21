"use strict";
(() => {
  const node = document.getElementById("handoff-data");
  if (!node) return;
  const data = JSON.parse(node.textContent);
  // Include doctor, source and profile revisions: another doctor's or an older case
  // cannot silently populate these choices.
  const fingerprint = JSON.stringify([data.case_id, data.doctor_id, data.source, data.profile, data.scenes]);
  const storageKey = "dr-shigyo-handoff:" + fingerprint;
  const scenes = new Map(data.scenes.map(scene => [scene.id, scene]));
  let state = new Map(data.scenes.map(scene => [scene.id, {selected: scene.selected, omit: scene.omit, note: ""}]));
  const storageLabel = document.querySelector(".storage-state");
  const statusLabel = document.getElementById("selection-status");
  function report(message) { if (storageLabel) storageLabel.textContent = message; }
  function changed(scene, item) {
    return item.selected !== scene.selected || item.omit !== scene.omit || Boolean(item.note.trim());
  }
  function validateImport(value) {
    if (!value || value.schema_version !== 1 || value.case_id !== data.case_id ||
        value.doctor_id !== data.doctor_id || !value.source || value.source.sha256 !== data.source.sha256 ||
        value.source.version !== data.source.version || JSON.stringify(value.profile) !== JSON.stringify(data.profile) ||
        !Array.isArray(value.selections) || value.selections.length !== scenes.size) {
      throw new Error("案件・医師・原稿・本人設定の版が一致しません。対応するJSONを選んでください。");
    }
    const next = new Map();
    for (const item of value.selections) {
      const scene = item && scenes.get(item.scene_id);
      if (!scene || next.has(item.scene_id) || typeof item.omit !== "boolean" ||
          typeof item.note !== "string" || item.note.length > 100000 ||
          !(item.selected === null || scene.options.some(option => option.id === item.selected)) ||
          (item.omit && item.selected !== null)) {
        throw new Error("選択ID・修正メモの形式が不正です。");
      }
      next.set(item.scene_id, {selected: item.selected, omit: item.omit, note: item.note});
    }
    return next;
  }
  function exportData() {
    const selections = data.scenes.map(scene => {
      const item = state.get(scene.id);
      return {scene_id: scene.id, selected: item.selected, omit: item.omit, note: item.note,
        original_selected: scene.selected, original_omit: scene.omit,
        changed: changed(scene, item)};
    });
    return {schema_version: 1, case_id: data.case_id, title: data.title, doctor_id: data.doctor_id,
      source: data.source, profile: data.profile, exported_at: new Date().toISOString(),
      package_status: data.package_status,
      selection_status: selections.some(item => item.changed) ? "changes_pending" : "unchanged",
      selections};
  }
  function save() {
    try {
      localStorage.setItem(storageKey, JSON.stringify(exportData()));
      report("ブラウザー内に保存しました。別の端末へ渡すときはJSONを保存してください。");
    } catch (_) {
      report("このブラウザーでは自動保存できません。JSONを書き出せば選択とメモを保存できます。");
    }
  }
  function refresh() {
    let count = 0;
    document.querySelectorAll("[data-scene]").forEach(card => {
      const scene = scenes.get(card.dataset.scene);
      const item = state.get(scene.id);
      const isChanged = changed(scene, item);
      if (isChanged) count++;
      card.classList.toggle("is-changed", isChanged);
      const selectedOption = scene.options.find(option => option.id === item.selected);
      const newLabel = item.omit ? "素材なし" : selectedOption ? selectedOption.title : "未選択";
      card.querySelector(".change-state").textContent = isChanged ?
        "変更待ち：" + newLabel + "。下の納品素材は更新前です。書き出した選択・メモを反映して再生成してください。" : "";
      const radioValue = item.omit ? "__none__" : item.selected === null ? "__unselected__" : item.selected;
      card.querySelectorAll("input[type=radio]").forEach(radio => { radio.checked = radio.value === radioValue; });
      card.querySelector(".scene-memo").value = item.note;
    });
    const summary = document.querySelector(".summary");
    summary.classList.toggle("is-changed", Boolean(count));
    statusLabel.textContent = count ? count + "か所の変更待ち。現在のZIPにはまだ反映されていません。" : "選択変更はありません。";
    document.getElementById("package-status").textContent = count ? "変更待ち — 再生成が必要です" :
      data.package_status === "complete" ? "採用素材・台本の確認記録あり" : "要確認・制作待ちあり";
  }
  document.querySelectorAll("[data-scene]").forEach(card => {
    const sid = card.dataset.scene;
    card.querySelectorAll("input[type=radio]").forEach(radio => radio.addEventListener("change", () => {
      if (!radio.checked) return;
      const item = state.get(sid);
      item.selected = radio.value === "__none__" || radio.value === "__unselected__" ? null : radio.value;
      item.omit = radio.value === "__none__";
      refresh(); save();
    }));
    card.querySelector(".scene-memo").addEventListener("input", event => {
      state.get(sid).note = event.target.value;
      // Do not replace a focused textarea while the user is typing.
      const start = event.target.selectionStart, end = event.target.selectionEnd;
      refresh();
      event.target.setSelectionRange(start, end);
      save();
    });
  });
  function download(name, text, type) {
    if (document.body.dataset.previewMode) {
      let panel = document.getElementById("preview-export");
      if (!panel) {
        panel = document.createElement("section");
        panel.id = "preview-export"; panel.className = "preview-export";
        const label = document.createElement("label");
        label.htmlFor = "preview-export-text";
        label.textContent = "コピーして次の制作チャットへ貼り付けてください";
        const area = document.createElement("textarea");
        area.id = "preview-export-text"; area.readOnly = true;
        panel.append(label, area);
        document.getElementById("export").appendChild(panel);
      }
      panel.querySelector("textarea").value = text;
      panel.querySelector("textarea").focus();
      panel.querySelector("textarea").select();
      report(name + " をコピー欄に表示しました。ダウンロードできない画面でも内容を保存できます。");
      return;
    }
    const url = URL.createObjectURL(new Blob([text], {type}));
    const link = document.createElement("a");
    link.href = url; link.download = name; document.body.appendChild(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 30000);
  }
  document.getElementById("export-json").addEventListener("click", () =>
    download(data.case_id + "-selections.json", JSON.stringify(exportData(), null, 2) + "\n", "application/json;charset=utf-8"));
  document.getElementById("export-request").addEventListener("click", () => {
    const rows = ["# 台本・素材の修正依頼", "", "案件：" + data.title, "案件ID：" + data.case_id,
      "医師ID：" + data.doctor_id, "原稿SHA-256：" + data.source.sha256,
      "原稿版：" + data.source.version, "本人設定版：" + data.profile.version,
      "デザイン版：" + data.profile.design_version, "",
      "以下の選択と修正を反映し、同じ案件の確認ページを同じURLで更新してください。台本と素材が一体になった納品ZIPも更新してください。",
      "未制作の候補は実ファイルを制作・確認するまで完成扱いにしないでください。", ""];
    for (const scene of data.scenes) {
      const item = state.get(scene.id);
      const option = scene.options.find(value => value.id === item.selected);
      const label = item.omit ? "素材なしで確定" : option ? option.id + "｜" + option.title : "未選択";
      rows.push("- " + scene.id + "： " + label + (changed(scene, item) ? "【変更待ち】" : "【現状維持】"));
      if (item.note.trim()) rows.push("  修正メモ：" + item.note.trim().replace(/\n/g, "\n  "));
    }
    download(data.case_id + "-修正依頼.md", rows.join("\n") + "\n", "text/markdown;charset=utf-8");
  });
  document.getElementById("import-json").addEventListener("change", async event => {
    const file = event.target.files[0];
    if (!file) return;
    try {
      if (file.size > 4 * 1024 * 1024) throw new Error("JSONが大きすぎます。選択結果ファイルを指定してください。");
      state = validateImport(JSON.parse(await file.text()));
      refresh(); save();
    } catch (error) { report("読み込みできません：" + error.message); }
    event.target.value = "";
  });
  document.getElementById("reset-choices").addEventListener("click", () => {
    if (!window.confirm("このページで変更した選択と修正メモを初期化します。必要なら先にJSONを保存してください。")) return;
    state = new Map(data.scenes.map(scene => [scene.id, {selected: scene.selected, omit: scene.omit, note: ""}]));
    refresh(); save();
  });
  try {
    const previous = localStorage.getItem(storageKey);
    if (previous) {
      state = validateImport(JSON.parse(previous));
      report("このブラウザーに保存された選択と修正メモを復元しました。");
    }
  } catch (_) { report("自動保存の復元は使えません。保存したJSONを読み込めます。"); }
  refresh();
  const query = document.getElementById("search-query"), countLabel = document.getElementById("search-count");
  let hits = [], cursor = -1;
  function collect() {
    document.querySelectorAll(".search-hit").forEach(item => item.classList.remove("search-hit"));
    const value = query.value.trim();
    hits = value ? [...document.querySelectorAll(".source-text,.source-heading,.asset-card h3,.quote")].filter(item => item.textContent.includes(value)) : [];
    cursor = -1; countLabel.textContent = value ? hits.length + "件" : "";
  }
  function next() {
    if (!hits.length) return;
    document.querySelectorAll(".search-hit").forEach(item => item.classList.remove("search-hit"));
    cursor = (cursor + 1) % hits.length;
    hits[cursor].classList.add("search-hit");
    hits[cursor].scrollIntoView({behavior: "smooth", block: "center"});
    countLabel.textContent = (cursor + 1) + " / " + hits.length + "件";
  }
  query.addEventListener("input", collect);
  query.addEventListener("keydown", event => { if (event.key === "Enter") { event.preventDefault(); next(); } });
  document.getElementById("search-next").addEventListener("click", next);
})();

