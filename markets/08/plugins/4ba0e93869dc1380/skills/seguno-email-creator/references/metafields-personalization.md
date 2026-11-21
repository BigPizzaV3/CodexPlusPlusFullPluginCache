# Metafields Personalization

Use Liquid for customer personalization.

- Customer metafields use the `customer.metafields` prefix, for example `customer.metafields.facts.birthday`.
- `customer.first_name`, `customer.last_name`, and `customer.email` are special cases and do not use the metafields prefix.
- Add fallback text with the `default` filter, for example `{{ customer.first_name | default: "Bob" }}`.
- Insert a discount into the email with `{{ discount.code }}`. If choosing the option, the user must connect a discount in the Seguno editor
