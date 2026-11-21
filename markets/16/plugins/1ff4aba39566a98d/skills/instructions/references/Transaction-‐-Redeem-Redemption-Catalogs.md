# Redeem redemption catalogs

In this tutorial, you will learn how to redeem the redemption catalogs through the Kangaroo Rewards API. After the redemption is completed, a new transaction will be created.

**Objective:** Learn how to redeem the redemption catalog and create a redemption transaction by using the Kangaroo Rewards API.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

##  Redeem redemption catalogs

### 1. Authentication
Get an access token or refresh an existing one as explained [here](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication). With the access token, you can start making API calls.

### 2. Retrieve the redemption catalogs from the API. 
```bash
curl -X GET  https://api.kangaroorewards.com/customers/<customer_id>/rewards \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
```

> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.
>- Replace `<cusotmer_id>` with the actual customer id.

### 3. Make a request to the API endpoint using cURL

```bash
curl -X POST https://api.kangaroorewards.com/transactions \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-D “{
	"intent": "redeem",
	"catalog_items": [
		{
			"id": 4,
			"quantity": 1
		},
		{
			"id": 5,
			"quantity": 2
		}
	],
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

- **intent**: redeem
- **catalog_items**: Catalog items array.
- **catalog_items.*.id**: Catalog item ID, get it from step 2.
- **catalog_items.*.quantity**: The number of catalog items to be redeemed.
- **branch.id**: Branch ID is optional. The branch ID that the redemption transaction is associated with.
- **customer.id**: It’s required if the customer email and phone are not present.
- **customer.email**: It’s required if the customer id and phone are not present.
- **customer.phone**: It’s required if the customer id and email are not present.


> **Note**: 
> **customer**: At least one of id, email, phone is present in the request.

### 4. Handle the response appropriately in your code.

## Conclusion

By following this tutorial, redeeming redemption catalogs will be successfully completed. The corresponding redemption transaction will be created, and the points will be deducted from the customer's balance.

## Additional Resources

- **Official Documentation**: [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- **Community Support**: [Kangaroo Rewards Knowledge Base](https://support.kangaroorewards.com/knowledge)
- **Customer Rewards API Reference**: [Customer Rewards API Reference](https://api.kangaroorewards.com/docs/business.html#customer-rewards)
- **Create Transaction Reference**: [Create Transaction API Reference](https://api.kangaroorewards.com/docs/business.html#transactions-transaction-post)

Feel free to reach out to support if you have any questions or need further assistance.



