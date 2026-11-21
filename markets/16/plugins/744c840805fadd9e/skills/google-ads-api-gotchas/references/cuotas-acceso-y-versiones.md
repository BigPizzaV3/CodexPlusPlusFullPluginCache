# Cuotas, acceso y versiones

### El acceso Basic topa en 15.000 operaciones por 24 horas por proyecto de Google Cloud, lecturas incluidas
- **Tipo**: gotcha de API
- **Por qué**: cada request de `search` o `searchStream` cuenta 1, devuelva las filas que devuelva. El contador es del proyecto de Google Cloud de las credenciales, compartido por todo lo que use ese proyecto. Al pasarlo fallan también las lecturas: `429 ResourceExhausted`, `QuotaError`. Explorer topa en 2.880 operaciones al día en cuentas reales; Standard no tiene tope ([niveles de acceso](https://developers.google.com/google-ads/api/docs/api-policy/access-levels)).
- **Cómo detectarlo**: el mensaje `Number of operations for basic access` con un `Retry in N seconds` que puede ser de muchas horas.
- **Qué hacer**: contar operaciones antes de lanzar cargas grandes y tener en cuenta lo que corre ese día. Repartir la carga entre proyectos de Google Cloud o pedir un nivel de acceso superior. `change_event` no ve lecturas: registrar quién consume.
- **Evidencia**: Visto en 4+ cuentas, jun-sep 2026, v23-v24.

### El nivel de acceso va con el proyecto de Google Cloud de las credenciales OAuth
- **Tipo**: gotcha de API
- **Por qué**: desde el 9 de septiembre de 2026, el nivel de acceso (Test, Explorer, Basic, Standard) pertenece al proyecto de Google Cloud con el que se generan las credenciales OAuth. Un developer token enviado en las peticiones se ignora.
- **Cómo detectarlo**: si el proyecto de las credenciales solo tiene Test, las llamadas a cuentas reales fallan con `AuthorizationError.CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION`. El nivel de cada proyecto se ve en la página de la Google Ads API en Cloud Console.
- **Qué hacer**: si un cliente te da acceso con su nivel, necesitas su OAuth client, del proyecto que tiene ese nivel. El usuario que consiente puede ser externo si tiene acceso a la cuenta.
- **Evidencia**: Cambio documentado por Google, sep 2026 ([retirada de los developer tokens](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)).

### Las listas y portfolios del manager se mutan contra la cuenta dueña
- **Tipo**: gotcha de API
- **Por qué**: la vista proyectada en la cuenta hija devuelve un resource name con el ID de la hija. Mutar con ese ID da `RESOURCE_NOT_FOUND`. Con un login sin permiso sobre un manager intermedio sale `USER_PERMISSION_DENIED`.
- **Cómo detectarlo**: un `create` de sonda con `validate_only` sobre la lista falla. Consultar `customer_manager_link` de la hija para conocer sus managers.
- **Qué hacer**: mutar con `customer_id` = cuenta dueña y un `login_customer_id` con acceso. No deducir el dueño del resource name. Antes de añadir, contar en qué cuentas y campañas está enlazada la lista.
- **Evidencia**: Visto en 2-3 cuentas, ago-nov 2026, v24.

### Tras borrar en una lista del manager, la cuenta hija sigue viendo el criterio unos minutos
- **Tipo**: gotcha de API
- **Por qué**: la vista proyectada de la hija se actualiza con retraso. Desde la cuenta dueña el criterio desaparece al instante.
- **Cómo detectarlo**: un borrado correcto que la hija sigue devolviendo.
- **Qué hacer**: verificar contra la cuenta dueña. No repetir el mutate por un falso negativo.
- **Evidencia**: Visto en 1 cuenta, ago 2026, v24.

### La librería usa la versión de API más alta que trae
- **Tipo**: gotcha de API
- **Por qué**: `google-ads` elige por defecto la versión más reciente incluida. Los pins en `requirements.txt` no sirven si el script corre sobre otra instalación. Google retira versiones con pocos meses de aviso (v19 en feb-2026).
- **Cómo detectarlo**: avisos de sunset sobre una versión que nadie fija a mano. Comprobar la versión de la librería instalada en cada entorno.
- **Qué hacer**: no fijar el número de versión en el código salvo en un único sitio. Actualizar la librería en todos los entornos a la vez.
- **Evidencia**: Visto en 4+ cuentas, jul 2026, v21-v24.

### Una caché de lecturas tiene que caducar antes de un día
- **Tipo**: error de método
- **Por qué**: las conversiones maduran y cambian a diario. Una caché de varios días sirve datos rancios. Una consulta que incluye hoy no se debe cachear.
- **Cómo detectarlo**: cifras de ayer que no cambian entre ejecuciones de días distintos.
- **Qué hacer**: TTL por debajo de 24 horas, clave con customer, versión de API, versión de librería y consulta normalizada, y bypass si la consulta referencia hoy.
- **Evidencia**: Visto en 4+ cuentas, jun 2026, v23-v24.

### Con consent screen Internal, el código OAuth caduca en minutos
- **Tipo**: gotcha de API
- **Por qué**: si solo usuarios del dominio del cliente pueden consentir, alguien de ese dominio aprueba y devuelve la URL de redirección. El `code` caduca en unos 10 minutos y es de un solo uso.
- **Cómo detectarlo**: `invalid_grant` al canjear un código reenviado tarde.
- **Qué hacer**: flujo PKCE con redirect de loopback. La persona copia la URL de error del navegador, que contiene el `code`, y se canjea de inmediato.
- **Evidencia**: Visto en 1 cuenta, sep 2026.
