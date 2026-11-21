# Guía de buenas prácticas en movilidad eléctrica

Fuente: . Páginas 183–215 de bases2c.pdf.

<!-- guia-buenas-practicas-em:p183 · pág. 183 -->
1. Introducción
2. Glosario
3. ¿Conviene migrar a la movilidad eléctrica?
4. Sistema de carga
5. Recomendaciones para la red de cargadores con acceso público
6. Anexos

Introducción
El Programa de Gobierno del Presidente de la República Sebastián Piñera Echenique consigna, para el periodo
entre 2018 a 2022, la progresiva irrupción de la movilidad eléctrica como parte del abanico de oportunidades de
innovación y desarrollo tecnológico del sector energético al servicio del progreso del país, quedando lo anterior
plasmado en el documento de política energética denominado “Ruta Energética 2018-2022: Liderando la
modernización con sello ciudadano”, el cual busca definir el camino y prioridades en materia energética para los
próximos cuatro años. Dicho documento fue lanzado durante el mes de mayo de 2018 y en su eje 5 denominado
“Transporte Eficiente: Energía en movimiento”, señala como meta que al año 2022 existan al menos 10 veces
más vehículos eléctricos en las calles de nuestro país, lo que implica incentivar el desarrollo de puntos de carga
públicos y/o privados y la incorporación de nuevos vehículos a nuestro sistema de transporte. Por su parte la
Estrategia Nacional de Electromovilidad establece una meta de largo plazo que consiste en que el 100% de la
flota de transporte público y el 40% de los vehículos particulares sean eléctricos al 2050.
En este contexto, diferentes actores como municipalidades, distribuidoras de combustibles, centros comerciales,
distribuidoras de energía eléctrica, proveedores de tecnologías, academia, entre otros, han promovido la movilidad
eléctrica a través de la instalación de puntos de carga de energía e incorporación del vehículos eléctricos al
parque en circulación y desarrollo en investigación al respecto. Este avance, es relativamente incipiente todavía en
nuestro país y sin embargo ya existe experiencia acumulada que puede y debe ser compartida entre todos quienes
ya están involucrados con esta tecnología y todos quienes están pensando en sumarse en el corto y mediano
plazo.

<!-- guia-buenas-practicas-em:p185 · pág. 185 -->
Por ello, es necesario generar una Guía de Buenas Prácticas en Movilidad Eléctrica, especialmente en relación
a la instalación de cargadores en el bien nacional de uso público con el fin de mejorar el uso de estos espacios.
Esta Guía pretende que la incorporación de más actores se beneficie del camino ya recorrido, disminuyendo
las asimetrías de información, mejorando la experiencia de los nuevos usuarios de vehículos eléctricos y con
ello, lograr fomentar la introducción temprana de una mayor cantidad de este tipo de vehículos, y así alcanzar
beneficios para la mitigación del cambio climático, la disminución de la contaminación local, eficiencia energética
en transporte y mejoras en la calidad de vida.
El objetivo de esta Guía es convertirse en un documento de referencia en todo lo relacionado con la movilidad
eléctrica, tanto para los ciudadanos, administraciones públicas y entidades que les interese fomentar la movilidad
eléctrica, como también para los tomadores de decisiones durante el proceso de penetración de esta tecnología.

<!-- guia-buenas-practicas-em:p186 · pág. 186 -->
Glosario
Batería del vehículo: dispositivo de almacenamiento de la energía eléctrica del vehículo que se carga a través de
corriente continua (DC). La capacidad de esta batería, junto a otras variables como el rendimiento del vehículo y
estilo de conducción determinan su autonomía.
Cargador (EV Charger o EVC): dispositivo conectado a una fuente de energía eléctrica destinado para cargar las
baterías de un Vehículo Eléctrico. La carga se puede realizar en corriente alterna (AC) o en corriente continua (DC),
en el último caso el cargador posee un convertidor de energía eléctrica de alterna a continua (AC /DC), que realiza
la carga directa a la batería del BVE.
Combined Charging System (CCS): protocolo de carga de vehículos en corriente continua (DC). Popular en
vehículos de origen europeo para carga de vehículos con cargadores rápidos y ultra rápidos.
Charge on Move (CHAdeMO): protocolo de carga de vehículos en corriente continua (DC). Popular en vehículos
de origen asiático para carga de vehículos con cargadores rápidos y ultra rápidos.
Convertidor AC/DC: convertidor de energía que se encarga de transformar la corriente alterna que proviene de
la red eléctrica a corriente continua para almacenarla en la batería del vehículo (de AC a DC). Se puede encontrar
al interior del vehículo, así como al interior de los cargadores. En ocasiones el convertidor puede ser bidireccional
(AC/DC- DC/AC), es decir, es capaz de entregar electricidad a la red a partir de las baterías restringen a vehículos
motorizados de transporte terrestre de carga o pasajeros, que sean livianos o medianos (hasta 3.860 kg de peso
bruto vehicular).
Control de carga del vehículo: dispone el método de carga de la batería, la que puede ser a tensión, corriente
o potencia constante o una mezcla de ambos, pero no simultánea, en otras alternativas programadas por el
fabricante. Entre las funciones más relevantes es el monitoreo de la temperatura de las baterías, estado de
la conexión entre vehículo y cargador, estado interno de los módulos de potencia y convertidor del cargador,
sincronización de carga vehículo/cargador y estado de la carga.

<!-- guia-buenas-practicas-em:p187 · pág. 187 -->
Instalación eléctrica: corresponde a los elementos necesarios de protección, seguridad y la conducción de la
energía, desde la fuente de energía eléctrica, hasta el cargador.
Piloto control de carga: sirve para muchas funciones de control de la carga, entre ellas verificar la correcta
conexión del vehículo a la red, continuidad de la puesta a tierra entre otras. Se usa en las modo de carga modo 4,
modo 3 y en el modo 2 de carga se encuentra incorporado al cable de carga.
Toma de Carga AC (Carga AC): protocolo de carga de corriente alterna. Existen varios estándares, pero el más
masivo actualmente en la toma AC Type II. La carga AC siempre se considera una carga lenta ya que puede llegar a
demorarse el hasta 3 veces más que una carga por DC.
Vehículo: para efectos de esta guía, los vehículos de los que se habla se restringen a vehículos motorizados de
transporte terrestre de carga o pasajeros, que sean livianos o medianos (hasta 3.860 kg de peso bruto vehicular).
Vehículo de combustión interna (ICE): vehículo impulsado por un motor que utilice diésel o gasolina como
combustible.
Vehículo eléctrico (EV): vehículo impulsado por al menos un motor eléctrico. Incluye vehículo eléctrico a
baterías y vehículo híbrido enchufable (con recarga exterior).
Vehículo eléctrico a baterías (BEV): es un tipo de EV alimentado únicamente por baterías recargables (BEV, por
su sigla en inglés).
Vehículo híbrido con recarga exterior (PHEV): es un tipo de EV que contiene al menos dos motores, uno de
combustión interna que utiliza gasolina y otro eléctrico cuyas baterías pueden ser recargadas enchufando el
vehículo a una fuente externa de energía eléctrica, o a través de su propio motor de combustión interna (PHEV, por
su sigla en inglés).
Cargador de muro o pedestal (Wallbox): dispositivo de carga AC o DC que se instala en pared o pedestal tanto
en instalación públicas como particulares. Algunas marcas de vehículos lo ofrecen como accesorio opcional y
fabricantes de cargadores rápidos también ofrecen este tipo de cargadores.

<!-- guia-buenas-practicas-em:p188 · pág. 188 -->
¿Conviene migrar a la
movilidad eléctrica?
Los BEV poseen una serie de características y beneficios determinantes sobre los vehículos convencionales de
combustión interna. Algunas de ellas se mencionan a continuación:

Económicos
Precio: actualmente en el mercado chileno un vehículo eléctrico tiene un valor entre dos a tres veces mayor que
uno convencional, con similares prestaciones de servicio. En el Anexo 1, se muestran dos ejemplos en los que se
compara un BEVcon un ICE bajo supuesto de usos en la región metropolitana.
Costos de operación (energía eléctrica versus combustible): desde el punto de vista energético, un motor a
combustión tiene un eficiencia aproximada del 20 o 25%, mientras que un motor eléctrico, la eficiencia es del
95%. Esta mayor eficiencia de los vehículos eléctricos (de hasta 4 veces comparado a uno convencional) implica
un menor costo por kilómetro recorrido, por lo tanto, un vehículo eléctrico presenta menores costos de operación
que uno de combustión interna.
Por ejemplo, los recintos administrados por el estado la tarifa más predominante es la BT1, donde la recarga
debiera ser nocturna, el valor de la energía a la fecha es de $119,3(1) pesos por kilowatt-hora (kWh)(2) y el BEV tiene
un rendimiento eléctrico aproximado de 8,8 km/kWh ,comparado con un vehículo de combustión interna, que
carga gasolina $800(3) pesos por litro que tienen un rendimiento de 11 km/l, ahorra en cada kilómetro recorrido
$57 pesos. Si recorre un poco más de 40.000 kilómetros al año, puede llegar a ahorrar hasta 2,0 millones de
pesos al año. Por lo tanto, el recorrido anual de un vehículo es una variable determinante a la hora de evaluar la
rentabilidad de invertir en un vehículo eléctrico.

1 https://www.eneldistribucion.cl/tarifas/septiembre2018.
2 http://www.consumovehicular.cl/inicio#/
3 http://www.bencinaenlinea.cl/web2/buscador.php?region=7

<!-- guia-buenas-practicas-em:p189 · pág. 189 -->
Costos de mantención: dado que los vehículos eléctricos poseen menos componentes mecánicos que friccionan
entre sí y menor variación de temperatura, están expuestos a un menor desgaste, lo que se traduce en que
requiere menos sustituciones y revisiones regulares que un vehículo convencional. En la medida que se recojan
antecedentes de los proyectos pilotos en curso se podrá cuantificar el ahorro en mantención, los que serán
incorporados en siguiente versión de la guía.
Sin embargo, si simplificamos el ejercicio considerando la comparación de las mantenciones periódicas y que son
realizadas en concesionarias autorizadas para ello, al menos se debería tener en cuenta el ahorro por concepto
de reemplazo de lubricantes, que no son requeridos en las mantenciones de un BEV, y que en un vehículo de más
de 40.000 kilómetros de recorrido anual, está en torno a los $200.000.
Evaluación económica: como se ha visto, un BEV tiene un mayor costo de inversión (precio de compra) y al
mismo tiempo tiene menores costos de operación y mantención, por lo cual, para saber si conviene o no optar
por un vehículo de estas características es clave tener en consideración la cantidad de kilómetros recorridos
anualmente por el vehículo y su valor residual al término del periodo de evaluación.
De esta forma se puede hacer una evaluación económica, la cual nos indicará cuándo se puede llegar a obtener
un retorno positivo de la inversión. En el Anexo 1, se muestran dos ejemplos de cálculo simple, como primera
aproximación, en los cuáles se puede observar que para un recorrido anual mayor a 40.000 km, para el caso que
el valor del BEV es el doble del convencional y mayor a 70.000 km al año para el caso donde el valor del BEV es el
triple. En ambos ejemplo se calculan retorno positivo para un horizonte de evaluación de 8 años. Considerando el
valor residual cero para las alternativas comparadas y valores de energía de la Región Metropolitana.
Valoración económica de las externalidades negativas: en algunos entidades ya sea pública o privada
cuentan con metodologías para dar valor a la mejora de las externalidades negativas del transporte con motor
convencional.

<!-- guia-buenas-practicas-em:p190 · pág. 190 -->
Ambientales
Contaminación local: los vehículos eléctricos no emiten gases de
forma directa, por lo tanto no contaminan localmente con gases
(en el lugar donde se utilizan), es por eso que están exentos de
restricción vehicular. Sin embargo, la generación de la electricidad
que consume el BEV, el cual contaminará en la medida que las
centrales generadoras produzcan emisiones contaminantes.
Emisiones de gases efecto invernadero (GEI): las
emisiones de GEI dependen de la matriz de generación
eléctrica existente, es decir si la generación de
electricidad en el país proviene de energías
renovables se considera que la electromovilidad
tiene cero emisiones. En Chile con la matriz
eléctrica actual, un vehículo eléctrico emite cerca
de tres veces menos de GEI que uno a combustión.

Evaluación
Económica

Disminución en
contaminación
local

Inversión a
plazo

Menor
costo de
mantención

Contaminación acústica: los vehículos eléctricos
casi no emiten ruido, esto se hace más relevante para
flotas numerosas de vehículos, sobre todo cuando
estos son pesados y se mueven sobre los 50 km/h.
En algunos puntos de Santiago, el Ministerio de Medio
Ambiente ha reportado mediciones por sobre los 70 dB e
incluso llegando a 90 dB, lo que supera ampliamente los 55 dB
recomendados por la OMS para espacios al aire libre.

Residuos de mantención: es importante mencionar que dado
que no utilizan lubricantes y filtros contaminados, el manejo de
residuos peligrosos disminuye considerablemente, además, dado el
funcionamiento de los frenos regenerativos reduce el desgaste del
sistema de frenos. Sin embargo la disposición final de la baterías, es
algo por resolver.

Disminución en
contaminación
acústica

Electromovilidad

Menor
costo de
operación

Se reduce
3 veces la
contaminación

Menor
emisión
de CO2

<!-- guia-buenas-practicas-em:p191 · pág. 191 -->
¿Cómo se carga
un vehículo eléctrico?
La experiencia internacional y la incipiente experiencia nacional, muestran que la carga del vehículo eléctrico se
realiza aprovechando los momentos en que el BEV permanece estacionado por varias horas, por ejemplo en los
hogares durante la noche o en los lugares de trabajo o centros comerciales, tal como la mayoría de las personas
cargan su teléfono móvil. Sin embargo, la experiencia también muestra, que además se necesita una red de carga
pública para condiciones excepcionales, incluyendo los viajes de mayor duración, fuera de los centros urbanos. La
existencia de una red de carga es un incentivo a que la movilidad eléctrica se desarrolle de forma más acelerada,
puesto que tiende a calmar la llamada “ansiedad de autonomía”, que corresponde a la inquietud, principalmente
de aquellos que no poseen BEV, de si el vehículo les permitirá alcanzar su destino, y es uno de los factores que
retrasan la decisión de moverse hacia la electromovilidad.

<!-- guia-buenas-practicas-em:p192 · pág. 192 -->
Sistema de Carga
Los BEV cuentan con una batería donde se almacena la energía eléctrica que se usa para el traslado, la cual se
carga a través de corriente continua (DC). Las fuentes de energía que habitualmente disponemos en la red de
distribución eléctrica del país están en corriente alterna (AC), por eso es necesario hacer la transformación de
corriente de AC a DC. Esta transformación se puede hacer a través del conversor interno del vehículo, o a través de
un cargador externo al vehículo el cual contiene el conversor AC/DC.
En el siguiente esquema se puede apreciar, a modo ilustrativo, cómo se realiza la carga de un vehículo eléctrico.

En la recarga mediante corriente continua, en cuyo
caso el convertidor se encuentra en el cargador
externo al vehículo, la carga se hace directo a la
batería del vehículo, por lo tanto, la limitación
de velocidad de recarga estará dada por la
disponibilidad de potencia del cargador externo,
por la capacidad de la batería, la capacidad de
disipación de temperatura en la batería y el control
de carga del vehículo

Si la recarga es en corriente alterna,
obligatoriamente la carga deberá pasar por el
convertidor AC/DC incorporado en el vehículo y la
capacidad de éste será la que fijará el tiempo de
carga, aún si existe potencia disponible en la toma
de energía de la red eléctrica. Actualmente los
convertidores internos AC/DC poseen potencias
entre 3 a 7 kW y en algunos modelos recientes 11
y 22 kW.

Alternativa corriente continua

Alternativa corriente alterna

DC

AC
Convertidor
AC / DC

AC

Batería

Convertidor AC/DC

<!-- guia-buenas-practicas-em:p193 · pág. 193 -->
Modos de Carga
La carga del vehículo puede ser de cuatro modos distintos según la norma IEC 61851-1, que se ha asimilado
operacionalmente respecto de la conectividad y comunicación entre el cargador y el vehículo.
Modo
de carga

Enchufe no
dedicado

La conexión es a una toma de corriente alterna estándar
de una instalación eléctrica existente, sin protecciones
adicionales ni control dedicado a la carga del vehículo.

Corriente alterna,
limitado a 10 [A]
Sin comunicación

La batería del vehículo toma la energía eléctrica desde el
convertidor AC/DC incorporado en el vehículo.
Es importante revisar las instalaciones eléctricas y
verificar el buen estado de la aislación del conductor, la
toma de tierra, la protección diferencial y la protección
termo magnética(4).

Convertidor
AC/DC
Batería

4 En Chile todas las instalaciones eléctricas deben contar con estos aspectos de seguridad.

El modo 1 no es
recomendable para BEV,
por la incertidumbre
de calidad y estado de
la instalación eléctrica
desde donde será
tomada la energía
eléctrica.

AC

Modo
de carga

Enchufe no dedicado con protección y control
incorporada en el cable

En el modo de recarga 2 la conexión al auto se realiza
a través de un cable donde se ha incorporado un
control de carga del vehículo, el cual cuenta con
sistema de seguridad, de comprobación de la toma de
tierra, protecciones y con posibilidad de seleccionar la
velocidad de carga.
La conexión es en AC, se utiliza una instalación y
enchufe estándar y entre el enchufe y el vehículo se
incorpora un piloto control de carga.

Corriente alterna,
potencia hasta 2,2 [kW]
1Ø y hasta 11 [kW]
3Ø .Bajo control de
carga con el dispositivo
incorporado en el cable.

La batería del vehículo toma la energía eléctrica desde
el convertidor AC/DC incorporado en el mismo.

Convertidor
AC/DC
Batería

Control
Básico
AC

<!-- guia-buenas-practicas-em:p195 · pág. 195 -->
Modo
de carga

Enchufe
dedicado

Este modo de recarga es una conexión del vehículo eléctrico a la red, utilizando un circuito y equipamiento
de control incorporado en el cargador. Este modo incorpora la protección de sobrecarga, cortocircuito,
diferencial, puesta a tierra y un piloto control de carga entre el cargador y el vehículo eléctrico.
En este tipo de recarga, el vehículo eléctrico se conecta al cargador (caja de pared o tipo poste) mediante un
cable especial. El cargador es el que está dotado con un control inteligente que se encarga de gestionar la
seguridad y proceso de carga en conjunto con el control del vehículo. El modo 3, junto al modo
de carga 2, son los de uso más extendido, ya que presentan mayores condiciones de seguridad y
Corriente alterna, potencial
control, y requieren menor inversión con respecto al modo 4.
hasta 3,5 [kW] 1Ø y hasta
44 [kW] 3Ø en cargadores
• La conexión es en AC.
con cable. Alto control de
• Protección con función de piloto de control.
carga. Recomendable en
• Verificación de conexión correcta.
estacionamientos de larga
• Enchufe sin tensión, cuando el vehículo está correctamente conectado se energiza.
estadía.
• Continuidad de la puesta a tierra.
• Corriente nominal del cargador.
• Enchufe dedicado por el vehículo eléctrico.
• La batería del vehículo toma la energía eléctrica desde el convertidor AC/DC incorporado en el vehículo

Convertidor
AC/DC
Batería

Modo
de carga

Cargador
Externo

Este modo de recarga se realiza en corriente continua, por lo tanto, el convertidor AC/
DC se encuentra en el cargador y es de mayor potencia que el convertidor interno del
vehículo, lo que se traduce en menor tiempo de carga de la batería.
La instalación eléctrica hasta el cargador debe ser independiente y con las protecciones
de sobrecarga, cortocircuito, diferencial y puesta a tierra.
La infraestructura del cargador es mayor y más cara.
La carga es más rápida porque depende de la capacidad del cargador externo y de
la capacidad de recibir energía del vehículo (batería y circuito de carga) y no de las
restricciones de capacidad del cargador del vehículo eléctrico. Se carga directo a la
batería del vehículo, la energía eléctrica no pasa por el convertidor interno.

La carga se realiza con
corriente continua desde
un cargador que contiene
un convertidor de corriente
alterna a continua.
Las potencias son mayores a
24 [kW] y alto nivel de control
de carga.
Su uso es en lugares
públicos o abiertos a
terceros.

Batería

<!-- guia-buenas-practicas-em:p197 · pág. 197 -->
Resumen de esquema general de los
modos de carga
Características

Nivel de
comunicación

Nivel de
seguridad

Potencias

Modo 1
Enchufe no
dedicado

Modo 2
Enchufe no
dedicado con
protección
y control
incorporada en el
cable

Modo 3
Enchufe Dedicado

Modo 4
Cargador Externo

Sin comunicación

Comunicación
básica

Alto nivel de
comunicación que
permite control de
carga

Alto nivel de
comunicación que
permite control de
carga

Seguridad depende
de la instalación
eléctrica de la cual
se toma la energía.

Seguridad mínima,
depende de la
instalación eléctrica,
pero existe
comprobación de la
conexión a tierra.

Mayor seguridad
porque el gabinete
del cargador tiene
protecciones
incorporadas.

Mayor seguridad
porque el gabinete
del cargador tiene
protecciones
incorporadas.

Por el momento
entre 3,5 kW a 43
kW

Potencias mayores a
24 kW

< 3,5 kW

< 22 kW si es
trifásico.
< a 7 kW si es
monofásico

<!-- guia-buenas-practicas-em:p198 · pág. 198 -->
Tipos de conectores o enchufes
Los desarrolladores de vehículos eléctricos optan por los tipos de conectores según las normas y necesidades
que establece el mercado donde se va a comercializar el vehículo. Es Chile aún no se ha definido un estándar, sin
embargo es una tarea adoptada por el Ministerio de Transporte y Telecomunicaciones (MTT) y actualmente se
encuentra en revisión de la Contraloría General de la República. La red de carga deberá estar en sintonía con los
tipos de conectores integrados en los vehículos, según la norma que establezca el MTT, es decir el sistema de
conexión del vehículo-cargador que no permita cometer error en la conexión (concepto POKA-YOKE).
Para las cargas en corriente alterna se tiene el modo 1, modo 2 y modo 3 y podemos adelantar que el modo 1 se
ha propuesto prohibirlo para los vehículos que circulen en Chile.
El tipo de conector para el modo 1 y modo 2, en el lado fuente de energía es un enchufe hembra típico de las
instalaciones eléctricas existentes, ya que es directo a las tomas de corriente y para el lado carga o del vehículo
debe es un conector adecuado al vehículo eléctrico, por ejemplo conector Tipo 2 (Mennekes ) o conector Tipo 1
(Yazaki) .
En modo 3 los conectores más utilizados tanto para el lado fuente de energía como para el lado carga (Vehículo
Eléctrico) son los siguientes: Conector Tipo 1 [SAEJ1772] (USA), Conector Tipo 2 o Mennekes [IEC62196] (Europeo)
y Tipo GB/T [GB/T 20234] (China).
En la siguiente tabla se ilustran estos conectores:
Sistema de cargas AC / Modos 2 y 3
Tipo 1
[Saej 1772]
(USA)

Tipo 2
[IEC 62196]
(Europa)

Conectores

GB/T
[GB/T 20234]
(China)

<!-- guia-buenas-practicas-em:p199 · pág. 199 -->
Para cargas en corriente continua existe el modo 4.
Este modo de recarga es de mayor potencia y carga directamente a la batería del vehículo, por ello permite cargas
más rápidas, como las que requieren los vehículos en la vía pública, para estadías de corta duración en el punto de
carga. Este modo de carga, al requerir mayor potencia, no es viable en instalaciones domiciliarias comunes de baja
tensión.
En el modo 4, los conectores utilizados son: Tipo CHAdeMO (Japón), Tipo GB/T (China), Combinado Tipo 1,
compuesto por un conector AC Tipo 1 y un conector DC con dos terminales (USA) y Combinado Tipo 2 (Europeo),
compuesto por un conector AC Tipo 2 y un conector DC con dos terminales. La tabla siguiente muestra los
conectores más usados en modo 4.
Cargando...

Sistema de cargas DC / Tipo de conectores
Combinado
Tipo 2/CCS-2

Combinado
Tipo 1/CCS-1

GB/T

Conectores

CHAdeMO

Tiempo de carga
El tiempo que demore en cargar un vehículo eléctrico dependerá de varios factores, los principales son la potencia
disponible en el cargador y la capacidad de almacenamiento de energía de la batería que posea el vehículo, pero
también influyen otros como la potencia de carga máxima permitida o el control de la temperatura en la batería.
En la siguiente tabla se muestran ejemplos de tiempos de carga hasta el 80% de la capacidad de la batería.
Capacidad de
energía
de la batería en
[kWh]

Potencia disponible en el cargador
AC

DC

2,2 [kW]

3,5 [kW]

7[kW]

11 [kW]

22 [kW]

43 [kW]

50 [kW]

175 [kW]

11 h

5,5 h

3,5 h

1,5 h

50 min

25 min

20 min

7 min

14 h

7h

3h

2h

1h

30 min

30 min

8 min

18 h

9h

4,5 h

3h

1,5 h

45 min

40 min

11 min

24 h

12 h

6h

4h

2h

1h

50 min

15 min

39 h

19 h

9,5 h

6h

3h

1,5 h

1,3 h

23 min

41 h

20 h

10 h

6,5 h

3,5 h

1,5 h

1,5 h

25 min

Modo 2

Modo 3

Modo 4

(*) Es importante no olvidar que la capacidad de carga de un vehículo en corriente alterna está limitada
también por la potencia del convertidor AC/DC interno del vehículo. Por ejemplo, si tenemos potencia
cualquiera disponible en la red y la potencia de dicho conversor fuera de 7 [kW], para cargar una batería de 24
[kWh] sería siempre un poco más de 3 horas, independiente de la potencia del cargador, ya que la velocidad
está restringida por la potencia del conversor.
(**) Tiempo calculado sin considerar las restricciones del sistema del circuito de recarga interno del VE.

<!-- guia-buenas-practicas-em:p201 · pág. 201 -->
Recomendaciones para
la red de cargadores con
acceso público
La tecnología necesaria para implementar la movilidad eléctrica cuenta con diversos
estándares a nivel mundial, esto se debe principalmente a que se trata de una tecnología
aún en desarrollo sin un acuerdo global. Sin embargo, existen esfuerzos de estandarización
y ciertas tendencias tecnológicas que vale la pena difundir para lograr que en el mercado
chileno, la masificación de la movilidad eléctrica sea con un alto grado de compatibilidad
entre vehículos y estaciones de carga, para mejorar las experiencias de los usuarios,
actuales y futuros.
En el último tiempo se ha visto un gran interés por parte de la empresas privadas, tanto
proveedores de energía, como de algunos proveedores de vehículos, proveedores de
tecnología de carga, como también por parte de autoridades locales (municipalidades y
gobiernos regionales) y otros actores, por integrarse prontamente a la movilidad eléctrica,
involucrando a los operadores de transporte y usuarios en general para avanzar hacia la
movilidad eléctrica.

Adicionalmente a los factores generales que inciden en la compra del vehículo mismo,
en cuanto a sus características económicas y ambientales presentadas anteriormente en
esta Guía, es recomendable tener presente los modos de carga admisibles por el mismo, la
capacidad de la batería, la capacidad del convertidor interno del vehículo, los conectores
(enchufes) incluidos en el vehículo, el control de carga que limita la temperatura interna de
la batería y por lo tanto, restringe la potencia de carga en DC, entre otros temas de interés
particular. Ver gráficos en Anexo 2.
La tendencia actual en Chile(5), en cargadores públicos, es usar para carga en corriente
alterna, conector Tipo 2, el cual es compatible con conectores Tipo 1 y Tipo 2,
considerando un cable para la carga pública que funciona como adaptador(6) y que es
propiedad del usuario final. En el caso de carga DC, la tendencia es disponer de cargadores
compatibles con multi estándar, CHAdeMO y Combinado Tipo 2 (CCS 2) .

5 Conectores Tipo 1 (16% de cargadores en AC públicos instalados) y Tipo 2 (78% de cargadores en AC públicos instalados) y
para carga en DC, se observa el uso de CHAdeMo (53 % de cargadores en DC instalados) y Combinado Tipo 2 (CCS 2) 47 % de
cargadores en DC instalados.
6 Ver foto en el anexo 3.

<!-- guia-buenas-practicas-em:p203 · pág. 203 -->
Recomendaciones
Para las estaciones de carga que se instalen en autopistas,
vías interurbanas o en general en el exterior con acceso
público
Para recarga de corta estadía (menos de una hora), es recomendable que sean para modos
de carga 3 o 4, por el mayor control de la carga. Así mismo se recomienda que la potencia
mínima sea 40 [kW], con comunicación a internet protocolo OCPP 1.5 o 1.6 (GPRS, Wifi),
con posibilidad de futura gestión de carga (disminución o aumento de potencia según
demanda) y que permita acceso universal, de fácil integración posterior.

Recomendaciones
Para los puntos de recarga en edificios de
estacionamiento, centros comerciales, supermercados,
cines, restaurantes.
Donde sea posible esperar mayor tiempo, se sugiere modos de carga 3, cargador en
corriente alterna, de potencia mayor a 11 [kW],con comunicación a internet protocolo
OCPP 1.5 o 1.6 (GPRS, Wifi), con conector Tipo 2, con posibilidad de futura gestión de carga
y que permita acceso universal, de fácil integración posterior.

Para recargas habituales en el hogar
Son recomendables los cargadores lentos, que permitan carga nocturna con potencias
menores a 7 [kW] monofásicas y trifásicas, ambas en modos de carga 2 y 3. Pueden ser
instalados en casas y/o estacionamientos de edificios de departamentos y donde el
tiempo disponible para la recarga sea de horas, con comunicación a internet protocolo
OCPP 1.5 o 1.6 (GPRS, Wifi), con posibilidad de futura gestión de carga y que permita
acceso universal, de fácil integración posterior.

<!-- guia-buenas-practicas-em:p205 · pág. 205 -->
Aspectos generales
Todos los cargadores mencionados independiente del modo de carga 2, 3 y 4 deben cumplir EMC (Compatibilidad
Electromagnética).
La disponibilidad de comunicación a internet en los cargadores de mayor potencia y especialmente
todos los de acceso público, es necesaria para generar la red de información a los usuarios tal que
puedan leer la disponibilidad y velocidad de carga de cada punto, en el futuro poder administrar
los peak de demanda de potencia, mantener la compatibilidad con la red de distribución y también
permitir que los usuarios accedan a ofertas de energía según disponibilidad.

Los empalmes para los cargadores deben cumplir la normativa vigente para instalaciones eléctricas,
tanto en seguridad, protecciones a personas e instalaciones y con la compatibilidad con la red
eléctrica, como el Factor de Potencia, THDi, THDv, perturbaciones y flicker (todas distorsiones a la
calidad del producto eléctrico de la red).

Los empalmes o circuitos deben ser exclusivos, cumplir con la Norma Eléctrica NCH Elec. 4/2003
vigente y mientras no exista la norma de instalación del cargador debe seguir las indicaciones del
fabricante e informar a la SEC(8) las características, tales como modo de carga, potencia, tipos de
conectores, forma de acceso, ubicación, interoperabilidad, etc.
La instalación eléctrica para los cargadores debe ser realizada e inscrita por los profesionales
autorizados y registrados en SEC, según potencia y nivel tensión de la instalación eléctrica
proyectada.

.

Los cargadores deben cumplir las normas de construcción y seguridad reconocidas
internacionalmente tales como ANSI (American National Standard Institute Inc.), IEEE (Institute of
Electrical and Electronic Engineers), NEMA (National Electrical Manufacturers Association), NEC
(National Electrical Code), NFPA (National Fire Protection Association), ASTM (American Society for
Testing and Materials), e IEC (International Electrotechnical Commission), entre otras.

8 http://www.sec.cl/portal/page?_pageid=33,5307707&_dad=portal&_schema=PORTAL

<!-- guia-buenas-practicas-em:p206 · pág. 206 -->
Anexo n.1
En el siguiente cuadro se resume los costos beneficios considerando solo variables de precio y costos de
operación sensibilizando por el kilometraje anual.
Item

Vehículo convencional

Vehículo eléctrico

Inversión

$ 11.690.000

$ 24.000.000

Permiso de circulación

$ 170.000

$ 589.200

Seguros

$ 480.000

$ 660.000

Kilometraje recorrido anual

40.000 KM

40.000 KM

Precio combustible

800 $/Litro

119,3 [$/kWh] BT1

Rendimiento

11 [km/L]

8,8 [km/kWh]

Gasto combustible

$ 3.009.174

$ 556.226

Cambios de aceite anual

$ 205.000

$0

Gasto operacional anual*

$ 3.864.174

$ 1.798.426

Para el caso presentado, donde la diferencia de inversión inicial es casi el doble, se logra una VAN positivo a los
40.000 km recorridos al año. El flujo se evaluó en el periodo de 8 años, tiempo de garantía de las baterías y una
tasa 7 %.
(*) Suma del permiso de circulación, seguro, mantenimiento y combustible anual.

Para el caso presentado, donde la diferencia de inversión inicial es casi el triple, se logra un VAN positivo a los
70.000 km recorridos al año. El flujo se evaluó en el periodo de 8 años, tiempo de garantía de las baterías y una
tasa 7 %.

Item

Vehículo convencional

Vehículo eléctrico

Inversión

$ 8.200.000

$ 24.000.000

Permiso de circulación

$ 166.000

$ 589.200

Seguros

$ 480.000

$ 660.000

Kilometraje recorrido anual

70.000 KM

70.000 KM

Precio combustible

800 $/Litro

119,3 [$/kWh] BT1

Rendimiento

11 [km/L]

8,8 [km/kWh]

Gasto combustible

$ 3.669.725

$ 678.324

Cambios de aceite anual

$ 205.000

$0

Gasto operacional anual*

$ 4.340.891

$ 1.920.524

Anexo n.2
Según la experiencia publicada por la de la
red de carga fastned de Holanda, se tiene el
siguiente cuadro, con el porcentaje de carga de
la batería a potencia máxima, permitida por los
fabricantes de vehículos.
Mayor información en https://fastned.nl/en/
how-it-works. Esta es una información útil para
estimar mejor el tiempo de carga, dependiendo
de la potencia disponible en el cargador, modo
de carga y tipo de vehículo.

Vehículo

Capacidad de almacenamiento de las baterías [kWh]
22-24-26

30-33-36

MMW

80%

65%

Hyundai IONIQ

80%

Nissan LEAF

25%

65%

OPEL Amera-e
Volkswagen

40-45

80%
50%

80%

80%

<!-- guia-buenas-practicas-em:p209 · pág. 209 -->
BMW i3
El BMW i3 se ha vendido con dos packs de baterías, de 22
kWh y 33 kWh respectivamente. Las celdas del pack de mayor
tamaño permiten una carga ligeramente más rápida, con peak
de 50 kW.

Tiempo de carga (en kw)

• 22 kWh: carga rápida hasta el 65%, después se ralentiza.
• 33 kWh: carga rápida hasta el 85%, después se ralentiza.

Batertía % (SoC)

Hyundai IONIQ Eléctrico

Tiempo de carga (en kw)

El Hyundai IONIQ Eléctrico tiene unas baterías de 28 kWh, puede
cargar hasta los 70 kW de potencia. En apenas 15/25 minutos,
puede recuperar 100 km de carga. La potencia de carga cae de
forma significativa por encima del 75% de carga.

Batertía % (SoC)

Nissan LEAF
La primera generación de Nissan LEAF estaba
disponible en dos versiones: 24 kWh y 30 kWh, siendo
el segundo pack mucho mejor de cara a la carga rápida.
Curiosamente, el Nissan LEAF de segunda generación,
de 40 kWh, tiene una capacidad de carga rápida
sorprendentemente baja, no superando en ningún
momento los 40 kW de potencia.

Tiempo de carga (en kw)

24 kWh: carga rápida hasta el 25%, después se ralentiza.
30 kWh: carga rápida hasta el 80%, después se ralentiza.
40 kWh: carga rápida hasta el 60%, después se ralentiza.

Batertía % (SoC)

Opel Ampera-e

Tiempo de carga (en kw)

El Opel Ampera-e (Chevrolet Bolt) está limitado a una potencia de carga
de 45 kW, en parte debido al sistema de control térmico de la batería. El
Ampera-e carga unos 100 km en 20-25 minutos, y tiene carga rápida hasta
el 55%. A partir del 70%, el vehículo pasa a cargarse muy lentamente.

Batertía % (SoC)

Volkswagen e-Golf
El Volkswagen e-Golf cuenta con baterías de 24,2 kWh
y 35,8 kWh y permiten cargas rápidas del 75% y 80 %
respectivamente.

Tiempo de carga (en kw)

24,2 kWh: carga rápida hasta el 75%, después se ralentiza.
35,8 kWh: carga rápida hasta el 80%, después se ralentiza.

Batertía % (SoC)

<!-- guia-buenas-practicas-em:p214 · pág. 214 -->
Anexo n.3
Clasificación de los cargadores de acuerdo a la potencia y su relación del tiempo de carga.
Esta definición pronto quedará obsoleta, por los cambios tecnológicos respecto de la
densidad de energía que puede acumular y la capacidad de recibir energía sin calentarse.
Cargador Lento: es un dispositivo de carga AC y se conecta de manera
indirecta a la baterías del Vehículo. La diferencia está en que la corriente
entregada por este cargador ronda los 12 a 16 amperes y la carga del
vehículo se completaría en unas 8 horas.
Cargador Rápido (EV Fast Charger): este tipo de cargador entrega
la energía directamente a las baterías del BEV pero lo hace en menos
tiempo. Esto lo logra al entregar la energía con una intensidad de
corriente mayor en ocho a diez veces comparándolo con un cargador
convencional. La característica principal de estos cargadores es el
poder el cargar el 80% de las baterías de un BEV en un rango de 15 a 20
minutos.
Cargador Ultra Rápido o de Alta Potencia (EV Ultra Fast Charger
o High Power Charger): tal como el cargador rápido, este cargador
entrega la energía directamente a las baterías del BEV. La principal
diferencia es que llegan a tener entre 3 a 4 veces mayor potencia que un
cargador rápido por lo que cargarán el 80% de las baterías de un BEV en
un rango de 6 a 8 minutos.
