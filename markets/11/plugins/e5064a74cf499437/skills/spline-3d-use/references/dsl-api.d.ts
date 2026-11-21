// Spline 3D editor DSL: every function `3d_run_code` can call, with the
// argument types the sandbox checks each call against. Generated from the
// editor's own argument schemas. Return values are untyped here; the
// authoring guide documents what each function returns.

// ---- Create objects --------------------------------------------------------

/**
 * @param parameters a plain object of properties
 */
declare function add(objectType: string, geometryType?: string, parameters?: Record<string, unknown>): any;

/**
 * @param parameters a plain object of properties
 */
declare function mesh(geometryType: string, parameters?: Record<string, unknown>): any;

/**
 * @param params customMesh params — { vertices: number[] (flat x,y,z triples), indices?: int[], normals?: number[], uvs?: number[] }
 */
declare function customMesh(params: {
  vertices: number[];
  indices?: number[];
  normals?: number[];
  uvs?: number[];
}): any;

declare function object(name: string): any;

/**
 * @param props light props — { color?, intensity?, distance?, decay?, angle?, penumbra?, size?, shadows?, shadowRadius?, shadowResolution? }
 */
declare function light(type: string | {
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  color?: string | {
    r: number;
    g: number;
    b: number;
  };
  intensity?: number;
  distance?: number;
  decay?: number;
  angle?: number;
  penumbra?: number;
  penumbraSize?: number;
  size?: number;
  depth?: number;
  shadows?: boolean;
  shadowRadius?: number;
  shadowResolution?: number;
}, props?: {
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  color?: string | {
    r: number;
    g: number;
    b: number;
  };
  intensity?: number;
  distance?: number;
  decay?: number;
  angle?: number;
  penumbra?: number;
  penumbraSize?: number;
  size?: number;
  depth?: number;
  shadows?: boolean;
  shadowRadius?: number;
  shadowResolution?: number;
}): any;

/**
 * @param points an array of [x, y, z] points
 */
declare function path(points?: [number, number, number][]): any;

/**
 * @param typeOrProps 'new' (create an emitter) or a particle-props object (edit the selected emitter)
 * @param props particle emitter props — { birthRatePerSec?, life?, speed?, gravity?, direction?, material?, shape?, autoPlay?, emitTimeCycle?, … } (load the particles skill for the full reference)
 */
declare function particles(typeOrProps?: "new" | {
  birthRatePerSec?: number;
  life?: number;
  speed?: number;
  gravity?: number;
  /** an [x, y, z] array of 3 numbers */
  direction?: [number, number, number];
  directionMode?: "axis" | "normals";
  noiseStrength?: number;
  noiseScale?: number;
  noiseSeed?: number;
  noiseType?: "curl" | "simplex" | "fbm";
  randomRotation?: number;
  randomScale?: number;
  randomMass?: number;
  rootObjectType?: "instancedMesh" | "points";
  autoPlay?: boolean;
  emitTimeCycle?: "infinity" | "loop" | "one_time";
  emitTimeDuration?: number;
  emitTimeDelay?: number;
  colliderEntityId?: string | {
    id: string;
  } | null;
  collisionBounce?: number;
  /** particle sprite props — { color?, color2?, coloring?, ease?, easeSize?, size?: [start, end], spriteRotation?, transparent? } (sprite textures are not settable from code) */
  material?: {
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    color?: string | {
      r: number;
      g: number;
      b: number;
    };
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    color2?: string | {
      r: number;
      g: number;
      b: number;
    };
    coloring?: "gradient" | "random";
    /** an over-life ease — 'linearFadeIn' | 'linearFadeOut' | 'linearInOut' | 'quickFadeInOut' | 'exponentialInOut' | 'constant' */
    ease?: "linearFadeIn" | "linearFadeOut" | "linearInOut" | "quickFadeInOut" | "exponentialInOut" | "constant";
    /** an over-life ease — 'linearFadeIn' | 'linearFadeOut' | 'linearInOut' | 'quickFadeInOut' | 'exponentialInOut' | 'constant' */
    easeSize?: "linearFadeIn" | "linearFadeOut" | "linearInOut" | "quickFadeInOut" | "exponentialInOut" | "constant";
    /** a [start, end] array of 2 numbers */
    size?: [number, number];
    /** a [start, end] array of 2 numbers */
    spriteRotation?: [number, number];
    transparent?: boolean;
  };
  /** an emitter shape — { type?: 'Plane'|'Box'|'Sphere'|'Cone'|'Torus'|'Mesh', size?: [x,y,z] or number, fromMeshId? } */
  shape?: {
    /** 'Plane' | 'Box' | 'Sphere' | 'Cone' | 'Torus' | 'Mesh' (emit from another object) */
    type?: string;
    size?: number | [number, number, number];
    fromMeshId?: string | {
      id: string;
    } | null;
  };
}, props?: {
  birthRatePerSec?: number;
  life?: number;
  speed?: number;
  gravity?: number;
  /** an [x, y, z] array of 3 numbers */
  direction?: [number, number, number];
  directionMode?: "axis" | "normals";
  noiseStrength?: number;
  noiseScale?: number;
  noiseSeed?: number;
  noiseType?: "curl" | "simplex" | "fbm";
  randomRotation?: number;
  randomScale?: number;
  randomMass?: number;
  rootObjectType?: "instancedMesh" | "points";
  autoPlay?: boolean;
  emitTimeCycle?: "infinity" | "loop" | "one_time";
  emitTimeDuration?: number;
  emitTimeDelay?: number;
  colliderEntityId?: string | {
    id: string;
  } | null;
  collisionBounce?: number;
  /** particle sprite props — { color?, color2?, coloring?, ease?, easeSize?, size?: [start, end], spriteRotation?, transparent? } (sprite textures are not settable from code) */
  material?: {
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    color?: string | {
      r: number;
      g: number;
      b: number;
    };
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    color2?: string | {
      r: number;
      g: number;
      b: number;
    };
    coloring?: "gradient" | "random";
    /** an over-life ease — 'linearFadeIn' | 'linearFadeOut' | 'linearInOut' | 'quickFadeInOut' | 'exponentialInOut' | 'constant' */
    ease?: "linearFadeIn" | "linearFadeOut" | "linearInOut" | "quickFadeInOut" | "exponentialInOut" | "constant";
    /** an over-life ease — 'linearFadeIn' | 'linearFadeOut' | 'linearInOut' | 'quickFadeInOut' | 'exponentialInOut' | 'constant' */
    easeSize?: "linearFadeIn" | "linearFadeOut" | "linearInOut" | "quickFadeInOut" | "exponentialInOut" | "constant";
    /** a [start, end] array of 2 numbers */
    size?: [number, number];
    /** a [start, end] array of 2 numbers */
    spriteRotation?: [number, number];
    transparent?: boolean;
  };
  /** an emitter shape — { type?: 'Plane'|'Box'|'Sphere'|'Cone'|'Torus'|'Mesh', size?: [x,y,z] or number, fromMeshId? } */
  shape?: {
    /** 'Plane' | 'Box' | 'Sphere' | 'Cone' | 'Torus' | 'Mesh' (emit from another object) */
    type?: string;
    size?: number | [number, number, number];
    fromMeshId?: string | {
      id: string;
    } | null;
  };
}): any;

/**
 * @param typeOrProps 'new' (create a Hair System) or a hair-props object (edit the selected one)
 * @param props hair system props — { on?: 'ObjectName', hairLength?, hairWidth?, windStrength?, hairRootColor?, … } (load the hair skill for the full reference)
 */
declare function hair(typeOrProps?: "new" | {
  /** the object whose surface the strands grow from (name, id, or handle) */
  on?: {
    id: string;
  } | string | null;
  headShape?: string;
  gravity?: number;
  damping?: number;
  localStiffness?: number;
  globalStiffness?: number;
  globalRange?: number;
  stiffnessFalloff?: number;
  windStrength?: number;
  vspCoefficient?: number;
  elasticity?: number;
  hairLength?: number;
  tipSeparation?: number;
  kink?: number;
  kinkFrequency?: number;
  clumpStrength?: number;
  clumpSize?: number;
  clumpTipScale?: number;
  spreadRadius?: number;
  guideStrands?: number;
  hairColorSource?: string;
  hairShadeRoot?: number;
  hairShadeTip?: number;
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  hairRootColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  hairMidColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  hairTipColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  headColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  noiseEnabled?: boolean;
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorA?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorB?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorC?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorD?: string | {
    r: number;
    g: number;
    b: number;
  };
  noiseScale?: number;
  noiseMixHair?: number;
  noiseMixHead?: number;
  castShadow?: boolean;
  receiveShadow?: boolean;
  hairWidth?: number;
  specularPower?: number;
  specularIntensity?: number;
  diffuseIntensity?: number;
  ambientIntensity?: number;
  opacity?: number;
  tipFade?: number;
  autoPlay?: boolean;
}, props?: {
  /** the object whose surface the strands grow from (name, id, or handle) */
  on?: {
    id: string;
  } | string | null;
  headShape?: string;
  gravity?: number;
  damping?: number;
  localStiffness?: number;
  globalStiffness?: number;
  globalRange?: number;
  stiffnessFalloff?: number;
  windStrength?: number;
  vspCoefficient?: number;
  elasticity?: number;
  hairLength?: number;
  tipSeparation?: number;
  kink?: number;
  kinkFrequency?: number;
  clumpStrength?: number;
  clumpSize?: number;
  clumpTipScale?: number;
  spreadRadius?: number;
  guideStrands?: number;
  hairColorSource?: string;
  hairShadeRoot?: number;
  hairShadeTip?: number;
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  hairRootColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  hairMidColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  hairTipColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  headColor?: string | {
    r: number;
    g: number;
    b: number;
  };
  noiseEnabled?: boolean;
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorA?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorB?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorC?: string | {
    r: number;
    g: number;
    b: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  noiseColorD?: string | {
    r: number;
    g: number;
    b: number;
  };
  noiseScale?: number;
  noiseMixHair?: number;
  noiseMixHead?: number;
  castShadow?: boolean;
  receiveShadow?: boolean;
  hairWidth?: number;
  specularPower?: number;
  specularIntensity?: number;
  diffuseIntensity?: number;
  ambientIntensity?: number;
  opacity?: number;
  tipFade?: number;
  autoPlay?: boolean;
}): any;

/**
 * @param props a plain object of properties
 */
declare function clone(props: Record<string, unknown>): any;

/**
 * @param target a scene object (as returned by select/add/mesh)
 * @param props a plain object of properties
 */
declare function cloneTo(target: {
  id: string;
}, props: Record<string, unknown>): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function duplicate(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function component(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function instance(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

declare function detachInstance(): any;

// ---- Generate procedural content -------------------------------------------

/**
 * @param params terrain params — { width?, depth?, maxHeight?, resolution?, seed?, noiseScale?, octaves?, falloff?: 'none'|'island', plateau?: 0..1, color?, name?, position?: [x,y,z] }
 */
declare function terrain(params?: {
  /** range at least 10 */
  width?: number;
  /** range at least 10 */
  depth?: number;
  /** range at least 0 */
  maxHeight?: number;
  /** range 4 to 243 */
  resolution?: number;
  seed?: number;
  /** feature frequency across the width — 1.5-3 reads as rolling hills; higher values pack smaller hills (capped against the grid resolution to prevent spiky aliasing) (at most 12) */
  noiseScale?: number;
  /** range 1 to 8 */
  octaves?: number;
  falloff?: "none" | "island";
  /** range 0 to 1 */
  plateau?: number;
  /** a color string like '#7c9a5f' */
  color?: string;
  name?: string;
  /** an [x, y, z] array of 3 numbers */
  position?: [number, number, number];
}): any;

/**
 * @param params ocean params — { width?, depth?, waveHeight?, wavelength?, direction?: degrees, choppiness?: 0..1, resolution?, seed?, color?, name?, position?: [x,y,z] } — directional Gerstner swells, smooth-shaded
 */
declare function ocean(params?: {
  /** range at least 10 */
  width?: number;
  /** range at least 10 */
  depth?: number;
  waveHeight?: number;
  wavelength?: number;
  direction?: number;
  /** range 0 to 1 */
  choppiness?: number;
  /** range 8 to 243 */
  resolution?: number;
  seed?: number;
  /** a color string like '#7c9a5f' */
  color?: string;
  name?: string;
  /** an [x, y, z] array of 3 numbers */
  position?: [number, number, number];
}): any;

/**
 * @param params globe params — { radius?, style?: 'dots'|'relief', cellStep?, dotSize?, oceanColor?, landColor?, name?, position? } — REAL Earth continents; handle exposes project(lat, long) for city markers
 */
declare function globe(params?: {
  /** range at least 10 */
  radius?: number;
  /** 'dots' = dotted-matrix data-viz globe; 'relief' = raised low-poly land */
  style?: "dots" | "relief";
  /** range 2 to 12 */
  cellStep?: number;
  /** range at most 0.05 */
  dotSize?: number;
  /** a color string like '#7c9a5f' */
  oceanColor?: string;
  /** a color string like '#7c9a5f' */
  landColor?: string;
  name?: string;
  /** an [x, y, z] array of 3 numbers */
  position?: [number, number, number];
}): any;

/**
 * @param params building params — { width?, depth?, height?, style?: 'modern'|'futuristic'|'blocky', seed?, litRatio?: 0..1, bodyColor?, windowColor?, litColor?, name?, position? } — setback massing + real per-window geometry with a lit subset
 */
declare function building(params?: {
  /** range at least 20 */
  width?: number;
  /** range at least 20 */
  depth?: number;
  /** range at least 40 */
  height?: number;
  style?: "modern" | "futuristic" | "blocky";
  seed?: number;
  /** range 0 to 1 */
  litRatio?: number;
  /** a color string like '#7c9a5f' */
  bodyColor?: string;
  /** a color string like '#7c9a5f' */
  windowColor?: string;
  /** a color string like '#7c9a5f' */
  litColor?: string;
  name?: string;
  /** an [x, y, z] array of 3 numbers */
  position?: [number, number, number];
}): any;

/**
 * @param params tree params — { kind?: 'oak'|'pine'|'palm'|'birch'|'bush', height?, seed?, leafiness?: 0..1, style?: 'realistic'|'stylized', trunkColor?, leafColor?, name?, position?: [x,y,z] }
 */
declare function tree(params?: {
  kind?: "oak" | "pine" | "palm" | "birch" | "bush";
  /** range at least 10 */
  height?: number;
  seed?: number;
  /** range 0 to 1 */
  leafiness?: number;
  /** 'realistic' (the default): lobed, noise-displaced canopies on visible branches. 'stylized': smooth low-poly blobs — pass it ONLY when the prompt asks for cute/cartoon/toy scenes */
  style?: "realistic" | "stylized";
  /** a color string like '#7c9a5f' */
  trunkColor?: string;
  /** a color string like '#7c9a5f' */
  leafColor?: string;
  name?: string;
  /** an [x, y, z] array of 3 numbers */
  position?: [number, number, number];
}): any;

/**
 * @param params rock params — { size?, seed?, detail?: 0|1|2, angularity?: 0..1, flattenBottom?: 0..1, color?, name?, position?: [x,y,z] }
 */
declare function rock(params?: {
  /** range at least 1 */
  size?: number;
  seed?: number;
  /** range 0 to 2 */
  detail?: number;
  /** range 0 to 1 */
  angularity?: number;
  /** range 0 to 1 */
  flattenBottom?: number;
  /** a color string like '#7c9a5f' */
  color?: string;
  name?: string;
  /** an [x, y, z] array of 3 numbers */
  position?: [number, number, number];
}): any;

/**
 * @param params scatter params — { on: surface object, source: object to distribute, count?, seed?, align?: 'normal'|'up', spread?: 'random'|'even', scaleJitter?: 0..1, rotationJitter?: degrees, hideBase? }
 */
declare function scatter(params: {
  /** an object name, id, or an object handle returned by an alias */
  on: {
    id: string;
  } | string;
  /** an object name, id, or an object handle returned by an alias */
  source: {
    id: string;
  } | string;
  /** range 1 to 1000 */
  count?: number;
  seed?: number;
  align?: "normal" | "up";
  spread?: "random" | "even";
  /** range 0 to 1 */
  scaleJitter?: number;
  /** range 0 to 360 */
  rotationJitter?: number;
  hideBase?: boolean;
}): any;

/**
 * @param params layout params — { constraints: [...], objects?, fixed?, region?: { center?: [x,z], size: [w,d] }, seed?, iterations?, noOverlap? }
 */
declare function layout(params: {
  constraints: Array<{
    type: "near" | "apart" | "on" | "against" | "facing" | "align" | "inside" | "spread";
    /** an object name, id, or an object handle returned by an alias */
    a?: {
      id: string;
    } | string;
    /** an object name, id, or an object handle returned by an alias */
    b?: {
      id: string;
    } | string;
    items?: Array<{
      id: string;
    } | string>;
    axis?: "x" | "z";
    min?: number;
    max?: number;
    margin?: number;
    weight?: number;
  }>;
  objects?: Array<{
    id: string;
  } | string>;
  fixed?: Array<{
    id: string;
  } | string>;
  region?: {
    center?: [number, number];
    size: [number, number];
  };
  seed?: number;
  /** range 100 to 20000 */
  iterations?: number;
  noOverlap?: boolean;
}): any;

// ---- Select objects --------------------------------------------------------

/**
 * @param targetOrFilter a target — an object from select/add/mesh, an array of them, 'all', or a count
 * @param mode 'add'
 */
declare function select(targetOrFilter: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown), count?: number | string, mode?: "add"): any;

declare function unselect(targetOrFilter?: {
  id: string;
} | Array<{
  id: string;
}> | ((object: any) => unknown), count?: number): any;

/**
 * @param callback a callback
 */
declare function iterate(callback: (object: any) => unknown): any;

// ---- Transform, arrange and organize ---------------------------------------

/**
 * @param p a vector like { x?, y?, z? } with number components
 */
declare function position(p: {
  x?: number;
  y?: number;
  z?: number;
}): any;

/**
 * @param p a vector like { x?, y?, z? } with number components
 */
declare function translate(p: {
  x?: number;
  y?: number;
  z?: number;
}): any;

/**
 * @param r a vector like { x?, y?, z? } with number components
 */
declare function rotation(r: {
  x?: number;
  y?: number;
  z?: number;
}): any;

/**
 * @param s a vector like { x?, y?, z? } with number components
 */
declare function scale(s: {
  x?: number;
  y?: number;
  z?: number;
}): any;

/**
 * @param props { animate?: boolean, duration?: number }
 */
declare function align(path: string | {
  id: string;
}, props?: {
  animate?: boolean;
  duration?: number;
}): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function arrange(margins?: number, target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 * @param groupId an id string
 */
declare function group(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number, groupId?: string): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function ungroup(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param parent the new parent — an object from select/group, an id, a name, or 'root'/null for the page root
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 * @param options { before?: sibling, after?: sibling } — where to insert among the new siblings (omit to append last)
 */
declare function moveInto(parent: {
  id: string;
} | string | null, target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown), options?: {
  before?: {
    id: string;
  } | string;
  after?: {
    id: string;
  } | string;
}): any;

declare function rename(value: string): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function hide(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function show(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param changes { wireframe?: boolean, flatShading?: boolean, side?: 'front'|'back'|'double', shadowCatcher?: boolean (Rectangle/Plane only) }
 */
declare function visibility(changes: {
  wireframe?: boolean;
  flatShading?: boolean;
  /** 'front' | 'back' | 'double' (or Side enum 0|1|2) */
  side?: "front" | "back" | "double" | number;
  shadowCatcher?: boolean;
}): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function remove(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number): any;

// ---- Edit geometry ---------------------------------------------------------

/**
 * @param changes a plain object of properties
 */
declare function geometry(changes: Record<string, unknown>): any;

/**
 * @param operation 'union' | 'subtract' | 'intersect'
 * @param target a target — an object from select/add/mesh, a name/id string, an array mixing those, or 'all'
 * @param booleanId an id string
 */
declare function boolean(operation: "union" | "subtract" | "subtraction" | "difference" | "intersect" | "intersection", target?: {
  id: string;
} | Array<{
  id: string;
} | string> | string | number, booleanId?: string): any;

/**
 * @param target a target — an object from select/add/mesh, a name/id string, an array mixing those, or 'all'
 * @param booleanId an id string
 */
declare function union(target?: {
  id: string;
} | Array<{
  id: string;
} | string> | string | number, booleanId?: string): any;

/**
 * @param target a target — an object from select/add/mesh, a name/id string, an array mixing those, or 'all'
 * @param booleanId an id string
 */
declare function subtract(target?: {
  id: string;
} | Array<{
  id: string;
} | string> | string | number, booleanId?: string): any;

/**
 * @param target a target — an object from select/add/mesh, a name/id string, an array mixing those, or 'all'
 * @param booleanId an id string
 */
declare function intersect(target?: {
  id: string;
} | Array<{
  id: string;
} | string> | string | number, booleanId?: string): any;

/**
 * @param target a target — an object from select/add/mesh, a name/id string, an array mixing those, or 'all'
 */
declare function bakeBoolean(target?: {
  id: string;
} | Array<{
  id: string;
} | string> | string | number): any;

/**
 * @param target a target — an object from select/add/mesh, a name/id string, an array mixing those, or 'all'
 */
declare function merge(target?: {
  id: string;
} | Array<{
  id: string;
} | string> | string | number): any;

/**
 * @param target the mesh to reduce — a name/id string, an object from select/mesh, an array mixing those (e.g. get('selection')), or 'all'
 * @param ratio the fraction of the TRIANGLES to keep, between 0 and 1 (a 70k-triangle mesh at 0.5 comes back at 35k)
 * @param options decimate options — { creaseAngle?: number } (degrees, default 30: normals further apart than this at one position count as a hard edge and are preserved), { errorLimit?: number } (deviation budget as a fraction of the mesh diagonal, default 0.01: raise it to let the reduction reshape more)
 */
declare function decimate(target: {
  id: string;
} | Array<{
  id: string;
} | string> | string, ratio: number, options?: {
  /** range 0 to 180 */
  creaseAngle?: number;
  /** range at most 1 */
  errorLimit?: number;
}): any;

/**
 * @param targetOrProps a target (like boolean/subtract take) to combine into a new Shape Blend, or a props object to edit the selected blend / member shapes
 * @param blendId an id string
 */
declare function shapeBlend(targetOrProps?: {
  /** 'union' | 'subtract' | 'intersect' */
  operation?: "union" | "subtract" | "subtraction" | "difference" | "intersect" | "intersection";
  blendRange?: number | "global";
  useColor?: boolean;
  /** range 5 to 9 */
  resolutionLevel?: number;
  useChildrenColors?: boolean;
} | {
  id: string;
} | Array<{
  id: string;
} | string> | string | number, blendId?: string): any;

// ---- Color and materials ---------------------------------------------------

/**
 * @param value a color — a hex/CSS string like '#e0552b' or an { r, g, b } object
 */
declare function color(value: string | {
  r: number;
  g: number;
  b: number;
}): any;

/**
 * @param alpha a number between 0 and 1
 */
declare function opacity(alpha: number): any;

/**
 * @param m a complete material state — must include its `layers` array
 */
declare function material(m: {
  layers: unknown[];
}): any;

/**
 * @param name the material asset's name, e.g. 'Brushed Gold'
 * @param props material-asset props — { name?, layers?: [{ type, …props }] } (layer entries use layer()'s semantics)
 */
declare function createMaterial(name: string, props?: {
  /** rename the asset */
  name?: string;
  layers?: Array<{
    /** layer type — 'color', 'light', 'noise', 'texture', 'fresnel', 'cavity', 'dust', … */
    type: string;
  }>;
}): any;

/**
 * @param nameOrId a material asset's name or id, e.g. 'Brushed Gold'
 */
declare function applyMaterial(nameOrId: string): any;

/**
 * @param nameOrId a material asset's name or id, e.g. 'Brushed Gold'
 * @param props material-asset props — { name?, layers?: [{ type, …props }] } (layer entries use layer()'s semantics)
 */
declare function updateMaterial(nameOrId: string, props: {
  /** rename the asset */
  name?: string;
  layers?: Array<{
    /** layer type — 'color', 'light', 'noise', 'texture', 'fresnel', 'cavity', 'dust', … */
    type: string;
  }>;
}): any;

/**
 * @param nameOrId a material asset's name or id, e.g. 'Brushed Gold'
 */
declare function deleteMaterial(nameOrId: string): any;

/**
 * @param props a plain object of properties
 */
declare function layer(type: string, props?: Record<string, unknown>): any;

/**
 * @param props a plain object of properties
 * @param id an id string
 */
declare function addLayer(type: string, props?: Record<string, unknown>, id?: string): any;

/**
 * @param layerId an id string
 * @param props a plain object of properties
 */
declare function updateLayer(layerId: string, props: Record<string, unknown>): any;

/**
 * @param idOrType a layer id or a layer type like 'glass'
 */
declare function removeLayer(idOrType: string): any;

/**
 * @param name the texture's asset name, e.g. 'Red Bricks'
 * @param draw a callback
 * @param size tile size in px — 128, 256, 512 (default) or 1024
 */
declare function generateTexture(name: string, draw: (object: any) => unknown, size?: number): any;

/**
 * @param props shading props — { category?, flatShading?, wireframe?, side?: 'front'|'back'|'double', ...lightLayerProps }
 */
declare function shading(props: {
  category?: string;
  flatShading?: boolean;
  wireframe?: boolean;
  /** 'front' | 'back' | 'double' (or Side enum 0|1|2) */
  side?: "front" | "back" | "double" | number;
}): any;

/**
 * @param props a boolean (both flags) or { cast?: boolean, receive?: boolean }
 */
declare function shadows(props: boolean | {
  cast?: boolean;
  receive?: boolean;
  castShadow?: boolean;
  receiveShadow?: boolean;
}): any;

/**
 * @param palette a non-empty array of colors
 */
declare function style(palette: Array<string | {
  r: number;
  g: number;
  b: number;
}>, seed?: number): any;

declare function prettify(): any;

// ---- Lighting, environment and effects -------------------------------------

/**
 * @param props light props — { color?, intensity?, distance?, decay?, angle?, penumbra?, size?, shadows?, shadowRadius?, shadowResolution? }
 */
declare function updateLight(props: {
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  color?: string | {
    r: number;
    g: number;
    b: number;
  };
  intensity?: number;
  distance?: number;
  decay?: number;
  angle?: number;
  penumbra?: number;
  penumbraSize?: number;
  size?: number;
  depth?: number;
  shadows?: boolean;
  shadowRadius?: number;
  shadowResolution?: number;
}): any;

/**
 * @param value a color — a hex/CSS string like '#e0552b' or an { r, g, b } object
 */
declare function background(value: string | {
  r: number;
  g: number;
  b: number;
}): any;

declare function fog(props?: {
  enabled?: boolean;
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  color?: string | {
    r: number;
    g: number;
    b: number;
  };
  near?: number;
  far?: number;
  useBackgroundColor?: boolean;
  /** 'linear' (default) fades by camera distance between near/far; 'height' is realistic exponential height fog — density decays with altitude and is integrated along each view ray, so scenes read clear from above and fogged at ground level (tuned via density/heightFalloff/heightBase, near/far ignored); 'both' stacks the two media — a near/far distance haze plus the height layer, one shared fog color */
  mode?: "linear" | "height" | "both";
  /** height mode: fog density per world unit at heightBase (~0.005; the editor UI shows the reciprocal as "Distance" — sight range in world units, so a 400-unit fog distance is density 0.0025) */
  density?: number;
  /** height mode: density decay per world unit of altitude (~0.01; the editor UI shows the reciprocal as "Thickness" — the layer height in world units, so a 100-unit-tall layer is heightFalloff 0.01) */
  heightFalloff?: number;
  /** height mode: world Y of the fog floor (default 0) */
  heightBase?: number;
} | "none" | null): any;

declare function sky(props?: {
  /** 'physical' (atmosphere + clouds) | 'hdri' (env image) */
  mode?: "physical" | "hdri";
  /** hours 0-24 (~6 sunrise, 12 noon, ~18 sunset) */
  timeOfDay?: number;
  /** 'clear' | 'mostlyClear' | 'partlyCloudy' | 'mostlyCloudy' | 'overcast' | 'storm' */
  weather?: string;
  lighting?: boolean | string;
  affectLighting?: boolean | string;
  /** range at least 0 */
  lightingIntensity?: number;
  clouds?: boolean;
  /** range at least 0 */
  windSpeed?: number;
  /** range at least 0 */
  wind?: number;
  animateWind?: boolean;
  /** range at least 0 */
  exposure?: number;
  seed?: number;
  hdri?: {
    /** a shared image asset id, or null for none */
    image?: string | null;
    /** rotation around Y in DEGREES */
    rotation?: number;
    /** range at least 0 */
    blur?: number;
    /** draw the image behind the scene (default true; false keeps its lighting + reflections only) */
    showBackground?: boolean;
  } | string;
} | boolean | "none" | null): any;

/**
 * @param props environment props — { fog?, sky?, ambient?: { color?, intensity? } | false, ao?: boolean | { radius?, bias? }, softShadow?: 'normal' (stock shadows, default) | 'low'|'medium'|'high' (PCSS soft shadows) }
 */
declare function environment(props: {
  fog?: {
    enabled?: boolean;
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    color?: string | {
      r: number;
      g: number;
      b: number;
    };
    near?: number;
    far?: number;
    useBackgroundColor?: boolean;
    /** 'linear' (default) fades by camera distance between near/far; 'height' is realistic exponential height fog — density decays with altitude and is integrated along each view ray, so scenes read clear from above and fogged at ground level (tuned via density/heightFalloff/heightBase, near/far ignored); 'both' stacks the two media — a near/far distance haze plus the height layer, one shared fog color */
    mode?: "linear" | "height" | "both";
    /** height mode: fog density per world unit at heightBase (~0.005; the editor UI shows the reciprocal as "Distance" — sight range in world units, so a 400-unit fog distance is density 0.0025) */
    density?: number;
    /** height mode: density decay per world unit of altitude (~0.01; the editor UI shows the reciprocal as "Thickness" — the layer height in world units, so a 100-unit-tall layer is heightFalloff 0.01) */
    heightFalloff?: number;
    /** height mode: world Y of the fog floor (default 0) */
    heightBase?: number;
  } | "none" | null;
  sky?: {
    /** 'physical' (atmosphere + clouds) | 'hdri' (env image) */
    mode?: "physical" | "hdri";
    /** hours 0-24 (~6 sunrise, 12 noon, ~18 sunset) */
    timeOfDay?: number;
    /** 'clear' | 'mostlyClear' | 'partlyCloudy' | 'mostlyCloudy' | 'overcast' | 'storm' */
    weather?: string;
    lighting?: boolean | string;
    affectLighting?: boolean | string;
    /** range at least 0 */
    lightingIntensity?: number;
    clouds?: boolean;
    /** range at least 0 */
    windSpeed?: number;
    /** range at least 0 */
    wind?: number;
    animateWind?: boolean;
    /** range at least 0 */
    exposure?: number;
    seed?: number;
    hdri?: {
      /** a shared image asset id, or null for none */
      image?: string | null;
      /** rotation around Y in DEGREES */
      rotation?: number;
      /** range at least 0 */
      blur?: number;
      /** draw the image behind the scene (default true; false keeps its lighting + reflections only) */
      showBackground?: boolean;
    } | string;
  } | boolean | "none" | null;
  ambient?: {
    enabled?: boolean;
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    color?: string | {
      r: number;
      g: number;
      b: number;
    };
    intensity?: number;
  } | boolean | "none";
  ao?: {
    enabled?: boolean;
    radius?: number;
    bias?: number;
    /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
    aoColor?: string | {
      r: number;
      g: number;
      b: number;
    };
    aoFullRes?: boolean;
  } | boolean | "none";
  softShadow?: "normal" | "low" | "medium" | "high";
}): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function studio(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param mode 'studio'
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function stage(mode: "studio", target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

declare function fx(type: string | null, props?: Record<string, unknown> | "none" | null): any;

// ---- States, events and animation ------------------------------------------

/**
 * @param stateProps animate() state props — { position?, rotation?, scale?, color?, width?, height?, depth?, geometry?, material? }
 * @param transitionProps tween props like { duration?, delay?, easing?, loop?, direction?, trigger? }
 */
declare function animate(stateProps: {
  /** a vector like { x?, y?, z? } with number components */
  position?: {
    x?: number;
    y?: number;
    z?: number;
  };
  /** a vector like { x?, y?, z? } with number components */
  rotation?: {
    x?: number;
    y?: number;
    z?: number;
  };
  /** a vector like { x?, y?, z? } with number components */
  scale?: {
    x?: number;
    y?: number;
    z?: number;
  };
  /** a color — a hex/CSS string like '#e0552b' or an { r, g, b } object */
  color?: string | {
    r: number;
    g: number;
    b: number;
  };
  width?: number;
  height?: number;
  depth?: number;
  /** a plain object of properties */
  geometry?: Record<string, unknown>;
  /** a plain object of properties */
  material?: Record<string, unknown>;
}, transitionProps?: {
  duration?: number;
  delay?: number;
  easing?: string | number;
  loop?: boolean;
  direction?: string;
  trigger?: string;
  mass?: number;
  stiffness?: number;
  damping?: number;
  velocity?: number;
  repeat?: number;
}): any;

declare function addState(name?: string): any;

declare function removeState(state: string): any;

declare function renameState(state: string, name: string): any;

declare function selectState(state: string | null): any;

/**
 * @param type an event type ('MouseDown' | 'MouseUp' | 'MouseHover' | 'MousePress' | 'KeyDown' | 'KeyUp' | 'KeyPress' | 'Start' | 'LookAt' | 'Follow' | 'DragDrop' | 'Scroll' | 'GameControl' | 'Conditional' | 'Collision' | 'Trigger' | 'Resize' | 'VariableChange' | 'API' | 'WEBHOOK' | 'AIAssistantListener' | 'AIAssistantTrigger')
 * @param eventId an id string
 */
declare function addEvent(type?: "MouseDown" | "MouseUp" | "MouseHover" | "MousePress" | "KeyDown" | "KeyUp" | "KeyPress" | "Start" | "LookAt" | "Follow" | "DragDrop" | "Scroll" | "GameControl" | "Conditional" | "Collision" | "Trigger" | "Resize" | "VariableChange" | "API" | "WEBHOOK" | "AIAssistantListener" | "AIAssistantTrigger", eventId?: string): any;

/**
 * @param eventId an id string
 * @param props a plain object of properties
 */
declare function updateEvent(eventId: string, props: Record<string, unknown>): any;

/**
 * @param eventId an id string
 */
declare function removeEvent(eventId: string): any;

/**
 * @param eventId an id string
 * @param actionId an id string
 * @param initialTweenId an id string
 * @param tweenId an id string
 */
declare function addAction(eventId: string, eventTypeOrActionType: string, actionTypeOrContainer?: string, container?: string, actionId?: string, initialTweenId?: string, tweenId?: string): any;

/**
 * @param eventId an id string
 * @param actionId an id string
 * @param props a plain object of properties
 */
declare function updateAction(eventId: string, actionId: string, props: Record<string, unknown>): any;

/**
 * @param eventId an id string
 * @param actionId an id string
 */
declare function removeAction(eventId: string, actionId: string): any;

/**
 * @param eventId an id string
 * @param actionId an id string
 * @param props tween props like { duration?, delay?, easing?, loop?, direction?, trigger? }
 * @param tweenId an id string
 */
declare function addTween(eventId: string, actionId: string, props?: {
  duration?: number;
  delay?: number;
  easing?: string | number;
  loop?: boolean;
  direction?: string;
  trigger?: string;
  mass?: number;
  stiffness?: number;
  damping?: number;
  velocity?: number;
  repeat?: number;
}, tweenId?: string): any;

/**
 * @param eventId an id string
 * @param actionId an id string
 * @param tweenId an id string
 * @param props tween props like { duration?, delay?, easing?, loop?, direction?, trigger? }
 */
declare function updateTween(eventId: string, actionId: string, tweenId: string, props: {
  duration?: number;
  delay?: number;
  easing?: string | number;
  loop?: boolean;
  direction?: string;
  trigger?: string;
  mass?: number;
  stiffness?: number;
  damping?: number;
  velocity?: number;
  repeat?: number;
}): any;

/**
 * @param eventId an id string
 * @param actionId an id string
 * @param tweenId an id string
 */
declare function removeTween(eventId: string, actionId: string, tweenId: string): any;

declare function physics(props: Record<string, unknown> | null): any;

// ---- Variables -------------------------------------------------------------

/**
 * @param value a number, string, or boolean
 */
declare function setVariable(name: string, value: number | string | boolean): any;

/**
 * @param type 'counter' | 'random' | 'time' | 'timer' | 'stopwatch'
 * @param props a plain object of properties
 */
declare function dynamicVariable(name: string, type: "counter" | "random" | "time" | "timer" | "stopwatch", props?: Record<string, unknown>): any;

/**
 * @param nameOrId a variable's name or id
 */
declare function removeVariable(nameOrId: string): any;

/**
 * @param nameOrId a variable's name or id
 */
declare function renameVariable(nameOrId: string, name: string): any;

/**
 * @param property a bindable property — 'position.x/y/z', 'rotation.x/y/z', 'scale.x/y/z', 'width', 'height', 'depth', or 'text'
 * @param variable a variable's name or id
 */
declare function bindVariable(property: string, variable: string): any;

/**
 * @param property a bindable property — 'position.x/y/z', 'rotation.x/y/z', 'scale.x/y/z', 'width', 'height', 'depth', or 'text'
 */
declare function unbindVariable(property: string): any;

// ---- Cameras, view and play mode -------------------------------------------

declare function viewport(props: string | Record<string, unknown>): any;

declare function camera(props?: string | Record<string, unknown>): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function focus(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param target a target — an object from select/add/mesh, an array of them, 'all', or a count
 */
declare function zoom(target?: {
  id: string;
} | Array<{
  id: string;
}> | string | number | ((object: any) => unknown)): any;

/**
 * @param spec a vantage preset ('front'|'back'|'left'|'right'|'top'|'bottom'|'iso'|'threeQuarter') or { azimuth?, elevation?, distance?, target? } (degrees; target is [x,y,z] or 'selection')
 */
declare function lookFrom(spec: string | {
  azimuth?: number;
  elevation?: number;
  distance?: number;
  target?: [number, number, number] | "selection";
}): any;

/**
 * @param cameraRef a camera object (from add('PerspectiveCamera')), a camera id/name, or 'personal'
 */
declare function activateCamera(cameraRef?: {
  id: string;
} | string): any;

/**
 * @param cameraRef a camera object (from add('PerspectiveCamera')), a camera id/name, or 'personal'
 */
declare function setPlayCamera(cameraRef?: {
  id: string;
} | string): any;

/**
 * @param mode 'none' | 'orbit' | { rotate?, pan?, zoom?, autoRotate? } — play-mode camera controls
 */
declare function playControls(mode: "none" | "orbit" | {
  rotate?: boolean;
  pan?: boolean;
  zoom?: boolean;
  autoRotate?: boolean;
}): any;

declare function play(): any;

declare function stop(): any;

// ---- Read without changing anything ----------------------------------------

/**
 * @param target an object id or name, or an object from select/add/mesh (omit to read the single selected mesh)
 * @param options getGeometry options — { space?: 'local' (default) | 'world', start?: int (first vertex of the window), count?: int (window size in vertices; 0 = counts + bounds only, no arrays), channels?: ('vertices'|'indices'|'normals'|'uvs')[] }
 */
declare function getGeometry(target?: {
  id: string;
} | string, options?: {
  space?: "local" | "world";
  /** range at least 0 */
  start?: number;
  /** range at least 0 */
  count?: number;
  channels?: Array<"vertices" | "indices" | "normals" | "uvs">;
}): any;

declare function listMaterials(): any;

/**
 * @param nameOrId a material asset's name or id, e.g. 'Brushed Gold'
 */
declare function getMaterial(nameOrId: string): any;

/**
 * @param value any JSON-serializable value your script computed — a string, number, array or plain object
 */
declare function report(value: unknown): any;

// ---- Script helpers --------------------------------------------------------

declare function get(what: 'selection'): any[];

declare function rand(): number;

/** Euler rotation in degrees that aims a camera at yaw/pitch (degrees). */
declare function aimEuler(yawDeg: number, pitchDeg: number): { x: number; y: number; z: number };

// ---- Other names for the functions above ----------------------------------

declare const rotate: typeof rotation;
declare const ms: typeof mesh;
declare const ge: typeof geometry;
declare const cr: typeof path;
declare const det: typeof detachInstance;
declare const addLight: typeof light;
declare const particle: typeof particles;
declare const context: typeof select;
declare const centerView: typeof focus;
declare const view: typeof lookFrom;
declare const orbit: typeof lookFrom;
declare const useCamera: typeof activateCamera;
