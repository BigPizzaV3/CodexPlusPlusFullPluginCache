# Ficha del conector Fina para Claude

Texto preparado; no se creó ni envió una presentación.

- Nombre: Fina
- Desarrollador del paquete: Fina. El propietario debe confirmar la identidad de la organización que presentará la ficha.
- URL MCP: https://mcp.finamoney.co/mcp
- Transporte: Streamable HTTP remoto; en `.mcp.json` de Claude se declara `type: http`.
- Autenticación: OAuth mediante Fina; no distribuir API keys ni headers de autorización en el paquete. Usar el descubrimiento que ofrezca el endpoint, sin inventar client ID/secret.
- Sitio: https://finamoney.co/
- Documentación del paquete: https://github.com/stevedesignerdsmb/fina-plugins/tree/main/claude#readme
- Soporte: https://github.com/stevedesignerdsmb/fina-plugins/blob/main/SUPPORT.md
- Contacto: support@finamoney.co
- Privacidad: https://finamoney.co/privacy-policy
- Términos: https://finamoney.co/terms-conditions
- Categoría propuesta: Financial services
- Icono: el mismo logo Fina incluido en assets.

## Descripción

Connect your Fina account to organize and understand your personal finances. Review recorded purchases and income, current account estimates, subscriptions, upcoming card obligations, debts, investments, properties and saved goals. Start or resume setup from saved progress. Record or correct financial information you provide, with a preview and confirmation for bulk transaction imports. Fina records financial activity; it does not move money, execute payments or investment trades, or cancel services with merchants. Dashboards, files and scheduled updates use the capabilities and permissions of your Claude environment.

## Ejemplos

1. Ayúdame a configurar Fina o continúa desde donde me quedé.
2. Revisa mis gastos de este mes y mis próximos pagos.
3. Importa estas compras a Fina y muéstrame el plan antes de guardarlas.
4. Crea mi dashboard y programa que se actualice cada mañana, conservando el mismo.

## Datos y acciones

Lecturas: estado de configuración, cuentas, compras/ingresos registrados, compromisos, obligaciones, proyecciones, evidencia y contexto patrimonial del propietario autenticado. Escrituras: preferencias y registros solicitados; importación con preview/confirmación; correcciones, asociaciones y observaciones fechadas. La investigación inmobiliaria es una operación de investigación externa explícita. Las tareas y artefactos pertenecen al host, no al MCP. WhatsApp usa la misma cuenta financiera con conexión separada.

## Preparación de acceso

Preparar una cuenta de revisión independiente, poblada con datos sintéticos, y proporcionar credenciales/instrucciones únicamente mediante los campos seguros del portal. Mantener el acceso durante revisión. El ZIP no contiene una cuenta ni certifica que OAuth haya pasado la revisión.

Presentar conector y plugin desde la misma organización y exactamente el mismo endpoint. Los casos y la matriz de herramientas están en esta carpeta. Para el plugin público, seleccionar la carpeta `claude`, rama `main`, del repositorio indicado. Una instalación privada por ZIP no es la presentación pública. Continuar cualquier ficha existente en lugar de duplicarla; el envío y las declaraciones del portal los realiza el propietario.
