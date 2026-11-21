# Documents

Verified 2026-09-10. The old Secure File Storage public page does not describe the current Documents product.

Documents is a document-governance product with company and employee spaces.

## Spaces

Four structures exist:
- public company spaces
- private company spaces
- shared employee spaces
- private employee spaces

Public company spaces are visible to active employees. Private company spaces can use reusable access groups. Shared employee spaces are accessible to the employee plus authorised user administrators. Private employee spaces are admin-only unless another person separately has the required access.

## Files and folders

- Upload, download, preview, delete, category, comments, owner and file-size metadata are supported.
- Folders can be nested and inherit space access.
- One file is uploaded at a time.
- Allowed file types: txt, png, pdf, jpg and jpeg.
- Maximum file size: 5 MB.
- Do not claim bulk upload/download/delete, versioning, restore, moving, tags or advanced search.

## Retention and audit

Retention is optional per space. Reusable policies define a duration in months and an action. Delete is irreversible. Archive retains the file for an additional 30 days before deletion.

Audit activity includes upload, delete, download, preview, user-group changes and space changes. There is no general platform-wide customer-visible audit log.

## Security notes

Files use AWS S3 encryption at rest. File access requires an authenticated session and company/access checks. Copied download URLs do not bypass authentication or cross-company checks. Malware scanning is not currently provided.

Migration is manual. Prices are time-sensitive and must be checked live before quoting.
