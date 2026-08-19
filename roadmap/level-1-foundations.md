# Level 1 — Python Foundations (Projects 1–20)

Use only the standard library unless a project says otherwise. Keep each project small, type the code yourself, and commit after every working feature.

## 1. Profile Greeter CLI

**Build:** Ask for a name, city, learning goal, and weekly study hours; print a formatted developer profile. **Learn:** variables, strings, `input`, conversion, f-strings, functions, and `if` statements. **Structure:** `src/main.py`, `tests/test_main.py`.

**Code steps:** (1) Create `clean_text(value)` to strip whitespace and reject empty text. (2) Create `weekly_message(hours)` that returns a different message for `<3`, `3–7`, and `8+`. (3) Create `build_profile(name, city, goal, hours)` that returns one multiline string. (4) Let `main()` collect values, convert hours with `int`, catch `ValueError`, and print the result. **How it works:** terminal strings enter `main`, validation normalizes them, pure functions build the output, and `main` displays it. **Prove it:** test whitespace, boundary hours 3 and 8, empty names, and non-numeric hours. **Portfolio upgrade:** support a `--name` argument with `argparse` and include a screenshot.

## 2. Four-Operation Calculator

**Build:** A calculator for `+`, `-`, `*`, and `/` that can repeat until the user quits. **Learn:** numeric types, branches, loops, exceptions, and pure functions. **Structure:** `src/calculator.py`, `src/main.py`, tests for calculator rules.

**Code steps:** (1) Implement `calculate(left, operator, right)`. (2) Map each accepted operator to its calculation; reject unknown operators with `ValueError`. (3) explicitly reject division by zero. (4) Add `read_number(prompt)` that keeps asking until `float` conversion succeeds. (5) Run a `while` loop in `main` with a quit choice. **How it works:** the interface parses values; `calculate` owns arithmetic and returns a number; the interface formats it. **Prove it:** test all operators, negatives, decimals, zero division, and invalid operators. **Portfolio upgrade:** add calculation history and parameterized pytest cases.

## 3. Unit Converter

**Build:** Convert temperature, length, and weight in both directions. **Learn:** formulas, dictionaries, function composition, and floating-point rounding. **Structure:** `src/converters.py`, `src/main.py`, `tests/`.

**Code steps:** (1) Write and test `c_to_f`, `f_to_c`, `km_to_miles`, `miles_to_km`, `kg_to_lb`, and `lb_to_kg`. (2) Store menu choices in a dictionary that maps a key to a function, source unit, and target unit. (3) Read the choice and value. (4) Call the selected function and format to two decimals. **How it works:** a lookup table replaces a long branch; the selected function transforms one validated number. **Prove it:** test known points such as `0°C = 32°F`, negative temperatures, zero, and round trips. **Portfolio upgrade:** add command-line flags and document floating-point precision.

## 4. Tip and Bill Splitter

**Build:** Calculate tip, total, and per-person cost. **Learn:** validation, decimal money, functions, and formatted output. **Structure:** `src/bill.py`, `src/main.py`, tests.

**Code steps:** (1) Use `Decimal` rather than `float` for money. (2) Implement `split_bill(subtotal, tip_percent, people)` returning a small dictionary or named tuple. (3) Reject negative subtotal/tip and fewer than one person. (4) Round currency with `quantize(Decimal("0.01"))`. (5) Build a friendly prompt in `main`. **How it works:** text is converted to exact decimal values, one function applies the business rules, then currency formatting is applied only for display. **Prove it:** test one and several people, rounding pennies, zero tip, and invalid people counts. **Portfolio upgrade:** show how leftover cents are distributed fairly.

## 5. Number Guessing Game

**Build:** Guess a random number with high/low hints and a limited number of attempts. **Learn:** `random`, loops, state, comparisons, and dependency injection. **Structure:** `src/game.py`, tests.

**Code steps:** (1) Implement `check_guess(secret, guess)` returning `low`, `high`, or `correct`. (2) Make `play(secret=None, max_attempts=7)` choose a random secret only when none is supplied. (3) Track attempts and prior guesses. (4) Reject out-of-range and repeated guesses without consuming an attempt. (5) Show a win/loss summary. **How it works:** the game loop changes state after each valid guess; injecting a known secret makes tests deterministic. **Prove it:** test each hint, attempt exhaustion, duplicate guesses, and bounds. **Portfolio upgrade:** add difficulty modes and persistent best scores in JSON.

## 6. Rock–Paper–Scissors Tournament

**Build:** Best-of-N matches against the computer. **Learn:** sets, dictionaries, random choices, input normalization, and game state. **Structure:** `src/rules.py`, `src/game.py`, tests.

**Code steps:** (1) Define valid moves and a `BEATS` dictionary. (2) Implement `winner(player, computer)` returning win/loss/tie. (3) Validate that match length is a positive odd number. (4) Loop until either side reaches the required wins. (5) Print round history and final score. **How it works:** the dictionary encodes the rules once; the loop updates two counters based on each outcome. **Prove it:** test every move pair and match-length validation; inject a predictable computer move chooser. **Portfolio upgrade:** add rock–paper–scissors–lizard–Spock by changing data rather than conditionals.

## 7. Mad Libs Story Generator

**Build:** Fill named placeholders in story templates and save the result. **Learn:** lists, dictionaries, files, string formatting, and reusable functions. **Structure:** `templates/`, `src/story.py`, `output/`, tests.

**Code steps:** (1) Put placeholders such as `{animal}` in a text file. (2) Use `string.Formatter().parse()` to discover unique field names. (3) Prompt once for each field and store answers in a dictionary. (4) call `template.format(**answers)`. (5) Save with a timestamped filename. **How it works:** the template is data, the parser extracts required inputs, and one dictionary fills every occurrence consistently. **Prove it:** test repeated fields, missing values, braces, and an empty template. **Portfolio upgrade:** let users select templates and contribute new ones through pull requests.

## 8. Password Strength Checker

**Build:** Score a password locally and explain how to improve it; never store the password. **Learn:** string methods, regular expressions, scoring rules, and privacy-aware design. **Structure:** `src/checker.py`, tests.

**Code steps:** (1) Implement separate checks for length, uppercase, lowercase, number, symbol, and repeated/common patterns. (2) Have `evaluate(password)` return a score and list of messages, not print. (3) Translate score ranges into weak/medium/strong. (4) Read hidden input with `getpass.getpass`. (5) explicitly state that strength is not a guarantee of security. **How it works:** independent rules produce facts; an aggregator calculates a transparent score; the UI shows suggestions. **Prove it:** test empty, long, Unicode, repeated, and common-password examples. **Portfolio upgrade:** read a small common-password list and explain the limits of rule-based scoring.

## 9. Palindrome and Text Analyzer

**Build:** Determine whether text is a palindrome while ignoring spaces, punctuation, and case; also report text statistics. **Learn:** comprehensions, Unicode, slicing, and separation of concerns. **Structure:** `src/analyzer.py`, tests.

**Code steps:** (1) Implement `normalize(text)` with `casefold()` and `str.isalnum()`. (2) Implement `is_palindrome(text)` by comparing normalized text with its reverse. (3) Add `statistics(text)` for characters, letters, digits, words, and unique words. (4) Print a readable report. **How it works:** normalization creates one comparison form without changing the original; analysis functions consume that form and return data. **Prove it:** test punctuation, mixed case, empty input, numbers, and Unicode. **Portfolio upgrade:** analyze every line of a supplied file with `argparse`.

## 10. Word Frequency Counter

**Build:** Read a text file and show the most common words. **Learn:** file handling, `Counter`, tokenization, sorting, and command-line arguments. **Structure:** `src/frequency.py`, `sample_data/`, tests.

**Code steps:** (1) Implement `tokenize(text)` with a documented regular expression. (2) Normalize tokens with `casefold`. (3) optionally remove stop words loaded from a file. (4) Count using `collections.Counter`. (5) Accept file path and top-N with `argparse`; handle missing files and encoding errors. **How it works:** the file becomes text, tokenization becomes a list, normalization makes equivalent words match, and the counter ranks them. **Prove it:** test punctuation, ties, Unicode, empty files, and stop words. **Portfolio upgrade:** export CSV and include a bar chart later when you learn plotting.

## 11. In-Memory To-Do CLI

**Build:** Add, list, complete, and delete tasks during one session. **Learn:** lists of dictionaries, IDs, CRUD operations, and menus. **Structure:** `src/todos.py`, `src/main.py`, tests.

**Code steps:** (1) Decide the task shape: `id`, `title`, `done`. (2) Implement pure `add_task`, `complete_task`, `delete_task`, and `list_tasks`. (3) Generate IDs without using list positions. (4) Make a menu loop that parses commands. (5) Display clear errors without crashing. **How it works:** one list is the state; operations return changed state or mutate it consistently; presentation translates it for humans. **Prove it:** test missing IDs, deleting completed tasks, blank titles, and ID stability. **Portfolio upgrade:** use `dataclass` for `Task` before adding persistence in project 15.

## 12. Contact Book

**Build:** Store contacts in JSON and search by name or phone. **Learn:** JSON, dictionaries, persistence, validation, and safe writes. **Structure:** `src/models.py`, `src/storage.py`, `src/main.py`, `data/contacts.json`, tests.

**Code steps:** (1) Define a contact with stable ID, name, phone, and email. (2) Write validation functions. (3) Implement `load_contacts` that returns an empty list if the file is absent. (4) Implement add/update/delete/search. (5) Save to a temporary file and replace the original only after serialization succeeds. **How it works:** storage turns JSON into Python data at startup; commands update validated objects; storage persists the complete state. **Prove it:** use temporary directories to test missing/corrupt files, duplicate IDs, and case-insensitive search. **Portfolio upgrade:** add import/export and document your JSON schema.

## 13. CSV Expense Tracker

**Build:** Record dated expenses, list them, and summarize totals by category. **Learn:** `csv`, `datetime`, `Decimal`, aggregation, and file schemas. **Structure:** `src/expense.py`, `src/report.py`, `data/expenses.csv`, tests.

**Code steps:** (1) Define columns `id,date,description,category,amount`. (2) Parse dates with `datetime.strptime` and money with `Decimal`. (3) Append records using `csv.DictWriter`, writing the header for a new file. (4) Read rows and convert types. (5) Aggregate totals and filter by date range/category. **How it works:** serialization converts typed records to strings; parsing restores types; reporting groups records without modifying them. **Prove it:** test quoted commas, malformed rows, leap dates, negative amounts, and exact sums. **Portfolio upgrade:** generate a monthly Markdown report and sample anonymized data.

## 14. JSON Quiz Engine

**Build:** Load multiple-choice questions, randomize them, grade answers, and show explanations. **Learn:** JSON schemas, randomization, loops, validation, and scoring. **Structure:** `data/questions.json`, `src/quiz.py`, tests.

**Code steps:** (1) Define a question schema with prompt, choices, answer index, category, and explanation. (2) Validate loaded questions before starting. (3) shuffle a copy so original data is unchanged. (4) Implement `ask_question` and `calculate_score`. (5) show missed-question review and percentage. **How it works:** content stays outside code; validated records feed a session; responses create results; summary derives from results. **Prove it:** test bad answer indexes, empty question sets, score calculations, and deterministic shuffling with a seed. **Portfolio upgrade:** add difficulty/category filters and a documented question-contribution format.

## 15. Persistent To-Do App

**Build:** Upgrade project 11 with JSON storage, due dates, priority, and filters. **Learn:** `dataclass`, serialization, migrations, and layered design. **Structure:** `src/models.py`, `src/repository.py`, `src/service.py`, `src/cli.py`, tests.

**Code steps:** (1) Create a typed `Task` dataclass. (2) Add `to_dict`/`from_dict` conversion. (3) Make a repository responsible only for load/save. (4) Make a service responsible for validation and task rules. (5) Make the CLI responsible only for prompts and display. (6) Add filters for status, priority, and overdue. **How it works:** CLI calls service, service changes domain objects, repository persists them—each layer has one reason to change. **Prove it:** unit-test service with an in-memory fake repository and separately test JSON round trips. **Portfolio upgrade:** add a `data_version` and migrate an older sample file.

## 16. Countdown Timer and Stopwatch

**Build:** A countdown with pause/resume plus a stopwatch with laps. **Learn:** time measurement, loops, state machines, and terminal updates. **Structure:** `src/timer.py`, `src/clock.py`, tests.

**Code steps:** (1) Use `time.monotonic()` for elapsed time, not the wall clock. (2) Create states `READY`, `RUNNING`, `PAUSED`, `FINISHED`. (3) Implement transitions and reject invalid transitions. (4) Calculate remaining time from elapsed durations rather than decrementing a counter. (5) keep terminal display separate. **How it works:** timestamps are facts; elapsed time is derived, so slow rendering does not accumulate timing drift. **Prove it:** inject a fake clock and test pause/resume, finish, reset, and invalid transitions. **Portfolio upgrade:** build a Pomodoro preset and add an audible notification.

## 17. Dice Roller and Probability Lab

**Build:** Parse expressions such as `2d6+3`, roll them, and compare simulations with expected values. **Learn:** parsing, random numbers, statistics, and generators. **Structure:** `src/dice.py`, `src/simulation.py`, tests.

**Code steps:** (1) Parse count, sides, and modifier with a full-match regex. (2) validate safe limits. (3) Implement `roll(expression, rng)` returning individual rolls and total. (4) Simulate many trials and count totals. (5) calculate empirical mean and theoretical expected value. **How it works:** parsing turns text into a model; the roller consumes that model; simulation repeatedly calls the same tested roller; reporting compares theory with observations. **Prove it:** test malformed expressions, `1d1`, modifiers, seeded results, and range constraints. **Portfolio upgrade:** output a text histogram and explain why simulation approaches theory.

## 18. Text Adventure Game

**Build:** Explore rooms, collect items, solve a condition, and reach one of two endings. **Learn:** state modeling, dictionaries, functions, and content-driven design. **Structure:** `data/world.json`, `src/models.py`, `src/engine.py`, tests.

**Code steps:** (1) Model rooms with description, exits, items, and optional requirements. (2) Validate that exits point to real rooms. (3) implement commands `look`, `go`, `take`, `inventory`, `use`, and `quit`. (4) Store player location and inventory. (5) Evaluate win/lose conditions after actions. **How it works:** JSON defines the world graph; the engine validates commands and changes player state; rendering describes the new state. **Prove it:** test unreachable exits, required items, unknown commands, repeated pickup, and each ending. **Portfolio upgrade:** add a map validator and let contributors add worlds without editing Python.

## 19. Safe Downloads Organizer

**Build:** Preview how files would be categorized by extension, then move only after confirmation. Use a sample folder, not your real Downloads folder, while learning. **Learn:** `pathlib`, file metadata, mappings, collisions, and safe filesystem operations. **Structure:** `src/plan.py`, `src/organize.py`, `sample_files/`, tests.

**Code steps:** (1) Map extensions to categories. (2) Implement `build_plan(source)` that returns proposed source/destination pairs without changing anything. (3) Ignore directories, hidden files, and your program files. (4) Resolve name collisions by adding a counter. (5) display a dry-run plan; move with `Path.replace` only after explicit confirmation. **How it works:** planning is read-only and testable; execution consumes an approved plan. **Prove it:** use temporary directories for uppercase extensions, duplicate names, unknown types, and empty folders. **Portfolio upgrade:** add undo by recording every successful move in a manifest.

## 20. Web Server Log Analyzer

**Build:** Analyze a sample access log for status codes, popular paths, traffic by hour, and malformed lines. **Learn:** regular expressions, generators, `Counter`, datetime parsing, and reporting. **Structure:** `sample_data/access.log`, `src/parser.py`, `src/report.py`, tests.

**Code steps:** (1) Define a `LogEntry` dataclass. (2) Parse one line with named regex groups and return `None` or a structured error for malformed input. (3) Stream the file line by line with a generator. (4) aggregate status families, paths, clients, bytes, and hours. (5) output terminal and JSON reports. **How it works:** the parser converts untrusted text into typed events; aggregators consume events one at a time, so large files need little memory. **Prove it:** test valid and invalid lines, timezone offsets, missing byte counts, and an empty log. **Portfolio upgrade:** benchmark it on a generated large file and publish the method and results.

## Level 1 checkpoint

You should now be comfortable with functions, collections, loops, validation, files, exceptions, tests, and small program structure. Polish projects 13, 15, or 20 as your first pinned repository. Before continuing, rebuild one early project without looking at your old code.
