#!/usr/bin/env bash
# Convenience wrapper for stock analysis CLI
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
source .venv/bin/activate
python src/main.py "${1:-}"
