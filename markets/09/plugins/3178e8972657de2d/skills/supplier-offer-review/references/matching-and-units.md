# Matching identifiers and reading units

## Identifier hygiene

Before comparing identifiers across two files, normalise both sides the same way:

- **Scientific notation.** A barcode shown as `9.31E+12` has lost digits. It
  cannot be recovered from the cell; ask for the file with that column formatted
  as text.
- **Leading zeros.** `0093045123456` and `93045123456` may be the same code once
  stored as a number. Compare as text, padded to a standard length.
- **GTIN lengths.** UPC-A (12 digits), EAN-13 (13) and GTIN-14 (14) can encode
  the same product. Left-pad to 14 digits with zeros before comparing. A GTIN-14
  with a leading digit other than 0 usually identifies a carton or inner, not the
  each; match it to the pack, not the unit.
- **Whitespace and case.** Trim spaces, including non-breaking spaces, and
  compare supplier codes case-insensitively.
- **Check digit.** The last digit of a GTIN is a check digit. A code that fails
  the check is a typo or a truncated value; flag it rather than matching it.

## Match order

1. GTIN/barcode, exact after normalising.
2. Supplier code, exact, for the same supplier.
3. Manufacturer part number, exact, with the brand agreeing.
4. Description only as a candidate list for the buyer to confirm.

Report how many lines matched on each key. If several of your SKUs share one
identifier, say so and do not pick one silently.

## Numbers in part codes

A trailing number in a part code (`ABC123-24`) is not reliably a pack size. In
many ranges it is a specification: a gap, a temperature, a volume, a length.
Read pack size from a pack column or an explicit phrase ("box of 24", "6 pack"),
or ask. Never derive a quantity from a part-code suffix.

## Units checklist

| Field | Check |
| --- | --- |
| Demand | Per week, month or period? How many weeks in the period? |
| Lead time | Days, weeks or months? Order to dispatch, or order to shelf? |
| Cost | Per each, per inner or per carton? Ex or inc GST? Which currency? |
| Available | Units or cartons? Exact or a floor ("100+", "50+")? |
| Carton qty | Units per carton (usual) or number of cartons (rare; confirm)? |
| MOQ | Units, cartons or order value? Per line or per order? |
| ETA | When the supplier ships, or when it reaches you? |

A supplier's ETA is when their stock arrives with them. It says nothing about an
order you have placed.
