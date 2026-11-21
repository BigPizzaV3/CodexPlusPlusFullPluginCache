"""Silent, read-only optional checkout discovery; authorization belongs to the caller."""
from pathlib import Path
import os


def locate(cwd: Path, home: Path, configured: str | None = None) -> Path | None:
    if configured:
        candidates = [Path(configured).expanduser()]
    else:
        candidates = []
        for parent in (cwd, *cwd.parents):
            if parent.name == "envision_brain":
                candidates.append(parent)
            candidates.append(parent / "envision_brain")
        candidates.append(home / "Documents" / "ENVISION" / "envision_brain")
    for candidate in candidates:
        try:
            root = candidate.resolve(strict=True)
            if ((root / ".git").exists()
                    and (root / "AGENTS.md").is_file()
                    and (root / "README.md").is_file()
                    and (root / "docs").is_dir()):
                return root
        except (OSError, RuntimeError):
            continue
    return None


if __name__ == "__main__":
    try:
        found = locate(Path.cwd(), Path.home(), os.environ.get("ENVISION_BRAIN_PATH"))
        if found is not None:
            print(found)
    except (OSError, RuntimeError):
        pass
