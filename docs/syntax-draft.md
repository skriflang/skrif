# skrif Syntax Draft (May 10, 2025)

## Goals
- Prioritize human readability with natural language-like syntax.
- Support web, games, VR, AI, ML, compiling to JavaScript initially.
- Outshine Python’s simplicity by 2030.

## Proposed Syntax

### Variables
- Syntax: `set [name] to [value]`
- Example: set x to 5 set name to "Alice"
- Rationale: The phrase `set ... to` reads like plain English, making it more intuitive for non-programmers than Python’s `x = 5`. It’s explicit and clear, reducing ambiguity for beginners.

### Functions
- Syntax: `define function [name]([parameters]) do [body] end`
- Example: define function calculate_sum(a, b) do set result to a + b return result end
- Rationale: `define function` is more descriptive than Python’s `def`.

### Web Routes
- Syntax: `define route [method] '[path]' do [body] end`
- Example: define route get '/users' do return "User list" end
- Rationale: This syntax is intuitive for web developers, resembling frameworks like Express.js. It supports skrif’s initial compilation to JavaScript, integrating with Node.js for web applications.

## Next Steps
- Test syntax with a lexer using Python/SLY to validate parsing.
- Share with the community on Discord (https://discord.gg/ctPxDGeB) for feedback.
- Expand syntax for conditionals, loops, and AI/ML use cases in future iterations.