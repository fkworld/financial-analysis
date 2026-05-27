# Project Guidelines

## Overview

Financial analysis workspace that stores Chinese public company earnings reports as Markdown files. A Python script converts source PDFs to Markdown via `markitdown`.

## Architecture

- `src/reports/{公司名}/{公司名}-{year}.md` — Earnings reports (Chinese, from HK/US stock filings)
- `scripts/pdf-to-md.py` — PDF-to-Markdown converter (uses `markitdown` library)
- `src/index.ts` — TypeScript entrypoint (currently empty)

Reports are organized by company name (Chinese) with one directory per company. File names follow `{公司名}-{year}.md` pattern.

## Build and Test

| Task             | Command                 |
| ---------------- | ----------------------- |
| Install          | `pnpm install`          |
| Convert PDFs     | `pnpm run pdf-to-md`    |
| Lint (all)       | `pnpm run lint:oxlint`  |
| Format           | `pnpm run lint:oxfmt`   |
| File naming lint | `pnpm run lint:ls-lint` |

No test framework is configured yet.

## Conventions

- **Language**: Reports and financial data are in Chinese (Simplified/Traditional). Respond in the same language as the user's query when discussing report content.
- **Package manager**: pnpm 10 only — never use npm or yarn.
- **Formatting**: OXC formatter (`oxfmt`) with format-on-save. Do not add Prettier or ESLint.
- **Linting**: `oxlint` for JS/TS. Do not add ESLint.
- **Commits**: Conventional Commits enforced by commitlint + husky pre-commit hooks.
- **File naming**: kebab-case for all files except `src/reports/` which uses Chinese company names.
- **TypeScript**: ESNext target, strict mode, `noEmit` (type-checking only).
- **Module system**: ESM (`"type": "module"`).

## Code Style

- TypeScript with strict mode — do not use `any`.
- Follow existing OXC lint rules; do not disable rules without justification.
- Keep `src/index.ts` as the single entrypoint.
