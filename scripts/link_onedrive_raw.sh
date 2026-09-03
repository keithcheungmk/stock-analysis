#!/usr/bin/env bash
# Link repo data/raw to the OneDrive copy so Mac Mini / second Macs share the same files.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RAW_LINK="$REPO_ROOT/data/raw"
DEFAULT_DEST="${HOME}/Library/CloudStorage/OneDrive2-個人/Stock research/raw"
DEST="${STOCK_ANALYSIS_RAW_ROOT:-$DEFAULT_DEST}"

usage() {
  cat <<EOF
Usage: $(basename "$0") [--dest PATH]

Creates:  data/raw  ->  OneDrive .../Stock research/raw

OneDrive "Stock research" layout:
  raw/              Official SEC/IR filings (this link target)
  research/         Notes, skills, third-party PDFs, ticker folders
  _private-broker/  IB / activity statements (do not share)

Default dest:
  $DEFAULT_DEST

Override with --dest or STOCK_ANALYSIS_RAW_ROOT.

On Mac Mini / another Mac:
  1. Install OneDrive and sign into the same account
  2. Wait until "Stock research/raw" finishes syncing
  3. Clone this repo (or open your local copy)
  4. Run:  ./scripts/link_onedrive_raw.sh
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi
if [[ "${1:-}" == "--dest" ]]; then
  DEST="${2:?--dest requires a path}"
fi

if [[ ! -d "$DEST" ]]; then
  echo "ERROR: OneDrive raw folder not found:"
  echo "  $DEST"
  echo "Sign into OneDrive and wait for sync, or pass --dest PATH"
  exit 1
fi

mkdir -p "$REPO_ROOT/data"

if [[ -L "$RAW_LINK" ]]; then
  current="$(readlink "$RAW_LINK")"
  if [[ "$current" == "$DEST" ]]; then
    echo "Already linked: $RAW_LINK -> $DEST"
    exit 0
  fi
  echo "Replacing existing symlink ($current)"
  rm "$RAW_LINK"
elif [[ -d "$RAW_LINK" ]]; then
  # Newer clones can contain Git-tracked cloud catalog manifests under data/raw.
  # They are not the Mac's canonical raw library and can legitimately differ
  # from the newer OneDrive manifests. Only replace the directory when every
  # file can be recovered from Git, then hide those tracked paths locally.
  while IFS= read -r -d '' source_file; do
    repo_relative="${source_file#"$REPO_ROOT"/}"
    if ! git -C "$REPO_ROOT" ls-files --error-unmatch -- "$repo_relative" >/dev/null 2>&1; then
      echo "ERROR: refusing to replace data/raw because it contains a non-Git file:"
      echo "  $source_file"
      exit 1
    fi
  done < <(find "$RAW_LINK" -type f -print0)

  backup_root="$(mktemp -d "${TMPDIR:-/tmp}/stock-analysis-raw.XXXXXX")"
  backup="$backup_root/repo-raw"
  mv "$RAW_LINK" "$backup"
  if ! ln -s "$DEST" "$RAW_LINK"; then
    mv "$backup" "$RAW_LINK"
    exit 1
  fi

  while IFS= read -r -d '' source_file; do
    repo_relative="data/raw/${source_file#"$backup"/}"
    git -C "$REPO_ROOT" update-index --skip-worktree -- "$repo_relative"
  done < <(find "$backup" -type f -print0)

  rm -rf "$backup_root"
  echo "Kept Git catalog manifests in Git and marked them skip-worktree locally."
  echo "Linked: $RAW_LINK -> $DEST"
  test -f "$RAW_LINK/TSLA/2026-Q2/manifest.json" && echo "OK: sample manifest readable"
  exit 0
elif [[ -e "$RAW_LINK" ]]; then
  echo "ERROR: unexpected path at $RAW_LINK"
  exit 1
fi

ln -s "$DEST" "$RAW_LINK"
echo "Linked: $RAW_LINK -> $DEST"
test -f "$RAW_LINK/TSLA/2026-Q2/manifest.json" && echo "OK: sample manifest readable"
