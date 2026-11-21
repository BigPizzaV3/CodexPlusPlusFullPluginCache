<catalog_brief>
name: ReducedPriceCart
full_name: Discount on Items in Cart
description: Encourage purchase when prices drop on items added to the cart.
variant: omnichannel
</catalog_brief>

<trigger_instruction>
<brief>
Brief:
This is a trigger for reducing the price of a product added to the cart. The main goal is to stimulate the customer to complete the purchase by motivating him with a discount that appeared on the products in the cart. Communication is carried out by sending up to 3 messages to different channels.
</brief>

<start_trigger>
It should start for discount cart items segment once a day (any day of week) starting from tomorrow at 09:00, but no more than once a week for the specific contact.
</start_trigger>

<generation_plan>
The main flow should follow:
Start by sending a web push
Next step, send an email
Wait 24 hours
Send SMS, only when this channel and a valid message are available in the selected Reteno account
End of script
</generation_plan>
</trigger_instruction>
