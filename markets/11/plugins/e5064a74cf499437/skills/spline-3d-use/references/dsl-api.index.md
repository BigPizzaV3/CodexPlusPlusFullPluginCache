# Spline DSL API Index

> Full typings: `dsl-api.d.ts` (1,488 lines)
> Grep by function name to jump to its definition. All `L#` line numbers refer to that file.

---

## Create objects

| Function | Defined |
| --- | --- |
| `add(objectType, geometryType?, parameters?)` | L11 |
| `mesh(geometryType, parameters?)` | L16 |
| `customMesh(params)` | L21 |
| `object(name)` | L28 |
| `light(type, props?)` | L33 |
| `path(points?)` | L74 |
| `particles(typeOrProps?, props?)` | L80 |
| `hair(typeOrProps?, props?)` | L202 |
| `clone(props)` | L385 |
| `cloneTo(target, props)` | L391 |
| `duplicate(target?)` | L398 |
| `component(target?)` | L407 |
| `instance(target?)` | L416 |
| `detachInstance()` | L422 |

## Generate procedural content

| Function | Defined |
| --- | --- |
| `terrain(params?)` | L429 |
| `ocean(params?)` | L456 |
| `globe(params?)` | L479 |
| `building(params?)` | L500 |
| `tree(params?)` | L525 |
| `rock(params?)` | L546 |
| `scatter(params)` | L566 |
| `layout(params)` | L590 |

## Select objects

| Function | Defined |
| --- | --- |
| `select(targetOrFilter, count?, mode?)` | L632 |
| `unselect(targetOrFilter?, count?)` | L638 |
| `iterate(callback)` | L647 |

## Transform, arrange and organize

| Function | Defined |
| --- | --- |
| `position(p)` | L654 |
| `translate(p)` | L663 |
| `rotation(r)` | L672 |
| `scale(s)` | L681 |
| `align(path, props?)` | L690 |
| `arrange(margins?, target?)` | L700 |
| `group(target?, groupId?)` | L710 |
| `ungroup(target?)` | L719 |
| `moveInto(parent, target?, options?)` | L730 |
| `rename(value)` | L745 |
| `hide(target?)` | L750 |
| `show(target?)` | L759 |
| `visibility(changes)` | L768 |
| `remove(target?)` | L779 |

## Edit geometry

| Function | Defined |
| --- | --- |
| `geometry(changes)` | L790 |
| `boolean(operation, target?, booleanId?)` | L797 |
| `union(target?, booleanId?)` | L807 |
| `subtract(target?, booleanId?)` | L817 |
| `intersect(target?, booleanId?)` | L827 |
| `bakeBoolean(target?)` | L836 |
| `merge(target?)` | L845 |
| `decimate(target, ratio, options?)` | L856 |
| `shapeBlend(targetOrProps?, blendId?)` | L871 |

## Color and materials

| Function | Defined |
| --- | --- |
| `color(value)` | L890 |
| `opacity(alpha)` | L899 |
| `material(m)` | L904 |
| `createMaterial(name, props?)` | L912 |
| `applyMaterial(nameOrId)` | L924 |
| `updateMaterial(nameOrId, props)` | L930 |
| `deleteMaterial(nameOrId)` | L942 |
| `layer(type, props?)` | L947 |
| `addLayer(type, props?, id?)` | L953 |
| `updateLayer(layerId, props)` | L959 |
| `removeLayer(idOrType)` | L964 |
| `generateTexture(name, draw, size?)` | L971 |
| `shading(props)` | L976 |
| `shadows(props)` | L987 |
| `style(palette, seed?)` | L997 |
| `prettify()` | L1003 |

## Lighting, environment and effects

| Function | Defined |
| --- | --- |
| `updateLight(props)` | L1010 |
| `background(value)` | L1033 |
| `fog(props?)` | L1039 |
| `sky(props?)` | L1060 |
| `environment(props)` | L1095 |
| `studio(target?)` | L1175 |
| `stage(mode, target?)` | L1185 |
| `fx(type, props?)` | L1191 |

## States, events and animation

| Function | Defined |
| --- | --- |
| `animate(stateProps, transitionProps?)` | L1199 |
| `addState(name?)` | L1245 |
| `removeState(state)` | L1247 |
| `renameState(state, name)` | L1249 |
| `selectState(state)` | L1251 |
| `addEvent(type?, eventId?)` | L1257 |
| `updateEvent(eventId, props)` | L1263 |
| `removeEvent(eventId)` | L1268 |
| `addAction(eventId, eventTypeOrActionType, actionTypeOrContainer?, container?, actionId?, initialTweenId?, tweenId?)` | L1276 |
| `updateAction(eventId, actionId, props)` | L1283 |
| `removeAction(eventId, actionId)` | L1289 |
| `addTween(eventId, actionId, props?, tweenId?)` | L1297 |
| `updateTween(eventId, actionId, tweenId, props)` | L1317 |
| `removeTween(eventId, actionId, tweenId)` | L1336 |
| `physics(props)` | L1338 |

## Variables

| Function | Defined |
| --- | --- |
| `setVariable(name, value)` | L1345 |
| `dynamicVariable(name, type, props?)` | L1351 |
| `removeVariable(nameOrId)` | L1356 |
| `renameVariable(nameOrId, name)` | L1361 |
| `bindVariable(property, variable)` | L1367 |
| `unbindVariable(property)` | L1372 |

## Cameras, view and play mode

| Function | Defined |
| --- | --- |
| `viewport(props)` | L1376 |
| `camera(props?)` | L1378 |
| `focus(target?)` | L1383 |
| `zoom(target?)` | L1392 |
| `lookFrom(spec)` | L1401 |
| `activateCamera(cameraRef?)` | L1411 |
| `setPlayCamera(cameraRef?)` | L1418 |
| `playControls(mode)` | L1425 |
| `play()` | L1432 |
| `stop()` | L1434 |

## Read without changing anything

| Function | Defined |
| --- | --- |
| `getGeometry(target?, options?)` | L1442 |
| `listMaterials()` | L1453 |
| `getMaterial(nameOrId)` | L1458 |
| `report(value)` | L1463 |

## Script helpers

| Function | Defined |
| --- | --- |
| `get('selection')` | L1467 |
| `rand()` | L1469 |
| `aimEuler(yawDeg, pitchDeg)` | L1472 |

## Other names

| Name | Same as | Defined |
| --- | --- | --- |
| `rotate` | `rotation` | L1476 |
| `ms` | `mesh` | L1477 |
| `ge` | `geometry` | L1478 |
| `cr` | `path` | L1479 |
| `det` | `detachInstance` | L1480 |
| `addLight` | `light` | L1481 |
| `particle` | `particles` | L1482 |
| `context` | `select` | L1483 |
| `centerView` | `focus` | L1484 |
| `view` | `lookFrom` | L1485 |
| `orbit` | `lookFrom` | L1486 |
| `useCamera` | `activateCamera` | L1487 |
