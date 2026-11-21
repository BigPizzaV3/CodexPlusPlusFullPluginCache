<catalog_brief>
name: RegularDemand
full_name: Repeat Purchase
description: Encourage replenishment of products with regular demand.
variant: omnichannel
</catalog_brief>

<trigger_instruction>
<brief>
Brief:
This is a regular demand trigger. The main goal is to stimulate repeat sales of products that are ending and need to be restocked. Communication is carried out by sending up to 3 messages to different channels.
</brief>

<start_trigger>
It should start for repeat purchase segment once a day (any day of week) starting from tomorrow at 12:00, but no more than once a week for the specific contact.
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
