---
name: census-geocode
description: Geocode US address lists to coordinates, census tracts and districts with Excel and CSV downloads.
---
Use `geocode_addresses` for census tract lookup, address to lat long, batch geocoding, or block group lookup. Supply `addresses` as one address per line or CSV text with a header containing Address or Street. It accepts up to 1,000 data rows and 200,000 characters.

Use `find_address_districts` for congressional district by address or state legislative district by address, up to 100 data rows. It adds district codes and names, the boundary session/year, school district and place. It does not return representative names or contact details.

Preserve returned match statuses and notes, especially changed addresses and service errors. Report counts, preview rows, expiring Excel/CSV links, and the source retrieval line. The generated files preserve the original columns; the visible preview contains address fields and geography only. Explain that US Census geocodes are interpolated street points and PO boxes, rural routes or new streets may not match. Coverage is US addresses including DC, Puerto Rico and covered island areas. Do not use these tools for Toronto addresses or driving directions.
