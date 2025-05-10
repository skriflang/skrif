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

### Conditionals
- Syntax: `if [condition] then [body] end` or `if [condition] then [body] else [body] end`
- Example: if x greater than 5 then set result to "Large" else set result to "Small" end
- Rationale: `if ... then ... else ... end` is explicit and readable, avoiding Python’s `if ...:` and indentation ambiguity for beginners.

### Loops
- Syntax: `repeat while [condition] do [body] end`
- Example: set count to 0 repeat while count less than 5 do set count to count + 1 print count end
- Rationale: `repeat while ... do ... end` clearly signals repetition, improving clarity over Python’s `while ...:`.

### Arrays
- Syntax: `create array [name] with [elements]`
- Example: create array numbers with [1, 2, 3] create array names with ["Alice", "Bob"]
- Rationale: `create array ... with` is explicit and readable, using square brackets for JavaScript familiarity.

### Objects
- Syntax: `create object [name] with { [key]: [value], ... }`
- Example: create object user with { name: "Alice", age: 25 }
- Rationale: `create object ... with` is descriptive, mirroring JSON for web compatibility.

### Error Handling
- Syntax: `try [body] catch [error] do [handler] end`
- Example: try set x to 5 if x greater than 10 then raise "Value too large" end catch error do print error end
- Rationale: `try ... catch ... end` is clear, aligning with JavaScript’s try-catch for web compatibility.

### Arithmetic Operations
- Syntax: `add [value1] to [value2]`, `subtract [value1] from [value2]`
- Example: set x to 5 set y to add 3 to x # y = 8 set z to subtract 2 from y # z = 6
- Rationale: `add ... to`, `subtract ... from` are verbose and readable, avoiding symbolic operators for clarity.

## Next Steps
- Implement error handling in parser.
- Explore error handling and async syntax.
- Add multiplication/division operations.
- Expand syntax for arrays, objects, and AI/ML constructs.
- Update lexer to parse conditionals and loops using Python/SLY.
- Develop a basic parser to validate conditional syntax.
- Share with community on Discord (https://discord.gg/ctPxDGeB) for feedback.
