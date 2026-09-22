# AI Changelog

## [2026-09-22]

### Copilot

- Added a self-contained `index.html` Task Board with inline HTML, CSS, and JavaScript.
- Added task workflow documentation for Hermes review.
- Added an intentionally messy team-report table for the Hermes test.

### Hermes

- Reviewed and fixed `.messy-report` table semantics, keyboard-accessible horizontal overflow, and responsive layout.
- Hardened task `localStorage` loading/saving against malformed data and unavailable storage.
- Recorded the full review in `.ai/REVIEW.md` with status `PASS`.

### Tests

- `bash scripts/ai-workflow.sh` passed.
- Hermes review passed. Browser end-to-end automation remains a future follow-up.