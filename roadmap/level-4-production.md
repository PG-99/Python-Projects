# Level 4 — Production Systems (Projects 61–80)

These projects are about reliability as much as features. Add structured logs, configuration validation, database migrations, health checks, CI, containers, security notes, and a small operational runbook.

## 61. Django Marketplace

**Build:** A marketplace with seller listings, search, carts, mock checkout, reviews, and admin moderation; do not process real payments initially. **Learn:** Django models/views/forms, transactions, permissions, media, and admin. **Structure:** apps `accounts`, `catalog`, `orders`, `reviews`; settings by environment; tests.

**Code steps:** (1) model products, variants, inventory, carts, orders, and line-item price snapshots. (2) add migrations/admin. (3) build browse/search. (4) implement cart. (5) create order inside an atomic transaction with a fake payment provider. (6) enforce seller/buyer/moderator permissions. **Flow:** web request → form/service → transaction → template; order stores historical price rather than reading a later product price. **Prove it:** test overselling, permission boundaries, price changes, failed checkout rollback, and review eligibility. **Portfolio upgrade:** add background image processing and a deployment diagram.

## 62. Appointment Booking System

**Build:** Provider schedules, timezone-aware slots, booking/cancel/reschedule, waitlist, and reminders. **Learn:** interval logic, timezones, concurrency, idempotency, and notifications. **Structure:** `scheduling`, `bookings`, `notifications`, worker, tests.

**Code steps:** (1) store UTC instants plus provider timezone. (2) generate slots from availability and exceptions. (3) enforce a database uniqueness/exclusion rule to prevent overlaps. (4) book atomically. (5) enqueue idempotent reminders. (6) promote waitlist on cancellation. **Flow:** schedule facts generate candidate slots; transaction claims one; event schedules reminders. **Prove it:** daylight-saving changes, simultaneous booking, cancellation cutoff, duplicate reminder, and reschedule rollback. **Portfolio upgrade:** publish a sequence diagram and concurrency test.

## 63. Team Issue Tracker

**Build:** Projects, issues, comments, labels, assignments, status workflows, audit history, and notifications. **Learn:** domain workflows, authorization, search, event logs, and API/UI consistency. **Structure:** domain modules plus web/API adapters and worker.

**Code steps:** (1) define allowed status transitions. (2) model immutable audit events. (3) add issue CRUD and optimistic concurrency version. (4) implement search/filter pagination. (5) create notification preferences and outbox events. **Flow:** command validates permission/version/workflow; transaction updates issue and outbox; worker delivers notifications. **Prove it:** test forbidden transitions, conflicting edits, history completeness, filter combinations, and notification retries. **Portfolio upgrade:** include import/export and an ADR explaining the outbox pattern.

## 64. Invoicing SaaS Demo

**Build:** Organizations, clients, estimates, invoices, tax/discount rules, PDF generation, and payment-state simulation. **Learn:** multi-tenancy, money, document rendering, and immutable records. **Structure:** `organizations`, `billing`, `documents`, `payments`, tests.

**Code steps:** (1) scope every tenant-owned query by organization. (2) model money/currency explicitly. (3) calculate totals through one policy service. (4) snapshot client and line information on issue. (5) render versioned PDFs. (6) accept signed, replay-safe fake payment webhooks. **Flow:** draft is editable; issue freezes business facts; renderer creates artifact; webhook advances payment state idempotently. **Prove it:** tenant isolation, rounding, tax order, webhook replay/signature, and PDF snapshot tests. **Portfolio upgrade:** threat-model multi-tenant data leakage.

## 65. API Gateway Rate Limiter

**Build:** A reverse-proxy demo with per-key/IP limits, quotas, headers, and metrics. **Learn:** token bucket/sliding window algorithms, Redis atomicity, middleware, and load tests. **Structure:** `gateway/`, `policies/`, `storage/`, tests and load scripts.

**Code steps:** (1) specify burst and sustained rules. (2) implement a pure reference algorithm. (3) use a Redis script/atomic operation for shared state. (4) return 429 plus standard retry information. (5) make trusted proxy/IP handling explicit. **Flow:** middleware identifies subject/policy; atomic limiter decides; allowed requests proxy onward; every decision emits metrics. **Prove it:** boundary timestamps, concurrent requests, Redis failure policy, spoofed headers, and load fairness. **Portfolio upgrade:** compare fixed window, sliding window, and token bucket.

## 66. URL Analytics Microservices

**Build:** Split project 30 into link, redirect, and analytics services connected through events. **Learn:** service boundaries, contracts, eventual consistency, idempotency, and tracing. **Structure:** `services/link`, `redirect`, `analytics`, shared schemas only where justified, compose file, tests.

**Code steps:** (1) first state why separation is educational and where a monolith is better. (2) define APIs/events with versions. (3) make redirects fast and publish click events. (4) process events idempotently into aggregates. (5) propagate correlation IDs. **Flow:** link service owns mappings; redirect resolves and emits; analytics consumes later, so counters may lag. **Prove it:** contract tests, duplicate/out-of-order events, consumer restart, unavailable analytics, and trace linkage. **Portfolio upgrade:** measure complexity/latency against the monolith.

## 67. Configurable ETL Pipeline

**Build:** Incrementally ingest API/CSV data, transform it, and load validated tables with checkpoints and backfills. **Learn:** ETL, watermarks, idempotency, schemas, partitions, and orchestration. **Structure:** `pipeline/extractors`, `transforms`, `loaders`, `quality`, tests.

**Code steps:** (1) define source/target contracts. (2) extract a bounded interval into immutable staging files. (3) transform deterministically. (4) run quality checks and reconcile counts. (5) load with merge/upsert. (6) advance checkpoint only after success. **Flow:** each run owns a time partition; artifacts and metadata make it repeatable; checkpoint represents committed progress. **Prove it:** late records, duplicates, schema changes, partial failure, rerun, and backfill overlap. **Portfolio upgrade:** show lineage and a failure-recovery demo.

## 68. DuckDB Analytics Warehouse

**Build:** A local warehouse with dimensional models, Parquet facts, SQL transformations, and a metrics layer. **Learn:** star schemas, columnar storage, SQL analytics, slowly changing dimensions, and query plans. **Structure:** `warehouse/raw`, `models/staging`, `models/marts`, `src/build.py`, tests.

**Code steps:** (1) choose grain for each fact table. (2) create dimensions with surrogate keys. (3) transform staged data into facts/dimensions. (4) add data tests for uniqueness, relationships, and accepted values. (5) define reusable metrics. (6) profile queries. **Flow:** raw snapshots → clean staging views → dimensional marts → metrics/dashboard. **Prove it:** unknown dimension handling, duplicate facts, late data, slowly changing records, and total reconciliation. **Portfolio upgrade:** compare CSV versus Parquet size/query time.

## 69. Dependency-Aware Workflow Scheduler

**Build:** Run tasks arranged in a directed acyclic graph with retries, timeouts, logs, and backfills. **Learn:** DAGs, topological sorting, state machines, subprocess isolation, and scheduling. **Structure:** `scheduler/dag.py`, `executor.py`, `state.py`, `cli.py`, tests.

**Code steps:** (1) validate unique task IDs, dependencies, and no cycles. (2) topologically identify ready tasks. (3) execute with bounded workers. (4) persist run/task states. (5) retry according to policy and block dependents on final failure. (6) support a dry-run graph. **Flow:** scheduler repeatedly finds ready nodes; executor reports terminal state; state unlocks downstream nodes. **Prove it:** cycles, diamond graph, failure, retry, timeout, restart recovery, and backfill. **Portfolio upgrade:** build a visual run timeline.

## 70. Distributed Task Queue

**Build:** Submit background jobs to workers with acknowledgement, retry, dead-letter, scheduling, and idempotency. **Learn:** brokers, delivery guarantees, leases, worker crashes, and serialization. **Structure:** `queue/client.py`, `broker.py`, `worker.py`, `registry.py`, integration tests.

**Code steps:** (1) define a versioned job envelope. (2) register allowed task names—never deserialize arbitrary code. (3) claim with a visibility timeout. (4) acknowledge only after success. (5) retry with backoff/jitter, then dead-letter. (6) make sample tasks idempotent. **Flow:** producer stores envelope; worker leases it; success acknowledges; crash lets lease expire. **Prove it:** duplicate delivery, crash after side effect, poison job, unknown version, clock boundaries, and multiple workers. **Portfolio upgrade:** document at-least-once semantics and show chaos testing.

## 71. Redis-Backed Cache Service

**Build:** Add caching, invalidation, stampede protection, and metrics to a read-heavy API. **Learn:** cache-aside, TTL, serialization, distributed locks, and consistency. **Structure:** `cache/keys.py`, `service.py`, `metrics.py`, integration tests.

**Code steps:** (1) measure a slow read baseline. (2) design versioned tenant-aware keys. (3) implement cache-aside. (4) invalidate/update on writes. (5) prevent stampede with request coalescing or a short lock. (6) emit hit/miss/latency metrics. **Flow:** read checks cache then authoritative store; misses populate; writes change authority then invalidate. **Prove it:** stale entry, concurrent miss, Redis unavailable, corrupt value, permission-scoped keys, and TTL jitter. **Portfolio upgrade:** publish benchmark plus consistency tradeoff.

## 72. Event-Driven Notification Platform

**Build:** Consume domain events and deliver email-like, SMS-like, and in-app notifications using mock providers, preferences, templates, and retries. **Learn:** event routing, templates, idempotency, provider adapters, and compliance concepts. **Structure:** `events/`, `routing/`, `templates/`, `providers/`, `workers/`, tests.

**Code steps:** (1) version event schemas. (2) route by event type and user preference. (3) render validated templates. (4) create a delivery record/idempotency key. (5) call adapter with timeout. (6) classify retryable versus permanent failures. **Flow:** event → routing decisions → rendered deliveries → provider result → status/audit. **Prove it:** duplicates, opt-out, missing template field, retry, permanent rejection, provider outage, and redacted logs. **Portfolio upgrade:** add a preview tool and delivery SLO dashboard.

## 73. Real-Time Analytics Dashboard

**Build:** Ingest synthetic events, compute rolling metrics, and stream dashboard updates. **Learn:** event time, windows, late data, aggregation, WebSockets, and load shedding. **Structure:** `producer/`, `ingest/`, `aggregator/`, `api/`, dashboard, tests.

**Code steps:** (1) define versioned events with event/ingest timestamps. (2) validate and partition ingest. (3) maintain rolling window aggregates. (4) decide a lateness policy. (5) publish snapshots/deltas to clients. (6) persist enough state to recover. **Flow:** producer → ingest log → window aggregator → query store → push gateway → browser. **Prove it:** out-of-order/duplicate/late events, restart, slow client, burst, and window boundaries. **Portfolio upgrade:** display freshness and correction metrics.

## 74. Geospatial Route Planner

**Build:** Find routes across an openly licensed map extract and show distance/time alternatives. **Learn:** graph models, Dijkstra/A*, geospatial coordinates, heuristics, and map visualization. **Structure:** `src/graph.py`, `routing.py`, `geo.py`, API/UI, tests with tiny graphs.

**Code steps:** (1) turn nodes/edges into adjacency lists with non-negative costs. (2) implement Dijkstra. (3) add A* with admissible distance heuristic. (4) snap user points carefully. (5) reconstruct route and display. **Flow:** input points → graph nodes → frontier search → predecessor chain → geometry. **Prove it:** disconnected graph, one-way edges, equal routes, start=end, invalid negative weight, and known shortest paths. **Portfolio upgrade:** compare explored nodes/runtime for Dijkstra and A*.

## 75. Image Classification Pipeline

**Build:** Train, evaluate, and serve a small classifier using a licensed dataset and transfer learning. **Learn:** datasets, augmentation, training loops, leakage, evaluation, and model cards. **Structure:** `src/data.py`, `train.py`, `evaluate.py`, `serve.py`, configs, tests.

**Code steps:** (1) inspect labels/license and split by entity before augmentation. (2) make reproducible loaders. (3) train a baseline then fine-tune. (4) track experiments. (5) evaluate per-class metrics and errors. (6) export versioned artifact and bounded inference endpoint. **Flow:** dataset/config → training artifact → evaluation gate → registry folder → API. **Prove it:** transform shapes, label mapping, artifact load, invalid image, deterministic small run, and leakage audit. **Portfolio upgrade:** include model card and explain failure examples.

## 76. Time-Series Forecasting Service

**Build:** Forecast a public series with baselines, backtesting, intervals, and an API. **Learn:** temporal splits, seasonality, lag features, leakage, backtesting, and uncertainty. **Structure:** `src/features.py`, `backtest.py`, `train.py`, `forecast.py`, API, tests.

**Code steps:** (1) define horizon/frequency before modeling. (2) build naive/seasonal baselines. (3) create lag/rolling features using past only. (4) perform walk-forward validation. (5) compare MAE and interval coverage. (6) retrain and serve with cutoff metadata. **Flow:** history → leakage-safe features → backtests → selected model → dated forecast. **Prove it:** missing timestamps, short history, DST if hourly, cutoff, feature alignment, and baseline comparison. **Portfolio upgrade:** explain when forecasts should not be trusted.

## 77. Anomaly Detection System

**Build:** Detect unusual synthetic transactions or sensor readings, rank alerts, and capture analyst feedback. **Learn:** imbalanced data, unsupervised methods, thresholds, drift, and human-in-loop design. **Structure:** `src/features.py`, `model.py`, `scoring.py`, `feedback.py`, dashboard, tests.

**Code steps:** (1) define what an anomaly means operationally. (2) create time-safe features. (3) compare statistical baseline and Isolation Forest. (4) select threshold from alert capacity. (5) explain contributing features. (6) store feedback separately from raw events. **Flow:** event → features → score → threshold → alert queue → feedback. **Prove it:** synthetic injected anomalies, constant columns, missing data, extreme values, reproducibility, and drift signal. **Portfolio upgrade:** report precision-at-k and false-positive costs, not only accuracy.

## 78. Semantic Document Search

**Build:** Upgrade project 55 with embedding-based search, hybrid ranking, access filters, and measurable retrieval quality. **Learn:** vector indexes, hybrid retrieval, metadata filters, reranking, and evaluation. **Structure:** `ingest/`, `indexes/`, `retrieval/`, `evaluation/`, API, tests.

**Code steps:** (1) version chunker and embedding model. (2) store vector plus source/access metadata. (3) retrieve lexical and vector candidates. (4) fuse/rerank. (5) enforce authorization before returning results. (6) create labeled query/relevance set. **Flow:** query → filters → dual retrieval → fusion → cited ranked chunks. **Prove it:** deleted docs, changed permissions, duplicate chunks, empty query, model-version mismatch, and recall@k. **Portfolio upgrade:** publish an evaluation dashboard and latency/quality tradeoff.

## 79. Recommendation API with Feedback

**Build:** Serve recommendations, record impressions/clicks, retrain offline, and safely roll out model versions. **Learn:** online/offline features, feedback bias, batch training, model registry, and experiments. **Structure:** `training/`, `features/`, `serving/`, `events/`, `evaluation/`, tests.

**Code steps:** (1) define impression/click events. (2) make a popularity baseline. (3) build collaborative/content candidates. (4) filter unavailable/seen items. (5) store model version with every impression. (6) validate artifact before atomic rollout and retain rollback. **Flow:** events → training snapshot → artifact → serving candidates → impression events → future training. **Prove it:** cold user/item, empty candidates, artifact incompatibility, deterministic model, unavailable items, and rollback. **Portfolio upgrade:** discuss position/selection bias and guardrail metrics.

## 80. Model Serving and Monitoring Platform

**Build:** Host versioned models with validation, batching, latency/error metrics, data-drift summaries, and rollback. **Learn:** inference architecture, contracts, model registries, observability, and safe deployment. **Structure:** `registry/`, `serving/`, `monitoring/`, `deploy/`, load/integration tests.

**Code steps:** (1) define input/output schemas and resource bounds. (2) load artifacts at startup with signature checks. (3) implement readiness/liveness. (4) add bounded batching if valuable. (5) emit latency/errors/version and privacy-safe feature summaries. (6) canary new version and rollback on explicit gates. **Flow:** validated request → selected model → prediction → telemetry; asynchronous monitors compare distributions, not raw secrets. **Prove it:** corrupt model, invalid/oversized input, concurrent load, timeout, canary failure, and rollback. **Portfolio upgrade:** run a load test and write an operational runbook.

## Level 4 checkpoint

You can now discuss consistency, idempotency, concurrency, observability, security, and recovery—not merely frameworks. One polished project with diagrams, tests, metrics, and a runbook is enough to show serious engineering maturity.
