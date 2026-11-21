package com.example.sinch.jwt

import android.os.Handler
import android.os.Looper
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL
import java.util.concurrent.Executors

/**
 * Fetches a Sinch registration token from your own backend.
 *
 * The backend signs the token with the Application Secret (see
 * assets/registration-token-server.mjs) and decides which Sinch user ID the
 * signed-in session may register as. The app never holds the secret and never
 * asks for a token for an arbitrary user ID: it only sends its own session
 * credential.
 *
 * @param tokenEndpoint HTTPS URL of your backend token endpoint.
 * @param sessionToken  Returns the current app session credential (for example an OAuth access token).
 */
class BackendJWTFetcher(
    private val tokenEndpoint: String,
    private val sessionToken: () -> String?,
) : JWTFetcher {

    private val executor = Executors.newSingleThreadExecutor()
    private val mainHandler = Handler(Looper.getMainLooper())

    override fun acquireJWT(onSuccess: (String) -> Unit, onFailure: (Exception) -> Unit) {
        executor.execute {
            try {
                val session = sessionToken() ?: throw IllegalStateException("No signed-in session")
                val url = URL(tokenEndpoint)
                require(url.protocol == "https") { "Token endpoint must use HTTPS" }

                val connection = (url.openConnection() as HttpURLConnection).apply {
                    requestMethod = "POST"
                    connectTimeout = 10_000
                    readTimeout = 10_000
                    instanceFollowRedirects = false
                    setRequestProperty("Authorization", "Bearer $session")
                    setRequestProperty("Accept", "application/json")
                }
                try {
                    if (connection.responseCode != HttpURLConnection.HTTP_OK) {
                        throw IllegalStateException("Token endpoint returned HTTP ${connection.responseCode}")
                    }
                    val body = connection.inputStream.bufferedReader().use { it.readText() }
                    val token = JSONObject(body).getString("token")
                    mainHandler.post { onSuccess(token) }
                } finally {
                    connection.disconnect()
                }
            } catch (e: Exception) {
                mainHandler.post { onFailure(e) }
            }
        }
    }
}
