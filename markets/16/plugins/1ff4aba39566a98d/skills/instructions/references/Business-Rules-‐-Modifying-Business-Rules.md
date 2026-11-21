# Modifying Business Rules with Kangaroo Rewards API

Certain business rules can be updated through the API. This tutorial will provide an explanation for the rules that can be updated.

**Objective:** Learn how to update the business rules by using the Kangaroo Rewards API.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

## Update the business rules

### 1. Authentication
Get an access token or refresh an existing one as explained [here](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication). With the access token, you can start making API calls.

### 2. Make a request to the API endpoint using cURL

```bash
curl -X PATCH https://api.kangaroorewards.com/rules \
-H "Authorization: Bearer <access_token>" \
-H "X-Application-Key: <X-Application-Key>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json" \
-H "Content-Type: application/json" \
-d '{
	"reward_ratio": 10,
	"reward_milestone_amount": 1,
	"redemption_ratio": 5,
	"redemption_amount": 1,
	"round_up_points": true,
	"welcome_points": 26,
        "tiers_earning_override": true,
	"tiers_earning_rules": [
		{
			"id": 78,
			"amount": 1,
			"points": 15
		},
		{
			"id": 79,
			"amount": 1,
			"points": 20
		},
		{
			"id": 475,
			"amount": 1,
			"points": 25
		}
	]
}'
```

> **Note**: 
> Replace `<access_token>` with the actual access token.
> If you want to override one of the earning rules based on tiers, all the tier levels earning rules must be passed, and pass tiers_earning_override as true.

- **reward_ratio & reward_milestone_amount**: For each $ **{reward_milestone_amount}** the customer will earn **{reward_ratio}** points.
- **redemption_ratio & redemption_amount**: Each **{redemption_ratio}** points the customer can redeem $**{redemption_amount}** (only apply to the eCom integrations).
- **round_up_points**: Round up earning points. The reward points calculation involves taking the floor value of the amount spent divided by the reward milestone amount, then multiplying by the reward ratio to get the reward points. If the round-up earning points feature is enabled, then round up the calculated reward points.
- **welcome_points**: Customers who sign up at my store will earn **{welcome_points}** points.
- **tiers_earning_override**: Override earning rules based on Tiers. 
- **tiers_earning_rules**: All tier levels earning rules must be passed together.
- **tiers_earning_rules.*.id**: Tier level id.
- **tiers_earning_rules.*.amount & tiers_earning_rules.*.points**: $**{amount}** the customer will earn **{points}** points.


## Conclusion

In this tutorial, we listed all the available updatable business rules through the API and explained the meaning of each rule. By understanding these rules, you can effectively manage and customize your business logic to suit your specific needs. We hope this guide has been helpful and provides clarity on how to utilize the API for updating business rules.

## Additional Resources

- **Official Documentation**: [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- **Community Support**: [Kangaroo Rewards Knowledge Base](https://support.kangaroorewards.com/knowledge)
- **Business Rules Reference**: [Business Rules API Reference](https://api.kangaroorewards.com/docs/business.html#business-rules-business-rules-put)

Feel free to reach out to support if you have any questions or need further assistance.

