# Level 3 — Web, APIs, and Data (Projects 41–60)

At this level, learn one framework deeply enough to explain request flow, persistence, configuration, tests, and deployment. Use anonymized or openly licensed data and include source attribution.

## 41. Flask Blogging Platform

**Build:** A multi-page blog with posts, drafts, tags, pagination, and an admin-only editor. **Learn:** application factories, blueprints, templates, forms, ORM, and migrations. **Structure:** `app/__init__.py`, `models.py`, `auth/`, `blog/`, `templates/`, migrations, tests.

**Code steps:** (1) Create an app factory with environment configuration. (2) model users, posts, and tags. (3) add migrations. (4) implement read routes before write routes. (5) add login, CSRF-protected forms, authorization, and pagination. (6) seed demo data. **Flow:** request → route → service/model → template response; session identifies the user; authorization protects mutations. **Prove it:** test anonymous/admin permissions, drafts, invalid forms, pagination, and database rollback. **Portfolio upgrade:** deploy it with a custom domain, accessibility audit, and editor workflow demo.

## 42. FastAPI Task REST API

**Build:** A documented API for projects and tasks with filtering, pagination, and status transitions. **Learn:** HTTP semantics, Pydantic schemas, dependency injection, OpenAPI, and async endpoints. **Structure:** `app/api/`, `domain/`, `repositories/`, `services/`, `db/`, tests.

**Code steps:** (1) Design resources and status codes on paper. (2) create separate create/update/response schemas. (3) implement repository and service. (4) add CRUD routes, validation, filtering, and cursor/page metadata. (5) centralize errors. **Flow:** framework parses request into schema; service enforces rules; repository persists; response schema prevents accidental field leaks. **Prove it:** test 201/200/204/400/404/409/422 behavior, filters, transitions, and OpenAPI. **Portfolio upgrade:** add Docker, CI, generated client example, and hosted docs.

## 43. Authentication and Authorization Service

**Build:** Registration, verified login, session or token refresh, logout, password reset, and roles. **Learn:** password hashing, token lifecycle, cookies, authorization, and security testing. **Structure:** `app/auth/`, `users/`, `tokens/`, `mail/`, tests.

**Code steps:** (1) write the threat model and choose browser sessions or bearer tokens. (2) hash passwords with Argon2/bcrypt library. (3) create short-lived, single-use verification/reset tokens stored as hashes. (4) rate-limit sensitive endpoints. (5) enforce roles in one authorization layer. **Flow:** credentials are verified, an authenticated identity is established, authorization decides the action; secrets never appear in responses/logs. **Prove it:** test enumeration resistance, expiry, reuse, logout/revocation, cookie flags, role denial, and CSRF where applicable. **Portfolio upgrade:** document security decisions and run a dependency/security scan; never claim perfection.

## 44. Third-Party API Dashboard

**Build:** Combine two public APIs—such as weather and air quality—into one location dashboard. **Learn:** adapter pattern, parallel requests, caching, resilience, and provenance. **Structure:** `app/providers/`, `services/`, `cache/`, `web/`, tests with recorded fixtures.

**Code steps:** (1) define one internal location/measurement model. (2) adapt each external schema to it. (3) fetch independently with strict timeouts and retries only for safe failures. (4) cache by location/time. (5) render partial results when one provider fails. **Flow:** query is normalized; adapters fetch concurrently; service combines timestamped facts; UI labels source and freshness. **Prove it:** test timeouts, changed/missing fields, units, cache hit, and partial failure. **Portfolio upgrade:** add observability showing provider latency and reliability.

## 45. Streamlit Personal Finance Dashboard

**Build:** Import bank CSV files locally, map categories, and visualize monthly spending without uploading private data. **Learn:** pandas, Streamlit, data cleaning, interactive charts, and caching. **Structure:** `app.py`, `src/importers/`, `src/transform.py`, `src/charts.py`, synthetic samples, tests.

**Code steps:** (1) define a canonical transaction schema. (2) build provider-specific import adapters. (3) normalize dates, signs, descriptions, and categories. (4) let user review mappings. (5) calculate KPIs and render filters/charts. **Flow:** uploaded bytes → validated DataFrame → canonical transactions → filtered aggregates → charts. **Prove it:** test duplicate rows, missing columns, invalid dates, refunds, and reconciliation totals. **Portfolio upgrade:** include only synthetic data, a privacy statement, and one-click local run instructions.

## 46. Reproducible Data Cleaning Pipeline

**Build:** Turn a messy public dataset into documented, validated clean tables. **Learn:** pandas, schemas, missing data, reproducibility, and data lineage. **Structure:** `data/raw/` ignored, `data/sample/`, `src/extract.py`, `clean.py`, `validate.py`, `reports/`, tests.

**Code steps:** (1) write a data dictionary and expected schema. (2) acquire data with a checksum. (3) profile nulls/ranges/duplicates. (4) encode every cleaning decision as a function. (5) validate outputs with Pandera or equivalent. (6) create a quality report. **Flow:** immutable raw data → deterministic transforms → validated outputs → report; no manual spreadsheet fixes. **Prove it:** tests use miniature bad datasets for every rule and verify row-count reconciliation. **Portfolio upgrade:** add a pipeline diagram and explain disputed cleaning decisions.

## 47. Sales Analytics Case Study

**Build:** Answer five business questions from a public or synthetic sales dataset with a notebook plus reusable Python package. **Learn:** exploratory analysis, groupby, visualization, storytelling, and avoiding leakage. **Structure:** `notebooks/`, `src/analysis/`, `data/`, `reports/figures/`, tests.

**Code steps:** (1) write questions before exploring. (2) validate grain and units. (3) move reusable cleaning/metrics out of notebook. (4) calculate revenue, growth, mix, retention, and seasonality where supported. (5) state assumptions and limitations. **Flow:** tested package creates analysis-ready data; notebook calls it and explains findings; figures support conclusions. **Prove it:** reconcile totals, test metric formulas and date boundaries, and restart/run notebook top-to-bottom. **Portfolio upgrade:** publish a concise executive summary with actionable but appropriately qualified insights.

## 48. Market Data Explorer

**Build:** Explore historical market prices and indicators for education—not trading advice. **Learn:** time series, API adapters, resampling, rolling windows, and adjusted prices. **Structure:** `src/provider.py`, `src/indicators.py`, `app.py`, tests with fixed data.

**Code steps:** (1) cache dated provider responses and respect licensing/limits. (2) normalize timestamps and trading calendars. (3) calculate returns, moving averages, volatility, and drawdown. (4) plot with clear units. (5) separate descriptive history from forecasts. **Flow:** provider data → canonical series → deterministic indicators → interactive chart. **Prove it:** test missing dates, splits/adjustments, divide-by-zero, short windows, and known indicator examples. **Portfolio upgrade:** compare assets with explicit caveats and a data-source attribution page.

## 49. Survey Analysis Toolkit

**Build:** Import survey responses, clean multi-select fields, summarize groups, and generate an accessible report. **Learn:** categorical data, weighting basics, confidence, privacy, and charts. **Structure:** `src/schema.py`, `clean.py`, `analysis.py`, `report.py`, synthetic dataset, tests.

**Code steps:** (1) define question metadata. (2) validate allowed responses and missing codes. (3) reshape multi-select responses. (4) suppress very small groups. (5) calculate counts and percentages with denominators shown. **Flow:** metadata guides cleaning; normalized answers feed aggregations; privacy rules filter report tables. **Prove it:** test skip logic, unknown options, denominators, multi-select, and small-group suppression. **Portfolio upgrade:** add a methodology appendix and accessible color/text alternatives.

## 50. A/B Test Simulator

**Build:** Simulate experiments and analyze conversion differences with confidence intervals and power. **Learn:** probability, sampling, hypothesis tests, practical significance, and reproducibility. **Structure:** `src/simulate.py`, `src/analyze.py`, notebook/dashboard, tests.

**Code steps:** (1) accept baseline rate, effect, group size, and seed. (2) sample binomial outcomes. (3) calculate absolute/relative lift and interval. (4) repeat experiments to estimate power and false positives. (5) visualize distributions. **Flow:** parameters generate controlled data; analyzer returns estimates; repeated runs show uncertainty. **Prove it:** seeded tests, equal-rate behavior, extreme rates, tiny samples, and formula comparison with a trusted library. **Portfolio upgrade:** explain p-values versus business impact without claiming certainty.

## 51. Content Recommendation Engine

**Build:** Recommend movies/books from a public dataset using content similarity and evaluate results. **Learn:** feature engineering, TF-IDF, cosine similarity, offline evaluation, and cold start. **Structure:** `src/data.py`, `features.py`, `recommend.py`, `evaluate.py`, API/demo, tests.

**Code steps:** (1) define item metadata and user input. (2) clean text/categories. (3) fit vectorizer on a training set. (4) rank unseen items with explanations from shared features. (5) calculate precision/recall on held-out interactions if available. **Flow:** items become vectors; user profile aggregates liked vectors; similarity ranks candidates; filters remove seen items. **Prove it:** test deterministic ranks, empty profile, duplicate titles, unknown item, and no data leakage. **Portfolio upgrade:** compare popularity, content, and hybrid baselines honestly.

## 52. Sentiment Analysis Service

**Build:** Train and serve a text sentiment classifier with confidence and limitations. **Learn:** NLP preprocessing, pipelines, model evaluation, serialization, and inference APIs. **Structure:** `src/train.py`, `evaluate.py`, `inference.py`, FastAPI app, model metadata, tests.

**Code steps:** (1) inspect label balance/licensing. (2) split before fitting. (3) build a scikit-learn TF-IDF + logistic regression pipeline. (4) evaluate per class and inspect errors. (5) serialize model plus training metadata. (6) serve bounded inputs. **Flow:** training fits preprocessing and model together; inference loads a versioned artifact and returns label/probability. **Prove it:** test empty/long/Unicode input, artifact compatibility, schema, and a tiny known fixture. **Portfolio upgrade:** create a model card covering dataset, metrics, bias, and appropriate use.

## 53. Spam Message Classifier

**Build:** Classify SMS/email-like text as spam or not and expose interpretable top features. **Learn:** imbalanced classification, precision/recall, thresholds, and explainability. **Structure:** similar to 52 with experiment config and reports.

**Code steps:** (1) deduplicate before stratified splitting. (2) train a simple baseline first. (3) choose a threshold based on the cost of false positives. (4) evaluate confusion matrix, PR curve, and calibration. (5) show influential terms without treating them as proof. **Flow:** normalized text → probability → chosen threshold → label; evaluation connects threshold to harm. **Prove it:** guard against train/test duplicates, empty messages, adversarial spacing, and artifact drift. **Portfolio upgrade:** compare two models and write a responsible-use section.

## 54. Receipt OCR Pipeline

**Build:** Extract merchant, date, totals, and candidate line items from sample receipt images, with a correction screen. **Learn:** OCR, image preprocessing, regex/parsing, confidence, and human review. **Structure:** `src/preprocess.py`, `ocr.py`, `extract.py`, `schemas.py`, demo, tests with permitted samples.

**Code steps:** (1) orient/gray/contrast images. (2) call an installed OCR engine or API behind an adapter. (3) retain text boxes/confidence. (4) use rules to propose fields. (5) validate totals and allow manual correction. **Flow:** image → pixels → OCR tokens → candidate structured fields → human-confirmed record. **Prove it:** unit-test parsing with text fixtures; test blurry/rotated/missing-total cases and never log private receipts. **Portfolio upgrade:** publish synthetic examples and field-level accuracy, not vague “AI accuracy.”

## 55. Document Search Assistant

**Build:** Search a small collection of your own/public documents with citations, using keyword retrieval first and optional embeddings second. **Learn:** chunking, indexing, ranking, provenance, and grounded answers. **Structure:** `src/ingest.py`, `index.py`, `search.py`, `answer.py`, tests, evaluation set.

**Code steps:** (1) extract text and keep document/page metadata. (2) chunk without losing provenance. (3) build BM25/FTS search. (4) return excerpts with source links. (5) optionally ask an LLM to summarize only retrieved context and say when evidence is absent. **Flow:** ingest creates traceable chunks; query ranks chunks; response cites chunk origins. **Prove it:** evaluation questions include answerable and unanswerable cases; test deletion/reindex, Unicode, and citation correctness. **Portfolio upgrade:** compare keyword and vector retrieval using recall@k.

## 56. Job Listing Aggregator

**Build:** Aggregate listings only from permitted APIs/feeds, normalize them, deduplicate, filter, and notify. **Learn:** multi-source adapters, canonical schemas, fuzzy matching, scheduling, and ethics. **Structure:** `src/providers/`, `normalize.py`, `dedupe.py`, `repository.py`, web/CLI, tests.

**Code steps:** (1) define canonical job fields and provenance. (2) implement one adapter at a time. (3) normalize location, employment type, and dates. (4) deduplicate using source IDs then conservative similarity. (5) save searches and new-result markers. **Flow:** adapters → canonical records → dedupe → database → filters/alerts. **Prove it:** fixtures cover provider schema changes, reposts, missing salary, remote labels, and rate limits. **Portfolio upgrade:** show source health and clearly honor usage terms.

## 57. Uptime and Content Monitor

**Build:** Check configured URLs, record response time/status, detect selected content changes, and send deduplicated alerts. **Learn:** scheduling, timeouts, retries, hashing, state, and notifications. **Structure:** `src/checks.py`, `scheduler.py`, `repository.py`, `alerts.py`, tests.

**Code steps:** (1) define interval, timeout, expected status, and optional selector. (2) execute bounded checks. (3) normalize selected content and hash it. (4) persist outcomes. (5) alert only on state transitions and recovery. **Flow:** scheduler triggers check; result updates state; transition detector decides whether notification is necessary. **Prove it:** fake HTTP/time; test timeout, redirect policy, selector missing, flapping, repeated failure, and recovery. **Portfolio upgrade:** add latency charts, health endpoint, and runbook.

## 58. Async Download Manager

**Build:** Download a list of authorized files concurrently with limits, retries, progress, resume, and checksums. **Learn:** `asyncio`, `aiohttp`, semaphores, streaming, cancellation, and integrity. **Structure:** `src/download.py`, `manifest.py`, `cli.py`, local test server, tests.

**Code steps:** (1) validate URLs/output names. (2) bound concurrency with a semaphore. (3) stream chunks to `.part` files. (4) resume only when server range support is verified. (5) atomically rename after size/checksum validation. (6) cancel cleanly. **Flow:** tasks share a bounded session; each streams independently; manifest records final facts. **Prove it:** local server simulates slow, interrupted, wrong checksum, ignored Range, and 404 responses. **Portfolio upgrade:** compare throughput at several concurrency limits.

## 59. Real-Time WebSocket Chat

**Build:** Chat rooms with authenticated users, presence, typing status, message history, and reconnect. **Learn:** WebSockets, async state, pub/sub concepts, and browser clients. **Structure:** FastAPI/Starlette `app/`, `chat/`, `auth/`, static client, tests.

**Code steps:** (1) authenticate the WebSocket handshake. (2) create a connection manager keyed by room. (3) define typed message events. (4) persist chat messages but keep presence ephemeral. (5) add heartbeat, disconnect cleanup, rate/size limits, and HTML escaping. **Flow:** client event → server validation → persistence/broadcast → subscribed clients; reconnect fetches missed history. **Prove it:** test two clients, unauthorized join, malformed event, disconnect, ordering, and script content. **Portfolio upgrade:** use Redis pub/sub so multiple server processes can share rooms.

## 60. Focused Web Crawler and Search Index

**Build:** Crawl a small permitted documentation site within strict boundaries and provide local search. **Learn:** graph traversal, URL canonicalization, robots/politeness, indexing, and ranking. **Structure:** `src/crawler.py`, `frontier.py`, `extract.py`, `index.py`, `search.py`, tests with local site.

**Code steps:** (1) define allowed host/path, delay, depth, and page cap. (2) canonicalize URLs and keep visited/frontier sets. (3) fetch politely and parse title/text/links. (4) reject non-HTML and out-of-scope links. (5) index content with SQLite FTS5 and rank queries. **Flow:** frontier yields URL; fetch/parser produces page plus links; policy filters new links; index stores searchable text and provenance. **Prove it:** local fixture site covers cycles, fragments, redirects, duplicate content, robots restrictions, and broken links. **Portfolio upgrade:** visualize the crawl graph and publish crawl statistics, not copyrighted page dumps.

## Level 3 checkpoint

You can build tested web applications, integrate unreliable external systems, and produce reproducible data/ML work. Strong portfolio options are 42, 46, 51, 55, 57, and 59. Pick one, deploy it, add an architecture diagram, and write down a real engineering tradeoff.
