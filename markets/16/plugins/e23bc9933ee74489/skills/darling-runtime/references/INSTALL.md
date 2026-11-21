# Installation

Bundled target: Ubuntu 24.04 (Noble), amd64/x86_64.

From this skill directory:

```bash
./assets/install.sh
```

Or manually:

```bash
sudo apt update
sudo apt install -y ./assets/binaries/*.deb
```

`apt` resolves normal Ubuntu host dependencies. The bundle intentionally contains no `darling` meta-package because that meta-package requires the omitted Ruby component.
