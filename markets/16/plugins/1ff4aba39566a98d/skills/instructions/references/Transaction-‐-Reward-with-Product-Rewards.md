# Reward Transaction with Attaching Product Rewards

In this tutorial, you will learn how to reward the customer with attaching product rewards through the Kangaroo Rewards API. After the reward is completed, a new transaction will be created.

**Objective:** To demonstrate the process of rewarding customers with product rewards (A La Carte) via the Kangaroo Rewards API and automatically generating new transactions upon completion.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)
* Retrieve and prepare product reward IDs by listing available options through our [Product Rewards API](https://github.com/kangaroorewards/api-docs/wiki/Product-Rewards-%E2%80%90-List)

## Step-by-Step Instructions

### Step 1: Set up your environment with issuing an access token
First, ensure you have your API access key and X-Application-Key from Kangaroo Rewards. This key is necessary for authenticating your API requests.

```bash
export ACCESS_KEY="YOUR_ACCESS_KEY_HERE"
export APPLICATION_KEY="YOUR_APPLICATION_KEY_HERE"
```

For instructions on issuing an access token, please refer to [this tutorial link.](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

### Step 2: List product rewards

To retrieve a list of product rewards, make a GET request to the appropriate endpoint, including the necessary information.

```bash
curl -X GET "https://api.kangaroorewards.com/product-rewards" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
```

### Step 3: Create a reward transaction with attaching the product rewards

To create a reward transaction, make a POST request to the appropriate endpoint, including the necessary information.

```bash
curl -X POST https://api.kangaroorewards.com/transactions \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-d '{
	"intent": "reward",
	"amount": 50.55,
	"branch": {
		"id": "11eb82ae6d3f1ec4b847e2865c66d9cc"
	},
	"customer": {
		"email": "test@example.com"
	},
        "product_rewards": [
        {
          "id": 123,
          "quantity": 3
        },
        {
          "id": 124,
          "quantity": 1
        }
    ]
}'
```

- **intent**: reward _(required)_
- **amount**: This field is required when none of the points or visits are present.
- **points**: This field is required when none of the amount or visits are present.
- **visits**: This field is required when none of the amount or points are present.
- **branch.id**: The branch ID that the redemption transaction is associated with _(optional)_.
- **customer.id**: It’s _required_ if the customer email and phone are not present.
- **customer.email**: It’s _required_ if the customer id and phone are not present.
- **customer.phone**: It’s _required_ if the customer id and email are not present.
- **product_rewards**: List of product reward IDs and their quantity _(required)_.
- **product_reward.id**: This field is _required_ and represents the product reward ID. It should be fetched from the product rewards object. Each product reward object has a unique ID, which should be utilized here.
- **product_reward.quantity**: This field determines the quantity of the product reward item purchased and is _required_.

### Step 4: Handle the response appropriately in your code.

## Summary

In this tutorial, we explored how to retrieve and prepare product reward IDs by listing available options through our API. This process is crucial for effectively managing rewards and facilitating transactions for customers. By leveraging our API, users can seamlessly access and organize product rewards, streamlining the reward issuance process and enhancing customer satisfaction.

## Best Practices

- Always store your client secret and access token securely and never expose them in your source code.
- Handle API responses appropriately, including error handling to manage failed requests.
- Limit the number of API requests to avoid exceeding your quota.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [Product Rewards API Reference](https://api.kangaroorewards.com/docs/business.html#product-rewards-get)
- [Create Transaction API Reference](https://api.kangaroorewards.com/docs/business.html#transactions-transaction-post)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.

**Below are examples of errors and explanations for why they occurred**
***



1. **401 - Unauthorized:** This error occurs when the access token is invalid or when the access token is associated with a different scope than required, such as regular user access.

```json
{
  "error": {
    "message": "Unauthenticated.",
    "description": "Unauthenticated.",
    "status_code": 401,
    "link": "https://api.kangaroorewards.com/docs"
  }
}
```

2. **422 - Unprocessable entity:** This error indicates that there are missing required variables or some values are not valid. For example, the amount field is required when none of points or visits are present. Similarly, the points field is required when none of amount or visits are present. Additionally, the visits field is required when none of amount or points are present. Lastly, the selected product_rewards ID is invalid.

```json
{
  "amount": [
    "The amount field is required when none of points / visits are present."
  ],
  "points": [
    "The points field is required when none of amount / visits are present."
  ],
  "visits": [
    "The visits field is required when none of amount / points are present."
  ],
  "product_rewards.0.id": [
    "The selected product_rewards.0.id is invalid."
  ]
}
```
