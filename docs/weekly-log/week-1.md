# Skrif Development Log: Week 1 (May 9-15, 2025)

## Overview
Week 1 initialized the Skrif project, defined core syntax, set up project tracking, expanded syntax with conditionals, loops, arrays, and objects, and established a changelog to advance Phase 1: Planning and Design.

## Day 1 (May 9, 2025)
### Tasks Completed
- Initialized GitHub repository (github.com/skriflang/skrif) with MIT License.
- Standardized lowercase **skriflang** branding for organization (github.com/skriflang/skrif, @skriflang on X, Discord) and **skrif** for the language.
- Set up skrif.org domain via Namecheap and created Discord server (https://discord.gg/ctPxDGeB).
- Created initial files: README.md, LICENSE, .gitignore, docs/roadmap.md, src/main.py.
- Documented progress in docs/daily-log/day-1.md.

### Challenges and Solutions
- None reported.

### Key Outputs
- Repository: github.com/skriflang/skrif
- Domain: skrif.org
- Discord: https://discord.gg/ctPxDGeB
- Initial Files: README.md, LICENSE, .gitignore, docs/roadmap.md, src/main.py, docs/daily-log/day-1.md

### Time Spent
~1 hour

## Day 2 (May 10, 2025)
### Tasks Completed
- Drafted initial skrif syntax for variables, functions, and web routes in docs/syntax-draft.md.
- Tested a simple lexer for variable declarations in src/lexer_test.py using SLY.
- Created GitHub Project board (skrif Development) with To Do, In Progress, Done columns.
- Documented progress in docs/daily-log/day-2.md.

### Challenges and Solutions
- Incorrect Project board URL (github.com/users/skriflang/projects/3) caused 404 error. Fixed by using repository-scoped URL (github.com/skriflang/skrif/projects/9) and ensuring public visibility.

### Key Outputs
- Syntax Draft: docs/syntax-draft.md
- Lexer Test: src/lexer_test.py
- Project Board: [https://github.com/users/skriflang/projects/9]
- GitHub: [https://github.com/skriflang/skrif]
### Time Spent
~1 hour

## Day 3 (May 11, 2025)
### Tasks Completed
- Expanded skrif syntax with conditionals and loops in docs/syntax-draft.md.
- Updated lexer in src/lexer_test.py to parse new tokens for conditionals and loops.
- Created basic parser in src/parser_test.py to validate conditional syntax, achieving [('set', 'x', '5'), ('print', 'x', 5)].
- Documented progress in docs/daily-log/day-3.md.

### Challenges and Solutions
- Fixed Project board 404 error by creating a public, repository-scoped board at github.com/skriflang/skrif/projects/9.
- Encountered 'No such file or directory' error in Git Bash due to incorrect working directory. Fixed by changing to C:\Users\JanStrydom\Projects\skrif.
- Encountered ModuleNotFoundError: No module named 'src' in PowerShell. Fixed by adding src/__init__.py and setting PYTHONPATH.
- Encountered PowerShell dir error for src/__init__.py due to double underscore parsing. Fixed with quoted paths and -Path parameter.
- Encountered SLY syntax error in parser_test.py due to missing END token and NAME token ambiguity. Fixed by adding END to lexer, resolving NAME ambiguity with condition and print_name rules, and adding program/statements rules.
- Resolved Git non-fast-forward push error by pulling remote changes and cleaning up unwanted files (e.g., =, .pyc, src/src/).

### Key Outputs
- Syntax Draft: docs/syntax-draft.md
- Lexer: src/lexer_test.py
- Parser: src/parser_test.py
- Package: src/__init__.py
- Project Board: [https://github.com/users/skriflang/projects/9]
- GitHub: [https://github.com/skriflang/skrif]

### Time Spent
~1.5 hours

## Day 4 (May 12, 2025)
### Tasks Completed
- Expanded skrif syntax with arrays and objects in docs/syntax-draft.md.
- Updated lexer and parser in src/lexer_test.py and src/parser_test.py to handle arrays, achieving [('array', 'numbers', [1, 2, 3])].
- Initialized CHANGELOG.md to track skrif milestones.
- Transitioned from daily to weekly logs, documenting progress in this file.

### Challenges and Solutions
- None reported.

### Key Outputs
- Syntax Draft: docs/syntax-draft.md
- Lexer: src/lexer_test.py
- Parser: src/parser_test.py
- Changelog: CHANGELOG.md
- Weekly Log: docs/weekly-log/week-1.md
- Project Board: [https://github.com/users/skriflang/projects/9]
- GitHub: [https://github.com/skriflang/skrif]

### Time Spent
~2 hours

## Total Time Spent
~5.5 hours

## Alignment with Skrif’s Vision
Week 1 established Skrif’s open-source foundation, defined a readable syntax rivaling Python, built a functional lexer and parser for compilation to JavaScript, and set up scalable documentation with weekly logs, supporting web development goals and future expansion into games, VR, AI, and ML.