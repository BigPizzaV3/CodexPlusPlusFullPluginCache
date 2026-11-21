# Customer CRM Fields - Update

In this tutorial, you will learn how to update certain CRM fields for a single customer through the Kangaroo Rewards API.

**Objective:** To demonstrate the process of modifying the customer CRM fields via the Kangaroo Rewards API.

**Prerequisites:**

* Basic understanding of APIs and HTTP requests.
* A registered business account with Kangaroo Rewards.
* An API client like Postman or cURL installed.
* [An OAuth2 App registered with Kangaroo Rewards](https://github.com/kangaroorewards/api-docs/wiki/Register-an-app-with-Kangaroo-Rewards)
* [A valid Access Token](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)
* Enable the CRM fields from the Kangaroo business portal. 
* Retrieve the CRM field attributes by calling the [List API endpoint](https://github.com/kangaroorewards/api-docs/wiki/Customer-CRM-Fields-%E2%80%90-List)

> Note: If the CRM fields are not visible under your account, it indicates that the CSR needs to grant you access to this module.

## Step-by-Step Instructions

### Step 1: Set up your environment with issuing an access token
First, ensure you have your API access key and X-Application-Key from Kangaroo Rewards. This key is necessary for authenticating your API requests.

```bash
export ACCESS_KEY="YOUR_ACCESS_KEY_HERE"
export APPLICATION_KEY="YOUR_APPLICATION_KEY_HERE"
```

For instructions on issuing an access token, please refer to [this tutorial link.](https://github.com/kangaroorewards/api-docs/wiki/Implement-OAuth2-Authentication)

### Step 2: Retrieve CRM fields for a customer

To retrieve the customer's CRM fields, make a GET request to the appropriate endpoint, including the necessary information. Through this call, you can retrieve the CRM `name` attribute from the list object you intend to update for the customer.

```bash
curl -X GET "https://api.kangaroorewards.com/customers/11eb5b4433edf7bfaaffb42e99312ac8/crm-fields" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
```

### Step 3: Retrieve the tags list (Optional)

You can optionally perform the following step if you want to update the tags for the customer. First, list the available tags in our system and retrieve the name attribute from the list object that should be added in the CRM fields.

#### Request

```bash
curl -X GET "https://api.kangaroorewards.com/tags" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
```
#### Response
```json
{
  "data": [
    {
      "id": 247,
      "name": "Red tag",
      "abbreviation": "RT",
      "color": "#0000ff",
      "created_at": "2024-01-01T07:27:13+00:00"
    },
    {
      "id": 246,
      "name": "Black tag",
      "abbreviation": "BT",
      "color": "#0000ff",
      "created_at": "2024-01-01T15:03:37+00:00"
    }
  ]
}
```

### Step 4: Update customer CRM fields

To update the customer's CRM fields, make a PATCH request to the appropriate endpoint, including the necessary information

```bash
curl -X PATCH "https://api.kangaroorewards.com/customers/11eb5b4433edf7bfaaffb42e99312ac8/crm-fields" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
-d '{
	"first_name":"John edited",
	"gender":"male",
	"promotions_mail": true,
  	"custom_field_1": "John custom field 1",
	"custom_field_2": "John custom field 2",
	"custom_field_3": "John custom field 3",
	"custom_field_4": "John custom field 4",
	"tags":[
		{
		  "tag_name":"Red tag"
		},
		{
		  "tag_name": "Black tag"
		}
	]
}'
```

> All the attributes below are optional. However, the payload should contains at least one attribute.

* **first_name**: string
* **gender**: string | 'male' or 'female'
* **promotions_mail**: boolean
* **custom_field_1**: string
* **custom_field_2**: string
* **custom_field_3**: string
* **custom_field_4**: string
* **tags**: array of objects
* **tags.tag_name**: string


### Step 5: Handle the response appropriately in your code

```json
{
  "data": [
    {
      "name": "first_name",
      "label": "First Name",
      "value": "John edited",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": false,
      "display_order": 3
    },
    {
      "name": "last_name",
      "label": "Last Name",
      "value": "Doe",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": false,
      "display_order": 4
    },
    {
      "name": "gender",
      "label": "Gender",
      "value": "male",
      "is_hidden": false,
      "is_required": false,
      "field_type": "select",
      "is_custom_field": false,
      "display_order": 5
    },
    {
      "name": "address",
      "label": "Address",
      "value": "",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": false,
      "display_order": 8
    },
    {
      "name": "promotions_mail",
      "label": "Promotions by Mail",
      "value": true,
      "is_hidden": false,
      "is_required": false,
      "field_type": "checkbox",
      "is_custom_field": false,
      "display_order": 11
    },
    {
      "name": "tags",
      "label": "Tags",
      "value": [
        {
          "tag_name": "Red tag"
        },
        {
          "tag_name": "Black tag"
        }
      ],
      "is_hidden": false,
      "is_required": false,
      "field_type": "multi_select",
      "is_custom_field": false,
      "display_order": 12
    },
    {
      "name": "custom_field_1",
      "label": "Custom Field Label 1",
      "value": "John custom field 1",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": true,
      "display_order": 13
    },
    {
      "name": "custom_field_2",
      "label": "Custom Field Label 2",
      "value": "John custom field 2",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": true,
      "display_order": 14
    },
    {
      "name": "custom_field_3",
      "label": "Custom Field Label 3",
      "value": "John custom field 3",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": true,
      "display_order": 15
    },
    {
      "name": "custom_field_4",
      "label": "Custom Field Label 4",
      "value": "John custom field 4",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": true,
      "display_order": 16
    },
    {
      "name": "custom_field_5",
      "label": "Custom Field Label 5",
      "value": "John custom field 5",
      "is_hidden": false,
      "is_required": false,
      "field_type": "text",
      "is_custom_field": true,
      "display_order": 17
    }
  ]
}
```

## Summary
In this tutorial, we demonstrated how to update the customer CRM fields using the Kangaroo Rewards API. We provided a step-by-step guide on how to make a call to our API endpoint and what are the attributes needed.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [List Customer CRM Fields](https://api.kangaroorewards.com/docs/business.html#customer-crm-fields-customer-crm-fields-collection-get)
- [Update Customer CRM Fields](https://api.kangaroorewards.com/docs/business.html#customer-crm-fields-customer-crm-fields-collection-patch)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.