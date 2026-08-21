#!/usr/bin/env bash
# Convenience wrapper for stock analysis CLI
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
export MPLBACKEND="${MPLBACKEND:-Agg}"
if [[ ! -x "$ROOT/.venv/bin/python" ]]; then
  echo "Missing .venv. From the repo root run:" >&2
  echo "  uv venv .venv --python 3.12" >&2
  echo "  uv pip install --python .venv/bin/python -r requirements.txt" >&2
  exit 1
fi
# shellcheck disable=SC1091
source .venv/bin/activate
python src/main.py "${1:-}"
