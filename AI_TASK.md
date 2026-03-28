# AI_TASK.md

## Purpose

This file defines how the AI agent must behave while working on tasks in this repository.

The AGENTS.md defines architecture and engineering rules.  
This file defines execution behavior.

The agent must follow both.

---

## Core Behavior

### Rule: Be Intentional Before Acting

Before writing any code, the agent must:

1. understand the task
2. identify the affected layer(s)
3. identify the domain concepts involved
4. check architectural constraints from AGENTS.md

Do not start coding immediately.

---

### Rule: Think in Domain First, Code Second

The agent must:

- model the domain before implementing
- identify Entities, Value Objects, and Dependent Entities
- understand relationships and invariants

Code must reflect domain understanding, not just implementation mechanics.

---

### Rule: Follow TDD Strictly

The agent must always:

1. write a failing test first
2. implement the minimum code required
3. make the test pass
4. refactor safely

Do not skip steps.

Do not write production code before tests.

---

### Rule: Expand Scope Through TDD, Not Shortcuts

If a task reveals missing behavior:

1. stop current implementation
2. define the missing behavior explicitly
3. write a failing test for it
4. implement it
5. return to the original task

Do not bypass missing pieces with temporary or incorrect solutions.

---

### Rule: Never Break Architecture to Move Faster

The agent must never:

- bypass service layer
- instantiate dependencies directly
- violate layer boundaries

If a solution seems to require a violation:
- stop
- rethink the design
- introduce or use a service

---

### Rule: Prefer Correct Design Over Fast Completion

The goal is not to finish quickly.

The goal is to:
- preserve architecture
- maintain domain integrity
- produce consistent design

---

## Communication Behavior

### Rule: Explain When Necessary, Not Always

The agent should:

- explain decisions when they are not obvious
- explain architectural choices
- explain tradeoffs

The agent should not:
- over-explain trivial code
- add unnecessary verbosity

---

### Rule: Raise Architectural Concerns

If the agent detects:

- unclear domain modeling
- conflicting rules
- ambiguous requirements

It must:
- stop
- ask for clarification or
- propose alternatives

Do not guess silently.

---

### Rule: Suggest Improvements Proactively

The agent is encouraged to:

- suggest better naming
- suggest better abstractions
- suggest domain improvements

But must:
- keep suggestions relevant
- avoid overengineering

---

## Coding Behavior

### Rule: Do Not Invent Concepts

Only introduce new classes, methods, or modules when:

- they are required by the task
- they are justified by domain modeling
- they fit the architecture

Do not create speculative abstractions.

---

### Rule: Keep Changes Minimal and Focused

The agent must:

- change only what is necessary
- avoid unrelated refactors
- avoid large rewrites unless explicitly requested

---

### Rule: Maintain Consistency

The agent must:

- follow existing patterns in the codebase
- reuse existing services when possible
- keep naming consistent

---

### Rule: Respect Naming Rules

When naming is unclear:

- propose alternatives
- explain reasoning briefly

Do not force awkward names just to follow patterns blindly.

---

## Error Handling Behavior

### Rule: Fail Explicitly

The agent must:

- avoid silent failures
- avoid hidden fallbacks
- prefer clear errors

---

## Documentation Behavior

### Rule: Keep README Structure Section Updated

Whenever the agent:

- creates a new file
- creates a new folder
- moves or renames files or folders

It must update the **Structure** section of `README.md` accordingly.

The project structure documentation must always reflect the current state of the repository.

Do not postpone this update.

Documentation must be updated as part of the same task where the structural change occurs.

---

### Rule: Structure Documentation Must Be Accurate and Readable

When updating the Structure section:

- keep formatting clean and consistent
- reflect real folder hierarchy
- avoid outdated or missing entries
- do not include irrelevant files (e.g., caches, temporary files)

The README is considered part of the deliverable.

---

### Rule: Documentation Is Part of Definition of Done

A task that modifies project structure is not complete until:

- the README Structure section is updated
- the structure accurately reflects the current repository

Failing to update documentation is considered an incomplete task.

---

### Rule: Documentation Changes Do Not Require Tests

Changes to documentation files (e.g., README.md, LICENSE, markdown files) must NOT generate unit or functional tests.

TDD applies only to:
- domain logic
- application behavior
- services
- infrastructure code

TDD does NOT apply to:
- documentation
- markdown files
- comments
- static text content

Do not create tests for documentation updates under any circumstance.

---

### Rule: Do Not Treat Documentation as Testable Behavior

Documentation is not executable behavior.

Do not:
- create tests for documentation
- validate documentation through test cases
- introduce test files related to README or markdown updates

Documentation correctness is ensured by clarity and accuracy, not automated tests.

---

## Completion Behavior

### Rule: Validate Before Finishing

Before completing a task, the agent must ensure:

- tests exist and pass
- architecture rules were respected
- no shortcuts were introduced
- naming is clear
- changes are coherent

---

### Rule: Do Not Leave Partial Work

The agent must not:

- leave TODOs as placeholders for required logic
- leave broken flows
- leave untested behavior

---

## Pre-Completion Safety Checks

### Rule: Run a Sanity Security Review Before Finishing

Before considering any task complete, the agent must perform a sanity security review of all created or modified files.

This review must look for accidental exposure of sensitive or environment-specific information, including but not limited to:

- API keys
- tokens
- passwords
- private credentials
- secrets in code, tests, fixtures, or documentation
- absolute file system paths
- server-specific paths
- local machine usernames
- private URLs or internal endpoints
- internal IP addresses
- private certificates or keys
- sensitive environment variable values
- accidental debug data
- hardcoded confidential identifiers

If any such content is found, the agent must remove, replace, or sanitize it before finishing the task.

A task is not complete until this review is done.

---

### Rule: Never Commit Sensitive Data

The agent must never introduce into the repository:

- real secrets
- real credentials
- real private tokens
- real private keys
- real production endpoints
- real internal infrastructure details

When examples are needed, use placeholders such as:

- `YOUR_API_KEY`
- `YOUR_TOKEN_HERE`
- `/path/to/project`
- `example.com`
- `127.0.0.1`

Never use realistic sensitive values.

---

### Rule: Sanitize Environment-Specific Details

The agent must avoid exposing local or server-specific information in the codebase.

Replace or generalize:

- absolute local paths
- personal home directories
- machine-specific folders
- internal hostnames
- deployment-specific structure details

Prefer neutral examples and portable paths.

Good examples:

    /path/to/project
    ./data/config.json
    ${PROJECT_ROOT}/config

Avoid examples like:

    /home/username/private-project/config.json
    /var/www/internal/app/secrets.json

---

### Rule: Review Documentation and Tests for Leaks

The security sanity review must include:

- production code
- tests
- fixtures
- examples
- documentation
- README updates
- configuration files

Sensitive information often leaks through non-production files.
Do not review code only.

---

### Rule: Replace Secrets With Placeholders

If a task requires showing configuration examples, use placeholders instead of real values.

Examples:

- `STRATFORGE_API_KEY=YOUR_API_KEY`
- `DATABASE_URL=postgresql://user:password@localhost:5432/dbname`

Do not use real internal values, even temporarily.

---

### Rule: Security Review Is Part of Definition of Done

A task that creates or modifies files is not complete until the sanity security review has been performed.

This review is mandatory before the agent considers the work ready for commit or push.

---

### Rule: Passing Tests Is Not Enough for Completion

Passing tests, lint, and formatting do not replace the mandatory sanity security review.

The agent must check both:
- technical correctness
- accidental exposure risks

---

## Sensitive Data Red Flags

The agent must pay extra attention to:

- strings that look like tokens or keys
- `.env` values copied into examples
- stack traces exposing local paths
- copied terminal output containing usernames or directories
- test fixtures containing real secrets
- config files with filled credentials
- internal domains, hosts, or IPs

---

## When Unsure

If uncertain, the agent must prefer:

- architectural correctness
- domain clarity
- explicit design
- testability

If uncertainty remains:
- ask or explain the ambiguity
- do not guess silently

---

## Anti-Behavior Rules

The agent must not:

- break layer boundaries
- instantiate dependencies directly
- create helper/utils modules
- introduce business logic outside the domain layer
- bypass TDD
- implement without understanding the domain
- overengineer prematurely
- ignore AGENTS.md rules

---

## Execution Mindset

The agent should behave as:

- a senior software engineer
- a domain-aware designer
- a careful refactorer
- a strict follower of architectural rules

Not as:

- a code generator
- a shortcut taker
- a guess-based implementer
