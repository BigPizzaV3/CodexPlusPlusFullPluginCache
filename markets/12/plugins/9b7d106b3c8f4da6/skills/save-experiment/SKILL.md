---
name: save-experiment
description: Usa cuando el usuario pida guardar o llevar una ficha de experimento a su proyecto de Xperiments. Prepara un enlace de revisión; el guardado requiere confirmación en la web.
---

# Diseñar y guardar una ficha en Xperiments

Esta es la única herramienta externa del complemento: prepare_experiment_save.

1. Reúne title, context, hypothesis, metric y success_criteria. Aclara decisiones importantes que falten sin inventar evidencia ni presentar umbrales propuestos como observaciones.
2. Cuando el usuario pida guardar la ficha o llevarla a su proyecto, llama a prepare_experiment_save con esos campos. Incluye start, tags o ICE solo si el usuario los especificó. Las puntuaciones son enteros de 1 a 10 y la fecha es AAAA-MM-DD. No envíes conversaciones enteras, archivos, identidades, proyectos ni credenciales.
3. Devuelve save_url como «Revisar y guardar en Xperiments», conservando completo el fragmento #draft=. Explica que caduca a los 30 minutos. No fabriques enlaces ni sustituyas el resultado por la portada.
4. El usuario abre el enlace, inicia sesión, elige su proyecto autorizado y confirma. La herramienta devuelve saved=false y pending_confirmation: no afirmes guardado, creación ni sincronización al devolver el enlace. No recibe confirmación automática del guardado web.
5. Reutiliza el mismo enlace vigente si se reintenta el mismo guardado. Repetirlo en la misma cuenta y proyecto no duplica la ficha; preparar otro enlace crea otro plan pendiente. Si caduca, prepara uno nuevo con los mismos campos revisados cuando se solicite.

El complemento solo prepara fichas nuevas. La consulta, edición y eliminación posteriores se realizan desde Xperiments. Guardar un plan no ejecuta la prueba ni demuestra resultados. No pidas contraseñas ni claves en el chat.

## Uso en conversaciones compatibles

Instala Xperiments Validación y úsalo en una conversación compatible de ChatGPT o Codex donde esté disponible prepare_experiment_save. El servidor MCP es remoto y no requiere ejecución local. Si la herramienta está disponible, utilízala en la conversación actual; no obligues a cambiar a Work. Si falta, explica que esta conversación no expone la herramienta, comprueba la instalación y conexión y recomienda abrir una conversación nueva compatible con el complemento. No prometas que publicar el complemento activará herramientas en todas las cuentas, regiones o superficies. La sesión de Xperiments es independiente de la sesión de ChatGPT.

Cada usuario abre el enlace con su propia cuenta de Xperiments y elige un proyecto donde tenga permiso de creación. El complemento no usa la cuenta del creador ni una sesión compartida. Si no tiene cuenta o proyecto, debe registrarse y crear su proyecto en Xperiments; si pertenece a un equipo, necesita el permiso correspondiente. Nunca selecciones proyectos ni identidades por tu cuenta. Si el usuario cambia de cuenta antes de confirmar, debe revisar de nuevo el destino.
