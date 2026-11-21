# Redeem offers

In this tutorial, you will learn how to redeem the offer through the Kangaroo Rewards API. 

**Before you start**
- First, you need to understand the concept of offers. There are four types of offers: Basic Offer (coupon), Points Multiplier, Free Product, Bonus Points. Each offer might have a list of actions for that customer.
- Only basic offers can be redeemed through the API.
- To redeem an offer, we need to get the coupon before redeeming.

**Objective:** Learn how to redeem the offers by using the Kangaroo Rewards API.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

##  Redeem offers

### 1. Authentication
Get an access token or refresh an existing one as explained [here](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication). With the access token, you can start making API calls.

### 2. Get the offers from the API.

```bash
curl -X GET  https://api.kangaroorewards.com/customers/<customer_id>/offers \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
```
> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.
>- Replace `<cusotmer_id>` with the actual customer id.

### 3. Retrieve the available coupons from the API.
```bash
curl -X GET  https://api.kangaroorewards.com/customers/<customer_id>/available-coupons \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
```
> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.
>- Replace `<cusotmer_id>` with the actual customer id.

In the response, you can get the available coupons and the coupon's offer id.

### 4. If there is no coupon for the offer, assign the offer's coupon to the customer through the transactions API endpoint using cURL

```bash
curl -X POST https://api.kangaroorewards.com/transactions \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-D '{
	"intent": "get_coupon",
	"offer": {
		"id": 2305
	},
	"branch": {
		"id": "11eb82ae6d3f1ec4b847e2865c66d9cc"
	},
	"customer": {
		"id": "11eea0e1e994d24d9fede2865c66d9cc"
	}
}'
```
> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.
>- Replace `<cusotmer_id>` with the actual customer id.

- **intent**: get_coupon
- **offer.id**: Offer id
- **branch.id**: Branch ID is optional. The branch ID that the transaction is associated with.
- **customer.id**: It’s required if the customer email and phone are not present.
- **customer.email**: It’s required if the customer id and phone are not present.
- **customer.phone**: It’s required if the customer id and email are not present.


> **Note**: 
- **customer**: At least one of id, email, phone is present in the request.

You can find the coupon id in the response if it's been successfully done.

### 5. Redeem the coupon through the transactions API endpoint using cURL

```bash
curl -X POST https://api.kangaroorewards.com/transactions \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-D '{
	"intent": "claim_coupon",
	"offer": {
		"id": 2305
	},
	"coupon": {
		"id": 20904
	},
	"branch": {
		"id": "11eb82ae6d3f1ec4b847e2865c66d9cc"
	},
	"customer": {
		"id": "11eea0e1e994d24d9fede2865c66d9cc"
	}
}'

```

> **Note**: 
>- Replace `<access_token>` with the actual access token.
>- Replace `<X-Application-Key>` with the actual X-Application-Key.

- **intent**: claim_coupon
- **offer.id**: Offer id.
- **couon.id**: Coupon id.
- **branch.id**: Branch ID is optional. The branch ID that the transaction is associated with.
- **customer.id**: It’s required if the customer email and phone are not present.
- **customer.email**: It’s required if the customer id and phone are not present.
- **customer.phone**: It’s required if the customer id and email are not present.


> **Note**: 
>- **customer**: At least one of id, email, phone is present in the request.

### 6. Handle the response appropriately in your code.

## Conclusion

By following this tutorial, redeeming offer will be successfully completed. The corresponding offer claim transaction will be created.

## Additional Resources

- **Official Documentation**: [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- **Community Support**: [Kangaroo Rewards Knowledge Base](https://support.kangaroorewards.com/knowledge)
- **Customer Offers API Reference**: [Customer Offers API Reference](https://api.kangaroorewards.com/docs/business.html#customer-offers-customer-offer-get)
- **Customer Available Coupons API Reference**: [Customer Available Coupons API Reference](https://api.kangaroorewards.com/docs/business.html#customer-available-coupons-customer-available-coupons-get)
- **Create Transaction Reference**: [Create Transaction API Reference](https://api.kangaroorewards.com/docs/business.html#transactions-transaction-post)

Feel free to reach out to support if you have any questions or need further assistance.


