# Skrif Language Specification

## Version
0.1.0 (May 13, 2025)

## Overview
Skrif is an open-source programming language designed for readability, compiling to JavaScript for web, games, VR, AI, and ML applications.

## File Extension
- **Extension**: `.skr`
- **Purpose**: All Skrif source code files use the `.skr` extension (e.g., `app.skr`, `hello.skr`).
- **Format**: Plain text, UTF-8 encoded.
- **Rationale**: `.skr` is short, memorable, and aligns with Skrif’s branding. Validation (docs/setup/extension-validation.md) confirms minimal conflicts with niche formats (e.g., PGP keyrings).
- **Usage**: Skrif’s compiler processes `.skr` files, and tools like VS Code extensions provide syntax highlighting for `.skr`.

## Syntax
- Variables: `set [name] to [value]` (e.g., `set x to 5`)
- Conditionals: `if [condition] then [body] end` (e.g., `if x greater than 3 then print x end`)
- Loops: `repeat while [condition] do [body] end`
- Arrays: `create array [name] with [elements]` (e.g., `create array numbers with [1, 2, 3]`)
- Objects: `create object [name] with { [key]: [value], ... }`

## Next Steps
- Expand syntax with error handling and arithmetic.
- Integrate `.skr` into compiler and tooling.