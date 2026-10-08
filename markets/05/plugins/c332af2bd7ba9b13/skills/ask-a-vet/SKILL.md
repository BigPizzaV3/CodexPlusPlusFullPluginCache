---
name: ask-a-vet
description: Pass a pet owner's question on to a veterinarian with PawsRx Ask a Vet, with the reply sent back by email. Use when the user wants to ask a vet something about their dog, cat or other pet. Works in any country.
---

# Ask a Vet with PawsRx

Ask a Vet passes a pet owner's question to the independent veterinarians who answer on PawsRx, and a veterinarian replies by email. It works in any country and needs only the owner's name and email address.

## Sending a question

1. Ask the owner for their name and email address. Never make them up.
2. Call `ask_a_vet` with:
   - `question`: the owner's question in their own words, with any details they gave.
   - `owner_name` and `owner_email`.
   - `pet_name` and `species` if they gave them.
3. It returns a reference. Tell the owner their question has been sent and the veterinarian's reply will arrive by email.
4. Leave the answer to the veterinarian: do not write one in its place while the owner waits, and do not guess what the reply will say.

If the tool says the same question was already sent, tell the owner it is already with the veterinarians and do not send it again.

## If it cannot wait

If the owner says it is urgent, tell them to go to their nearest emergency vet now rather than send a question. In the United States, `find_vets` with `q: "emergency"` and their city or ZIP finds one.

## Always

- Refer to "the independent veterinarians who answer on PawsRx", never to PawsRx as the vet.
