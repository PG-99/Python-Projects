# Getting Started from Zero

## 1. Install the essentials

Install Python 3.12 or newer, Git, and a code editor such as Visual Studio Code. During Python installation on Windows, select **Add Python to PATH**.

Check the installation in a terminal:

```powershell
python --version
git --version
```

Create a free GitHub account and configure Git once:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email as your GitHub account if you want commits attributed to your profile. Never put passwords, API keys, or `.env` files in Git.

## 2. Learn this small Python core first

Before project 1, be able to recognize these ideas. You do not need to master them.

```python
name = "Ada"                         # variable and string
age = 20                             # integer
skills = ["Python", "Git"]          # list
profile = {"name": name, "age": age} # dictionary

def greeting(person: str) -> str:    # function, type hints, return value
    return f"Hello, {person}!"

for skill in skills:                 # loop
    print(skill)

if age >= 18:                        # condition
    print(greeting(name))
```

The core mental model is **input → validate → process → output**. Nearly every project in this roadmap follows it.

## 3. Start every project the same way

Replace `project-name` with a short lowercase name such as `tip-calculator`.

```powershell
mkdir project-name
cd project-name
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
git init
```

Create these files:

```text
project-name/
├── README.md
├── .gitignore
├── requirements.txt       # only when third-party packages are used
├── src/
│   └── main.py
└── tests/
    └── test_main.py
```

Put this in `.gitignore`:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.coverage
.env
dist/
build/
*.egg-info/
.DS_Store
Thumbs.db
```

Run the program with `python src/main.py`. When the project starts using packages, record them with a short, hand-maintained `requirements.txt`; for example `requests==2.32.4`. Avoid uploading the `.venv` folder.

## 4. Write code in small passes

For every project, use this loop:

1. Write one sentence describing the input and expected output.
2. Write function names before function bodies.
3. Make the smallest example work.
4. Move input/output away from the calculation logic.
5. Handle invalid input with helpful messages.
6. Add at least three tests: normal, edge, and invalid cases.
7. Improve names and remove repeated code.
8. Update the README and commit.

Example separation:

```python
def calculate_tip(bill: float, rate: float) -> float:
    """Pure logic: easy to test because it does not ask for input."""
    if bill < 0 or rate < 0:
        raise ValueError("Bill and rate must be non-negative")
    return round(bill * rate, 2)


def main() -> None:
    """User interface: collects input and displays output."""
    bill = float(input("Bill amount: "))
    rate = float(input("Tip percentage: ")) / 100
    print(f"Tip: ${calculate_tip(bill, rate):.2f}")


if __name__ == "__main__":
    main()
```

`calculate_tip` contains the rule. `main` handles the terminal. The last two lines mean “run `main` only when this file is executed directly,” which lets tests import the function without starting the prompt.

## 5. Test your work

Install the test runner inside the activated virtual environment:

```powershell
python -m pip install pytest
python -m pytest
```

Example test:

```python
import pytest
from src.main import calculate_tip


def test_calculate_tip() -> None:
    assert calculate_tip(100, 0.20) == 20


def test_negative_bill_is_rejected() -> None:
    with pytest.raises(ValueError):
        calculate_tip(-1, 0.20)
```

Tests are executable proof that the important behavior works. Test public behavior, not internal implementation details.

## 6. Make useful Git commits

Commit after small milestones:

```powershell
git add .
git commit -m "feat: calculate tip and split total"
git commit -m "test: cover invalid bill amounts"
git commit -m "docs: add setup and usage examples"
```

Useful prefixes are `feat`, `fix`, `test`, `docs`, `refactor`, and `chore`. A commit history should tell the story of how you built the project; do not make 50 artificial commits after everything is done.

## 7. Upload a project to GitHub

On GitHub, create a new empty repository. Do not initialize it with a README if you already made one locally. Then copy the repository URL and run:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/PROJECT-NAME.git
git push -u origin main
```

For later changes:

```powershell
git add .
git commit -m "feat: describe the change"
git push
```

If GitHub asks for authentication, use the browser sign-in offered by Git Credential Manager or an SSH key. Do not use your GitHub password as a command-line password.

## 8. Label projects so recruiters can scan them

On each GitHub repository page, add a short description and relevant **Topics** such as:

```text
python beginner-project cli pytest sqlite fastapi pandas machine-learning
```

Use only accurate topics. Add releases such as `v1.0.0` to mature projects, use GitHub Issues for planned improvements, and add a project screenshot or animated demo near the top of the README.

## 9. Protect secrets

Read API keys from environment variables:

```python
import os

api_key = os.getenv("WEATHER_API_KEY")
if not api_key:
    raise RuntimeError("Set WEATHER_API_KEY before running the app")
```

Keep local values in `.env`, keep `.env` in `.gitignore`, and publish an `.env.example` containing names but no secrets:

```dotenv
WEATHER_API_KEY=replace-me
```

If a secret is ever committed, deleting the line is not enough because Git keeps history. Revoke or rotate the secret immediately.

## 10. How to use each project guide

Each project has seven parts:

- **Build:** the outcome.
- **Learn:** the main concepts.
- **Structure:** suggested files; adapt it as the project grows.
- **Code steps:** the order in which to implement functions or classes.
- **How it works:** the data flow you should be able to explain.
- **Prove it:** tests and edge cases.
- **Portfolio upgrade:** one improvement that makes the repository more credible.

Do not add every possible feature. Finish the stated version, tag it `v1.0.0`, then choose a stretch improvement.

