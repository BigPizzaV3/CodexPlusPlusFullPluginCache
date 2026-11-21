---
name: schedule-test-drive
description: Check test drive availability and schedule a test drive at a BMW dealer
---

# Schedule a BMW Test Drive

Help users book a test drive at a BMW dealership.

## Available Tools

- `get-test-drive-availability` — Check available test drive time slots at a dealer
- `submit-test-drive-request` — Submit a test drive booking request

## Workflow

1. Ensure the user has selected a dealer (use `find-dealers` if needed)
2. Use `get-test-drive-availability` to show available time slots
3. Let the user pick a preferred date and time
4. Collect required contact information for the booking
5. Use `submit-test-drive-request` to submit the reservation

## Information Needed

- **Dealer** (required): Which dealership
- **Date/Time** (required): Preferred appointment slot
- **Contact info** (required): Name, phone, email
- **Vehicle interest** (optional): Which model they want to test drive

## Tips

- Suggest test driving a vehicle the user has been exploring in inventory or has configured
- Confirm all details before submitting the request
- Let users know they'll receive a confirmation from the dealer
- If no slots are available, suggest alternative dates or nearby dealers
