# Mapping a menu document onto Liftory

## Meals, options, and groups

- A meal heading is a slot. Each numbered or named alternative under it is an option. A meal printed as one block with no alternatives gets a single option, named so that it does not repeat the meal's name.
- A run of rows with no marker is a group the client eats in full (chooseOne false). A marker that says to pick one of the rows makes a chooseOne group.
- Where no marker says which rows belong together, the document's borders, boxes, and colours decide. A row in its own box after a pick-one block is a separate group.
- Leave a group's category empty unless the document states it, so Liftory infers it from the foods.

## Notes and flags

- A comment beside one row is that item's note; beside a run of rows, the group's note; about the whole option, the option's prepNote; printed under the meal heading for every option, the slot's note.
- A row marked optional gets optional true, and the marker is removed from the item name.
- A list ranked from best to worst marks its first item preferred.
- Supplementation, moderation lists, and reminders that apply to the whole menu go in the menu's rules, as markdown with the coach's wording and line breaks.

## Amounts and foods

- The amount is the coach's text as written, in their units. grams is filled only when the text gives a weight, or a unit whose weight the document itself prints. When converting a unit needs a weight the document does not give, ask, or leave grams empty and put it on the decisions list.
- Two foods printed as one choice are one item with components, each with its own amount, grams, and foodId.
- A row that names a category with several example foods takes the first named food when the foods are nutritionally alike, and no foodId when they are not. A brand product takes the matching generic catalog food. Each of these goes on the decisions list.

## Weekly limits

- A cap on how often an option or a food may be eaten per week is a weekly limit: scoped to the meals it names, counting the options or items it names, in the order the document lists them.
