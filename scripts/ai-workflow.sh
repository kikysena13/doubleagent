#!/usr/bin/env bash

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"

echo "======================================"
echo " AI DEVELOPMENT WORKFLOW"
echo "======================================"

echo
echo "[1/6] Checking repository..."
git status

echo
echo "[2/6] Checking AI files..."

required_files=(
    ".ai/TASK.md"
    ".ai/CONTEXT.md"
    ".ai/HANDOFF.md"
    ".ai/REVIEW.md"
    ".github/agents/hermes.agent.md"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "ERROR: Missing $file"
        exit 1
    fi
done

echo "AI workspace OK."

echo "Hermes custom agent configured."

echo
echo "[3/6] Current branch:"
git branch --show-current

echo
echo "[4/6] Current commit:"
git log -1 --oneline

echo
echo "[5/6] AI handoff:"
cat .ai/HANDOFF.md

echo
echo "[6/6] Hermes review:"
cat .ai/REVIEW.md

echo
echo "======================================"
echo " Workflow information loaded."
echo "======================================"