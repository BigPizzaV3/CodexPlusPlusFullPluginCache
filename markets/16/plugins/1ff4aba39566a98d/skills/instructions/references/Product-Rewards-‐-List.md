# Listing Product Rewards with Kangaroo Rewards API

In this tutorial, we will demonstrate how to retrieve a list of product rewards using the Kangaroo Rewards API and explain the purpose of each attribute in the response.

**Objective:** Learn how to list all product rewards using the Kangaroo Rewards API and understand the applicable filters.

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

### Step 2: List product rewards

To retrieve a list of product rewards, make a GET request to the appropriate endpoint, including the necessary information.

```bash
curl -X GET "https://api.kangaroorewards.com/product-rewards" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json" \
```

### Step 3: Include relationships in the response (Optional)

You can include additional related data in the response by specifying relationships in the URL. For example, to include product details in the response:

```bash
curl -X GET "https://api.kangaroorewards.com/product-rewards?relationships=product" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json"
```

### Step 4: Use filters to refine your query (Optional)

You can apply filters to the query string to retrieve specific products. The only applicable filter at the moment is the product SKU:

```bash
curl -X GET "https://api.kangaroorewards.com/product-rewards?relationships=product&products.product_sku=eq%7CSKU123" \
-H "Authorization: Bearer <ACCESS_KEY>" \
-H "X-Application-Key: <APPLICATION_KEY>" \
-H "Accept: application/vnd.kangaroorewards.api.v1+json;" \
-H "Content-Type: application/json"
```

### Step 5: Understanding the response

The response will contain a list of product rewards with various attributes. Here's an example response and an explanation of each attribute:

```json
{
  "data": [
    {
      "id": 123,
      "points": 50,
      "product": {
        "id": 456,
        "title": "Sample product",
        "description": "Description of the product",
        "images": [],
        "product_sku": "SKU123",
        "actual_price": 19.99,
        "real_price": 19.99,
        "terms_conditions": "",
        "link": "",
        "product_languages": [
          {
            "language_id": 1,
            "title": "Sample product",
            "description": "Description of the product",
            "terms_conditions": null,
            "link": null,
            "language": {
              "id": 1,
              "abbreviation": "en",
              "name": "English"
            }
          }
        ]
      }
    }
  ],
  "links": {
    "first": "https://api.kangaroorewards.com/product-rewards?page=1",
    "last": null,
    "prev": null,
    "next": null
  },
  "meta": {
    "current_page": 1,
    "from": 1,
    "path": "https://api.kangaroorewards.com/product-rewards",
    "per_page": 15,
    "to": 1
  }
}
```
* **id:** The unique identifier for the product reward.
* **points:** The number of reward points associated with the product. These points are awarded to the customer upon completing a transaction involving the product.
* **product.id:** The unique identifier for the product.
* **product.title:** The title or name of the product.
* **product.description:** A description of the product (if available).
* **product.images:** An array containing URLs or references to images of the product.
* **product.product_sku:** The stock keeping unit (SKU) assigned to the product.
* **product.actual_price:** The original price of the product before any discounts or promotions.
* **product.real_price:** The current price of the product after applying any discounts or promotions.
* **product.terms_conditions:** Any terms and conditions associated with the product (if provided).
* **product.link:** A link or URL associated with the product (if applicable).
* **product.product_languages:** An array containing language-specific details of the product, such as title, description, terms_conditions, and link, for different languages supported.

## Summary

By following these steps, you can effectively retrieve and filter product rewards using the Kangaroo Rewards API, as well as understand the detailed information included in the API response.

## Best Practices

- Always store your client secret and access token securely and never expose them in your source code.
- Handle API responses appropriately, including error handling to manage failed requests.
- Limit the number of API requests to avoid exceeding your quota.

## Additional Resources
- [Kangaroo Rewards API Documentation](https://api.kangaroorewards.com/docs/business.html)
- [Implement Authentication](https://api.kangaroorewards.com/docs/business.html#header-implement-authentication)
- [Access Kangaroo API](https://api.kangaroorewards.com/docs/business.html#header-access-kangaroo-rewards-rest-api)
- [Product Rewards API Reference](https://api.kangaroorewards.com/docs/business.html#product-rewards-get)
- [cURL](https://curl.se/)

## Troubleshooting
- Ensure your Access Token is correct, isn't expired and has the necessary permissions.
- Check the API endpoint URLs for any typos.
- Double check all the required headers are present including Content-Type and Accept.
- Review the error messages returned by the API for clues on what went wrong.