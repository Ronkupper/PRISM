#!/usr/bin/env bash
# Build the uploadable PRISM plugin package for Claude Desktop's
# "Customize → Plugins → Personal → + → Upload plugin" (a non-marketplace
# install path that bypasses the marketplace entirely).
#
# Requirements enforced by the desktop upload handler (verified against
# anthropics/claude-code #40414 and the Cowork packaging convention):
#   - extension MUST be .zip (the handler rejects .plugin and others)
#   - the plugin CONTENTS must sit at the archive ROOT
#     (.claude-plugin/plugin.json, commands/, skills/ directly) — NOT wrapped
#     in a top-level folder
#   - under 50 MB
#
# Output: PRISM-plugin-<version>.zip at the repo root (gitignored; attach it to
# the matching GitHub Release per RELEASING.md, do not commit it).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_DIR="$ROOT/plugins/prism"
VER="$(python3 -c "import json,sys;print(json.load(open('$PLUGIN_DIR/.claude-plugin/plugin.json'))['version'])")"
OUT="$ROOT/PRISM-plugin-${VER}.zip"

rm -f "$OUT"
( cd "$PLUGIN_DIR" && zip -rq "$OUT" . -x '*.DS_Store' )

# Verify the manifest landed at the archive root (the upload handler looks there).
# Capture the file list first so grep -q closing the pipe early can't trip pipefail.
NAMES="$(unzip -Z1 "$OUT")"
if ! printf '%s\n' "$NAMES" | grep -qx '\.claude-plugin/plugin\.json'; then
  echo "ERROR: .claude-plugin/plugin.json is not at the archive root — aborting." >&2
  exit 1
fi

echo "Built $OUT"
unzip -l "$OUT" | tail -1
