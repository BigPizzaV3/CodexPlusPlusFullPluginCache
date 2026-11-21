> **Not a schema.** This file shows iOS SDK installation and client-initialization examples
> for In-App Calling. For SDK method signatures and initialization options, refer to the
> canonical `developers.sinch.com` docs linked from the parent [SKILL.md](../SKILL.md) before
> writing code or prose that states payload structure.

# SDK Installation — In-App Calling (iOS)

In-App Calling uses the **Sinch RTC SDK** (Swift) — a separate client-side SDK from `@sinch/sdk-core`. Authentication is handled via JWT tokens generated on your backend using Application Key + Application Secret credentials.

Based on the [official getting-started guide](https://developers.sinch.com/docs/in-app-calling/getting-started/ios/create-app.md).

## Prerequisites

- Xcode
- In-App Calling [SDK for iOS](https://developers.sinch.com/docs/in-app-calling/sdk-downloads.md)
- APNs signing key from your [Apple Developer Account](https://developer.apple.com/) uploaded to your [Sinch Developer Account](https://dashboard.sinch.com/voice/apps)

## Add the SDK

Download the Sinch Swift SDK from the [SDK download page](https://developers.sinch.com/docs/in-app-calling/sdk-downloads.md) and add `SinchRTC.xcframework` to your Xcode project. Set it to **Embed & Sign** — otherwise you'll get `dylib` loading failures.

In your project's Target → Signing & Capabilities:
- Enable **Voice over IP** under Background Modes (required for CallKit / LiveCommunicationKit)
- Add the **Push Notifications** capability

## Configuration

Create a `Config.swift` file:

```swift
let APPLICATION_KEY = "YOUR_APPLICATION_KEY" // the key is public; the secret stays on your backend

let ENVIRONMENT_HOST = "ocra.api.sinch.com"

let TOKEN_ENDPOINT = URL(string: "https://api.example.com/sinch-token")!
```

## Initialize via SinchClientMediator

Create a `SinchClientMediator` class as a wrapper around `SinchClient`:

```swift
import SinchRTC
import OSLog

typealias ClientStartedCallback = (_ error: Error?) -> Void

class SinchClientMediator {

  var clientStartedCallback: ClientStartedCallback!

  private(set) var sinchClient: SinchClient?

  func createAndStartClient(with userId: String, and callback: @escaping (_ error: Error?) -> Void) {
    do {
      sinchClient = try SinchRTC.client(withApplicationKey: APPLICATION_KEY,
                                        environmentHost: ENVIRONMENT_HOST,
                                        userId: userId)
    } catch let error as NSError {
      callback(error)
      return
    }

    clientStartedCallback = callback

    guard let sinchClient = sinchClient else { return }

    sinchClient.delegate = self
    sinchClient.start()
  }
}
```

## Provide Credentials (SinchClientDelegate)

Implement `SinchClientDelegate` for credential provisioning and client status monitoring:

```swift
struct TokenResponse: Decodable { let token: String }

enum TokenError: Error { case notSignedIn, badStatus(Int) }

extension SinchClientMediator: SinchClientDelegate {

  func clientRequiresRegistrationCredentials(_ client: SinchRTC.SinchClient,
                                             withCallback callback: SinchRTC.SinchClientRegistration) {
    guard let sessionToken = authSession.currentAccessToken else {
      callback.registerDidFail(error: TokenError.notSignedIn)
      return
    }
    var request = URLRequest(url: TOKEN_ENDPOINT)
    request.httpMethod = "POST"
    request.timeoutInterval = 10
    request.setValue("Bearer \(sessionToken)", forHTTPHeaderField: "Authorization")

    URLSession.shared.dataTask(with: request) { data, response, error in
      DispatchQueue.main.async {
        if let error = error {
          callback.registerDidFail(error: error)
          return
        }
        let status = (response as? HTTPURLResponse)?.statusCode ?? 0
        guard status == 200, let data = data,
              let body = try? JSONDecoder().decode(TokenResponse.self, from: data) else {
          callback.registerDidFail(error: TokenError.badStatus(status))
          return
        }
        callback.register(withJWT: body.token)
      }
    }.resume()
  }

  func clientDidStart(_ client: SinchClient) {
    guard clientStartedCallback != nil else { return }
    clientStartedCallback(nil)
    clientStartedCallback = nil
  }

  func clientDidFail(_ client: SinchClient, error: Error) {
    guard clientStartedCallback != nil else { return }
    clientStartedCallback(error)
    clientStartedCallback = nil
  }
}
```

> **Note:** The backend signs the token (see [`registration-token-server.mjs`](../assets/registration-token-server.mjs)) for the user ID tied to the caller's authenticated session. Never put the Application Secret in the app bundle, `Info.plist`, or Keychain defaults.

## Push Notifications (APNs)

Upload your APNs signing key to your Sinch application configuration. See [configuring APNs](https://developers.sinch.com/docs/in-app-calling/ios/push-notifications.md#configuring-an-apns-authentication-signing-key) for details. Expired certificates cause silent failures.

## Enable Logging (Optional)

```swift
import OSLog
import SinchRTC

SinchRTC.setLogCallback { (severity: SinchRTC.LogSeverity,
                               area: String,
                                msg: String,
                                  _: Date) in
  os_log("%{public}@", log: .sinchOSLog(for: area), type: severity.osLogType, msg)
}
```

## Key Points

- `environmentHost` is the REST API endpoint the SDK targets (`ocra.api.sinch.com` for production)
- `userId` is the user identifier registered within your application
- `SinchClient` is a **singleton per user session** — create one instance and retain it for the entire app lifetime
- The `clientRequiresRegistrationCredentials` callback fires on start and when the registration TTL nears expiry
- **Never embed the Application Secret in client-side code** — generate JWTs on your backend
- The Objective-C SDK is also available

## Links

- [In-App Calling Overview](https://developers.sinch.com/docs/in-app-calling/overview.md)
- [iOS Getting Started: Create App](https://developers.sinch.com/docs/in-app-calling/getting-started/ios/create-app.md)
- [iOS First Time Setup](https://developers.sinch.com/docs/in-app-calling/ios/first-time-setup.md)
- [iOS Push Notifications](https://developers.sinch.com/docs/in-app-calling/ios/push-notifications.md)
- [SDK Downloads](https://developers.sinch.com/docs/in-app-calling/sdk-downloads.md)
- [Reference Applications (GitHub)](https://github.com/sinch/rtc-reference-applications/tree/master/ios)
