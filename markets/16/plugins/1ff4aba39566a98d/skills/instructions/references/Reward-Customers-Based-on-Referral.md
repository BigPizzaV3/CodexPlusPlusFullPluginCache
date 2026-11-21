## Reward Customers Based on Referral

In this tutorial, you will learn how to reward the referred and referee customers through the Kangaroo Rewards API.

**Objective:** Learn how to reward your customers based on the referral program through the Kangaroo Rewards API.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)
* [Create a referral program](https://github.com/kangaroorewards/api-docs/wiki/Create-Referral-Program)

## Step-by-Step Instructions

### Step 1: Set up your environment with issuing an access token
First, ensure you have your API access key and X-Application-Key from Kangaroo Rewards. This key is necessary for authenticating your API requests.

```bash
export ACCESS_KEY="YOUR_ACCESS_KEY_HERE"
export APPLICATION_KEY="YOUR_APPLICATION_KEY_HERE"
```

For instructions on issuing an access token, please refer to [this tutorial link.](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

### Step 2: Create a customer with attaching the referral program details
To create a new customer with including the referral details, make a POST request to the appropriate endpoint, including the necessary information.

```bash
curl -X POST "https://api.kangaroorewards.com/customers" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
-d '{
  "first_name":"John",
  "last_name": "Doe",
  "email": "john@example.com",
  "referral": {
    "referral_program_id": 1056,
    "referrer_id": "11eaa697ae8f46bd9df9b42e99312ac8"
  }
}'
```

* **first_name**: _Optional_ - The customer's first name.
* **last_name**: _Optional_  - The customer's last name.
* **email**: _Required_ - Only if the customer's phone and country code are not present.
* **phone**: _Required_ - Only if the customer's email is not present.
* **referral**: _Required_ - Array of referral details.
* **referral_program_id**: _Required_ - The active referral program ID.
* **referrer_id**: _Required_ - The customer who has referred someone.

### Step 3: Create a transaction for the referred customer
To create a referral-reward transaction for the referred customer, make a POST request to the appropriate endpoint, including the necessary information.

```bash
curl -X POST "https://api.kangaroorewards.com/transactions" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
-d '{
  "intent": "reward_referral",
  "amount":40.99,
  "customer": {
    "id": "11eaa697ae8f46bd9df9b42e99312ac8"
  }
}'
```

- **intent**: _Required_ - reward_referral
- **amount**: _Required_ - The purchase amount.
- **customer.id**: It’s _required_ if the customer email and phone are not present.
- **customer.email**: It’s _required_ if the customer id and phone are not present.
- **customer.phone**: It’s _required_ if the customer id and email are not present.
- **customer.country_code**: It’s _required_ if the customer phone is present.

### Step 4: Handle the response appropriately in your code.

## Summary
In this tutorial, we demonstrated how to create and reward the customers based on the referral program using the Kangaroo Rewards API. We provided a step-by-step guide, including how to set up referral details. By following these instructions, users can efficiently manage their referral programs and reward customers appropriately.

## Best Practices

- Always store your client secret and access token securely and never expose them in your source code.
- Handle API responses appropriately, including error handling to manage failed requests.
- Limit the number of API requests to avoid exceeding your quota.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [Create Referral Program API Reference](https://api.kangaroorewards.com/docs/business.html#referral-programs-referral-program-post)
- [Create Transaction API Reference](https://api.kangaroorewards.com/docs/business.html#transactions-transaction-post)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.