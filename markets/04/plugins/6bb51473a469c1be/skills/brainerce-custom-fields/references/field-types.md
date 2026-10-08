# The fifteen custom-field types

Distilled from the Brainerce merchant help centre. Pick the type before the
values are entered: changing a definition's type afterwards means re-entering
every value on every product.

| Type | Holds | Reach for it when | Filterable |
|---|---|---|---|
| **Text** | One line | A short label, a supplier SKU, a tagline, engraving text | No |
| **Long Text** | A textarea | Care instructions, warranty terms, anything a paragraph long | No |
| **Number** | A numeric value | Wattage, capacity, thread count. ⛔ Cannot be filtered; if shoppers must narrow by it, use a Select with bands | No |
| **Yes/No** | A boolean | One claim per field: organic, dishwasher safe, kosher | **Yes** |
| **Date** | A date | Expiry, release date | No |
| **Date and Time** | A timestamp | Event start, an availability window | No |
| **JSON** | A structured blob | A full spec sheet, a nested config the storefront parses | No |
| **URL** | A validated address | Size guide, video, 3D model | No |
| **Colour** | A hex colour | A swatch the storefront paints | No |
| **Dimension** | A length or size with a unit | 12.5cm by 7cm | No |
| **Weight** | A weight with a unit | 1.2kg | No |
| **Image** | One image reference | A certification badge, an alternate photo | No |
| **Gallery** | Several image references | Extra product photos beyond the main gallery | No |
| **Select** | One value from a list | Condition, country of origin, metal colour | **Yes** |
| **Multi-select** | Several values from a list | Certifications, materials, allergens | **Yes** |

For **Select** and **Multi-select**, the choices go in **Allowed Values** on the
definition, before saving.

## Values on the wire

A value arrives on the product as an entry in the `metafields` array:

```
{ id, definitionId, definitionKey, definitionName, type, value, variantId }
```

`value` is a **string** for every type. `variantId` is null for a product-level
value and set when the value belongs to one variant. For Multi-select and
Gallery the string carries a list, so parse by `type` rather than printing it.

The SDK exports `getProductMetafieldValue(product, key)`, which reads by
`definitionKey` and parses numbers, booleans and dates into real types. Prefer it
over reading `value` by hand.

## Filtering, precisely

Only Select, Multi-select and Yes/No can carry the **Show in storefront filters**
flag. Once one does, a storefront discovers the filterable set and passes chosen
values back when listing products:

```js
const { definitions } = await brainerce.getPublicMetafieldDefinitions();
const filters = definitions.filter((d) => d.filterable);

const { data: products } = await brainerce.getProducts({
  metafields: { condition: ['Refurbished'], kosher: ['true'] },
});
```

Keys are the definition keys. Values combine **AND across fields, OR within a
field**, so the call above returns products that are Refurbished **and** Kosher.
For Yes/No pass the strings `"true"` and `"false"`.

## Customer Input, precisely

A definition with **Customer Input** on renders as a form input on the product
page. It carries a picker for which products it applies to: all products, or a
named selection. Fields set to "applies to all products" appear at product
creation; product-specific ones can only be assigned after the product is saved.

The shopper's answer is stored as a **line-item detail on the order**, visible in
the order detail view beside the product. It is not a variant, it does not
consume stock, and it does not create a SKU.

⛔ Not the same as **checkout custom fields**, which collect one answer for the
whole order (delivery notes, gift wrapping, a tax id) and are a separate feature
configured elsewhere. If the merchant describes something asked once at the end
rather than per item, it is a checkout field and this skill is the wrong one.

## The product editor, for merchants doing it by hand

Once definitions exist, a **Custom Fields** section appears in the right column
of the product editor, split in two:

- **Product Attributes**: the non buyer-facing fields. Specs, certifications,
  descriptions. Stored on the product and returned through the SDK.
- **Buyer Input Fields**: the Customer Input ones. Only those set to "applies to
  all products" show while creating; the rest appear after the first save.

Values save with the rest of the product, in the same **Save**.
