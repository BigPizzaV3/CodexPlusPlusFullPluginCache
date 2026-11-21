# RIC N°09 – Sistemas de autogeneración

Fuente: REx 33.877 (30/12/2020), SEC — publicada en Diario Oficial 12/01/2021. Páginas 215–236 de bases1c.pdf.

<!-- ric09:preambulo · pág. 215 -->
DIVISIÓN DE INGENIERÍA DE ELECTRICIDAD

PLIEGO TÉCNICO NORMATIVO : RIC N°09

MATERIA : SISTEMAS DE AUTOGENERACIÓN.

FUENTE LEGAL : DECRETO CON FUERZA DE LEY N°4/20.018, DE
2006, DEL MINISTERIO DE ECONOMÍA,
```
FOMENTO    Y   RECONSTRUCCIÓN,      LEY
```
GENERAL DE SERVICIOS ELÉCTRICOS.

FUENTE REGLAMENTARIA : DECRETO N°8, DE 2019, DEL MINISTERIO DE
ENERGÍA, REGLAMENTO DE SEGURIDAD DE
LAS INSTALACIONES DE CONSUMO DE
ENERGÍA ELÉCTRICA.

DICTADO POR : RESOLUCIÓN EXENTA Nº 33.877, DE FECHA
30/12/2020, DE LA SUPERINTENDENCIA DE
ELECTRICIDAD Y COMBUSTIBLES.

<!-- ric09:1 · pág. 215 -->
1 OBJETIVOS

El objetivo del presente pliego técnico es establecer los requisitos de seguridad que deben cumplir los
sistemas de autogeneración en las instalaciones de consumo de energía eléctrica del país.

<!-- ric09:2 · pág. 215 -->
2 ALCANCE Y CAMPO DE APLICACIÓN

Las disposiciones de este pliego técnico son aplicables al diseño, ejecución, inspección y mantenimiento
y conexión de todas las instalaciones de consumo de energía eléctrica, en adelante e indistintamente,
instalaciones, que dispongan de sistemas de autogeneración que entregan la energía generada a la
instalación de consumo de forma simultánea a la suministrada por la empresa distribuidora y que no
inyectan esta energía a la red eléctrica de distribución.

No son aplicables las disposiciones de este pliego a las instalaciones a que se refiere el inciso sexto del
artículo 149° y el artículo 149° bis de la Ley General de Servicios Eléctricos.

<!-- ric09:3 · pág. 215 -->
3 REFERENCIAS NORMATIVAS

Las normas técnicas a las que se hace referencia a continuación son parte integrante del presente
pliego técnico y solo deben ser aplicadas en los puntos en los cuales son citadas.

```
3.1     IEC 60255-1                2009        Measuring relays and protection equipment –
```
Part 1: Common requirements.

Nota: Para la aplicación de este pliego técnico se podrá utilizar, en reemplazo de las normas IEC,
las normas equivalentes UNE, IEEE o UL.

<!-- ric09:4 · pág. 215 -->
4 TERMINOLOGÍA

<!-- ric09:4.1 · pág. 215 -->
4.1 Anti-isla: Sistema de protecciones que consiste en el uso de relés o controles, para evitar el
abastecimiento de consumos del sistema de distribución en forma aislada del resto del sistema
interconectado.

<!-- ric09:4.2 · pág. 215 -->
4.2 CA: Corriente Alterna

<!-- ric09:4.3 · pág. 215 -->
4.3 CC: Corriente Continua

<!-- ric09:4.4 · pág. 216 -->
4.4 Equipo de monitoreo de generación, destinado de manera exclusiva al sistema de generación.

<!-- ric09:4.5 · pág. 216 -->
4.5 Equipo de monitoreo de inyección, destinado de manera exclusiva al sistema de limitación de
inyecciones.

<!-- ric09:4.6 · pág. 216 -->
4.6 Interruptor de acoplamiento: Dispositivo de protección con capacidad de apertura bajo
corrientes de carga y de cortocircuito, cuya función es desconectar el o los equipos de generación
del sistema de distribución. Posee dos dispositivos eléctricos de desconexión conectados en serie
(con redundancia).

<!-- ric09:4.7 · pág. 216 -->
4.7 Inversor: Convertidor de tensión y corriente continua en tensión y corriente alterna.

<!-- ric09:4.8 · pág. 216 -->
4.8 Isla: Condición provocada cuando se ha producido un corte de energía en la red eléctrica
suministrada por la empresa distribuidora y esta área de la red que ha quedado aislada,
permanece eléctricamente separada del resto de la red eléctrica, quedando energizada
solamente por el o los equipamientos de generación.

<!-- ric09:4.9 · pág. 216 -->
4.9 Isla interna: Condición provocada cuando se ha producido un corte de energía en la red eléctrica
suministrada por la empresa distribuidora y la instalación interior de consumo del usuario queda
aislada del resto del sistema de distribución, quedando ella energizada por el o los equipamientos
de autogeneración.

<!-- ric09:4.10 · pág. 216 -->
4.10 Norma técnica de conexión y operación de equipamiento de generación (NT NETBILLING):
Norma técnica que establece los procedimientos, metodologías y demás exigencias para la
conexión y operación de equipamientos de generación

<!-- ric09:4.11 · pág. 216 -->
4.11 NTD: Norma técnica de calidad de servicio para sistemas de distribución.

<!-- ric09:4.12 · pág. 216 -->
4.12 Operación en paralelo: Condición en que, operan el sistema de generación de algún productor
independiente y el sistema de distribución eléctrica, de forma que exista la posibilidad de transferir
energía eléctrica a la instalación de consumo por medio de la red de distribución eléctrica y el
sistema de autogeneración de manera simultánea o bien independiente.

<!-- ric09:4.13 · pág. 216 -->
4.13 Potencia nominal del generador: Suma de las potencias máximas de las unidades
generadoras.

<!-- ric09:4.14 · pág. 216 -->
4.14 Protección de potencia inversa: Es el elemento de protección que funciona sobre un valor
deseado de potencia en una dirección dada o sobre la inversión de potencia.

<!-- ric09:4.15 · pág. 216 -->
4.15 Protección de red e instalación (RI): Protección que actúa sobre el interruptor de acoplamiento
cuando al menos un valor de operación del sistema de distribución se encuentra fuera del rango
de ajuste de esta protección. Esta protección puede estar integrada en el inversor o ser externa
al inversor.

<!-- ric09:4.16 · pág. 216 -->
4.16 Red de baja tensión: Red cuya tensión nominal es igual o inferior a 1000 V.

<!-- ric09:4.17 · pág. 216 -->
4.17 Sistemas de autogeneración: Sistema de generación de energía eléctrica destinado a
suministrar el consumo local del recinto donde el equipamiento se encuentra ubicado bajo la
tuición y responsabilidad de su dueño o usuario, con independencia o con posibilidad de
funcionamiento en paralelo con la red de distribución.

<!-- ric09:4.18 · pág. 216 -->
4.18 Sistema de control de inyección cero: Es un sistema de control dinámico de potencia,
conformado por dispositivos eléctricos y/o electrónicos que impiden la inyección de potencia a la
red pública a través de la modulación de la generación para corregir la diferencia entre la potencia
generada y la potencia consumida en la instalación.

<!-- ric09:4.19 · pág. 216 -->
4.19 Sistemas de transferencia abierta: Estado de operación en el cual el traspaso de consumos
desde la red de distribución pública al sistema de generación se realiza sin interconexión eléctrica
entre ambos sistemas.

<!-- ric09:4.20 · pág. 216 -->
4.20 Sistemas de transferencia cerrada: Estado de operación en el cual el sistema de generación y
la red de distribución pública permanecen interconectados en sincronismo, en forma momentánea
o permanente.

<!-- ric09:5 · pág. 217 -->
5 DISPOSICIONES GENERALES

<!-- ric09:5.1 · pág. 217 -->
5.1 Todo sistema de autogeneración deberá ejecutarse de acuerdo con un proyecto técnicamente
concebido, el cual deberá asegurar que la instalación no presenta riesgos para los operadores o
usuarios y cosas, sea eficiente, proporcione un buen servicio, permita un fácil y adecuado
mantenimiento y tenga la flexibilidad necesaria como para permitir modificaciones o ampliaciones
con facilidad.

<!-- ric09:5.2 · pág. 217 -->
5.2 La potencia máxima de los sistemas de autogeneración no podrá ser superior a la capacidad del
empalme eléctrico de la instalación de consumo.

<!-- ric09:5.3 · pág. 217 -->
5.3 La instalación de los equipos y componentes que forman parte del sistema de autogeneración
debe facilitar el mantenimiento seguro y efectuarse de acuerdo con las recomendaciones del
fabricante del equipo.

<!-- ric09:5.4 · pág. 217 -->
5.4 El funcionamiento de las instalaciones de un sistema de autogeneración no deberá provocar
averías en la red, disminuciones de las condiciones de seguridad y de calidad, ni alteraciones
superiores a las admitidas por la normativa vigente.

<!-- ric09:5.5 · pág. 217 -->
5.5 En caso que la línea de distribución quede sin energía o la acometida del empalme del cliente
quede desconectada de la red de distribución, ya sea por trabajos de mantenimiento requeridos
por la empresa distribuidora o por haber actuado alguna protección de la línea o del empalme del
cliente, las instalaciones eléctricas de un sistema de autogeneración no deberán mantener
tensión en la línea de distribución, ni dar origen a condiciones peligrosas de trabajo para el
personal de mantenimiento y explotación de la red de distribución.

<!-- ric09:5.6 · pág. 217 -->
5.6 Todo sistema de autogeneración con capacidad de funcionamiento en paralelo con la red de
distribución, previo a su ejecución deberá solicitar el informe de condiciones previas o factibilidad
técnica de suministro ante la empresa distribuidora, definida en el artículo 5-3 de la NTD,
acompañando todos los antecedentes técnicos y las características principales del sistema de
autogeneración que le permitan dar respuesta a dicha solicitud, en conformidad con lo definido
en el artículo 15 del DS N°8/2019 del Ministerio de Energía.

Los estudios para la factibilidad técnica o informe de condiciones previas del sistema de
autogeneración deberán cumplir con lo definido en el artículo 5-3 punto 1.9 de la NTD.

<!-- ric09:5.7 · pág. 217 -->
5.7 Todo sistema de autogeneración, previo a su puesta en servicio, deberá ser declarado mediante
una comunicación de energización ante la Superintendencia, adjuntando la factibilidad técnica o
informe de condiciones previas establecido en la NTD, los resultados de los estudios en caso de
que se requieran, y los datos técnicos del sistema de autogeneración.

<!-- ric09:5.8 · pág. 217 -->
5.8 La Superintendencia establecerá el procedimiento de comunicación de energización de las
instalaciones de autogeneración a través de una instrucción técnica de carácter general.

<!-- ric09:5.9 · pág. 217 -->
5.9 Toda instalación eléctrica de un sistema de autogeneración que se conecte a la red debe ser
proyectada y ejecutada bajo la supervisión directa de un instalador eléctrico autorizado por la
Superintendencia, clase A o B, según corresponda en función de las competencias establecidas
por su licencia.

<!-- ric09:5.10 · pág. 217 -->
5.10 Una vez inscrita la comunicación de energización de la instalación ante la Superintendencia, el
interesado deberá notificar la entrada en operación a la empresa distribuidora, adjuntado todos
los antecedentes técnicos del proyecto. Las empresas distribuidoras deberán mantener un
registro con todos los sistemas de autogeneración conectados a sus redes de distribución.

<!-- ric09:5.11 · pág. 217 -->
5.11 Durante todo el período de operación del sistema de autogeneración, sus propietarios u
operadores deberán conservar los diferentes estudios y documentos técnicos utilizados en el
diseño y construcción de las instalaciones y sus modificaciones, como asimismo los registros de
las auditorías, certificaciones e inspecciones de que hubiera sido objeto, todo lo cual deberá estar
a disposición de la Superintendencia en caso de que esta lo solicite.

<!-- ric09:5.12 · pág. 217 -->
5.12 Todo sistema de autogeneración deberá cumplir con el sistema de protecciones de interconexión
definidos en la sección 6 de este pliego, el cual podrá ser auditado en cualquier etapa del proyecto
o en su operación por la empresa distribuidora, con el objetivo de salvaguardar la seguridad de
la red de distribución.

<!-- ric09:5.13 · pág. 218 -->
5.13 Los sistemas de autogeneración aislados de la red de distribución deberán ser diseñados y
declarados de acuerdo con la instrucción técnica de carácter general que imparta la
Superintendencia y no les serán aplicables las disposiciones técnicas de este pliego.

<!-- ric09:5.14 · pág. 218 -->
5.14 Los equipos de generación que cuenten con sistemas de transferencia cerrada deberán cumplir
con las disposiciones de este pliego técnico, en cambio a los equipos de generación con
transferencia abierta no les serán aplicables las disposiciones técnicas de este pliego.

<!-- ric09:5.15 · pág. 218 -->
5.15 Los sistemas de almacenamiento asociados a los sistemas de autogeneración deberán ser
diseñados de acuerdo con la instrucción técnica de carácter general que imparta la
Superintendencia para tales efectos.

<!-- ric09:5.16 · pág. 218 -->
5.16 De acuerdo con lo establecido en la Ley Nº 18.410, cualquier duda en cuanto a la interpretación
de las disposiciones de este pliego técnico será resuelta por la Superintendencia.

<!-- ric09:5.17 · pág. 218 -->
5.17 En materias de diseño, construcción, operación, mantenimiento, reparación, modificación,
inspección y término de operación, la Superintendencia podrá permitir el uso de tecnologías
diferentes a las establecidas en el presente pliego técnico, siempre que se mantenga el nivel de
seguridad que el texto normativo contempla. Estas tecnologías deberán estar técnicamente
respaldadas en normas, códigos o especificaciones nacionales o extranjeras, así como en
prácticas recomendadas de ingeniería internacionalmente reconocidas, o bien ser parte de
instalaciones de prueba para nueva tecnología. Para ello el instalador deberá presentar el
proyecto y un ejemplar completo de la versión vigente de la norma, código o especificación
extranjera utilizada debidamente traducida, cuando corresponda, así como cualquier otro
antecedente que solicite la Superintendencia.

<!-- ric09:5.18 · pág. 218 -->
5.18 En los casos en que la empresa distribuidora detecte a un usuario que posea un sistema de
autogeneración irregular, que no cumpla con la normativa vigente, la distribuidora deberá
proceder de la siguiente forma:

<!-- ric09:5.18.1 · pág. 218 -->
5.18.1 Notificará al usuario en forma inmediata, con copia a la Superintendencia, indicándole
que debe dejar de operar dicho sistema y le informará que debe proceder con la
normalización de sus instalaciones a través de un instalador autorizado por la
Superintendencia en un plazo no superior a 60 días hábiles.

<!-- ric09:5.18.2 · pág. 218 -->
5.18.2 En el caso que el usuario cuente con un medidor electromecánico o un medidor
unidireccional, se deberá cambiar el medidor en forma inmediata a un medidor
bidireccional cumpliendo con las exigencias de la sección 8 de este pliego, para
salvaguardar la correcta medición de los consumos ya que el equipo de medida al
funcionar en sentido contrario pierde su exactitud en la medición y también tiene el
objetivo de auditar que no existan inyecciones a la red de distribución que pongan en
peligro la operación de la red.

<!-- ric09:5.18.3 · pág. 218 -->
5.18.3 En el caso que la empresa distribuidora detecte que el sistema de autogeneración
irregular inyecta energía cuando la red o empalme del cliente queda sin suministro, la
empresa deberá cortar en forma inmediata el suministro de energía de esta instalación y
notificar a la Superintendencia, aportando los antecedentes que acrediten el hecho.

<!-- ric09:5.18.4 · pág. 218 -->
5.18.4 En el caso de que transcurrido el plazo indicado en el punto 5.18.1 el usuario no hubiese
normalizado su instalación o no hubiese acordado con la empresa distribuidora un nuevo
plazo para normalizar, la empresa deberá denunciar esto a la Superintendencia, para lo
cual deberá aportar todos los antecedentes, tales como el registro de consumo e
inyecciones de energía, imágenes del sistema instalado y copia de la notificación enviada
al usuario y todos los antecedentes que permitan acreditar la denuncia ante la
Superintendencia, enviando una copia de la denuncia al usuario.

<!-- ric09:5.18.5 · pág. 218 -->
5.18.5 En los casos en que la empresa distribuidora detecte que el medidor bidireccional registra
inyecciones después de la notificación de no operar su sistema de autogeneración, la
empresa deberá denunciar esto a la Superintendencia en forma inmediata adjuntado
todos los antecedentes del caso. La empresa también deberá notificar al usuario
adjuntado la denuncia presentada ante la Superintendencia, y en la carta también deberá
volver a indicarle que no puede operar su sistema, y que en el caso de hacerlo
nuevamente procederá con el corte de su suministro.

<!-- ric09:5.18.6 · pág. 219 -->
5.18.6 En los casos en que el usuario no acate las instrucciones de no operar el sistema de
autogeneración irregular indicado en los puntos 5.18.3 y 5.18.5 y la empresa distribuidora
detecte por tercera vez inyecciones a la red de distribución, deberá denunciar por escrito
este hecho a la Superintendencia con copia al usuario, informando la fecha en que
procederá con el corte de suministro. Una vez que se haya enviado la carta a la
Superintendencia con copia al usuario, se deberá proceder con el corte o la suspensión
del suministro, hasta que dicha instalación sea regularizada.

<!-- ric09:5.18.7 · pág. 219 -->
5.18.7 Los sistemas de autogeneración irregulares podrán acreditar su normalización ante la
empresa distribuidora presentando un nuevo certificado de inscripción de la comunicación
de energización de la instalación emitido por la Superintendencia. La empresa
distribuidora deberá reponer el suministro dentro de las 24 horas siguientes a los clientes
que presenten este certificado ante ella.

<!-- ric09:6 · pág. 219 -->
6 EXIGENCIAS PARA LA CONEXIÓN A LA RED

<!-- ric09:6.1 · pág. 219 -->
6.1 En las instalaciones de sistemas de autogeneración, los equipos de protección medirán la tensión
y la corriente de cada fase y desconectarán el sistema de autogeneración ante fluctuaciones en
la corriente o la tensión de cualquier fase, en cumplimiento de la normativa nacional vigente. En
el caso de que las instalaciones del cliente tengan múltiples sistemas de autogeneración, los
equipos de protección deberán desconectar todos los sistemas de autogeneración ante
fluctuaciones en la tensión o la corriente de cualquier fase. Para una comprensión simplificada
acerca de los requisitos para los diferentes sistemas de autogeneración ver el anexo 9.1.

<!-- ric09:6.2 · pág. 219 -->
6.2 Los sistemas de autogeneración que funcionen en paralelo con la red deberán contar con las
siguientes funciones de protección:

<!-- ric09:6.2.1 · pág. 219 -->
6.2.1 Protección por sobre corriente de fases.

<!-- ric09:6.2.2 · pág. 219 -->
6.2.2 Protección por falla a tierra.

<!-- ric09:6.2.3 · pág. 219 -->
6.2.3 Protección de red e instalación (RI), que deberá contar con las siguientes funciones:

<!-- ric09:6.2.3.1 · pág. 219 -->
6.2.3.1 Funciones de protección por sobre y baja tensión (Nema 59/ Nema 27).

<!-- ric09:6.2.3.2 · pág. 219 -->
6.2.3.2 Funciones de protección por sobre y baja frecuencia (Nema 81O/ Nema 81U).

<!-- ric09:6.2.3.3 · pág. 219 -->
6.2.3.3 Función de protección anti-Isla.

<!-- ric09:6.2.4 · pág. 219 -->
6.2.4 Protección de potencia inversa: Corresponde al relé (Nema 32) con ajuste de pick up por
potencia activa.

<!-- ric09:6.2.5 · pág. 219 -->
6.2.5 Sistema de control de inyección cero.

<!-- ric09:6.3 · pág. 219 -->
6.3 Protección por sobre corriente de fases.

<!-- ric09:6.3.1 · pág. 219 -->
6.3.1 La protección por sobre corriente de fases podrá estar contenida en un interruptor
termomagnético de corte omnipolar, de una capacidad adecuada para la potencia del
sistema de autogeneración. El interruptor magnetotérmico será bipolar, para el caso de
las instalaciones monofásicas o tetrapolar para el caso de las instalaciones trifásicas, con
una corriente de cortocircuito superior a la indicada por la empresa distribuidora en el
punto de conexión.

<!-- ric09:6.4 · pág. 219 -->
6.4 Protección por falla a tierra.

<!-- ric09:6.4.1 · pág. 219 -->
6.4.1 La protección por falla a tierra podrá estar contenida en un interruptor diferencial o en un
bloque diferencial como parte del interruptor termomagnético indicado en el punto
anterior. El diferencial deberá ser del tipo A o B y su corriente diferencial no será superior
a 30 mA para unidades de generación para potencia instalada inferiores a 10 kW,
mientras que para unidades de generación igual o superior a 10 kW su corriente
diferencial no será superior a 300 mA.

<!-- ric09:6.4.2 · pág. 220 -->
6.4.2 La protección por falla a tierra indicada en el punto 6.2.2, podrá ser del tipo electrónico
asociado a toroide y contactor o interruptor desconectador, debiendo cumplir con lo
siguiente:

<!-- ric09:6.4.2.1 · pág. 220 -->
6.4.2.1 El contactor, en caso de falla deberá cortar todos los conductores activos en
forma automática, deberá emplear la categoría de utilización AC-1 y será
protegido ante sobrecargas y cortocircuitos.

<!-- ric09:6.4.2.2 · pág. 220 -->
6.4.2.2 La sección del transformador toroidal deberá ser dimensionada para circundar
el cableado de alimentación y neutro juntos. Su medición de corriente y su
relación de transformación deben ser iguales o mayores a la corriente nominal
del punto de la instalación que se está midiendo.

<!-- ric09:6.4.2.3 · pág. 220 -->
6.4.2.3 Debe regularse su tiempo de operación como mínimo en 20 ms y su corriente
nominal debe ser igual o mayor a la corriente nominal de la protección
termomagnética aguas arriba.

<!-- ric09:6.4.2.4 · pág. 220 -->
6.4.2.4 Debe ser de tipo A o B y su corriente diferencial no será superior a 30 mA para
unidades de generación para potencia instalada inferiores a 10 kW, mientras
que para unidades de generación igual o superior a 10 kW su corriente
diferencial no será superior a 300 mA.

<!-- ric09:6.5 · pág. 220 -->
6.5 Protección de red e instalación (RI)

<!-- ric09:6.5.1 · pág. 220 -->
6.5.1 La protección RI actúa sobre el interruptor de acoplamiento para la desconexión del
equipo de generación de la red, cuando se presentan valores inadmisibles de las
tensiones o la frecuencia. Esta protección no será exigible para grupos electrógenos.

<!-- ric09:6.5.2 · pág. 220 -->
6.5.2 La instalación de la protección RI indicada en el punto 6.2.3 precedente será de manera
centralizada y/o complementaria como se indica a continuación:

<!-- ric09:6.5.2.1 · pág. 220 -->
6.5.2.1 La protección RI centralizada deberá medir o censar sobre el alimentador
principal de la instalación de consumo, estará ubicada en un gabinete especial
llamado tablero de punto de conexión, el cual podrá albergar al interruptor de
acoplamiento, a la protección de potencia inversa y al sistema de control de
inyección cero, según corresponda, de tal forma que pueda ser sellado por la
empresa distribuidora.

<!-- ric09:6.5.2.2 · pág. 220 -->
6.5.2.2 La protección RI centralizada debe ser ubicada junto a la caja de empalme de
la instalación de consumo, y en caso de que esto no sea posible, se podrá
ubicar en el tablero de punto de conexión junto al tablero general de la
instalación. Esta protección actuará sobre el interruptor de acoplamiento.

<!-- ric09:6.5.2.3 · pág. 220 -->
6.5.2.3 La protección RI centralizada será obligatoria para todas las instalaciones de
generación cuya capacidad instalada supere los 100 kW de potencia. Ver Anexo
9.2

<!-- ric09:6.5.2.4 · pág. 220 -->
6.5.2.4 La protección RI complementaria estará ubicada en el lugar más próximo al
equipo de generación o en el tablero en que se conecta el equipo de generación
a la instalación de consumo. Esta protección podrá estar integrada al inversor
o al equipo de autogeneración o ser externa a él. Esta protección actuará sobre
el interruptor de acoplamiento. Ver anexo 9.2

<!-- ric09:6.5.2.5 · pág. 220 -->
6.5.2.5 La protección RI complementaria será obligatoria para todas las instalaciones
de generación cuya capacidad instalada sea igual o inferior a 100 kW. Ver
anexos 9.3 y 9.4

<!-- ric09:6.5.2.6 · pág. 220 -->
6.5.2.6 Independiente de la exigencia de la RI centralizada, en los casos que el equipo
de autogeneración cuente con una RI complementaria, ésta siempre deberá
estar activada.

<!-- ric09:6.5.3 · pág. 220 -->
6.5.3 La protección RI se configurará de acuerdo con los parámetros definidos en la norma
técnica de conexión y operación de equipamiento de generación (NTCO-EG) o en las
disposiciones que la reemplacen.

<!-- ric09:6.5.4 · pág. 221 -->
6.5.4 La protección RI centralizada debe incorporar un botón de prueba que permita verificar el
correcto funcionamiento del circuito entre la protección RI y el interruptor de
acoplamiento. Para este fin, al presionar el botón de prueba debe ser posible visualizar
la activación del interruptor de acoplamiento.

<!-- ric09:6.5.5 · pág. 221 -->
6.5.5 En la protección RI centralizada debe ser posible leer la información independientemente
de las condiciones de operación del equipamiento de generación, y sin necesidad de
medios auxiliares. En la protección RI integrada se permite que la información sea
obtenida a través de una interfaz de comunicación.

<!-- ric09:6.5.6 · pág. 221 -->
6.5.6 Protección anti-Isla

<!-- ric09:6.5.6.1 · pág. 221 -->
6.5.6.1 El sistema de generación deberá contar con una protección anti-isla, necesaria
para evitar que éste energice un circuito que se encuentre aislado del sistema
interconectado. De surgir una situación de isla eléctrica, el sistema de
generación deberá desconectarse del sistema de distribución en un tiempo
máximo de dos segundos. Esta protección deberá ser del tipo ROCOF, Vector
Shift, u otro de características a lo menos equivalentes o superior.

<!-- ric09:6.5.7 · pág. 221 -->
6.5.7 Interruptor de acoplamiento

<!-- ric09:6.5.7.1 · pág. 221 -->
6.5.7.1 Para la conexión de un equipo de generación a la red de distribución se deberá
emplear un interruptor de acoplamiento. El cual será comandado por la
protección de red e instalación (Protección RI centralizada o complementaria) y
se disparará automáticamente cuando opere al menos una función de
protección.

<!-- ric09:6.5.7.2 · pág. 221 -->
6.5.7.2 Al igual que la protección RI, la protección de potencia inversa también podrá
operar sobre este interruptor de acoplamiento, siempre que las condiciones
técnicas de los equipos lo permitan y siempre que el interruptor de acoplamiento
se ubique según lo definido en el punto 6.5.2, de no cumplirse con esta
condición la protección de potencia inversa no podrá operar sobre este
interruptor.

<!-- ric09:6.5.7.3 · pág. 221 -->
6.5.7.3 El interruptor de acoplamiento conecta el equipo de generación con el resto de
las instalaciones del cliente o usuario final.

<!-- ric09:6.5.7.4 · pág. 221 -->
6.5.7.4 La instalación del interruptor de acoplamiento indicado en el punto 6.5.7.1 podrá
ubicarse en:

<!-- ric09:6.5.7.4.1 · pág. 221 -->
6.5.7.4.1 El tablero de punto de conexión donde se ubica la protección RI
centralizada o en el tablero más próximo al equipo de generación o
en el lugar definido en el punto 6.5.2.

<!-- ric09:6.5.7.4.2 · pág. 221 -->
6.5.7.4.2 El tablero más próximo al equipo de generación, pudiendo estar
integrado al inversor o al equipo de autogeneración y deberá ser
comandado por la protección RI complementaria y/o la protección RI
centralizada.

<!-- ric09:6.5.7.5 · pág. 221 -->
6.5.7.5 El tiempo máximo de desconexión desde ocurrida una falla no debe superar los
200 ms. El tiempo de desconexión del interruptor debe indicarse en los
documentos del fabricante.

<!-- ric09:6.5.7.6 · pág. 221 -->
6.5.7.6 El interruptor de acoplamiento debe ejecutarse como dos elementos de
interrupción galvánicas en serie (ej: relés, interruptor protector de motor,
interruptor de corriente mecánico) y debe cumplir el criterio N-1. La capacidad
de apertura de ambos interruptores que forman el interruptor de acoplamiento
deberá ser dimensionada en concordancia con la máxima contribución de
corriente de corto circuito proveniente del sistema de distribución o del
equipamiento de generación. En este último caso, se deberá garantizar la
desconexión de todos los polos

<!-- ric09:6.5.7.7 · pág. 221 -->
6.5.7.7 En el caso en que el interruptor de acoplamiento se ubique en un lugar distinto
a la protección RI, ésta deberá actuar sobre el interruptor de acoplamiento
mediante un sistema de disparo transferido. Para este caso la protección de
flujo inverso no podrá operar sobre este interruptor y deberá operar sobre su
propio interruptor cumpliendo con el punto 6.6.2. Ver anexo 9.2.

<!-- ric09:6.5.7.8 · pág. 222 -->
6.5.7.8 El sistema de disparo transferido deberá cumplir con las siguientes
características mínimas:

<!-- ric09:6.5.7.8.1 · pág. 222 -->
6.5.7.8.1 En caso de falla del enlace para la transferencia del disparo, el
interruptor de acoplamiento deberá desacoplar al equipamiento de
generación inmediatamente.

<!-- ric09:6.5.7.8.2 · pág. 222 -->
6.5.7.8.2 Se deberá tomar resguardo contra interferencias que puedan afectar
al sistema de disparo transferido.

<!-- ric09:6.5.7.8.3 · pág. 222 -->
6.5.7.8.3 En caso de presencia de grupos de emergencia, se deberá tomar
los resguardos necesarios para evitar el paralelismo no intencional
entre éstos y el o los equipamientos de generación.

<!-- ric09:6.5.7.8.4 · pág. 222 -->
6.5.7.8.4 Se deberá habilitar también las protecciones RI e interruptores de
acoplamiento en los equipamientos de generación.

<!-- ric09:6.5.7.8.5 · pág. 222 -->
6.5.7.8.5 La pérdida de la tensión auxiliar de la protección RI centralizada o
del control de la protección RI integrada debe llevar a la apertura
inmediata del interruptor de acoplamiento.

<!-- ric09:6.6 · pág. 222 -->
6.6 Protección de potencia inversa

<!-- ric09:6.6.1 · pág. 222 -->
6.6.1 La función de protección de potencia inversa (Nema 32) deberá actuar sobre un contactor
de poder o sobre el interruptor de acoplamiento, o sobre el reconectador, el cual será el
encargado de interrumpir la inyección de energía hacia la red en caso de que el nivel de
generación sea superior al consumo. El contactor o interruptor debe ser capaz de
interrumpir el suministro completo de dicha instalación o solo la generación, lo que
dependerá del punto de conexión del sistema de autogeneración. Sobre este interruptor
también podrá operar la protección RI centralizada, siempre que sea factible
técnicamente por los equipos que se utilicen en la instalación.

<!-- ric09:6.6.2 · pág. 222 -->
6.6.2 La protección de potencia inversa y el contactor de poder o el interruptor de acoplamiento
o reconectador indicado en el punto 6.6.1 anterior, deberá instalarse en el punto de
conexión del cliente y formar parte del empalme de la instalación de consumo, pudiendo
instalarse en la caja del empalme o en el tablero de punto de conexión adosado a la caja
de empalme, el cual deberá ser sellado por la empresa distribuidora.

<!-- ric09:6.6.3 · pág. 222 -->
6.6.3 La protección de potencia inversa deberá operar cuando se superen los valores definidos
en el punto 6.6.7, por lo cual su operación tendrá las siguientes acciones:

<!-- ric09:6.6.3.1 · pág. 222 -->
6.6.3.1 La operación de la protección de potencia inversa cortará sólo el suministro del
sistema de autogeneración cuando éste se conecta directamente al contactor
de poder o al interruptor de acoplamiento o al reconectador indicado en el punto
6.6.1 y la unión del equipo de generación se realiza en la caja de empalme o en
el tablero de punto de conexión indicado en el punto 6.5.2. Ver anexos 9.2
Opción A y B, 9.4 Opción A.

<!-- ric09:6.6.3.2 · pág. 222 -->
6.6.3.2 La operación de la protección de potencia inversa cortará el suministro de toda
la instalación de consumo cuando el punto de conexión del sistema de
autogeneración se efectúa en el interior de la instalación de consumo. Ver
anexos 9.2 Opción C y D, 9.4 Opción B.

<!-- ric09:6.6.4 · pág. 222 -->
6.6.4 La protección de potencia inversa exigido en el punto 6.2.4 de este pliego técnico deberá
ser del tipo de regulación de potencia activa.

<!-- ric09:6.6.5 · pág. 222 -->
6.6.5 Los relés de potencia inversa deberán cumplir con la norma IEC 60255-1 “Measuring
relays and protection equipment” o equivalentes UE, IEEE.

<!-- ric09:6.6.6 · pág. 222 -->
6.6.6 Para proyectos de autoconsumo donde la potencia instalada de generación sea superior
a 100 kW, el relé de potencia inversa será del tipo microprocesado.

<!-- ric09:6.6.7 · pág. 223 -->
6.6.7 La regulación para la función del relé de potencia inversa (Nema 32) exigido en el punto
6.2.4 de este pliego técnico será la siguiente:

```
Potencia instalada de        Tiempo de operación relé       Ajuste de Operación
    generación                         32                          (Pickup)
      ≤300kW                           10s                2% de la potencia nominal
                                                              de la unidad o del
 >300kW y ≤1500kW                       5s                  conjunto de unidades
                                                             generadoras de un
                                                                  sistema de
        >1500kW                         2s                     autogeneración
```

<!-- ric09:6.6.8 · pág. 223 -->
6.6.8 Se eximirán de la protección inversa requerida en el punto 6.2.4, aquellos sistemas de
autogeneración que cuenten con un sistema de inyección cero de potencia a la red y que
cumplan con una de las siguientes condiciones:

<!-- ric09:6.6.8.1 · pág. 223 -->
6.6.8.1 Que el o los equipos de generación tengan una potencia máxima menor o igual
a 300 kW y que su potencia de generación no supere el 10% de la capacidad
del empalme de la instalación de consumo. Ver Anexo 9.3.

<!-- ric09:6.6.8.2 · pág. 223 -->
6.6.8.2 Que en instalaciones domiciliarias con empalmes en baja tensión de hasta 10
kW, el o los equipos de generación tengan una potencia de generación que no
supere el 30% de la capacidad del empalme de la instalación de consumo. Ver
Anexo 9.3.

<!-- ric09:6.7 · pág. 223 -->
6.7 Sistema de control de inyección cero

<!-- ric09:6.7.1 · pág. 223 -->
6.7.1 Todos los sistemas de autogeneración conectados en paralelo con la red de distribución
que utilicen convertidores estáticos deberán contar con un sistema de control de
inyección cero, el que deberá controlar y evitar la inyección de energía generada hacia
las redes de distribución y prevenir la operación de la protección de potencia inversa
indicada en el punto 6.2.4.

<!-- ric09:6.7.2 · pág. 223 -->
6.7.2 Todos los sistemas de control de inyección cero que formen parte de un sistema de
autogeneración deberán estar autorizados por la Superintendencia para tales efectos. Si
el sistema de autogeneración con control de inyección cero está constituido por más de
un inversor o convertidor estático, la comunicación entre ellos debe realizarse de forma
alámbrica, con RS485, ethernet o equivalente dispuesto por el fabricante. El sistema de
comunicación elegido e implementado debe utilizar un cableado de largo efectivo menor
a lo que el protocolo y fabricante recomiendan para garantizar buen desempeño. Ver
anexo N°9.5

<!-- ric09:6.7.3 · pág. 223 -->
6.7.3 El máximo tiempo de actuación del sistema de control de inyección cero, en reducir y
evitar una inyección de potencia a la red será de 5 segundos y sus ajustes de operación
no deben exceder el 2% de la potencia nominal del autogenerador. Para instalaciones
con potencia instalada de generación superiores a 1500 kW, este tiempo operación no
deberá exceder de 2 segundos.

<!-- ric09:6.7.4 · pág. 223 -->
6.7.4 La comunicación entre los inversores, equipos de generación, equipos de monitoreo de
inyección u otros dispositivos utilizados en el sistema de control de inyección cero debe
operar en señales en una ventana de 1 segundo.

<!-- ric09:6.7.5 · pág. 223 -->
6.7.5 En caso de que cualquiera de los componentes sistema de control de inyección cero,
falle, pierda su comunicación, señal o su fuente de alimentación, el sistema deberá reducir
la potencia a un valor igual a cero en una ventana de 5 segundos.

<!-- ric09:6.7.6 · pág. 223 -->
6.7.6 El sistema de control de inyección cero deberá actuar sobre los inversores o equipos de
autogeneración.

<!-- ric09:6.7.7 · pág. 223 -->
6.7.7 Para los casos indicados en el punto 6.6.8 donde el equipo de generación no cuente con
la protección de potencia inversa, el sistema de control de inyección cero deberá estar
ubicado en el tablero de punto de conexión, el cual deberá ser sellado por la empresa de
distribución, ubicado al costado del empalme o lo más cercano posible a él. Ver anexo
N°9.3.

<!-- ric09:7 · pág. 224 -->
7 EXIGENCIAS DE DISEÑO DEL EQUIPO DE GENERACIÓN

<!-- ric09:7.1 · pág. 224 -->
7.1 Todas aquellas materias relativas al diseño, construcción, mantenimiento, reparación,
modificación e inspección, fabricación, ensayos e instalación de equipos, materiales y accesorios
de unidades de generación, se establecerán en conformidad a las instrucciones técnicas de
carácter general que emita la Superintendencia para tales efectos.

En ausencia de éstas podrán aplicarse las instrucciones técnicas normativas definidas bajo las
disposiciones establecidas en el artículo 149 bis y siguientes de la Ley General de Servicios
Eléctricos (DFL Nª4/2006) o las normas extranjeras, internacionalmente reconocidas, emitidas
por las organizaciones que a continuación se indican: International Electrotechnical Commission
(IEC), International Organization for Standardization (ISO), Normas DIN/VDE y American Society
of Testing Materials/American National Standards Institute (ASTM/ANSI), Institute of Electrical
and Electronics Engineers (IEEE), National Fire Protection Association (NFPA). En todo caso, la
aplicación de estas normas deberá ser aprobada por la Superintendencia, a requerimiento
expreso del solicitante.

<!-- ric09:7.2 · pág. 224 -->
7.2 Los equipos que formen parte de un sistema de autogeneración deberán cumplir con lo definido
en el protocolo de análisis y/o ensayos de productos eléctricos respectivo, establecido por la
Superintendencia. En ausencia de estos los equipos que formen parte de un sistema de
autogeneración deberán contar con una autorización previa de la Superintendencia para ser
utilizados en instalaciones de consumo. La Superintendencia será la encargada de emitir el
procedimiento de autorización.

<!-- ric09:7.3 · pág. 224 -->
7.3 Los sistemas de autogeneración que utilicen sistemas de almacenamiento se deben marcar con
la tensión máxima de operación, incluyendo cualquier tensión de ecualización y la polaridad del
conductor del circuito puesto a tierra.

<!-- ric09:7.4 · pág. 224 -->
7.4 Se debe considerar la contribución de las corrientes de falla, de todas las fuentes de energía
conectadas, para el cálculo de la capacidad de interrupción y de corriente de cortocircuito del
equipo de generación, así como de las protecciones indicadas en los puntos 6.6.y 6.7 del presente
pliego.

<!-- ric09:8 · pág. 224 -->
8 MEDIDORES

<!-- ric09:8.1 · pág. 224 -->
8.1 Las instalaciones que cuenten con sistema de autogeneración con capacidad de funcionamiento
en paralelo con la red de distribución deberán cumplir con el artículo 5-19 de la NTD y contar con
una unidad de medida que cumpla con el título 4-1 del anexo técnico de los sistemas de medición,
monitoreo y control (SMMC), el cual deberá ser implementado por la empresa distribuidora en
conformidad el artículo 6-11 de la NTD. Estos sistemas deberán ser capaces de generar alertas
cuando se produzcan inyecciones de energía a la red no autorizadas. La empresa distribuidora
será la responsable de monitorear esta alerta y en caso de detectar clientes que inyecten energía
a la red, se deberá notificar al usuario, como se indica en el punto 5.18 de este pliego. En caso
de que esto no se normalice, la empresa distribuidora deberá denunciar este hecho a la
Superintendencia.

<!-- ric09:8.2 · pág. 224 -->
8.2 Todo sistema de autogeneración con una potencia instalada superior a 30 kW deberá contar con
un equipo de monitoreo de generación, que sea capaz de registrar exclusivamente la generación,
el cual deberá quedar montado en el tablero de distribución del equipamiento de autogeneración
y claramente rotulado.

<!-- ric09:9 · pág. 225 -->
9 OPERACIÓN DEL EQUIPO DE GENERACIÓN

<!-- ric09:9.1 · pág. 225 -->
9.1 Un sistema de autogeneración está destinado a funcionar en paralelo con la red pública; por ello
debe contar en su implementación con todo el equipamiento y protecciones necesarias para un
adecuado funcionamiento, desde el punto de vista técnico como de seguridad.

<!-- ric09:9.2 · pág. 225 -->
9.2 La entrada de un generador u otra fuente de autogeneración de energía eléctrica que opere en
paralelo con un sistema de suministro de energía eléctrica deberá ser compatible con la tensión
eléctrica, la forma de la onda y la frecuencia del sistema al cual se va a conectar.

<!-- ric09:9.3 · pág. 225 -->
9.3 En caso de pérdida de energía en la red de distribución, todas las fuentes de generación de
energía eléctrica se deben desconectar automáticamente de la red pública y no se deben volver
a conectar, hasta que se restablezca el suministro de energía de la red de distribución, bajo
condiciones de normalidad operacional.

<!-- ric09:9.4 · pág. 225 -->
9.4 Los sistemas de autogeneración que funcionen en modo isla interna deberán contar con un
sistema de transferencia abierta, que permita operar el sistema una vez que se desconecte de la
red de distribución.

<!-- ric09:9.5 · pág. 225 -->
9.5 Esta nueva operación de sistemas de autogeneración en modo isla interna, se realizará mediante
el sistema de transferencia abierta, que asegure que en ningún momento existirá conexión con
la red de distribución mientras se encuentre operando en este modo.

<!-- ric09:9.6 · pág. 225 -->
9.6 La conexión o reconexión de los equipos de generación a la red de distribución sólo puede ocurrir
si el equipo de generación establece que la tensión y la frecuencia de la red están dentro del
rango de tolerancia, en el artículo 5-16 de la NTCO-EG.

Los propietarios de sistemas de autogeneración, cuya potencia instalada sea superior a 300 kW,
deben designar a un responsable técnico, el que deberá contar con conocimiento técnico sobre
la conexión, operación y mantenimiento de la instalación de autogeneración.

<!-- ric09:10 · pág. 226 -->
10 CONEXIÓN PARA EQUIPOS DE GENERACIÓN SINCRÓNICOS Y ASINCRÓNICOS

<!-- ric09:10.1 · pág. 226 -->
10.1 Un sistema de autogeneración que no se basa en tecnologías con convertidores estáticos, para
el control de sus parámetros de funcionamiento y de sincronización con la red, deberá contar a
lo menos con los siguientes equipos:

<!-- ric09:10.1.1 · pág. 226 -->
10.1.1 Voltímetros que midan simultáneamente las tensiones de la red y de la fuente.

<!-- ric09:10.1.2 · pág. 226 -->
10.1.2 Frecuencímetros que midan simultáneamente las frecuencias de la red y de la fuente.

<!-- ric09:10.1.3 · pág. 226 -->
10.1.3 Sincronoscopio.

<!-- ric09:10.2 · pág. 226 -->
10.2 Para la protección y el control de la puesta en paralelo, o separación de la fuente y la red, el
sistema de autogeneración deberá contar con un relé de sincronismo (25) que permita la puesta
en paralelo automática cuando se alcancen las condiciones de paralelismo.

<!-- ric09:10.3 · pág. 226 -->
10.3 Se deberá contar con un esquema de control y explicación para la partida del autogenerador, el
cual sólo aplicará para equipos de generación asincrónicos. Este esquema de control deberá
estar impreso de forma legible e indeleble cercano al tablero eléctrico del autogenerador.

<!-- ric09:10.4 · pág. 226 -->
10.4 El equipamiento de generación debe incluir un equipo de sincronización que permita acoplar un
generador a una red energizada. Los interruptores de potencia pueden ser cerrados únicamente
si las tensiones en ambos lados del interruptor abierto están en sincronismo, lo que se corroborará
midiendo la tensión, la frecuencia y el desfase del generador y la red.

<!-- ric09:10.5 · pág. 226 -->
10.5 En el caso de la conexión de generadores sincrónicos y asincrónicos que no son conectados en
ausencia de tensión, se debe disponer de un equipo de sincronización. Los valores de ajuste para
efectos de sincronización deben respetar las siguientes tolerancias máximas:

10.5.1 Δφ = 10° Desfase entre tensiones.

10.5.2 Δf = 500 mHz Diferencia entre ambas frecuencias.

10.5.3 ΔV = 10% Vn Porcentaje de diferencia de las tensiones.

<!-- ric09:10.6 · pág. 226 -->
10.6 En el caso de generadores asincrónicos que parten como motor, y que son conectados a una
velocidad entre 95% y 105% de la velocidad sincrónica, el factor de corriente de conmutación
máximo (kimáx) debe ser igual o inferior a 4.

<!-- ric09:10.7 · pág. 226 -->
10.7 El valor de kimáx corresponde a la relación entre la corriente de arranque o partida con la corriente
nominal del generador.

<!-- ric09:10.8 · pág. 226 -->
10.8 Para módulos de autogeneración con alternadores de alta frecuencia, que se rectifica y a través
de un inversor entrega corriente alterna, solo pueden ser conectados a la red con un factor de
corriente de conmutación máximo (kimax) menor a 1,2.

<!-- ric09:10.9 · pág. 226 -->
10.9 Para cualquier sistema de autogeneración, la corriente de partida no deberá generar tensiones
transitorias en su propia barra ni en otras del sistema de distribución inferior a 0,9 pu.

<!-- ric09:11 · pág. 226 -->
11 ROTULACIÓN Y SEÑALIZACIÓN

<!-- ric09:11.1 · pág. 226 -->
11.1 Todas las rotulaciones, señalizaciones, procedimientos y advertencias requeridas en este pliego
deberán cumplir con lo siguiente:

<!-- ric09:11.1.1 · pág. 226 -->
11.1.1 Ser indelebles.

<!-- ric09:11.1.2 · pág. 226 -->
11.1.2 Ser legibles.

<!-- ric09:11.1.3 · pág. 226 -->
11.1.3 Estar diseñadas y fijas de manera que sean legibles durante la vida útil del
equipo o tablero al que están adheridas o relacionadas.

<!-- ric09:11.1.4 · pág. 226 -->
11.1.4 Ser simples y comprensibles.

<!-- ric09:11.2 · pág. 227 -->
11.2 La caja de empalme deberá contar con una placa de advertencia ubicada al frente o a un costado,
de manera que sea visible y con el siguiente texto:

PRECAUCIÓN
ESTA PROPIEDAD CUENTA CON UN SISTEMA DE AUTOGENERACIÓN

<!-- ric09:11.3 · pág. 227 -->
11.3 El tamaño de la placa indicada en el punto 11.2 anterior deberá tener como mínimo de 70 mm
por 40 mm. La inscripción deberá ser indeleble y la letra deberá tener un tamaño de 5 mm cómo
mínimo.

<!-- ric09:11.4 · pág. 227 -->
11.4 Todos los equipamientos, protecciones, interruptores, terminales y alimentadores del equipo de
autogeneración a la llegada de la barra del punto de conexión deben estar rotulados.

<!-- ric09:11.5 · pág. 227 -->
11.5 Se deberá identificar claramente el o los conductores provenientes del equipamiento de
autogeneración que ingresen a la barra de distribución de un tablero diferente al tablero de
autogeneración, tanto en su aislación o cubierta protectora como en el tablero. Se deberá
identificar además la barra de distribución donde se conecte la generación, diferenciándola del
resto de barras de distribución que contenga el tablero eléctrico.

<!-- ric09:11.6 · pág. 227 -->
11.6 Se deberá instalar una placa de identificación legible e indeleble por parte del instalador al
momento de montaje de la unidad de autogeneración, ubicada en el tablero eléctrico que contiene
sus protecciones eléctricas o en los medios de desconexión, en un sitio accesible, en el cual se
especifique la fuente energética y que indique:

<!-- ric09:11.6.1 · pág. 227 -->
11.6.1 Nombre del tablero eléctrico.

<!-- ric09:11.6.2 · pág. 227 -->
11.6.2 Potencia máxima (CA).

<!-- ric09:11.6.3 · pág. 227 -->
11.6.3 Corriente máxima (CA).

<!-- ric09:11.6.4 · pág. 227 -->
11.6.4 La corriente de operación (CC).

<!-- ric09:11.6.5 · pág. 227 -->
11.6.5 La tensión de operación (CC).

<!-- ric09:11.6.6 · pág. 227 -->
11.6.6 La tensión máxima del sistema (CC).

<!-- ric09:11.6.7 · pág. 227 -->
11.6.7 Corriente de cortocircuito (CC).

<!-- ric09:11.7 · pág. 227 -->
11.7 Todas las cajas de paso, unión o derivación empleadas entre el equipo de autogeneración y su
tablero eléctrico deberán contar con una señalética de peligro.

<!-- ric09:11.8 · pág. 227 -->
11.8 Los propietarios de los sistemas de autogeneración deberán contar con procedimientos
abreviados de apagado de emergencia, operación en modo isla (sólo si tiene este modo de
operación) y funcionamiento normal, el cual deberá estar ubicado a un costado del tablero de
autogeneración. El tamaño de la letra del procedimiento será como mínimo de 6 mm.

<!-- ric09:Anexo 9.1 · pág. 228 -->
ANEXO N°9.1
RESUMEN DE EXIGENCIA DE PROTECCIONES PARA SISTEMAS DE AUTOGENERACIÓN

```
                               Potencia de                                         Protección            Protección    Protección de                      Registrador de
                                                   Protección por    Protección                                                            Sistema de
 Sistemas de               autogeneración en                                           RI                    RI          potencia                       energía del sistema
                                                   sobre corriente   por falla a                                                           control de
autogeneración           relación a la capacidad                                 complementaria         centralizada      inversa                         autogeneración
                                                      de fases         tierra                                                            inyección cero
                              del empalme                                              (a)                   (b)            (c)                                 (d)
                                 ≤ 30%
                            Cap. empalme BT               X               X                X                                                    X
```
de hasta 10kW
```
Potencia instalada
    >a1W y
```
≤ a 10 kW > 30%
```
Cap. empalme BT               X               X                X                                  X                 X
```
de hasta 10kW

```
≤ 10%
```
Potencia instalada
Cap. empalme BT o MT
```
                                                         X               X                X                                                    X                X
> a 10 kW y
                              > 10%
≤ a 100 kW                                               X               X                X                                  X                 X                X
```
Cap. empalme BT o MT

≤ 100%
Potencia instalada
>100 kW
```
Cap. empalme                X               X                                  X                X                 X                X
```
BT o MT

(a) : La RI complementaria debe operar sobre el interruptor de acoplamiento, en caso de que se cuente con inversores, la RI integrada debe operar sobre el inversor desconectando el sistema
de autogeneración asociado al inversor.
(b) : Si la capacidad instalada del sistema de autogeneración es ≤ 100 kW, no se requiere de la protección RI centralizada, siempre y cuando se cuente con la protección RI complementaria o
con la RI integrada en el inversor. Asimismo, en el caso de equipos de autogeneración sin inversores la protección RI deberá ser del tipo centralizada.
(c) : La protección de potencia inversa no será exigida para aquellas instalaciones que cumplan con:
i) equipos de autogeneración cuya capacidad instalada (CI) sea ≤ a 10 kW, que a su vez dicha CI no supere el 30% de la capacidad del empalme, y tenga sistema de control de inyección.
ii) equipos de autogeneración cuya capacidad instalada (CI) sea ≤ a 100 kW, que a su vez dicha CI no supere el 10% de la capacidad del empalme, y tenga sistema de control de inyección.
(d) : Este equipo destinado de forma exclusiva a la medición del sistema de será exigido en todo sistema de autogeneración con una potencia instalada superior a 30 kW.

<!-- ric09:Anexo 9.2 · pág. 229 -->
ANEXO N° 9.2
ESQUEMA DE PROTECCIONES PARA SISTEMAS DE AUTOGENERACIÓN >100KW

OPCIÓN A: PROTECCIÓN RI CENTRALIZADA JUNTO A PROTECCIÓN DE POTENCIA INVERSA Y SISTEMA
DE CONTROL DE INYECCIÓN CON OPERACIÓN SOBRE INTERRUPTOR DE ACOPLAMIENTO
CENTRALIZADO QUE DESCONECTARÁ EL SUMINISTRO DEL SISTEMA DE AUTOGENERACIÓN

La operación de la protección de potencia inversa para este esquema tipo, debe cortar sólo el suministro del
sistema de autogeneración, como lo establece el numeral 6.6.3.1, pudiendo operar sobre el mismo interruptor de
acoplamiento de la protección RI Centralizada, siempre que las condiciones técnicas de los equipos lo permitan y
todos los equipos indicados en este esquema estén en el mismo gabinete (Tablero de Punto de Conexión).

Como la potencia instalada del sistema de autogeneración es superior a 100 kW, deberá contar con la protección
RI Centralizada (de forma independiente a las protecciones RI complementarias en caso de que se tengan), la
cual comandará al interruptor de acoplamiento en caso de presentarse una operación en modo isla o cuando se
presentan valores inadmisibles de las tensiones o la frecuencia.

* El sistema de control de inyección cero se ejemplifica en el Anexo N° 9.5 de este pliego técnico

*Sistema de autogeneración con potencia instalada superior a 30 kW debe contar con un registrador de la energía
que mida en forma exclusiva la generación del sistema.

OPCIÓN B: PROTECCIÓN DE POTENCIA INVERSA JUNTO A SISTEMA DE CONTROL DE INYECCIÓN Y
PROTECCIÓN RI CENTRALIZADA CON OPERACCIÓN SOBRE INTERRUPTOR DE ACOPLAMIENTO A
TRAVÉS DE DISPARO TRANSFERIDO QUE DESCONECTARÁ SÓLO EL SUMINISTRO DEL SISTEMA DE
AUTOGENERACIÓN)

La operación de la protección de potencia inversa para este esquema tipo, debe cortar sólo el suministro del
sistema de autogeneración, como lo establece el numeral 6.6.3.1, debiendo operar sobre su propio interruptor de
acoplamiento, contactor de poder o reconectador (según corresponda al tipo de instalación).

Como la potencia instalada del sistema de autogeneración es superior a 100 kW, deberá contar con la protección
RI Centralizada (de forma independiente a las protecciones RI complementarias), la cual comandará al
interruptor de acoplamiento centralizado que en este ejemplo es a través del disparo transferido.

* Interruptor de acoplamiento debe provocar la desconexión del sistema de autogeneración en caso de que tenga
una pérdida de la señal de control.
**Sistema de autogeneración con potencia instalada superior a 30 kW debe contar con un registrador de la energía
que mida en forma exclusiva la generación del sistema.

OPCIÓN C: PROTECCIÓN RI CENTRALIZADA JUNTO A PROTECCIÓN DE POTENCIA INVERSA Y SISTEMA
DE CONTROL DE INYECCIÓN CON OPERACIÓN SOBRE INTERRUPTOR DE ACOPLAMIENTO
CENTRALIZADO QUE DESCONECTARÁ EL SUMINISTRO DE LA INSTALACIÓN DE CONSUMO

La operación de la protección de potencia inversa para este esquema tipo, debe cortar el suministro de toda la
instalación de consumo, como lo establece el numeral 6.6.3.2, pudiendo operar sobre el mismo interruptor de
acoplamiento de la protección RI Centralizada, siempre que las condiciones técnicas de los equipos lo permitan y
todos los equipos indicados en este esquema estén en el mismo gabinete (Tablero de Punto de Conexión).

Como la potencia instalada del sistema de autogeneración es superior a 100 kW, deberá contar con la protección
RI Centralizada (de forma independiente a las protecciones RI complementarias en caso de que se tengan), la
cual comandará al interruptor de acoplamiento en caso de presentarse una operación en modo isla o cuando se
presentan valores inadmisibles de las tensiones o la frecuencia.

* El sistema de control de inyección cero se ejemplifica en el Anexo N° 9.5 de este pliego técnico
** Sistema de autogeneración con potencia instalada superior a 30 kW debe contar con un registrador de la energía
que mida en forma exclusiva la generación del sistema.

OPCIÓN D: SISTEMA DE CONTROL DE INYECCIÓN JUNTO A PROTECCIÓN RI CENTRALIZADA Y
PROTECCIÓN DE POTENCIA INVERSA CON OPERACIÓN SOBRE INTERRUPTOR DE ACOPLAMIENTO QUE
DESCONECTARÁ EL SUMINISTRO DE LA INSTALACIÓN DE CONSUMO

La operación de la protección de potencia inversa para este esquema tipo, debe cortar el suministro de toda la
instalación de consumo, como lo establece el numeral 6.6.3.2, debiendo operar sobre su propio interruptor de
acoplamiento, contactor de poder o reconectador (según corresponda al tipo de instalación).

Como la potencia instalada del sistema de autogeneración es superior a 100 kW, deberá contar con la protección
RI Centralizada (de forma independiente a las protecciones RI complementarias), la cual comandará al
interruptor de acoplamiento que en este ejemplo es a través del disparo transferido.

* Interruptor de acoplamiento debe provocar la desconexión del sistema de autogeneración en caso de que tenga
una pérdida de la señal de control.
**Sistema de autogeneración con potencia instalada superior a 30 kW debe contar con un registrador de la energía
que mida en forma exclusiva la generación del sistema.

<!-- ric09:Anexo 9.3 · pág. 233 -->
ANEXO N° 9.3
ESQUEMA DE PROTECCIONES PARA SISTEMAS DE AUTOGENERACIÓN ≤ 100 KW Y QUE
CUMPLAN CON LO INDICADO EN EL PUNTO 6.6.8
(SISTEMA DE CONTROL DE INYECCIÓN JUNTO A PROTECCIÓN RI COMPLEMENTARIA)

a) Aplica para potencia instalada de autogeneración menor o igual a 100 kW y que su potencia de
generación no supere el 10% de la capacidad del empalme de la instalación de consumo.

b) Aplica para instalaciones domiciliarias con empalmes en baja tensión de hasta 10 kW y que el
o los equipos de autogeneración tengan una potencia de generación que no supere el 30% de
la capacidad del empalme de la instalación de consumo.

El esquema tipo que se señala en este Anexo, muestra un sistema de generación a través de Energías Renovables
con inversor con protección RI integrada, pero también podría contar con una protección RI
complementaria externa al equipo de autogeneración.

Como este esquema tipo NO requiere contar con la protección de potencia inversa, por no cumplir con lo indicado
en 6.6.8, debiendo contar con su sistema de control de inyección cero en un gabinete (Tablero de Punto de
Conexión) que será sellado por la Empresa Distribuidora.

La protección RI operará sobre el interruptor de acoplamiento en caso de presentarse una operación en modo isla
o cuando se presentan valores inadmisibles de las tensiones o la frecuencia.

* El sistema de control de inyección cero se ejemplifica en el Anexo N° 9.5 de este pliego técnico

<!-- ric09:Anexo 9.4 · pág. 234 -->
ANEXO N° 9.4
ESQUEMA DE PROTECCIONES PARA SISTEMAS DE AUTOGENERACIÓN ≤ 100 KW
POTENCIA INSTALADA DE AUTOGENERACION SUPERA 10% DE LA CAPACIDAD DEL
EMPALME O NO CUMPLEN CON LOS CRITERIOS DEL PUNTO 6.6.8

OPCIÓN A: PROTECCIÓN RI COMPLEMENTARIA JUNTO A SISTEMA DE CONTROL DE INYECCIÓN Y
PROTECCIÓN DE POTENCIA INVERSA CON OPERACIÓN SOBRE INTERRUPTOR DE ACOPLAMIENTO QUE
DESCONECTARÁ SÓLO EL SUMINISTRO DEL SISTEMA DE AUTOGENERACIÓN)

Como este esquema tipo SI requiere contar con la protección de potencia inversa, por no cumplir con lo indicado
en 6.6.8, debiendo contar además con su sistema de control de inyección cero en un gabinete (Tablero de Punto
de Conexión) que será sellado por la Empresa Distribuidora.

El esquema tipo que se señala en este Anexo, muestra un sistema de generación a través de Energías Renovables
con inversor con protección RI integrada, pero también podría contar con una protección RI
complementaria externa al equipo de autogeneración.

La protección RI complementaria operará sobre el interruptor de acoplamiento en caso de presentarse una
operación en modo isla o cuando se presentan valores inadmisibles de las tensiones o la frecuencia.

*La operación de la protección de potencia inversa para este esquema tipo, debe cortar sólo el suministro del
sistema de autogeneración, como lo establece el numeral 6.6.3.1.
** El sistema de control de inyección cero se ejemplifica en el Anexo N° 9.5 de este pliego técnico
***Sistema de autogeneración con potencia instalada superior a 30 kW debe contar con un registrador de la energía
que mida en forma exclusiva la generación del sistema.

OPCIÓN B: PROTECCIÓN RI COMPLEMENTARIA JUNTO A SISTEMA DE CONTROL DE INYECCIÓN Y
PROTECCIÓN DE POTENCIA INVERSA CON OPERACIÓN SOBRE INTERRUPTOR DE ACOPLAMIENTO QUE
DESCONECTARÁ EL SUMINISTRO DE LA INSTALACIÓN DE CONSUMO)

Como este esquema tipo SI requiere contar con la protección de potencia inversa, por no cumplir con lo indicado
en 6.6.8, debiendo contar además con su sistema de control de inyección cero en un gabinete (Tablero de Punto
de Conexión) que será sellado por la Empresa Distribuidora.

El esquema tipo que se señala en este Anexo, muestra un sistema de generación a través de Energías Renovables
con inversor con protección RI integrada, pero también podría contar con una protección RI
complementaria externa al equipo de autogeneración.

La protección RI complementaria operará sobre el interruptor de acoplamiento en caso de presentarse una
operación en modo isla o cuando se presentan valores inadmisibles de las tensiones o la frecuencia.

*La operación de la protección de potencia inversa para este esquema tipo, debe cortar el suministro de toda la
instalación de consumo, como lo establece el numeral 6.6.3.2.
* El sistema de control de inyección cero se ejemplifica en el Anexo N° 9.5 de este pliego técnico
*Sistema de autogeneración con potencia instalada superior a 30 kW debe contar con un registrador de la energía
que mida en forma exclusiva la generación del sistema.

<!-- ric09:Anexo 9.5 · pág. 236 -->
ANEXO N°9.5
ESQUEMA TIPO PARA UNIDADES DE AUTOGENERACIÓN CON EQUIPO CONTROL DE
INYECCIÓN CERO

El esquema tipo que se señala en este anexo, muestra un sistema de generación fotovoltaica
controlada por un dispositivo central autónomo. Este esquema requiere de un equipo externo
al sistema de generación (para el ejemplo, se utiliza el equipo de monitoreo de inyección que
tiene la capacidad de medir el consumo neto de energía hacia la red), quien comunica al (los)
inversor (es) al momento de limitar las inyecciones configuradas.

El máximo tiempo de actuación del sistema de limitación de inyección en reducir la potencia
aparente exportada actual a un valor igual o menor a la capacidad exportable máxima será de
5 segundos.

El sistema de limitación de inyección debe ser fail-safe o falla-segura, de forma que, si
cualquier componente o sistema de señales que comprometa la limitación de energía falla o
pierde su fuente de alimentación, el esquema debe reducir la potencia activa inyectada a la
red a un valor que sea menor o igual a la máxima potencia exportable en una ventana de 5
segundos.

El sistema de control de inyección cero deberá estar ubicado en el tablero de punto de
conexión, el cual deberá ser sellado por la empresa de distribución, ubicado al costado del
empalme o lo más cercano posible a él.
