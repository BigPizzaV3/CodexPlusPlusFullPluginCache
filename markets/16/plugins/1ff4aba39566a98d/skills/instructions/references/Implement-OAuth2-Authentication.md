# How to Implement OAuth2 Authentication
OAuth2 is a widely adopted framework for authorization, enabling applications to access resources on behalf of a user. In this tutorial, we will demonstrate how to implement OAuth2 authentication step by step. By following this guide, you will learn how to register an application, obtain an access token, and make authenticated API calls.

**Objective**: Learn how to implement OAuth2 authentication by registering an application, obtaining an access token, and making authenticated API calls.

**Prerequisites**: 

* Basic understanding of APIs and HTTP requests.
* An API client like Postman or `cURL` installed.
* A registered business account in Kangaroo Rewards.

Kangaroo Rewards API uses OAuth 2.0 for authentication. Follow these steps to implement it:

## Authorization Code Flow

### Step 1: Register Your Application
First, you need to register your application with Kangaroo Rewards (OAuth2 provider) to obtain client credentials.

* **Go to the Kangaroo Rewards developer portal**.
Navigate to the [developer registration page](https://api.kangaroorewards.com/developers/register)

* **Create a new application**.
Fill out the necessary details, such as the application name, description, and redirect URI (the URL to which the OAuth2 provider will send the authorization code).

* **Obtain your client credentials**.
After registration, note down the client ID and client secret provided by the OAuth2 provider. These credentials are necessary for the subsequent steps.

### Step 2: Get your app approved

By default, the application you recently created is **NOT Approved**. Please contact Kangaroo Rewards Support and get the application APPROVED and ask for a `X-Application-Key` before continuing with the Authentication implementation.

### Step 3: Request an Authorization Code
The next step is to request an authorization code from the OAuth2 provider. This code is required to obtain an access token.
It consists of User Authentication and Authorization, the user (Business Admin usually) authenticates with the OAuth2 provider and authorizes the client application to access their account.

* **Construct the authorization URL**.

The URL typically looks like this:
```
https://api.kangaroorewards.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=REQUESTED_SCOPES
```
Replace `YOUR_CLIENT_ID`, `YOUR_REDIRECT_URI`, and `REQUESTED_SCOPES` with your application's details.

Example:
```
https://api.kangaroorewards.com/oauth/authorize?client_id=1234
&redirect_uri=https://example.com/callback
&response_type=code
&scope=admin
```

* **Direct the user to the authorization URL**.
Open the authorization URL in a web browser. The user (employee) will be prompted to authorize your application.

* **Handle the authorization response**.
After the user authorizes the application, they will be redirected to the specified redirect URI with an authorization code included in the query parameters.

### Step 4: Exchange the Authorization Code for an Access Token

Now, you need to exchange the authorization code for an access token.

* **Prepare the token request**.
Use the following cURL command to make a POST request to the token endpoint:

```bash
curl -X POST "https://api.kangaroorewards.com/oauth/token" \
-H "Accept: application/x-www-form-urlencoded" \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "X-Application-Key: YOUR_APPLICATION_KEY" \
-d "grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=YOUR_REDIRECT_URI&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET"
```

Replace `YOUR_APPLICATION_KEY`, `AUTHORIZATION_CODE`, `YOUR_REDIRECT_URI`, `YOUR_CLIENT_ID`, and `YOUR_CLIENT_SECRET` with your application's details.

Example:
```bash
curl -v -X POST https://api.kangaroorewards.com/oauth/token \
   -H "Accept: application/x-www-form-urlencoded" \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -H "X-Application-Key: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
   -d "grant_type=authorization_code \
        &code=def502009ac5c81 \
        &client_id=1234 \
        &client_secret=8fysa8dfds9fj283 \
        &redirect_uri=https://example.com/callback \
        &scope=admin"
```

* **Handle the token response**.
The response will include an access token and potentially a refresh token. Store these tokens securely, as they will be used to authenticate API requests.

### Step 5: Make an Authenticated API Call

With the access token, you can now make authenticated API calls.

* **Construct the API request**.
Use the following cURL command to make an authenticated request:

```bash
curl -X GET "https://api.kangaroorewards.com/customers" \
-H "Accept: Bearer application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json; charset=UTF-8" \
-H "X-Application-Key: Bearer YOUR_APPLICATION_KEY" \
-H "Authorization: Bearer ACCESS_TOKEN"
```

Replace `ACCESS_TOKEN` and `YOUR_APPLICATION_KEY` with the token obtained in the previous step and `X-Application-Key`.

* **Handle the API response**.
The response will contain the requested resource data. Ensure your application processes this data appropriately.

For more info please refer to [API reference](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)

## Password Credentials Flow

The OAuth2 Password Credentials flow allows your application to obtain an access token by exchanging a user's username and password directly. This flow is suitable for trusted applications where the client can securely handle user credentials. In this tutorial, we will demonstrate how to implement the Password Credentials flow step by step.

### Step 1: Register Your Application
See Authorization Code Flow [Step 1](#step-1-register-your-application)

### Step 2: Get your app approved
See Authorization Code Flow [Step 2](#step-2-get-your-app-approved)

### Step 3: Request an Access Token

* **Prepare the Token Request**:
Use the following cURL command to make a POST request to the token endpoint:

```bash
curl -X POST "https://api.kangaroorewards.com/oauth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "X-Application-Key: YOUR_APPLICATION_KEY" \
-d "grant_type=password&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&username=USER_USERNAME&password=USER_PASSWORD&scope=REQUESTED_SCOPES"
```

Replace `YOUR_APPLICATION_KEY`, `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `USER_USERNAME`, and `USER_PASSWORD` and `REQUESTED_SCOPES` with your application's details and the user's credentials.

Example:
```bash
curl --request POST \
  --url https://api.kangaroorewards.com/oauth/token \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header "X-Application-Key: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" \
  --data grant_type=password \
  --data client_id=1234 \
  --data client_secret=8fysa8dfds9fj283  \
  --data username=john@example.com \
  --data password=your-super-password \
  --data scope=admin \
  --data application_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
```

>NOTE:
> The `X-Application-Key` can be passed in the request header or request body (application_key=YOUR_APPLICATION_KEY)

* **Handle the Token Response**:
The response will include an access token. Store this token securely, as it will be used to authenticate API requests.

Example response:

```json
{
    "access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI5ZTk0NTRkYTRmOTY5Y2U2ZTUxMmFlMTRkZTdkMWJhZWQ",
    "refresh_token":"2riNuUlbhlW1MWKb4Jos9FOYgIzz5ZJtK7rQjIgLD",
    "expires_in":3920,
    "token_type":"Bearer"
}
```

### Step 4: Make an Authenticated API Call

With the access token, you can now make authenticated API calls.

* **Construct the API request**.
Use the following cURL command to make an authenticated request:

```bash
curl -X GET "https://api.kangaroorewards.com/customers" \
-H "Accept: Bearer application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json; charset=UTF-8" \
-H "X-Application-Key: Bearer YOUR_APPLICATION_KEY" \
-H "Authorization: Bearer ACCESS_TOKEN"
```

Replace `ACCESS_TOKEN` and `YOUR_APPLICATION_KEY` with the token obtained in the previous step and `X-Application-Key`.

* **Handle the API response**.
The response will contain the requested resource data. Ensure your application processes this data appropriately.

For more info please refer to [API reference](https://api.kangaroorewards.com/docs/business.html#header-oauth-password-credentials-grant)

## Conclusion

In this tutorial, you learned how to implement the OAuth2 Password Credentials and Authorization Code flow by obtaining an access token using a user's credentials and making authenticated API calls.

## Best Practices

* **Secure Your Client Credentials**: Never expose your client ID and client secret in client-side code or public repositories.
* **Use HTTPS**: Always use HTTPS to ensure that all data is encrypted during transmission.
* **Refresh Tokens**: Implement token refresh mechanisms to handle token expiration gracefully.
* **Minimize Scopes**: Request only the permissions necessary for your application to reduce security risks.

## Troubleshooting

### 400 Error Code
When you encounter a 400 error code during the OAuth2 authentication process, there are a few possible issues that you should consider:

* **Incorrect Authentication Flow**: A common cause of a 400 error is using the wrong authentication flow for the OAuth client.
  * If the OAuth client's Grant Type is set to **Authorization Code** in the developer portal, you should implement the [OAuth - Web Application Flow](https://api.kangaroorewards.com/docs/business.html#header-oauth-web-application-flow). This flow is typically used for web applications where the client can securely store the client secret and it involves a redirect.
  * If the OAuth client's Grant Type is set to **Password Grant**, you should implement the [Password Credentials Grant Flow](https://api.kangaroorewards.com/docs/business.html#header-oauth-password-credentials-grant). This flow is used for trusted applications, such as native mobile apps or backend services, where the client can securely store the client credentials.

Ensure that you are using the correct flow based on the configured Grant Type for your OAuth client.

* **Invalid Client Credentials**: Another possible cause of a 400 error is the use of invalid client credentials (client ID and client secret). Double-check that you are using the correct client ID and client secret, and that they have been correctly configured in your application.

* **Invalid User Credentials**: When getting the following error message: "The user credentials were incorrect" it means the username/email or password provided are incorrect. Double-check that the username or password values you entered are correct. Ensure that the credentials belong to an employee with Business Admin privileges, not a developer.

* **Scope Issues**: The 400 error can also occur if the requested scopes are not valid or are not granted to the OAuth client. Ensure that the scopes you are requesting are correctly defined and that the OAuth client has been granted the necessary permissions.

* **Redirect URI Mismatch**: If the redirect URI used in your application does not match the one configured for the OAuth client, you may encounter a 400 error. Verify that the redirect URI in your application matches the one registered in the OAuth provider's settings (Developer Portal).

### 401 Error Code

* **Unauthorized**: Ensure the access token is included in the Authorization header is correct and has not expired.

# Additional Resources

[Kangaroo Rewards API Reference](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)

[Authorization-vs-Authentication](https://www.oauth.com/oauth2-servers/openid-connect/authorization-vs-authentication/)

[Postman API Client](https://www.postman.com/)

[cURL Documentation](https://curl.se/)

