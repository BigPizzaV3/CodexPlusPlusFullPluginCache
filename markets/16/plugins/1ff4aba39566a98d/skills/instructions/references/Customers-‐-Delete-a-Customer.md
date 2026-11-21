# How to Delete a Customer with Kangaroo Rewards API

In this tutorial, we will guide you through the process of deleting a customer using the Kangaroo Rewards API. This operation is essential for managing customer data or to be compliant with data privacy regulations.

When you delete a customer, the following data is deleted:

- First and last name
- Email address
- Phone number
- Gender
- Address
- Language
- Points balance

**Objective:**
Learn how to delete a customer using the Kangaroo Rewards API, from setting up your environment to making authenticated API calls.

**Prerequisites:**
- Basic understanding of APIs and HTTP requests.
- A registered business account with Kangaroo Rewards.
- Client ID and client secret from an OAuth2 application that has been approved.
- An API client like Postman or cURL installed.

## Step-by-Step Instructions

### Step 1: Set up your environment

First, ensure you have your API access key and X-Application-Key from Kangaroo Rewards. This key is necessary for authenticating your API requests.

```bash
export ACCESS_KEY="YOUR_ACCESS_KEY_HERE"
export APPLICATION_KEY="YOUR_APPLICATION_KEY_HERE"
```

### Step 2: Identify the Customer ID

You need the unique identifier (customer_id) of the customer you wish to delete. You can retrieve this information via the API or your customer management system.

### Step 3: Make a DELETE Request to the API

To delete a customer, send a DELETE request to the appropriate endpoint with the `customer_id`.

```bash
curl -X DELETE "https://api.kangaroorewards.com/customers/{customer_id}" \
-H "Authorization: Bearer $ACCESS_KEY" \
-H "X-Application-Key: $APPLICATION_KEY" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json"
```

Replace `{customer_id}` with the actual ID of the customer you want to delete.

> WARNING!
>
> Deleting a customer cannot be undone. It will permanently remove customers which may cause discrepancies in your data.

### Step 4: Handle the Response

The API will respond with a status code indicating the success or failure of the operation. A successful deletion returns a 204 status code.

```bash
response=$(curl -X DELETE "https://api.kangaroorewards.com/customers/{customer_id}" \
-H "Authorization: Bearer $ACCESS_KEY" \
-H "X-Application-Key: $APPLICATION_KEY" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json")

echo "Response: $response"
```

Check the response for any error messages or status codes that indicate issues.

## Conclusion

In this tutorial, we covered how to delete a customer using the Kangaroo Rewards API. By following these steps, you can effectively manage your customer database and maintain compliance with data privacy regulations.

**Best Practices:**
- Be extremely cautious when deleting customers, since this action is irreversible.
- Always verify that you have the correct `customer_id` before making a delete request to avoid accidental data loss.
- Handle API responses appropriately, including error handling to manage failed requests.
- Regularly audit your customer deletion process to ensure compliance with data privacy laws.

**Additional Resources:**
- [Kangaroo Rewards API Reference](https://api.kangaroorewards.com/docs/business.html)
- [Delete Customer API Reference](https://api.kangaroorewards.com/docs/business.html#customers-customer-resource-delete)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

**Troubleshooting:**
- Ensure your Access Token is correct, has not expired, and has the necessary permissions.
- Verify that the `customer_id` you are using exists and is correct.
- Review the error messages returned by the API for clues on what went wrong.
- If a customer has been deleted, a subsequent request to delete that customer would return a 404 Not Found status, as the customer no longer exists in the system.

