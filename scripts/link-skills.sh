#!/usr/bin/env bash
set -euo pipefail
# Link every skill into local harness skill dirs (mirrors mattpocock/skills scripts/link-skills.sh).
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
link_bucket() {
  local dest="$1"
  mkdir -p "$dest"
  while IFS= read -r skill; do
    local name
    name="$(basename "$skill")"
    ln -sfn "$skill" "$dest/$name"
    echo "linked $name -> $dest/$name"
  done < <(find "$REPO_DIR/skills" -maxdepth 2 -mindepth 2 -type d)
}
link_bucket "$HOME/.claude/skills"
link_bucket "$HOME/.agents/skills"
