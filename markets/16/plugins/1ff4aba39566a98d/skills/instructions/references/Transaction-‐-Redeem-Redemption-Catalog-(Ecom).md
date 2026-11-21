# Redeem redemption catalog (Ecom)

In this tutorial, you will learn how to redeem the redemption catalog and get the Ecom integration coupon code through the Kangaroo Rewards API. After the redemption is completed, a new transaction will be created. Currently, this functionality is only applicable to the Shopify integration.

**Objective:** Learn how to redeem the redemption catalog and generate the ecom integration coupon code.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)
* Shopify-Kangaroo Rewards integration is authorized.

##  Redeem redemption catalog

### 1. Authentication
Get an access token or refresh an existing one as explained [here](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication). With the access token, you can start making API calls.

### 2. Get the eCom branch id from the branches API.

```bash
curl -X GET https://api.kangaroorewards.com/branches?include=virtual_branch \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
```
Loop through the branches in the response to find the eCom branch, which has virtual_branch_flag set to true.

### 3. Retrieve the redemption catalogs from the API. 
```bash
curl -X GET  https://api.kangaroorewards.com/customers/<customer_id>/rewards?relationships=branches \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
```

> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.
>- Replace `<cusotmer_id>` with the actual customer id.
>- When redeeming a redemption catalog item, it must be available at the specified branch.

### 4. Make a request to the transaction API endpoint using cURL

```bash
curl -X POST https://api.kangaroorewards.com/transactions \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-D “{
	"intent": "redeem_ecom_coupon",
	"catalog_item": {
		"id": 4,
	},
	"branch": {
		"id": "11eb82ae6d3f1ec4b847e2865c66d9cc"
	},
	"customer": {
		"id": "11eea0e1e994d24d9fede2865c66d9cc"
	}
}”


```

> **Note**: 
> Replace `<access_token>` with the actual access token.
> Replace `<X-Application-Key>` with the actual X-Application-Key.

- **intent**: redeem_ecom_coupon
- **catalog_item.id**: Catalog item ID, get it from step 3. Only can redeem one catalog item at a time.
- **branch.id**: Branch ID is required and must be a virtual branch. When redeeming a redemption catalog, it must be available at the specified branch.
- **customer.id**: It’s required if the customer email and phone are not present.
- **customer.email**: It’s required if the customer id and phone are not present.
- **customer.phone**: It’s required if the customer id and email are not present.


> **Note**: 
>- **customer**: At least one of id, email, phone is present in the request.
>- You will find the ecom_coupon.code from the response, this is the eCom platform's coupon code.

### 5. Handle the response appropriately in your code.

## Conclusion

By following this tutorial, redeeming redemption catalogs will be successfully completed. The corresponding redemption transaction will be created, and the points will be deducted from the customer's balance.

## Additional Resources

- **Official Documentation**: [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- **Community Support**: [Kangaroo Rewards Knowledge Base](https://support.kangaroorewards.com/knowledge)
- **Branches API Reference**: [Branches API Reference](https://api.kangaroorewards.com/docs/business.html#branches-get)
- **Customer Rewards API Reference**: [Customer Rewards API Reference](https://api.kangaroorewards.com/docs/business.html#customer-rewards)
- **Create Transaction Reference**: [Create Transaction API Reference](https://api.kangaroorewards.com/docs/business.html#transactions-transaction-post)

Feel free to reach out to support if you have any questions or need further assistance.



