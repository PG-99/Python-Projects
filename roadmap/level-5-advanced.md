# Level 5 — Advanced Engineering (Projects 81–100)

These are study projects, not claims that you have replaced mature production software. Clearly document limitations, threat models, protocol subsets, and what you learned from established implementations.

## 81. Publishable Python Package

**Build:** Extract a useful library from an earlier project and package it with typed API, documentation, CI, and releases. **Learn:** `pyproject.toml`, build backends, semantic versioning, wheels, and public API design. **Structure:** `src/package_name/`, `tests/`, `docs/`, `.github/workflows/`, changelog.

**Code steps:** (1) choose one narrow problem and public namespace. (2) configure metadata and dependencies. (3) add type hints, docstrings, tests, lint, and build. (4) test wheel in a clean environment. (5) automate release checks. (6) publish to TestPyPI before PyPI if desired. **Flow:** source → tests/build → wheel/sdist → package index → user install. **Prove it:** test minimum/latest supported Python, built artifact contents, imports outside repo, and backwards-compatible examples. **Portfolio upgrade:** respond well to one external issue or contribution.

## 82. Professional CLI Framework Project

**Build:** Turn a practical tool into a polished installable CLI with subcommands, config, shell completion, structured output, and plugins. **Learn:** command design, exit codes, configuration precedence, logging, and extensibility. **Structure:** `src/tool/cli.py`, `commands/`, `config.py`, `plugins.py`, tests.

**Code steps:** (1) define command grammar and stable exit codes. (2) use Typer/Click or `argparse`. (3) implement defaults < config file < environment < CLI precedence. (4) separate human and JSON output. (5) discover trusted plugins through entry points. (6) add completion/help docs. **Flow:** arguments/config normalize into a command object; service runs; presenter selects output; exit code reflects result. **Prove it:** isolated filesystem tests, config conflicts, broken plugin, signals, JSON schema, and help snapshots. **Portfolio upgrade:** distribute a wheel and standalone executable.

## 83. Python Static Linter

**Build:** Parse Python files and report a small set of useful custom rules with file/line/column and ignore controls. **Learn:** AST traversal, source positions, diagnostics, configuration, and editor/CI integration. **Structure:** `src/linter/rules/`, `visitor.py`, `config.py`, `cli.py`, fixture tests.

**Code steps:** (1) parse with `ast.parse` and report syntax errors. (2) define a diagnostic model and rule interface. (3) implement three precise rules. (4) traverse AST while tracking scope. (5) add per-line/project suppression. (6) produce text and JSON/SARIF-like output. **Flow:** file → AST → rule visitors → sorted diagnostics → formatter/exit code. **Prove it:** positive/negative fixtures, nested scopes, syntax errors, Unicode columns, suppressions, and version-specific syntax. **Portfolio upgrade:** make it a pre-commit hook and explain false-positive control.

## 84. Formatter for a Small Data Language

**Build:** Parse and consistently format a small configuration/query language without changing meaning. **Learn:** tokens, concrete syntax trees, pretty printing, comments, and idempotence. **Structure:** `src/formatter/lexer.py`, `parser.py`, `printer.py`, tests/golden files.

**Code steps:** (1) write a grammar and examples. (2) tokenize while preserving comments. (3) parse into syntax nodes. (4) print using indentation/line-width rules. (5) expose check/write/diff modes. (6) preserve or explicitly reject invalid input. **Flow:** source → tokens → tree → document layout → formatted source. **Prove it:** `format(format(x)) == format(x)`, parse equivalence, comments, long lines, invalid syntax, and golden diffs. **Portfolio upgrade:** add editor integration and benchmark a corpus.

## 85. Mini Programming Language Interpreter

**Build:** A language with numbers, strings, variables, conditions, loops, functions, and readable errors. **Learn:** lexing, parsing, ASTs, environments, evaluation, and language semantics. **Structure:** `src/minilang/lexer.py`, `parser.py`, `ast.py`, `interpreter.py`, `errors.py`, REPL, tests.

**Code steps:** (1) write grammar/semantics. (2) tokenize with line/column. (3) implement recursive-descent parser by precedence. (4) build AST. (5) evaluate in nested environments. (6) add functions/returns and REPL. **Flow:** text → tokens → AST → evaluation against environment → value/side effect. **Prove it:** precedence, lexical scope, recursion limit, type errors, undefined names, and error locations. **Portfolio upgrade:** add bytecode later and compare architecture.

## 86. Toy Relational Database

**Build:** Store tables on disk and support a documented subset of `CREATE`, `INSERT`, `SELECT`, filters, and indexes. **Learn:** pages, serialization, query execution, B-trees/hash indexes, and durability concepts. **Structure:** `db/storage.py`, `catalog.py`, `sql/`, `executor.py`, tests.

**Code steps:** (1) define typed row/page binary format with version/checksum. (2) build catalog and table heap. (3) parse a tiny SQL subset. (4) implement scans/filters/projections. (5) add one index type. (6) add write-ahead journal or atomic commit demonstration. **Flow:** SQL → plan → operators → storage pages → rows; writes become durable through an explicit protocol. **Prove it:** reopen persistence, corrupt/truncated page detection, duplicate keys, type mismatch, crash simulation, and scan/index equivalence. **Portfolio upgrade:** publish format/spec and query plan visualizer.

## 87. Git-Like Version Control System

**Build:** A learning VCS with init, add, commit, log, status, branch, checkout, and simple three-way merge. **Learn:** content-addressed storage, trees, DAGs, hashing, diffs, and merge conflicts. **Structure:** `src/vcs/objects.py`, `index.py`, `refs.py`, `worktree.py`, `merge.py`, tests.

**Code steps:** (1) store immutable blobs by hash. (2) create an index. (3) serialize tree/commit objects deterministically. (4) update refs atomically. (5) compare working/index/head states. (6) add branches and merge base. (7) perform simple line merge. **Flow:** files → blobs/tree → commit DAG; refs name commits; checkout materializes a tree. **Prove it:** deterministic hashes, changed/deleted files, branch switch safety, divergent histories, binary conflict, and interrupted ref update. **Portfolio upgrade:** visualize object graph and compare your subset with Git.

## 88. HTTP/1.1 Server from Sockets

**Build:** A learning HTTP server supporting a safe subset of requests, routing, static files, keep-alive limits, and concurrency. Do not expose it to the public internet. **Learn:** TCP, protocol parsing, buffering, timeouts, and security limits. **Structure:** `server/socket.py`, `http/parser.py`, `response.py`, `router.py`, tests.

**Code steps:** (1) read RFC sections for chosen subset. (2) incrementally parse request line/headers/body. (3) enforce byte/time/header limits. (4) construct correct responses. (5) add exact routes and safe static path resolution. (6) handle connections in threads/async tasks with caps. **Flow:** TCP bytes → framed request → handler → response bytes; buffers retain incomplete/pipelined data. **Prove it:** fragmented input, malformed length, oversized headers, traversal, slow client, keep-alive, and standard client interoperability. **Portfolio upgrade:** packet-level explanation and benchmark against a mature server, with caveats.

## 89. Minimal Async Web Framework

**Build:** On top of an ASGI server, create routing, request/response objects, middleware, dependency injection, and error handling. **Learn:** ASGI, async call chains, routing algorithms, and framework ergonomics. **Structure:** `framework/app.py`, `routing.py`, `requests.py`, `responses.py`, `middleware.py`, tests.

**Code steps:** (1) implement ASGI callable for HTTP scope. (2) read request events safely. (3) match static/path-parameter routes and methods. (4) create responses including streaming. (5) wrap handlers in middleware. (6) centralize exceptions and lifecycle. **Flow:** ASGI events → request → middleware chain → endpoint → response events. **Prove it:** async test client covers route precedence, method mismatch, streaming disconnect, exception, middleware order, and concurrent requests. **Portfolio upgrade:** build one small app and document missing production features.

## 90. Peer-to-Peer File Transfer

**Build:** Transfer authorized files between peers on a trusted network with discovery/manual addressing, chunks, resume, checksums, and optional library-based encryption. **Learn:** protocol design, framing, backpressure, integrity, and peer identity. **Structure:** `protocol/messages.py`, `peer.py`, `transfer.py`, `security.py`, tests/simulator.

**Code steps:** (1) specify versioned length-prefixed messages and limits. (2) exchange metadata and explicit acceptance. (3) stream numbered chunks. (4) persist resume bitmap. (5) verify full checksum before final rename. (6) authenticate/encrypt using established TLS/crypto primitives. **Flow:** handshake negotiates; sender streams under receiver backpressure; acknowledgements enable resume; verification commits. **Prove it:** disconnect/reconnect, duplicate/out-of-order chunk, corrupt data, wrong peer, full disk simulation, and malicious filename. **Portfolio upgrade:** include protocol specification and throughput/loss experiments.

## 91. Secure File Vault

**Build:** Encrypt files into a versioned vault with authenticated metadata, recovery key workflow, integrity verification, and safe extraction. **Learn:** threat modeling, envelope encryption, streaming AEAD patterns, key rotation, and secure deletion limits. **Structure:** `vault/format.py`, `crypto.py`, `keys.py`, `archive.py`, `cli.py`, tests.

**Code steps:** (1) threat-model attacker and non-goals. (2) design versioned format. (3) generate random data key; wrap it with password-derived/master key. (4) encrypt chunks with unique nonces and authenticated ordering. (5) verify before releasing plaintext. (6) prevent extraction traversal. **Flow:** key hierarchy separates data from credentials; authentication detects any alteration. **Prove it:** wrong key, swapped/missing chunks, modified header, rotation, large streaming file, and malicious paths. **Portfolio upgrade:** request security review and label it educational until audited.

## 92. Reproducible Task Runner

**Build:** Read a declarative task file, resolve dependencies, cache outputs, execute isolated commands, and show clear logs. **Learn:** build graphs, content hashes, subprocesses, environment control, and reproducibility. **Structure:** `runner/config.py`, `graph.py`, `cache.py`, `executor.py`, tests.

**Code steps:** (1) define safe explicit task schema. (2) validate DAG. (3) hash command, inputs, config, and declared environment. (4) skip when cache/output is valid. (5) execute with timeout and streamed logs. (6) run independent tasks concurrently with caps. **Flow:** config → DAG → fingerprints → ready/cached decision → subprocess result → cache metadata. **Prove it:** cycles, changed input, missing output, failed dependency, timeout, spaces in paths, signals, and cache corruption. **Portfolio upgrade:** visualize critical path and benchmark incremental builds.

## 93. Cross-Platform CI Quality Project

**Build:** Turn an earlier package into an example of strong automation across Python/OS versions, coverage, types, security checks, docs, and releases. **Learn:** CI matrices, caching, reproducible builds, supply-chain hygiene, and release gates. **Structure:** workflows, `pyproject.toml`, docs, changelog, release config.

**Code steps:** (1) define supported matrix. (2) run unit/integration tests and type/lint checks. (3) cache dependencies safely. (4) build artifacts once and inspect them. (5) use least-privilege permissions and pinned action versions. (6) publish only from protected tags/environments. **Flow:** commit → independent checks → build artifact → verification → approved release. **Prove it:** intentionally break each gate on a branch, test lowest dependency/Python where practical, and install built wheel. **Portfolio upgrade:** add badges sparingly and a release provenance explanation.

## 94. Observability Platform Demo

**Build:** Instrument several sample services and correlate logs, metrics, and traces in dashboards and alerts. **Learn:** telemetry signals, context propagation, sampling, cardinality, SLOs, and incident response. **Structure:** `services/`, `telemetry/`, `dashboards/`, `alerts/`, `runbooks/`, load generator.

**Code steps:** (1) define a user journey and SLI. (2) add structured logs with correlation IDs. (3) record bounded-cardinality metrics. (4) trace cross-service calls. (5) create latency/error/saturation dashboard. (6) write symptom-based alert and runbook. **Flow:** request context propagates; each component emits signals to collectors; dashboards join them by time/trace. **Prove it:** inject latency, errors, dependency outage, and dropped telemetry; verify alert and diagnosis. **Portfolio upgrade:** record a five-minute incident drill.

## 95. Distributed Key–Value Store

**Build:** A learning cluster with partitioning, replication, consistent hashing, quorum-like operations, hinted handoff, and repair simulation. **Learn:** distributed consistency, failure detection, vector/version concepts, and tradeoffs. **Structure:** `cluster/node.py`, `ring.py`, `replication.py`, `versions.py`, simulator, tests.

**Code steps:** (1) build a deterministic in-process network simulator. (2) place keys with consistent hashing. (3) replicate to N nodes. (4) coordinate reads/writes using chosen R/W rules. (5) detect/represent conflicts. (6) add repair and membership changes. **Flow:** coordinator maps key to replicas; acknowledgements decide success; later reconciliation repairs divergence. **Prove it:** partitions, delayed/duplicate messages, node restart, concurrent writes, rebalance, and invariant checks. **Portfolio upgrade:** state exactly which consistency guarantees your model does and does not provide.

## 96. Consensus Algorithm Simulator

**Build:** An in-memory Raft-style simulator for leader election and replicated log under controlled faults—not a production implementation. **Learn:** state machines, terms, voting, quorum, replicated logs, and deterministic simulation. **Structure:** `consensus/node.py`, `messages.py`, `log.py`, `simulator.py`, model tests.

**Code steps:** (1) read the paper and define invariants. (2) implement follower/candidate/leader states and randomized election timers. (3) request votes. (4) send heartbeats/log replication. (5) advance commit index only by quorum rules. (6) simulate partitions/restarts. **Flow:** deterministic event queue delivers messages/timers; nodes transition; committed log drives a state machine. **Prove it:** at most one leader per term, leader completeness scenarios, split vote, stale messages, partition/heal, and crash recovery model. **Portfolio upgrade:** animate terms/logs and cite the paper precisely.

## 97. Small-Language Compiler

**Build:** Compile the project-85 language to bytecode or another safe target with semantic checks and a small VM. **Learn:** symbol tables, type checking, intermediate representation, code generation, and runtimes. **Structure:** `compiler/semantic.py`, `ir.py`, `codegen.py`, `vm.py`, disassembler, tests.

**Code steps:** (1) freeze language spec. (2) resolve names/scopes in semantic pass. (3) optionally infer/check simple types. (4) lower AST to IR. (5) generate stack bytecode. (6) execute in bounded VM and add disassembly/debug info. **Flow:** source → AST → checked IR → bytecode → VM state/output. **Prove it:** compiler/interpreter equivalence on corpus, invalid programs, jumps, calls, stack limits, source locations, and deterministic output. **Portfolio upgrade:** measure optimization passes without overstating benefit.

## 98. End-to-End MLOps Pipeline

**Build:** Reproducibly train, validate, register, deploy, monitor, and roll back one modest model. **Learn:** data/model versioning, experiment tracking, validation gates, CI/CD, drift, and governance. **Structure:** `pipelines/`, `training/`, `registry/`, `serving/`, `monitoring/`, model cards/tests.

**Code steps:** (1) version dataset snapshot and schema. (2) create reproducible training config. (3) log parameters/metrics/artifacts. (4) gate candidate against baseline and slices. (5) register approved immutable model. (6) canary deploy. (7) monitor performance proxies/drift and rollback. **Flow:** versioned inputs → reproducible run → evidence gate → registry → controlled serving → feedback. **Prove it:** changed schema, failed metric gate, artifact tampering, canary regression, rollback, and training/serving feature parity. **Portfolio upgrade:** publish model card, lineage graph, and incident exercise.

## 99. Codebase Knowledge Assistant

**Build:** Index an authorized source repository and answer architecture questions with exact file/line citations, lexical/semantic retrieval, and an “insufficient evidence” response. **Learn:** code parsing, symbol graphs, retrieval, context selection, evaluation, and safe tool boundaries. **Structure:** `ingest/`, `symbols/`, `retrieval/`, `answering/`, `evaluation/`, UI/API.

**Code steps:** (1) honor ignore rules and secret filters. (2) parse files into symbols/chunks with commit/path/line provenance. (3) build lexical and optional vector indexes. (4) expand results through import/call relationships. (5) answer only from selected context and cite. (6) invalidate changed files incrementally. **Flow:** repository snapshot → traceable index → query retrieval/graph expansion → grounded answer. **Prove it:** versioned question set, renamed/deleted file, secret fixture, huge generated file, ambiguous symbol, no-answer question, and citation accuracy. **Portfolio upgrade:** report retrieval metrics and latency by repository size.

## 100. Capstone: Developer Collaboration Platform

**Build:** Combine your strongest skills into a platform where teams manage projects/issues, upload searchable documents, view activity analytics, and receive real-time notifications. Include authentication, organization isolation, background jobs, APIs, and a polished UI. **Learn:** system design, scope control, end-to-end delivery, operations, security, and communication. **Structure:** modular monolith first: `app/accounts`, `organizations`, `projects`, `documents`, `search`, `analytics`, `notifications`, `workers`; infrastructure/docs/tests.

**Code steps:** (1) write a one-page problem statement, personas, non-goals, threat model, and success metrics. (2) draw data model and request/event flows. (3) deliver a walking skeleton: sign in → create organization/project → create issue. (4) enforce tenant boundaries in every layer. (5) add document ingestion/search with citations. (6) add transactional outbox, worker, and real-time notifications. (7) add analytics from events. (8) test, containerize, deploy, observe, back up, and rehearse restore. **Flow:** synchronous commands update the primary database and outbox atomically; workers perform slow work; search/analytics are derived; UI consumes APIs/events. **Prove it:** tenant-isolation suite, authorization matrix, idempotent jobs, concurrent edits, search permissions, backup restore, load test, dependency failure, and end-to-end critical journey. **Portfolio upgrade:** publish architecture diagram, ADRs, demo video, live demo, seeded account, runbook, roadmap, and retrospective explaining what you deliberately did not build.

## Level 5 checkpoint

You now have material for deep technical interviews. Your credibility comes from explaining constraints, evidence, failures, and tradeoffs—not from calling a toy system “production-ready.” Choose projects that match the roles you want, and make the final capstone coherent rather than feature-heavy.
