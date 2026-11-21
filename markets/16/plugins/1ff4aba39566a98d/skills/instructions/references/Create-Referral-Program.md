# Create Referral Program

In this tutorial, you will learn how to create a referral program through the Kangaroo Rewards API.

**Objective:** To demonstrate the process of creating a referral program via the Kangaroo Rewards API.
> Note: It's important to note that modifying the email template is restricted to updates made solely from the Kangaroo business portal.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

## Step-by-Step Instructions

### Step 1: Set up your environment with issuing an access token
First, ensure you have your API access key and X-Application-Key from Kangaroo Rewards. This key is necessary for authenticating your API requests.

```bash
export ACCESS_KEY="YOUR_ACCESS_KEY_HERE"
export APPLICATION_KEY="YOUR_APPLICATION_KEY_HERE"
```

For instructions on issuing an access token, please refer to [this tutorial link.](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

### Step 2: Create a referral program

To create a referral program, make a POST request to the appropriate endpoint, including the necessary information.
> Note: When creating a new referral program, the previous active referral program will be deactivated, and the new one will be enabled.

```bash
curl -X POST "https://api.kangaroorewards.com/referral-programs" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
-d '{
  "cond_min_amount": 30.00,
  "referee_earns": 50,
  "referer_earns": 10,
  "expires_in": 35,
  "enabled": true,
  "link_referral_enabled": true,
}'
```

* **cond_min_amount**: _Required_ - The minimum purchase amount condition.
* **expires_in**: _Required_ - Expires in number of days.
* **referee_earns**: _Required_ - How many points the referee earns.
* **referer_earns**: _Required_ - How many points the referer earns.
* **link_referral_enabled**: _Optional_ - It indicates whether the referral link is enabled, it's true be default.
* **enabled**: _Optional_ - It indicates whether the referral program is enabled, it's true be default.

### Step 3: Handle the response appropriately in your code.
Response sample:

```json
{
  "data": {
    "id": 1370,
    "rule_name": "BACKEND_REFERRAL_RULES_PURCHASE",
    "cond_min_amount": 30,
    "referee_earns": 50,
    "referer_earns": 10,
    "expires_in": 35,
    "enabled": true,
    "link_referral_enabled": true,
    "referral_link": ""
  }
}
```

## Summary
In this tutorial, we demonstrated how to create a referral program using the Kangaroo Rewards API. We provided a step-by-step guide, including how to set up referral details. Additionally, we highlighted that modifying the email template must be done exclusively through the Kangaroo business portal. By following these instructions, users can efficiently manage their referral programs.

## Best Practices

- Always store your client secret and access token securely and never expose them in your source code.
- Handle API responses appropriately, including error handling to manage failed requests.
- Limit the number of API requests to avoid exceeding your quota.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [Create Referral Program API Reference](https://api.kangaroorewards.com/docs/business.html#referral-programs-referral-program-post)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.
