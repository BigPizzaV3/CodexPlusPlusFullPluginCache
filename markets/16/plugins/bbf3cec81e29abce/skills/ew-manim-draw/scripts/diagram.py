"""Version-dispatched EW Diagram CLI; retain schema 0.4 behavior."""
import json, sys
from pathlib import Path
if __name__ == '__main__':
    if len(sys.argv) > 1 and Path(sys.argv[1]).is_file() and json.loads(Path(sys.argv[1]).read_text()).get('schema_version') == '0.5':
        from guided import main
    else:
        from diagram_v04 import main
    main()
else:
    from diagram_v04 import validate, layout, make_html, svg
