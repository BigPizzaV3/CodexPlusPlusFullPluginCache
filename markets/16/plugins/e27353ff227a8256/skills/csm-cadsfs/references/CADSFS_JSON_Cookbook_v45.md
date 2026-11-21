# CADSFS CSM Cookbook v45

> **Novedades v45 (R441):** un control room completo, con el texto para el
> usuario y el JSON (§52.5), y lo que esta guía decía distinto.
>
> - **§52.5 · El ejemplo.** 5,7 × 4,2 × 3,0 m, 24 objetos. Todo sale de la
>   receta de §52.2 y está probado en CADSFS: se aplica sin correcciones ni
>   avisos. Tm de 0,22 s por Sabine, con un nominal de EBU de 0,21 s; el
>   trazado de rayos da T30 0,29 s. Muestra el informe que se espera:
>   - la sala;
>   - el RT, objetivo y estimado;
>   - el tratamiento, con sus cuentas;
>   - los monitores;
>   - el aislamiento;
>   - lo que no se cumple.
> - **Con el tratamiento en objetos, el recinto va reflectante** (§2, §25,
>   §29.1, §52.5). Las superficies de la tabla de §2 más los objetos de un
>   diseño completo dan una sala muerta: Tm de 0,17 s por Sabine y 0,13 s
>   por Eyring.
> - **El techo acústico de los estudios.** La placa de 20 mm (σ≈8k) +
>   plenum 200 mm tiene la absorción en serrucho de un tercio al siguiente.
>   En los estudios va la de 18 mm (σ≈15k) + plenum 200 mm, que es pareja
>   (§2).
> - **§52.2:** dónde va la fuente de un control room (en el monitor
>   izquierdo) y dónde va el material de un objeto (en todo el objeto, o en
>   la cara que mira a la sala).
> - **Correcciones:**
>   - Los monitores de §12 van con `mount: "monitor"` y
>     `channel: "stereo"`. Decía `"flying"`: al editarlos se abría el
>     asistente de line array.
>   - La ventana de control es una abertura también en A13 y en §26.2.
>     Decían «objeto».
>   - En un estudio, la pared del frente va absorbente detrás de monitores
>     en pie, y reflectante sólo si van empotrados (§26.3). Decía
>     «reflectante o flush-mount».

> **Novedades v44 (R438):** lo que salió de «hazme un control room de 3x4x3»
> (26/09/2026): la IA hizo una sala de 5 × 4,2 × 3 con paredes inclinadas,
> copiando el ejemplo de control room y la regla del volumen mínimo, y el
> programa no corrigió nada porque la planta no era un rectángulo.
>
> - **Las medidas del usuario no se cambian (§52.1).** Si el pedido trae
>   las medidas del recinto, el recinto mide eso: rectangular, salvo que se
>   pida otra forma. Una recomendación que no se cumple (volumen mínimo,
>   Bolt, splay) se comenta en el texto. El asistente interno le agrega al
>   pedido una nota con las medidas y, si la IA igual no las respeta, lleva
>   el recinto a esas medidas y reacomoda lo de adentro.
> - **El control room, con fórmulas (§52.2 y §52.3):** el oyente al 38 %,
>   el triángulo equilátero, la mesa de frente delante del oyente, los
>   paneles en los puntos de primera reflexión, la nube, las trampas
>   tocando las dos paredes, el difusor, la simetría. Un ejemplo resuelto.
> - **El corrector de geometría mira cualquier planta (§0.5, §42, §52.4):**
>   paredes inclinadas, L, herradura; objetos girados en Z; paneles de canto
>   o separados de una pared oblicua; muebles de pared; trampas a la
>   esquina; muebles metidos en paneles; parlantes, fuente o receptor afuera
>   o adentro de un objeto macizo; el material puesto en una cara que no se
>   ve. En un estudio, además: el triángulo, el apuntado de los monitores, la
>   mesa y las primeras reflexiones. Lo que es diseño, se avisa.
> - **`rotation_deg` se respeta (§0.5).** Hasta la R437 el asistente
>   interno y `/api/design` lo tiraban: el objeto quedaba derecho.
> - **Los ejemplos de estudio corregidos:** el receptor de ejemplo
>   ([1,0 0 1,2], al 70 % de su sala) y los monitores que no apuntaban al
>   oyente (§8, §12, §18 del prompt); la pared con la ventana, que no es de
>   vidrio (§12, §28.7, §29.1).

> **Novedades v43 (R437):** lo que cambia para la IA interna y para un agente.
>
> - **Hacé lo que se pide (§26).** Un pedido sólo geométrico («una sala de
>   8×8×3», «un recinto de 10×6×4») se entrega tal cual: el recinto, un
>   material real en cada superficie y la fuente y el receptor, sin
>   tratamiento, muebles ni parlantes que no se pidieron; al final se ofrece
>   en una línea lo que se agregaría. El máximo detalle es para cuando el
>   pedido dice el uso o el tipo («diseñame un control room», «un teatro
>   para 600») o pide el tratamiento. Hasta la v42 decía «SIEMPRE MÁXIMO».
> - **Dónde va el centro de un panel (§0.5).** Las fórmulas para apoyar un
>   panel contra cada pared, una nube en el techo y una trampa en una
>   esquina, con un ejemplo resuelto.
> - **El programa respeta el formato de esta cookbook.** Hasta la R436, el
>   convertidor del asistente interno y de `/api/design` perdía
>   `surface_group_material` (y la cara B, el espesor, el aspecto y las
>   claves de los assemblies), `source_pos` y `receiver_pos` (la fuente y el
>   receptor quedaban juntos en [0, 0, 1.2]), los `beam_arrays`, las
>   `audience_zones`, el RT medido, la `c_m_s`, el nivel y la directividad
>   de la fuente. Ahora llegan. Cómo se escriben las claves de superficie:
>   §4.
> - **Objetos que atraviesan el recinto (§0.5, §42).** En un recinto
>   rectangular alineado con los ejes, un objeto `box` sin rotación que
>   atraviesa una pared, el piso o el techo se acomoda y se informa en
>   `corrections` (`method: "geometria"`); con `strict` o sin `autofix`,
>   sólo se avisa, con la `suggestion`.
> - **JSON completo = sala nueva (§51).** Para modificar, comandos. Si el
>   JSON completo trae otra sala (otro recinto), reemplaza al proyecto; si
>   trae la misma, se conserva lo que no mande, un objeto renombrado se
>   reconoce por su lugar y los materiales que manda para un objeto ganan.

> **Novedades v42 (R430):** lo que cambia en los resultados para el mismo JSON.
>
> - **`c_m_s` fija la constante de Sabine** en todo el programa: `K = 24·ln(10)/c`,
>   0,161114 s/m con 343 m/s (hasta R429 era 0,161 redondeado y todos los RT salían
>   un 0,07 % cortos). La usan el RT60, la distancia crítica, la calibración de
>   materiales y las normas; los optimizadores, la exacta con 343 m/s.
> - **El público de `audience_zones` absorbe en todos los tercios.** Su absorción
>   viene por octava (63 Hz–8 kHz) y cada tercio toma la de su octava (31 y 40 Hz la
>   de 63; 12,5 kHz la de 8 kHz). Hasta R429 sólo la recibían los tercios centrales
>   de octava y el RT tenía un serrucho (800 y 1250 Hz sin público, 1000 con él).
>   El Millington-Sette también la suma.
> - **Cajas juntas: acoplamiento mutuo.** Dos cajas a menos de media longitud de
>   onda que emiten la misma señal no suman potencias: el reverberante del mapa, del
>   análisis del sistema, de la IR y del Walker lo tiene en cuenta, con los
>   retardos y la `polarity` de cada una. Dos subgraves a 0,6 m en fase: +2,8 dB de
>   potencia en 63 Hz sobre la suma; un par cardioide: −3,9 dB en 63 Hz. Con cajas
>   separadas no cambia nada.
> - **`polarity: -1`** entra también en el reverberante, en las reflexiones de la
>   pestaña Reflexiones que usa la IR y en la cola del Walker.
> - **`air_temp_C` y `air_humid_pct`:** 0 °C y 0 % son valores. Hasta R429 el RT60,
>   el ISM, el campo del sistema, el trazado de rayos, los conos y sus conversiones
>   los tomaban como 20 °C y 50 %.
> - **`channel` en el Walker:** con un archivo multicanal, cada caja suena con el
>   canal del archivo que lleva su código, sin distinguir mayúsculas (ver §«Campos
>   clave por elemento»); hasta R429 las de surround y de altura recibían la mezcla.
> - **El T por banda de las tablas de métricas** (ISM, trazado de rayos, conos) ya
>   no suma el aire dos veces: en 8 kHz salía hasta un 41 % corto.
> - **La IR del trazado de rayos** en el diálogo de medición: métricas desde la
>   llegada del directo, con su energía y con las columnas de la tabla (hasta R429
>   la tabla salía casi vacía, el T60 de banda ancha a la mitad y el diálogo se
>   cortaba al dibujar la fase).

> **Novedades v41 (distancia crítica, R429):** el programa calcula la distancia
> crítica con una sola definición en todos sus paneles ---Hopkins–Stryker,
> `d_c = √(Q·R / 16π)` con `R = A / [(1−ᾱ)·e^(−4mV/S)]`, el aire incluido---.
> Muestra la de la sala (fuente omnidireccional, Q = 1) y, cuando hay sistema, la
> del sistema hacia el receptor: la Q del conjunto de cajas en esa dirección, con
> el directo sumado en fase como en el mapa, junto al D/R en el receptor. El RT
> medido (`measured_rt60_s`) vale para todos los paneles de distancia crítica.
> Se corrige §F2.

> **Novedades v40 (arrays y refuerzo):** se agregan las dos
> frecuencias que limitan un array de haz ---control y aliasing--- con
> su geometría, y se nivela lo que sabe la IA interna con lo que ya
> traía este documento sobre refuerzo sonoro.
>
> **Novedades v29 (el agente hace el trabajo completo):** se agregan
> las bibliotecas de aislantes y altavoces, el asistente de array y
> el apuntado que respeta el herraje. Con eso un agente puede
> dibujar la sala, tratarla, aislarla, diseñar el sistema y
> verificar contra norma sin intervención.
>
> **Novedades v28 (arrays de haz controlado):** se agrega
> **`beam_arrays`**, la clave que describe columnas orientables,
> matrices, arcos, cilindros y casquetes esféricos sin escribir los
> transductores uno por uno: la app los genera con sus retardos.
> Incluye **módulos matriciales** (§36.7), que es lo que hay que usar
> en instalaciones grandes para que la banda declarada no sea falsa.
> Se documentan además los **grupos de superficie** (§37) y las
> **zonas de audiencia** (§38).
>
> ## ⛔ ANTES DE ESCRIBIR ALTAVOCES
>
> Si el recinto es reverberante, es una iglesia, una nave, un domo
> o una sala esférica, o si se nombran columnas orientables, beam
> steering o la Sphere: **NO escribas los altavoces uno por uno.**
> Usá `beam_arrays` (§36) y la app genera los transductores con sus
> retardos.
>
> Trescientos altavoces con `delay_ms` en cero no son un array: son
> trescientas cajas sueltas. **Sin retardos no hay haz.**
>
> **ÍNDICE RÁPIDO — leé la sección que corresponde antes de escribir
> el JSON:**
> §0 ejes · §1 estructura · §2 materiales · §3 geometría ·
> §4 superficies · §5 assemblies · §6 sistemas de altavoces ·
> §9 checklist · §10 errores comunes · §12 estudios ·
> §14 audiencia · §16 exterior · §18 surround · §21 directrices ·
> §24 salas famosas · §28 aberturas ·
> **§36 arrays de haz** · **§37 grupos de superficie** ·
> **§38 zonas de audiencia**

> **Novedades v26 (corrección física de subs):** se **corrige el arreglo end-fire** del §6 (Preset D), que en v25 tenía la **rampa de delay invertida** y disparaba hacia el **escenario** en vez de hacia la audiencia (F/B −14.4 dB → +14.4 dB a 63 Hz tras el arreglo). Se **corrige el delay del cardioide** (Preset C): usaba 5.8 ms para un offset real de 0.72 m, cuando corresponde **2.1 ms** (el valor viejo hasta **invertía** el lóbulo por encima de 80 Hz). Se documentan los presets **Cardioide 3+1** y **Cardioide 2+1 (cancelación trasera)** (renombrados, sin marca), el patrón de fuente **Dodecaédrico (ISO 3382)** (`source_polar_pattern`) y el campo **`measured_rt60_s`** (override de RT medido para la distancia crítica). Todo aditivo salvo los delays corregidos. Ver §6 y §17.

> **Novedades v25:** el aislamiento se calcula con el **motor TMM validado** (80 construcciones medidas en laboratorio): matriz de transferencia con Delany-Bazley, puentes estructurales y cotas físicas. Se agregan **53 materiales validados**, el cálculo de **impacto (Ln,w/IIC/L'nT,w)** y **lluvia**, y descriptores in situ. Todo aditivo: los IDs y campos previos siguen válidos. Ver §5b.

> Basado en: `TEATRO_PARA_ENTRENAMIENTO.csm` (funcionando al 100%).
> Software: CADSFS V1.06 (CANA SAN MARTIN Audio Tools 2026).
> **Formato de archivo:** `.csm` (CANA San Martín). El contenido es JSON estándar;
> solo cambia la extensión para identificar proyectos CADSFS.
> Los archivos `.json` legacy se pueden abrir con Archivo → Abrir.
> **v24**: Orientación de subs corregida (apuntan al mismo lado que el PA).
> **v40**: `yaw_deg` corregido. La v24 fijó el valor equivocado: `0° = +X`, no `90°`. Nueva sección de recintos grandes y RT60 (evita reverb absurda en graves de arenas). Validación de enclosure watertight para análisis modal. Lecciones del caso Gran Canaria Arena.
> **v23**: Conteo de materiales corregido a **2665** (era 2678, dato verificado contra el blob real).
> Campo `project_designer` documentado para el watermark dinámico ("CADSFS — <diseñador>").
> **v22**: Verificación normativa 60 normas/21 países (§31), biblioteca constructiva 29 sistemas (§32),
> Modo Arquitecto wizard (§33), herramientas CAD completas (§34), Bolt/Louden/Bonello,
> plugin SketchUp (.CSM), DXF import con layers, eyedropper materiales, capas/grupos.
> **v20**: Materiales obligatorios por tipo de recinto (§2), nombres corregidos en aberturas (§28),
> aberturas en techo/piso (§28.6), validación RT60 flat = material Default (§9),
> ejemplos completos de surface_group_material por tipo (§29), auto-checklist de la IA (§30).
> **v19**: 90+ directrices acústicas de diseño (§21-§25), fórmulas heurísticas (§22),
> interpretación de imágenes (§23), copia de salas famosas (§24), inferencia automática (§25),
> nivel de detalle máximo obligatorio (§26), inferencia avanzada para copiar/recrear (§27).

---

## 0. Convención de ejes — LEER PRIMERO

```
              Z (altura)
              ↑
              |   Y (ancho / lateral)
              |  /
              | /
   -X ←——————(0,0,0)——————→ +X (profundidad)
  escenario              audiencia
```

| Eje | Significado | Ejemplo: teatro 20×12×8 m |
|-----|------------|---------------------------|
| **X** | **Profundidad** (largo). Escenario en −X, audiencia en +X | −10 a +10 |
| **Y** | **Ancho** (lateral). Y=0 es el **eje de simetría** de la sala | −6 a +6 |
| **Z** | **Altura**. Z=0 = piso, Z=alto = techo | 0 a 8 |

### Regla de centrado (CRÍTICA)

El **centro geométrico** de la sala (enclosure) va en **X=0, Y=0**. Z=0 es el piso.

Para un recinto de profundidad D, ancho W, alto H:
- X va de **−D/2** a **+D/2**
- Y va de **−W/2** a **+W/2**
- Z va de **0** a **H**

Esto se logra con `make_box(cx=0, cy=0, z_floor=0, w=D, d=W, h=H)`.

### Reglas derivadas

- `size_xyz = [X, Y, Z]` = **[profundidad, ancho, alto]** — NUNCA al revés.
  Para paneles contra una pared el vector cambia según la pared: ver §0.5.
- **Y=0** es el **eje de simetría lateral** de la sala (mejor visual 3D, simetría natural L/R).
- **Escenario** está en **X negativo** (−X), **audiencia** en **X positivo** (+X).
- **Orientación de parlantes (`yaw_deg`):** `0° = +X`, `90° = +Y`,
  `180° = −X`, `−90° = −Y`. Como la audiencia está en **+X**, un PA que
  cubre la platea lleva **`yaw_deg: 0`**.

  > ⚠ **Corregido en la v40.** Hasta la v40 esta línea decía lo
  > contrario ---que `yaw_deg: 90` apuntaba a la audiencia--- y lo
  > llamaba «convención verificada». Era falso, y contradecía a la
  > propia §7.2 de este documento, que siempre dijo `0° = +X`.
  >
  > Todos los ejemplos de sistemas de sonido anteriores a la v40
  > llevaban `yaw_deg: 90`. **Si tenés un `.csm` hecho con una versión
  > anterior, revisá el yaw: es probable que todo el sistema apunte a
  > la pared lateral.**
  - **Regla de oro: los subs apuntan al MISMO lado que el PA.** Sea cual sea el `yaw` del PA en tu sala, los subs llevan el mismo, sin ángulo lateral. No es un valor fijo: es **el yaw que calculaste para el PA**.
- **`source_pos`** va en la zona de escenario: `[−D×0.35, 0, 1.5]` (X negativo, centrado en Y).
- **`receiver_pos`** va en la zona de audiencia: `[+D×0.15, 0, 1.2]` (X positivo, centrado en Y).
  En un **estudio o control room**, el punto de escucha va al 38 % de la
  profundidad desde el frente: `[−D/2 + 0.38×D, 0, 1.2]` (§52).
- **Extrusiones** (`polygon_xy`): centradas en (0,0). X = profundidad, Y = ancho. CCW visto desde arriba.

> ⚠ **Error frecuente 1**: invertir ancho y profundidad en `size_xyz` hace que la sala quede rotada 90° y los parlantes apunten a una pared lateral.

> ⚠ **Error frecuente 2**: poner el recinto partiendo de (0,0,0) en vez de centrado. Esto desplaza el eje de simetría Y y rompe la visual 3D.

---

---

## 0.5 Antes de escribir un solo objeto

Esta sección está antes que todo lo demás porque el error más caro de
este formato no se comete escribiendo un objeto: se comete **antes**,
al decidir dónde va el escenario.

### El fallo que motivó esta sección

Una IA construyó un teatro completo ---veinticuatro objetos, seis
sistemas de sonido, doce zonas de audiencia--- girado noventa grados
respecto de la convención. La sala era coherente consigo misma. Pero
después aplicó las recetas de este documento al pie de la letra, y
esas recetas están escritas para la convención.

El resultado: dieciséis de veintitrés objetos fuera del recinto, los
subgraves apuntando a la pared lateral y el sistema principal
disparando al techo.

**Ninguna de las dos mitades era absurda. El problema fue mezclarlas.**

---

### Comprobación obligatoria · el trazado

Antes de escribir el primer objeto, respondé estas tres y anotá el
resultado:

```
1. ¿En qué eje está el escenario?          debe ser X NEGATIVO
2. ¿En qué eje está la audiencia?          debe ser X POSITIVO
3. ¿Cuál es el eje de simetría lateral?    debe ser Y = 0
```

**Si tu sala no cumple las tres, no sigas.** Reorientá el trazado
entero antes de escribir nada: permutá X por Y en cada cota, en cada
polígono y en cada posición.

No es una preferencia de estilo. Todas las recetas de este documento
---los tamaños de panel, la orientación de los subgraves, los valores
de `yaw`--- están atadas a esa convención. Usarlas en una sala girada
produce un archivo que el programa acepta y calcula mal.

#### La comprobación numérica

Una sala rectangular de profundidad **D** y ancho **W**:

```
enclosure   X de −D/2 a +D/2        ← la dimensión MAYOR suele ir en X
            Y de −W/2 a +W/2
            Z de 0 a H

escenario   centro en X ≈ −D×0.35   ← X NEGATIVO
audiencia   centro en X ≈ +D×0.15   ← X POSITIVO
```

**Si el número mayor te quedó en Y, está girada.**

---

### Cómo orientar un objeto: `rotation_deg`

Todo objeto tiene `rotation_deg = [roll_X, pitch_Y, yaw_Z]` en grados.
Vale cero por omisión, y en la mayoría de los casos **debe quedar en
cero**: es preferible dar el tamaño correcto que rotar una caja.

```json
"rotation_deg": [0.0, 0.0, 0.0]
```

El giro es alrededor del **centro** del objeto; `yaw_Z` positivo es
antihorario visto desde arriba (+X hacia +Y). Hasta la R437 el asistente
interno y `/api/design` **tiraban** el `rotation_deg` de los objetos: un
objeto girado quedaba derecho. Desde la R438 se respeta (en los `box`; una
extrusión ya trae su forma en el polígono). El corrector del programa usa el
giro en Z para poner un panel paralelo a una pared inclinada.

**Para un panel plano contra una pared, no uses rotación: usá el
tamaño que corresponde a esa pared.** La tabla siguiente lo resuelve
sin girar nada.

---

### Los paneles: el tamaño depende de la pared

Un panel tiene que ser **delgado en el eje normal a la pared que lo
sostiene**. Ese eje cambia según la pared, así que **no existe un
`size_xyz` de panel**: existe uno por pared.

| Dónde va | Normal | `size_xyz` | Ejemplo 5 × 2,8 m, 18 cm |
|---|---|---|---|
| Pared del fondo o del frente | X | `[espesor, ancho, alto]` | `[0.18, 5.0, 2.8]` |
| Pared lateral | Y | `[largo, espesor, alto]` | `[5.0, 0.18, 2.8]` |
| Techo o nube | Z | `[largo, ancho, espesor]` | `[5.0, 2.8, 0.18]` |

> ⚠ **El mismo panel de cinco metros tiene tres vectores distintos
> según dónde se cuelgue.** Copiar el vector de una pared a otra es el
> error que sacó dieciséis objetos fuera del recinto en el caso que
> motivó esta sección.

#### Dónde va el centro

`center` es el **centro** del objeto. Para que un panel quede apoyado,
su cara de atrás tiene que coincidir con la pared: el centro va a medio
espesor de la pared, hacia adentro. Recinto de profundidad **D** (X),
ancho **W** (Y) y alto **H** (Z), centrado como pide §0:

| Dónde va | `size_xyz` / `dimensions` | centro |
|---|---|---|
| Pared izquierda (−Y) | `[largo, e, alto]` | `[x, −W/2 + e/2, z]` |
| Pared derecha (+Y) | `[largo, e, alto]` | `[x, +W/2 − e/2, z]` |
| Pared del frente (−X) | `[e, ancho, alto]` | `[−D/2 + e/2, y, z]` |
| Pared del fondo (+X) | `[e, ancho, alto]` | `[+D/2 − e/2, y, z]` |
| Techo | `[largo, ancho, e]` | `[x, y, H − e/2]` (más abajo si cuelga) |
| Piso (una tarima) | `[largo, ancho, e]` | `[x, y, e/2]` |
| Trampa de lado a y alto h, esquina (+X, +Y) | `[a, a, h]` | `[D/2 − a/2, W/2 − a/2, h/2]` |

Las otras esquinas, cambiando los signos. Izquierda y derecha son las
del que mira al escenario (−X), como en el prompt del asistente: la
izquierda es −Y.

**Ejemplo resuelto.** Sala de 8 × 8 × 3 m (X de −4 a 4, Y de −4 a 4, Z
de 0 a 3) y un panel de 1,8 m de largo, 1,5 m de alto y 0,18 m de
espesor en la pared izquierda, centrado en X y a 1,35 m de altura:

```json
{"name": "Panel absorción pared izquierda", "kind": "box",
 "dimensions": [1.8, 0.18, 1.5], "center": [0.0, -3.91, 1.35]}
```

`−W/2 + e/2 = −4 + 0,09 = −3,91`. Va de y = −4,00 (la pared) a
y = −3,82. **No** `[0.18, 1.8, 1.5]`: ése es el vector de la pared del
fondo, y en la lateral queda de canto y la atraviesa. Es exactamente el
error del caso que dio origen a la v43 (el centro, además, a 0,2 m de la
pared: el panel salía 0,7 m afuera).

Una trampa de 0,4 × 0,4 × 1,6 m en la esquina (+X, +Y) de la misma sala:
`"dimensions": [0.4, 0.4, 1.6], "center": [3.8, 3.8, 0.8]`. En
[3.6, 3.6, 0.8] queda a 0,2 m de las dos paredes: no está en la esquina.

#### La comprobación

Para cada panel, antes de escribirlo:

```
el valor más chico de size_xyz debe estar
en la MISMA posición que el eje normal de su pared

pared lateral  → normal Y → el más chico va SEGUNDO
pared de fondo → normal X → el más chico va PRIMERO
techo          → normal Z → el más chico va TERCERO
```

---

### Los parlantes: calcular, no copiar

Los valores de `yaw_deg` y `pitch_deg` que aparecen en los ejemplos de
este documento **son de los ejemplos**. No son constantes del formato.

#### `pitch_deg`: positivo es ABAJO

```
pitch = +30   apunta 30° hacia ABAJO    ← lo normal en un PA colgado
pitch =   0   horizontal
pitch = −30   apunta 30° hacia ARRIBA   ← al techo
```

Es la convención contraria a la intuición de mucha gente, y por eso se
equivoca tan seguido. **Un sistema principal colgado siempre tiene
pitch positivo.**

#### La curva J: las de abajo apuntan MÁS abajo

En un line array colgado, la caja superior cubre el fondo de la sala y
la inferior las primeras filas. Por eso:

```
caja de arriba   pitch pequeño     ej. +5°    casi horizontal
   ↓                  ↓
caja de abajo    pitch grande      ej. +45°   bien abajo
```

**El `pitch` crece hacia abajo del array.** Si tu caja inferior tiene
menos pitch que la superior, la curva está invertida y el array
dispara al techo.

#### Los subgraves: el mismo yaw que el PA

```
yaw de los subs = yaw del PA        ± 15° como mucho
```

No es `yaw = 0`. Es el yaw que tenga el PA en **tu** sala. Si el PA
mira a −90° porque así lo pide tu trazado, los subs también van a −90°.

#### La comprobación

```
1. ¿Todos los pitch del PA son POSITIVOS?
2. ¿El pitch crece de la caja de arriba a la de abajo?
3. ¿El yaw de los subs está a menos de 15° del yaw del PA?
4. Proyectá la caja superior: partiendo de su altura y su pitch,
   ¿a qué altura llega al fondo de la sala? Debe caer DENTRO
   de la audiencia, no por encima del techo.
```

La cuarta es una resta y atrapa el caso más caro:

```
altura_al_fondo = z_caja − D × tan(pitch)

si  altura_al_fondo > H     el array dispara al techo
si  altura_al_fondo < 0     el array dispara al piso
```

---

### Comprobación final antes de entregar

Seis cuentas. Ninguna necesita el programa.

```
[ ] si el usuario dio medidas, el recinto mide eso (§52.1)
[ ] el escenario está en X negativo
[ ] la dimensión mayor del recinto está en X
[ ] ningún objeto se sale del enclosure
      para cada objeto: min ≥ min_recinto y max ≤ max_recinto
[ ] cada panel tiene su valor más chico en el eje normal de su pared
[ ] todos los pitch del PA son positivos y crecen hacia abajo
[ ] el yaw de los subs está a menos de 15° del yaw del PA
```

**Si alguna falla, el archivo va a abrir igual y a calcular mal.**
El programa corrige una parte. Desde la R438, con **cualquier planta**
(rectangular, con paredes inclinadas, en L, en herradura) y con objetos
`box` girados sólo en Z:

- un **panel** (0,35 m de espesor o menos, y menos de la mitad de su
  medida siguiente) que atraviesa **de canto** una pared se gira y se
  apoya contra ella; uno **casi paralelo** (hasta 20°) que la atraviesa, o
  que quedó a 10 cm o menos sin ser paralelo (la pared es oblicua y el
  panel se escribió como si no lo fuera), se pone paralelo ---con giro,
  si la pared es oblicua--- y se apoya;
- de qué pared es un panel: primero, la que tiene paralela y casi toca;
  si el nombre dice cuál («trasero», «lateral izquierdo»), ésa. Un panel
  del fondo metido en una esquina se desliza por el fondo;
- un **mueble de pared** (sofá, biblioteca, difusor, panel grueso) que
  atraviesa una pared de punta se gira y se apoya de espaldas; si se mete
  en un panel de esa pared, se separa;
- una **trampa de graves** a 25 cm o menos de las dos paredes de una
  esquina va a la esquina;
- lo demás que atraviesa algo se corre lo mínimo, con las mismas medidas;
- un **panel o un mueble de pared que tapa una puerta o una ventana** de
  su pared se corre a lo largo de ella lo mínimo para dejarla libre, sin
  tapar otra ni meterse en otro objeto (una cortina, una persiana o el
  marco, no: la tapan a propósito);
- un **parlante**, la fuente o el receptor fuera del recinto se entran;
  uno adentro de un objeto macizo (un sub «debajo» de una mesa que es una
  caja desde el piso) sale al lugar libre más cercano del contorno de ese
  objeto; un parlante o la fuente, no del lado del oyente (entre el punto
  de escucha y la mesa, o a menos de 0,75 m de él) si hay otro lugar;
- el **material** puesto sólo en caras que no se ven (la de atrás de un
  panel, la de abajo de un mueble) pasa a las que miran a la sala;
- en un **estudio** (monitores L y R, menos de 400 m³): el triángulo, el
  apuntado de los monitores, la mesa y las primeras reflexiones (§52.4).

Lo informa en `corrections` (`method`: `"geometria"`, `"caras"`,
`"estudio"` o `"medidas"`), con el antes y el después y un `message`; el
asistente interno lo muestra en el chat y te lo devuelve en el pedido
siguiente. Lo que es una decisión de diseño no se toca y se avisa en
`warnings`: objetos que se meten uno en otro, un panel que tapa una
abertura y no tiene dónde correrse, un objeto delante de una puerta (a
menos de lo que barre su hoja: la mesa de un estudio, una trampa), un
triángulo estéreo lejos de 60°, un punto de escucha lejos del 38 %,
paredes laterales con materiales distintos, una ventana en un punto de
primera reflexión. Con `strict` o
sin `autofix` no toca nada: todo va a `warnings`, con la `suggestion`; lo
que habría corregido empieza con «Propuesta sin aplicar».

Un objeto **entero** afuera no se toca (se avisa): hay usos legítimos.
Tampoco se valida un PA apuntando al techo. **Lo demás de la lista sigue
siendo tuyo**, y un objeto corregido por el programa es un objeto que
escribiste mal.

---

---

## 0.6 Dónde apunta cada sistema, y cuánto se retarda

El apuntado **se calcula**. Los valores de `yaw_deg` y `pitch_deg` que
aparecen en los ejemplos son de esos ejemplos: valen para esa sala y
para ninguna otra.

Esta sección da las dos fórmulas y el criterio de cada sistema.

---

### La premisa, antes de las fórmulas

```
COLGADO    cubre hacia adelante y hacia ABAJO     pitch POSITIVO
APILADO    cubre hacia adelante y hacia ARRIBA    pitch NEGATIVO
```

No es una convención: es dónde está cada uno respecto del público.

Un array colgado está por encima de todas las cabezas, así que mira
hacia abajo. Un stack está **al nivel del público o por debajo** ---y
en una sala con pendiente, muy por debajo del fondo--- así que mira
hacia arriba.

> Si tu stack tiene pitch positivo en todas las cajas, está disparando
> al piso. Si tu colgado tiene pitch negativo, está disparando al
> techo. Son las dos comprobaciones más rápidas que existen.

#### La altura del oído NO es 1,10 m

Es **1,10 m sobre el piso de esa zona**, y el piso casi nunca está en
cero:

```
z_oído = z_piso_de_la_zona
       + (x − x_inicio_de_la_zona) × tan(pendiente)
       + 1,10
```

Tomar 1,10 absolutos es el error que invierte el signo de un stack
entero. En una platea con `z_m = 1,15` y 4° de pendiente, el oído del
fondo está a **3,72 m**: por encima de la caja más alta de un stack
sobre el escenario.

| zona | piso | oído |
|---|---|---|
| Platea baja | 1,15 → 2,62 | 2,25 → 3,72 |
| Palco | 5,90 → 7,63 | 7,00 → 8,73 |
| Pullman | 9,60 → 12,47 | 10,70 → 13,57 |
| Super Pullman | 13,20 → 15,26 | 14,30 → 16,36 |

En esa sala, **el Super Pullman está por encima del array colgado** a
11,40 m. Un array no puede cubrir una bandeja que le queda arriba: esa
bandeja lleva su propio sistema.

---

### Las dos fórmulas

Un parlante en `(xs, ys, zs)` que tiene que cubrir un punto
`(xt, yt, zt)`:

```
zt = z_piso_zona + (xt − x_inicio_zona) × tan(pendiente) + 1,10

Δx = xt − xs        Δy = yt − ys        Δz = zt − zs
d_horizontal = √(Δx² + Δy²)

yaw_deg   = atan2(Δy, Δx)   en grados
pitch_deg = atan2(−Δz, d_horizontal)   en grados
```

La primera línea es la que se olvida. Sin ella, un stack sobre un
escenario de un metro sale apuntando al piso.

El signo negativo en el pitch no es un descuido: **pitch positivo
apunta hacia abajo**, así que un objetivo más bajo que el parlante
---que es el caso normal--- da pitch positivo.

#### La comprobación al revés

Partiendo del ángulo, ¿dónde cae el eje?

```
alcance_horizontal = (zs − zt) / tan(pitch)
```

Con el PA colgado a 6 m, el oído a 1,1 m y pitch de 3°, el eje toca la
audiencia a **94 metros**. Si la sala mide treinta, esa caja no está
cubriendo a nadie: pasa por encima de todos y pega en la pared del
fondo.

---

### El sistema principal

**Dónde va.** Colgado en el proscenio, por delante del borde del
escenario, a los lados del hueco de boca. En X, apenas por delante del
escenario; en Y, separado del eje lo suficiente para que el ancho de
cobertura llegue a las butacas laterales.

**A dónde apunta cada caja.** No al centro de la platea: **cada caja
cubre una franja distinta.**

```
caja de ARRIBA  →  la ÚLTIMA fila        pitch pequeño
     ↓                    ↓
caja de ABAJO   →  la PRIMERA fila       pitch grande
                    que deba cubrir
```

La razón es geométrica: la última fila está lejos, así que se alcanza
casi en horizontal. La primera está abajo y cerca, así que hace falta
apuntar fuerte hacia abajo.

**La curva J sale sola de eso**: el pitch crece a medida que se baja
por el array. Si en tu archivo el pitch decrece hacia abajo, está al
revés.

#### El array se cuelga: la posición sale del ángulo

**No pongas las cajas y después calcules los ángulos.** En un colgado
real la posición de cada caja es una *consecuencia* del splay, no un
dato aparte. Ponerlas primero obliga a inventar un arco, y el arco
inventado nunca coincide con el que produce el rigging.

El orden correcto tiene tres pasos:

```
1. La caja de ARRIBA
   Su ángulo sale de la última fila, que es la que llega más lejos:
       pitch_0 = atan2(z_pasador − 1.1, x_lejos − x_pasador)
   Es la caja más plana del colgado.

2. El splay: NO es un dato, sale del reparto
   Repartí las distancias de forma logarítmica entre la última fila y
   la primera que el array deba cubrir, y sacá el ángulo de cada una:

       r = (d_cerca / d_lejos) ^ (1 / (N−1))
       d_i = d_lejos × r^i
       pitch_i = atan2(z_caja_i − 1.1, d_i − avance_i)

   El splay CRECE hacia abajo sin que haya que forzarlo, porque el
   ángulo es el arcotangente de una distancia que decrece
   geométricamente.

3. La posición, que sale sola
   Cada caja gira sobre el pasador DELANTERO de la de arriba, así que
   el frente avanza y baja:
       x += alto_caja × sin(pitch)
       z −= alto_caja × cos(pitch)
```

> ⚠ **No pongas una progresión fija de splay.** Una tabla del tipo «2°
> arriba, 10° abajo» anda con seis cajas y revienta con catorce:
> acumula 78° y la de abajo apunta al piso. **El splay depende de
> cuántas cajas haya**, porque el arco vertical a cubrir es el mismo y
> se reparte entre todas.
>
> | cajas | splay medio | pitch de la de abajo |
> |---|---|---|
> | 4 | 7,9° | 37,6° |
> | 8 | 3,3° | 37,2° |
> | 12 | 1,7° | 32,8° |
> | 16 | 0,8° | 26,6° |
>
> Misma sala, mismo arco. Con más cajas, cada una abre menos. Es lo
> que hace que un array de catorce sirva más que uno de seis: no cubre
> más, cubre con más resolución.

#### La forma que sale de ahí

Como el frente avanza en cada paso, **el extremo inferior del array
queda por delante del tope.** Visto desde el costado, el array parece
inclinarse hacia atrás, y así es como se ve un colgado real.

Para un array de seis cajas de 29 cm con splay de 2° a 10°, el extremo
inferior queda unos **75 cm por delante** del tope. Si en tu archivo
esa diferencia es de pocos centímetros, las posiciones no salieron del
splay: están puestas a mano.

> En un array **apilado sobre los subs** la cadena va al revés ---se
> arma de abajo hacia arriba--- y cada caja que se agrega retrocede.
> El resultado visto desde el costado es el mismo: el tope queda
> atrás.

#### Hasta dónde llega es un RESULTADO

Éste es el punto que más se equivoca. **El array no recibe la primera
fila como requisito.** Recibe la última, que fija el ángulo de la caja
de arriba, y una progresión de splay. Hasta dónde alcanza por abajo
sale de cuántas cajas hay y de cuánto se pueden abrir.

Si le exigís cubrir hasta un punto que su geometría no alcanza, la
única salida es forzar ángulos que ningún rigger puede armar. **Lo que
falta lo toman los front fills**, que para eso están.

```
calculá el array
mirá hasta dónde llega la caja de abajo:
    x_cerca = x_caja + (z_caja − 1.1) / tan(pitch)
los front fills cubren de la primera fila hasta ahí
```

#### Downfill: módulo más chico abajo

Un array puede llevar dos secciones: las cajas grandes arriba, para el
campo lejano, y un **downfill** de módulo más chico abajo, que cubre
las filas cercanas.

El downfill no es un capricho. Las cajas chicas **abren más splay**
---catorce grados contra diez--- y eso es justo lo que hace falta
abajo, donde el arco se cierra rápido.

```
cada sección lleva su propio alto de módulo y su propio tope de splay
    main      10 cajas × 0,35 m    splay hasta 10°
    downfill   4 cajas × 0,25 m    splay hasta 14°
```

Si tu archivo trata las catorce cajas como iguales, el downfill queda
limitado al splay de las grandes y no cubre lo que debería.

#### Subgraves colgados por encima

Con los subs arriba, **el array no arranca en el punto de izaje**: hay
que restar el alto de la pila de subs y la holgura del herraje.

```
z_pasador = z_motor − n_subs × alto_sub − 0,30
```

Olvidarlo no es un detalle. Cuatro subs de 60 cm bajan el pasador
**2,70 m**, y con él todo el array:

```
sin contarlo   la caja de arriba a 19,9°
contándolo     a 16,0°
```

Cuatro grados en todo el colgado, que a treinta metros son **2,3 m de
error en altura** sobre la última fila: el array pasa por encima del
público o le pega al balcón.

#### El tope mecánico

```
splay entre cajas contiguas    0° a 10°    (15° en algunos módulos)
acumulado en un array de 6      hasta 50°
```

Un pitch de 60° o más en la caja de abajo no es un array agresivo: es
un array que no se puede colgar.

> El punto de mira va a la altura del oído sentado: **z = 1,1 m**
> sobre el piso de esa zona. No al piso, no a 1,7 m.

---

### Si te piden un stack, el sistema se declara como stack

El programa tiene **dos constructores distintos** de line array, y el
que usa lo decide un solo campo:

```json
"mount": "flying"     el array cuelga     ← constructor de colgado
"mount": "stacked"    el array se apila   ← constructor de apilado
```

#### El valor tiene que ser exactamente `stacked`

El programa comprueba `mount.lower().startswith("stack")`. Cualquier
otra cosa cae en la rama de colgado:

```
"stacked"        ✓  reconocido
"stack"          ✓  reconocido
"ground_stack"   ✗  NO empieza con «stack» → se trata como COLGADO
"ground"         ✗
"stackeado"      ✓
```

> `ground_stack` parece razonable y no lo es. Un archivo con ese valor
> construye un stack por fuera y el programa lo arma como colgado por
> dentro: el sub queda arriba, la cadena va al revés y el editor no
> puede reabrirlo como lo que es.

#### Qué hace cada constructor

| | colgado | apilado |
|---|---|---|
| orden de las cajas | de arriba hacia abajo | **de abajo hacia arriba** |
| origen de la cadena | el punto de izaje | **el piso** |
| el sub | colgado **encima** del array | **debajo**, como base |
| el splay acumula | `cum_pitch += splay` | `cum_pitch −= splay` |
| el frente se inclina | hacia **abajo** | hacia **arriba** |

La fila 1 de la tabla del editor es **la base** en un stack y **la
caja de arriba** en un colgado. Es la misma tabla y significa lo
contrario.

#### El sub de un stack

En un stack el sub **es la base y define la altura de arranque**:

```json
{
  "name": "Array stackeado (6×dB VIO L210 + SUB dB VIO S218)",
  "mount": "stacked",
  "elements": [ … ]
}
```

El primer elemento es el sub, con:

```json
{
  "name": "SUB base",
  "pitch_deg": 0.0,
  "roll_deg": 0.0,
  "sub_orientation": "upright"
}
```

```
sub_orientation    "upright"   parado, roll 0°     altura = dimensión Z
                   "on_side"   acostado, roll 90°  altura = dimensión Y
```

El array arranca **encima del sub**, no en el piso:

```
z_base_del_array = z_piso + alto_del_sub
```

#### Cómo nombrar el sistema

El programa arma el nombre así, y conviene respetarlo para que el
editor lo reconozca al reabrirlo:

```
Array colgado (N×Modelo + SUB Modelo)
Array stackeado (N×Modelo + SUB Modelo)
```

#### El signo del splay en un stack

Éste es el detalle que invierte todo. En el constructor de apilado:

```
cum_pitch −= splay_deg        el splay POSITIVO inclina el frente ARRIBA
```

Un splay positivo en la tabla del editor sube el frente de la caja
siguiente. Es coherente con la premisa ---un stack cubre hacia
adelante y hacia arriba--- pero es el signo contrario al del colgado, y
copiar los splays de un colgado a un stack invierte la curva entera.

---

### El array apilado es otro problema, no un colgado más bajo

Ésta es la confusión que más daño hace, porque el archivo sale
coherente y el error sólo se ve proyectando dónde cae cada caja.

#### Por qué se cuelgan los arrays

Un array colgado está **ocho o diez metros por encima del oído**, así
que ve la platea con un arco vertical grande ---treinta o cuarenta
grados--- y puede repartirlo entre sus cajas.

Un stack está **uno o dos metros por encima del oído**. El arco que ve
es ínfimo:

```
stack sobre el escenario, cajas de z=1,68 a z=3,28
platea con piso a 1,15 m y 4° de pendiente
oído real: de 2,25 m en la primera fila a 3,72 m en la última

    caja de abajo  → la primera fila   −4,9°   ↑
    caja de arriba → la última fila    −0,9°   ↑
    ────────────────────────────────────────
    arco disponible                     4,0°
```

**Las seis apuntan hacia arriba**, porque el público está por encima
del stack en toda la platea. Un stack que en esta sala tuviera pitch
positivo estaría tirando contra el piso del escenario.

**Menos de un grado para seis cajas.** El splay es prácticamente cero y
el array trabaja casi como una línea recta.

Eso no es un defecto del cálculo: **es la razón física por la que
existen los arrays colgados.** Un stack no tiene control vertical, y
pedirle que lo tenga produce un archivo imposible.

#### El error típico: aplicarle el splay de un colgado

```
                        arco      caja de abajo
    lo que hace falta    0,8°           5,0°
    un splay de colgado 25,0°          28,0°
```

Con 28° desde 1,68 m de altura, la caja de abajo toca la altura del
oído **a un metro del stack**: dispara al escenario. En un caso real,
cuatro de seis cajas apuntaban al escenario y al foso de orquesta, y
la de arriba pasaba once metros más allá de la pared del fondo.

#### Cómo se arma un stack

```
1. El sub va ABAJO y el array encima
       z_base = z_escenario + alto_sub

2. El arco, medido antes de repartir nada
       th_lejos = atan2(z_caja_arriba − 1,10 · d_ultima_fila)
       th_cerca = atan2(z_caja_abajo  − 1,10 · d_primera_fila)
       arco = th_cerca − th_lejos

3. Si el arco es menor que 5°, el splay es CERO o casi
       splay = arco / (N − 1)

4. La cadena va de ABAJO hacia ARRIBA, y cada caja que se agrega
   RETROCEDE, porque gira sobre el pasador de la de abajo
       x −= alto_caja × sin(pitch)
       z += alto_caja × cos(pitch)
```

> El paso 3 es el que se saltea. Si tu stack tiene splays de cinco
> grados o más, no calculaste el arco: copiaste un colgado.

#### Lo que un stack no puede hacer

Aceptarlo es parte del diseño:

```
sin control vertical       no puede separar filas cercanas de lejanas
cae 6 dB por distancia     el fondo queda mucho más bajo que el frente
tapa la vista              al público de las primeras filas
```

Si la sala necesita control vertical, **el sistema tiene que colgarse**.
Un stack de seis cajas no equivale a un colgado de seis cajas: es otra
herramienta.

#### La comprobación

Una resta por caja, y atrapa el caso entero:

```
para cada caja:
    x_donde_cae = x_caja + (z_caja − 1,10) / tan(pitch)

    ninguna puede caer ANTES de la primera fila
    ninguna puede caer DESPUÉS de la pared del fondo
```

En el caso real que motivó esta sección:

```
    caja 1   28°  →  X = −3,5    al escenario
    caja 2   23°  →  X = −2,5    al escenario
    caja 3   18°  →  X = −0,9    al foso
    caja 4   13°  →  X = +2,0    recién acá empieza la audiencia
    caja 5    8°  →  X = +8,5
    caja 6    3°  →  X = +36,8   once metros detrás de la pared
```

---

### Un colgado con las cajas en línea vertical no existe

Si tu array tiene splay entre cajas, **las posiciones tienen que
avanzar**. Un archivo con las cuatro cajas en la misma X y ángulos de
10°, 17°, 25° y 34° no se puede armar: los herrajes no cierran.

```
splay de 10° a 34° en cajas de 37 cm  →  0,54 m de avance
```

Es la comprobación más rápida que existe para un colgado: **si todas
las cajas tienen la misma X y distinto ángulo, el array está mal
generado.**

---

### La cobertura horizontal

El vertical lo resuelve el splay. El horizontal lo resuelve **dónde
apunta el array y qué apertura tiene la caja**, y son dos cosas
distintas que conviene no mezclar.

#### El yaw es la BISECTRIZ del arco, no el centro del área

Éste es el error más frecuente, y es sutil porque el resultado parece
razonable.

La caja radia un patrón **simétrico respecto de su eje**. Para que ese
patrón cubra una zona, el eje tiene que ir en la mitad angular de la
zona ---la bisectriz--- y no en su centro geométrico.

No son lo mismo. El centro del área pondera por metros cuadrados; la
bisectriz pondera por grados, que es lo que la caja reparte.

```
para cada butaca de SU mitad, con el array en (xa, ya):
    ángulo = atan2(y_butaca − ya, x_butaca − xa)

yaw  = (ángulo_mínimo + ángulo_máximo) / 2
arco =  ángulo_máximo − ángulo_mínimo
```

> En una sala real la diferencia entre los dos criterios llega
> fácilmente a **diez o quince grados**, que en el borde de la
> cobertura son varios decibelios.

#### El arco lo fija la fila MÁS CERCANA

El arco angular de una zona **depende de la distancia**: cuanto más
cerca, más ancho. Así que el requisito lo pone la primera fila que el
array cubre, no la última.

```
    a X      al borde    al eje     arco
   −1,2       −33,9°     +45,6°    79,6°   ← manda ésta
    2,0       −24,7°     +30,6°    55,4°
    5,0       −18,3°     +23,0°    41,3°
    9,9       −12,7°     +16,2°    28,9°
```

Calcular el arco en el centro de la sala da la mitad del que hace
falta, y el array deja las butacas laterales de las primeras filas sin
cubrir.

#### Qué apertura necesita la caja

```
arco necesario ≤ apertura nominal de la caja
```

Las aperturas de catálogo son 70°, 90°, 110° y 120°, medidas a **−6
dB**. Si el arco supera la apertura, hay tres salidas y ninguna es
apretar el yaw:

```
1. caja de apertura mayor
2. un side hang que tome las butacas laterales
3. out fills, si lo que falta es sólo el borde cercano
```

#### Dónde se cruzan las dos mitades

Cada array cubre **su mitad más el eje**. Los bordes a −6 dB se cruzan
en el centro de la sala, y ahí las dos contribuciones suman.

```
el eje de la sala entra en el arco de LOS DOS arrays
```

Si cada array apunta al centro en vez de a su bisectriz, el centro
recibe los dos ejes: sube de nivel, aparece filtrado de peine y los
laterales quedan cortos. Es el defecto más común de un montaje L/R mal
aimado.

#### El toe-in

De lo anterior sale solo, y suele ser **pequeño**. Para el Vorterix:

```
PA L  a Y = −4,5   yaw = +5,8°    apenas hacia el eje
PA R  a Y = +4,5   yaw = −5,8°
```

Un toe-in de veinte o treinta grados no es «apuntar mejor al público»:
es cruzar los dos arrays en el centro y desatender los costados.

#### Los balcones laterales

Un balcón lateral se ve desde el array con un **ángulo muy abierto**,
porque está cerca y a un costado. Si lo incluís en el cálculo del
arco, el número crece de golpe ---en el Vorterix pasó de 58° a 80°---
y puede sacarte de la apertura de la caja.

Cuando eso ocurre, **el balcón no es del PA principal**: lleva su
propio sistema, sea un side hang o delays bajo el balcón superior.

---

### Los subgraves

**Dónde van.** En el piso, delante del escenario, en el eje o
repartidos a lo ancho.

**A dónde apuntan.**

```
yaw   = el EJE de la sala, no la bisectriz de un lado
pitch = 0
```

Los subs no cubren una mitad: cubren el eje. Su yaw es el que apunta
al centro de la audiencia desde su propia posición, que en una sala
simétrica da cero.

**No copies el yaw del PA.** El PA lleva la bisectriz de su mitad y
los subs no tienen mitad. En el Vorterix el PA va a ±5,8° y los subs a
0°, y las tres cifras son correctas. Si el PA mira a 0° porque la audiencia está en +X, los subs
también a 0°.

El pitch va en cero porque a esas frecuencias la caja es casi
omnidireccional: inclinarla no cambia nada y sólo complica el montaje.

---

### Los front fills

**Para qué.** Las primeras dos o tres filas quedan por debajo del
alcance del PA, aun de su caja más baja. Los front fills las cubren.

**Dónde van.** Sobre el borde del escenario, al ras, repartidos cada
dos a tres metros.

**A dónde apuntan.** A la fila que el PA no alcanza:

```
x_objetivo = la primera fila
z_objetivo = 1,1 m
```

El pitch sale más fuerte de lo que la intuición sugiere, porque la
fila está cerca. Un front fill a 1,8 m que cubre una fila a dos metros
da unos veinte grados; a cinco metros, ocho. **Calculalo, no lo
supongas:** es el sistema donde más se equivoca la intuición, porque el
parlante parece estar casi a la altura del oyente.

---

### Los out fills

**Para qué.** Las butacas laterales, fuera del ancho de cobertura del
PA principal.

**A dónde apuntan.** Se abren respecto del PA:

```
out fill izquierdo   yaw = yaw_PA − (45° a 70°)
out fill derecho     yaw = yaw_PA + (45° a 70°)
```

> ⚠ El ángulo **entre los dos** tiene que superar los 90°. Si queda
> por debajo, los out fills están apuntando al mismo sitio que el PA y
> no cubren nada nuevo.

---

### Los delays

Aquí hay dos cosas distintas y conviene no mezclarlas: **dónde
apuntan** y **cuánto se retardan**.

#### Cuándo hacen falta

```
bajo balcón      cuando el balcón tapa la vista directa al PA
torre de delay   más allá de 25 a 30 m del PA
                 o donde el nivel cae 6 dB por debajo del frente
```

#### Dónde apuntan

Con la misma fórmula de arriba, **al centro de la zona que cubren**.
No al fondo de la sala ni al eje: a su propia zona, que suele ser
pequeña.

Un delay bajo balcón cubre las filas que el balcón ensombrece. Si esa
franja va de X=10,2 a X=15,2, el objetivo es su centro, X≈12,7.

#### Cuánto se retardan

El retardo es el tiempo que tarda el sonido del PA en llegar **hasta
el delay**, no hasta la audiencia:

```
d = distancia del CENTRO ACÚSTICO del PA al delay
t = d / c              c = 343 m/s a 20 °C
t_ms = d × 2,92        ≈ 3 ms por metro
```

#### El desfase de Haas

A ese tiempo se le **suma** de 5 a 15 ms:

```
t_final = d/c + offset        offset de 5 a 15 ms
```

Sin ese suplemento, el delay y el PA llegan juntos y el oyente
localiza el sonido en el parlante que tiene encima ---a dos metros---
en vez de en el escenario. Con el suplemento, el PA llega primero y la
imagen se queda en el escenario, que es de donde la gente espera que
venga.

Quince milisegundos es un margen cómodo; más de treinta ya se oye como
eco.

#### Ejemplo completo

PA colgado con su centro acústico en `(−5,5 · −4,5 · 5,8)`. Delay bajo
balcón en `(9,6 · −4,45 · 3,15)`, que cubre la franja X de 10,2 a 15,2.

```
EL RETARDO
  Δ = (15,10 · 0,05 · −2,65)
  d = √(15,10² + 0,05² + 2,65²) = 15,33 m
  t = 15,33 / 343 = 44,7 ms
  + desfase de Haas, 10 ms
  ────────────────────────────
  delay_ms = 54,7

EL APUNTADO
  objetivo: centro de su franja, oído sentado  (12,7 · −2,5 · 1,1)
  Δ = (3,10 · 1,95 · −2,05)
  yaw   = atan2(1,95 · 3,10)          = +32,2°
  pitch = atan2(2,05 · 3,66)          = +29,2°
```

---

### Los monitores y los side fills

Apuntan **al escenario**, no a la audiencia. Es la única familia de
sistemas que va al revés que todas las demás, y por eso conviene
revisarla aparte.

```
monitor de piso   objetivo: la cabeza del músico, z ≈ 1,6 m de pie
side fill         objetivo: el centro del escenario
```

Un side fill que apunte a la platea está alimentando el micrófono
abierto de la voz y realimentando el sistema.

---

### La comprobación

Cinco cuentas, ninguna necesita el programa.

```
[ ] la altura del oído incluye el piso de la zona y su pendiente
[ ] cada yaw y cada pitch salieron de atan2, no de un ejemplo
[ ] el COLGADO tiene pitch positivo: cubre adelante y abajo
[ ] el APILADO tiene pitch negativo: cubre adelante y arriba
[ ] todos los pitch del PA colgado son positivos y CRECEN hacia abajo
[ ] la caja superior del PA no pasa por encima de la última fila
      alcance = (z_caja − 1,1) / tan(pitch)   debe caer DENTRO de la sala
[ ] el yaw de los subs es igual al del PA
[ ] cada delay tiene delay_ms ≈ distancia_al_PA × 2,92 + 5 a 15
[ ] los monitores y side fills apuntan al escenario, no a la platea
```

---

## 1. Estructura general del JSON

```json
{
  "app": "CADSFS",
  "version": "1.49.84",
  "bands_hz": [31,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500],
  "c_m_s": 343.0,

  "materials": [],
  "selected_material_name": "Default",

  "objects": [ ... ],
  "speaker_systems": [ ... ],

  "source_pos": [x, y, z],
  "receiver_pos": [x, y, z],
  "source_spl_db": 94.0,
  "source_polar_pattern": "Omni",
  "receiver_radius_m": 0.1,
  "measured_rt60_s": {},

  "surface_group_material":   { "1|Floor": "Nombre material", ... },
  "surface_group_material_b": { "1|Wall +X": "Material cara B", ... },
  "surface_assembly_map":     { "1|Floor": "asm_xxxxx", ... },
  "surface_thickness_dir":    { "1|Floor": "inward", ... },

  "wall_assemblies": { ... },
  "audience_areas": [],
  "audience_areas_enabled": true,
  "ground_conditions": { ... },

  "active_enclosure_id": 1,
  "outdoor_mode": false,
  "surround_mode": false,
  "surround_format": "2.0",
  "project_name": "",
  "project_designer": "",
  "project_builder": "",
  "project_client": "",
  "project_location": "",
  "project_date": "",
  "project_venue_type": "",
  "project_notes": "",
  "local_view_radius_m": 8.0,
  "show_wall_sections": true,
  "xray_alpha": 0.08,
  "xray_fraction": 0.20,

  "autocad_accoreconsole_exe": "",
  "oda_file_converter_exe": "",
  "sketchup_exe": ""
}
```

### `source_polar_pattern` — Directividad de la fuente puntual

Aplica a la **fuente puntual del proyecto** (`source_pos` + `source_spl_db`), la que se usa cuando NO hay `speaker_systems` y se excita la sala con una única fuente — típicamente para **predicción de acústica de salas / medición estilo ISO 3382** (RT60, C80, D50, STI). No confundir con los parlantes de un sistema de refuerzo (esos llevan su propia directividad por `model_id`).

Valores válidos (string exacto; la lógica es independiente del idioma de la UI):

| Valor | Uso |
|-------|-----|
| `"Omni"` | Fuente omnidireccional ideal (default). |
| `"Dodecaédrico (ISO 3382)"` | **Fuente dodecaédrica normalizada** — la fuente estándar para medir parámetros de sala según **ISO 3382**. |
| `"Cardioide"` | Directividad cardioide. |
| `"Supercardioide"` | Supercardioide. |
| `"Hipercardioide"` | Hipercardioide. |
| `"Dipolo"` | Figura-8 (dipolo). |

> **Dodecaédrico es un modelo físico real, no un "omni ideal" con otra etiqueta.** CADSFS lo modela como **12 drivers coherentes en las 12 caras de un dodecaedro** (radio de esfera ≈ 0.2 m, tipo B&K 4292, Ø≈0.4 m): a bajas frecuencias es prácticamente omni, pero por encima de la frecuencia donde la circunferencia de la esfera se acerca a λ aparece el **rizado de directividad característico** de una dodecaédrica real. Es la opción correcta cuando querés que la predicción reproduzca las condiciones de una medición ISO 3382 (y no un omni perfecto que ninguna fuente real logra en agudos).

Para escenas de **refuerzo sonoro** (con PA/subs), este campo es irrelevante: dejalo en `"Omni"` y definí la directividad real vía los `model_id` de los `speaker_systems`.

---

## 2. REGLA CRÍTICA — Materials

```json
"materials": [],
```

**NUNCA incluir materiales custom.** El software tiene una base de datos interna de **2665 materiales** con coeficientes de absorción y scattering calibrados. Si el JSON incluye un array `materials` con entradas, el software **REEMPLAZA** toda su base interna con ese subconjunto → rompe colores 3D, lookups, opacidad, todo.

Los nombres en `surface_group_material` se resuelven contra la base interna por búsqueda fuzzy. Si un nombre no existe, se asigna "Default" (α=0.10 flat → RT60 plano sin variación por frecuencia → resultado sin sentido físico).

> ⚠ **REGLA ABSOLUTA: NUNCA "Default" como material final.** Toda superficie DEBE tener un material REAL asignado en `surface_group_material`. Si la IA deja alguna superficie con "Default", el cálculo de RT60 será plano e irreal (mismo valor en todas las bandas). El campo `selected_material_name: "Default"` es solo el fallback interno — las asignaciones explícitas lo sobreescriben.

### Nombres de materiales absorbentes disponibles (ejemplos comunes)

| Categoría | Nombres exactos (case-sensitive, verificados en DB) |
|-----------|----------------------------------|
| Hormigón | `Hormigón liso`, `Hormigón liso`, `Hormigón rugoso / encofrado`, `Hormigón pulido (microrelieve)` |
| Ladrillo | `Ladrillo visto`, `Ladrillo visto`, `Ladrillo visto (con juntas/relieve)`, `Ladrillo pintado`, `Ladrillo hueco visto`, `Ladrillo hueco visto (irregular)` |
| Yeso | `Yeso liso pintado`, `Yeso liso pintado`, `Yeso liso pintado (con juntas/relieve)`, `Pladur / placa de yeso (sobre perfilería)` |
| Madera | `Madera maciza barnizada (panel)`, `Madera maciza barnizada (panel)`, `Madera maciza barnizada 15 mm (sobre rastreles)`, `Madera maciza sin barniz` |
| Vidrio | `Vidrio (ventana)`, `Vidrio (ventana)` |
| Baldosa | `Baldosa cerámica con juntas`, `Baldosa cerámica 10 mm + underlay 20 mm (sobre hormigón)`, `Azulejo cerámico esmaltado` |
| Cortina | `Cortina pesada (100% fruncido)`, `Cortina ligera (poca fruncido)`, `Cortina media (50% fruncido)` |
| Alfombra | `Alfombra ligera (sin underlay)`, `Alfombra ligera (sin underlay)` |
| Butacas | `Butaca tapizada (vacía)`, `Butaca tapizada (ocupada)`, `Butaca tapizada (vacía)` |

> **Sobre las butacas.** La biblioteca distingue
> `Butaca tapizada (vacía)` de `Butaca tapizada (ocupada)`, y la
> diferencia entre las dos es la que decide el RT60 de una sala de
> espectáculos. Elegí la que corresponda al escenario que se está
> calculando: una sala vacía y la misma sala llena no son el mismo
> problema acústico.
| Panel perf. | `Panel perforado MDF t=16mm φ=5% cav=50mm`, `Panel perforado MDF t=16mm φ=5% cav=50mm + lana 25mm` |
| Metal | `Acero pintado / chapa`, `Aluminio anodizado / chapa` |
| Piso madera | `Parquet de madera barnizado`, `Tarima flotante (laminado) sobre espuma` |
| Techo acúst. | `Placa de techo fibra mineral 18 mm (σ≈15k) + plenum 200 mm`, `Placa de techo fibra mineral 20 mm (σ≈22k) + plenum 100 mm` |
| Lana mineral | `Lana mineral (roca) 50 mm (pared rígida)`, `Lana mineral (roca) 100 mm (pared rígida)`, `Lana mineral (roca) 50 mm + cámara 50 mm (pared rígida)` |
| Absorbentes | `Absorbente (espuma) genérico 50mm`, `Panel textil tensado con cámara 50 mm (sin relleno)`, `Tapiz / tela gruesa sobre pared` |
| Nube/Cloud | `Nube acústica suspendida (fibra mineral) 80 mm (σ≈6k)`, `Nube acústica suspendida (fibra de vidrio) 60 mm (σ≈6k)` |
| Difusores | `Difusor (1D) genérico`, `Difusor (2D) genérico`, `Difusor QRD 1D N=7 (f_min≈700 Hz) - madera` |

### Materiales obligatorios por tipo de recinto

La IA DEBE asignar materiales DIFERENCIADOS. Mínimo por superficie:

| Tipo de recinto | Piso | Techo | Pared frontal | Paredes lat. | Pared trasera | Puertas | Ventanas |
|----------------|------|-------|---------------|-------------|--------------|---------|----------|
| **Estudio CR** | `Alfombra ligera (sin underlay)` o `Parquet de madera barnizado` | `Placa de techo fibra mineral 18 mm (σ≈15k) + plenum 200 mm` | `Lana mineral (roca) 50 mm (pared rígida)` | `Panel textil tensado con cámara 50 mm (sin relleno)` | `Panel perforado MDF t=16mm φ=5% cav=50mm` (absorbe medios: no es un difusor) | `Madera maciza barnizada (panel)` | `Vidrio (ventana)` |
| **Live Room** | `Parquet de madera barnizado` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` | `Lana mineral (roca) 50 mm (pared rígida)` o `Difusor (1D) genérico` | `Panel perforado MDF t=16mm φ=5% cav=50mm` | `Madera maciza barnizada (panel)` | `Vidrio (ventana)` |
| **Concierto/Ópera** | `Parquet de madera barnizado` o `Alfombra ligera (sin underlay)` | `Yeso liso pintado` o `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` | `Yeso liso pintado` o `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` o `Yeso liso pintado` | `Madera maciza barnizada (panel)` | `Vidrio (ventana)` |
| **Venue amplificado** | `Hormigón pulido (microrelieve)` | `Acero pintado / chapa` | `Hormigón rugoso / encofrado` | `Ladrillo visto` | `Ladrillo visto` | `Acero pintado / chapa` | — |
| **Cine** | `Alfombra ligera (sin underlay)` | `Placa de techo fibra mineral 20 mm (σ≈8k) + plenum 200 mm` | `Cortina pesada (100% fruncido)` | `Cortina pesada (100% fruncido)` | `Cortina pesada (100% fruncido)` | `Cortina pesada (100% fruncido)` | — |
| **Teatro** | `Alfombra ligera (sin underlay)` o `Parquet de madera barnizado` | `Yeso liso pintado` | `Cortina pesada (100% fruncido)` | `Yeso liso pintado` | `Cortina pesada (100% fruncido)` | `Madera maciza barnizada (panel)` | — |

> **Estudio CR: la fila de la tabla es para cuando el tratamiento lo hacen las
> superficies del recinto.** En un diseño completo el tratamiento va en objetos
> (§26.2): paneles, trampas, nube, difusores. En ese caso las paredes y el techo
> van de `Pladur / placa de yeso (sobre perfilería)`, el piso de
> `Parquet de madera barnizado` y el frente con lana (§52.5). Si además las
> superficies llevan absorbente, la sala queda muerta: con los objetos de §52.5 y
> las superficies de esta fila, Tm de 0,17 s por Sabine y 0,13 s por Eyring, con
> los graves tres veces más largos que los medios.
>
> **El techo acústico, por su curva en tercios.** La placa
> `Placa de techo fibra mineral 20 mm (σ≈8k) + plenum 200 mm` sube y baja de un
> tercio al siguiente: 0,20 en 800 Hz, 0,53 en 1 kHz, 0,33 en 1,6 kHz y 0,75 en
> 2 kHz. Con ella la curva de RT sale en serrucho. En un estudio va la de 18 mm
> (σ≈15k) + plenum 200 mm, que es pareja: de 0,28 en 125 Hz a 0,86 en 4 kHz.

### Materiales por zona — Teatro lírico / Ópera / Salas con palcos

Para teatros complejos con múltiples objetos internos (escenario, foso, palcos, galería, etc.), la IA DEBE asignar materiales **diferenciados por zona Y por tipo de superficie** dentro de cada zona.

| Objeto / Zona | Floor (Piso) | Ceiling (Techo) | Walls (Paredes) |
|----------------|-------------|-----------------|-----------------|
| **Recinto (envolvente)** | — (no visible, cubierto por objetos) | `Yeso liso pintado` | `Yeso liso pintado` |
| **Escenario** | `Parquet de madera barnizado` | `Cortina pesada (100% fruncido)` | `Cortina pesada (100% fruncido)` |
| **Foso de orquesta** | `Parquet de madera barnizado` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Platea / Butacas** | `Alfombra ligera (sin underlay)` | `Butaca tapizada (ocupada)` | `Butaca tapizada (ocupada)` |
| **Palcos (todos los niveles)** | `Alfombra ligera (sin underlay)` | `Yeso liso pintado` | `Madera maciza barnizada (panel)` |
| **Galería alta / Paraíso** | `Alfombra ligera (sin underlay)` | `Yeso liso pintado` | `Madera maciza barnizada (panel)` |
| **Reflectores laterales** | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Cúpula / Domo** | — | `Yeso liso pintado` | `Yeso liso pintado` |
| **Proscenio / Embocadura** | `Parquet de madera barnizado` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Telón / Cortinado** | — | — | `Cortina pesada (100% fruncido)` |

### Materiales por zona — Sala de conciertos (shoebox / vineyard)

| Objeto / Zona | Floor (Piso) | Ceiling (Techo) | Walls (Paredes) |
|----------------|-------------|-----------------|-----------------|
| **Recinto** | — | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Escenario** | `Parquet de madera barnizado` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Platea / Butacas** | `Alfombra ligera (sin underlay)` | `Butaca tapizada (ocupada)` | `Butaca tapizada (ocupada)` |
| **Balcones** | `Alfombra ligera (sin underlay)` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Reflectores** | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |

### Materiales por zona — Auditorio multiuso

| Objeto / Zona | Floor (Piso) | Ceiling (Techo) | Walls (Paredes) |
|----------------|-------------|-----------------|-----------------|
| **Recinto** | — | `Placa de techo fibra mineral 20 mm (σ≈8k) + plenum 200 mm` | `Yeso liso pintado` |
| **Escenario** | `Parquet de madera barnizado` | `Yeso liso pintado` | `Cortina pesada (100% fruncido)` |
| **Butacas** | `Alfombra ligera (sin underlay)` | `Butaca tapizada (ocupada)` | `Butaca tapizada (ocupada)` |
| **Cabina técnica** | `Alfombra ligera (sin underlay)` | `Yeso liso pintado` | `Vidrio (ventana)` (frontal), `Yeso liso pintado` (laterales) |

### Materiales por zona — Iglesia / Templo

| Objeto / Zona | Floor (Piso) | Ceiling (Techo) | Walls (Paredes) |
|----------------|-------------|-----------------|-----------------|
| **Nave principal** | `Mármol pulido` o `Baldosa cerámica con juntas` | `Yeso liso pintado` | `Hormigón liso` o `Ladrillo visto` |
| **Altar / Presbiterio** | `Mármol pulido` | `Yeso liso pintado` | `Hormigón liso` |
| **Coro** | `Parquet de madera barnizado` | `Madera maciza barnizada (panel)` | `Madera maciza barnizada (panel)` |
| **Bancos (feligreses)** | `Madera maciza barnizada (panel)` | — | — |

> **REGLA**: la IA DEBE cruzar el **nombre del objeto** con el **tipo de superficie** (Floor/Ceiling/Wall) para elegir el material. NO asignar el mismo material a todas las superficies de un objeto.

> **VALIDACIÓN**: si TODAS las bandas de RT60 dan el mismo valor, alguna superficie tiene "Default". Revisar `surface_group_material`.

### Tipologías de sala — guía rápida para el AI

Al recibir imágenes o descripciones, el AI debe **identificar la tipología** antes de generar geometría y materiales:

| Tipología | Forma planta | Altura típica | Material dominante | Objetos internos típicos |
|-----------|-------------|---------------|-------------------|--------------------------|
| **Teatro lírico / ópera** | Herradura (17+ vértices) | 18–30 m | Madera barnizada + yeso | Escenario, foso, platea, 2-4 niveles palcos, galería, reflectores |
| **Sala de conciertos (shoebox)** | Rectangular o con terrazas | 12–20 m | Madera maciza | Escenario, platea, balcones laterales |
| **Sala de conciertos (vineyard)** | Orgánica / terrazas envolventes | 15–25 m | Madera + hormigón visto | Escenario central, terrazas, reflectores de techo |
| **Auditorio multiuso** | Abanico | 8–15 m | Yeso + placas acústicas | Escenario, butacas, cabina técnica |
| **Teatro de prosa** | Abanico o rectangular | 8–12 m | Yeso + cortinado | Escenario, platea, balcón |
| **Iglesia / Templo** | Nave + crucero | 10–30 m | Piedra / hormigón / ladrillo | Altar, nave, coro, baptisterio |
| **Estudio de grabación (CR)** | Rectangular | 2.8–4 m | Absorbentes + difusores | — (single room) |
| **Live Room** | Rectangular o irregular | 3–5 m | Madera + absorbentes | — (single room) |
| **Venue amplificado** | Rectangular o L | 4–8 m | Hormigón + ladrillo | Escenario, barra, balcón |
| **Cine** | Abanico | 6–12 m | Cortinado pesado | Pantalla, butacas |

> La tipología determina qué tabla de materiales usar (ver secciones anteriores) y qué objetos internos crear.

---

### Recintos GRANDES (arenas, estadios, pabellones) — RT60 y absorción

> ⚠ **El error más grave en recintos grandes: RT60 absurdo en graves (20–60 s).**
> No es un bug del software: es física correcta de un modelo mal balanceado.

**Por qué pasa:** RT60 de Sabine = K · V / A, con K = 24·ln(10)/c = 0,1611 s/m
(c = 343 m/s, el `c_m_s` del proyecto). Una arena tiene un volumen
enorme (una arena de 116×96×26 m ≈ **270.000 m³**). Si la envolvente es hormigón
(absorbe ~1 % en 63 Hz), el área absorbente A es minúscula frente a V, y el
cociente explota: RT60 en graves de 45–140 s. **Esto es lo que pasó en un caso real.**

**Reglas para que el RT60 sea realista en recintos grandes:**

1. **El público DEBE aportar su absorción — y esto requiere `audience_zones`, NO `audience_areas`.**
   En una arena ocupada, la mayor parte de la absorción en graves viene del público.
   CADSFS distingue DOS conceptos que NO hay que confundir:
   - **`audience_areas`**: zonas para EVALUAR cobertura SPL (campos `target_db`,
     `tolerance_db`, `slope_deg`). **NO aportan absorción.** Son zonas de medición.
   - **`audience_zones`**: zonas de PÚBLICO con absorción (campos `type`,
     `occupancy_pct`, `density`). **ESTAS SÍ** suman absorción al RT60.
   - Para un recinto OCUPADO: crear `audience_zones` con `type: "seated_upholstered"`
     (o el tipo que corresponda) y `occupancy_pct` (ej. 90), sobre las gradas.
     Sin esto, el público NO existe acústicamente y el RT60 en graves se dispara.
   - Además, asignar `Butaca tapizada (ocupada)` (α≈0.20 en 63 Hz, 0.40 en 125 Hz)
     a las superficies de los asientos.

2. **No dejar toda la envolvente en hormigón duro.** Una arena real tiene tratamiento:
   - Cubierta/techo: en arenas multipropósito suele haber `Lana mineral (roca) 50 mm (pared rígida)` o
     `Absorbente (espuma) genérico 50mm` en el deck, no metal desnudo. Si el techo es reflectante,
     el RT en graves se dispara.
   - Considerar `Cortina pesada (100% fruncido)` o materiales absorbentes en fondos de escenario.

3. **Verificá el balance V/A.** Si el RT60 da > 5 s en graves para una arena con
   público, falta absorción: revisá que las butacas y el público estén contando.
   Un estadio ocupado típico tiene RT60 medio de 1.5–3 s (no 45).

4. **Si el recinto es semiabierto** (techo retráctil, laterales abiertos),
   usá aberturas (`opening`) o `outdoor_mode` para que la energía escape; un
   recinto modelado como CERRADO y reflectante atrapa toda la energía → RT alto.

> **Nota de validación:** tras generar un recinto grande, pedir mentalmente
> el chequeo: «¿el RT60 en 63 Hz es < 5 s?». Si no, el modelo tiene demasiada
> superficie reflectante y poca absorción de público/tratamiento.

## 3. Objects (geometría)

Cada objeto tiene esta estructura exacta (todos los campos son obligatorios):

```json
{
  "obj_id": 1,
  "name": "Sala Principal",
  "parent_id": null,
  "is_enclosure": true,
  "two_sided": false,
  "side_a_exterior": false,
  "source": {
    "kind": "box",
    "path": null,
    "scale_to_m": 1.0,
    "size_xyz": [10.0, 8.0, 4.0],
    "centered": false,
    "polygon_xy": null,
    "height": null,
    "plane": null
  },
  "base_vertices_world": { "dtype": "float32", "shape": [8, 3], "data": "..." },
  "faces_local":         { "dtype": "int32",   "shape": [12, 3], "data": "..." },
  "face_to_group_idx":   { "dtype": "int32",   "length": 12, "data": "..." },
  "group_order": ["Floor", "Ceiling", "Wall +X", "Wall +Y", "Wall -X", "Wall -Y", "Unassigned"],
  "group_material": {
    "Floor": "Baldosa cerámica 10 mm + underlay 20 mm (sobre hormigón)",
    "Ceiling": "Yeso liso pintado",
    "Wall +X": "Ladrillo visto (con juntas/relieve)",
    "Wall +Y": "Ladrillo visto (con juntas/relieve)",
    "Wall -X": "Ladrillo visto (con juntas/relieve)",
    "Wall -Y": "Ladrillo visto (con juntas/relieve)",
    "Unassigned": "Default"
  },
  "pivot_world": [0.0, 0.0, 2.0],
  "rotation_deg": [0.0, 0.0, 0.0],
  "translation_m": [0.0, 0.0, 0.0]
}
```

> En este ejemplo, la sala de 10×8×4 m queda: X de −5 a +5, Y de −4 a +4, Z de 0 a 4.
> Los vértices en `base_vertices_world` se generan con `make_box(cx=0, cy=0, z_floor=0, w=10, d=8, h=4)`.
> `pivot_world = [0, 0, 2]` = centro geométrico.

### Reglas de objetos

**`source`**: Debe incluir TODOS los campos (incluso los null). Para box: `kind="box"`, `size_xyz=[X,Y,Z]` = `[profundidad, ancho, alto]`. Para extrusión: `kind="extrude"`, `polygon_xy=[[x,y]...]`, `height=H`.

**`group_order`**: Para un box siempre es `["Floor", "Ceiling", "Wall +X", "Wall +Y", "Wall -X", "Wall -Y", "Unassigned"]`. El `"Unassigned"` al final es OBLIGATORIO.

**`group_material`**: Debe incluir `"Unassigned": "Default"`.

**`face_to_group_idx`**: Para un box, 12 triángulos → 2 por cara → `[0,0,1,1,2,2,3,3,4,4,5,5]`.

**`pivot_world`**: Centro geométrico del objeto en coordenadas mundo. Para el enclosure centrado en (0,0) con alto H: `pivot_world = [0, 0, H/2]`. Para objetos internos: `pivot_world = [cx, cy, z_floor + h/2]`.

**`base_vertices_world`**: Las coordenadas FINALES de los vértices en el mundo. El enclosure se genera con `make_box(cx=0, cy=0, z_floor=0, ...)` para que quede centrado en XY con el piso en Z=0.

### Enclosure vs objetos internos

| Campo | Enclosure (sala) | Objeto interno (escenario) |
|-------|-------------------|---------------------------|
| `is_enclosure` | `true` | `false` |
| `side_a_exterior` | `false` | `true` |
| `two_sided` | `false` | `false` |

**Todos los objetos cuyo centroide está dentro del enclosure afectan los modos** — no importa `side_a_exterior` ni `is_enclosure`.

### REGLA CRÍTICA — Parlantes NUNCA son objetos de geometría

**Los parlantes, subwoofers, pedestales de parlantes y soportes de monitores NUNCA deben crearse como objetos en la sección `objects`.** Van EXCLUSIVAMENTE en `speaker_systems` con sus `elements` y `pedestals`.

Si se crean cajas 3D para representar parlantes como objetos de geometría:
- El análisis modal los cuenta como volumen sólido dentro del recinto → modos incorrectos.
- Duplican los parlantes ya definidos en `speaker_systems`.
- La masa de triángulos extra ralentiza toda la simulación.
- CADSFS ya renderiza las cajas y pedestales automáticamente desde `speaker_systems`.

**Excepción**: Muebles que *contienen* o *soportan* parlantes (como una consola, una mesa, un rack) SÍ son objetos de geometría legítimos. Pero el parlante en sí no.

| Elemento | ¿Es objeto en `objects`? | ¿Es elemento en `speaker_systems`? |
|----------|:---:|:---:|
| Parlante (ATC SCM300, L-Acoustics X8…) | **NO** | **SÍ** |
| Pedestal de parlante | **NO** | SÍ (campo `pedestal` en el elemento) |
| Subwoofer | **NO** | **SÍ** (mount: sub_array) |
| Consola de mezcla | SÍ | No |
| Rack de equipos | SÍ | No |
| Silla del operador | SÍ | No |

### Encoding de arrays binarios

```python
import numpy as np, base64, zlib

def encode_vertices(verts_array):
    """verts_array: np.array shape (N,3) float32"""
    v = np.asarray(verts_array, dtype=np.float32)
    compressed = zlib.compress(v.tobytes())
    return {
        "dtype": "float32",
        "shape": list(v.shape),
        "data": base64.b64encode(compressed).decode("ascii")
    }

def encode_faces(faces_array):
    """faces_array: np.array shape (M,3) int32"""
    f = np.asarray(faces_array, dtype=np.int32)
    compressed = zlib.compress(f.tobytes())
    return {
        "dtype": "int32",
        "shape": list(f.shape),
        "data": base64.b64encode(compressed).decode("ascii")
    }

def encode_f2g(f2g_array):
    """f2g_array: np.array shape (M,) int32"""
    a = np.asarray(f2g_array, dtype=np.int32)
    compressed = zlib.compress(a.tobytes())
    return {
        "dtype": "int32",
        "length": int(a.size),
        "data": base64.b64encode(compressed).decode("ascii")
    }
```

### Box: vértices y caras estándar

```python
def make_box(cx, cy, z_floor, w, d, h):
    """Genera vértices y caras para un box centrado en (cx,cy), piso en z_floor."""
    x0, x1 = cx - w/2, cx + w/2
    y0, y1 = cy - d/2, cy + d/2
    z0, z1 = z_floor, z_floor + h

    V = np.array([
        [x0,y0,z0],[x1,y0,z0],[x1,y1,z0],[x0,y1,z0],  # piso
        [x0,y0,z1],[x1,y0,z1],[x1,y1,z1],[x0,y1,z1],  # techo
    ], dtype=np.float32)

    F = np.array([
        [0,2,1],[0,3,2],  # Floor    (g0)
        [4,5,6],[4,6,7],  # Ceiling  (g1)
        [1,2,6],[1,6,5],  # Wall +X  (g2)
        [2,3,7],[2,7,6],  # Wall +Y  (g3)
        [3,0,4],[3,4,7],  # Wall -X  (g4)
        [0,1,5],[0,5,4],  # Wall -Y  (g5)
    ], dtype=np.int32)

    f2g = np.array([0,0,1,1,2,2,3,3,4,4,5,5], dtype=np.int32)

    pivot = [cx, cy, z_floor + h/2]

    return V, F, f2g, pivot

# ── Uso para enclosure (sala centrada en 0,0) ──
# Teatro 20×12×8 m:
V, F, f2g, pivot = make_box(cx=0, cy=0, z_floor=0, w=20, d=12, h=8)
# → X: −10 a +10, Y: −6 a +6, Z: 0 a 8
# → pivot = [0, 0, 4]

# ── Uso para objeto interno (posición absoluta) ──
# Escenario 8×10×1 m centrado en X=−6 (zona de escenario):
V, F, f2g, pivot = make_box(cx=-6, cy=0, z_floor=0, w=8, d=10, h=1)
# → X: −10 a −2, Y: −5 a +5, Z: 0 a 1
```

### Extrusiones — REGLA ABSOLUTA

**REGLA**: SIEMPRE usar extrusión (`kind: "extrude"`) para TODO tipo de recinto. NUNCA usar `kind: "box"` para el enclosure. Incluso una sala perfectamente rectangular se modela como extrusión con 4 vértices.

> ⚠ **Enclosure watertight (estanco) — para que calcule modos y RT60:**
> El análisis modal y el RT60 requieren que el enclosure sea un volumen CERRADO.
> Una extrusión bien formada (`polygon_xy` cerrado + `height`) genera automáticamente
> un volumen estanco: el software extruye el perímetro y tapa piso y techo. **Esto
> funciona incluso con perímetros complejos de muchos vértices** (arenas tipo bowl,
> herraduras): el polígono se cierra solo si el primer y último punto coinciden o si
> está bien ordenado CCW.
> - **Si los modos NO aparecen en la pestaña modal:** casi siempre es porque (a) el
>   enclosure no es watertight, o (b) `active_enclosure_id` no apunta al objeto con
>   `is_enclosure: true`. Verificá ambos.
> - **El perímetro define la geometría real**, no hace falta crear cada pared como
>   objeto suelto. Las gradas/escenario/palcos van como objetos INTERNOS
>   (`is_enclosure: false`) DENTRO del enclosure, con su material absorbente.
> - **Polígono complejo (bowl/herradura):** dar el perímetro completo en `polygon_xy`
>   (decenas de puntos está bien), CCW visto desde arriba, centrado en (0,0). El
>   software lo extruye a un volumen cerrado.

### Sala rectangular como extrusión

```json
{
  "enclosure": {
    "kind": "extrude",
    "polygon": [[-5, -4], [-5, 4], [5, 4], [5, -4]],
    "height": 3.0
  }
}
```

Equivale a una sala de 10×8×3m centrada en (0,0). El sentido del polígono no importa: este
ejemplo es horario visto desde arriba (sube por x = −5 y sigue hacia +X), otros son
antihorarios, y el programa resuelve los dos. `Pared k` es la arista del vértice k al k+1.

### Cuándo NO hay enclosure

| Escenario | Geometría |
|-----------|-----------|
| **Cualquier recinto cerrado** | `kind: "extrude"` con polígono |
| **Aire libre / outdoor** | Sin enclosure. `"outdoor_mode": true` |
| Objetos internos (consola, sofá, panel) | `kind: "box"` (son objetos, no enclosures) |

### Modo Outdoor (aire libre)

Para festivales, estadios sin techo, escenarios al aire libre:

```json
{
  "outdoor_mode": true,
  "objects": [
    {
      "name": "Suelo",
      "kind": "box",
      "dimensions": [50, 30, 0.1],
      "center": [0, 0, -0.05],
      "is_enclosure": false,
      "side_a_exterior": true
    }
  ]
}
```

RT60 retorna T=0 (volumen infinito). La cobertura usa solo SPL directo. Opcionalmente se puede modelar el suelo como objeto plano para reflejos de piso.

### Source para extrusión

```json
"source": {
    "kind": "extrude",
    "path": null,
    "scale_to_m": 1.0,
    "size_xyz": null,
    "centered": true,
    "polygon_xy": [
        [-3.30, -2.50], [-3.40, 0.00], [-3.30, 2.50],
        [-1.20, 2.75], [1.50, 2.40],
        [3.30, 1.90], [3.30, -1.90],
        [1.50, -2.40], [-1.20, -2.75]
    ],
    "height": 3.8,
    "plane": null
}
```

**Reglas del polígono**: CCW visto desde arriba. X = profundidad, Y = ancho (ver §0). Cada arista genera un `Pared N` (N = 0..len(polygon)-1). El `group_order` será `["Piso", "Techo", "Pared 0", ..., "Pared N-1", "Unassigned", "Default"]`.

> **Convención de nombres para extrusiones**: Las paredes se nombran por índice del polígono: `Pared 0`, `Pared 1`, etc. Las keys de `surface_group_material` y `surface_assembly_map` deben usar estos nombres: `"1|Pared 0"`, `"1|Pared 1"`, etc.

### Generador de extrusión

```python
def make_extrusion(polygon_xy, height, z0=0.0):
    N = len(polygon_xy)
    verts = []
    for x, y in polygon_xy:
        verts.append([x, y, z0])           # anillo inferior
    for x, y in polygon_xy:
        verts.append([x, y, z0 + height])  # anillo superior
    V = np.array(verts, dtype=np.float32)

    faces, f2g_list = [], []
    # Floor (g0): fan desde vértice 0
    for i in range(1, N-1):
        faces.append([0, i+1, i]); f2g_list.append(0)
    # Ceiling (g1): fan desde vértice N
    for i in range(1, N-1):
        faces.append([N, N+i, N+i+1]); f2g_list.append(1)
    # Walls (g2..g(N+1)): 2 tris por arista
    for i in range(N):
        j = (i+1) % N
        faces.append([i, j, N+j]); f2g_list.append(2+i)
        faces.append([i, N+j, N+i]); f2g_list.append(2+i)

    group_order = ["Floor","Ceiling"] + [f"Wall {i+1}" for i in range(N)] + ["Unassigned"]
    pivot = [float(np.mean([p[0] for p in polygon_xy])),
             float(np.mean([p[1] for p in polygon_xy])),
             z0 + height/2]
    return V, np.array(faces, np.int32), np.array(f2g_list, np.int32), pivot, group_order
```

### Patrones de diseño para control rooms

> **Sólo si el usuario no da medidas o pide paredes inclinadas.** Con
> medidas dadas («un control room de 3x4x3»), el recinto es el rectángulo
> de esas medidas (§52.1). Un quiebre de 10 cm en las laterales no cambia
> la acústica y sí agranda la planta.

```
Convención: X = profundidad (front→back), Y = ancho (izq→der)

Front wall en V (soffit de monitores):
    (-3.3, -2.5) → (-3.4, 0.0) → (-3.3, 2.5)
    El centro (X=-3.4) es más profundo → crea un soffit natural.

Laterales splayed (anti flutter echo):
    Quiebre a ~1/3 de profundidad (en X).
    Ejemplo: se abren de Y=±2.50 a Y=±2.75 y luego cierran a Y=±2.40.

Back wall más ancho (splayed):
    (3.3, ±2.5) → el back wall es ~5.0m (Y) — más ancho que el frente (~3.2m).
    El splay abre de frente a fondo para mejor imagen estéreo y RFZ.
```

### Polígonos de herradura (teatros/ópera)

La herradura se abre desde la embocadura (escenario en −X) hacia la audiencia (+X),
con máximo ancho en la zona media y cierre curvo en el fondo (+X).

**Regla:** El escenario está en −X (frente angosto). La herradura se ensancha hacia +X
y se cierra con una curva en el fondo (+X). **Nunca invertir la curva.**

```
# Teatro en herradura ~34×24m, 18m de alto
# Escenario en −X, audiencia en +X, herradura cierra en +X
# Vértices CCW vistos desde arriba

"polygon_xy": [
    [-17.0, -8.0],   # embocadura izq (escenario)
    [-17.0,  8.0],   # embocadura der (escenario)
    [-12.0, 11.0],   # lateral se abre
    [ -5.0, 12.0],   # máximo ancho
    [  3.0, 11.5],   # comienza cierre
    [  9.0, 10.0],   # herradura cierra
    [ 14.0,  7.0],   # curva fondo
    [ 16.0,  3.0],   # curva fondo
    [ 17.0,  0.0],   # punto más profundo (fondo sala)
    [ 16.0, -3.0],   # curva fondo (simétrico)
    [ 14.0, -7.0],
    [  9.0,-10.0],
    [  3.0,-11.5],
    [ -5.0,-12.0],
    [-12.0,-11.0]
],
"height": 18.0
```

**Patrón visual (planta):**
```
  Escenario (−X)          Fondo sala (+X)
     ┌──────┐
    /        \
   /    ☆     \          ☆ = fuente (escenario)
  |   sala     )         ★ = receptor (platea)
  |    ★      /
   \        /
    \──────/
```

Puntos clave:
- Más vértices en la curva del fondo = mejor aproximación acústica
- Simetría en Y (espejo respecto a Y=0)
- El ancho máximo NO está en el fondo sino en la zona media (~X=−5)
- Para ópera/lírica: 12–20 vértices. Para abanico simple: 6–8 vértices

---

## 4. Surface maps (materiales, aislamiento, espesores)

Estos diccionarios usan la key `"OBJ_ID|GROUP_NAME"`:

### Cómo se escriben las claves (formato cookbook, desde la R437)

- **`OBJ_ID`**: el recinto es **1**; los objetos, **2, 3, …** en el orden
  en que aparecen en `objects`.
- **Recinto extrusión**: `Piso`, `Techo` y `Pared k`, con k la arista que
  va del vértice k al k+1 del `polygon`. También valen `Floor` y
  `Ceiling`, y **`Wall +X` / `Pared +X`** (y ±Y): es la pared (o las
  paredes) que mira hacia ese lado. Así se puede escribir un recinto box,
  que el asistente convierte en extrusión, sin contar aristas.
- **Objetos box**: `Piso`/`Floor`, `Techo`/`Ceiling` y `Pared ±X`/`Wall
  ±X`, `Pared ±Y`/`Wall ±Y`, con el nombre del objeto adelante o sin él:
  `"2|Panel izquierdo Pared +X"` y `"2|Pared +X"` son la misma cara.
- Vale igual para las cinco capas: `surface_group_material`,
  `surface_group_material_b`, `surface_assembly_map`,
  `surface_thickness_dir` y `surface_render_look`.
- `"Default"` o vacío no pisa nada. Si dos claves caen en la misma cara,
  manda la escrita exacta.

Hasta la R436, en el formato cookbook el asistente interno y
`/api/design` **perdían** estas capas (la de assemblies pasaba, pero sin
llevar las claves a los grupos): lo que la IA elegía para cada superficie
terminaba reemplazado por un material adivinado por el nombre del objeto
(un «Panel absorción…» quedaba de yeso pintado).

### `surface_group_material` (cara A — interior)

```json
{
  "1|Floor": "Baldosa cerámica 10 mm + underlay 20 mm (sobre hormigón)",
  "1|Ceiling": "Yeso liso pintado",
  "1|Wall +X": "Ladrillo visto (con juntas/relieve)",
  "2|Floor": "Madera maciza barnizada 9 mm (sobre rastreles)",
  "2|Ceiling": "Madera maciza barnizada 9 mm (sobre rastreles)"
}
```

### `surface_group_material_b` (cara B — exterior, solo para paredes del enclosure)

```json
{
  "1|Wall +X": "Ladrillo hueco visto",
  "1|Ceiling": "Yeso liso pintado",
  "1|Floor": "Hormigón liso"
}
```

### `surface_assembly_map` (assembly de aislamiento por superficie)

```json
{
  "1|Floor": "asm_22843",
  "1|Ceiling": "asm_90169",
  "1|Wall +X": "asm_4776"
}
```

### `surface_thickness_dir` (dirección del espesor)

```json
{
  "1|Floor": "inward",
  "1|Ceiling": "inward",
  "1|Wall +X": "inward",
  "3|Floor": "center",
  "3|Wall +X": "center"
}
```

Para el enclosure usar `"inward"`. Para objetos internos usar `"center"`.

### Ejemplo completo: Control Room con extrusión (6 paredes)

Para una extrusión con `polygon` de 6 vértices (Pared 0..5), las 3 capas de materiales quedan:

```json
"surface_group_material": {
  "1|Piso": "Alfombra ligera (sin underlay)",
  "1|Techo": "Placa de techo fibra mineral 18 mm (σ≈15k) + plenum 200 mm",
  "1|Pared 0": "Lana mineral (roca) 100 mm (pared rígida)",
  "1|Pared 1": "Panel perforado MDF t=16mm φ=5% cav=50mm",
  "1|Pared 2": "Panel perforado MDF t=16mm φ=5% cav=50mm",
  "1|Pared 3": "Cortina pesada (100% fruncido)",
  "1|Pared 4": "Lana mineral (roca) 50 mm (pared rígida)",
  "1|Pared 5": "Lana mineral (roca) 50 mm (pared rígida)"
},
"surface_group_material_b": {
  "1|Piso": "Hormigón liso",
  "1|Techo": "Hormigón liso",
  "1|Pared 0": "Pladur / placa de yeso (sobre perfilería)",
  "1|Pared 1": "Pladur / placa de yeso (sobre perfilería)",
  "1|Pared 2": "Pladur / placa de yeso (sobre perfilería)",
  "1|Pared 3": "Pladur / placa de yeso (sobre perfilería)",
  "1|Pared 4": "Pladur / placa de yeso (sobre perfilería)",
  "1|Pared 5": "Pladur / placa de yeso (sobre perfilería)"
},
"wall_assemblies": {
  "asm_pared_estudio": {
    "layers": [
      {"material_id": "gyp_125", "thickness_mm": 12.5, "bonded_with_prev": true},
      {"material_id": "mineral_wool_80", "thickness_mm": 80, "bonded_with_prev": false},
      {"material_id": "air_50", "thickness_mm": 50, "bonded_with_prev": false},
      {"material_id": "gyp_125", "thickness_mm": 12.5, "bonded_with_prev": true}
    ]
  },
  "asm_piso_flotante": {
    "layers": [
      {"material_id": "concrete_200", "thickness_mm": 200, "bonded_with_prev": true},
      {"material_id": "neoprene_25", "thickness_mm": 25, "bonded_with_prev": false},
      {"material_id": "concrete_100", "thickness_mm": 100, "bonded_with_prev": true}
    ]
  },
  "asm_techo_desacoplado": {
    "layers": [
      {"material_id": "gyp_125", "thickness_mm": 12.5, "bonded_with_prev": true},
      {"material_id": "air_200", "thickness_mm": 200, "bonded_with_prev": false},
      {"material_id": "mineral_wool_100", "thickness_mm": 100, "bonded_with_prev": false},
      {"material_id": "concrete_150", "thickness_mm": 150, "bonded_with_prev": true}
    ]
  }
},
"surface_assembly_map": {
  "1|Piso": "asm_piso_flotante",
  "1|Techo": "asm_techo_desacoplado",
  "1|Pared 0": "asm_pared_estudio",
  "1|Pared 1": "asm_pared_estudio",
  "1|Pared 2": "asm_pared_estudio",
  "1|Pared 3": "asm_pared_estudio",
  "1|Pared 4": "asm_pared_estudio",
  "1|Pared 5": "asm_pared_estudio"
}
```

> **REGLA CRÍTICA**: La IA DEBE generar las 3 capas (absorción A, absorción B, aislamiento TL) para CADA superficie del enclosure. Para objetos internos con espesor constructivo relevante (paneles acústicos, divisorios, ventanas, puertas), también asignar assemblies. Objetos simples como mesas, sofás, sillas NO necesitan assembly — solo material de absorción.

### Ejemplo assembly para objetos con espesor constructivo

```json
"surface_assembly_map": {
  "2|Ventana Pared +X": "asm_ventana"
},
"wall_assemblies": {
  "asm_ventana": {
    "layers": [
      {"material_id": "glass_6", "thickness_mm": 6, "bonded_with_prev": true},
      {"material_id": "air_12", "thickness_mm": 12, "bonded_with_prev": false},
      {"material_id": "glass_6", "thickness_mm": 6, "bonded_with_prev": true}
    ]
  }
}
```

Criterio: si el objeto tiene capas constructivas que afectan el TL (vidrio doble, panel multicapa, puerta maciza con sellos), asignar assembly. Si es un mueble sólido simple (mesa, consola, sofá), solo asignar material de absorción superficial.

---

## 5. Wall assemblies (aislamiento acústico)

```json
"wall_assemblies": {
  "asm_xxxxx": {
    "id": "asm_xxxxx",
    "name": "Pared doble ladrillo + lana",
    "layers": [
      {"material_id": "brick_solid_120", "thickness_mm": 120.0, "bonded_with_prev": true},
      {"material_id": "glass_wool_16",   "thickness_mm": 50.0,  "bonded_with_prev": false},
      {"material_id": "brick_solid_115", "thickness_mm": 115.0, "bonded_with_prev": true}
    ],
    "connection_profile": "Manual",
    "coupling": 0.2,
    "bridge_k": 0.0,
    "panel_span_x_m": 3.0,
    "panel_span_y_m": 2.8,
    "panel_boundary": "Apoyado",
    "R_curve": [],
    "Rw": null,
    "STC": null,
    "C": null,
    "Ctr": null
  }
}
```

`R_curve`, `Rw`, `STC`, `C`, `Ctr` pueden ser `[]`/`null` — el software los calcula al presionar "Calcular".

### `material_id` — IDs de materiales de aislamiento (TL)

Son IDs internos del motor de Transmission Loss. **No confundir con los nombres de materiales absorbentes.**

| Categoría | IDs disponibles |
|-----------|----------------|
| **Hormigón** | `concrete_100`, `concrete_120`, `concrete_150`, `concrete_200`, `concrete_250`, `concrete_300`, `concrete_lightweight_100`, `concrete_lightweight_150`, `concrete_lightweight_200` |
| **Ladrillo** | `brick_solid_115`, `brick_solid_120`, `brick_solid_230`, `brick_hollow`, `brick_hollow_90`, `brick_hollow_120` |
| **Bloque** | `cinder_block_190`, `aac_block_100`, `aac_block_150`, `aac_block_200`, `gypsum_block_80` |
| **Yeso/Placa** | `gyp_125`, `gyp_15`, `gyp_18`, `gyp_hd_125`, `gyp_hd_15`, `gypsum_9_5`, `gypsum_15`, `gypsum_std_10`, `gypsum_hd_10`, `gypsum_hd_13` |
| **Vidrio** | `glass_4`, `glass_5`, `glass_6`, `glass_8`, `glass_10`, `glass_lam_6_4`, `glass_lam_8_8`, `glass_lam_12_8`, `glass_laminated_4_4`, `glass_laminated_6_6` |
| **Madera** | `plywood_9`, `plywood_12`, `plywood_15`, `plywood_18`, `mdf_12`, `mdf_16`, `mdf_18`, `mdf_19`, `mdf_25`, `osb_11`, `osb_15`, `osb_18`, `chipboard_16`, `clt_100`, `clt_120`, `clt_160`, `clt_200` |
| **Metal** | `steel_sheet_0_5`, `steel_sheet_0_7`, `steel_sheet_1`, `steel_sheet_1_5`, `steel_sheet_2`, `aluminium_1`, `aluminium_2`, `aluminium_3`, `copper_1`, `copper_2` |
| **Absorbente poroso** | `mineral_wool`, `mineral_wool_50`, `mineral_wool_80`, `glass_wool_16`, `glass_wool_24`, `acoustic_foam_25`, `polyester_fiber_30`, `lana_roca_40`, `lana_roca_60`, `lana_roca_80`, `lana_roca_120`, `lana_vidrio_16`, `lana_vidrio_32`, `lana_vidrio_48`, `poliester_20`, `espuma_melamina_10`, `celulosa_insuflada_45` |
| **Aire (cavidad)** | `air`, `air_10`, `air_20`, `air_40`, `air_60`, `air_80`, `air_100`, `air_thin` (25mm), `air_large` (150mm) |
| **Otros** | `fibrocemento_6`, `fibrocemento_10`, `cement_board_12`, `eps_20`, `cellulose_45`, `corcho_3`, `polietileno_foam_5`, `rubber_mat_5` |
| **Membrana** | `vinyl_barrier_2`, `vinyl_barrier_4`, `vinyl_barrier_6`, `vinyl_barrier_8`, `heavy_membrane_3`, `heavy_membrane_5`, `heavy_membrane_7`, `heavy_membrane_10`, `plomo_1` |

### Materiales de aislamiento validados agregados en v25

Estos 53 IDs se suman a la tabla anterior (todos los IDs previos siguen válidos). Provienen del motor validado contra laboratorio; en conflictos de nombre con IDs previos, los valores validados son los que usa el motor.

| Categoría | IDs disponibles (v25) |
|-----------|----------------------|
| **Mampostería** | `aac_100`, `aac_150`, `brick_hollow_double_240`, `brick_masonry_solid`, `brick_partition_70`, `brick_perforated_240`, `ceb_earth`, `clay_tile_hollow`, `concrete`, `concrete_block_filled_200`, `concrete_block_solid_200`, `concrete_reinforced_2500`, `lightweight_concrete_150`, `plaster_render`, `stone_masonry`, `thermal_clay_240`, `weber_screed_40` |
| **Panel** | `aluminum_sheet_1`, `calcium_silicate_12`, `clt_finland_slab`, `cork_board_20`, `fibercement_8`, `glass_mono_12`, `gyproc_gl15`, `gyproc_gn13`, `gypsum_13_typex`, `gypsum_16_typex`, `gypsum_fireX_15`, `hardboard_6`, `knauf_danogips_a13`, `kronofloor_laminate_8`, `pmma_10`, `polycarbonate_6`, `steel_sheet_1_0`, `steel_sheet_2_0` |
| **Absorbente poroso** | `expanded_cork_120`, `glass_fibre_batt`, `glasswool_32`, `hemp_40`, `isover_acoustic_10`, `melamine_foam_10`, `mineral_fibre_batt`, `pur_spray_40`, `rockwool_100`, `sheep_wool_25`, `textile_felt_20`, `woodfiber_50` |
| **Membrana** | `asphalt_membrane_3`, `bitumen_membrane_4`, `epdm_15`, `lead_sheet_1`, `mlv_10`, `recycled_rubber_6` |

### `bonded_with_prev`

- `true`: La capa está pegada/adherida a la anterior (misma hoja, revoque sobre mampostería)
- `false`: Hay separación mecánica (cámara de aire, montantes resilientes, capas desacopladas)

La primera capa siempre es `true`.

### Presets de assemblies comunes

```
Pared simple hormigón:     [{concrete_200, 200, bonded:true}]
Pared simple ladrillo:     [{brick_solid_120, 120, bonded:true}]
Pared doble + lana:        [{brick_solid_120, 120, T}, {glass_wool_16, 50, F}, {brick_solid_115, 115, T}]
Tabique yeso W111:         [{gyp_125, 12.5, T}, {air, 70, F}, {mineral_wool_50, 50, F}, {gyp_125, 12.5, T}]
Tabique yeso W112 doble:   [{gyp_125, 25, T}, {air, 70, F}, {mineral_wool_50, 50, F}, {gyp_125, 25, T}]
Piso: losa hormigón:       [{concrete_200, 200, bonded:true}]
Techo: losa + cielorraso:  [{gyp_125, 12.5, T}, {air, 90, F}, {mineral_wool_80, 80, F}, {gyp_125, 12.5, T}]
DVH vidrio:                [{glass_4, 4, T}, {air, 12, F}, {glass_4, 4, T}]
```

---

## 5b. Motor de aislamiento validado (TMM) y opciones avanzadas (v25)

CADSFS calcula el aislamiento con el **motor TMM validado** (matriz de transferencia con
Delany-Bazley para porosos, puentes estructurales por perfil de conexión, y cotas físicas),
contrastado contra 80 construcciones medidas en laboratorios independientes. **Es el motor por
defecto**; no hace falta elegirlo.

### Campos opcionales de assembly (todos con default; el motor tolera su ausencia)

| Clave | Tipo | Significado |
|---|---|---|
| `engine` | string | `"tmm"` (por defecto, recomendado) o `"heuristico"` |
| `studs_spacing_mm` | number | Espaciamiento de montantes/conexiones (mm); afecta el puente en TMM. Default 600 |
| `connection_profile` | string | (ya existía) `"Montantes metálicos"`, `"Amarres metálicos (cavidad)"`, `"Montantes madera"`, `"Canal resiliente"`, `"Clips resilientes"`, `"Desacoplado ideal"`, `"Manual"` |
| `flanking_scenario` | string | Escenario de flancos ISO 12354-1 para R'w (aparente) |

### Excitación por impacto (pisos / forjados)

Para forjados se calcula el **ruido de impacto** (Ln,w, IIC) y, con el volumen del recinto,
L'nT,w. La excitación de impacto es contextual al elemento (solo pisos).

| Clave | Tipo | Significado |
|---|---|---|
| `compute_impact` | bool | Habilita el cálculo de Ln,w del forjado |
| `floating_f0_hz` | number | Resonancia del suelo flotante (Hz), si hay |
| `covering_delta_lw_db` | number | Mejora del revestimiento sobre Ln,w (dB): laminado≈20, vinilo≈15, moqueta≈25 |
| `floating_s_prime_mn_m3` | number | Rigidez dinámica de la banda resiliente (MN/m³) |
| `floating_mass_kg_m2` | number | Masa de la capa flotante (kg/m²) |
| `ceiling_mass_kg_m2` / `ceiling_cavity_mm` | number | Falso techo suspendido (masa y cámara) |

### Excitación por lluvia (cubiertas / claraboyas)

Para cubiertas o claraboyas livianas expuestas, se estima el nivel de ruido de lluvia radiado
al interior desde la masa y el amortiguamiento del elemento. Se dispara desde la pestaña
Aislamiento (no requiere campo en el JSON). Intensidades: `ligera`, `moderada`, `fuerte`,
`intensa`, `tromba`.

### Descriptores in situ (DnT,w / L'nT,w)

Con la geometría del recinto receptor se obtienen los descriptores que usan los reglamentos:

| Clave | Tipo | Significado |
|---|---|---|
| `room_volume_m3` | number | Volumen del recinto receptor → DnT,w y L'nT,w |
| `element_area_m2` | number | Área del elemento separador → DnT,w |

- **DnT,w** = R'w + 10·log₁₀(0,32·V/S)
- **L'nT,w** = Ln,w − 10·log₁₀(0,032·V)

### Reglas para la IA

- El motor por defecto es **TMM**; no pongas `engine` salvo que quieras el heurístico.
- Para **pisos/forjados entre unidades**, poné `compute_impact: true` — así el Modo Arquitecto
  verifica IIC / L'nT,w (antes quedaban "No verificable").
- Para **cubiertas/claraboyas livianas** expuestas, la lluvia se calcula desde la masa del
  elemento (excitación contextual, solo techos/cubiertas).
- Dá `room_volume_m3` (y `element_area_m2` para aéreo) cuando quieras los descriptores de campo.
- **Todos los IDs de material previos siguen válidos**; sumá los 53 nuevos si aplica. Las
  cavidades de aire (`air`, `air_NN`) resuelven por espesor aunque el ID exacto no esté tabulado.
- La excitación aérea / de impacto / de lluvia es un paradigma distinto del emisor/receptor de
  sala: actúa sobre un **elemento constructivo**, no sobre una fuente puntual en el recinto.

---

## 29. Ejemplos completos de asignación de materiales por tipo de recinto

> Estos ejemplos son **copy-paste-ready**: los nombres de materiales son exactos de la DB interna de 2665 entradas. Si la IA genera un proyecto, la sección `surface_group_material` DEBE verse como uno de estos ejemplos (adaptado a la cantidad de paredes del polígono).

### 29.1 Estudio — Control Room (extrusión 6 paredes, con ventana y puerta)

```json
"surface_group_material": {
  "1|Piso":       "Alfombra ligera (sin underlay)",
  "1|Techo":      "Placa de techo fibra mineral 18 mm (σ≈15k) + plenum 200 mm",
  "1|Pared 0":    "Lana mineral (roca) 50 mm (pared rígida)",
  "1|Pared 1":    "Panel textil tensado con cámara 50 mm (sin relleno)",
  "1|Pared 2":    "Panel textil tensado con cámara 50 mm (sin relleno)",
  "1|Pared 3":    "Panel perforado MDF t=16mm φ=5% cav=50mm + lana 25mm",
  "1|Pared 4":    "Panel textil tensado con cámara 50 mm (sin relleno)",
  "1|Pared 5":    "Panel textil tensado con cámara 50 mm (sin relleno)",
  "1|Ventana CR-LR": "Vidrio (ventana)",
  "1|Puerta entrada": "Madera maciza barnizada (panel)",
  "2|Bass trap NE Piso":  "Lana mineral (roca) 100 mm (pared rígida)",
  "2|Bass trap NE Techo": "Lana mineral (roca) 100 mm (pared rígida)",
  "2|Bass trap NE Pared +X": "Lana mineral (roca) 100 mm (pared rígida)",
  "2|Bass trap NE Pared +Y": "Lana mineral (roca) 100 mm (pared rígida)",
  "2|Bass trap NE Pared -X": "Lana mineral (roca) 100 mm (pared rígida)",
  "2|Bass trap NE Pared -Y": "Lana mineral (roca) 100 mm (pared rígida)",
  "3|Cloud techo Piso":  "Lana mineral (roca) 50 mm (pared rígida)",
  "3|Cloud techo Techo": "Lana mineral (roca) 50 mm (pared rígida)",
  "3|Cloud techo Pared +X": "Lana mineral (roca) 50 mm (pared rígida)",
  "3|Cloud techo Pared +Y": "Lana mineral (roca) 50 mm (pared rígida)",
  "3|Cloud techo Pared -X": "Lana mineral (roca) 50 mm (pared rígida)",
  "3|Cloud techo Pared -Y": "Lana mineral (roca) 50 mm (pared rígida)"
},
"surface_group_material_b": {
  "1|Piso":    "Hormigón liso",
  "1|Techo":   "Hormigón liso",
  "1|Pared 0": "Ladrillo visto",
  "1|Pared 1": "Ladrillo visto",
  "1|Pared 2": "Ladrillo visto",
  "1|Pared 3": "Ladrillo visto",
  "1|Pared 4": "Ladrillo visto",
  "1|Pared 5": "Ladrillo visto"
}
```

**Notas**: las keys `1|Ventana CR-LR` y `1|Puerta entrada` corresponden a aberturas (openings) del enclosure — CADSFS las agrega automáticamente al group_order cuando reconstruye el mesh. Las keys de objetos internos (bass traps, cloud) usan el obj_id como prefijo.

Con el polígono de §28.7: `Pared 0` es el frente (con la ventana), `Pared 1` y `Pared 5` los
quiebres del frente, `Pared 2` y `Pared 4` las laterales, `Pared 3` el fondo (con la puerta).
Las laterales y los quiebres, **de a pares con el mismo material** (A7); la pared con la
ventana y la pared con la puerta, **con el material de su tipo**: la abertura tiene el suyo.
Hasta la v43 este ejemplo hacía de vidrio la pared entera del fondo y tenía las dos laterales
distintas.

Este juego es para cuando el tratamiento lo hacen las superficies del recinto. **Si el
tratamiento va en objetos** (paneles, trampas, nube, difusores: lo que pide §26.2), las
superficies del recinto van reflectantes: placa de yeso, parquet y el frente con lana. Así
lo hace §52.5. Con este juego y los objetos de §52.5 la sala queda muerta: Tm de 0,17 s por
Sabine.

### 29.2 Teatro / Ópera (extrusión rectangular 4 paredes, con 6 puertas)

```json
"surface_group_material": {
  "1|Piso":       "Parquet de madera barnizado",
  "1|Techo":      "Yeso liso pintado",
  "1|Pared 0":    "Madera maciza barnizada (panel)",
  "1|Pared 1":    "Yeso liso pintado",
  "1|Pared 2":    "Cortina pesada (100% fruncido)",
  "1|Pared 3":    "Yeso liso pintado",
  "1|Puerta L1":  "Madera maciza barnizada (panel)",
  "1|Puerta L2":  "Madera maciza barnizada (panel)",
  "1|Puerta L3":  "Madera maciza barnizada (panel)",
  "1|Puerta R1":  "Madera maciza barnizada (panel)",
  "1|Puerta R2":  "Madera maciza barnizada (panel)",
  "1|Puerta R3":  "Madera maciza barnizada (panel)",
  "2|Escenario Piso":     "Parquet de madera barnizado",
  "2|Escenario Techo":    "Madera maciza barnizada (panel)",
  "2|Escenario Pared +X": "Madera maciza barnizada (panel)",
  "2|Escenario Pared -X": "Madera maciza barnizada (panel)",
  "2|Escenario Pared +Y": "Madera maciza barnizada (panel)",
  "2|Escenario Pared -Y": "Madera maciza barnizada (panel)",
  "3|Butacas platea Piso":     "Butaca tapizada (ocupada)",
  "3|Butacas platea Techo":    "Butaca tapizada (ocupada)",
  "3|Butacas platea Pared +X": "Butaca tapizada (ocupada)",
  "3|Butacas platea Pared -X": "Butaca tapizada (ocupada)",
  "3|Butacas platea Pared +Y": "Butaca tapizada (ocupada)",
  "3|Butacas platea Pared -Y": "Butaca tapizada (ocupada)"
},
"surface_group_material_b": {
  "1|Piso":    "Hormigón liso",
  "1|Techo":   "Hormigón liso",
  "1|Pared 0": "Ladrillo visto",
  "1|Pared 1": "Ladrillo visto",
  "1|Pared 2": "Ladrillo visto",
  "1|Pared 3": "Ladrillo visto"
}
```

**Notas**: las keys `1|Puerta L1` etc. son las aberturas del enclosure. Las butacas como objeto interno con material `Butaca tapizada (ocupada)` tienen α alto en mid/high → controlan el RT60 correctamente. Para ópera target RT60=1.2-1.6s, para sinfónica 1.8-2.2s — ajustar proporción butacas/madera/yeso.

### 29.3 Venue amplificado (extrusión rectangular 4 paredes)

```json
"surface_group_material": {
  "1|Piso":    "Hormigón pulido (microrelieve)",
  "1|Techo":   "Acero pintado / chapa",
  "1|Pared 0": "Hormigón rugoso / encofrado",
  "1|Pared 1": "Ladrillo visto",
  "1|Pared 2": "Ladrillo visto (con juntas/relieve)",
  "1|Pared 3": "Ladrillo visto",
  "2|Escenario Piso":     "Parquet de madera barnizado",
  "2|Escenario Techo":    "Madera maciza barnizada (panel)",
  "2|Escenario Pared +X": "Madera maciza barnizada (panel)",
  "2|Escenario Pared -X": "Madera maciza barnizada (panel)",
  "2|Escenario Pared +Y": "Madera maciza barnizada (panel)",
  "2|Escenario Pared -Y": "Madera maciza barnizada (panel)",
  "3|Barra bar Piso":   "Acero pintado / chapa",
  "3|Barra bar Techo":  "Acero pintado / chapa",
  "3|Barra bar Pared +X": "Acero pintado / chapa",
  "3|Barra bar Pared -X": "Acero pintado / chapa",
  "3|Barra bar Pared +Y": "Acero pintado / chapa",
  "3|Barra bar Pared -Y": "Acero pintado / chapa"
},
"surface_group_material_b": {
  "1|Piso":    "Hormigón liso",
  "1|Techo":   "Acero pintado / chapa",
  "1|Pared 0": "Hormigón liso",
  "1|Pared 1": "Ladrillo visto",
  "1|Pared 2": "Ladrillo visto",
  "1|Pared 3": "Ladrillo visto"
}
```

### 29.4 Cine / Home Theater (extrusión rectangular 4 paredes)

```json
"surface_group_material": {
  "1|Piso":    "Alfombra ligera (sin underlay)",
  "1|Techo":   "Placa de techo fibra mineral 20 mm (σ≈8k) + plenum 200 mm",
  "1|Pared 0": "Cortina pesada (100% fruncido)",
  "1|Pared 1": "Cortina pesada (100% fruncido)",
  "1|Pared 2": "Cortina pesada (100% fruncido)",
  "1|Pared 3": "Cortina pesada (100% fruncido)",
  "2|Pantalla Piso":     "Cortina pesada (100% fruncido)",
  "2|Pantalla Techo":    "Cortina pesada (100% fruncido)",
  "2|Pantalla Pared +X": "Cortina pesada (100% fruncido)",
  "2|Pantalla Pared -X": "Cortina pesada (100% fruncido)",
  "2|Pantalla Pared +Y": "Cortina pesada (100% fruncido)",
  "2|Pantalla Pared -Y": "Cortina pesada (100% fruncido)",
  "3|Butacas Piso":     "Butaca tapizada (ocupada)",
  "3|Butacas Techo":    "Butaca tapizada (ocupada)",
  "3|Butacas Pared +X": "Butaca tapizada (ocupada)",
  "3|Butacas Pared -X": "Butaca tapizada (ocupada)",
  "3|Butacas Pared +Y": "Butaca tapizada (ocupada)",
  "3|Butacas Pared -Y": "Butaca tapizada (ocupada)"
},
"surface_group_material_b": {
  "1|Piso":    "Hormigón liso",
  "1|Techo":   "Hormigón liso",
  "1|Pared 0": "Hormigón liso",
  "1|Pared 1": "Hormigón liso",
  "1|Pared 2": "Hormigón liso",
  "1|Pared 3": "Hormigón liso"
}
```

### 29.5 Regla de oro

> **Si la IA genera un surface_group_material y la palabra "Default" aparece en CUALQUIER valor, el proyecto está MAL.** Volver a §2 y asignar el material real correspondiente al tipo de recinto.

---

## 6. Speaker systems

### Array colgado (line array) — GEOMETRÍA OBLIGATORIA

```json
{
  "name": "Array colgado (8×d&b V8) [L]",
  "mount": "flying",
  "elements": [
    {"name": "LA 1", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.50, -3.5, 7.80], "yaw_deg": 0.0, "pitch_deg": 0.0, "channel": "L"},
    {"name": "LA 2", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.50, -3.5, 7.49], "yaw_deg": 0.0, "pitch_deg": 0.0, "channel": "L"},
    {"name": "LA 3", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.50, -3.5, 7.18], "yaw_deg": 0.0, "pitch_deg": 0.0, "channel": "L"},
    {"name": "LA 4", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.49, -3.5, 6.87], "yaw_deg": 0.0, "pitch_deg": 2.0, "channel": "L"},
    {"name": "LA 5", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.47, -3.5, 6.56], "yaw_deg": 0.0, "pitch_deg": 5.0, "channel": "L"},
    {"name": "LA 6", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.43, -3.5, 6.26], "yaw_deg": 0.0, "pitch_deg": 9.0, "channel": "L"},
    {"name": "LA 7", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.36, -3.5, 5.97], "yaw_deg": 0.0, "pitch_deg": 14.0, "channel": "L"},
    {"name": "LA 8", "model_id": "db_v8", "spl_db": 108.99, "polar": "LineArray",
     "pos": [-1.27, -3.5, 5.69], "yaw_deg": 0.0, "pitch_deg": 19.0, "channel": "L"}
  ]
}
```

**Reglas físicas de arrays colgados (CRÍTICO)**:

1. **pitch SIEMPRE crece de arriba a abajo**: LA 1 (arriba, rigging) tiene pitch ≈ 0°. LA N (abajo) tiene el pitch más alto. NUNCA hacer que la caja inferior apunte hacia arriba — es **físicamente imposible** en un array colgado por gravedad.

2. **Las 2-3 cajas superiores van a splay 0°** (planas, sin ángulo entre ellas). Esto forma el "bloque de cabeza" que da cobertura al fondo de la sala.

3. **El splay aumenta progresivamente** a partir de la caja 3-4: típico 0°,0°,0°,2°,3°,4°,5°,5° para 8 cajas.

4. **J-curve** (cobertura trasera/balcón): SOLO las 1-2 cajas **superiores** pueden tener pitch negativo leve (-2° a -5°). Esto inclina la cabeza del array hacia arriba/atrás. Las cajas **inferiores NUNCA** tienen pitch negativo en un array colgado.

5. **Pitch acumulativo** = suma de splays desde la caja 1. Ejemplo: splays=[0,0,0,2,3,4,5,5] → pitch=[0,0,0,2,5,9,14,19].

6. **Posiciones X/Z**: cada caja se desplaza ligeramente hacia atrás (-X) y abajo (-Z) por el splay. Para un array real, el software calcula esto con hinge-chain; para el JSON generado por IA, basta con estimar posiciones incrementales.

**Array stackeado**: `mount: "stacked"`. La caja 1 es la inferior (sobre el sub/piso). El pitch va de 0° a negativo (apuntando hacia arriba). Ejemplo 4 cajas: pitch=[0,-2,-5,-8].

**`mount`**: `"flying"` (colgado) o `"stacked"`. NUNCA usar `"sub_array"` para line arrays.

**`yaw_deg`**: Rotación horizontal. `0° = +X`, `90° = +Y`. Ambos lados L y R tienen el mismo yaw apuntando hacia la audiencia.

**`channel`**: `"L"`, `"R"`, o `"M"` (mono). Cada lado L y R es un speaker_system separado.

### Arreglo de subs (REGLA CRÍTICA)

> ⚠ **ORIENTACIÓN — error frecuente:** los subs deben apuntar al MISMO lado que el PA: hacia la audiencia (`yaw_deg: 90`), sin ángulo lateral. Dejar los subs en `yaw_deg: 0` es un ERROR (quedan apuntando a +Y, al costado). Salvo configuración cardioide/end-fire (donde un sub trasero va a 270°), TODOS los subs van con el mismo `yaw_deg: 90` que el PA principal.

**Campos obligatorios del sistema**: `mount: "sub_array"`, `channel`, `sub_decoupling`.

**Campos obligatorios por elemento**: `sub_orientation: "upright"` (o `"on_side"`), `channel`.

**`sub_decoupling`**: `"direct"` (sobre losa), `"isolators"`, `"floating"`, `"flown"`.

**Posición Z de subs**: `z = altura_sub / 2.0` (centro del gabinete).

NUNCA mezclar subs con line arrays en el mismo speaker_system.

#### Preset A — Stereo L/R (2 stacks)

Dos pilas de 2 subs, una a cada lado del escenario. 2 sistemas separados.

```json
{"name": "Subs L", "mount": "sub_array", "sub_decoupling": "direct",
 "elements": [
   {"name": "SUB L1", "model_id": "lacoustics_ks28", "pos": [-1.0, -4.0, 0.275], "yaw_deg": 0.0, "sub_orientation": "upright", "channel": "L"},
   {"name": "SUB L2", "model_id": "lacoustics_ks28", "pos": [-1.0, -4.0, 0.825], "yaw_deg": 0.0, "sub_orientation": "upright", "channel": "L"}
]}
```

#### Preset B — Mono central (2-4 subs apilados)

Todos centrados debajo del escenario. 1 sistema, channel "M".

```json
{"name": "Subs Mono", "mount": "sub_array", "sub_decoupling": "direct",
 "elements": [
   {"name": "SUB 1", "model_id": "db_v_sub", "pos": [-1.0, 0.0, 0.303], "yaw_deg": 0.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 2", "model_id": "db_v_sub", "pos": [-1.0, 0.0, 0.909], "yaw_deg": 0.0, "sub_orientation": "upright", "channel": "M"}
]}
```

#### Preset C — Cardioide 2+1 (cancelación trasera) — 2 front + 1 rear

2 cajas al frente + 1 caja invertida detrás. Rechaza energía hacia el escenario (−X) manteniendo el lóbulo hacia la audiencia (+X). La caja trasera va girada 180° (`yaw_deg: 270`), con `polarity: -1` y un delay igual al **tiempo de vuelo del offset físico frente↔trasero**.

> **REGLA DEL DELAY (crítica):** `delay_ms = offset_m / 343.0 × 1000`, donde `offset_m` es la distancia **real** en X entre las cajas frontales y la trasera. Aquí las frontales están en X=−1.0 y la trasera en X=−1.72 → offset = **0.72 m** → delay = **2.1 ms** (NO 5.8 ms). Un delay demasiado grande degrada el rechazo y, por encima de ~80 Hz, **invierte el lóbulo hacia el escenario**. Con 2.1 ms el rechazo frontal/trasero es **+7.3 dB a 63 Hz** y crece de forma monótona en toda la banda de subs; con el viejo 5.8 ms caía a +2.9 dB y se volvía **negativo (−2.9 dB) a 100 Hz**.

```json
{"name": "Subs Cardioide 2+1", "mount": "sub_array", "sub_decoupling": "coupled",
 "elements": [
   {"name": "SUB F1", "model_id": "lacoustics_ks28", "pos": [-1.0, -0.67, 0.275], "yaw_deg": 0.0, "delay_ms": 0.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB F2", "model_id": "lacoustics_ks28", "pos": [-1.0,  0.67, 0.275], "yaw_deg": 0.0, "delay_ms": 0.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB R1", "model_id": "lacoustics_ks28", "pos": [-1.72, 0.0, 0.275], "yaw_deg": 270.0, "delay_ms": 2.1, "polarity": -1, "sub_orientation": "upright", "channel": "M"}
]}
```

> El nombre del preset en la app es **"Cardioide 2+1 (cancelación trasera)"** (antes rotulado con marca comercial; el `model_id` sigue siendo el parlante real).

#### Preset C+ — Cardioide 3+1 (cancelación trasera) — 3 front + 1 rear

Variante de **máximo SPL frontal**: 3 cajas acopladas al frente (≈ +9.5 dB sobre una caja) + 1 caja invertida detrás. Da un poco menos de rechazo trasero que el 2+1 (más energía frontal domina el balance), pero mantiene el lóbulo firmemente en la audiencia. Rechazo frontal/trasero **+4.2 dB a 63 Hz** (promedio de banda +3.8 dB), siempre hacia +X. Las 3 frontales van lado a lado en Y separadas por el ancho de caja (KS28 ≈ 1.34 m → separación 1.35 m para no solaparse); la trasera, offset 0.72 m en X, `polarity: -1`, delay 2.1 ms.

```json
{"name": "Subs Cardioide 3+1", "mount": "sub_array", "sub_decoupling": "coupled",
 "elements": [
   {"name": "SUB F1", "model_id": "lacoustics_ks28", "pos": [-1.0, -1.35, 0.275], "yaw_deg": 0.0, "delay_ms": 0.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB F2", "model_id": "lacoustics_ks28", "pos": [-1.0,  0.0,  0.275], "yaw_deg": 0.0, "delay_ms": 0.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB F3", "model_id": "lacoustics_ks28", "pos": [-1.0,  1.35, 0.275], "yaw_deg": 0.0, "delay_ms": 0.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB R1", "model_id": "lacoustics_ks28", "pos": [-1.72, 0.0, 0.275], "yaw_deg": 270.0, "delay_ms": 2.1, "polarity": -1, "sub_orientation": "upright", "channel": "M"}
]}
```

> Nombre en la app: **"Cardioide 3+1 (cancelación trasera)"**. Elegí 2+1 cuando importa el silencio en el escenario; 3+1 cuando importa el nivel en la audiencia. En cajas reales la directividad del gabinete mejora algo el rechazo respecto de este modelo idealizado de fuente puntual.

#### Preset D — End-fire (delay progresivo) — máximo rechazo trasero

Subs en **línea sobre el eje X** (mismo Y), separados por la profundidad de la caja. La cancelación end-fire es un fenómeno de interferencia: para que los frentes de onda se sumen hacia la audiencia (+X) y se cancelen hacia el escenario (−X), **la caja del FONDO (la más lejana de la audiencia, X más negativo) dispara PRIMERO (delay 0)** y cada caja hacia el frente suma un tiempo de vuelo de caja, de modo que **la caja del FRENTE (más cerca de la audiencia) tiene el delay MÁXIMO**.

> **⚠ ERROR DE v25 (corregido):** la rampa estaba **invertida** — la caja del frente tenía delay 0 y la del fondo el máximo. Eso hace que el arreglo dispare hacia el **ESCENARIO** (lóbulo a 179°, F/B = −14.4 dB a 63 Hz). La regla correcta: **el delay CRECE hacia la audiencia (+X)**; el fondo dispara primero. Así corregido: lóbulo a 1° (audiencia), **F/B = +14.4 dB a 63 Hz**.

```json
{"name": "Subs End-Fire", "mount": "sub_array", "sub_decoupling": "coupled",
 "elements": [
   {"name": "SUB 1", "model_id": "jbl_vtx_b18", "pos": [-2.725, 0.0, 0.21], "yaw_deg": 0.0, "delay_ms": 0.0,  "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 2", "model_id": "jbl_vtx_b18", "pos": [-2.15,  0.0, 0.21], "yaw_deg": 0.0, "delay_ms": 1.68, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 3", "model_id": "jbl_vtx_b18", "pos": [-1.575, 0.0, 0.21], "yaw_deg": 0.0, "delay_ms": 3.35, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 4", "model_id": "jbl_vtx_b18", "pos": [-1.0,   0.0, 0.21], "yaw_deg": 0.0, "delay_ms": 5.03, "sub_orientation": "upright", "channel": "M"}
]}
```

**SUB 1 es la del FONDO** (X=−2.725, más lejos de la audiencia, dispara primero); **SUB 4 es la del FRENTE** (X=−1.0, más cerca de la audiencia, delay máximo). Fórmula: `delay_ms = (distancia_al_sub_del_fondo_m / 343.0) × 1000`. Para JBL VTX B18 (depth = 0.575 m, separación 0.575 m): 0 / 1.68 / 3.35 / 5.03 ms. Todos con `yaw_deg: 90` (miran a la audiencia); no hay caja invertida en end-fire.

#### Preset E — Arco (3-6 subs curvados)

Subs en semicírculo, los externos rotados hacia adentro. Buenos para salas anchas.

```json
{"name": "Subs Arco", "mount": "sub_array", "sub_decoupling": "coupled",
 "elements": [
   {"name": "SUB 1", "model_id": "db_v_sub", "pos": [-1.0, -2.0, 0.303], "yaw_deg": 110.0, "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 2", "model_id": "db_v_sub", "pos": [-1.0, -0.7, 0.303], "yaw_deg": 95.0,  "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 3", "model_id": "db_v_sub", "pos": [-1.0,  0.7, 0.303], "yaw_deg": 85.0,  "sub_orientation": "upright", "channel": "M"},
   {"name": "SUB 4", "model_id": "db_v_sub", "pos": [-1.0,  2.0, 0.303], "yaw_deg": 70.0,  "sub_orientation": "upright", "channel": "M"}
]}
```

**Polaridad invertida** (para cardioid): `"polarity": -1` + `yaw_deg` rotado 180° respecto a los frontales (la caja trasera mira al escenario, `yaw_deg: 270`) + **delay = offset físico / 343 × 1000 ms** (típicamente 2.1 ms para un offset de una profundidad de caja, ~0.72 m). Nunca uses un delay "de catálogo" sin verificar el offset real: en cardioide, delay de más **invierte el lóbulo**; en end-fire, la rampa al revés **dispara al escenario**.

### Sistema surround / inmersivo (REGLAS CRÍTICAS)

Ver **§18** para la referencia completa. Reglas que la IA DEBE seguir:

**REGLA 1 — UN solo sistema**: Un arreglo surround/inmersivo es **UN solo `speaker_systems` entry** con `mount: "surround"`. NUNCA dividir en múltiples sistemas (Front, Surrounds, Height, LFE separados). Todos los canales van como `elements` del mismo sistema.

**REGLA 2 — Canales ITU obligatorios**: Cada elemento DEBE tener el código de canal ITU correcto. NUNCA usar solo `"L"` y `"R"` para surrounds.

| Capa | Canales (en orden) |
|------|-------------------|
| Ear level | `L`, `R`, `C`, `LFE`, `Ls`, `Rs` (5.1) |
| Ear level ext. | + `Lss`, `Rss`, `Lrs`, `Rrs` (7.1) |
| Height | `Ltf`, `Rtf`, `Ltr`, `Rtr` (7.1.4) |
| Height ext. | + `Lts`, `Rts` (9.1.6) |

**REGLA 3 — Proyecto**: OBLIGATORIO setear a nivel proyecto:
```json
{
  "surround_mode": true,
  "surround_format": "7.1.4"
}
```

**REGLA 4 — Parlantes NO son objetos**: Los parlantes van SOLO en `speaker_systems`. Ver §3 regla crítica.

**Ejemplo correcto** (resumen):
```json
{
  "name": "Surround 7.1.4 Dolby Atmos (12 spk)",
  "mount": "surround",
  "surround_format": "7.1.4",
  "elements": [
    {"channel": "L",   "pos": [...], "model_id": "...", ...},
    {"channel": "R",   "pos": [...], ...},
    {"channel": "C",   "pos": [...], ...},
    {"channel": "LFE", "pos": [...], ...},
    {"channel": "Lss", "pos": [...], ...},
    {"channel": "Rss", "pos": [...], ...},
    {"channel": "Lrs", "pos": [...], ...},
    {"channel": "Rrs", "pos": [...], ...},
    {"channel": "Ltf", "pos": [...], ...},
    {"channel": "Rtf", "pos": [...], ...},
    {"channel": "Ltr", "pos": [...], ...},
    {"channel": "Rtr", "pos": [...], ...}
  ],
  "pedestals": [ ... ]
}
```

### Comportamiento de los rayos de dirección

Los rayos de dirección que se dibujan en 3D y en las 4 vistas **se detienen al llegar al sweet spot** (posición del receptor). Esto permite visualizar si los parlantes están correctamente apuntados. El rayo se corta en el punto más cercano entre la primera superficie de impacto y la proyección del sweet spot sobre el eje de dirección del parlante.

### Dirección de parlantes — Escenario → Audiencia (REGLA)

Si hay escenario (`source_pos`) y audiencia (`receiver_pos`) definidos, **TODOS los parlantes del sistema principal** (L, R, C, fills) deben apuntar **DESDE source_pos HACIA receiver_pos**, independientemente de la orientación de la sala:

- Calcular `yaw_principal = atan2(receiver_y - source_y, receiver_x - source_x)` en grados
- Todos los parlantes del sistema principal usan `yaw_deg ≈ yaw_principal`
- Pitch: positivo (hacia abajo) para cubrir la audiencia desde altura
- **NUNCA** asumir que el escenario está siempre en -X — usar `source_pos`/`receiver_pos`

Ejemplos:

| source_pos | receiver_pos | yaw_principal | Orientación |
|-----------|-------------|---------------|-------------|
| [-5, 0, 1.5] | [3, 0, 1.2] | 0° | Escenario en -X (convención default) |
| [0, -5, 1.5] | [0, 3, 1.2] | 90° | Escenario en -Y |
| [5, 0, 1.5] | [-3, 0, 1.2] | 180° | Escenario en +X |

### Outfills — Cobertura lateral (REGLA)

Los outfills completan la cobertura en los **costados** que L y R no alcanzan. El ángulo entre los dos outfills debe ser **MAYOR a 90°** (abierto hacia afuera):

Reglas de outfill:
- Cada outfill se rota entre 45° y 70° hacia afuera respecto al `yaw_principal` (ver regla anterior)
- Outfill izquierdo: `yaw_deg = yaw_principal - (45° a 70°)`
- Outfill derecho: `yaw_deg = yaw_principal + (45° a 70°)`
- Si `|yaw_L - yaw_R| < 90°` → los outfills están demasiado cerrados y no cubren laterales

Ejemplos:

| yaw_principal | Outfill L | Outfill R | Ángulo | OK? |
|--------------|----------|----------|--------|-----|
| 0° | -50° | +50° | 100° | ✓ |
| 90° | 40° | 140° | 100° | ✓ |
| 0° | -20° | +20° | 40° | ✗ demasiado cerrado |

---

## 7. Ground conditions

```json
"ground_conditions": {
  "soil_type": "arcilla_media",
  "soil_vs_m_s": 200.0,
  "soil_rho_kg_m3": 1900.0,
  "soil_damping": 0.04,
  "water_table_m": 5.0,
  "foundation_type": "zapata_continua",
  "foundation_depth_m": 1.0,
  "foundation_slab_thickness_m": 0.15,
  "ground_surface": "hormigon",
  "ground_surface_alpha": 0.03,
  "floor_joint": false,
  "floor_joint_type": "none",
  "floor_joint_width_mm": 10.0
}
```

---

## 8. Posiciones de fuente y receptor

```python
# Regla: mínimo 0.5 m de distancia a cualquier superficie
# Centro de la sala = (0, 0). Escenario en −X, audiencia en +X.
# D = profundidad, W = ancho, H = alto

# Para recintos de MÚSICA (teatro, auditorio, club, arena):
source_pos   = [−D * 0.35, 0.0, 1.5]   # en el escenario (X negativo)
receiver_pos = [+D * 0.15, 0.0, 1.2]   # en la audiencia (X positivo)

# Para recintos SIN escenario (sala de conferencias, oficina, aula):
source_pos   = [−D * 0.25, 0.0, 1.5]   # frente de la sala
receiver_pos = [+D * 0.15, 0.0, 1.2]   # zona de asientos
```

Ejemplo para teatro de 20×12×8 m (X: −10 a +10, Y: −6 a +6):
- `source_pos = [-7.0, 0.0, 1.5]` → X=−7 (escenario), Y=0 (centrado), Z=1.5
- `receiver_pos = [3.0, 0.0, 1.2]` → X=+3 (audiencia), Y=0 (centrado), Z=1.2

### Regla inteligente — Posicionar desde objetos del modelo

Si el modelo tiene objetos nombrados (escenario, platea, butacas), usar sus centroides:

```python
# PREFERIDO: calcular desde el centro de los objetos creados
# 1) Buscar objeto con nombre que contenga "escenario" / "stage" / "tarima"
#    → source_pos = centroide XY de ese objeto, Z = 1.5
# 2) Buscar objeto con nombre que contenga "butaca" / "platea" / "audiencia"
#    → receiver_pos = centroide XY de ese objeto, Z = 1.2

# Ejemplo: Escenario center=[-11, 0], Platea center=[5, 0]
source_pos   = [-11.0, 0.0, 1.5]
receiver_pos = [5.0, 0.0, 1.2]
```

> ⚠ **NUNCA**: `source_pos = [0,0,1.2]` y `receiver_pos = [0,0,1.2]`. Si no sabés dónde ponerlos, usar la fórmula D×0.15/0.35 del recinto. NUNCA dejar ambos en el origen.

> **Regla para recintos de música**: la fuente omnidireccional (`source_pos`) representa la fuente sonora acústica (voz, instrumento). Debe ir **en el escenario** (X negativo). El receptor (`receiver_pos`) representa un oyente y debe ir **en la audiencia** (X positivo). Esto asegura que RT60, EDT, C80 y STI se calculen con la geometría correcta escenario→sala.

> **Regla para estudios / control rooms**: `source_pos` va cerca del frente, entre los monitores (X negativo). `receiver_pos` va en el sweet spot, al 38 % de la profundidad desde el frente: `x = −D/2 + 0.38×D`. Ejemplo para un CR de 6×4.2×3: `source_pos = [-2.5, 0.0, 1.2]`, `receiver_pos = [-0.72, 0.0, 1.2]` (hasta la v43 decía `[1.0, 0.0, 1.2]`: el 67 % de la sala, y la IA lo copiaba en salas de cualquier tamaño). **Calculalo con tu sala**; la receta completa, en §52. **NUNCA** poner ambos en el mismo punto.

> ⚠ **Error fatal**: `source_pos = [0,0,1.2]` y `receiver_pos = [0,0,1.2]` — fuente y receptor en el mismo punto invalida TODA la simulación (RT60, C80, STI, cobertura).

> **Hasta la R436** el asistente interno y `/api/design` tiraban
> `source_pos` y `receiver_pos` del formato cookbook y dejaban los dos
> en [0, 0, 1.2], el error fatal de arriba, aunque la IA los hubiera
> escrito bien. Desde la R437 se respetan. La forma vieja
> (`"source": {"pos": [...]}`) también se lee.

---

## 9. Checklist de validación (fusión §9 + §30)

> La IA DEBE ejecutar mentalmente esta checklist ANTES de devolver el JSON al usuario. Si algún punto falla, CORREGIR antes de enviar.

### 9.1 Estructura JSON

- [ ] `"materials": []` (vacío — NUNCA incluir materiales custom)
- [ ] `"selected_material_name": "Default"`
- [ ] Enclosure tiene `is_enclosure: true`, `side_a_exterior: false`
- [ ] Objetos internos tienen `is_enclosure: false`, `side_a_exterior: true`
- [ ] Todos los objetos tienen `source` con TODOS los campos (incluso null)
- [ ] `group_order` incluye `"Unassigned"` al final
- [ ] `group_material` incluye `"Unassigned": "Default"`
- [ ] `face_to_group_idx` tiene `length` (no `shape`) como key
- [ ] `active_enclosure_id` coincide con el `obj_id` del enclosure

### 9.2 Geometría

- [ ] **Enclosure SIEMPRE usa `kind: "extrude"`** — NUNCA `kind: "box"`. Rectangulares = 4 vértices
- [ ] Polígono centrado en (0,0) con **Y=0 como eje de simetría**
- [ ] Dimensiones coherentes con tipo de recinto (estudio 20-80m³, venue 500-5000m³, concierto 5000-30000m³)
- [ ] Objetos internos están DENTRO del enclosure (ninguna coordenada excede los límites)
- [ ] Suficientes objetos internos (estudio ≥8, concierto ≥6, venue ≥4)
- [ ] `size_xyz` sigue convención `[X=profundidad, Y=ancho, Z=alto]` (ver §0)
- [ ] Si `outdoor_mode: true`, no se requiere enclosure (RT60 retorna T=0, cobertura usa solo SPL directo)

### 9.3 Materiales — LA VERIFICACIÓN MÁS IMPORTANTE

- [ ] **¿Algún valor en `surface_group_material` es "Default"?** → SI: **CORREGIR ANTES DE ENVIAR**
- [ ] Cada superficie tiene un material DIFERENTE según su función (piso ≠ techo ≠ paredes ≠ puertas). Usar tabla de §2 según tipo de recinto
- [ ] Materiales son nombres REALES de la DB (§2), en español ("Vidrio (ventana)" no "glass_window", "Madera maciza barnizada (panel)" no "wood_door_solid")
- [ ] **Verificación RT60**: si TODAS las bandas dan el mismo valor → material "Default" olvidado. REVISAR
- [ ] RT60 estimado (Sabine: 0,1611×V/A) coherente con tipo de recinto:
  - Estudio CR: 0.2-0.4s | Live Room: 0.4-1.0s | Teatro: 0.6-1.0s
  - Concierto: 1.5-2.2s | Ópera: 1.2-1.6s | Venue: 1.0-3.0s | Cine: 0.3-0.8s
- [ ] `surface_group_material_b` (cara B exterior) asignada para TODAS las paredes del enclosure
- [ ] **Keys de material/assembly usan nombres del group_order**: "1|Pared 0", "1|Piso" — NO "1|Floor"

### 9.4 Assemblies

- [ ] **Wall assemblies multi-capa** definidos para CADA superficie con `surface_assembly_map`
- [ ] Assemblies tienen ≥2 capas para paredes aisladas (yeso + cavidad + yeso mínimo)
- [ ] Objetos con espesor constructivo (paneles, ventanas, puertas) también tienen assembly
- [ ] `surface_assembly_map` usa IDs de TL válidos (ver tabla §5)
- [ ] `surface_thickness_dir` usa `"inward"` para enclosure, `"center"` para internos

### 9.5 Parlantes

- [ ] **Parlantes apuntan source→receiver**: yaw = atan2(dy, dx) desde source a receiver. NUNCA al revés
- [ ] **source_pos ≠ receiver_pos** — NUNCA en el mismo punto. Source = escenario o frente (X negativo); receiver = la audiencia (X positivo) en un recinto de música, o el punto de escucha de un estudio, al 38 % de la profundidad (`x = −D/2 + 0.38×D`, un poco antes del centro, §52)
- [ ] **Y=0 es el eje de simetría** lateral — parlantes L/R simétricos en ±Y
- [ ] Fuente y receptor están a ≥ 0.5 m de cualquier superficie
- [ ] **Outfills abiertos (ángulo >90°)**: yaw_principal ± (45° a 70°). NUNCA cerrados (<90°)
- [ ] Subs en sistema separado con `mount: "sub_array"`, `channel`, `sub_decoupling`
- [ ] Arrays colgados tienen `mount: "flying"`
- [ ] **Parlantes NUNCA son objetos de geometría** — van SOLO en `speaker_systems` (ver §3)

### 9.6 Surround

- [ ] **UN solo sistema** con `mount: "surround"` y `surround_format` válido — NUNCA dividir en Front/Surr/Height/LFE separados
- [ ] Cada elemento tiene `channel` con código ITU correcto (Lss, Rss, Ltf, Rtf, etc.)
- [ ] `surround_mode: true` y `surround_format` a nivel proyecto
- [ ] **≥ 5.1 DEBE incluir canal LFE** — 5.1 = 6 elementos: L,R,C,LFE,Ls,Rs
- [ ] Pedestales: cada elemento con pedestal tiene `"pedestal": {"type": "floor_stand", ...}` embebido

### 9.7 Aberturas

- [ ] Puertas/ventanas como `openings` del enclosure, NUNCA como objetos superpuestos
- [ ] Materiales de aberturas: `Vidrio (ventana)` (NOT glass_window), `Madera maciza barnizada (panel)` (NOT wood_door_solid)
- [ ] Ventana CR↔LR tiene vidrios de distinto espesor en su assembly
- [ ] Cada abertura con aislamiento tiene `assembly_id`

### 9.8 Coherencia acústica

- [ ] Estudio tiene absorción suficiente (α_avg > 0.3 típico)
- [ ] Sala de conciertos NO sobre-absorbida (α_avg < 0.20)
- [ ] Superficies reflectantes donde deben (techo reflectante en concierto, absorbente en estudio)
- [ ] Bass traps si el recinto es estudio (lana mineral ≥200mm en esquinas)
- [ ] Volumen por butaca coherente (sinfónica 8-11m³, ópera 6-8m³)

---

## 10. Errores comunes

| Síntoma | Causa | Solución |
|---------|-------|----------|
| Colores rotos en 3D / xray no funciona | `materials` contiene array custom | Setear `"materials": []` |
| Material "Default" no encontrado | Falta en `group_material` | Agregar `"Unassigned": "Default"` |
| **Todas las superficies en "Default" / sin tratamiento** | **IA no asignó materiales reales** | **Asignar material real a CADA superficie según tipo de recinto (ver §2 y §29)** |
| **5.1 sin graves / sub no aparece** | **Falta canal LFE en surround** | **Agregar elemento con channel:"LFE", model_id:"sub_omni_ideal"** |
| **Sala desplazada / no centrada en Y=0** | **center del enclosure no en [0,0,H/2]** | **Polígono de extrusión SIEMPRE centrado en (0,0). Para rectangular: vértices en [-D/2,-W/2]...[D/2,W/2]** |
| **Source y receiver en el mismo punto** | **IA puso [0,0,1.2] para ambos** | **Source en el escenario o el frente (X negativo); receiver en la audiencia (X positivo) o, en un estudio, al 38 % de la profundidad (§52). Nunca iguales** |
| **Assembly map no aplica a superficies** | **Keys en inglés vs group_order en español** | **Keys de surface_assembly_map deben coincidir con group_order: "1\|Piso" no "1\|Floor"** |
| Subs no editables con Sub Array Builder | Falta `mount: "sub_array"` | Agregar `mount`, `channel`, `sub_decoupling` al sistema |
| Objeto no afecta modos | `is_enclosure: true` sin `side_a_exterior` | Usar `is_enclosure: false, side_a_exterior: true` |
| TL material no encontrado | ID incorrecto | Verificar contra tabla de IDs en §5 |
| Subs aparecen en el array colgado | Subs en mismo sistema que line array | Separar en `speaker_systems` distintos |
| pitch positivo apunta arriba | Convención invertida | pitch POSITIVO = ABAJO |
| **Line array colgado con caja inferior apuntando hacia arriba** | **J-curve mal aplicada** | **Pitch SIEMPRE crece de arriba a abajo en flying. Solo las 1-2 cajas SUPERIORES pueden tener pitch negativo (§6)** |
| **Array colgado con curva en J para el lado equivocado** | **Cajas inferiores con pitch negativo** | **Físicamente imposible: la gravedad tira la caja inferior hacia abajo. La J-curve solo se logra inclinando la CABEZA del array (cajas superiores) hacia atrás** |
| **Subs en el mismo sistema que line arrays** | **Mezclar tipos** | **Subs SIEMPRE en speaker_system separado con mount:'sub_array'. Line arrays con mount:'flying' o 'stacked'** |
| **Sub array sin dirección / sin delay** | **Falta patrón de arreglo** | **Usar presets: cardioide (polarity -1 + yaw 180° + delay), end-fire (delays incrementales), arco (yaw progresivo). Ver §6** |
| Sala rotada 90° / parlantes apuntan a pared lateral | `size_xyz` con ancho y profundidad invertidos | `size_xyz = [X=profundidad, Y=ancho, Z=alto]` — ver §0 |
| Sala descentrada, eje de simetría fuera de Y=0 | Enclosure parte de (0,0,0) en vez de centrado | Usar `make_box(cx=0, cy=0, ...)` — ver §0 |
| RT60/C80/STI dan valores incorrectos | Fuente en audiencia / receptor en escenario | Fuente en escenario (X negativo), receptor en audiencia (X positivo) |
| RT60 falla en estadio/aire libre | No hay enclosure watertight | Activar `"outdoor_mode": true` — RT60 retorna T=0, cobertura usa solo SPL directo |
| Sala rectangular causa flutter echo | Paredes paralelas | Absorción o difusión en una de las dos paredes paralelas; paredes inclinadas (>5°) sólo si el usuario no dio las medidas (§52.1) |
| **Estudio modelado como box rectangular** | **IA usó kind:"box"** | **NUNCA usar box para enclosures. Siempre kind:"extrude" — rectangulares con 4 vértices (§11)** |
| **Falta aislamiento / TL no se calcula** | **Sin wall_assemblies ni surface_assembly_map** | **Definir assemblies multi-capa y asignarlos a CADA superficie con surface_assembly_map (§4)** |
| **Solo absorción cara A, sin cara B** | **Sin surface_group_material_b** | **Asignar material exterior (cara B) a todas las paredes del enclosure** |
| **Assembly map con keys incorrectas para extrusión** | **Usar "Pared +X" en extrusión** | **Extrusiones usan "Pared 0", "Pared 1"... (índice del polígono)** |
| **Ventana/panel sin TL** | **Objeto sin assembly** | **Si tiene espesor constructivo (vidrio doble, panel multicapa), asignar assembly (§4)** |
| **RT60 falla en evento outdoor** | **Enclosure cerrado para aire libre** | **Usar outdoor_mode:true sin enclosure. Suelo como objeto plano opcional (§11)** |
| **Parlantes apuntan al escenario** | **yaw calculado al revés** | **yaw_principal = atan2(receiver_y-source_y, receiver_x-source_x). Parlantes usan ese yaw (§6)** |
| **Outfills no cubren laterales** | **Ángulo entre outfills < 90°** | **Outfills: yaw_principal ± (45° a 70°). Ángulo total >90° (§6)** |
| **Outfills se superponen con L/R** | **Outfills apuntan casi igual que el main** | **Outfill complementa donde L/R no llega. Rotarlo más hacia afuera** |
| Monitores de estudio sin modelo | Usar `point_60` genérico | Usar model_id real: `genelec_8040b`, `neumann_kh120_ii`, `yamaha_hs7`, etc. (30 monitores verificados en librería). Fallback: `point_90` |
| **Modos incorrectos con parlantes como geometría** | **Parlantes/subs/pedestales creados como objetos en `objects`** | **Eliminar esos objetos — van SOLO en `speaker_systems` (§3)** |
| **Surround no reconocido por el software** | **Sistema dividido en múltiples entries (Front, Surr, Height)** | **UN solo sistema con `mount: "surround"` y TODOS los canales** |
| **Surround no activa canales ITU extendidos** | **`surround_mode` no seteado a nivel proyecto** | **Agregar `"surround_mode": true, "surround_format": "7.1.4"` al JSON raíz** |
| **Canales surround no se identifican** | **Usar solo `"L"` y `"R"` para surrounds/alturas** | **Usar códigos ITU: Lss, Rss, Lrs, Rrs, Ltf, Rtf, Ltr, Rtr, Lts, Rts** |

---

## 12. Diseño de estudios — Monitores y metodología

### Monitores de estudio

La librería incluye **30 monitores de estudio verificados** de 10 marcas profesionales. Para estudios de grabación/mezcla, usar speaker systems con `model_id` real:

```json
{
    "name": "Nearfield Monitors L/R",
    "mount": "monitor",
    "channel": "stereo",
    "elements": [
        {
            "name": "Monitor L",
            "model_id": "genelec_8040b",
            "spl_db": 105.0,
            "polar": "Model",
            "pos": [-2.45, -1.0, 1.25],
            "yaw_deg": 30.0,
            "pitch_deg": 1.4,
            "channel": "L"
        },
        {
            "name": "Monitor R",
            "model_id": "genelec_8040b",
            "spl_db": 105.0,
            "polar": "Model",
            "pos": [-2.45, 1.0, 1.25],
            "yaw_deg": -30.0,
            "pitch_deg": 1.4,
            "channel": "R"
        }
    ]
}
```

**Marcas de monitores disponibles** (usar `model_id` exacto):

| Marca | Modelos (model_id) | Uso típico |
|-------|-------------------|------------|
| Genelec | `genelec_8010a`, `genelec_8020d`, `genelec_8030c`, `genelec_8040b` | Nearfield/midfield |
| Neumann | `neumann_kh80_dsp`, `neumann_kh120_ii`, `neumann_kh150` | Nearfield/midfield (DSP) |
| ADAM Audio | `adam_t7v`, `adam_a4v`, `adam_a7v`, `adam_a77x` | Nearfield/midfield |
| KRK | `krk_rokit5_g4`, `krk_rokit7_g4`, `krk_rokit8_g4` | Home studio / nearfield |
| Focal | `focal_alpha50_evo`, `focal_alpha65_evo`, `focal_shape65` | Nearfield |
| ATC | `atc_scm25a_pro`, `atc_scm45a_pro` | Midfield pro |
| Dynaudio | `dynaudio_lyd5`, `dynaudio_lyd48`, `dynaudio_bm5_mkiii` | Nearfield/midfield |
| Amphion | `amphion_one18`, `amphion_two18` | Nearfield (pasivos) |
| Yamaha HS | `yamaha_hs5`, `yamaha_hs7`, `yamaha_hs8` | Nearfield referencia |
| IK Multimedia | `ik_iloud_micro`, `ik_iloud_mtm`, `ik_iloud_precision5` | Nearfield compacto |

El ejemplo es para una sala de 6 × 4,2 × 3 con el oyente en `[-0.72, 0, 1.2]` (el 38 %): los
monitores a 2,0 m entre sí y a 2,0 m del oyente, `yaw = atan2(0 − (−1.0), −0.72 − (−2.45)) = 30°`
y `pitch = atan2(1.25 − 1.2, 2.0) = 1,4°` hacia abajo. Hasta la v43 decía `yaw 0` y `pitch 10`:
los monitores miraban de frente y al piso. **Con otra sala, otras cuentas** (§52.2).

`"mount": "monitor"` y `"channel": "stereo"` son los del par de estudio. Hasta la v44 este
ejemplo decía `"flying"`, que es el de un array colgado: al editar el sistema, el programa
abría el asistente de line array.

**Un control room completo** ---la sala, el tratamiento con sus cuentas, los monitores, el
aislamiento, el JSON y el texto para el usuario--- está en §52.5.

**Posicionamiento de monitores**: Triángulo equilátero con el sweet spot. Separación entre L y R = distancia de cada uno al ingeniero. El yaw y el pitch **se calculan** para que apunten al oído (pitch positivo es hacia abajo). Altura típica: 1.2-1.3m (oído sentado).

**Sub de estudio**: Un solo sub mono debajo o al lado de la consola, `mount: "sub_array"`, `channel: "M"`, `sub_decoupling: "direct"`.

**Monitoreo surround / Atmos**: Para estudios de mezcla surround, usar el Wizard Surround (§18) en vez de colocar monitores manualmente. El wizard posiciona automáticamente según ITU-R BS.775 / Dolby Atmos, con pedestales y desacople incluidos. Formatos típicos: `5.1` para broadcast/cine, `7.1.4` para Atmos.

### Metodología de diseño de salas

**Paso 1 — Geometría**
- Teatros/salas de eventos: box es suficiente. Agregar objetos internos (escenario, balcones).
- Control rooms: extrusión SIEMPRE (de 4 vértices si es rectangular). Paredes inclinadas y front wall en V sólo si el usuario las pide o no da medidas: con medidas dadas, el rectángulo de esas medidas (§52.1).
- Live rooms: pueden ser box si son grandes, extrusión si tienen geometría especial.

**Paso 2 — Materiales absorbentes**
- Elegir de la base de datos interna (2665 materiales). Nombres exactos, case-sensitive.
- Front wall de CR: absorción pesada (lana mineral 100mm+).
- Back wall de CR: difusión o absorción (cortina pesada, difusor QRD).
- Una ventana es una **abertura** (§28) con material `Vidrio (ventana)`: la pared que la tiene **conserva su material**, igual que la de enfrente (simetría, §21.1 A7). Hasta la v43 esta línea decía «Laterales con ventanas: `Vidrio (ventana)`» y la IA hacía de vidrio la pared entera. Si la ventana cae sobre un punto de primera reflexión, inclinala 5-10° (A13) o corrila.
- Techo de CR: paneles de madera (reflexión controlada) o absorción.

**Paso 3 — Aislamiento (assemblies)**
- Paredes entre salas: triple hoja desacoplada (STC 60+). Coupling ≤ 0.05.
- Paredes exteriores: doble yeso HD + lana roca (STC 50+).
- Techo: losa HA + cámara + lana + cielorraso flotante (clips resilientes).
- Piso: losa + caucho/neopreno + plywood/tarima (piso flotante).
- Ventanas: DVH con vidrios asimétricos + cámara amplia (100mm+).
- `surface_thickness_dir`: `"inward"` para enclosure, `"center"` para internos.

**Paso 4 — Sistemas de audio**
- Teatros: line arrays colgados L/R + subs cardioide. Sistemas separados.
- Estudios: nearfield monitors + sub mono.
- Cada sistema es un `speaker_system` independiente.
- Subs SIEMPRE con `mount: "sub_array"`, `channel`, `sub_decoupling`, `sub_orientation`.

---

## 13. Speaker Library — 447 modelos verificados

El software tiene una librería embebida de 447 modelos (incluyendo 30 monitores de estudio). Al generar JSONs, usar solo `model_id` — **no incluir el objeto `model` completo**. El software resuelve el modelo desde su librería interna.

> **Si necesitás un model_id que no aparece acá, consultá la lista completa en el código Python** (`_default_speaker_library_data()`). La convención de naming es `marca_modelo` en lowercase con underscores (ej: `lacoustics_k2`, `db_v8`, `jbl_vtx_a12`).

### Ejemplos representativos por categoría (3 por tipo)

**Line arrays**: `lacoustics_k2`, `db_v8`, `jbl_vtx_a12`
**Point source**: `lacoustics_x12`, `db_e12`, `jbl_srx815p`
**Subwoofers**: `lacoustics_ks28`, `db_sl_sub`, `jbl_srx928s`
**Columnas**: `dbt_ingenia_ig3t`, `meyer_cal64`, `ev_evolve_50`
**Monitores estudio**: `genelec_8040b`, `neumann_kh120_ii`, `adam_a7v`

### Marcas disponibles (22)

ADAMSON, d&b, dBTechnologies, Electro-Voice, JBL, L-Acoustics, Martin Audio, Meyer Sound, NEXO, QSC, RCF, Yamaha, Genelec, Neumann, ADAM Audio, KRK, Focal, ATC, Dynaudio, Amphion, IK Multimedia.

### Presets genéricos (fallback)

`point_90`, `point_60`, `point_120`, `omni_ideal`, `sub_omni_ideal`, `line_array_generic_5deg`, `line_array_generic_10deg`, `column_generic`.

### Uso en JSON — solo `model_id`

```json
{
    "name": "LA 1",
    "model_id": "lacoustics_k2",
    "spl_db": 112.0,
    "polar": "LineArray",
    "pos": [-1.5, -4.0, 8.0],
    "yaw_deg": 0.0, "pitch_deg": 0.0, "roll_deg": 0.0,
    "gain_db": 0.0, "delay_ms": 0.0,
    "channel": "L"
}
```

**No incluir el campo `model`** — el software lo resuelve automáticamente desde la librería interna usando `model_id`. Si el `model_id` no existe en la librería, el software usa `point_90` (tops) o `sub_omni_ideal` (subs) como fallback.

---

## 14. Audience areas y butacas como volumen

### Butacas como objeto de volumen

Las butacas reales se reemplazan por una **caja sólida** que ocupa el mismo volumen. Esta caja funciona como objeto interno (`is_enclosure: false`, `side_a_exterior: true`) y bloquea modos en el análisis modal.

```json
{
    "obj_id": 4,
    "name": "Butacas platea",
    "is_enclosure": false,
    "side_a_exterior": true,
    "source": {
        "kind": "box",
        "size_xyz": [16.0, 12.0, 1.2]
    },
    "group_material": {
        "Floor": "Butaca tapizada (vacía)",
        "Ceiling": "Butaca tapizada (vacía)",
        "Wall +X": "Butaca tapizada (vacía)",
        "...": "..."
    }
}
```

Dimensiones típicas: ancho y profundidad de la zona de butacas, **altura 1.2 m** (altura de butacas plegadas con respaldo).

### Audience areas (rectángulos de escucha)

Los audience areas se apoyan **sobre** la superficie de las butacas a z = 1.2 m (oído sentado). Son rectángulos planos que definen dónde se calcula la cobertura del sistema de PA.

```json
"audience_areas": [
    {
        "name": "Platea",
        "polygon_xy": [[2.0, -6.0], [16.0, -6.0], [16.0, 6.0], [2.0, 6.0]],
        "bbox_xy": [2.0, -6.0, 16.0, 6.0],
        "z_m": 1.2,
        "slope_deg": 0.0,
        "slope_axis_deg": 0.0,
        "target_db": 100.0,
        "tolerance_db": 6.0
    },
    {
        "name": "Balcon",
        "polygon_xy": [[14.0, -8.0], [17.0, -8.0], [17.0, 8.0], [14.0, 8.0]],
        "bbox_xy": [14.0, -8.0, 17.0, 8.0],
        "z_m": 5.7,
        "slope_deg": 10.0,
        "slope_axis_deg": 0.0,
        "target_db": 98.0,
        "tolerance_db": 6.0
    }
],
"audience_areas_enabled": true
```

**Campos**:
- `polygon_xy`: rectángulo en coordenadas XY (4 vértices CCW)
- `bbox_xy`: bounding box `[x_min, y_min, x_max, y_max]`
- `z_m`: altura del plano de escucha (1.2m = oído sentado sobre piso, o z del balcón + 1.2m)
- `slope_deg`: inclinación de la grada (0° = plano, 10°-15° = grada típica)
- `slope_axis_deg`: dirección del slope (0° = sube en X positivo)
- `target_db`: nivel objetivo SPL en dB
- `tolerance_db`: tolerancia aceptable (típico 6 dB)

**Para múltiples niveles** (platea + balcón + palcos): crear un audience area por cada nivel, con su propio `z_m` y `slope_deg`.

---

## 15. Puntos de apoyo/anclaje y flanqueo

Los assemblies de aislamiento tienen campos que controlan el comportamiento mecánico y el flanqueo:

```json
{
    "connection_profile": "Clips resilientes",
    "coupling": 0.05,
    "bridge_k": 0.0,
    "panel_span_x_m": 3.5,
    "panel_span_y_m": 3.0,
    "panel_boundary": "Apoyado"
}
```

**`connection_profile`**: Tipo de conexión mecánica entre hojas.
- `"Manual"`: conexión rígida directa (peor aislamiento)
- `"Clips resilientes"`: clips de desacople (mejor aislamiento, menos flanqueo)
- `"Montantes metálicos"`: perfilería estándar

**`coupling`**: Factor de acoplamiento mecánico entre hojas (0.0–1.0). Menor = mejor aislamiento.
- `0.02`: triple hoja totalmente desacoplada (estudio profesional)
- `0.05`: clips resilientes (estudio/cine)
- `0.10`: piso flotante sobre caucho
- `0.15`: montantes metálicos estándar
- `0.20`: conexión rígida (tabique simple)

**`bridge_k`**: Rigidez de puentes acústicos adicionales (0.0 = sin puentes). Para montantes que atraviesan la cavidad.

**`panel_span_x_m` / `panel_span_y_m`**: Dimensiones del panel entre apoyos (afecta la frecuencia de coincidencia y la radiación).

**`panel_boundary`**: Tipo de apoyo del panel.
- `"Apoyado"`: bordes simplemente apoyados (típico)
- `"Empotrado"`: bordes empotrados (ventanas en marco rígido)

**Regla**: Para máximo aislamiento, minimizar `coupling` y usar `"Clips resilientes"`. Para ventanas usar `"Empotrado"` con coupling bajo.

---

## 16. Modo Outdoor (aire libre / estadios)

Para proyectos al aire libre —festivales, conciertos outdoor, estadios sin techo cerrado— **no se necesita un box de recinto gigante que simule el aire**. CADSFS soporta esto nativamente con `outdoor_mode`.

### Activación en JSON

```json
{
  "outdoor_mode": true,
  "active_enclosure_id": null
}
```

### Comportamiento cuando `outdoor_mode: true`

| Módulo | Comportamiento |
|--------|---------------|
| **RT60** | Retorna T = 0 en todas las bandas con nota "Modo outdoor: RT60 no aplica (volumen infinito)" |
| **Cobertura SPL** | Funciona normalmente (solo campo directo + absorción del aire). Modo de extensión se fuerza automáticamente a `radius_masked` |
| **Reflexiones** | Calculan sobre las superficies que existan (tribunas, piso, escenario). Los rayos que no impacten nada se pierden |
| **Modal** | No aplica (sin volumen cerrado) |
| **Aislamiento (ISO 12354)** | No aplica |

### Cuándo usar outdoor_mode

- **Festival / concierto al aire libre**: solo piso + escenario + parlantes. Sin paredes.
- **Estadio abierto**: tribunas + piso + techo parcial. No necesita enclosure watertight.
- **Estadio con techo cerrado**: NO usar outdoor_mode. Modelar como recinto normal con enclosure.
- **Plaza / espacio urbano**: piso + fachadas de edificios como objetos reflectantes.

### Ejemplo mínimo — Festival outdoor

```json
{
  "app": "CADSFS",
  "version": "1.49.84",
  "bands_hz": [31,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500],
  "c_m_s": 343.0,
  "materials": [],
  "selected_material_name": "Default",
  "outdoor_mode": true,
  "active_enclosure_id": null,
  "local_view_radius_m": 80.0,
  "objects": [
    {
      "obj_id": 1,
      "name": "Piso",
      "is_enclosure": false,
      "side_a_exterior": true,
      "source": {
        "kind": "box",
        "path": null,
        "scale_to_m": 1.0,
        "size_xyz": [100.0, 80.0, 0.05],
        "centered": false,
        "polygon_xy": null,
        "height": null,
        "plane": null
      },
      "group_order": ["Floor", "Unassigned", "Default"],
      "group_material": {"Floor": "Pasto / césped (campo deportivo)", "Unassigned": "Default", "Default": "Default"}
    }
  ],
  "speaker_systems": [],
  "source_pos": [-15.0, 0.0, 1.5],
  "receiver_pos": [15.0, 0.0, 1.2]
}
```

### Notas importantes

- En modo outdoor, `local_view_radius_m` debe ser grande (50–100 m) para ver toda el área de cobertura.
- El software auto-adapta el radio de vista local si es menor al 50% de la diagonal del bbox del modelo.
- Los objetos en outdoor (piso, tribunas, escenario) deben tener `is_enclosure: false` y `side_a_exterior: true`.
- La grilla del piso 3D se puede ocultar desde Vista → "Grilla y ejes".
- El modo outdoor se activa/desactiva también desde el menú Archivo → "Modo Outdoor (aire libre)".

---

## 17. Propiedades del proyecto

Campos opcionales que aparecen en el resumen y el PDF exportado. Se editan desde Archivo → Propiedades del proyecto.

```json
{
  "project_name": "Auditorio Municipal",
  "project_designer": "Ing. Juan Pérez",
  "project_builder": "Constructora ABC S.A.",
  "project_client": "Municipalidad de Zacatecas",
  "project_location": "Av. López Mateos 123, Zacatecas",
  "project_date": "Marzo 2026",
  "project_venue_type": "Teatro",
  "project_notes": "Diseño para 500 butacas con refuerzo L-Acoustics A15"
}
```

Todos los campos son strings opcionales (vacío = no se muestra). El `project_name` también aparece en el título de la ventana.

### `measured_rt60_s` — RT medido como override de la distancia crítica

Campo opcional a nivel de proyecto: un **RT60 medido por banda**, en segundos, que **sobrescribe el RT calculado** al computar la **distancia crítica** (d_crít). Formato: diccionario `{ banda_Hz : RT_en_segundos }`. Desde R429 vale para **todos** los paneles que la muestran (overlay ♫, Info del recinto, pestaña Radio crítico del diálogo de medición, rótulo del panel de cobertura, informe PDF); hasta R428 sólo lo leía el overlay ♫. Los cálculos de nivel y decaimiento (mapa de cobertura, IR sintética, Walker) siguen usando los materiales.

```json
"measured_rt60_s": { "125": 1.8, "250": 1.8, "500": 1.5, "1000": 1.5, "2000": 1.2, "4000": 1.2 }
```

**Cuándo usarlo.** En salas **conocidas / ya medidas**, un mesh muy detallado puede **inflar la superficie** y hacer que el RT calculado (Eyring) salga mal, arrastrando la distancia crítica. El **volumen encerrado** sí es confiable: volumen + RT medido → d_crít correcta. Es un override quirúrgico solo para la d_crít, no reemplaza el cálculo modal ni el de aislamiento.

**Reglas:**
- Bandas soportadas: **125, 250, 500, 1000, 2000, 4000 Hz**. En la UI (Herramientas → *RT medido → distancia crítica*) se ingresan **3 valores** — graves, medios, agudos — que se mapean a 125/250, 500/1000 y 2000/4000 respectivamente.
- Por banda: si hay un valor medido > 0, se usa ese; si falta o es 0, se usa el RT **calculado** (Eyring) de esa banda. Entre dos bandas medidas (por ejemplo 160 Hz, entre 125 y 250) se interpola en escala logarítmica de frecuencia; fuera del rango medido se usa el calculado.
- **Diccionario vacío `{}` = usar el RT calculado** (comportamiento por defecto).
- Los valores se guardan/serializan como `{int(banda): float(segundos)}`.

> No lo pongas "por las dudas": solo tiene sentido cuando tenés una **medición real** del RT de la sala. Para salas nuevas o hipotéticas, dejalo vacío y confiá en el cálculo.

---

## 18. Sistema Surround / Inmersivo

> ⚠ **REGLAS CRÍTICAS para generación por IA:**
> 1. **UN solo sistema** — TODOS los canales (L/R/C/LFE/surrounds/alturas/subs) van como `elements` de UN solo `speaker_systems` entry con `mount: "surround"`.
> 2. **Canales ITU correctos** — NUNCA usar solo `"L"` y `"R"`. Usar códigos: `Lss`, `Rss`, `Lrs`, `Rrs`, `Ltf`, `Rtf`, `Ltr`, `Rtr`, `Lts`, `Rts`.
> 3. **`surround_mode: true`** a nivel proyecto — OBLIGATORIO.
> 4. **Parlantes NO son objetos** — NUNCA crear cajas en `objects` para representar parlantes. Solo `speaker_systems`.
> 5. **Subs dentro del surround** — Los LFE van como elementos con `channel: "LFE"` dentro del mismo sistema surround, NO como `speaker_systems` separado.

CADSFS incluye un Wizard Surround que coloca parlantes automáticamente según normas ITU-R BS.775 y Dolby Atmos. Se accede desde el menú Sistemas → "Surround / Inmersivo…" o desde el menú contextual del sistema.

### Formatos soportados

| Formato | Canales | Norma | Uso típico |
|---------|---------|-------|------------|
| `2.0` | L, R | Estéreo | Monitoreo estéreo, home studio |
| `5.1` | L, R, C, LFE, Ls, Rs | ITU-R BS.775 | Cine estándar, home theater |
| `7.1` | L, R, C, LFE, Lss, Rss, Lrs, Rrs | ITU-R BS.775-3 | Cine 7.1, broadcast |
| `7.1.2` | + Ltf, Rtf | Dolby Atmos | Atmos básico (altura frontal) |
| `7.1.4` | + Ltf, Rtf, Ltr, Rtr | Dolby Atmos | Atmos estándar (4 alturas) |
| `9.1.6` | + wide + 6 alturas | Dolby Atmos | Cine grande, dubbing theater |

### Posiciones angulares (azimut, elevación)

Los ángulos siguen la convención ITU: 0° = frente (C), positivo = izquierda, negativo = derecha. Los parlantes de altura tienen elevación 35° (7.1.2/7.1.4) o 45° (9.1.6). El LFE se coloca a z=0.25 m (en el piso).

### JSON del sistema surround

```json
{
  "name": "Surround 7.1.4 Dolby Atmos (12 spk)",
  "mount": "surround",
  "surround_format": "7.1.4",
  "elements": [
    {"channel": "L",    "pos": [2.5, -1.5, 1.2], "yaw_deg": -30.5, "pitch_deg": 0.0, "roll_deg": 0.0,
     "model_id": "lacoustics_x8", "model": "L-Acoustics X8", "spl_db": 129.0, "spl_1m_db": 129.0,
     "gain_db": 0.0, "delay_ms": 0.0, "muted": false, "polarity": 1, "dims_m": [0.164, 0.25, 0.424],
     "pedestal": {"type": "floor_stand", "height_m": 1.2, "width_m": 0.20, "depth_m": 0.20, "shape": "box", "visible": true},
     "decoupling": "IsoAcoustics ISO-130"},
    {"channel": "R",    "pos": [2.5, 1.5, 1.2], "yaw_deg": 30.5, "...": "..."},
    {"channel": "C",    "pos": [2.5, 0.0, 1.2], "yaw_deg": 0.0, "...": "..."},
    {"channel": "LFE",  "pos": [2.5, -0.5, 0.25], "yaw_deg": 0.0, "...": "..."},
    {"channel": "Lss",  "pos": [0.0, -2.5, 1.2], "yaw_deg": -90.0, "...": "..."},
    {"channel": "Rss",  "pos": [0.0, 2.5, 1.2], "yaw_deg": 90.0, "...": "..."},
    {"channel": "Lrs",  "pos": [-2.0, -2.2, 1.2], "yaw_deg": -135.0, "...": "..."},
    {"channel": "Rrs",  "pos": [-2.0, 2.2, 1.2], "yaw_deg": 135.0, "...": "..."},
    {"channel": "Ltf",  "pos": [1.8, -1.3, 3.5], "yaw_deg": -30.0, "pitch_deg": -25.0, "...": "..."},
    {"channel": "Rtf",  "pos": [1.8, 1.3, 3.5], "yaw_deg": 30.0, "pitch_deg": -25.0, "...": "..."},
    {"channel": "Ltr",  "pos": [-1.8, -1.3, 3.5], "yaw_deg": -135.0, "pitch_deg": -25.0, "...": "..."},
    {"channel": "Rtr",  "pos": [-1.8, 1.3, 3.5], "yaw_deg": 135.0, "pitch_deg": -25.0, "...": "..."}
  ],
  "pedestals": [
    {"type": "floor_stand", "height_m": 1.2, "width_m": 0.20, "depth_m": 0.20, "pos": [2.5, -1.5, 1.2]},
    {"type": "floor_stand", "height_m": 1.2, "width_m": 0.20, "depth_m": 0.20, "pos": [2.5, 1.5, 1.2]}
  ]
}
```

> **Nota**: `"..."` indica que los campos restantes (`model_id`, `spl_db`, `dims_m`, etc.) son iguales al primer elemento. En un JSON real, TODOS los campos deben estar presentes en cada elemento.
}
```

### Campos clave del sistema

| Campo | Valor | Descripción |
|-------|-------|-------------|
| `mount` | `"surround"` | Identifica sistema surround (OBLIGATORIO) |
| `surround_format` | `"7.1.4"` | Formato ITU/Atmos elegido |
| `pedestals` | `[...]` | Lista de pedestales a nivel de sistema para renderizado 3D |

### Campos clave por elemento

| Campo | Valores | Descripción |
|-------|---------|-------------|
| `channel` | `"L"`, `"R"`, `"C"`, `"LFE"`, `"Ls"`, `"Rs"`, `"Lss"`, `"Rss"`, `"Lrs"`, `"Rrs"`, `"Ltf"`, `"Rtf"`, `"Ltr"`, `"Rtr"`, `"Lts"`, `"Rts"` | Canal ITU asignado (escribirlo como en esta lista). En el Walker, con un archivo multicanal, la caja suena con el canal del archivo que lleva su código, sin distinguir mayúsculas (5.1: L R C LFE Ls Rs; 7.1: L R C LFE Lss Rss Lrs Rrs; en un 5.1, `Lss`/`Rss` toman `Ls`/`Rs`); las `M` y las de un canal que el archivo no trae reciben la mezcla de todos los canales menos el LFE |
| `pedestal.type` | `"none"`, `"floor_stand"`, `"desk_stand"`, `"wall_arm"`, `"ceiling"` | Tipo de soporte |
| `decoupling` | `"none"`, `"Foam pad"`, `"IsoAcoustics ISO-130"`, `"IsoAcoustics ISO-155"`, `"IsoAcoustics ISO-200"`, `"Primacoustic RX7"`, `"Auralex MoPad"` | Desacople mecánico (monitores) |
| `decoupling` (LFE) | `"none"`, `"Auralex SubDude"`, `"IsoAcoustics Zazen"`, `"SVS SoundPath"`, `"Foam pad"`, `"Plataforma flotante"` | Desacople para subwoofer |

### Pedestales — dos niveles de almacenamiento

Los pedestales se guardan en **dos lugares** (redundantes para compatibilidad):

1. **Nivel de elemento**: `el["pedestal"] = {"type": "floor_stand", "height_m": 1.2, ...}` — define el tipo de soporte para ese parlante específico.
2. **Nivel de sistema**: `sysd["pedestals"] = [{"type": "floor_stand", "pos": [...], ...}]` — lista plana con posición para renderizado 3D.

El renderer busca primero `sysd["pedestals"]`; si está vacío, extrae pedestales de cada elemento automáticamente.

### Apuntar al Sweet Spot

Desde el menú contextual del sistema (clic derecho en la lista de sistemas), "⟳ Apuntar al Sweet Spot" recalcula `yaw_deg` y `pitch_deg` de todos los elementos para que apunten a `receiver_pos`. La fórmula:

```
dx, dy, dz = sweet_spot - speaker_pos
yaw_deg   = atan2(dy, dx)     → ángulo horizontal desde +X
pitch_deg = atan2(-dz, horiz)  → ángulo vertical (negativo = apunta arriba)
```

Esto funciona para **cualquier** tipo de sistema, no solo surround.

### Campos a nivel de proyecto

```json
{
  "surround_mode": true,
  "surround_format": "7.1.4"
}
```

Se activan automáticamente al crear un sistema surround. `surround_mode: true` habilita la asignación extendida de canales en el menú contextual.

---

## 19. Guía de selección de modo de proyecto

### ¿Cuándo usar cada modo?

| Escenario | `outdoor_mode` | Enclosure | Ejemplo |
|-----------|---------------|-----------|---------|
| **Sala cerrada** (teatro, cine, iglesia, estudio) | `false` | Sí (`is_enclosure: true`) | Teatro de 500 butacas |
| **Estadio con techo cerrado** | `false` | Sí | Estadio cubierto para eventos |
| **Festival / concierto al aire libre** | `true` | No (`active_enclosure_id: null`) | Festival con escenario + piso |
| **Estadio abierto** | `true` | No | Estadio sin techo, tribunas como objetos |
| **Plaza / espacio urbano** | `true` | No | Plaza con fachadas reflectantes |

### ¿Cuándo usar surround?

| Escenario | `surround_mode` | Formato típico |
|-----------|----------------|----------------|
| **PA en vivo (teatro/concierto)** | `false` | No surround — usar arrays L/R + subs |
| **Cine estándar** | `true` | `5.1` o `7.1` |
| **Cine Dolby Atmos** | `true` | `7.1.4` o `9.1.6` |
| **Home theater / control room** | `true` | `5.1` o `7.1.4` |
| **Estudio de música (monitoreo)** | `false` | No surround — usar monitores L/R estéreo |
| **Estudio de mezcla surround** | `true` | `5.1` o `7.1.4` |
| **Instalación inmersiva (museo, venue)** | `true` | `7.1.4` o `9.1.6` |

### Combinaciones válidas

```
outdoor_mode=false + surround_mode=false  →  Sala estándar con PA (lo más común)
outdoor_mode=false + surround_mode=true   →  Cine / estudio surround / home theater
outdoor_mode=true  + surround_mode=false  →  Festival / outdoor con PA
outdoor_mode=true  + surround_mode=true   →  Instalación inmersiva al aire libre (raro)
```

### Módulos afectados por cada modo

| Módulo | Sala estándar | Outdoor | Surround |
|--------|:---:|:---:|:---:|
| RT60 | ✓ | ✗ (T=0) | ✓ |
| Cobertura SPL | ✓ | ✓ (solo directo) | ✓ |
| Reflexiones | ✓ | ✓ (sobre objetos existentes) | ✓ |
| Modal | ✓ | ✗ | ✓ |
| Aislamiento (TL) | ✓ | ✗ | ✓ |
| Análisis estéreo | ✓ | ✓ | ✗ (N/A) |
| Canales ITU extendidos | ✗ | ✗ | ✓ |
| Wizard posicionamiento | ✗ | ✗ | ✓ |

---

## 21. Directrices acústicas por tipo de recinto

> Estas directrices guían a la IA para tomar decisiones de diseño informadas ANTES de que el usuario corra la simulación. La IA usa aritmética básica (proporciones, volumen, Schroeder) para elegir geometría, materiales y configuraciones coherentes con el objetivo acústico.

### 21.1 Estudios de grabación / mezcla / mastering

**A1. Proporciones de sala (ratios de Bolt).**
Verificar que las dimensiones del control room caigan dentro del área de Bolt. Ratios recomendados: 1:1.28:1.54 (IEC), 1:1.4:1.9 (Sepmeyer), 1:1.6:2.33 (Louden). Si las dimensiones caen fuera, advertir que habrá concentración de modos.

**A2. Zona libre de reflexiones (RFZ).**
Los primeros 15-20 ms después del sonido directo deben estar libres de reflexiones especulares en el sweet spot. Verificar que las primeras reflexiones laterales (paredes ±Y) no lleguen antes de ese umbral, o indicar tratamiento absorbente en esos puntos.

**A3. Puntos de primera reflexión lateral.**
Regla del espejo: trazar línea desde cada monitor al sweet spot reflejada en pared lateral. Esos puntos necesitan absorción ≥50mm (lana mineral, paneles acústicos). Calcular las posiciones y asignar material apropiado. La fórmula, en §52.2.

**A4. Pared trasera: difusión, no absorción pura.**
En control rooms tipo RFZ/LEDE, la pared trasera (+X, detrás del ingeniero) debe tener difusión (QRD, skyline, policilíndricos) para mantener la envolvente del campo sonoro sin reflexiones especulares. Nunca hormigón desnudo ni absorción completa.

**A5. Bass traps en triedros.**
Los 8 triedros (esquinas 3-superficies) concentran todos los modos axiales. Recomendar trampas de graves en al menos los 4 triedros superiores y los 4 inferiores si hay espacio. Material: lana mineral ≥60 kg/m³, ≥200mm de profundidad.

**A6. Cloud (tratamiento de techo).**
En la zona del sweet spot, el techo necesita un panel absorbente o absorbente-difusor (cloud) para controlar la reflexión del techo (ITDG < 15ms). Mínimo 1.5m × 1.5m centrado sobre el sweet spot. Altura <2.8m → absorción; >3.5m → absorción+difusión.

**A7. Simetría obligatoria.**
Y=0 debe ser eje de simetría acústica. Materiales, objetos y geometría en +Y y -Y deben ser simétricos. Si hay ventana a un solo lado, compensar con panel de masa equivalente en el opuesto para imagen estéreo.

**A8. Volumen mínimo del control room.**
Para monitoreo preciso en graves, volumen mínimo recomendado: 40m³ (≈4×3.5×3m). Por debajo de 30m³ los modos están demasiado separados y la respuesta de graves es errática. Advertir si el volumen es insuficiente. **Si el usuario dio las medidas, se advierte en el texto y las medidas no se cambian** (§52.1): «un control room de 3x4x3» son 36 m³, y la IA que lo agrandó a 5 × 4,2 hizo otra sala.

**A9. Criterio de ruido de fondo NC.**
Estudios de grabación: NC 15-20. Control rooms de mezcla: NC 20-25. Estudios de ensayo: NC 30-35. Considerar estas metas al diseñar assemblies de aislamiento.

**A10. Aislamiento entre salas adyacentes (STC/Rw).**
Múltiples recintos: CR↔LR: STC ≥ 55. CR↔exterior: STC ≥ 60. Iso booth↔LR: STC ≥ 50. Puertas: mínimo STC 40 (doble puerta con trampa de aire).

**A11. Piso flotante.**
En estudios profesionales el piso debe ser flotante (desacoplado). Assembly: losa de concreto + neopreno/aislador + contrapiso flotante + terminación. Nunca una sola capa.

**A12. Techo desacoplado.**
Assembly: yeso suspendido con tirantes resilientes + cavidad con lana mineral + losa estructural. Nunca adherir yeso directamente a la losa.

**A13. Ventana de control (CR ↔ Live Room).**
Se modela como **abertura** del recinto (§28), no como objeto, con su assembly multicapa:
vidrios de espesores distintos, para que sus caídas por coincidencia no caigan en la misma
frecuencia, y cámara ancha. En CADSFS, vidrio 6 + cámara 100 + vidrio 10 da Rw 38; laminado
12,8 + cámara 200 + laminado 8,8 da Rw 45 (§52.5). En la obra, el vidrio interior va
inclinado 5-10° para no mandar reflexiones al oyente. En el modelo la abertura es plana: si
cae sobre un punto de primera reflexión, se corre.

**A14. Posición del subwoofer en estudio.**
No en esquina (máxima excitación de todos los modos) ni centrado (nodo del fundamental). Posición recomendada: 1/3 de la pared frontal desde una esquina, en el piso.

**A15. Distancia monitores-pared frontal.**
Flush-mount (soffit): empotrados en pared frontal. Sobre stands: mínimo 0.6m de la pared trasera del monitor a la pared frontal para evitar SBIR. Si <0.3m, recomendar flush-mount o bass trap detrás.

### 21.2 Recintos de música amplificada / venues

**B1. Líneas de delay — timing.**
Ubicar donde el SPL del sistema principal cae 6dB. Delay = distancia a fuente / 343 + 5-15ms de precedencia (Haas).

**B2. Front fills — primeras filas.**
Primeras 3-5 filas bajo el ángulo de cobertura vertical del array principal. Front fills: point source 60-90° en borde de escenario, pitch -15° a -30°, nivel -6 a -10 dB respecto al principal.

**B3. Under-balcony fills.**
Sugerir fills debajo del balcón si la profundidad del balcón supera 1.5× la altura libre debajo de él.

**B4. Uniformidad de cobertura (SPL variance).**
Objetivo: ±3 dB en zona de audiencia (excluyendo últimas filas). ±6 dB aceptable para venues grandes.

**B5. Separación temporal máxima entre arrays.**
Diferencia de llegada sistema principal vs refuerzo: <20ms ideal, <30ms aceptable, >50ms eco claro.

**B6. Ángulo de inclinación vertical (downtilt).**
Centro del lóbulo principal debe apuntar a 2/3 de la profundidad de la audiencia, no a la última fila.

**B7. Altura mínima de rigging.**
Caja inferior del array ≥ 2m por encima de la cabeza del espectador más cercano. z_bottom ≥ z_cabeza + 2m (z_cabeza ≈ 1.7m de pie, 1.2m sentado).

**B8. Overlap L/R en el centro.**
Overlap en Y=0: -3 a -6 dB por lado (suma = 0 dB). Si >0 dB por lado: comb filtering. Si <-10 dB: hueco central.

**B9. Relación directa/reverberante.**
SPL directo ≥ 6 dB por encima del campo reverberante en toda la audiencia para inteligibilidad. Si RT60 alto, mayor directividad o más absorción.

**B10. Posición del FOH.**
A 2/3 de la profundidad, centrado en Y=0, sin obstrucciones. Nunca debajo de balcón ni contra pared del fondo. Se puede usar como receiver_pos.

**B11. Splay en clusters point-source.**
Splay entre cajas ≈ 50-70% de la cobertura nominal. Cajas de 60° → splay 30-40°.

**B12. Ground stack vs flown.**
Ground-stack: mejor primeras filas, más reflexiones de piso. Flown: línea de visión limpia, primeras filas en off-axis vertical.

### 21.3 Recintos no amplificados / salas de concierto / ópera

**C1. RT60 objetivo según uso.**
Sinfónica: 1.8-2.2s. Cámara: 1.4-1.8s. Ópera: 1.2-1.6s. Recital: 1.3-1.7s. Teatro hablado: 0.6-1.0s. Multiuso: 1.2-1.6s. Comparar RT60 calculado con estos targets y sugerir ajustes de materiales.

**C2. Volumen por butaca.**
Sinfónica: 8-11 m³/butaca. Ópera: 6-8. Teatro hablado: 4-6. Multiuso: 7-9. Si el usuario da butacas y dimensiones, verificar la relación V/N.

**C3. Primeras reflexiones laterales (Lateral Fraction).**
Reflexiones laterales tempranas (5-80ms) dan envolvente y espacialidad. LF > 0.15 para buena impresión espacial. Paredes laterales cercanas (W < 20m) favorecen LF. Shoebox > abanico en LF.

**C4. Early Decay Time (EDT).**
EDT ≈ RT60 indica buen acoplamiento. EDT << RT60 (>30% menor): absorción excesiva cerca de fuente/audiencia. EDT >> RT60: energía temprana excesiva.

**C5. Claridad musical (C80).**
Rango ideal para música: -2 a +2 dB. C80 > +5 dB: sala demasiado seca. C80 < -5 dB: falta claridad.

**C6. Inteligibilidad (STI / C50).**
Teatro, conferencias, ópera: STI ≥ 0.60 (bueno), ≥0.75 (excelente). C50 ≥ -2 dB. Si RT60 > 1.5s y se usa para palabra, advertir STI insuficiente sin refuerzo.

**C7. Forma de planta.**
Shoebox (rectangular): mejor LF, uniforme. Abanico: mayor capacidad pero LF pobre. Viñedo: intimidad pero diseño complejo. Herradura (ópera): palcos absorben, RT60 controlado.

**C8. Concha orquestal.**
Modelar como objeto con paredes y techo reflectantes (madera dura 15-25mm). Sin concha, la energía del escenario se pierde en bambalinas.

**C9. Efecto de balcón (shadowing).**
Profundidad del balcón ≤ 2× altura libre debajo (D/H ≤ 2). Si D/H > 2, últimas filas bajo el balcón reciben energía reverberante insuficiente.

**C10. Superficies cóncavas — focalización.**
Paredes o techos curvos cóncavos concentran sonido en punto focal. Advertir si la extrusión tiene segmentos cóncavos con radio < 2× distancia a audiencia. Solución: difusión o facetas.

**C11. Flutter echo.**
Paredes paralelas + ambas reflectantes = flutter echo. Verificar paralelismo en extrusiones. Solución: absorción/difusión en al menos una, o splayed walls (>5°) si el usuario no dio las medidas (con medidas dadas, el recinto es el rectángulo de esas medidas: §52.1).

**C12. Foso de orquesta.**
Modelar como volumen con apertura hacia la sala. Boca más abierta: más directo de orquesta; más cerrada: la orquesta se mezcla antes de llegar.

### 21.4 Estadios y recintos al aire libre

**D1. Atenuación por distancia.**
Sin enclosure: -6 dB por duplicación de distancia + absorción atmosférica (significativa >2kHz a >50m). En throws >100m, pérdida HF puede ser >10 dB respecto a LF.

**D2. Efecto del viento.**
Viento a favor: sonido se curva hacia abajo (más alcance). Viento en contra: se curva arriba (sombra acústica). Recomendar +6 dB de reserva en venues expuestos.

**D3. Gradiente de temperatura.**
Día (caliente abajo): sonido se curva arriba (menos alcance). Noche/inversión térmica: se curva abajo (más alcance, quejas de ruido lejano).

**D4. Reflejo de piso (ground bounce).**
Ground stack: reflexión de piso genera cancelaciones en frecuencias específicas. Elevar array a 2-3m mejora el patrón. Modelar suelo reflectante como objeto.

**D5. Delay towers en estadios.**
Throws >60m: delay towers cada 30-50m. Cada tower se alinea al principal + 5-15ms de precedencia.

**D6. Cobertura de tribuna (rake angle).**
Audiencia en tribuna: ángulo vertical 20-40°. Cobertura vertical del array ≥ ángulo subtendido por la tribuna.

**D7. Límites de ruido (noise ordinance).**
Típicamente 65-75 dB(A) en límite de propiedad. Cobertura lo más directiva posible para minimizar spill.

**D8. SPL máximo en audiencia.**
Protección auditiva: ≤100 dB(A) LAeq,15min (EU). SPL pico primera fila ≤120 dB. Advertir si se superan.

**D9. Redundancia.**
Si un amplificador falla, la cobertura no debe caer >3 dB en ninguna zona. Sugerir L+R independientes.

**D10. Sistemas distribuidos vs central.**
Sin punto de rigging: cajas en postes (4-6m) cada 15-25m logran mejor uniformidad que sistema central lejano.

**D11. Pantalla LED como obstáculo.**
LED wall bloquea cobertura directa. Posicionar parlantes a los lados o por encima, nunca detrás. Si la pantalla >8m de ancho, outfills más abiertos.

### 21.5 Cine / Home Theater / Inmersivo Dolby Atmos

**E1. Canales de pantalla (L, C, R).**
Detrás de pantalla acústicamente transparente, a 2/3 de la altura, separación angular 45° entre L y R respecto al centro. C centrado horizontal y verticalmente.

**E2. Surrounds: distribución uniforme.**
Laterales (Lss/Rss): cobertura 60°-135° respecto al eje frontal. Traseros (Lrs/Rrs): 135°-150°. Separación entre parlantes adyacentes ≤3m.

**E3. Canales de altura (Atmos top).**
Elevación 30-55° respecto al oyente. Si techo <3m, la sensación de elevación se pierde. Mínimo 2.8m de altura libre.

**E4. LFE y modos en cine.**
No poner sub en esquina ni centrado. Recomendación: 2 subs en paredes opuestas o 4 en esquinas con EQ individual.

**E5. Nivel de referencia cinematográfico.**
85 dB(C) SPL por canal (83 dB LFE) a 2/3 de profundidad, centrado. Headroom mínimo +20 dB (105 dB sin distorsión).

**E6. RT60 para cine.**
Mucho más bajo que concierto: 0.3-0.5s (<150 butacas), 0.4-0.6s (medianas), 0.5-0.8s (>500 butacas). Inteligibilidad de diálogos es prioridad.

**E7. Absorción detrás de pantalla perforada.**
Mineral wool ≥100mm para evitar reflexiones de pared frontal que pasen a través de la pantalla con delay.

**E8. Baffle wall.**
Pared frontal continua (pantalla + paredes laterales al mismo nivel) elimina difracción de bordes. Parlantes screen como flush-mount.

**E9. Riser / escalonamiento.**
Audiencia en cine tiene riser para visibilidad. Modelar como planos inclinados, no horizontal. Afecta reflexiones de piso y cobertura vertical.

**E10. Zona de escucha extendida.**
En cine la zona ideal es un área (60% central), no un punto. Surrounds deben dar envolvente uniforme en toda esa zona.

---

## 22. Fórmulas acústicas para decisiones de diseño

> La IA puede usar estas fórmulas con aritmética simple para tomar mejores decisiones. No reemplazan la simulación de CADSFS — son heurísticas de diseño.

**F1. Frecuencia de Schroeder.**
`f_s = 2000 × √(RT60 / V)` donde V = volumen en m³. Por debajo de f_s el comportamiento es modal (ondas estacionarias). Todo tratamiento de graves debe operar por debajo de f_s.
- Ejemplo: estudio V=60m³, RT60≈0.4s → f_s = 2000×√(0.4/60) ≈ 163 Hz → bass traps deben absorber <163 Hz → lana mineral ≥200mm, no espuma de 50mm.

**F2. Distancia crítica.**
`d_c = 0.141 × √(Q × R)`, con `R = A / [(1 − ᾱ)·e^(−4mV/S)]` la constante de sala (Hopkins–Stryker con el aire): A es la absorción total en m² Sabins ---superficies, público y, en agudos, el aire (4mV)---, ᾱ la absorción media de las superficies y e^(−4mV/S) el aire del primer recorrido del directo. En graves y medios el aire no pesa y queda `R ≈ A / (1 − ᾱ)`; con ᾱ chico, R ≈ A. Q es la directividad del parlante **hacia la audiencia** (Q = 1 para caracterizar la sala sola). Es la definición que usa CADSFS en todos sus paneles desde R429. Los parlantes deben cubrir la audiencia dentro de 2× d_c para inteligibilidad.
- Ejemplo: Q=10 (line array), A=200 m² con ᾱ ≈ 0,2 → R = 250 m² → d_c ≈ 7,0 m. Más allá de d_c domina el campo reverberante; a 2× d_c (14 m) el reverberante ya está 6 dB por encima del directo.

**F3. ITDG (Initial Time Delay Gap).**
Intervalo entre sonido directo y primera reflexión fuerte. ITDG corto (<20ms): intimidad. ITDG largo (>30ms): grandeza. Estimar desde geometría: ITDG_techo ≈ 2×(H-1.2)/343 × 1000 ms; ITDG_lateral ≈ 2×(W/2)/343 × 1000 ms (para fuente y receptor en eje central).

**F4. RT60 estimado (Sabine simplificado).**
`RT60 ≈ K × V / A` donde A = Σ(Sᵢ × αᵢ) y K = 24·ln(10)/c = 0,1611 s/m con c = 343 m/s (el `c_m_s` del proyecto; CADSFS usa esa K exacta desde R430 y, en agudos, suma el aire: A + 4mV). Permite estimar si los materiales elegidos llevarán al RT60 objetivo. Si RT60 estimado >> objetivo, más absorción. Si << objetivo, reducir absorción o aumentar volumen.

**F5. Absorción excesiva.**
Si α_avg > 0.35, la sala pierde energía reverberante útil y se siente "muerta". Verificar que no se sobre-absorba al asignar materiales.

**F6. Frecuencia de coincidencia de paneles.**
`f_c ≈ c² / (1.8 × h × cL)` donde h = espesor del panel, cL = velocidad de flexión del material. Simplificado: vidrio 6mm ≈ 2100 Hz, yeso 12.5mm ≈ 3000 Hz, madera 18mm ≈ 1500 Hz. En doble acristalamiento, usar vidrios de distinto espesor para que no coincidan.

**F7. Masa-resorte-masa.**
`f₀ = 60 / √(m₁ × d)` donde m₁ = masa superficial (kg/m²), d = profundidad cavidad (m). Por debajo de f₀ el aislamiento mejora. Verificar que f₀ esté por debajo de la frecuencia más baja de interés.

**F8. Difusión vs absorción: criterio.**
Absorber: donde hay problemas (flutter, primeras reflexiones fuertes, control de RT60). Difundir: donde se quiere mantener energía pero mejorar uniformidad (pared trasera de CR, techos de salas de concierto). Nunca poner espuma acústica esperando que controle graves — solo absorbe >500Hz.

**F9. Puertas y ventanas — eslabón débil.**
Pared STC 60 + puerta STC 25 → aislamiento compuesto ≈ 35 dB. Estudios: doble puerta con air lock. Ventanas: doble/triple vidrio con cámara ≥100mm, vidrios de distinto espesor.

**F10. Orientación vs ruido exterior.**
Paredes con mayor STC hacia la fuente de ruido. Ventana de control (menor STC) en el lado protegido.

---

## 23. Interpretación de imágenes y planos

> Directrices para cuando el usuario adjunta una imagen (plano, foto, render) y la IA debe interpretar geometría, materiales y disposición.

**G1. Extracción de escala.**
Si hay barra de escala, usarla. Si no, usar referencias: puertas estándar (0.80-0.90m), silla de escritorio (0.55m), mesa de mezcla (1.8m ancho), piano de cola (2.7m). SIEMPRE declarar al usuario: "Estimé las dimensiones usando la puerta visible como referencia de 0.85m."

**G2. Planta sin sección: inferir altura.**
Si solo hay vista en planta, inferir altura según tipo:
- Estudio/CR: 2.8-3.5m
- Sala de ensayo: 3.0-4.0m
- Conciertos <300 butacas: 6-8m
- Conciertos 300-1000: 8-12m
- Conciertos >1000: 12-18m
- Teatro/ópera: 10-15m
- Iglesia: 8-15m (nave), 15-25m (catedral)
- Estadio cubierto: 15-25m
SIEMPRE declarar: "La altura no se ve en el plano; estimé Xm. Podés ajustarla."

**G3. Códigos gráficos arquitectónicos.**
Líneas gruesas = muros estructurales (hormigón, mampostería). Dobles finas = tabiques (yeso). Arcos en puertas = aberturas. Punteadas = proyecciones (balcones). Achurado = corte de material. Interpretar para asignar materiales correctos.

**G4. Orientación escenario/audiencia.**
Buscar: escenario elevado, butacas orientadas, mesa de mezcla, consola, parlantes visibles, telón, concha orquestal. Sin indicadores claros: preguntar antes de asumir.

**G5. Múltiples recintos.**
Preguntar cuál diseñar primero. Nunca intentar 3+ recintos en una sola respuesta — la complejidad es excesiva.

**G6. Simplificación de geometría irregular.**
Simplificar a vértices acústicamente significativos (cambios >15° o >0.3m). Un nicho de 5cm para tubería no afecta la acústica.

**G7. Anotaciones del usuario.**
Flechas, círculos, texto sobre la imagen son instrucciones prioritarias. "Escenario aquí", "ventana", medidas a mano → prioridad sobre inferencia automática.

**G8. Fotos vs planos técnicos.**
Foto del espacio real: inferir con cautela. Declarar: "Desde la foto estimo dimensiones aproximadas; para mayor precisión, proporcioná medidas o plano acotado."

**G9. Corte/sección.**
Priorizar: altura real, forma de techo (plano/inclinado/abovedado), balcones, escalonamiento de audiencia, altura de rigging. El corte da información que la planta no da.

**G10. Mobiliario acústico visible.**
Paneles, difusores, bass traps, clouds en el plano → modelar como objetos internos con materiales apropiados.

**G11. Renders 3D e inferencia de materiales.**
Madera clara = Madera (panel). Tela gris = Cortina pesada. Hormigón visto = Hormigón rugoso / encofrado. Vidrio = Vidrio. Declarar las inferencias.

**G12. Imagen borrosa o incompleta.**
Si no se ve bien, declarar qué partes no se pueden interpretar y pedir aclaraciones. Nunca completar con suposiciones silenciosas.

---

## 24. Copia de salas famosas

> Directrices para cuando el usuario pide "haceme un venue como X" o "copiá la sala Y".

**H1. Parámetros de salas de referencia mundial.**

| Sala | Tipo | Butacas | V (m³) | RT60 (s) | Dimensiones aprox. |
|------|------|---------|--------|----------|-------------------|
| Musikverein (Viena) | Shoebox | 1680 | 15000 | 2.0 | 53×20×18m |
| Concertgebouw (Amsterdam) | Shoebox | 2036 | 18700 | 2.2 | 44×28×17m |
| Boston Symphony Hall | Shoebox | 2625 | 18750 | 1.9 | 57×23×19m |
| Berlin Philharmonie | Viñedo | 2440 | 26000 | 2.0 | 60×44×22m |
| Walt Disney Concert Hall | Viñedo | 2265 | 19000 | 2.0 | 58×40×21m |
| Teatro Colón (Buenos Aires) | Herradura | 2487+500 | 20000 | 1.8 | 75×30×28m |
| Sydney Opera House (Concert) | Abanico mod. | 2679 | 24600 | 2.0 | 52×35×25m |
| Sagrada Familia (Barcelona) | Catedral | — | 45000 | 8-10 | 90×60×45m |
| Abbey Road Studio One | Rectangular | — | ~5400 | 2.2 | 28×16×12m |
| Abbey Road Studio Two | Rectangular | — | ~1300 | 1.7 | 17×11×7m |
| Capitol Studios A | Rectangular | — | ~2500 | 1.5 | 18×14×10m |

**H2. Escalar manteniendo proporciones.**
"Musikverein para 500 personas": NO escalar linealmente. Mantener proporciones L:W:H (≈2.9:1.1:1 para Musikverein). Ajustar volumen: 500 × 9m³ = 4500m³ → ~31×12×11m.

**H3. Rasgo acústico dominante.**
- Shoebox (Musikverein, Boston): paredes laterales paralelas cercanas → LF alto → envolvente.
- Viñedo (Berlín, Disney): terrazas envolventes → intimidad + reflexiones múltiples.
- Herradura (Colón, La Scala): palcos absorben energía → RT60 controlado + intimidad.
- Abanico: mayor capacidad pero LF bajo → requiere difusión lateral.
Si se pierde el rasgo al escalar, advertir.

**H4. Datos no publicados.**
Si no hay parámetros verificados de la sala pedida, declararlo: "No tengo datos acústicos verificados de esta sala. Puedo diseñar con geometría similar, pero materiales y RT60 serán estimaciones."

**H5. Adaptar al contexto local.**
Si el espacio disponible no permite las dimensiones de la referencia, adaptar los principios (tipo, proporciones, materialidad) y declarar las diferencias.

**H6. Materialidad histórica → moderna.**
Yeso ornamentado ≈ Yeso liso pintado. Terciopelo de butacas ≈ Butaca tapizada (ocupada). Madera de escenario ≈ Parquet de madera barnizado. Mármol ≈ Hormigón pulido (microrelieve). Traducir manteniendo propiedades acústicas.

**H7. Acústica variable.**
Salas con cortinas retráctiles, paneles giratorios, cámaras de reverberación: modelar UNA configuración y declarar cuál.

**H8. Copiar estudio desde fotos.**
Inferir monitores por apariencia (Genelec=verdes/grises redondeados, ATC=negros con SL, KRK=amarillos). Tratamiento visible (paneles, bass traps, skyline). Declarar que son inferencias visuales.

**H9. Variar proyecto existente.**
Si el usuario tiene un .csm y quiere variarlo ("igual pero más grande"), partir del estado actual, aplicar cambios pedidos, no rediseñar desde cero.

**H10. Venues deportivos.**
Simplificar: tribuna = plano inclinado, techo = plano superior, cancha = plano reflectante a Z=0. No modelar cada escalón ni estructura metálica.

---

## 25. Inferencia y completado automático

> Directrices para que la IA complete información faltante, detecte incoherencias y adapte el nivel de detalle.

**I1. Defaults por tipo de recinto.**
Si el usuario da dimensiones pero no materiales:
- **Estudio**, con el tratamiento en objetos (lo normal en un diseño, §26.2): paredes y techo=`Pladur / placa de yeso (sobre perfilería)`, piso=`Parquet de madera barnizado`, frontal=`Lana mineral (roca) 50 mm (pared rígida)` (§52.5). Sin objetos: paredes=`Lana mineral (roca) 50 mm (pared rígida)`, techo=`Placa de techo fibra mineral 18 mm (σ≈15k) + plenum 200 mm`, piso=`Alfombra ligera (sin underlay)`, frontal=`Lana mineral (roca) 50 mm (pared rígida)` (con monitores en pie, el frente absorbe: A15)
- **Sala de conciertos**: paredes=`Madera maciza barnizada (panel)`, techo=`Yeso liso pintado`, piso=`Parquet de madera barnizado`, escenario=`Parquet de madera barnizado`
- **Teatro**: butacas=`Butaca tapizada (ocupada)`, piso=`Alfombra ligera (sin underlay)`, paredes=`Yeso liso pintado`, escenario=`Parquet de madera barnizado`
- **Venue amplificado**: paredes=`Hormigón rugoso / encofrado`, techo=`Acero pintado / chapa`, piso=`Hormigón pulido (microrelieve)`
- **Cine**: paredes=`Cortina pesada (100% fruncido)`, techo=`Placa de techo fibra mineral 20 mm (σ≈8k) + plenum 200 mm`, piso=`Alfombra ligera (sin underlay)`

**I2. Inferir tipo desde contexto.**
"Monitores Genelec" → estudio. "Line array d&b" → venue amplificado. "Orquesta" o "cuarteto" → no amplificado. "Público de pie" → venue amplificado. "Tribuna" → estadio. "Pantalla" + "LCR" → cine.

**I3. Preguntar solo si la ambigüedad es crítica.**
Tipo de recinto indeterminado y RT60 varía 0.4s vs 2.0s → preguntar. Carpet vs wood en área secundaria → decidir y mencionar.

**I4. Reutilizar configuración existente.**
Si el proyecto ya tiene parlantes/materiales y el usuario pide rediseñar la sala, mantener speaker_systems existentes y cambiar solo lo pedido. Lo que se modifica va con comandos (§51). Si hay que mandar el JSON completo de otra sala, los parlantes que se quieran conservar van **dentro** de ese JSON, con las posiciones de la sala nueva: el programa no le suma a otra sala nada del proyecto anterior.

**I5. Detectar incoherencias.**
RT60=0.3s en 20000m³, monitores nearfield en estadio, line array en cuarto 4×3m → advertir, no ejecutar ciegamente.

**I6. Intención sobre literalidad.**
"Un JBL en cada esquina" probablemente = cobertura distribuida, no literalmente en esquinas apuntando a paredes. Interpretar la intención acústica y explicar la propuesta profesional.

**I7. Lo que se pide, completo.**
Un pedido de diseño («diseñame un estudio», «cómo sería un estudio acá») se entrega completo: todos los objetos, materiales y assemblies, como si fuera el diseño final y no un borrador. Un pedido sólo geométrico («una sala de 8×8×3») se entrega tal cual y se ofrece el resto en una línea (§26.1). Agregar lo que no se pidió no es detalle: es otro pedido.

**I8. Documentar decisiones.**
Justificar en lenguaje natural: "Elegí paredes absorbentes porque la distancia monitor-pared es <1m" o "Difusión en pared trasera para mantener energía sin reflexiones especulares." Esto educa al usuario.

---

## 26. Nivel de detalle — lo que se pide; el máximo, cuando se pide un diseño

> Cuando se pide DISEÑAR un recinto (se dice el uso o el tipo, o se pide el tratamiento), la IA genera el diseño más detallado y completo posible: una simulación realista del espacio, no un esquema. La regla: si un acústico profesional lo incluiría en un modelo de simulación, la IA también. Cuando se pide sólo una geometría, se entrega esa geometría (§26.1).

### 26.1 Principio fundamental

**Hacé lo que se pide.** Si el pedido es sólo la geometría ---medidas o forma, sin decir para qué es: «una sala de 8×8×3», «un recinto de 10×6×4», «hazme una caja de 5×4×3»---, entregá **esa** sala: el recinto, un material real en cada superficie (neutro si no se sabe el uso: yeso pintado, hormigón, parquet o alfombra) y `source_pos` y `receiver_pos` (§8). **Sin tratamiento, muebles ni parlantes que no se pidieron.** Al final, en una línea, ofrecé lo que agregarías y para qué («¿Le agrego tratamiento para un control room, o es para otro uso?»). El caso que motivó esta regla (26/09/2026): a «Hazme una sala de 8×8×3» la IA le agregó dos paneles y una trampa que nadie pidió, y encima mal puestos.

Cuando el pedido dice el uso o el tipo, o pide tratamiento, vale todo lo que sigue. Si dice el
tipo **y** las medidas («un control room de 3x4x3»), el tipo manda el detalle y las medidas mandan
el recinto (§52.1).

**NUNCA entregar una sala de un tipo vacía, con solo superficies y parlantes.** Un recinto real tiene puertas, ventanas, mobiliario, tratamiento acústico, escenario, audiencia. Todo eso afecta la simulación (RT60, modos, cobertura, STI) y debe estar presente. Si el usuario pide "diseñame un estudio", la respuesta debe incluir la sala, el tratamiento acústico completo (absorción, difusión, bass traps), la mesa de mezcla como objeto, los racks de equipamiento, la ventana de control, las puertas, el piso flotante en el assembly, el techo desacoplado — no solo una caja con dos monitores.

### 26.2 Qué incluir SIEMPRE como objetos internos

**En TODOS los recintos:**
- Puertas (con assembly que modele su TL — madera maciza, doble puerta, etc.)
- Ventanas (con assembly multicapa — vidrio simple, doble, triple)
- Columnas estructurales si las hay (afectan reflexiones y modos)
- Cualquier nicho, escalón o cambio de nivel significativo (>0.3m)

**En estudios / control rooms:**
- Mesa de mezcla / escritorio (afecta reflexiones tempranas al sweet spot)
- Racks de equipamiento (absorben algo, reflejan a frecuencias altas)
- Sofá de clientes (absorción significativa en medios)
- Paneles absorbentes en puntos de primera reflexión (calcular posiciones)
- Difusores en pared trasera (QRD/skyline como objetos)
- Bass traps en triedros/esquinas (como objetos con material de alta absorción)
- Cloud de techo (panel suspendido sobre sweet spot)
- Ventana de control CR↔Live Room: una abertura (§28), con assembly de vidrio multicapa (A13)
- Doble puerta / airlock si hay aislamiento

Un control room con todo esto, calculado y probado: §52.5.

**En salas de concierto / teatro:**
- Butacas como volumen de audiencia (absorción significativa — la audiencia es el material más absorbente de la sala)
- Escenario como plataforma elevada (madera, reflectante)
- Concha orquestal si aplica (paredes reflectantes de madera)
- Balcones como objetos con su piso y antepecho
- Foso de orquesta si es ópera
- Cortinas / telones si existen (absorción pesada)
- Órgano de tubos si existe (difusor natural gigante)

**En venues amplificados:**
- Escenario / stage como plataforma
- Barras de seguridad / barriers frente al escenario
- Cabina de FOH / mesa de sonido como objeto
- Balcones / mezanines
- Barras/mostradores si afectan el volumen
- Pantallas LED si obstruyen cobertura

**En cine / home theater:**
- Pantalla (opaca o perforada, con su material)
- Risers / escalonamiento de butacas
- Paso acústico detrás de pantalla (volumen con absorción)

**En aire libre:**
- Plano de suelo con material (pasto, concreto, tierra)
- Estructura de escenario (techo, paredes laterales)
- Tribunas/gradas como planos inclinados
- Barreras acústicas si las hay

### 26.3 Materiales: siempre diferenciados por superficie

NUNCA asignar el mismo material a todas las superficies. Un recinto real tiene:
- **Piso**: tipo específico (parquet, alfombra, concreto, goma, flotante)
- **Techo**: tipo específico (yeso, acústico suspendido, concreto expuesto, metal deck)
- **Cada pared**: puede tener tratamiento distinto (frontal ≠ trasera ≠ laterales)
- **Objetos**: material propio (madera, vidrio, tela, metal)

Para estudios, la diferenciación es particularmente importante:
- Pared frontal: absorbente detrás de monitores en pie (SBIR, A15); reflectante sólo si
  van empotrados (flush-mount)
- Paredes laterales en zona RFZ: absorbente
- Paredes laterales fuera de RFZ: difusión o mezcla
- Pared trasera: difusión (QRD/skyline) o absorción+difusión
- Techo zona sweet spot: absorción (cloud)
- Techo zona trasera: difusión o reflectante
- Piso: alfombra gruesa o piso flotante de madera

Cuando el tratamiento va en objetos (paneles, nube, trampas, difusores), las superficies del
recinto van reflectantes, salvo el frente, y la absorción se reparte en los tres ejes: el
frente y el fondo, las dos laterales, el piso y el techo (§52.5).

### 26.4 Assemblies: siempre multicapa para estudios y aislamiento

En recintos que requieren aislamiento (estudios, cines, salas de ensayo), NUNCA generar assemblies de una sola capa. La realidad constructiva siempre tiene múltiples capas:
- Pared mínima: yeso + estructura + aislante + yeso (4 capas)
- Pared de estudio: yeso doble + estructura + lana mineral + cámara de aire + yeso doble (6+ capas)
- Piso flotante: losa + aislador + contrapiso + terminación (4 capas)
- Techo desacoplado: yeso + suspensión resiliente + cavidad + lana + losa (5 capas)
- Ventana de control: vidrio + cámara + vidrio (3 capas mínimo, espesores distintos)
- Puerta de estudio: hoja maciza + burlete + cámara + hoja maciza (doble puerta)

### 26.5 Assemblies: completar incluso para recintos no aislados

Incluso para recintos que no requieren aislamiento especial (salas de concierto, venues), los assemblies DEBEN existir para modelar correctamente el TL:
- Pared de hormigón: concrete_200 (una capa, pero ESPECIFICAR el espesor)
- Pared de ladrillo: brick_150 + enlucido (2 capas)
- Techo metálico: steel_deck_1.5 (una capa)
- Vidriado: glass_6 (o multicapa si es doble)
- Esto permite que CADSFS calcule correctamente la pérdida de transmisión entre el interior y el exterior.

---

## 27. Inferencia avanzada — Cómo copiar y recrear

> Directrices específicas para cuando la IA debe recrear un espacio existente a partir de referencias (nombre, foto, plano, descripción verbal).

### 27.1 Cuando el usuario dice "haceme X sala"

Proceso obligatorio:
1. **Identificar** la sala (buscar en datos de §24 si es famosa, o deducir tipo)
2. **Geometría**: dimensiones, forma de planta, altura, balcones, escenario
3. **Acústica**: RT60 objetivo, materiales típicos del tipo/época
4. **Sistemas de sonido**: solo si aplica (venue amplificado, estudio) o si el usuario lo pide
5. **Objetos internos**: butacas, escenario, concha, balcones, columnas, tratamiento acústico
6. **Assemblies**: composición constructiva de paredes, piso, techo
7. **Source/receiver**: posiciones correctas según el tipo
8. **Explicación**: describir cada decisión y qué se preservó de la referencia

NUNCA entregar solo el paso 2 (geometría) y omitir los pasos 3-8. Si no hay información para algún paso, usar los defaults del tipo de recinto (§25 I1) y declararlo.

Esto vale cuando X es un tipo o una sala real («un control room», «el Colón»). Si X es sólo una medida («haceme una sala de 8×8×3»), no es un tipo: §26.1.

### 27.2 Cuando el usuario adjunta una imagen

Proceso obligatorio:
1. **Describir lo que se ve**: "Veo un plano en planta de un control room de aproximadamente 5×4m con una ventana grande en la pared +X y una puerta en la pared -Y"
2. **Calibrar escala** (§23 G1): declarar la referencia usada
3. **Extraer geometría**: polígono de extrusión con todos los vértices significativos
4. **Identificar elementos**: puertas, ventanas, mobiliario, tratamiento acústico visible
5. **Inferir lo que no se ve**: altura (§23 G2), materiales de paredes, tratamiento acústico necesario
6. **Generar con máximo detalle**: incluyendo todos los objetos detectados + los inferidos como necesarios
7. **Declarar inferencias**: separar lo medido/visto de lo supuesto/inferido

NUNCA saltar del paso 1 al paso 6 sin los pasos intermedios. La descripción (paso 1) es crítica porque el usuario puede corregir interpretaciones erróneas antes de que se aplique el diseño.

### 27.3 Deducción de tratamiento acústico desde el tipo de recinto

Cuando se pide diseñar un recinto de un tipo y no se especifica el tratamiento, la IA lo infiere. Con un pedido sólo geométrico no se infiere: se ofrece (§26.1).

**Estudio de grabación (live room):**
- Paredes: combinación de superficies reflectantes (madera) y absorbentes (paneles) — nunca todo igual
- Techo: parcialmente absorbente (difusores + absorción)
- Piso: madera flotante (reflectante, para brillo)
- Esquinas: bass traps
- Diseño variable si es posible (paneles giratorios para cambiar RT60)

**Control room:**
- Zona RFZ: absorción total en primeras reflexiones laterales + techo
- Zona trasera: difusión (QRD, policilíndricos, skyline)
- Pared frontal: reflectante (o flush-mount para monitores)
- Piso: alfombra (absorción para reducir reflexión del escritorio)
- Esquinas superiores: bass traps siempre
- Cloud sobre sweet spot

**Sala de conciertos:**
- Escenario: madera reflectante
- Paredes laterales: parcialmente difusas (molduras, pilastras, balcones)
- Techo: reflectante con difusión (coffered ceiling, nubes reflectoras)
- Pared trasera: absorbente o muy difusa (evitar eco de fondo)
- Piso de audiencia: parcialmente absorbente (butacas tapizadas + pasillo alfombrado)

**Teatro:**
- Similar a concierto pero con más absorción (RT60 más bajo)
- Cortinas/telones como absorbentes pesados
- Proscenio y bambalinas: absorbentes

**Venue amplificado:**
- Mínimo tratamiento (hormigón, acero) — la acústica se controla con los parlantes
- Pero si RT60 es excesivo (>3s), recomendar absorción en techo y pared trasera

**Cine:**
- Todas las paredes: tela absorbente sobre lana mineral
- Techo: absorbente pesado
- Piso: alfombra
- Detrás de pantalla: absorción total
- Meta: RT60 muy bajo (0.3-0.6s)

### 27.4 Deducción de sistemas de sonido desde el tipo de recinto

Si el usuario no especifica parlantes pero el tipo lo requiere:

**Estudio/CR (sin indicar formato):** stereo L/R con monitores nearfield apropiados al tamaño de la sala:
- Sala <15m²: Genelec 8020D o Neumann KH 80
- Sala 15-25m²: Genelec 8030C o Adam A7V o Yamaha HS7
- Sala 25-40m²: Genelec 8040B o Neumann KH 120 II o ATC SCM25A
- Sala >40m²: ATC SCM45A o Neumann KH 150 o Focal Shape 65

**Estudio con formato surround:** agregar surround + LFE al par stereo. El formato depende del uso:
- Mezcla para cine → 5.1 o 7.1
- Mezcla inmersiva → 7.1.4 Atmos
- Masterización: stereo o 5.1

**Venue amplificado (<500 personas):** par L/R point source + 1-2 subs
**Venue amplificado (500-2000):** par L/R line array (6-8 cajas) + sub array
**Venue amplificado (>2000):** L/R line array (8-12 cajas) + outfills + sub array + delays
**Sala de concierto/ópera:** sin sistema a menos que se pida
**Cine:** sistema screen L/C/R + surrounds + LFE + tops si Atmos

### 27.5 Deducción de dimensiones desde la capacidad

Si el usuario da la capacidad pero no las dimensiones:

**Butaca estándar:** 0.55m de ancho × 0.90m de profundidad (entre filas)
**Público de pie:** 2-3 personas/m²
**Pasillos:** central 1.5m, laterales 1.0m
**Escenario:** 8-15m de boca × 8-12m de profundidad (según tamaño de sala)

Ejemplo: "auditorio para 600 personas sentadas"
- 600 butacas a 0.50m² efectivos/butaca = 300m² de audiencia
- Con pasillos y circulación: ×1.35 = 405m²
- Audiencia rectangular: 27m de profundidad × 15m de ancho
- + escenario 12m × 10m = 120m²
- Total planta: ~37m × 15m
- Altura por V/butaca (8m³): V = 4800m³ → H ≈ 4800/555 ≈ 8.6m → usar 9m

### 27.6 Deducción desde el nombre del venue

Cuando el usuario nombra un venue real pero no famoso ("haceme el Movistar Arena de Buenos Aires", "copiá la Usina del Arte"):
1. Si la IA conoce datos del venue, usarlos
2. Si no tiene datos concretos, deducir el tipo (arena → estadio cubierto, usina → sala multiuso reconvertida) y aplicar los defaults de ese tipo
3. Declarar: "No tengo las dimensiones exactas del venue; diseño uno del mismo tipo con los estándares acústicos correspondientes. Si tenés un plano o foto, compartilo para mayor fidelidad."

### 27.7 Nivel de detalle: escala de complejidad

Para guiar la cantidad de objetos y detalle:

| Tipo de recinto | Objetos internos mínimos | Assemblies mínimos |
|-----------------|-------------------------|-------------------|
| Estudio/CR pequeño (<20m²) | 8-12 (mesa, paneles×4, bass traps×4, puerta, ventana, cloud) | 4-5 (pared, piso flotante, techo desacoplado, ventana, puerta) |
| Estudio/CR mediano (20-40m²) | 12-18 (+ racks, sofá, difusores traseros) | 5-6 |
| Sala de conciertos | 6-10 (escenario, butacas×1-3 zonas, balcón, concha, columnas) | 3-4 (pared principal, techo, piso, vidriado si hay) |
| Teatro | 8-12 (escenario, butacas, balcón, foso, cortinas, proscenio) | 3-4 |
| Venue amplificado | 4-8 (escenario, barras, FOH, balcón si hay) | 2-3 |
| Cine | 6-10 (pantalla, risers×2-3, paso behind screen, paredes cortina) | 3-4 |
| Aire libre | 3-6 (suelo, escenario+techo, tribunas, barreras) | 1-2 |

Estos son MÍNIMOS. La IA siempre puede agregar más detalle si la información está disponible.

### 27.8 Nombres descriptivos para objetos y sistemas

Nunca usar nombres genéricos ("Objeto 1", "Sistema 1"). Usar nombres que describan función y posición:
- Objetos: "Bass trap esquina NE sup", "Difusor QRD pared trasera", "Mesa de mezcla", "Ventana CR-LR", "Puerta doble entrada", "Cloud techo sweet spot", "Panel absorción lateral L", "Escenario madera", "Butacas platea baja", "Balcón nivel 2"
- Sistemas: "Monitores Stereo L/R", "Surround 5.1 ATC", "PA Principal L", "PA Principal R", "Outfill L", "Outfill R", "Sub Array Central", "Delay Tower Fondo", "Front Fill Boca"

### 27.9 Coherencia geométrica entre objetos

Todos los objetos deben respetar la geometría del recinto:
- Los paneles acústicos se apoyan en las paredes: su cara de atrás coincide con la pared, así que el centro va a medio espesor hacia adentro (§0.5, «Dónde va el centro»)
- Los bass traps van en las esquinas: dos de sus caras coinciden con dos paredes
- La mesa de mezcla está delante del sweet spot (receiver_pos + offset en -X)
- Las butacas cubren la zona de audiencia (entre source_pos y receiver_pos)
- El escenario está en la zona de source_pos
- Los balcones están adosados a paredes y tienen objetos debajo y encima

NUNCA poner objetos flotando en el medio sin relación con la geometría del recinto.

---

## 28. Aberturas (Openings) — Puertas, ventanas y huecos

> Las aberturas recortan visualmente la pared y asignan material/assembly propio a la zona del hueco. Acústicamente cada abertura es una región de la pared con propiedades distintas (absorción, TL). También se pueden crear en techo y piso (claraboyas, huecos de escalera, etc.).

### 28.1 Formato JSON

Las aberturas se definen dentro del `enclosure`:

```json
{
  "enclosure": {
    "kind": "extrude",
    "polygon": [[-3,-2.1], [-3,2.1], [3,2.1], [3,-2.1]],
    "height": 3.0,
    "openings": [
      {
        "wall": 2,
        "name": "Ventana CR-LR",
        "type": "window",
        "pos_along": 0.8,
        "pos_up": 0.9,
        "width": 1.5,
        "height": 1.2,
        "material_a": "Vidrio (ventana)",
        "assembly_id": "asm_ventana_doble"
      },
      {
        "wall": 0,
        "name": "Puerta principal",
        "type": "door_closed",
        "pos_along": 1.5,
        "pos_up": 0.0,
        "width": 0.9,
        "height": 2.1,
        "material_a": "Madera maciza barnizada (panel)",
        "assembly_id": "asm_puerta_maciza"
      },
      {
        "wall": 3,
        "name": "Pasillo a Live Room",
        "type": "door_open",
        "pos_along": 1.0,
        "pos_up": 0.0,
        "width": 1.2,
        "height": 2.4
      },
      {
        "wall": 1,
        "name": "Ventana alta decorativa",
        "type": "window",
        "pos_along": 2.0,
        "pos_up": 2.0,
        "width": 1.0,
        "height": 0.8,
        "material_a": "Vidrio (ventana)"
      },
      {
        "wall": -2,
        "name": "Claraboya techo",
        "type": "window",
        "pos_along": 1.5,
        "pos_up": 1.0,
        "width": 1.0,
        "height": 1.0,
        "material_a": "Vidrio (ventana)"
      }
    ]
  }
}
```

### 28.2 Campos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `wall` | int | Índice de la pared (0..N-1 del polígono de extrusión). **-1 = Piso, -2 = Techo** |
| `name` | str | Nombre descriptivo — aparece como face group en el viewport |
| `type` | str | Tipo de abertura (ver tabla abajo) |
| `pos_along` | float | Distancia en metros desde el vértice inicial de la pared al borde izquierdo de la abertura. Para piso/techo: offset X desde el borde mínimo del bounding box |
| `pos_up` | float | Distancia en metros desde el piso al borde inferior. Para piso/techo: offset Y desde el borde mínimo del bounding box. **Libre para todos los tipos** (ventanas a media altura, huecos en el medio de la pared, etc.) |
| `width` | float | Ancho de la abertura en metros |
| `height` | float | Alto de la abertura en metros |
| `material_a` | str | Material cara interior. DEBE ser un nombre real de la DB (§2). Default automático: `Vidrio (ventana)` (window), `Madera maciza barnizada (panel)` (door_closed), `open_air_WxH` (door_open/opening) |
| `material_b` | str | Material cara exterior. Default: igual a material_a |
| `assembly_id` | str | ID del assembly en `wall_assemblies` para el TL de esta abertura |

### 28.3 Tipos de abertura

| Tipo | Descripción | Material default | Rendering |
|------|-------------|-----------------|-----------|
| `window` | Ventana cerrada | `Vidrio (ventana)` (α≈0.03) | Color vidrio (celeste claro) |
| `door_closed` | Puerta cerrada | `Madera maciza barnizada (panel)` (α≈0.10) | Color madera |
| `door_open` | Puerta abierta | `open_air_WxH` (α dependiente de frecuencia) | Casi transparente (hueco visible) |
| `opening` | Hueco permanente (arco, pasillo, comunicación entre salas) | `open_air_WxH` (α dependiente de frecuencia) | Casi transparente |

### 28.4 Comportamiento acústico

- **`window`**: la región de ventana tiene coeficiente de absorción de vidrio (muy bajo, α≈0.03) y TL del assembly de vidrio multicapa. El resto de la pared mantiene su material original.
- **`door_closed`**: igual que window pero con α y TL de madera/metal.
- **`door_open` / `opening`**: filtro pasa-altos dependiente de frecuencia. f_c = 343/(2×d_min) donde d_min es el menor de width/height. Arriba de f_c: α=0.99 (transparente). Debajo de f_c/4: α=0.05 (refleja). Transición smoothstep entre ambos. Ejemplo: puerta 0.9m → f_c≈191Hz; pasillo 2m → f_c≈86Hz.
- **TL compuesto**: CADSFS calcula el TL de cada superficie por separado. Una pared con STC 55 y una ventana con STC 30 dará un aislamiento compuesto ponderado por área — la ventana domina.

### 28.5 Impacto en la simulación

- **RT60**: las aberturas abiertas actúan como absorción dependiente de frecuencia (alta en agudos). Una puerta abierta de 2m² en una sala de 100m² de superficie reduce el RT60 en HF notablemente.
- **Reflexiones (ISM/RT)**: los rayos que pegan en la abertura rebotan con el α del material asignado. Para `open_air`, el rayo se termina en HF.
- **Modos**: la geometría sigue cerrada (la abertura tiene caras) → el cálculo modal funciona normalmente.
- **Cobertura (SPL)**: la cobertura directa no se afecta. La cobertura con campo reverberante sí, porque RT60 cambia.

### 28.6 Aberturas en Techo y Piso

Para claraboyas, huecos de escalera, bocas de escenario, etc.:

- `wall: -1` → Piso
- `wall: -2` → Techo
- `pos_along` y `pos_up` son offsets X e Y respectivamente desde la esquina mínima del bounding box del polígono
- La abertura reasigna triángulos existentes del piso/techo cuyo centroide cae dentro del rectángulo

```json
{
  "wall": -2,
  "name": "Claraboya central",
  "type": "window",
  "pos_along": 2.0,
  "pos_up": 1.5,
  "width": 1.5,
  "height": 1.5,
  "material_a": "Vidrio (ventana)",
  "assembly_id": "asm_claraboya"
}
```

### 28.7 Ejemplo completo: Control Room con ventana y puerta

```json
{
  "enclosure": {
    "kind": "extrude",
    "polygon": [[-3,-1.6], [-3,1.6], [-2.5,1.9], [3,2.1], [3,-2.1], [-2.5,-1.9]],
    "height": 3.0,
    "openings": [
      {
        "wall": 0,
        "name": "Ventana CR-LR",
        "type": "window",
        "pos_along": 0.7,
        "pos_up": 1.0,
        "width": 1.8,
        "height": 0.9,
        "material_a": "Vidrio (ventana)",
        "assembly_id": "asm_ventana_doble"
      },
      {
        "wall": 3,
        "name": "Puerta entrada",
        "type": "door_closed",
        "pos_along": 0.3,
        "pos_up": 0.0,
        "width": 0.9,
        "height": 2.1,
        "material_a": "Madera maciza barnizada (panel)",
        "assembly_id": "asm_puerta_doble"
      }
    ]
  },
  "wall_assemblies": {
    "asm_ventana_doble": {
      "layers": [
        {"material_id": "glass_6", "thickness_mm": 6, "bonded_with_prev": true},
        {"material_id": "air_100", "thickness_mm": 100, "bonded_with_prev": false},
        {"material_id": "glass_10", "thickness_mm": 10, "bonded_with_prev": true}
      ]
    },
    "asm_puerta_doble": {
      "layers": [
        {"material_id": "wood_45", "thickness_mm": 45, "bonded_with_prev": true},
        {"material_id": "air_50", "thickness_mm": 50, "bonded_with_prev": false},
        {"material_id": "wood_45", "thickness_mm": 45, "bonded_with_prev": true}
      ]
    }
  }
}
```

La ventana CR↔LR va en la pared del **frente** (`wall: 0`, la de x = −3), centrada
(`pos_along = (3,2 − 1,8)/2 = 0,7`) y por encima de la mesa (`pos_up = 1,0`): el ingeniero
mira el live room por encima de los monitores. La puerta, en el **fondo** (`wall: 3`). Hasta
la v43 este ejemplo ponía la ventana en el fondo, detrás del ingeniero, y la puerta en el
frente, detrás de los monitores. Las paredes que tienen aberturas **conservan su material**
(§29.1).

### 28.8 Reglas para la IA

- SIEMPRE incluir puertas y ventanas como `openings` del enclosure, NUNCA como objetos separados superpuestos
- **Materiales REALES de la DB**: `Vidrio (ventana)` (NO `glass_window`), `Madera maciza barnizada (panel)` (NO `wood_door_solid`). Ver tabla en §2
- Para estudios: ventana CR↔LR siempre con vidrios de distinto espesor (6mm + 10mm mínimo) y cámara ≥100mm
- `pos_up` es libre para todos los tipos: puertas normalmente 0.0, ventanas 0.8-1.0m, pero se puede poner un hueco a cualquier altura
- Si el usuario menciona "puerta abierta" o "comunicación entre salas": usar `type: "door_open"` o `type: "opening"`
- Toda abertura con aislamiento debe tener `assembly_id` apuntando a un assembly en `wall_assemblies`
- `name` debe ser descriptivo: "Ventana CR-LR", "Puerta principal", "Pasillo a Live Room"
- Techo/Piso: usar `wall: -2` (techo) o `wall: -1` (piso) para claraboyas, huecos, etc.
- **VALIDACIÓN**: verificar que material_a de cada abertura sea un nombre real de la DB de §2


---

## 31. Verificación de cumplimiento normativo

CADSFS V1.06 incluye un motor de verificación automática con **60 normas acústicas de 21 países**.

### 31.1 Cómo acceder

- **Menú Crear → Verificar cumplimiento normativo…** — diálogo completo con selector de norma y recinto
- **Menú Crear → Modo Arquitecto** — wizard paso a paso con auto-matching de norma por tipo+país

### 31.2 Normas disponibles por país

| País | Norma | Espacios |
|------|-------|----------|
| 🌐 Internacional | ISO 3382, ANSI S12.60, OMS, EBU, THX, ASHRAE | Todos |
| 🇦🇷 Argentina | IRAM 4044 | Aulas, viviendas, oficinas, hospitales |
| 🇪🇸 España | CTE DB-HR | Viviendas, aulas, hospitales |
| 🇬🇧 UK | Part E, BB93 | Residential, classrooms, music rooms |
| 🇧🇷 Brasil | NBR 15575, NBR 10152 | Habitações, aulas, hospitais |
| 🇩🇪 Alemania | DIN 4109 | Wohnungen, Schulen |
| 🇫🇷 Francia | NRA | Logements, enseignement |
| 🇮🇹 Italia | DPCM 5/12/1997 | Residenziale, scuole, ospedali |
| 🇺🇸 EE.UU. | IBC | Residential |
| 🇨🇦 Canadá | NBCC | Residential |
| 🇦🇺 Australia | NCC, AS 2107 | Residential, classrooms |
| 🇲🇽 México | NOM-081 | Vivienda |
| 🇨🇴 Colombia | NSR-10 | Vivienda |
| 🇨🇱 Chile | NCh 352 | Vivienda |
| 🇨🇳 China | GB 50118 | 住宅, 教室, 医院 |
| 🇯🇵 Japón | JIS/AIJ | 住宅, 学校, コンサートホール |
| 🇰🇷 Corea del Sur | KS F 2810 | 주거, 교실 |
| 🇮🇳 India | NBC 2016 | Residential, classrooms |
| 🇸🇬 Singapur | SS 553 | Residential |
| 🇹🇼 Taiwán | 建築技術規則 | 住宅 |
| 🇦🇪 EAU/Dubai | Dubai Municipality | Residential, classrooms |
| 🇵🇹 Portugal | RRAE | Habitação |

### 31.3 Parámetros verificados

- **RT60 máximo/mínimo** (estimado por Eyring con α promedio del proyecto)
- **STI mínimo** (estimación simplificada desde RT60 + ruido)
- **Ruido de fondo máximo** (dBA, ingresado por el usuario)
- **Rw / STC mínimo** (desde ensamblajes asignados, si existen)
- **C80 min/max** (estimado desde RT60)

### 31.4 Resultado

Cada parámetro muestra:
- Límite de la norma (con ≤ o ≥)
- Valor medido/calculado
- Delta: "margen: X.XX" si cumple, "excede en X.XX" o "falta X.XX" si no cumple
- Resultado global: ✅ CUMPLE / ❌ NO CUMPLE
- Exportable a PDF

### 31.5 Reglas para la IA

- Si el usuario pregunta "¿cumple la norma?", indicar que use Crear → Modo Arquitecto
- Si pregunta por un país específico, indicar qué norma aplica de la tabla
- Si pide mejorar el RT60, sugerir cambios de material (más absorción) o agregar tratamiento
- Si pide mejorar el aislamiento (Rw), recomendar un sistema constructivo de la biblioteca (§32)

---

## 32. Biblioteca de sistemas constructivos

29 sistemas constructivos pre-definidos, agrupados por categoría.

### 32.1 Cómo acceder

Menú Crear → Biblioteca de sistemas constructivos

### 32.2 Sistemas disponibles

| Categoría | Sistema | Rw aprox. |
|-----------|---------|-----------|
| **Tabique liviano** | Simple 70mm (1×12.5 + 45LM + 1×12.5) | 38 dB |
| | Simple 100mm (1×12.5 + 70LM + 1×12.5) | 42 dB |
| | Doble placa 120mm (2×12.5 + 70LM + 2×12.5) | 48 dB |
| | HD doble placa | 52 dB |
| | Doble montante (2×12.5 + 50LM + aire + 50LM + 2×12.5) | 56 dB |
| **Mampostería** | Ladrillo hueco 120mm + revoque | 35 dB |
| | Ladrillo hueco 180mm + revoque | 42 dB |
| | Hormigón armado 150mm | 48 dB |
| | Hormigón armado 200mm | 52 dB |
| | Hormigón armado 300mm | 57 dB |
| | Bloque de hormigón 150mm + revoque | 43 dB |
| **Muro compuesto** | Ladrillo 120 + LM 50 + placa yeso | 48 dB |
| | Hormigón 150 + LM 50 + placa yeso | 55 dB |
| | Doble pared (ladrillo + aire + LM + ladrillo) | 55 dB |
| **Losa / Piso** | Hormigón 150mm | 48 dB |
| | Hormigón 200mm | 52 dB |
| | Contrapiso flotante (150 + LM 30 + 50) | 55 dB |
| **Cielorraso** | Suspendido yeso 15mm | 20 dB |
| | Suspendido LM 50 + doble placa | 30 dB |
| **Vidrio** | Simple 6mm | 30 dB |
| | DVH 4+12+4 | 29 dB |
| | DVH 6+16+6 | 33 dB |
| | Laminado 6+6mm (PVB) | 37 dB |
| **Puerta** | Hueca estándar | 18 dB |
| | Maciza 45mm | 28 dB |
| | Acústica Rw 35 | 35 dB |
| | Acústica Rw 42 | 42 dB |
| **Estudio** | Pared triple (3×12.5 + 100LM + 3×12.5) | 60 dB |
| | Room-in-room (hormigón + aire + LM + doble yeso) | 65 dB |

### 32.3 Reglas para la IA

- Si el usuario pregunta "qué pared necesito para Rw 50 dB", recomendar:
  - Tabique doble placa (Rw≈48) → cercano pero puede no alcanzar
  - Tabique HD doble (Rw≈52) → cumple con margen
  - Hormigón 200mm (Rw≈52) → alternativa de masa
- Para estudios de grabación, recomendar Pared triple (Rw≈60) o Room-in-room (Rw≈65)
- Para separar viviendas (típicamente Rw ≥ 45-53 según país), recomendar doble placa o mampostería gruesa
- Indicar que se aplica desde Crear → Biblioteca de sistemas constructivos
- El DVH 4+12+4 tiene Rw≈29 (peor que vidrio simple 6mm = 30) por resonancia en la cámara — esto es normal

---

## 33. Modo Arquitecto

Wizard paso a paso diseñado para arquitectos que necesitan verificación acústica rápida.

### 33.1 Cómo acceder

Menú Crear → Modo Arquitecto

### 33.2 Los 5 pasos

1. **Tipo de proyecto + País**: seleccionar entre 13 tipos de recinto y 22 países. Auto-matching de la norma más apropiada.
2. **Geometría**: crear con preset de sala (6 formas) o importar DXF con layers. Selector de recinto para proyectos con múltiples salas.
3. **Asignar construcciones**: abrir la biblioteca de 29 sistemas constructivos y asignarlos a superficies.
4. **Verificar**: botón VERIFICAR CUMPLIMIENTO — muestra resultado ✅/❌ con detalle por parámetro.
5. **Exportar informe PDF**: genera informe profesional para presentar al comitente o municipio.

### 33.3 Funciona con cualquier proyecto

El Modo Arquitecto funciona con proyectos creados de cualquier forma:
- Dibujados con las herramientas CAD
- Importados desde DXF, SketchUp, OBJ, etc.
- Creados por la IA
- Abiertos desde un .csm existente

Solo requiere que los objetos estén marcados como `is_enclosure = true`.

### 33.4 Reglas para la IA

- Si el usuario es arquitecto o menciona "cumplimiento", "norma", "municipio", indicar el Modo Arquitecto
- Si pregunta "¿cómo verifico si mi sala cumple?", explicar los 5 pasos
- No intentar calcular cumplimiento normativo desde el AI — redirigir al Modo Arquitecto que tiene las 60 normas

---

## 34. Herramientas CAD (V1.06)

CADSFS incluye un editor CAD integrado en las vistas ortográficas (4 vistas).

### 34.1 Barra de herramientas (fila 2)

`⊞ ◇ | Grilla:÷ | 🖼✕ | 📏 | ✏ □ ↩ | 📐✕ | ✥ ✎ ⊕ ⟳ ▭ | 👁`

| Botón | Función |
|-------|---------|
| ⊞ | Snap a grilla (5cm a 5m) |
| ◇ | Snap a vértice más cercano |
| 🖼 | Blueprint (imagen de fondo) |
| 📏 | Regla acústica (distancia + λ→Hz) |
| ✏ | Dibujar polígono (3 planos) |
| □ | Rectángulo rápido (2 clicks) |
| ↩ | Undo último punto |
| 📐 | Cotas dimensionales persistentes |
| ✥ | Mover objeto (click-click) |
| ✎ | Editar vértice |
| ⊕ | Partir arista |
| ⟳ | Rotar objeto |
| ▭ | Acotado automático |
| 👁 | Toggle visibilidad blueprint |

### 34.2 Overlay de modos en tiempo real

Mientras se dibuja (≥2 puntos), se muestra automáticamente:
- BBox dimensions, modos axiales (f₁/f₂/f₃)
- V, RT60≈ (Eyring α̅=0.15), f_Schroeder, d_crítica
- Bolt: ✓/✗ dentro del área óptima
- Louden: CV del spacing (Excelente/Bueno/Aceptable/Pobre)
- Bonello: monotonía + degeneración de modos ≤250 Hz

### 34.3 Atajos de teclado

- **Esc**: cancelar herramienta activa
- **Ctrl+Z / Del / Backspace**: undo último punto
- **Enter**: cerrar polígono (≥3 puntos)
- **Ctrl+C / Ctrl+V**: copiar/pegar objetos
- **Ctrl+S**: guardar proyecto

### 34.4 Context menu (click derecho en Escena)

Duplicar, Espejo X/Y/Z, Array lineal, Offset de polígono, Alinear/Distribuir, Agrupar/Desagrupar, Asignar capa, Eliminar, Info del recinto (con Bolt/Louden/Bonello).


---

## 35. Plugins de exportación para software externo

CADSFS V1.06 incluye plugins de exportación a .CSM para los 3 softwares más usados por arquitectos.

### 35.1 SketchUp (Ruby)

- **Archivo:** `cadsfs_sketchup_exporter.rb`
- **Instalar:** Copiar a la carpeta Plugins de SketchUp
- **Uso:** Extensions → CADSFS → Exportar a CADSFS (.csm)
- **Detecta:** Caras horizontales → las extruye a la altura indicada
- **Preserva:** Layers, grupos, componentes
- **Codificación:** float32+int32 → zlib → base64 (compatible nativo)

### 35.2 AutoCAD (AutoLISP)

- **Archivo:** `cadsfs_autocad_exporter.lsp`
- **Instalar:** APPLOAD en AutoCAD, o agregar a acaddoc.lsp
- **Uso:** Comando `CADSFS` en la línea de comandos
- **Detecta:** LWPOLYLINE cerradas, agrupadas por layer
- **Parámetros:** Altura de extrusión + factor de escala (m/mm/cm)
- **Salida:** .CSM con vertices/faces en JSON plano (sin base64)

### 35.3 Rhino / Grasshopper (Python)

- **Archivo:** `cadsfs_rhino_exporter.py`
- **Instalar:** Copiar a la carpeta scripts de Rhino
- **Uso:** `_RunPythonScript` → seleccionar el archivo
- **Detecta:** Curvas cerradas planares + superficies horizontales (Brep)
- **Auto-escala:** Detecta unidades del modelo (mm/cm/m/in/ft) y convierte a metros
- **Compatible con Grasshopper:** Se puede llamar desde GhPython

### 35.4 Flujo de trabajo unificado

```
AutoCAD / SketchUp / Rhino  →  Plugin exporta .CSM  →  CADSFS abre directamente
                                                         ↓
                                                   Modo Arquitecto
                                                         ↓
                                              Verificar cumplimiento
                                                         ↓
                                               Informe PDF normativo
```

### 35.5 Reglas para la IA

- Si el usuario menciona AutoCAD/DWG: indicar el plugin AutoLISP (comando CADSFS)
- Si menciona Rhino/Grasshopper: indicar el plugin Python
- Si menciona SketchUp: indicar el plugin Ruby
- Todos exportan a .CSM que se abre directamente con Archivo → Abrir
- Los plugins NO requieren CADSFS instalado en la misma máquina

---

## 36. Arrays de haz controlado — `beam_arrays`

### 36.1 Cuándo usar uno

Es la decisión que más pesa en un diseño y la que menos se puede
corregir después. Antes de escribir nada, elegí el TIPO de sistema.

**Señales que piden un array de haz controlado:**

| señal | por qué |
|---|---|
| RT60 alto para el uso (>1,8 s con palabra) | un line array excita la reverberación y la inteligibilidad se cae |
| iglesia, catedral, nave, atrio, hall, museo | volumen grande, superficies duras, público en un plano |
| edificio patrimonial o vidriado | no se puede colgar nada a la vista |
| techo alto, público lejos en un solo plano | hace falta llevar la energía al público y no al techo |
| platea y anfiteatro desde un solo punto | varios haces con niveles distintos |
| el usuario nombra: columna orientable, beam steering, haz controlado, sonido dirigido, la Sphere, un domo | lo está pidiendo |

**Cuándo NO:**

- recinto con RT razonable y música amplificada → line array clásico
- estudio, sala de control, home cinema → monitores
- el usuario pide una marca concreta de line array

Un array de haz cuesta más y su banda útil tiene dos límites duros. No
es mejor en general: es mejor en su caso.

### 36.2 Cuál de las cinco formas

| forma | controla | para qué |
|---|---|---|
| `linea` | un eje | columna: inclina el haz arriba y abajo pero no lo lleva a un costado. Nave, pasillo, iglesia |
| `plano` | dos ejes | matriz: reparte zonas a izquierda y derecha, o platea y anfiteatro con niveles distintos |
| `arco` | un eje, con curvatura | frente curvo: la curvatura reparte sin gastar retardo y amplía el rango antes del lóbulo fantasma |
| `cilindro` | dos ejes | el arco repetido en altura, sobre pared curva que envuelve al público |
| `esfera` | dos ejes | casquete: sala esférica o domo, altavoces detrás de la superficie apuntando al centro |

### 36.3 Cómo se escribe

**Vos describís el array y la app genera los transductores con sus
retardos.** Nunca escribas los transductores uno por uno: son miles de
líneas y los retardos hay que calcularlos.

Columna orientable, el caso más común:

```json
"beam_arrays": [{
  "nombre": "Columna nave central",
  "forma": "linea",
  "n": 24,
  "paso_m": 0.105,
  "origen": [0, 0, 4.5],
  "eje": [0, 0, 1],
  "spl_1m_db": 90,
  "ventana": "hann",
  "haces": [{"azim_deg": 0, "elev_deg": -18, "nivel_db": 0}]
}]
```

Casquete esférico, sala esférica o domo:

```json
"beam_arrays": [{
  "nombre": "Casquete",
  "forma": "esfera",
  "centro": [0, 0, 24],
  "radio_m": 34,
  "n_anillos": 28,
  "n_por_anillo": 68,
  "elev_min_deg": -40,
  "elev_max_deg": 60,
  "mira_adentro": true,
  "spl_1m_db": 94,
  "modulo": {"nu": 8, "nv": 8, "paso_m": 0.10},
  "haces": [{"foco": [0, 0, 8]}]
}]
```

### 36.4 Las claves, por forma

**Todas:** `nombre`, `spl_1m_db`, `ventana`, `haces`, `progresivo`.

`ventana` reparte la energía entre transductores y decide el compromiso
entre lóbulos secundarios y ancho del haz:

| ventana | lóbulos | haz |
|---|---|---|
| `uniforme` | −13 dB | el más angosto |
| `hann` | −31 dB | 60 % más ancho |
| `blackman` | −58 dB | casi el doble |
| `rampa` | reparte energía hacia un extremo | compensa la distancia al fondo |

Por forma:

| forma | claves |
|---|---|
| `linea` | `n`, `paso_m`, `origen`, `eje` |
| `plano` | `nu`, `nv`, `paso_u_m`, `paso_v_m`, `origen`, `eje_u`, `eje_v` |
| `arco` | `n`, `radio_m`, `abertura_deg`, `origen`, `eje`, `normal` |
| `cilindro` | `nu`, `nv`, `radio_m`, `abertura_deg`, `paso_v_m`, `origen` |
| `esfera` | `n_anillos`, `n_por_anillo`, `radio_m`, `centro`, `elev_min_deg`, `elev_max_deg` |

### 36.5 Los haces

Cada entrada de `haces` es una dirección o un punto:

Por ángulo:

```json
{"azim_deg": 0, "elev_deg": -18, "nivel_db": 0}
```

Por foco:

```json
{"foco": [12, 0, 1.2], "nivel_db": -3, "retardo_ms": 4.5}
```

- `elev_deg` **negativo apunta hacia abajo**, que es lo normal con el
  array por encima del público.
- Con `foco`, el haz converge en ese punto. **Poné el foco donde está
  el público**, a la altura del oído: 1,2 m sentado, 1,6 m de pie.
- `retardo_ms` alinea ese haz con otra fuente. No cambia la forma del
  haz: un retardo igual para todos no cambia la interferencia.

Varios haces cubren varias zonas desde el mismo array. En una
superficie curva la app reparte los transductores entre ellos y apaga
los que miran para el otro lado; ésos quedan en la escena, silenciados.

`"mira_adentro": true` sólo en esfera y cilindro que **envuelven** al
público, con los altavoces detrás de la superficie. En un arco convexo
con el público delante va `false` o se omite.

### 36.6 Dos vías

Un array de una sola clase de transductor tiene un conflicto que no se
puede resolver: con paso grande controla en graves pero aliasa en
agudos, y con paso chico llega arriba pero no controla abajo.

```json
"capas": [
  {"nombre": "woofers",  "n": 16, "paso_m": 0.105,
   "f_low": 100,  "f_high": 1600},
  {"nombre": "tweeters", "n": 48, "paso_m": 0.035,
   "f_low": 1600, "f_high": 18000}
]
```

Con `capas` **no** pongas `n` ni `paso_m` en el nivel de arriba: cada
capa trae los suyos.

Sobre una forma curva las capas conservan su **densidad relativa**: si
la de agudos tiene el doble de transductores, sobre el casquete tendrá
el doble de puntos.

### 36.7 Módulos matriciales — obligatorio en instalaciones grandes

Una instalación grande no pone transductores sueltos sino **módulos**,
y cada módulo es a su vez una matriz que conforma su propio haz.

Una sala esférica de referencia tiene unos 1.600 módulos permanentes
más 300 móviles, con 96 transductores cada uno: **167.000 en total**.

No intentes modelar los 167.000. Poné los módulos y declarás lo que
cada uno lleva dentro:

```json
"modulo": {"nu": 8, "nv": 8, "paso_m": 0.10}
```

Con esa clave la app calcula la directividad real del módulo y la banda
que corresponde. **Sin ella el modelo cree que cada módulo es un punto
y declara una banda falsa:**

| | aliasing declarado |
|---|---|
| sin `modulo` | 154 Hz — falso, es el paso entre módulos |
| con `modulo` | 3.430 Hz — el de la matriz interna |

### Las dos frecuencias que limitan un array de haz

Cualquier array orientable —una columna DSP, un módulo matricial—
controla el haz sólo dentro de una banda, y las dos fronteras salen de
la geometría:

```
f_control  = c / (2·L)     L = longitud total del array
f_aliasing = c / (2·d)     d = paso entre transductores
```

**Por debajo de `f_control`** el array es demasiado corto respecto de
la longitud de onda: no dirige nada y se comporta como una fuente
puntual, por muy sofisticado que sea el procesado.

**Por encima de `f_aliasing`** aparece el lóbulo de rejilla: una copia
del haz apuntando donde nadie la quiere. En una sala eso significa
energía sobre una pared, o realimentación en un micrófono.

```
L = 2,0 m  →  controla desde 86 Hz
d = 0,16 m →  aliasing en 1.072 Hz
```

Ese array **no dirige por debajo de 86 Hz ni por encima de 1.072**, así
que sirve para inteligibilidad de palabra y no para música de rango
completo.

`cadsfs_array_haz` devuelve las dos cifras, y con `solo_calcular` las
informa **sin tocar el proyecto**: conviene mirarlas antes de proponer
una columna, no después de montarla.

Poné `modulo` siempre que los puntos queden separados más de medio
metro. Si están a centímetros son transductores sueltos y no hace
falta.

### 36.8 Reglas que evitan diseños que no funcionan

**La longitud manda en graves.** El array controla desde
`f ≈ 2·c/L`. Una columna de 1 m controla desde 686 Hz; para bajar a
300 Hz hacen falta 2,3 m. Esta fórmula está calibrada contra lo que los
fabricantes publican, no es el límite geométrico teórico.

**El paso manda en agudos.** Aliasa desde `f ≈ c/paso`. Con paso
105 mm eso es 3,3 kHz. Para llegar más arriba hay que juntarlos o usar
dos capas.

**No pongas el foco en el centro de una esfera.** Todos los
transductores quedan a la misma distancia, los retardos salen cero y
enfocar no hace nada. Es un caso degenerado, no un error del modelo.

**En una línea el acimut no tiene efecto.** Una columna no controla
fuera de su eje. Si hace falta llevar el haz a un costado, usá `plano`.

**Espaciado progresivo.** `"progresivo": 0.8` separa más los extremos
que el centro. Un array de paso uniforme tiene una periodicidad, y toda
periodicidad produce un lóbulo fantasma; sin periodicidad única el
fantasma se reparte en vez de concentrarse. Baja unos 5 dB, que es lo
que se consigue en la práctica.

**Más de 20.000 elementos se descarta.** Un casquete de 28 anillos ×
68 da unos 1.600 módulos, que es el tamaño de una sala esférica real.
Si el número sale mucho mayor, revisá los anillos y el paso.

---

## 37. Grupos de superficie — el recinto por partes

### 37.1 Qué objeto es el recinto

Un objeto se marca con `"is_enclosure": true`. Puede haber **varios**,
y la app elige el activo así:

> **el recinto marcado más pequeño que contenga a la fuente y al
> receptor.**

Eso importa más de lo que parece:

- Si la fuente y el receptor están en la nave, el activo es la nave
  aunque haya un recinto mayor que la contenga.
- Si están en salas distintas, el cálculo no encuentra un recinto que
  contenga a los dos y el resultado no es el que esperabas. **Ponelos
  siempre en el mismo recinto**, salvo que estés estudiando
  aislamiento entre locales.
- Los objetos con `"is_enclosure": false` absorben y difractan pero
  **no cierran volumen**: son mobiliario, paneles, escenario, butacas.

### 37.2 Cómo se arma un recinto de varias partes

Una nave con ábside, un teatro con caja escénica o una sala en L no se
modelan con un solo objeto. Se arman con varios, y cada uno lleva sus
propios grupos de superficie.

```json
"objects": [
  {"name": "Nave", "kind": "extrude", "is_enclosure": true,
   "polygon": [[-14,-9],[14,-9],[14,9],[-14,9]], "height": 12},
  {"name": "Ábside", "kind": "extrude", "is_enclosure": true,
   "polygon": [[14,-5],[22,-5],[22,5],[14,5]], "height": 9}
]
```

Reglas que evitan resultados sin sentido:

- **Los objetos tienen que tocarse en una cara**, no solaparse. Si se
  superponen, el volumen se cuenta dos veces y el RT60 sale largo.
- **La cara de contacto no lleva material absorbente**: no es una
  pared, es la abertura entre las dos partes. Si le ponés un material
  duro, el modelo la trata como pared y el ábside queda desconectado.
- El volumen del recinto activo sale del objeto que se elija, no de la
  suma. Con dos partes muy distintas el decaimiento tiene **dos
  pendientes**, y para eso está el modelo de recintos acoplados: la
  app avisa cuando lo detecta.

### 37.3 Los grupos y sus materiales

Cada cara pertenece a un grupo, y el grupo es lo que lleva el material.
Se nombran `"idObjeto|NombreCara"`:

```json
"surface_group_material": {
  "1|Pared 0": "Ladrillo visto",
  "1|Pared 1": "Ladrillo visto",
  "1|Techo":   "Lana mineral (roca) 50 mm (pared rígida)",
  "1|Piso":    "Loseta moqueta 6 mm (sobre hormigón)",
  "2|Pared 0": "Yeso liso pintado",
  "2|Techo":   "Ladrillo visto"
}
```

Y para el aislamiento, la cara exterior de cada superficie:

```json
"surface_group_material_b": {
  "1|Pared 0": "Hormigón liso"
},
"surface_assembly_map": {
  "1|Pared 0": "Ladrillo visto"
}
```

Reglas:

- **Nunca dejes un grupo en `Default`.** El cálculo sale mal y no
  avisa: si todas las bandas de RT60 dan el mismo valor, es por eso.
- El nombre del material tiene que estar exacto como figura en la
  biblioteca, en español.
- Un objeto de N caras genera N grupos. Un extrude de polígono de 6
  vértices da 6 paredes más techo y piso: ocho grupos que hay que
  asignar.
- Con `surface_assembly_map` la superficie usa el motor de aislamiento
  en vez de un coeficiente de absorción suelto: es lo que corresponde
  cuando interesa lo que pasa del otro lado.

### 37.4 Qué hace la app con los grupos

Conviene saberlo para no pelearse con el modelo:

- La **absorción media** se pondera por **área**, no por número de
  caras. Una pared de 80 m² pesa lo que ocho de 10 m².
- Los **planos del recinto** se extraen agrupando caras coplanares con
  una tolerancia angular, y se usan para las reflexiones tempranas y
  el mapa de cobertura. Un objeto con muchas caras casi coplanares
  se reduce a un plano.
- Las superficies del recinto se distinguen de los **obstáculos
  interiores**: sólo los segundos producen sombra acústica sobre el
  sonido directo.

---

## 38. Zonas de audiencia

El público se declara para que los mapas y los arrays sepan dónde está:

```json
"audience_plane_enabled": true,
"audience_center_pos": [0, 0, 0],
"audience_plane_z_m": 1.2,
"audience_size_x_m": 20,
"audience_size_y_m": 14,
"audience_occupancy_pct": 80
```

Y por zonas, cuando hay platea y anfiteatro:

```json
"audience_zones": [
  {"name": "Platea",     "x": 0, "y": 6,  "size_x": 18,
   "size_y": 12, "z": 1.2, "enabled": true},
  {"name": "Anfiteatro", "x": 0, "y": 22, "size_x": 16,
   "size_y": 8,  "z": 4.5, "enabled": true}
]
```

- `audience_plane_z_m` es la altura del **oído**, no del piso: 1,2 m
  sentado, 1,6 m de pie.
- La ocupación cambia la absorción. 0 % es la sala vacía y 80 % un
  concierto normal; con público la reverberación baja bastante, así que
  declararla importa.
- La absorción del público se define por octava (63 Hz a 8 kHz) y cada
  tercio toma la de su octava: 31 y 40 Hz la de 63, 12,5 kHz la de 8 kHz
  (desde R430; antes sólo los tercios centrales de octava).
- Un array de haz puede tomar la franja de distancias de estas zonas:
  si las declarás, el reparto de haces sale de ellas en vez de a ojo.

---

## 39. Aspecto en el render — `surface_render_look`

**Novedad de la v28.** Permite poner una imagen o un color en una
superficie, para el render 3D.

**No toca el cálculo.** La absorción la fija el material del paso
anterior. Una foto de ladrillo en una pared no cambia el RT60, y si
pudiera cambiarlo el modelo dejaría de ser defendible. Esta clave sólo
decide qué se ve.

### La estructura

```json
"surface_render_look": {
  "1|Pared fondo": {
    "color": "#8a7f6d",
    "imagen": "iVBORw0KGgoAAAANSUhEUg...",
    "modo": "mosaico",
    "ancho_m": 0.25,
    "alto_m": 0.06,
    "rot_deg": 0.0
  },
  "1|Pared fondo::B": {
    "color": "#4a4a4a",
    "modo": "mosaico"
  }
}
```

La clave es la del grupo de superficie, la misma de
`surface_group_material`. El sufijo `::B` es la cara opuesta: la que
NO mira al recinto.

### Los tres modos

| `modo` | qué hace | cuándo |
|---|---|---|
| `mosaico` | repite la imagen al tamaño real de `ancho_m` × `alto_m` | un material: ladrillo, madera, tela. Conserva la escala. |
| `estirar` | cubre la superficie entera, deforma si no coincide | un mural, una pantalla |
| `centrar` | cubre sin deformar; lo que sobra queda del `color` | una imagen que no debe distorsionarse |

**Con `mosaico`, `ancho_m` y `alto_m` son el tamaño REAL del motivo**,
no de la superficie. Un ladrillo de 25 × 6 cm va con
`"ancho_m": 0.25, "alto_m": 0.06`, y el programa calcula cuántas veces
se repite.

### La imagen

`imagen` es un PNG en base64, sin el prefijo `data:image/png;base64,`.

**Que no pase de mil píxeles de lado.** El proyecto se guarda en texto
y una foto de cámara incrustada pesaría más que todo el resto junto: a
la distancia a la que se mira un render, mil píxeles no se distinguen
de cuatro mil.

Sin `imagen`, la superficie se ve del `color` liso. Sin `color` ni
`imagen`, la clave se puede omitir.

---

## 40. Materiales en tercios de octava

**Novedad de la v28.** El importador de XLSX acepta las dos
resoluciones, y no hay nada que configurar: el archivo declara cuál usa
por el solo hecho de traer una u otra columna.

### Las dos resoluciones

**Octavas** — ocho bandas:

```
alpha_63  alpha_125  alpha_250  alpha_500
alpha_1000  alpha_2000  alpha_4000  alpha_8000
```

**Tercios de octava** — veintisiete bandas:

```
alpha_31  alpha_40  alpha_50  alpha_63  alpha_80
alpha_100  alpha_125  alpha_160  alpha_200  alpha_250
alpha_315  alpha_400  alpha_500  alpha_630  alpha_800
alpha_1000  alpha_1250  alpha_1600  alpha_2000  alpha_2500
alpha_3150  alpha_4000  alpha_5000  alpha_6300  alpha_8000
alpha_10000  alpha_12500
```

La primera se admite como `alpha_31` o `alpha_32`: los catálogos
difieren y el importador las trata igual.

Para dispersión: `s_NNN`, `scat_NNN` o `scattering_NNN`, con las mismas
bandas.

### Por qué convienen los tercios

El motor calcula en tercios. Un material declarado en octavas se
interpola a las bandas que faltan, y esa interpolación **borra justo lo
que un dato en tercios tiene de valioso.**

La muesca de un resonador cae en una o dos bandas de tercio. Un
resonador de Helmholtz de 250 Hz sube de 0,12 a 0,91 en cinco bandas;
en octavas esas cinco son un solo número y la muesca desaparece.

Con un panel perforado, la diferencia entre el dato real y el
interpolado puede llegar a 0,2 en α, justo en la banda donde el
material hace su trabajo.

Y hay un asunto de rango: las octavas van de 63 a 8000, y el programa
calcula de 31,5 a 12.500. Por fuera de ese rango el material se
extrapola repitiendo el valor del extremo, lo que en graves es
especialmente pobre.

### Lo que el importador NO hace

- **No sobrescribe.** Un material que ya existe en el proyecto se
  salta: para reemplazarlo hay que borrarlo primero.
- **No valida rangos.** Un α de 1,5 o de −0,2 entra sin protesta.
- Las columnas con frecuencias que no son de octava ni de tercio se
  ignoran, pero **se declaran en el registro** con su nombre.

---

## 41. La regla del splay — por qué nunca puede ser negativo

**Esto corrige un error de razonamiento que un agente puede cometer
aunque copie bien los ejemplos.**

### El error

Ante «apuntá el array al público», la respuesta intuitiva es calcular,
para cada caja, el ángulo que la lleva desde su posición hasta el punto
de escucha. **Eso está mal.**

Las cajas de un line array están unidas por un herraje que fija el
ángulo entre vecinas. Ese ángulo ---el splay--- es **siempre positivo o
nulo**: cada caja mira más abajo que la anterior, nunca más arriba.

Si se apunta cada caja al mismo punto, la de arriba ---más alta, más
lejos del suelo--- recibe más inclinación que la de abajo, y el array
se abre en abanico invertido con la parte baja hacia adelante. **Ese
montaje no existe.** Con doce cajas colgadas de 8,0 a 5,4 m apuntando a
un sweet spot a 20 m, los doce pares quedan con splay negativo.

### La regla

> **El pitch tiene que crecer monótonamente de arriba hacia abajo.**
>
> `pitch[i+1] >= pitch[i]` para todo par de cajas vecinas, ordenadas
> desde la superior.

### Cómo se apunta un array de verdad

**El azimut sí gira.** Rotar el array sobre su eje vertical es lo que
el herraje permite y lo que se hace en obra. Todas las cajas comparten
el mismo `yaw_deg`.

**La inclinación se aplica al conjunto.** Se decide el pitch de la caja
superior ---la que cuelga del punto de vuelo--- y ese mismo incremento
se suma a todas las demás. La curvatura no se toca.

```json
"elements": [
  {"pos": [-1.50, -3.5, 7.80], "yaw_deg": 0.0, "pitch_deg": 4.0},
  {"pos": [-1.50, -3.5, 7.49], "yaw_deg": 0.0, "pitch_deg": 4.0},
  {"pos": [-1.50, -3.5, 7.18], "yaw_deg": 0.0, "pitch_deg": 5.0},
  {"pos": [-1.49, -3.5, 6.87], "yaw_deg": 0.0, "pitch_deg": 7.0},
  {"pos": [-1.47, -3.5, 6.56], "yaw_deg": 0.0, "pitch_deg": 10.0},
  {"pos": [-1.43, -3.5, 6.26], "yaw_deg": 0.0, "pitch_deg": 14.0}
]
```

Mismo `yaw_deg` en todas, `pitch_deg` creciente hacia abajo, y las dos
o tres de arriba con el mismo valor ---la parte plana del array, que
cubre el fondo.

Para inclinar el conjunto 5° más, se suman 5 a los seis valores. **No
se recalcula caja por caja.**

### Qué hace la interfaz

El botón «Alinear al Sweet Spot» distingue los dos casos por la
geometría:

- **Cajas alineadas en vertical y próximas** → las trata como array:
  gira el azimut de todas y traslada la inclinación conservando la
  curvatura.
- **Cajas sueltas** ---front fills, delays, torres--- → apunta cada una
  por separado, que es lo correcto porque no comparten herraje.

Si la curvatura que se declaró tuviera algún par con splay negativo,
avisa: es un montaje que el herraje no admite.

---

## 42. La API de agente — lo que se agregó

El programa expone 52 rutas REST y un servidor MCP con 39 herramientas.
Estas son las que se sumaron después de la v27.

### Verificación normativa

| ruta | qué hace |
|---|---|
| `GET /api/norms` | las 86 normas de 37 países, filtrables por `pais` y `tipo` |
| `POST /api/norms/check` | verifica el proyecto contra una norma, parámetro por parámetro |

**Los parámetros que no se pudieron evaluar vuelven como PENDIENTES**,
no como cumplidos, y el veredicto general queda sin definir mientras
quede alguno. El caso típico es el ruido de fondo: no se predice, se
mide. Hay que pasarlo en `ruido_fondo_dba` para obtener un veredicto
completo.

### Posiciones

| ruta | qué hace |
|---|---|
| `GET /api/positions` | dónde están fuente, receptor y cada altavoz |
| `POST /api/positions` | mueve la fuente, el receptor o un sistema entero |

Para un sistema se pasa el índice y el vector de desplazamiento, lo que
**conserva la geometría relativa del array**. Mover caja por caja la
rompería.

### Lote

`POST /api/batch` procesa varios `.csm` **sin tocar el proyecto
abierto**: calcula el RT60 de cada uno y, si se indica una norma, lo
verifica. Un archivo que falla no aborta el lote.

Es la ruta para «verificá estas doce aulas y decime cuáles no cumplen».
Abrirlas de a una pisaría el proyecto del usuario.

### Deshacer

| ruta | qué hace |
|---|---|
| `POST /api/undo` | deshace las últimas operaciones |
| `POST /api/redo` | rehace |
| `GET /api/undo/stack` | qué hay en la pila, sin deshacer nada |

**Importante para un agente:** el proyecto sobre el que se trabaja es
el que el usuario tiene abierto, con su trabajo. Si una operación sale
mal, hay que deshacerla en vez de corregir encima.

### Vigencia de los resultados

| ruta | qué hace |
|---|---|
| `GET /api/results/status` | qué está calculado y si sigue correspondiendo |
| `GET /api/project/resumen` | el proyecto sin mallas ni imágenes |

Cuando algo cambia ---se mueve una fuente, se cambia un material, se
activa el modo exterior--- los resultados calculados antes dejan de
corresponder, y `/api/results` los devuelve marcados:

```json
"_vigencia": {
  "vigente": false,
  "aviso": "el proyecto cambió desde el último cálculo: estos
            resultados NO corresponden a la configuración actual"
}
```

La marca distingue lo que importa: cambiar la imagen de una pared no
invalida nada, porque no cambia la acústica. Mover un altavoz sí.

**Usar `/api/project/resumen` para razonar**, no `/api/project/full`:
el archivo entero de una sala grande puede no entrar en el contexto del
modelo.

### Diseño: lo que corrige `/api/validate` y `/api/design` (R437, R438)

Con el formato cookbook, además de los materiales:

- **La geometría** (desde la R438 con cualquier planta y con objetos
  girados en Z; en la R437, sólo en un rectángulo alineado con los ejes):
  con `autofix` (lo normal) lo que atraviesa paredes, los paneles de canto
  o separados de una pared oblicua, los muebles de pared, las trampas, los
  parlantes, la fuente y el receptor se acomodan y vuelven en
  `corrections`, con `method: "geometria"`, `was` y `now` (medidas,
  centro y giro) y el `message`. Detalle en §0.5.
- **Las caras** (`method: "caras"`): el material que un objeto tiene sólo
  en caras que no se ven pasa a las que miran a la sala; `now` trae las
  claves `"N|Pared -X"`… que se agregaron.
- **Un estudio** (`method: "estudio"`): el triángulo, el apuntado, la mesa,
  los paneles de primera reflexión y la nube (§52.4).
- Con `strict: true` o `autofix: false` no se toca nada: todo vuelve en
  `warnings` con una `suggestion`. Lo que es una decisión de diseño vuelve
  siempre como aviso. Un objeto entero afuera, también.
- `method: "medidas"` sólo lo produce el asistente interno, que sabe qué
  medidas pidió el usuario (§51).
- **Las capas de superficie** (`surface_group_material` y las otras
  cuatro) se llevan a los grupos que arma el convertidor, con las
  claves como las describe §4. Hasta la R436 se perdían.
- **`source_pos`, `receiver_pos`** y lo demás que documenta esta
  cookbook (`beam_arrays`, `audience_zones`, `measured_rt60_s`, `c_m_s`,
  `source_spl_db`, `source_polar_pattern`, `receiver_radius_m`,
  `outdoor_mode`, `ground_conditions`, `audience_*`) llegan al proyecto.
  Los números, sólo si son números positivos.

### Otras

| ruta | qué hace |
|---|---|
| `GET /api/engine/suggest` | qué motor conviene y por qué |
| `POST /api/beam-array` | arma un array de haz y devuelve su banda útil |
| `POST /api/outdoor` | activa el modo aire libre |
| `POST /api/render/look` | imagen o color en una superficie |
| `POST /api/auralize` | la respuesta al impulso |
| `POST /api/export` | csm, dxf, obj, json, pdf, csv |
| `GET /api/log` | el registro de diagnóstico, filtrable |
| `GET /api/progress` | en qué paso va un cálculo largo |

### El servidor MCP

`POST /mcp` implementa JSON-RPC 2.0 con `initialize`, `tools/list` y
`tools/call`. Las 31 herramientas llaman a las mismas rutas: no hay dos
caminos que puedan dar resultados distintos.

Se enciende desde **Inteligencia artificial → Agentes externos**, en el
puerto 8781 por defecto.

---

## 43. Objetos silenciados y el análisis modal

**Corrección de la v28.** Un objeto con `"muted": true` no define la
sala.

Silenciar un objeto es la manera de probar el recinto sin él: sin esa
columna, sin esa platea, sin ese palco. El análisis modal restaba el
volumen de los objetos silenciados igual, así que **las frecuencias de
los modos salían de una geometría distinta de la que usaban el RT60, la
cobertura y las reflexiones.**

Ahora los cinco caminos modales los excluyen:

```
_fd_solve                    el solver de diferencias finitas
_compute_fdtd_impulse…       el FDTD
_RoomModesDlgV2              el diálogo de modos propios
_get_room_dims               la corrección modal del informe
_modal_correction_at_pos     la corrección por posición
```

**La malla global sigue conteniéndolos a propósito**: el visor los
dibuja en gris para que se vea qué se apagó. Lo que cambia es que el
cálculo ya no los mide.

---

## 44. Aislamiento por API — el flujo completo

Hasta la v28 el agente podía escribir `wall_assemblies` en el `.csm`
pero **no podía saber qué materiales existen**. Ahora sí.

### La distinción que hay que tener clara

```
absorción    cómo suena la sala POR DENTRO
             manda la porosidad
             GET /api/materials  →  ~2.679 materiales, con α por banda

aislamiento  cuánto ruido pasa AL OTRO LADO
             manda la masa y la rigidez
             GET /api/insulation/materials  →  163, con ρ, E, ν, η, σ
```

**Son listas distintas y no se pueden mezclar.** Un panel de lana
mineral absorbe muy bien y no aísla nada; su ficha de absorción no dice
nada del aislamiento.

### Las cinco rutas

| ruta | qué hace |
|---|---|
| `GET /api/insulation/materials` | los 163, con sus propiedades elásticas |
| `GET /api/insulation/assemblies` | los ensamblajes del proyecto y qué superficie lleva cada uno |
| `POST /api/insulation/assembly` | crea uno por capas |
| `POST /api/insulation/assign` | lo asigna a un grupo de superficie |
| `GET /api/insulation/results` | R, R', Rw, Ln,w y las contribuciones |

### Qué devuelve la lista de materiales

```json
{
  "materiales": [
    {"id": "gyp_125", "name": "…", "category": "panel",
     "acoustic_model": "plate",
     "rho_kg_m3": 750.0, "young_pa": 2.1e9,
     "poisson": 0.24, "loss_factor": 0.012,
     "flow_resistivity_pa_s_m2": null}
  ],
  "total": 163,
  "categorias": ["air", "masonry", "membrane", "panel",
                 "porous", "porous_absorber"]
}
```

**Filtrable:** `?categoria=panel` y `?buscar=yeso`.

### Qué significa cada propiedad

| campo | qué decide |
|---|---|
| `rho_kg_m3` | la masa, y con ella la ley de masa: duplicarla da 6 dB |
| `young_pa` | **dónde cae la coincidencia**, la frecuencia a la que el aislamiento se hunde |
| `poisson` | entra en la rigidez a flexión, junto con Young |
| `loss_factor` | **cuán profunda es la caída** de coincidencia |
| `flow_resistivity_pa_s_m2` | sólo porosos: alimenta Delany-Bazley |

**El factor de pérdidas es el que menos se conoce y más importa.** Un
vidrio simple tiene η = 0,002 y su caída es profunda y estrecha; uno
laminado tiene diez veces más y la caída se rellena. Ésa es toda la
diferencia entre los dos, con el mismo espesor.

### Crear un ensamblaje

```json
POST /api/insulation/assembly
{
  "id": "asm_medianera",
  "nombre": "Medianera doble hoja",
  "conexion": "elastica",
  "capas": [
    {"material": "gyp_125",         "espesor_mm": 12.5},
    {"material": "air_90",          "espesor_mm": 90},
    {"material": "mineral_wool_80", "espesor_mm": 80},
    {"material": "gyp_125",         "espesor_mm": 12.5}
  ]
}
```

**Las capas van del lado A al lado B, en el orden físico.** Un
ensamblaje asimétrico no da lo mismo del derecho que del revés en las
frecuencias donde la coincidencia de cada hoja difiere.

### La conexión: lo que más cambia el resultado

```
rigida     las dos hojas atornilladas al mismo montante
elastica   montantes desfasados, o banda elástica
perfil     un perfil concreto de la biblioteca
manual     un factor de acoplamiento declarado
```

En construcción ligera esto pesa más que los materiales:

```
mismo tabique, dos montajes:
  montante compartido     Rw = 42 dB
  montantes desfasados    Rw = 54 dB
```

**Doce decibelios sin cambiar un solo material.** Es la decisión más
barata y más rentable de un proyecto de aislamiento, y la que más se
pasa por alto.

### Los dos errores que la ruta rechaza

**Material inexistente** — devuelve los parecidos, no sustituye en
silencio:

```json
{"ok": false,
 "error": "material de aislamiento desconocido: yeso15",
 "capa": 0,
 "parecidos": ["gyp_125", "gyp_150", "gyp_double_125"],
 "hint": "Pedí la lista completa con GET /api/insulation/materials"}
```

**Capa sin espesor** — el TMM lo necesita:

```json
{"ok": false,
 "error": "la capa 1 no tiene espesor. El TMM lo necesita: sin
           espesor no hay matriz de transferencia"}
```

### Las cámaras de aire se sintetizan

`air_NN` funciona para cualquier `NN`: `air_50`, `air_90`, `air_200`.
El programa las genera con las propiedades del aire y el espesor que se
declare. **No hace falta que estén en la lista.**

### Leer los resultados

```
GET /api/insulation/results
```

Devuelve **R y R' por separado**, que es la distinción que decide un
proyecto:

```
R      el elemento solo, lo que mide un laboratorio
R'     el aislamiento aparente, con el flanqueo incluido
```

Entre los dos puede haber **catorce decibelios** que no están en ningún
catálogo. Las normas suelen exigir el aparente.

### El flujo completo

```
1  GET  /api/surfaces                 qué superficies hay
2  GET  /api/insulation/materials     qué materiales, con sus propiedades
3  POST /api/insulation/assembly      armar el sistema constructivo
4  POST /api/insulation/assign        asignarlo a las superficies que separan
5  POST /api/compute steps=['aislamiento']
6  GET  /api/insulation/results       R, R', y qué vía domina
```

**El paso 6 dice dónde trabajar.** Las contribuciones vienen ordenadas
por cuánto aportan, con tres decimales: mejorar la puerta que aporta el
0,098 % no cambia nada; mejorar la pared que aporta el 55 % sí.

---

## 45. Altavoces por API — elegir en vez de inventar

Hasta la v28, un agente sólo podía poner `point_90` —una fuente
genérica— o inventar un `model_id`, con el mismo riesgo de fallo
silencioso que el recetario declara para los materiales.

### La ruta

```
GET /api/speakers
GET /api/speakers?tipo=line&marca=meyer
GET /api/speakers?buscar=k2&max=10
```

### Qué devuelve cada modelo

```json
{
  "id": "adamson_cs10",
  "name": "Adamson CS10",
  "type": "line",
  "default_polar": "LineArray",
  "coverage_deg": 110.0,
  "splay_default_deg": 5.0,
  "default_spl_db": 106.3,
  "max_spl_db": 141.3,
  "dimensions_m": [0.737, 0.526, 0.265],
  "weight_kg": 27.0,
  "rigging": "SlideLock Rigging System"
}
```

| campo | para qué |
|---|---|
| `id` | **el `model_id` que va en el `.csm`** |
| `type` | `line` \| `point` \| `sub` \| `monitor` |
| `coverage_deg` | la cobertura nominal |
| `splay_default_deg` | el splay de fábrica entre cajas del array |
| `default_spl_db` | sensibilidad a 1 m |
| `max_spl_db` | **el SPL de PICO** |
| `dimensions_m`, `weight_kg` | para el rigging |

### El aviso que la ruta devuelve

> `max_spl_db` es de PICO. El nivel continuo es de doce a veinte
> decibelios menor según el factor de cresta del material.

```
música comprimida     12 dB
música pop / rock     14 a 16 dB
música sinfónica      hasta 20 dB
palabra               12 a 15 dB
```

**Un altavoz de 141 dB de pico sostiene 121 con música sinfónica.** Es
la causa más común de un refuerzo que «no alcanza» estando bien
calculado sobre el papel.

### Las marcas

```
GET /api/speakers  →  "marcas": [...]  y  "tipos": [...]
```

Vienen en la respuesta, así que no hace falta conocerlas de antemano.

---

## 46. El asistente de array por API

Antes había que generar cada caja a mano, con su posición y sus tres
ángulos, y sin saber el peso ni las dimensiones para el rigging.

### La ruta

```json
POST /api/systems/array
{
  "modelo": "adamson_cs10",
  "n": 12,
  "altura_m": 9.0,
  "angulo_primera_deg": 0.0,
  "splay": "progresivo",
  "pos_xy": [0.0, -14.0],
  "nombre": "Main PA Left"
}
```

### Qué devuelve

```json
{
  "sistema": "Main PA Left",
  "cajas": 12,
  "modelo": "Adamson CS10",
  "peso_total_kg": 324.0,
  "pitch_deg": [0.0, -4.0, -8.4, ...],
  "splay_deg": [4.0, 4.4, 4.7, ...],
  "splay_negativo": []
}
```

**`peso_total_kg` es lo que hay que colgar del punto de vuelo.** Con
esa cifra se decide si el rigging aguanta antes de montar nada.

### Los dos repartos

**`progresivo`** — el splay crece hacia abajo. Es lo que cubre una
platea con distancia variable: las cajas de arriba apuntan lejos con
poco ángulo entre ellas, y las de abajo cubren las primeras filas
abriéndose más.

**`uniforme`** — todas llevan el mismo. Sirve para una audiencia a
distancia pareja.

### `splay_deg` y `splay_negativo`

La respuesta trae los splay resultantes **y la lista de los que
quedaron negativos**. Si esa lista no está vacía, el array es
imposible: el herraje no admite que una caja mire más arriba que la
anterior.

---

## 47. Apuntar un sistema — y por qué no caja por caja

```json
POST /api/systems/aim
{
  "sistema": "Main PA Left",
  "objetivo": [0.0, 12.0, 1.2]
}
```

### Lo que hace, según qué sea el sistema

La ruta **detecta si es un array** —cajas alineadas en vertical, con la
misma planta— y actúa distinto:

```
array          gira el AZIMUT del conjunto
               TRASLADA la inclinación, conservando la curvatura

cajas sueltas  cada una se apunta por separado
```

### Por qué la distinción importa

Apuntar cada caja de un array al mismo punto **produce splay negativo
en todos los pares**: las de abajo tendrían que mirar más arriba que
las de encima para alcanzar el mismo objetivo. Eso es un montaje que el
herraje no admite.

Un rigging real hace lo otro: gira el conjunto y conserva la curvatura
que el diseño le dio.

### Qué devuelve

```json
{
  "sistema": "Main PA Left",
  "modo": "array: azimut al conjunto, curvatura conservada",
  "yaw_deg": 0.0,
  "pitch_deg": [-2.1, -6.1, -10.5, ...],
  "splay_deg": [4.0, 4.4, ...]
}
```

Y si algo quedó mal:

```json
"aviso": "Hay 3 par(es) con splay NEGATIVO: el herraje no lo
          admite. Revisá la curvatura."
```

---

## 48. Las herramientas MCP nuevas

El servidor MCP expone **39 herramientas**. Estas ocho son las que se
sumaron:

| herramienta | qué hace |
|---|---|
| `cadsfs_aislantes` | los 163 materiales de aislamiento |
| `cadsfs_ensamblajes` | los del proyecto, y las superficies sin asignar |
| `cadsfs_ensamblaje` | crear uno por capas |
| `cadsfs_asignar_ensamblaje` | asignarlo a una superficie |
| `cadsfs_aislamiento_resultados` | R, R', Rw, Ln,w |
| `cadsfs_altavoces` | los 447, con SPL y rigging |
| `cadsfs_array_colgado` | el asistente de array |
| `cadsfs_apuntar` | apuntado que respeta el herraje |

**Se descubren solas con `tools/list`**, con su esquema de entrada y su
descripción. Un agente MCP no necesita este documento para usarlas —
pero sí para entender por qué el splay no puede ser negativo.

---

## 49. Beamforming: sólo licencia Full

El diseño de arrays de haz controlado —shading, steering y factor de
array— **es exclusivo de las licencias Full y Enterprise**.

```
función                      Est   Arq   Full  Ent
speaker_systems              ✓     —     ✓     ✓
beamforming                  —     —     ✓     ✓
speaker_systems_immersive    —     —     ✓     ✓
```

**Al beamforming se llega por cinco caminos** —el botón de Sistemas,
dos de Análisis Avanzado, el paso 9 de «calcular todo» y el paso del
agente— y los cinco pasan por el mismo guardia. **La API y el MCP
también**, porque el control está en la función y no en el botón.

Si la licencia no lo incluye:

```
desde la interfaz     el botón queda deshabilitado, con el motivo
desde «calcular todo» el paso se saltea, sin abrir ningún diálogo
desde la API          la llamada no hace nada
```

`/api/beam-array` —el array de haz controlado— sigue disponible para
consultar la banda útil con `solo_calcular`, porque eso es información
y no diseño.

---

## 50. El flujo completo de un agente

Con lo agregado en esta versión, un agente puede hacer el proyecto
entero. Éste es el orden que corresponde:

### 1 · Entender el encargo

```
GET /api/cookbook       las reglas y la lista de materiales
GET /api/schema/csm     el esquema formal
GET /api/norms?pais=AR  qué exige la norma que aplica
```

### 2 · Dibujar

```
POST /api/validate      antes de construir
POST /api/design        construir, y leer qué corrigió
```

**Leer `corrections` no es opcional.** Si el agente inventó un
material, ahí dice cuál puso en su lugar.

### 3 · Tratar la sala

```
GET  /api/surfaces
GET  /api/materials
POST /api/surfaces/material
POST /api/compute steps=['rt60']
```

Iterando hasta el objetivo. **En 500 y 1000 Hz está casi la mitad del
peso del STI**, así que un tratamiento que sólo funciona en agudos
apenas mueve la inteligibilidad.

### 4 · Aislar

```
GET  /api/insulation/materials
POST /api/insulation/assembly
POST /api/insulation/assign
POST /api/compute steps=['aislamiento']
GET  /api/insulation/results
```

### 5 · Diseñar el sistema

```
GET  /api/speakers?tipo=line
POST /api/systems/array
POST /api/systems/aim
POST /api/compute steps=['cobertura','sti']
```

### 6 · Verificar y entregar

```
GET  /api/engine/suggest        ¿el motor elegido conviene?
POST /api/norms/check           ¿cumple?
GET  /api/results/status        ¿los resultados siguen vigentes?
POST /api/report.pdf            el informe
```

### La regla que atraviesa todo

**Antes de informar un resultado, comprobar que sigue vigente.**

```
GET /api/results/status
```

Un cálculo deja de corresponder al proyecto en cuanto se cambia algo
acústicamente relevante. Informar un RT60 calculado antes de reasignar
los materiales es el error más caro de esta cadena, porque el número
sigue siendo plausible.

---

## 51. El asistente interno: sala nueva y modificaciones (R437)

El JSON completo es para **crear** una sala. Para modificar lo que ya
existe ---mover, cambiar un material, agregar un panel, sacar un
objeto--- van los **comandos** (el bloque `commands` del prompt:
`set_material`, `move_object`, `add_panel`, `remove_object`,
`modify_enclosure`…). Así lo dicen la regla 6 y los COMANDOS LOCALES
del prompt; hasta la R436, una línea de las INSTRUCCIONES decía lo
contrario («para CUALQUIER modificación, el proyecto completo»).

Si igual llega un JSON completo con un proyecto abierto, el programa
lo trata así:

| el JSON trae… | qué pasa |
|---|---|
| **otra sala** (el recinto cambia más de 5 cm en alguna medida, o de cantidad de paredes) | **reemplaza** al proyecto: no se le suman los objetos, los parlantes, las posiciones ni los materiales del anterior. Sí se conservan, si el JSON no los trae, el nombre, el diseñador, el cliente, el lugar, el constructor y la fecha del proyecto |
| la **misma sala**, con al menos tantos objetos como el proyecto | se usa el JSON; los objetos del proyecto que el JSON no trae se **conservan** (con un id nuevo si el suyo ya lo usa otro) |
| la **misma sala**, con menos objetos (y el proyecto tiene más de dos) | se conserva el proyecto y se le **agregan** los objetos nuevos del JSON |
| la **misma sala**, con menos objetos y un proyecto de uno o dos | se usa el JSON tal cual |

En los dos casos de la misma sala:

- **Un objeto renombrado se reconoce por su lugar** (la misma caja
  envolvente, ±5 cm): no se duplica ni se agrega de nuevo.
- **Los materiales, la cara B, los assemblies, el espesor y el aspecto
  que el JSON manda para un objeto ganan**, también para un objeto que se
  conservó. Hasta la R436 ganaban los del proyecto anterior, porque sus
  claves estaban escritas de otra forma.
- Los parlantes que el JSON no trae se conservan; si los trae, los
  reemplaza.
- Los datos del proyecto que el JSON no trae (o trae vacíos) se
  conservan.

Para que el resultado sea exactamente el que describe el JSON, lo mejor
es mandarlo completo: todos los objetos, con sus nombres de siempre.

### Las medidas del pedido (R438)

Si el pedido trae las medidas del recinto («hazme un control room de
3x4x3», «una sala de 10 × 6 × 4,5 m», «de 5 por 4 por 3», «de 8x6 con 3 m
de alto»), el asistente interno le agrega al mensaje, al final y sin
mostrarlo en el chat, una nota: `[CADSFS · medidas del pedido: planta de
3 × 4 m y 3 m de alto. …]`. Con dos medidas, sólo si el texto habla de un
recinto y no de un objeto («un panel de 1,2x0,6» no cuenta).

Cuando llega el JSON que contesta ese pedido, si su recinto no mide eso
(±2 %, o ±5 cm), el programa lo lleva a esas medidas antes de validar. La
planta: si tiene quiebres o paredes inclinadas que el pedido no nombra,
queda el rectángulo exacto (también con las medidas bien); si el pedido
habla de otra forma («con paredes inclinadas», «en L»), se escala esa
forma. La medida mayor, donde la IA puso la suya. Lo de adentro, sin
cambiarle el tamaño: lo que estaba contra una pared queda a la misma
distancia de esa pared; lo que la atravesaba la sigue atravesando igual,
para que el corrector lo gire y lo apoye; lo demás, en proporción; lo que
ocupaba casi todo un lado, se escala con la sala. Las aberturas: la que
está a 1 m o menos de una esquina, a la misma distancia de esa esquina;
las demás, en proporción a su pared (en el rectángulo, en la pared de su
lado). Después
el corrector termina de acomodar. Va al chat con `method: "medidas"`.

### V4: el recinto centrado en Y (R438)

Si el polígono no está centrado en Y = 0, el programa lo centra (V4).
Hasta la R437 corría sólo el polígono y lo de adentro quedaba corrido
respecto de sus paredes; desde la R438 corre todo el diseño: objetos,
parlantes, fuente, receptor, zonas de audiencia y centros de arrays.

---

## 52. Control room: la receta y lo que hace el programa (R438)

El caso que motivó esta sección (26/09/2026): «hazme un control room de
3x4x3». La IA devolvió una sala de 5 × 4,2 × 3 con paredes inclinadas
(copió el ejemplo de control room de 6 × 4,2 y la regla del volumen
mínimo), el receptor de ejemplo `[1,0 0 1,2]` (al 70 % de su sala, con un
triángulo estéreo de 31°), la mesa de punta con el oyente encima, el
difusor de canto con 0,86 m afuera del fondo, el sofá atravesando el
fondo, las trampas metidas en las paredes y los paneles laterales a 4-8
cm de la pared inclinada. El «Difusor (1D)» estaba en la cara que da
contra la pared. Y la pared de la ventana, entera de vidrio.

### 52.1 Las medidas del usuario

Si el usuario da las medidas del recinto, **el recinto mide eso**:

- las dos medidas de planta, en el orden que convenga al uso (en un
  control room, la **mayor en X**, el eje de escucha, salvo que el usuario
  diga cuál es el ancho);
- la altura;
- **rectangular, de 4 vértices**, salvo que el usuario pida otra forma.

Ninguna recomendación de esta guía (el volumen mínimo de A8, las
proporciones de Bolt, las paredes inclinadas de §3, los ejemplos) autoriza
a cambiarlas. Si no se cumple alguna, **se dice en el texto**: «Con 3 × 4 ×
3 m el volumen es de 36 m³, por debajo de los 40 recomendados: los modos
van a estar más separados; lo compensan las trampas de graves».

### 52.2 La receta

Con **D** la profundidad (X), **W** el ancho (Y) y **H** el alto, el frente
en −X y el recinto centrado en (0, 0):

| qué | dónde |
|---|---|
| **oyente** (`receiver_pos`) | `x_r = −D/2 + 0,38·D`, `y = 0`, `z = 1,2` |
| **monitores L y R** | triángulo equilátero: separación `s` de 1,2 a 1,8 m (y no más de `W − 1`); `x_m = x_r − 0,866·s`, `y = ∓s/2` (L en −Y), `z` 1,2 a 1,3; a 0,6 m o más del frente (SBIR; en una sala chica, 0,3 m como mínimo: si no entran, achicá `s`) |
| su apuntado | `yaw = atan2(y_r − y_m, x_r − x_m)` (≈ +30° el L, −30° el R); `pitch = atan2(z_m − z_r, distancia horizontal)`, positivo hacia abajo |
| **fuente** (`source_pos`) | en el monitor izquierdo, en la misma posición que el elemento L: el RT60 y las reflexiones se calculan desde ahí. CADSFS pide al menos 1,5 m entre la fuente y el receptor; si no, los separa por su cuenta. Con `s` menor que 1,5 m, la fuente va en el eje (`y = 0`), sobre el frente, a más de 1,5 m del oyente |
| **mesa de mezcla** | `dimensions = [profundidad, ancho, alto]`, p. ej. `[0.9, 1.8, 0.77]`: el ancho en Y, de frente al oyente; su borde de este lado 0,40 m delante del oyente: `x = x_r − 0,40 − profundidad/2`, `y = 0` |
| **paneles de primera reflexión** | uno por lateral: la reflexión del monitor m en la pared izquierda (`y = −W/2`) cae en `x = x_m + (x_r − x_m)·(W/2 + y_m)/(W + y_m + y_r)`; en la derecha, con las `y` cambiadas de signo. Un panel de 1,2 a 1,8 m centrado entre los puntos de L y de R, a `z ≈ 1,2`, contra la pared, sin tapar la ventana |
| **nube** | centrada en `x = x_m + (x_r − x_m)·(H − z_m)/(2H − z_m − z_r)`, `y = 0`; 1,5 × 1,2 m o más, a 5-10 cm del techo |
| **trampas de graves** | en las esquinas, **tocando las dos paredes**: `[D/2 − a/2, W/2 − a/2, h/2]` y los signos |
| **difusor** | contra el fondo, `dimensions = [espesor, ancho, alto]`, centrado en `y = 0`, a la altura del oído |
| **sofá** u otro mueble de pared | de espaldas a su pared, **delante** de los paneles o el difusor de esa pared |
| **sub** | en el piso, a 1/3 del frente desde una esquina (A14); no adentro de una mesa maciza: si va debajo, la mesa se modela como una tapa de 5 cm a 0,72-0,77 m |
| **ventana CR-LR** | una abertura (§28), en el frente, por encima de la mesa; si cae sobre un punto de primera reflexión, inclinada 5-10° |
| **puerta** | en la pared del fondo o en una lateral, detrás del oyente; nunca detrás de la mesa (queda a 0,1-0,3 m del frente) ni donde va una trampa de graves |
| **simetría** | las dos laterales con el mismo material (A7) |

**El material de un objeto.** Lo más simple: en todo el objeto, con
`"material"` (panel, trampa, nube, difusor o mueble), como en §52.5. La cara que
da contra la pared no la ve ningún rayo. Si una cara tiene que llevar otro
material, va en `surface_group_material` con la clave de esa cara, y la que
cuenta es la que **mira a la sala**:
- en la pared izquierda (−Y), `"Pared +Y"`;
- en la derecha, `"Pared -Y"`;
- en el fondo, `"Pared -X"`;
- en el frente, `"Pared +X"`;
- en una nube, `"Piso"`.

Nunca pongas el material sólo en la cara que da contra la pared: el programa
lo corre a la que se ve (§52.4).

### 52.3 Un ejemplo resuelto: 3 × 4 × 3

Planta de 3 × 4 m: la mayor en X. `D = 4`, `W = 3`, `H = 3`; el recinto,
`[[-2,-1.5],[-2,1.5],[2,1.5],[2,-1.5]]`.

- Oyente: `x_r = −2 + 0,38·4 = −0,48` → `[-0.48, 0, 1.2]`.
- Monitores: `s = 1,2` da `x_m = −0,48 − 0,866·1,2 = −1,52`, a 0,48 m
  del frente: menos de 0,6 m pero más de 0,3, se acepta en una sala chica
  (con `s = 1,0`, `x_m = −1,35`, a 0,65 m) → `[-1.52, ∓0.6, 1.25]`,
  `yaw = atan2(0.6, 1.04) = ±30°`, `pitch = atan2(0.05, 1.2) = 2,4°`.
- Mesa `[0.9, 1.8, 0.77]` en `x = −0,48 − 0,40 − 0,45 = −1,33` → centro
  `[-1.33, 0, 0.385]` (de −1,78 a −0,88). Los monitores quedan sobre la
  mesa, en pies, a 0,26 m de su borde de atrás.
- Panel izquierdo: monitor L (`y_m = −0,6`): `x = −1,52 + 1,04·(1,5 −
  0,6)/(3 − 0,6) = −1,13`; monitor R (`y_m = +0,6`): `x = −1,52 +
  1,04·(1,5 + 0,6)/(3 + 0,6) = −0,91`. Un panel de 1,2 m centrado entre
  los dos, en −1,02: `dimensions [1.2, 0.1, 1.2]`, `center [-1.02, -1.45,
  1.2]`, material en `"Pared +Y"`. El derecho, espejado: `center [-1.02,
  1.45, 1.2]`, material en `"Pared -Y"`.
- Nube: `x = −1,52 + 1,04·(1,75)/(3,55) = −1,01` → `[1.5, 1.2, 0.1]` en
  `[-1.01, 0, 2.9]`, material en `"Piso"`.
- Trampas `[0.4, 0.4, 1.6]` en `[±1.8, ±1.3, 0.8]`.
- Difusor `[0.18, 1.8, 1.1]` en `[1.91, 0, 1.2]`, material en `"Pared -X"`.
- Sofá `[0.75, 1.6, 0.85]` delante del difusor: `x = 2 − 0,18 − 0,375 =
  1,445` → `[1.445, 0, 0.425]`.

El volumen, 36 m³, está por debajo de los 40 recomendados: **se dice**, y
la sala sigue siendo de 3 × 4 × 3.

Un diseño completo con esta receta, con el texto para el usuario: §52.5.

### 52.4 Lo que hace el programa

Al aplicar el diseño (y en `/api/validate` y `/api/design`, §42):

**Corrige**, porque tiene una sola respuesta correcta:

- lo geométrico de §0.5: paneles, muebles, trampas, lo que atraviesa
  paredes, lo que tapa una puerta o una ventana, parlantes y puntos
  afuera o adentro de un objeto macizo (un sub que queda adentro de la
  mesa sale al costado, no a las piernas del oyente);
- el material en caras que no se ven;
- **el triángulo**: si abre menos de 50° o más de 70° y el vértice del
  triángulo equilátero con los monitores deja al oyente más cerca del
  38 %, el oyente va al vértice (con monitores L, R y C; con un surround
  no, porque cambiaría los ángulos de los de atrás);
- **el apuntado**: todos los monitores (también los de surround) apuntan
  al oyente, en yaw y en pitch;
- **la mesa**: de frente (el lado largo cruzado al eje de escucha) y con
  su borde 0,40 m delante del oyente cuando el eje de escucha la cruza y
  el oyente quedaba encima, pegado, detrás o a más de 0,6 m; lo que la
  mesa pisa en su lugar nuevo se corre al costado;
- **los paneles de primera reflexión**: si hay uno solo en una lateral y
  no cubre los puntos de primera reflexión, se desliza por la pared hasta
  cubrirlos (o el más fuerte), sin tapar aberturas ni meterse en otros
  objetos;
- **la nube**: si hay una y no cubre los puntos de reflexión del techo,
  se corre sobre ellos.

**Avisa**, porque es una decisión de diseño: el triángulo que sigue lejos
de 60°, el oyente lejos del 38 %, paredes laterales con materiales
distintos, una ventana en un punto de primera reflexión, un panel que tapa
una abertura y no tiene dónde correrse, un objeto delante de una puerta,
objetos que se meten uno en otro, paneles que no se pudieron correr.

Un estudio, para el programa: monitores `L` y `R` (modelos de estudio de
la librería o con «monitor» en el nombre, fuera de un `sub_array`), un
`receiver_pos` adentro y menos de 400 m³.

### 52.5 Un diseño completo, con el informe: control room de 5,7 × 4,2 × 3,0 m

El pedido: «diseñame un control room de 5,7 × 4,2 × 3 m para mezcla estéreo».
Abajo están el texto que ve el usuario y el JSON. Cada medida sale de una cuenta
(§52.2), y el diseño se probó en CADSFS:
- se aplica sin correcciones ni avisos;
- el RT se calculó por Sabine, por Eyring y con el trazado de rayos.

**Es un ejemplo: con otra sala, otras cuentas.** No copies medidas ni
posiciones: copiá el método y el nivel de detalle. El ejemplo de §52.3 (3 × 4 × 3)
es la misma receta con otra sala.

#### El texto para el usuario

Va sin fragmentos entre comillas invertidas ni nombres de campos: el usuario lee
medidas, materiales y el porqué. El JSON va después, en su bloque.

> **Control room de 5,70 × 4,20 × 3,00 m para mezcla estéreo**
>
> **1. La sala.**
> - 5,70 × 4,20 × 3,00 m: proporción 1 : 1,4 : 1,9 (Sepmeyer).
> - 72 m³ en bruto; con el tratamiento y los muebles quedan unos 60 m³ de aire.
> - La frecuencia de Schroeder anda por 120 Hz: por debajo mandan los modos.
> - Los axiales hasta 200 Hz: 30, 41, 57, 60, 82, 90, 114, 120, 122, 150, 163,
>   172 y 180 Hz. Quedan juntos 57 y 60 Hz, y 120 y 122 Hz.
> - El oyente al 38 % del largo evita los nulos de los tres primeros modos a lo
>   largo. A cambio, el cuarto modo a lo largo (120 Hz) tiene un nulo en ese
>   punto; y, por estar en el eje, también el primero y el tercero a lo ancho
>   (41 y 122 Hz).
>
> **2. Reverberación.**
> - El objetivo de EBU Tech 3276 para 60 m³ es Tm = 0,25·(V/100)^(1/3) = 0,21 s:
>   el promedio de los tercios de 200 Hz a 4 kHz. Tiene que quedar entre 0,2 y
>   0,4 s, sin saltos de más de 0,05 s entre tercios vecinos.
> - Con las superficies que ve el sonido, el Tm da 0,22 s por Sabine y 0,18 s
>   por Eyring.
> - Por octava (Sabine): 0,47 s en 63 Hz, 0,33 en 125, 0,25 en 250, 0,22 en 500,
>   0,21 en 1 y 2 kHz y 0,20 en 4 kHz. No hay saltos entre tercios.
> - Eyring queda algo por debajo de 0,2 s. Pero las dos fórmulas suponen campo
>   difuso, y acá el tratamiento no está repartido en forma pareja: el T real va a
>   salir más largo que Eyring. Verificalo con el trazado de rayos antes de
>   construir. Si diera menos de 0,2 s, se saca absorción de agudos: la lana de
>   50 mm del frente alrededor de la ventana, o la de arriba de los difusores.
>
> **3. Tratamiento.**
> - **Frente.** Detrás de cada monitor, un absorbente de 250 mm (100 mm de lana
>   de roca y 150 mm de cámara), de 0,90 m de ancho y del piso a 2,10 m, sin tapar
>   la ventana. El resto del frente, lana de 50 mm detrás de tela.
> - **Primeras reflexiones laterales.** En la pared izquierda, la del monitor L
>   cae en x = −1,54 m y la del R en x = −1,27 m. Va un panel de lana de 100 mm de
>   1,60 × 1,20 m, centrado en x = −1,40 m, de 0,60 a 1,80 m de altura. El de la
>   derecha, espejado.
> - **Techo.** Los puntos de reflexión de los dos monitores caen en x = −1,39 m,
>   y = ±0,41 m. Va una nube de lana de 100 mm de 1,80 × 1,60 m, a 8 cm del techo.
> - **Graves.**
>   - En las cuatro esquinas, trampas de 0,50 × 0,50 m de piso a techo: lana de
>     200 mm con 300 mm de cámara y velo de aluminio.
>   - En las aristas del techo con el frente y con el fondo, trampas de
>     0,40 × 0,40 m.
>   - En el techo de atrás, dos absorbentes de membrana de contrachapado de 6 mm:
>     uno sobre 300 mm de cámara (63 Hz) y otro sobre 100 mm (110 Hz).
> - **Fondo.** Un difusor QRD de 2,0 × 1,0 m a la altura del oído. Arriba, un
>   resonador de placa de yeso perforada sobre 200 mm de cámara, que absorbe de
>   160 a 400 Hz.
> - **Laterales detrás del oyente.** Difusores QRD de 1,40 × 1,20 m. Arriba de
>   cada uno, lana de 100 mm: corta el ida y vuelta entre las dos paredes.
> - **Superficies.** Paredes y techo de placa de yeso. Piso de parquet, con una
>   alfombra de 2,15 × 3,0 m entre la silla y el sofá: corta el ida y vuelta
>   entre el piso y el techo de atrás.
>
> **4. Monitores y escucha.**
> - El oyente, en x = −0,68 m (al 38 % desde el frente), en el eje, a 1,20 m.
> - ADAM A7V en triángulo equilátero de 1,60 m: en x = −2,07 m, y = ±0,80 m, a
>   1,25 m. Apuntan al oído: ±30° y 1,8° hacia abajo.
> - Quedan a 0,78 m de la pared del frente, así que la cancelación de esa
>   reflexión cae cerca de 110 Hz. El absorbente de 250 mm la atenúa, pero no la
>   borra.
> - La mesa, de 0,90 × 1,80 m, tiene su borde a 0,40 m del oyente, con racks a
>   los costados. Los monitores van en pies, detrás de la mesa.
> - El sub va en el piso, a un tercio del ancho desde la esquina izquierda del
>   frente.
> - El RT y las reflexiones se calculan desde el monitor izquierdo.
>
> **5. Aislamiento.**
> - Paredes: doble placa de yeso de 15 mm, 80 mm de lana, 20 mm de aire y
>   ladrillo de 120 mm. Rw 69.
> - Techo: doble placa de 15 mm suspendida, 80 mm de lana, 100 mm de aire y losa
>   de 150 mm. Rw 69.
> - Piso flotante: contrachapado de 18 mm y carpeta de 100 mm sobre 50 mm de
>   lana, sobre una losa de 200 mm. Rw 70.
> - Ventana a la sala de grabación: laminado de 12,8 mm, 200 mm de cámara y
>   laminado de 8,8 mm. Rw 45. Con ella, la pared del frente llega a unos 55 dB.
> - Puerta: MDF de 25 mm, 50 mm de lana y MDF de 25 mm. Rw 51.
>
> **6. Lo que no se cumple, o hay que medir.**
> - **La mesa.** Su reflexión llega 0,7 ms después del directo y apenas 2 dB por
>   debajo; EBU pide 10 dB en los primeros 15 ms. Pasa con cualquier mesa: se
>   reduce con una mesa más baja, más corta o inclinada, no con absorbente. Las
>   demás reflexiones de los primeros 15 ms quedan más de 10 dB abajo.
> - **La planta.** Tiene 24 m², y EBU pide 40 m² para una sala de escucha de
>   referencia. Como control room de mezcla, sirve.
> - **Los graves.** Por debajo de 120 Hz la sala es modal: en el punto de escucha
>   va a haber picos y valles que el RT no muestra, sobre todo cerca de 120 Hz.
>   Hay que medirlos.
> - **El frente.** La cancelación de alrededor de 110 Hz queda atenuada, pero no
>   eliminada.
> - **La ventana.** En la obra, el vidrio interior va inclinado 5-10°; en el
>   modelo, la abertura es plana.

#### El JSON

```json
{
  "project_name": "Control room 5,7 × 4,2 × 3,0 (ejemplo de referencia)",
  "project_venue_type": "Estudio · control room",
  "enclosure": {"kind": "extrude", "name": "Control room", "height": 3.0, "polygon": [[-2.85, -2.1], [-2.85, 2.1], [2.85, 2.1], [2.85, -2.1]], "openings": [
    {"wall": 0, "name": "Ventana CR-LR", "type": "window", "pos_along": 1.5, "pos_up": 1.0, "width": 1.2, "height": 0.9, "material_a": "Vidrio (ventana)", "assembly_id": "asm_ventana"},
    {"wall": 3, "name": "Puerta", "type": "door_closed", "pos_along": 0.55, "pos_up": 0.0, "width": 0.9, "height": 2.05, "material_a": "Madera maciza barnizada (panel)", "assembly_id": "asm_puerta"}
  ]},
  "objects": [
    {"name": "Absorbente frente izq. (SBIR)", "kind": "box", "dimensions": [0.25, 0.9, 2.1], "center": [-2.725, -1.1, 1.05], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (σ≈18k) + cámara 150 mm (pared rígida)"},
    {"name": "Absorbente frente der. (SBIR)", "kind": "box", "dimensions": [0.25, 0.9, 2.1], "center": [-2.725, 1.1, 1.05], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (σ≈18k) + cámara 150 mm (pared rígida)"},
    {"name": "Panel 1.ª reflexión izq.", "kind": "box", "dimensions": [1.6, 0.1, 1.2], "center": [-1.403, -2.05, 1.2], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (pared rígida)"},
    {"name": "Panel 1.ª reflexión der.", "kind": "box", "dimensions": [1.6, 0.1, 1.2], "center": [-1.403, 2.05, 1.2], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (pared rígida)"},
    {"name": "Nube de techo", "kind": "box", "dimensions": [1.8, 1.6, 0.1], "center": [-1.387, 0.0, 2.87], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (pared rígida)"},
    {"name": "Trampa esquina frente izq.", "kind": "box", "dimensions": [0.5, 0.5, 3.0], "center": [-2.6, -1.85, 1.5], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 200 mm (σ≈18k) + cámara 300 mm (foil aluminio) (pared rígida)"},
    {"name": "Trampa esquina frente der.", "kind": "box", "dimensions": [0.5, 0.5, 3.0], "center": [-2.6, 1.85, 1.5], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 200 mm (σ≈18k) + cámara 300 mm (foil aluminio) (pared rígida)"},
    {"name": "Trampa esquina fondo izq.", "kind": "box", "dimensions": [0.5, 0.5, 3.0], "center": [2.6, -1.85, 1.5], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 200 mm (σ≈18k) + cámara 300 mm (foil aluminio) (pared rígida)"},
    {"name": "Trampa esquina fondo der.", "kind": "box", "dimensions": [0.5, 0.5, 3.0], "center": [2.6, 1.85, 1.5], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 200 mm (σ≈18k) + cámara 300 mm (foil aluminio) (pared rígida)"},
    {"name": "Trampa arista techo-frente", "kind": "box", "dimensions": [0.4, 3.1, 0.4], "center": [-2.65, 0.0, 2.8], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (σ≈6k) + cámara 300 mm (papel kraft) (pared rígida)"},
    {"name": "Trampa arista techo-fondo", "kind": "box", "dimensions": [0.4, 3.1, 0.4], "center": [2.65, 0.0, 2.8], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (σ≈6k) + cámara 300 mm (papel kraft) (pared rígida)"},
    {"name": "Difusor QRD fondo", "kind": "box", "dimensions": [0.2, 2.0, 1.0], "center": [2.75, 0.0, 1.4], "is_enclosure": false, "side_a_exterior": true, "material": "Difusor QRD 1D N=7 depth=180mm w=100mm (f_min≈476 Hz) - MDF"},
    {"name": "Resonador perforado fondo", "kind": "box", "dimensions": [0.215, 3.1, 0.6], "center": [2.743, 0.0, 2.25], "is_enclosure": false, "side_a_exterior": true, "material": "Panel perforado Yeso t=15mm d=6mm φ=8% cav=200mm"},
    {"name": "Difusor lateral trasero izq.", "kind": "box", "dimensions": [1.4, 0.2, 1.2], "center": [0.55, -2.0, 1.4], "is_enclosure": false, "side_a_exterior": true, "material": "Difusor QRD 1D N=7 depth=180mm w=100mm (f_min≈476 Hz) - MDF"},
    {"name": "Difusor lateral trasero der.", "kind": "box", "dimensions": [1.4, 0.2, 1.2], "center": [0.55, 2.0, 1.4], "is_enclosure": false, "side_a_exterior": true, "material": "Difusor QRD 1D N=7 depth=180mm w=100mm (f_min≈476 Hz) - MDF"},
    {"name": "Absorbente lateral alto izq.", "kind": "box", "dimensions": [1.4, 0.1, 0.6], "center": [0.55, -2.05, 2.35], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (pared rígida)"},
    {"name": "Absorbente lateral alto der.", "kind": "box", "dimensions": [1.4, 0.1, 0.6], "center": [0.55, 2.05, 2.35], "is_enclosure": false, "side_a_exterior": true, "material": "Lana mineral (roca) 100 mm (pared rígida)"},
    {"name": "Membrana techo 110 Hz", "kind": "box", "dimensions": [1.35, 3.1, 0.106], "center": [0.275, 0.0, 2.947], "is_enclosure": false, "side_a_exterior": true, "material": "Absorbente de membrana: Contrachapado 6 mm (~3 kg/m²) + cámara 100 mm"},
    {"name": "Membrana techo 63 Hz", "kind": "box", "dimensions": [1.4, 3.1, 0.306], "center": [1.7, 0.0, 2.847], "is_enclosure": false, "side_a_exterior": true, "material": "Absorbente de membrana: Contrachapado 6 mm (~3 kg/m²) + cámara 300 mm"},
    {"name": "Mesa de mezcla", "kind": "box", "dimensions": [0.9, 1.8, 0.77], "center": [-1.534, 0.0, 0.385], "is_enclosure": false, "side_a_exterior": true, "material": "Madera (panel)"},
    {"name": "Rack izq.", "kind": "box", "dimensions": [0.6, 0.5, 0.9], "center": [-1.534, -1.2, 0.45], "is_enclosure": false, "side_a_exterior": true, "material": "Madera (panel)"},
    {"name": "Rack der.", "kind": "box", "dimensions": [0.6, 0.5, 0.9], "center": [-1.534, 1.2, 0.45], "is_enclosure": false, "side_a_exterior": true, "material": "Madera (panel)"},
    {"name": "Sofá", "kind": "box", "dimensions": [0.8, 1.6, 0.85], "center": [2.2, 0.0, 0.425], "is_enclosure": false, "side_a_exterior": true, "material": "Sofá 2 plazas (sin ocupación) tapizado fabric, relleno thick"},
    {"name": "Alfombra", "kind": "box", "dimensions": [2.15, 3.0, 0.012], "center": [0.675, 0.0, 0.006], "is_enclosure": false, "side_a_exterior": true, "material": "Alfombra"}
  ],
  "materials": [],
  "source_pos": [-2.07, -0.8, 1.25],
  "receiver_pos": [-0.684, 0.0, 1.2],
  "surface_group_material": {
    "1|Piso": "Parquet de madera barnizado",
    "1|Techo": "Pladur / placa de yeso (sobre perfilería)",
    "1|Pared 0": "Lana mineral (roca) 50 mm (pared rígida)",
    "1|Pared 1": "Pladur / placa de yeso (sobre perfilería)",
    "1|Pared 2": "Pladur / placa de yeso (sobre perfilería)",
    "1|Pared 3": "Pladur / placa de yeso (sobre perfilería)",
    "1|Ventana CR-LR": "Vidrio (ventana)",
    "1|Puerta": "Madera maciza barnizada (panel)"
  },
  "surface_group_material_b": {
    "1|Piso": "Hormigón liso",
    "1|Techo": "Hormigón liso",
    "1|Pared 0": "Ladrillo visto",
    "1|Pared 1": "Ladrillo visto",
    "1|Pared 2": "Ladrillo visto",
    "1|Pared 3": "Ladrillo visto"
  },
  "wall_assemblies": {
    "asm_pared": {"layers": [
      {"material_id": "gyp_15", "thickness_mm": 15, "bonded_with_prev": true},
      {"material_id": "gyp_15", "thickness_mm": 15, "bonded_with_prev": true},
      {"material_id": "mineral_wool_80", "thickness_mm": 80, "bonded_with_prev": false},
      {"material_id": "air_20", "thickness_mm": 20, "bonded_with_prev": false},
      {"material_id": "brick_solid_120", "thickness_mm": 120, "bonded_with_prev": false}
    ]},
    "asm_techo": {"layers": [
      {"material_id": "gyp_15", "thickness_mm": 15, "bonded_with_prev": true},
      {"material_id": "gyp_15", "thickness_mm": 15, "bonded_with_prev": true},
      {"material_id": "mineral_wool_80", "thickness_mm": 80, "bonded_with_prev": false},
      {"material_id": "air_100", "thickness_mm": 100, "bonded_with_prev": false},
      {"material_id": "concrete_150", "thickness_mm": 150, "bonded_with_prev": false}
    ]},
    "asm_piso": {"layers": [
      {"material_id": "plywood_18", "thickness_mm": 18, "bonded_with_prev": true},
      {"material_id": "concrete_100", "thickness_mm": 100, "bonded_with_prev": true},
      {"material_id": "mineral_wool_50", "thickness_mm": 50, "bonded_with_prev": false},
      {"material_id": "concrete_200", "thickness_mm": 200, "bonded_with_prev": false}
    ]},
    "asm_ventana": {"layers": [
      {"material_id": "glass_lam_12_8", "thickness_mm": 12.8, "bonded_with_prev": true},
      {"material_id": "air_200", "thickness_mm": 200, "bonded_with_prev": false},
      {"material_id": "glass_lam_8_8", "thickness_mm": 8.8, "bonded_with_prev": false}
    ]},
    "asm_puerta": {"layers": [
      {"material_id": "mdf_25", "thickness_mm": 25, "bonded_with_prev": true},
      {"material_id": "mineral_wool_50", "thickness_mm": 50, "bonded_with_prev": false},
      {"material_id": "mdf_25", "thickness_mm": 25, "bonded_with_prev": false}
    ]}
  },
  "surface_assembly_map": {
    "1|Piso": "asm_piso",
    "1|Techo": "asm_techo",
    "1|Pared 0": "asm_pared",
    "1|Pared 1": "asm_pared",
    "1|Pared 2": "asm_pared",
    "1|Pared 3": "asm_pared",
    "1|Ventana CR-LR": "asm_ventana",
    "1|Puerta": "asm_puerta"
  },
  "speaker_systems": [
    {"name": "Monitores L/R", "enabled": true, "mount": "monitor", "channel": "stereo", "elements": [
      {"name": "Monitor L", "channel": "L", "model_id": "adam_a7v", "pos": [-2.07, -0.8, 1.25], "yaw_deg": 30.0, "pitch_deg": 1.8},
      {"name": "Monitor R", "channel": "R", "model_id": "adam_a7v", "pos": [-2.07, 0.8, 1.25], "yaw_deg": -30.0, "pitch_deg": 1.8}
    ]},
    {"name": "Sub", "enabled": true, "mount": "sub_array", "sub_decoupling": "direct", "elements": [
      {"name": "Sub", "channel": "M", "model_id": "sub_omni_ideal", "pos": [-2.4, -0.7, 0.25], "yaw_deg": 0.0, "pitch_deg": 0.0}
    ]}
  ]
}
```

#### Cómo se llegó a esto

- **Todo sale de la receta de §52.2.** Con estos números:
  - oyente: `x_r = −2,85 + 0,38·5,70 = −0,684`;
  - monitores: `x_m = −0,684 − 0,866·1,60 = −2,070`;
  - reflexión del monitor L en la pared izquierda:
    `x = −2,070 + 1,386·(2,10 − 0,80)/(4,20 − 0,80) = −1,540`;
  - la del R: `−2,070 + 1,386·(2,10 + 0,80)/(4,20 + 0,80) = −1,266`;
  - techo: `t = (3,00 − 1,25)/(6,00 − 1,25 − 1,20) = 0,493`, así que la nube va
    en `x = −2,070 + 0,493·1,386 = −1,387`;
  - mesa: `x = −0,684 − 0,40 − 0,45 = −1,534`.
- **El recinto, reflectante; el tratamiento, en objetos.** Las superficies del
  recinto son placa de yeso y parquet, con lana en el frente. Con las de la tabla
  de §2 la sala da Tm de 0,13 s por Eyring.
- **La absorción, repartida en los tres ejes:** frente y fondo, las dos
  laterales, piso y techo. Sin la alfombra y sin la lana alta de los laterales,
  Sabine y Eyring daban el nominal justo (0,25 y 0,21 s), pero el trazado de rayos
  de CADSFS daba T20 de 0,37 s: el piso y el techo reflectantes y paralelos
  estiraban la cola. Con este JSON (100 000 rayos), el trazado da EDT 0,19 s,
  T20 0,27 s y T30 0,29 s, dentro del rango de EBU. Por eso el estimado se apunta
  con Sabine al valor nominal y se pide verificar con el trazado.
- **El material, en todo el objeto (`"material"`).** Las caras que dan contra la
  pared no cuentan.
- **La fuente (`source_pos`), en el monitor izquierdo.** Con `s` = 1,6 m queda a
  1,60 m del oyente, más de los 1,5 m que pide CADSFS.
- **Los graves, con tres recursos:**
  - trampas en las esquinas y en las aristas, donde todos los modos tienen
    presión máxima;
  - membranas sintonizadas: `f0 = 60/√(m·d)`, con 3 kg/m² y 0,30 m da 63 Hz, y
    con 0,10 m, 110 Hz;
  - un resonador perforado para la zona de 160-400 Hz.
- **24 objetos.** El «8-12» de §27.7 es un mínimo, no un tope.
