#!/usr/bin/env python3
import os
import time
import subprocess
from pathlib import Path

# Direktori yang dipantau (root project)
ROOT = Path(__file__).resolve().parent.parent
WATCHED_EXTENSIONS = {".html", ".js", ".md", ".sh", ".py"}

def get_file_states():
    states = {}
    for path in ROOT.rglob("*"):
        if any(part.startswith('.') for part in path.parts if part != '.'):
            # Abaikan folder tersembunyi kecuali .ai jika diperlukan, tapi abaikan .git
            if '.git' in path.parts:
                continue
        if path.is_file() and path.suffix in WATCHED_EXTENSIONS:
            try:
                states[str(path)] = path.stat().st_mtime
            except FileNotFoundError:
                pass
    return states

def main():
    print(f"[Hermes Watcher] Memulai pemantauan file di {ROOT}...")
    last_states = get_file_states()

    while True:
        time.sleep(3)
        current_states = get_file_states()

        changed = False
        for path, mtime in current_states.items():
            if path not in last_states or last_states[path] != mtime:
                print(f"[Hermes Watcher] Perubahan terdeteksi pada: {path}")
                changed = True
                break

        if changed:
            print("[Hermes Watcher] Menjalankan workflow otomatis...")
            subprocess.run(["./scripts/ai-workflow.sh"], cwd=ROOT)
            last_states = current_states

if __name__ == "__main__":
    main()
