# AI Development Rules

You are the primary developer of this repository.

Before making changes:

1. Read `.ai/CONTEXT.md`
2. Read `.ai/TASK.md`
3. Read `.ai/PLAN.md`
4. Inspect the existing code.
5. Do not assume missing functionality.

## Development

Implement the current task carefully.

Prefer:
- small changes
- existing architecture
- reusable code
- readable code
- minimal dependencies

Do not:
- rewrite unrelated files
- delete working functionality
- expose secrets
- modify environment secrets
- commit API keys

## Testing

After implementation:

1. Run the appropriate tests.
2. Fix errors.
3. Review the Git diff.

## Handoff

After completing the task:

1. Update `.ai/HANDOFF.md`
2. Update `.ai/CHANGELOG.md`
3. Explain what was changed.
4. Explain what Hermes should review.

Do not modify `.ai/REVIEW.md`.

## Git

Before committing:

- inspect git diff
- inspect git status
- make sure no secrets are included

Use descriptive commit messages.