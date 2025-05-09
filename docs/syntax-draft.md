# skrif Syntax Draft (May 10, 2025)

## Goals
- Prioritize human readability with natural language-like syntax.
- Support web, games, VR, AI, ML, compiling to JavaScript initially.
- Outshine Python’s simplicity by 2030.

## Proposed Syntax

### Variables
- Syntax: `set [name] to [value]`
- Example: `set x to 5`
- Rationale: Reads like English, clearer than Python’s `x = 5` for beginners.

### Functions
- Syntax: `define function [name]([parameters]) do [body] end`
- Example: define function calculate_sum(a, b) do set result to a + b return result end
- Rationale: `define function` is more descriptive than Python’s `def`.

### Web Routes
- Syntax: `define route [method] '[path]' do [body] end`
- Example: define route get '/users' do return "User list" end
- Rationale: Intuitive for web developers, aligns with JavaScript ecosystem (Node.js).

## Next Steps
- Test syntax with a lexer using Python/SLY.
- Share with community on Discord (https://discord.gg/ctPxDGeB) for feedback.