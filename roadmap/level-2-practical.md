# Level 2 — Practical Python (Projects 21–40)

Begin using third-party packages, virtual environments, dependency files, structured logging, and SQLite. Read package documentation instead of relying only on tutorials.

## 21. Currency Converter with Cache

**Build:** Convert currencies using a public exchange-rate API and a cached last-known response. **Learn:** HTTP, JSON, timeouts, environment configuration, caching, and failure handling. **Structure:** `src/client.py`, `src/service.py`, `src/cache.py`, tests with fixtures.

**Code steps:** (1) Define a rate-provider interface. (2) use `requests.get(..., timeout=10)` and check status. (3) validate response fields instead of trusting JSON. (4) cache response plus fetch time. (5) calculate through `Decimal` and label stale results. **Flow:** CLI → conversion service → cache/provider → validated rates → amount. **Prove it:** fake the provider; test rate inversion, unavailable network, stale cache, unknown currency, and rounding. **Portfolio upgrade:** compare two providers behind the same interface and document API attribution.

## 22. Pomodoro Desktop Timer

**Build:** A Tkinter timer with work/break presets, start/pause/reset, and session count. **Learn:** GUI widgets, event loops, callbacks, state, and non-blocking scheduling. **Structure:** `src/model.py`, `src/ui.py`, tests for the model.

**Code steps:** (1) Create a timer model independent of Tkinter. (2) design allowed state transitions. (3) build labels and buttons. (4) update once per second using `after`, never `sleep`. (5) save preferences in JSON. **Flow:** button callback changes model; scheduled tick reads model; UI redraws; the event loop stays responsive. **Prove it:** test model transitions with a fake clock and manually test rapid clicks and window close. **Portfolio upgrade:** add accessible keyboard shortcuts and a short demo GIF.

## 23. SQLite Notes App

**Build:** Create, tag, search, edit, and archive notes. **Learn:** SQL, schema design, parameterized queries, migrations, and context managers. **Structure:** `src/db.py`, `src/repository.py`, `src/service.py`, `src/cli.py`, `migrations/`, tests.

**Code steps:** (1) Design `notes`, `tags`, and `note_tags` tables. (2) enable foreign keys. (3) write migration 001. (4) implement repository CRUD with `?` parameters. (5) add service validation and search. (6) add CLI. **Flow:** user commands become service calls; repository executes transactions; rows become domain objects. **Prove it:** use a temporary database for CRUD, tag relationships, apostrophes, rollback, and migrations. **Portfolio upgrade:** add full-text search with SQLite FTS5 and explain the index.

## 24. Habit Tracker

**Build:** Track daily completions, streaks, missed days, and weekly summaries in SQLite. **Learn:** date arithmetic, relational modeling, business rules, and charts. **Structure:** `src/models.py`, `src/repository.py`, `src/streaks.py`, `src/report.py`, tests.

**Code steps:** (1) Store habits and completion dates with a uniqueness constraint. (2) implement check/uncheck. (3) calculate a streak by walking backward through dates. (4) respect a configured timezone and creation date. (5) render a text calendar. **Flow:** persistence stores facts; streak/report functions derive metrics without storing redundant totals. **Prove it:** test leap days, duplicate checks, a missed day, today incomplete, and timezone boundary. **Portfolio upgrade:** export a GitHub-style contribution grid image.

## 25. Inventory Manager

**Build:** Manage products, stock movements, reorder alerts, and inventory value. **Learn:** OOP boundaries, transactions, enums, and audit trails. **Structure:** `src/domain.py`, `src/repository.py`, `src/service.py`, tests.

**Code steps:** (1) Model products and immutable stock movements. (2) derive quantity by summing movements. (3) prevent outgoing stock below zero in a transaction. (4) add SKU search and reorder report. (5) export CSV. **Flow:** commands create movements; the ledger is the source of truth; reports aggregate it. **Prove it:** test concurrent-looking sequences, insufficient stock, duplicate SKU, returns, and exact value using `Decimal`. **Portfolio upgrade:** add optimistic locking and explain why audit records should not be edited.

## 26. Library Lending System

**Build:** Catalog books and copies, register members, issue loans, return items, and calculate overdue status. **Learn:** class design, relationships, policies, and dates. **Structure:** `src/domain/`, `src/services/`, `src/storage/`, tests.

**Code steps:** (1) Separate a book title from physical copies. (2) model members and loans. (3) put borrowing limit and loan duration in a policy object. (4) implement checkout/return as service operations. (5) report availability and overdue loans. **Flow:** service checks policy and availability, creates a loan, and updates copy status atomically. **Prove it:** test unavailable copies, member limits, same-day return, overdue boundaries, and lost items. **Portfolio upgrade:** expose the service through a small REST API later without changing domain rules.

## 27. Bank Account Simulator

**Build:** Simulate accounts, transfers, statements, interest, and overdraft rules—no real financial connection. **Learn:** encapsulation, `Decimal`, transactions, custom exceptions, and ledgers. **Structure:** `src/accounts.py`, `src/ledger.py`, `src/service.py`, tests.

**Code steps:** (1) Make ledger entries immutable. (2) derive balance from entries. (3) implement deposit/withdraw rules. (4) transfer with matched debit/credit IDs and rollback on failure. (5) generate statements by date. **Flow:** services validate commands and append balanced entries; balance and statements are projections. **Prove it:** test rounding, insufficient funds, failed transfer atomicity, interest dates, and conservation of total money. **Portfolio upgrade:** add property-based tests with Hypothesis for ledger invariants.

## 28. Student Gradebook

**Build:** Import assignments and scores, apply weighted categories, calculate letter grades, and export reports. **Learn:** CSV validation, aggregation, configuration, and reporting. **Structure:** `src/importer.py`, `src/grades.py`, `src/report.py`, tests.

**Code steps:** (1) define input schemas. (2) validate weights total 100%. (3) calculate category averages with a stated missing-work policy. (4) map numeric grades to configurable bands. (5) export per-student and class summaries. **Flow:** importer returns validated records; grade policy calculates results; report formats them. **Prove it:** test missing scores, zero-point work, boundary grades, extra credit, and malformed CSV. **Portfolio upgrade:** show distribution charts and document fairness tradeoffs.

## 29. Recipe Manager and Meal Planner

**Build:** Store recipes with scaled ingredients, search tags, plan a week, and create a shopping list. **Learn:** data modeling, fractions, normalization, and aggregation. **Structure:** `src/domain.py`, `src/scaling.py`, `src/planner.py`, SQLite repository, tests.

**Code steps:** (1) model ingredient amount/unit separately from display text. (2) scale by desired servings using `Fraction` or `Decimal`. (3) normalize compatible units carefully. (4) assign recipes to dates/meals. (5) aggregate identical shopping items. **Flow:** recipes are source data; plan references recipes; scaling creates planned quantities; aggregation forms the list. **Prove it:** test fractional amounts, zero servings, incompatible units, duplicates, and missing ingredients. **Portfolio upgrade:** add a documented import format and printable weekly plan.

## 30. Flask URL Shortener

**Build:** Create short links, redirect, track visits, and expire links. **Learn:** Flask routes, HTTP status codes, templates, SQLite, and web security basics. **Structure:** `app/` with `routes.py`, `models.py`, `services.py`, `templates/`; tests.

**Code steps:** (1) validate `http/https` URLs. (2) generate collision-checked random codes. (3) create POST form and result page. (4) redirect with a 302 and record visit metadata conservatively. (5) return 404/410 for missing/expired codes. **Flow:** request → route validation → service/repository → response; redirects trigger analytics. **Prove it:** Flask test client covers create, redirect, collision, invalid scheme, and expiry. **Portfolio upgrade:** add rate limiting, privacy notice, Dockerfile, and deployed demo.

## 31. Static Site Generator

**Build:** Turn Markdown posts and templates into a complete static website. **Learn:** parsing, templates, paths, incremental builds, and CLI design. **Structure:** `content/`, `templates/`, `assets/`, `src/sitegen/`, tests.

**Code steps:** (1) parse front matter and Markdown. (2) validate metadata. (3) render posts through Jinja templates. (4) build index, tag, and RSS pages. (5) copy assets and clean only the configured output folder. **Flow:** content files become typed pages; indexes derive from page metadata; renderer writes deterministic output. **Prove it:** snapshot-test HTML, broken metadata, duplicate slugs, relative links, and empty content. **Portfolio upgrade:** package it as an installable CLI and use it for your own portfolio blog.

## 32. Markdown Preview Server

**Build:** Serve a live HTML preview that refreshes when a Markdown file changes. **Learn:** local servers, file watching, HTML sanitization, and browser refresh. **Structure:** `src/server.py`, `src/render.py`, templates, tests.

**Code steps:** (1) render Markdown to HTML. (2) sanitize raw HTML or disable it. (3) serve only files beneath an allowed root. (4) watch for changes and notify the page with server-sent events or polling. (5) add a CLI path option. **Flow:** browser requests preview; renderer reads authorized file; watcher changes a version; browser refreshes. **Prove it:** test path traversal attempts, script input, missing files, and rapid writes. **Portfolio upgrade:** add syntax highlighting and document the security boundary.

## 33. Batch Image Processor

**Build:** Resize, rotate, watermark, and convert images while preserving originals. **Learn:** Pillow, pipelines, metadata, and batch errors. **Structure:** `src/operations.py`, `src/pipeline.py`, `src/cli.py`, `samples/`, tests.

**Code steps:** (1) represent operations as configuration. (2) discover supported files. (3) apply EXIF orientation, color conversion, resizing, then output format. (4) write to a separate output folder with collision rules. (5) summarize successes/failures. **Flow:** discovery → decode → ordered transforms → encode; one corrupt file should not stop the batch. **Prove it:** generate tiny fixtures for aspect ratio, transparency, corruption, and unchanged originals. **Portfolio upgrade:** benchmark sequential versus process-pool execution.

## 34. PDF Toolkit

**Build:** Merge, split, rotate, and extract metadata from PDFs you are authorized to process. **Learn:** binary files, pypdf, page ranges, validation, and CLI subcommands. **Structure:** `src/pdf_tool/commands.py`, `src/pdf_tool/cli.py`, tests with generated PDFs.

**Code steps:** (1) design `merge`, `split`, `rotate`, and `info` subcommands. (2) validate paths and page ranges before writing. (3) use context managers. (4) write to a new file, never overwrite by default. (5) handle encrypted/corrupt files clearly. **Flow:** CLI parses a command; validator builds a safe operation; library reads pages and writes the result. **Prove it:** inspect resulting page counts/order/rotation and test invalid ranges. **Portfolio upgrade:** add bookmarks and a dry-run manifest.

## 35. Ethical Website Scraper

**Build:** Collect permitted public data from one documented site into CSV. **Learn:** requests, BeautifulSoup, selectors, pagination, politeness, and schema validation. **Structure:** `src/fetch.py`, `src/parse.py`, `src/export.py`, saved HTML fixtures, tests.

**Code steps:** (1) read the site's terms and robots guidance. (2) set an honest user agent, timeout, delay, and page limit. (3) separate fetching from parsing. (4) parse saved fixtures into records. (5) deduplicate and export source URLs/fetch time. **Flow:** rate-limited fetch returns HTML; pure parser returns validated records; exporter writes provenance. **Prove it:** tests never hit the live site; cover missing fields, pagination end, and changed markup. **Portfolio upgrade:** include an ethics/design section and incremental resume support.

## 36. RSS News Reader

**Build:** Subscribe to feeds, fetch new entries, mark read/favorite, and search locally. **Learn:** XML/feed parsing, HTTP cache headers, deduplication, and SQLite. **Structure:** `src/client.py`, `src/repository.py`, `src/service.py`, `src/cli.py`, tests.

**Code steps:** (1) store feed URLs and entries with a stable unique key. (2) parse through `feedparser`. (3) send stored ETag/Last-Modified headers. (4) upsert entries. (5) implement unread/favorite/search views. **Flow:** refresh asks servers only for changes; normalized entries are deduplicated; user state remains local. **Prove it:** fixture feeds cover missing IDs, date formats, duplicate items, 304 responses, and malformed XML. **Portfolio upgrade:** schedule refresh and display source health without hammering feeds.

## 37. Registration Validator Library

**Build:** A reusable package for validating usernames, emails, passwords, and dates, returning all field errors. **Learn:** package layout, typed results, regex limits, and API design. **Structure:** `src/formcheck/`, `tests/`, `pyproject.toml`.

**Code steps:** (1) define `ValidationError(field, code, message)`. (2) make each validator small and composable. (3) normalize only fields where safe. (4) return errors rather than printing. (5) expose a stable public API. **Flow:** raw fields pass through independent rules; errors accumulate; caller decides presentation. **Prove it:** table-driven tests cover boundaries and Unicode; do not pretend regex proves an email exists. **Portfolio upgrade:** publish generated API docs and semantic version tags.

## 38. Local Password Vault

**Build:** Store generated credentials in an encrypted local vault for learning; rely on audited cryptography libraries, never invent encryption. **Learn:** secrets, key derivation, authenticated encryption, threat modeling, and secure input. **Structure:** `src/vault/crypto.py`, `storage.py`, `service.py`, `cli.py`, tests.

**Code steps:** (1) write a threat model. (2) derive a key from a master password using a library-provided KDF and random salt. (3) encrypt authenticated JSON with a fresh nonce. (4) write atomically with restrictive permissions where supported. (5) implement add/get/list/delete without logging secrets. **Flow:** password exists only in memory; KDF creates key; authenticated decryption detects tampering. **Prove it:** test round trip, wrong password, modified ciphertext, uniqueness of salts/nonces, and no plaintext on disk. **Portfolio upgrade:** commission peer review; label it educational, not production-ready.

## 39. Duplicate File Finder

**Build:** Find duplicate files safely using size and hashes, then produce a review report; do not delete automatically. **Learn:** hashing, chunked I/O, grouping, filesystem identity, and concurrency. **Structure:** `src/scanner.py`, `src/hash.py`, `src/report.py`, tests.

**Code steps:** (1) group candidate files by size. (2) hash only groups with matching sizes. (3) read in chunks. (4) account for symlinks, permission failures, and hard links. (5) output JSON/HTML report with estimated reclaimable size. **Flow:** cheap filters reduce expensive hashing; identical digest groups become review candidates. **Prove it:** temporary files cover empty files, same size/different content, permissions, symlinks, and hard links. **Portfolio upgrade:** add optional byte-for-byte verification and performance measurements.

## 40. Versioned Backup Utility

**Build:** Make incremental, verifiable backups to a chosen destination with restore and dry-run support. **Learn:** manifests, hashes, copy semantics, retention, logging, and recovery design. **Structure:** `src/backup/plan.py`, `manifest.py`, `copy.py`, `restore.py`, tests.

**Code steps:** (1) explicitly validate source/destination and forbid nesting. (2) scan into a manifest of relative path, size, time, and hash. (3) compare with prior manifest. (4) copy changed files into a timestamped snapshot. (5) verify hashes. (6) restore only into a new/confirmed location. **Flow:** planner is read-only; executor copies an approved plan; verifier proves output; manifest makes history auditable. **Prove it:** temp trees cover changed/deleted files, interrupted copy, collisions, and restore integrity. **Portfolio upgrade:** add retention policies and a disaster-recovery walkthrough.

## Level 2 checkpoint

You can now work with APIs, databases, packages, GUIs, binary files, and safer automation. Good portfolio candidates are 23, 30, 31, 35, or 40. Make one of them installable from a fresh clone and add continuous integration before Level 3.
