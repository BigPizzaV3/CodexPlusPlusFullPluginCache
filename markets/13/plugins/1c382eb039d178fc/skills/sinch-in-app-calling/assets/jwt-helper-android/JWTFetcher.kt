package com.example.sinch.jwt

/**
 * Obtains a Sinch registration token (JWT) for the signed-in user.
 *
 * Implementations must get the token from your backend (see BackendJWTFetcher).
 * Never sign tokens on the device: that requires shipping the Application Secret.
 */
interface JWTFetcher {

    /**
     * @param onSuccess Invoked on the main thread with the signed JWT.
     * @param onFailure Invoked on the main thread if no token could be obtained.
     */
    fun acquireJWT(onSuccess: (String) -> Unit, onFailure: (Exception) -> Unit)
}
