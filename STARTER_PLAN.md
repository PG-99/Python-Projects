# A 12-Week Starter Plan

This plan assumes roughly 7–10 hours each week. It does not try to finish all 100 projects. Its purpose is to build enough fundamentals to complete and publish your first credible portfolio project. Slow it down if you need to; consistency matters more than speed.

## Weekly rhythm

- **Learn (20%):** read or watch material for the concepts listed in the project.
- **Build (55%):** type the code in small working pieces.
- **Test and debug (15%):** write tests and investigate failures.
- **Explain and publish (10%):** update the README, commit, and push.

Keep a short `LEARNING_LOG.md` in each repository. After every session, write the date, what you built, one problem, how you solved it, and the next small step. Rewrite those notes into a concise “What I learned” section before publishing.

## Weeks 1–2: syntax and functions

Build projects 1–4. Focus on values, types, conversion, branches, functions, return values, and readable error messages.

**Checkpoint:** Without looking at the guide, write a function that validates input, calculates a result, and returns it. Explain why calculation code should not call `input()`.

## Weeks 3–4: loops, collections, and testing

Build projects 5, 6, 9, and 10. Learn lists, dictionaries, sets, loops, random behavior, tokenization, and pytest.

**Checkpoint:** You can write normal, boundary, and invalid test cases. You can make random behavior testable by passing in a seed, secret, or random-number generator.

## Weeks 5–6: persistence and data modeling

Build projects 12–15. Spend extra time on project 15 because its layers—model, repository, service, and CLI—will reappear in larger applications.

**Checkpoint:** Delete your local data file, run the program, and confirm it recovers sensibly. Corrupt a copy and confirm it gives a helpful error. Explain serialization in plain language.

## Week 7: safe automation

Build project 19 or 20. Use only sample data. Practice preview/dry-run behavior, careful path handling, streaming input, and structured reports.

**Checkpoint:** Your tests create temporary folders/files and never depend on your personal folders.

## Week 8: SQL

Build project 23. Learn `CREATE TABLE`, primary/foreign keys, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, indexes, parameterized queries, and transactions.

**Checkpoint:** Draw your schema and explain why SQL values are passed as parameters instead of being inserted into query strings.

## Week 9: HTTP and APIs

Build project 21. Learn request/response, status codes, JSON, timeouts, caching, and API keys.

**Checkpoint:** Your program still behaves usefully when the network is slow, the server fails, or the JSON is missing a field. No secret appears in Git.

## Weeks 10–11: first web API

Build project 42, initially with in-memory data and then SQLite. Use the framework's generated API documentation to exercise each endpoint.

**Checkpoint:** Another person can create, read, update, filter, and delete tasks. Tests verify both successful and failed HTTP responses.

## Week 12: polish and publish

Choose project 15, 23, or 42 as your first pinned repository.

1. Remove unfinished features or clearly list them as future work.
2. Run every test from a fresh virtual environment.
3. Improve names, errors, docstrings, and type hints.
4. Add realistic sample data that contains no personal information.
5. Add screenshots or a 30–90 second demo.
6. Complete the portfolio checklist.
7. Ask a friend to follow the README without your help.
8. Fix what confused them, create release `v1.0.0`, and pin the repository.

## After week 12

Choose a direction rather than building everything in order:

| Target role | Recommended next projects |
|---|---|
| Python/backend developer | 30, 41, 42, 43, 57, 59, 63, 70 |
| Data analyst | 45, 46, 47, 49, 50, 68 |
| Data engineer | 46, 60, 67, 68, 69, 73 |
| Machine-learning engineer | 50–55, 75–80, 98 |
| Automation/tooling engineer | 31–40, 58, 81–84, 92–94 |
| Systems-focused engineer | 69, 70, 83–90, 95–97 |

For each new level, keep one “learning build” private or inside this roadmap and turn one strong result into a polished standalone public repository. This avoids filling your profile with near-identical exercises.
