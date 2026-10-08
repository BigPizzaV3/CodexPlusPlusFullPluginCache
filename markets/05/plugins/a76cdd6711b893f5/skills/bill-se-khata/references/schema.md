# Workbook schema

Use Excel tables with unique names and stable text IDs. Receipts is the document header table; Line_Items is the detail table. Join the remaining tables through Receipt_ID and, where applicable, Line_ID. Never merge cells inside database tables.

The packaged template contains one blank formula row in each table. When appending, add table rows rather than overwriting headers. Preserve formulas, validation, number formats, and conditional formatting.

## Receipts

Table name: ReceiptsTable. One row per source document.

Columns in order:

1. Receipt_ID — text; required internal key
2. Source_File — text
3. Source_Page_Count — whole number
4. Imported_At — datetime
5. Invoice_Date — date
6. Posting_Date — date
7. Financial_Year — formula result such as FY 2026-27, April to March
8. Tax_Period — formula result in yyyy-mm
9. Document_Type — controlled list
10. Invoice_Number — text
11. Supplier_Legal_Name — text
12. Supplier_Trade_Name — text
13. Outlet_Name — text
14. Supplier_GSTIN — text
15. Supplier_Address — text
16. Supplier_State — controlled list or reviewed text
17. Supplier_State_Code — text, preserving leading zero
18. Recipient_Business_Name — text
19. Recipient_GSTIN — text
20. Place_of_Supply — text
21. Supply_Type — Intra-state, Inter-state, or Unknown
22. Currency — default INR
23. Payment_Mode — controlled list
24. Subtotal — currency
25. Discount_Total — currency
26. Taxable_Value — currency
27. CGST_Total — currency
28. SGST_UTGST_Total — currency
29. IGST_Total — currency
30. Cess_Total — currency
31. Other_Charges — currency
32. Round_Off — signed currency
33. Grand_Total — currency
34. Reverse_Charge — Yes, No, or Unknown
35. IRN — text
36. EInvoice_QR_Present — Yes, No, or Unknown
37. Expense_Category — controlled list
38. Business_Purpose — text
39. Cost_Centre — text
40. Food_Business_Use — controlled list
41. ITC_Review_Status — controlled list; default Review required
42. GSTR2B_Match_Status — controlled list
43. Overall_Confidence — decimal from 0 to 1
44. Review_Status — Ready, Needs review, or Blocked
45. Duplicate_Key — formula or deterministic normalized key
46. Duplicate_Flag — Clear or Candidate
47. Arithmetic_Check — Pass, Check, or Insufficient data
48. Extraction_Notes — text

Recommended formula behavior:

- Financial_Year derives from Invoice_Date using the April-to-March Indian financial year.
- Tax_Period derives from Invoice_Date.
- Duplicate_Key combines normalized supplier GSTIN or supplier name, invoice number, invoice date, and grand total. A match is a review candidate, not proof of duplication.
- Arithmetic_Check compares Grand_Total with Taxable_Value + GST components + Cess_Total + Other_Charges + Round_Off, adjusted only for explicitly captured discounts. Use Lists_Config arithmetic tolerance.

## Line_Items

Table name: LineItemsTable. One row per item or separately stated non-tax charge.

Columns in order:

1. Line_ID
2. Receipt_ID
3. Line_Number
4. Item_Description_Raw
5. Item_Description_Normalized
6. Brand_or_Manufacturer
7. Item_Category
8. Food_Business_Subcategory
9. Business_Use
10. HSN_SAC
11. Quantity
12. Unit
13. Unit_Price
14. Gross_Amount
15. Discount_Amount
16. Taxable_Value
17. Tax_Treatment
18. GST_Rate_Total
19. CGST_Rate
20. CGST_Amount
21. SGST_UTGST_Rate
22. SGST_UTGST_Amount
23. IGST_Rate
24. IGST_Amount
25. Cess_Rate
26. Cess_Amount
27. Other_Charge_Amount
28. Line_Total
29. Value_Source
30. Allocation_Method
31. ITC_Review_Status
32. ITC_Review_Reason
33. Extraction_Confidence
34. Needs_Review
35. Review_Reason
36. Notes

Do not force tax-summary amounts into line items. When the receipt has only a rate-wise summary, leave item tax fields blank and capture the printed values in Tax_Summary.

## Tax_Summary

Table name: TaxSummaryTable. One row per receipt and printed tax-rate or HSN/SAC grouping.

Columns: Tax_Summary_ID, Receipt_ID, HSN_SAC, GST_Rate_Total, Taxable_Value, CGST_Rate, CGST_Amount, SGST_UTGST_Rate, SGST_UTGST_Amount, IGST_Rate, IGST_Amount, Cess_Rate, Cess_Amount, Source_Type, Confidence, Needs_Review, Notes.

Source_Type is Printed, Calculated, Allocated, User corrected, or Unknown.

## Vendors

Table name: VendorsTable.

Columns: Vendor_ID, Supplier_Legal_Name, Supplier_Trade_Name, GSTIN, GSTIN_Format_Status, Address, State, State_Code, Default_Expense_Category, First_Seen, Last_Seen, Receipt_Count, Total_Spend, Review_Status, Notes.

Use GSTIN as a matching signal when present, not as the only vendor key. Keep separate vendor records when two receipts use the same brand but clearly different legal entities.

## Review_Queue

Table name: ReviewQueueTable.

Columns: Issue_ID, Receipt_ID, Line_ID, Severity, Field_Name, Extracted_Value, Issue_Type, Issue_Reason, Confidence, Suggested_Action, Corrected_Value, Resolution_Status, Resolved_At, Resolution_Notes.

Create one issue per actionable ambiguity. Severity is High, Medium, or Low. Resolution_Status is Open, Confirmed, Corrected, or Dismissed.

## Audit_Log

Table name: AuditLogTable.

Columns: Event_ID, Timestamp, Action, Receipt_ID, Line_ID, Field_Name, Previous_Value, New_Value, Value_Source, Notes.

Add an Import event for every processed receipt. Add corrections without destroying the previously extracted value.

## Dashboard and Lists_Config

Dashboard is formula-driven from the database sheets. Show total spend, receipt count, captured GST, open reviews, duplicate candidates, monthly spend, category spend, and ITC/GSTR-2B review counts. Do not label captured GST as claimable ITC.

Lists_Config is the visible source of truth for validations and assumptions. It contains document types, payment modes, categories, tax treatments, units, review states, provenance values, confidence thresholds, arithmetic tolerance, and official reference URLs. Do not maintain an authoritative static GST-rate table.

## Validation

- IDs and GSTINs are text.
- Dates are real date values with yyyy-mm-dd display.
- Money uses INR numeric formatting.
- Rates are decimal percentages with 0.00% display.
- Confidence is a decimal from 0 to 1.
- Unknown facts are blank or the controlled value Unknown; do not substitute zero.
- Conditional formatting highlights Needs review, Candidate, Check, low confidence, and unresolved issues.
