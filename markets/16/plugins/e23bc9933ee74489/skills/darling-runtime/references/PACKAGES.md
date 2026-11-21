# Bundled packages

Included: core, system, cli, cli-extra, cli-gui-common, cli-python2-common, ffi, CLI developer/GUI common components, GUI, GUI stubs, IOKit daemon, IOSurface, Python 2, PyObjC, Perl, and the small JSC/WebKit common package present in the upstream release bundle.

Omitted for the <100 MB target:

- `darling-ruby` (~7.95 MB)
- `darling-jsc` (~11.59 MB)
- `darling` meta-package (depends on omitted Ruby)
- `darling-extra` meta-package (depends on `darling` and JSC)

The uploaded upstream ZIP is named `debs_20260608.zip`, while the contained DEBs carry version `0.1.20260609~noble`.
