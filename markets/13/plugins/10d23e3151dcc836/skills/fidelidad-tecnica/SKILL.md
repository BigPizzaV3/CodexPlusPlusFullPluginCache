---
name: fidelidad-tecnica
description: "Usar junto con la interpretación Astroanamnesis de cualquier carta o factor natal aportado en el chat, antes de presentar una lectura al consultante o profesional, para cotejar datos técnicos literales entre el prompt aprobado y la respuesta sin recalcular cartas. No se activa para preguntas generales sin datos de carta ni respuestas numéricas de los motores oficiales."
---

# Astroanamnesis · Fidelidad al prompt aprobado

Esta habilidad complementa, **sin sustituir ni alterar**, `skills/instructions/SKILL.md`, el método protegido, la autenticación y el criterio del astroanamnólogo. Actívala siempre que el complemento Astroanamnesis vaya a formular o revisar una interpretación técnica de una o más cartas o factores aportados explícitamente en la conversación actual, ya sea una respuesta breve, una lectura parcial o una lectura extensa.

No se usa para explicar el método en abstracto, gestionar la cuenta o devolver resultados numéricos tal como los proporciona un motor oficial sin reinterpretarlos. Si hay una interpretación añadida a una respuesta numérica, sí se audita esa interpretación.

## Autoridad y alcance

El **prompt original aprobado por la persona profesional** es la fuente autorizada. No calcular aspectos, posiciones, orbes, regencias ni planetas por inferencia; no rechazar el prompt porque difiera de un motor o de otras cartas; no corregir las discrepancias Tropical–Memoria ni hacer equivalencias entre mapas. La función consiste únicamente en comprobar si lo que se escribe coincide con lo que se ha proporcionado explícitamente para la misma carta. Ninguna afirmación biográfica se convierte en certeza por pasar el comparador.

Las fuentes permitidas son las cartas y los mensajes de este chat o el contenido recuperado con `shared_chart_read` cuando el usuario haya compartido explícitamente la carta. Las herramientas autenticadas conservan sus permisos y su propio procedimiento. No buscar casos anteriores, ni utilizar memoria, ni enviar contenido natal a un servicio distinto para auditarlo.

## Procedimiento cuando existan datos de carta

1. Identifica la fuente exacta del caso actual y conserva el texto original **literal** en UTF-8 sin cambios de signos, orbes, nombres, grados, espacios o saltos de línea. Si la carta está compartida, respeta primero el acceso y la lectura íntegra regulados por la habilidad `instructions`; solo utiliza la copia autorizada. No inventes ni solicites un `shareId` cuando se haya pegado texto suficiente en el chat. Si el texto aportado es solo un fragmento, no lo trates como carta completa.
2. **Antes de interpretar**, ejecuta realmente el script empaquetado `scripts/comparador_fidelidad.py` mediante Python 3.10+ usando `preparar`, sobre una copia literal del prompt. Lee el registro y sus `sourcePending`; no declares validado un dato no extraído. Si la extracción no reconoce hechos técnicos suficientes, evita afirmaciones no fundamentadas y señala el límite. La existencia del script en el paquete no demuestra que se haya ejecutado.
3. Redacta la respuesta dentro del método de Astroanamnesis, sin ampliar ni alterar los datos. Antes de publicarla, guarda una copia íntegra y **exacta** del texto que se va a mostrar, y ejecuta `auditar` con ese borrador y el mismo prompt, registro y versión del script. La auditoría debe cubrir toda la respuesta, no un resumen ad hoc ni una lista de datos construida para superar la prueba.
4. Lee los campos `fidelityStatus`, `issues`, `sourcePending`, `coverage` y `manualReviewRequired`. Si hay discrepancia reconocida, **corrige el texto, no el prompt**, y audita de nuevo. En un aspecto ambiguo, evita adivinar el sujeto: redáctalo con mapa, dos cuerpos y aspecto explícitos solo cuando la fuente lo permita; de lo contrario déjalo pendiente y no afirmes haberlo verificado. Usa las referencias de línea y las citas literales del resultado. No atribuyas al software cobertura global de la prosa.
5. Justo antes de entregar, usa `comprobar` con el prompt original, el texto definitivo y el recibo elegido. Si cambia cualquier carácter del texto después de la auditoría, repítela. El recibo vigente solamente acredita que se auditó ese contenido, no que todo sea correcto. La aprobación profesional, si corresponde, se registra aparte y nunca se inventa.

## Ejecutabilidad y respuesta

El comparador exige **ejecución Python real** con acceso al script y a los textos completos. Si el entorno de la conversación no dispone de Python o no puede recuperar la fuente literalmente, **no anuncies comprobación automática** ni marques la interpretación como validada. Puedes explicar los límites y trabajar con los datos visibles mediante contraste manual, indicando que tal contraste no es una auditoría por código. Si la solicitud pide expresamente una respuesta verificada antes de publicarse, conserva el borrador como pendiente cuando no exista ejecutor.

Para una consulta breve, compara únicamente lo realmente aportado, sin exigir tres cartas ni extender el texto para introducir más hechos. Si la respuesta está en otro idioma distinto del español o utiliza expresiones que el programa no reconoce, registra cobertura limitada y exige revisión de esas partes; no traduzcas el texto solo para pasar el validador. No añadas declaraciones técnicas de aspecto, casa o signo que falten en la fuente.

El resultado `matched_supported_claims` solo acredita coincidencia de **las afirmaciones reconocidas**, no validación total. `deliveryAllowed=false` permanece inalterado en el comparador: no debe editarse para simular aprobación. Un informe profesional completo requiere la revisión del profesional y sus controles específicos, aunque la auditoría automática no encuentre discrepancias.

Para comandos, límites, códigos de salida y gramática documentada, lee `references/README-comparador.md`. El script y las pruebas se suministran sin datos de consultantes ni comunicación de red. Nunca muestres como «68 pruebas superadas en esta conversación» una prueba que no se haya ejecutado aquí.
