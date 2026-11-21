# Update Social Media Call to Action

In this tutorial, you will learn how to update a social media call to action through the Kangaroo Rewards API.

**Objective:** To demonstrate the process of updating a social media call to action via the Kangaroo Rewards API.

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

### Step 20: Get Social Media Call to Action List

To get the list of created Social Media Call to Action, make a GET request to the appropriate endpoint, including the necessary information.

```bash
curl -X GET "https://api.kangaroorewards.com/call-to-actions" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
```

```json
{
  "data": [
    {
      "id": 489,
      "enabled": true,
      "points": 100,
      "result_freq": null,
      "result_count": 0,
      "action_freq": null,
      "action_count": 1,
      "action_duration_min": 0,
      "action_duration_unit": null,
      "conditions": null,
      "action_id": 4,
      "created_at": "2024-11-08T09:22:55+00:00"
    },
    {
      "id": 487,
      "enabled": true,
      "points": 0,
      "result_freq": null,
      "result_count": 1,
      "action_freq": null,
      "action_count": 1,
      "action_duration_min": 0,
      "action_duration_unit": null,
      "conditions": null,
      "action_id": 8,
      "created_at": "2024-11-08T08:49:16+00:00"
    },
    {
      "id": 486,
      "enabled": true,
      "points": 25,
      "result_freq": null,
      "result_count": 1,
      "action_freq": null,
      "action_count": 1,
      "action_duration_min": 0,
      "action_duration_unit": null,
      "conditions": null,
      "action_id": 7,
      "created_at": "2024-11-08T08:49:16+00:00"
    },
    {
      "id": 485,
      "enabled": true,
      "points": 5,
      "result_freq": null,
      "result_count": 1,
      "action_freq": null,
      "action_count": 1,
      "action_duration_min": 0,
      "action_duration_unit": null,
      "conditions": null,
      "action_id": 6,
      "created_at": "2024-11-08T08:49:16+00:00"
    },
  ],
}
```

* **call_to_action_id**: _Required_ - The call to action id associated to the desired Social Media Platform.
* **points**: _Required_ - The amount of points to reward for the desired social media CTA.

### Step 3: Update a Social Media Call to Action

To update a Social Media Call to Action, make a PATCH request to the appropriate endpoint, including the necessary information.

```bash
curl -X PATCH "https://api.kangaroorewards.com/call-to-actions/{call_to_action_id}" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
-d '{
  "points": 10
}'
```

* **call_to_action_id**: _Required_ - The call to action id associated to the desired Social Media Platform.
* **points**: _Required_ - The amount of points to reward for the desired social media CTA.

### Step 4: Handle the response appropriately in your code.
Response sample:

```json
{
  "data": {
    "id": 488,
    "enabled": true,
    "points": 100,
    "result_freq": null,
    "result_count": 0,
    "action_freq": null,
    "action_count": 1,
    "action_duration_min": 0,
    "action_duration_unit": null,
    "conditions": null,
    "action_id": 4,
    "created_at": "2024-11-08T09:15:40+00:00"
  }
}
```

## Summary
In this tutorial, we demonstrated how to get the list of all social media call to actions, and update the desired entity using the Kangaroo Rewards API. We provided a step-by-step guide, including how to change the amount of points to reward for the desired social media platform. By following these instructions, users can efficiently manage their Social media Call to Action events.

## Best Practices

- Always store your client secret and access token securely and never expose them in your source code.
- Handle API responses appropriately, including error handling to manage failed requests.
- Limit the number of API requests to avoid exceeding your quota.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.
