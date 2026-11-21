# Creating and Retrieving Customer Consent with Kangaroo Rewards API

In this tutorial, we will demonstrate how to create and retrieve customer consent using the Kangaroo Rewards API step by step. The Kangaroo Rewards API allows businesses to manage customer loyalty programs, including obtaining and handling customer consents, which are crucial for compliance with data privacy regulations.

**Objective:**
Learn how to create and retrieve customer consent using the Kangaroo Rewards API, from setting up your environment to making authenticated API calls.

**Prerequisites:**
- Basic understanding of APIs and HTTP requests.
- A registered business account with Kangaroo Rewards.
- Client ID and secret from an OAuth2 App approved.
- An API client like Postman or cURL installed.

## Step-by-Step Instructions

### Step 1: Set up your environment

First, ensure you have your API access key and X-Application-Key from Kangaroo Rewards. This key is necessary for authenticating your API requests.

```bash
export ACCESS_KEY="YOUR_ACCESS_KEY_HERE"
export APPLICATION_KEY="YOUR_APPLICATION_KEY_HERE"
```

### Step 2: Create Customer Consent

To create a customer consent, you need to send a POST request to the appropriate endpoint with the necessary customer information.

```bash
curl -X POST "https://api.kangaroorewards.com/customers/{customer_id}/consents" \
-H "Authorization: Bearer $ACCESS_KEY" \
-H "X-Application-Key: $APPLICATION_KEY" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
-d '{
  "allow_sms": false,
  "allow_email": true,
  "allow_push": true
}'
```

### Step 3: Retrieve Customer Consent

To retrieve a customer's consent, send a GET request to the specific endpoint with the customer ID.

```bash
curl -X GET "https://api.kangaroorewards.com/customers/{customer_id}/consents" \
-H "Authorization: Bearer $ACCESS_KEY" \
-H "X-Application-Key: $APPLICATION_KEY" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json"
```

### Step 4: Handle the Response

For both creating and retrieving customer consent, you need to handle the API response appropriately. Below is an example of handling a JSON response in a shell script.

```bash
response=$(curl -X GET "https://api.kangaroorewards.com/customers/{customer_id}/consents" \
-H "Authorization: Bearer $ACCESS_KEY" \
-H "X-Application-Key: $APPLICATION_KEY" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json")

echo "Response: $response"
```

Example Response:
```json
{
  "data": {
    "id": 123,
    "allow_sms": false,
    "allow_email": true,
    "allow_push": true
  }
}
```

## Conclusion

In this tutorial, we covered how to create and retrieve customer consent using the Kangaroo Rewards API. By following these steps, you can ensure compliance with data privacy regulations and manage customer consents efficiently.

## Best Practices
- Always store your client secret and access token securely and never expose them in your source code.
- Handle API responses appropriately, including error handling to manage failed requests.
- Limit the number of API requests to avoid exceeding your quota.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [Customer Consent API Reference](https://api.kangaroorewards.com/docs/business.html#customer-consents)
- [Postman](https://www.postman.com/)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.
