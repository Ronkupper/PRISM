#!/usr/bin/env python3
"""
Translate PRISM lint NDJSON into GitHub Actions workflow-command annotations.

Reads NDJSON findings from the file paths given as arguments (or from stdin if
none) and prints one `::error`/`::warning`/`::notice file=…,line=…::message`
per finding. Annotation-only: this never exits non-zero — the lint step's own
exit code is what gates the build.
"""
import json
import sys


def emit(line: str) -> None:
    line = line.strip()
    if not line:
        return
    o = json.loads(line)
    sev = o.get("severity")
    level = {"error": "error", "warning": "warning"}.get(sev, "notice")
    msg = f'{o["rule"]} ({o["alias"]}): {o["message"]}'
    print(f'::{level} file={o["file"]},line={o["line"]}::{msg}')


def main(argv) -> int:
    if argv:
        for path in argv:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    emit(line)
    else:
        for line in sys.stdin:
            emit(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
