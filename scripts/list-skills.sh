#!/usr/bin/env bash
set -euo pipefail
# List all skills in this repo.
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
find "$REPO_DIR/skills" -maxdepth 2 -mindepth 2 -type d | sort
