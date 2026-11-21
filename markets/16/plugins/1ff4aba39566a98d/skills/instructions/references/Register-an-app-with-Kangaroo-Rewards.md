# How to Register an OAuth2 App with Kangaroo Rewards

In this tutorial, we will walk you through the process of registering an OAuth2 application within the Kangaroo Rewards Developer Portal. Registering an OAuth2 app is essential for enabling secure and authorized access to the API's features and functionalities.

**Objective:**
Learn how to register an OAuth2 application with Kangaroo Rewards to enable secure API interactions and obtain a client ID and client secret.

**Prerequisites:**
- A registered business account with Kangaroo Rewards.
- Basic understanding of OAuth2 and API authentication.

## Step-by-Step Instructions

### Step 1: Access the Kangaroo Rewards Developer Portal

First, navigate to the Developer Portal and register or log in to your Kangaroo Rewards developer account.

- Open your web browser and go to the [Developer Portal](https://api.kangaroorewards.com/developers/register).
- Register or Log in with your developer account credentials.

### Step 2: Navigate to the OAuth2 App Registration Page

Once logged in, find the section for managing OAuth2 applications.

1. Click on "Applications" in the navigation menu.
2. Select "Register a new application" to start the registration process.

### Step 3: Fill in the App Registration Form

Provide the necessary details about your application.

* **Application Name:** Enter a name for your application. This should be a unique identifier for your app, something users will recognize and trust.
* **Grant Type:** Select the desired grant type depending on the authentication flow you would like to implement.
* **Authorization callback URL:** Enter the URI to which the API will redirect after authentication. Ensure these URL is correct and secure.
* **Description:** Optionally, provide a description of your application and its purpose.

> IMPORTANT
>
> OAuth2 is a powerful authorization framework that provides several grant types, each designed for specific use cases. Understanding these grant types and their appropriate use cases is essential for implementing secure and effective authentication mechanisms. Here are the currently supported OAuth2 grant types in Kangaroo Rewards API and when to use each.
>
> - **Authorization Code Grant**
The Authorization Code grant is the most commonly used OAuth2 flow. It involves an intermediary step where an authorization code is obtained and then exchanged for an access token. It usually requires a web server and it involves redirecting the user to a URL in a browser.
>
> Use Case: This flow is ideal for server-side applications where the client can securely handle secret keys. It is widely used for web applications where the client can securely store the client secret.
>
> - **Password Credentials Grant**
The Password Credentials grant type allows the client to obtain an access token by directly using the user's credentials (employee or business admin).
>
> Use Case: This flow is suitable for trusted applications where the client can securely handle and protect the user's credentials. It is typically used in first-party applications, Point of Sale (POS) Systems or mobile apps.
>
> `Ensure that you are using the correct flow based on the configured Grant Type for your OAuth client.`

### Step 4: Submit the Registration Form

After filling in the required details, submit the registration form.

1. Review the information to ensure accuracy.
2. Click "Register Application" to complete the registration.

### Step 5: Retrieve Client ID and Client Secret

Upon successful registration, you will be provided with a Client ID and Client Secret. These are essential for the OAuth2 flow.

* **Client ID:** This is a public identifier for your app.
* **Client Secret:** This is a confidential secret used to authenticate your app. Store it securely and do not expose it in your code or share with anyone.

### Step 6: Get Your Application Approved

Contact Kangaroo Rewards support to get your application approved, providing the application name or Application Client ID (never share the client secret). Also ask for the X-Application-Key for your registered business.

> NOTE:
> An API agreement must be signed and your application **approved** before using the API.

### Step 7: Configure Your Application

Use the Client ID and Client Secret to configure your application for OAuth2 authentication.

1. Add the Client ID and Client Secret to your application's configuration file or environment (.env) file.
2. Implement the OAuth2 flow in your application. This typically involves redirecting users to the authorization URL, obtaining an authorization code, and exchanging it for an access token.

### Step 8: Test the OAuth2 Flow

Ensure everything is set up correctly by testing the OAuth2 authentication flow.

1. Redirect users to the authorization URL:
   ```bash
   https://api.kangaroorewards.com/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=code&scope=admin
   ```
2. After users authenticate and authorize your app, they will be redirected to the specified redirect URI with an authorization code.
3. Exchange the authorization code for an access token:
   ```bash
   curl -v -X POST https://api.kangaroorewards.com/oauth/token \
   -H "Accept: application/x-www-form-urlencoded" \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -H "X-Application-Key: YOUR_APPLICATION_KEY." \
   -d "grant_type=authorization_code \
        &code=AUTHORIZATION_CODE\
        &client_id=YOUR_CLIENT_ID\
        &client_secret=YOUR_CLIENT_SECRET\
        &redirect_uri=YOUR_REDIRECT_URI \
        &scope=admin"

## Conclusion

By following these steps, you can successfully register an OAuth2 application with the Kangaroo Rewards API. This enables secure and authorized access to the API, allowing your application to interact with Kangaroo Rewards' API seamlessly.

## Best Practices
- Store your Client Secret securely and never expose it in your code or public repositories.
- Use HTTPS for all redirect URIs to ensure secure communication.
- Regularly review and update your application's permissions and scopes to maintain security.

## Additional Resources
- [Kangaroo Rewards API Reference](https://api.kangaroorewards.com/docs/business.html)
- [Build Your First App](https://api.kangaroorewards.com/docs/business.html#header-build-your-first-app-following-these-steps)
- [OAuth2 Overview](https://oauth.net/2/)
- [Securely Using OAuth2](https://tools.ietf.org/html/rfc6819)

## Troubleshooting
- Incorrect Authentication Flow. A common issue is using the wrong authentication flow for the OAuth client.
  - If the OAuth client's Grant Type is set to Authorization Code in the developer portal, you should implement the [OAuth - Web Application Flow](https://api.kangaroorewards.com/docs/business.html#header-oauth-web-application-flow). This flow is typically used for web applications where the client can securely store the client secret and it involves a redirect.
   - If the OAuth client's Grant Type is set to Password Grant, you should implement the [Password Credentials Grant Flow](https://api.kangaroorewards.com/docs/business.html#header-oauth-password-credentials-grant). This flow is used for trusted applications, such as native mobile apps or backend services, where the client can securely store the client credentials.

Ensure that you are using the correct flow based on the configured Grant Type for your OAuth client.
- Ensure the redirect URIs match exactly what you registered.
- Double-check your Client ID and Client Secret for any typos.
- Review the error messages from the API to understand and resolve issues.
