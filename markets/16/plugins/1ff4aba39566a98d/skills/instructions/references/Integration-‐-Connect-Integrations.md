# Connect integrations

In this tutorial, you will learn how to create and connect an integration to your business through the Kangaroo Rewards API. The integration can only be connected to the virtual branch. The same integration account can be connected to multiple virtual branches, with each location/store/subaccount connected to one branch.

**Objective:** Learn how to create and connect an integration for your business.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)
* The business has at least one branch with "Virtual Branch Group" checked.

##  Connect integrations

### 1. Authentication
To start, you need an access token. This token authenticates your requests and ensures that your application has permission to access the API. You can obtain it by following the OAuth2 authentication process provided in the [documentation](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication).

### 2. Get the branch id from the branches API.

You must retrieve the branch ID associated with your virtual branch.

```bash
curl -X GET https://integrations.kangarooapis.com/api/v1/branches \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
```

Parameters:
- `<access_token>`: Replace with your actual access token.
- `<X-Application-Key>`: Replace with your application key.

The response will list all branches, and you will need to identify the virtual branch where you want to link your integration. Look for the branch with `virtual_branch_flag` set to true.

### 3. Create an integration 

Next, you will create the integration. An integration must have a name and type.

```bash
curl -X POST https://integrations.kangarooapis.com/api/v1/integrations \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-D '{
  "name": "ABC",
  "type": 1
}'
```

> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.

- **name**: The name you wish to give your integration (e.g., "ABC E-commerce").
- **type**: Set to `1` for a POS/Ecommerce integration.

This step creates a unique integration ID that will be used later to link the integration to your virtual branch. The response will include the newly created `integration_id`.

### 4. Link the integration to the virtual branch

Now, you will link the integration to your virtual branch. For this you'll need some values from the previous steps, `branch_id` and `integration_id` along with some other required attributes.

```bash
curl -X POST https://integrations.kangarooapis.com/api/v1/branch-links \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-D '{
  "shop_id": "1234",
  "branch_id": "11eaa5c938ec36cc9df9b42e99312ac8",
  "account_id": "c36cc9df9",
  "integration_id": 20
}'

```

Example response:
```json
{
  "id": 1,
  "account_id": "string",
  "shop_id": "string",
  "store_name": "string",
  "store_domain": "http://example.com",
  "integration_id": 1,
  "branch_id": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "enabled": true
}
```
Store the `id` returned in the response in a database or configuration; it is also referred to as the `branch_link_id`.

> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.
>- The integration can only be linked to a virtual branch.
>- The same shop id can only be connected to one branch.

- **account_id**: string, required. The account ID from your POS or eCommerce platform.
- **shop_id**: string, required. The unique ID of your POS or eCommerce location.
- **store_name**: string, optional. The name of the store or location.
- **store_domain**: string<uri>. Required for E-commerce platforms only. The domain associated with your eCommerce platform.
- **integration_id**: Integration id from step 3.
- **branch_id**: string, required. The ID of the virtual branch you retrieved earlier that will be linked to this shop.

Linking the integration to the virtual branch allows the system to associate sales data correctly with the respective branch. This is important for accurate reward transactions and reporting.

Additionally, the `branch_link_id` will be used in future API requests like: Create Sales, Create Transactions, Retrieve Offers and Redemptions etc. 

### 5. Handle the response appropriately in your code.

Make sure to handle the API response in your code. You should check for success or error messages and take appropriate actions based on the response received.

## Conclusion

By following this tutorial, you will successfully connect your e-commerce/POS platform to your Kangaroo Rewards business account. This setup allows you to pass sales data to the API, ensuring that reward transactions are accurately associated with the correct branch using the account_id and shop_id.

## Additional Resources

- **Official Documentation**: [Kangaroo Rewards Integration API Documentation](https://kangaroorewards.stoplight.io/docs/integrations-v1/f4e6fa31af431-getting-started)
- **Knowledge Base**: [Kangaroo Rewards Knowledge Base](https://support.kangaroorewards.com/knowledge)
- **Branches API Reference**: [Branches API Reference](https://kangaroorewards.stoplight.io/docs/integrations-v1/3525481219cf3-list-branches)
- **Integration API Reference**: [Integration API Reference](https://kangaroorewards.stoplight.io/docs/integrations-v1/b2207c1eb1dd9-create-new-integration)
- **Branch Link API Reference**: [Branch Link API Reference](https://kangaroorewards.stoplight.io/docs/integrations-v1/8221b4ef1081a-create-branch-link)

Feel free to reach out to support if you have any questions or need further assistance.


