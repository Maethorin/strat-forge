# AGENTS.md

## Project Overview

- Project name: `StratForge`
- Package name: `strat_forge`
- Source layout: `src/strat_forge`
- Tests: `tests`
- Build backend: `hatchling`
- Supported Python: `>=3.14`

StratForge is a Python library that implements a GURPS-based engine intended to support multiple game genres, with a primary focus on RTS games.
It will be served as a python lib that can be installed and imported in others python projects. 
It will also have, in a future, C++ wrapper;

This document defines the mandatory engineering, architecture, modeling, and workflow rules for AI coding agents working in this repository.

The agent must treat this file as a hard constraint set, not as optional guidance.

This project must be implemented in **Python 3.14** and follow a strict **object-oriented design**.  
The architecture is based on **DDD-style layered boundaries**, with explicit rules about dependency direction, object creation, and development workflow.

The purpose of this file is to guide AI coding agents working in this repository so they make changes that are consistent with the project's architectural and engineering rules.

## Environment

- Preferred virtual environment root: `$VIRTUALENVS`
- Preferred Python executable: `${VIRTUALENVS}/strat-forge/bin/python`
- Preferred pip executable: `${VIRTUALENVS}/strat-forge/bin/pip`

---

## Common Commands

```bash
${VIRTUALENVS}/strat-forge/bin/python -m pip install -e ".[dev]"
${VIRTUALENVS}/strat-forge/bin/python -m pytest
${VIRTUALENVS}/strat-forge/bin/python -m ruff format --check .
${VIRTUALENVS}/strat-forge/bin/python -m ruff check .
```

---

## Project Rules

- Use the provided virtual environment for all local project commands.
- Keep the package in a `src` layout under `src/strat_forge`.
- Put tests under `tests/`.
- Keep dependencies and tool configuration in `pyproject.toml`.
- Prefer small, typed, importable modules over large script-style files.
- Update `README.md` when setup or usage changes.
- Do not add new runtime dependencies unless they are necessary for the library.
- Keep the public package API explicit in `src/strat_forge/__init__.py` when exports are added.

---

## Core Principles

### Rule: Python Version
- The project must be compatible with **Python 3.14**.
- Do not introduce code that depends on older compatibility patterns unless explicitly required.
- Prefer modern Python features when they improve clarity and maintainability.
- Always use type annotations
- Always create docstrings

### Rule: Main Stack
- Language: Python
- Test strategy: TDD
- Architecture style: DDD-inspired layered architecture
- Design style: strict OOP

### Rule: Object-Oriented Design Only
- The codebase must always use **OOP**.
- Model behavior inside classes, not as loose procedural functions.
- Avoid a procedural design disguised as classes.
- Prefer cohesive classes with clear responsibilities.
- Encapsulate domain behavior inside domain objects whenever appropriate.
- The python module, class name and method name should tell a story based on the domain

### Rule: Domain-Driven Design Boundaries
The project follows a layered architecture inspired by DDD.

Layers:

- `api`
- `forge`
- `infrastructure`
- `services`

#### Layer Responsibilities

##### `api`
Responsible for exposing the public interfaces of the library.

This layer may contain:
- request/input models
- validation logic
- serialization/deserialization logic
- adapters for user-facing inputs/outputs
- external libraries intended to support those concerns, such as Pydantic

##### `forge`
This is the domain layer of the library.

It contains:
- domain entities
- value objects
- domain services
- domain policies
- domain rules
- invariants
- engine behavior
- domain exceptions

Rules for this layer:
- It contains the core business/domain model of the engine
- It may import only:
  - Python standard library modules
  - modules from inside this project
- Avoid unnecessary external dependencies in this layer
- Domain concepts, rules, invariants, and behavior belong here

##### `infrastructure`
Support layer for technical concerns.

This layer may contain:
- I/O operations
- filesystem access
- HTTP integrations
- persistence implementations
- gateways/adapters to external systems
- other technical implementations that are not part of the domain itself

This layer must not own business rules.

##### `services`
Contains service factories used for decoupling, dependency injection, circular-import avoidance, and controlled module resolution.

This layer exists to:
- provide class-based service access
- centralize object resolution
- coordinate instantiation rules across the project
- reduce direct coupling between modules
- resolve project modules dynamically through `import_module` when needed

##### `exceptions`
The top-level `strat_forge.exceptions` module contains the library custom exception hierarchy.

This module exists to:
- centralize reusable library exceptions
- expose shared exception types across layers
- keep exception naming and reuse explicit

### Rule: Allowed External Libraries
External libraries may be used only when they clearly belong to the responsibility of the layer where they are introduced.

Examples:
- `api`: validation, serialization, schema tools such as Pydantic
- `infrastructure`: HTTP clients, persistence tooling, external integration libraries

Do not introduce external libraries into `forge` unless explicitly approved.

---

## Python-Specific Design Rules

### Rule: Prefer cached_property for Expensive or Repeated Access

Use `cached_property` when:
- the value is computed once and reused
- the computation is non-trivial
- the result is immutable for the lifecycle of the instance

Avoid recomputing values that can be cached safely.

Do not use caching if:
- the value can change during the object's lifecycle
- the computation is trivial

---

## Method and Property Design Rules

### Rule: Prefer Properties Over Parameterless Getters

If a method:
- takes no arguments
- represents a value or state

Prefer using a property instead of a `get_*` method.

Good:
    unit.health

Avoid:
    unit.get_health()

Use methods only when:
- behavior is being executed
- side effects are involved
- parameters are required

---

### Rule: Do Not Choose staticmethod Based on Implementation Detail

Do not decide between instance, classmethod, or staticmethod based only on whether the method uses `self` or `cls`.

Instead, decide based on object-oriented design intent.

Use:
- instance methods → when behavior belongs to the object
- classmethods → when behavior relates to class construction or class-level concepts
- staticmethods → only when the method truly has no relation to class or instance semantics

Prefer classmethods over staticmethods when in doubt, especially for factory or domain-related behavior.

Avoid turning domain behavior into static utility functions.

---

## Naming Conventions

---

## Allowed Dependency Directions

The following calls/import directions are allowed:

- `api -> forge`
- `api -> infrastructure`
- `api -> services`
- `forge -> services`
- `forge -> infrastructure`
- `infrastructure -> services`
- `services -> forge` through `import_module`
- `services -> infrastructure` through `import_module`
- `services -> api` through `import_module` when explicitly required

These directions apply to imports and effective dependency usage.

### Rule: Respect Layer Boundaries
Do not introduce dependencies outside the allowed directions above.

If a change appears to require an illegal import:
1. stop,
2. identify the architectural conflict,
3. introduce or use an appropriate service class in `services`,
4. preserve the dependency rules.

### Rule: No Layer Violations
If you need a dependency that breaks this rule:
1. stop
2. create/use a service
3. resolve via services layer

## Forbidden Dependency Directions

The following are forbidden unless the architecture is explicitly changed:

- direct imports from `services` to `forge`
- direct imports from `services` to `infrastructure`
- direct imports from `services` to `api`
- `infrastructure -> api`
- `forge -> api`

### Rule: No Layer Shortcuts
Never bypass the architecture because a direct import feels simpler.

If a dependency appears to require an illegal direction:
1. stop
2. identify the boundary violation
3. resolve the dependency via the correct service class
4. preserve the architecture

Violating a boundary is considered an architectural defect.

---

## Object Creation Rules

### Rule: Every Class Must Have a Factory Method
Every class must provide a factory method, even if it is minimal.

Examples:
- `create`
- `build`
- `from_payload`
- `from_config`

At minimum, a class may expose:

```python
@classmethod
def create(cls):
    return cls()
```

Use richer factory names when they communicate intent better, such as:
- `create`
- `build`
- `from_payload`
- `from_config`
- `from_values`
- `for_context`
- `for_a_card`

---

### Rule: No Direct Instantiation
A class must never directly instantiate another class that it depends on.

Never do:

    dependency = SomeClass()

Always do:

    dependency = SomeModuleService.get_some_class_instance()

Or, when the service is responsible for module resolution:

    dependency_module = SomeModuleService.domain
This rule applies even if the target class is simple.

---

### Rule: All Collaborator Resolution Must Be Service-Mediated
Whenever one class needs another class instance or domain module, it must obtain it through the appropriate service class.

This is required for:
- decoupling
- dependency injection
- construction consistency
- circular import avoidance
- architectural traceability

---

### Rule: No Hidden Construction
Do not hide instantiation inside:
- random utility functions
- unrelated modules
- ad-hoc local closures
- convenience shortcuts

Construction must remain explicit and discoverable.

---

## Service Layer Rules

### Rule: Use the `services.py` Module
Service classes live in `src/strat_forge/services.py` unless the architecture is intentionally expanded.

Do not create a parallel `service` module or package.

The canonical layer name is `services`.

---

### Rule: Service Classes Resolve Modules Through `import_module`
The base `Service` class resolves configured modules through `import_module`.

Service implementations should:
- set the `_domain` class attribute to the fully qualified module path they expose
- access the target module through the `domain` class property
- raise a library exception when used without a concrete domain configuration

Do not replace this mechanism with direct imports in the service class body when the purpose is decoupled module resolution.

---

### Rule: One Service Class Per Module Family
For each module or component family, there should be a corresponding service class responsible for serving its main components.

Example:
- `infrastructure/connections.py`
- corresponding service class: `ConnectionService`

Examples of acceptable names:
- `ConnectionService`
- `CombatService`
- `UnitService`
- `TerrainService`
- `BattleRuleService`

Prefer singular, explicit names.

---

### Rule: Service Classes Must Be Focused
A service class must have a clear reason to exist.

Service classes may:
- create instances
- provide configured implementations
- resolve dependencies
- centralize access to components
- wire collaborating objects

Service classes must not become generic dumping grounds.

---

### Rule: Service Methods Should Be Classmethods
Prefer service access through classmethods.

Example style:

    class UnitService:
        @classmethod
        def get_builder(cls):
            ...

This keeps usage predictable and consistent across the project.

---

## Domain Modeling Rules

### Rule: Rich Domain Model
The `forge` layer must contain behavior, not just data.

Avoid an anemic domain model.

Domain objects should:
- protect invariants
- express rules
- own meaningful behavior
- collaborate explicitly through domain concepts

Do not reduce domain classes to passive data containers.

---

### Rule: Entity vs Value Object
When modeling domain concepts, explicitly decide whether the concept is an **Entity** or a **Value Object**.

Use an **Entity** when:
- identity matters
- the object is tracked over time
- equality should not be based only on field values
- the object has autonomy

Use a **Value Object** when:
- the concept is defined by its values
- it is immutable or should behave as immutable
- identity does not matter
- it represents a domain concept such as cost, position, range, modifier, or rule parameter

Do not mix the two concepts carelessly.

---

### Rule: Entities Have Independent Identity and Lifecycle

An Entity is a domain object that:

- has a unique identity
- is tracked over time
- has a lifecycle independent of other objects
- can exist on its own within the domain

An Entity is not defined by its attributes, but by its identity.

Entities may:
- change state over time
- participate in multiple relationships
- be referenced by other objects

Examples:
- Unit
- Player
- Battle

---

### Rule: Distinguish Between Root Entities and Dependent Entities

There are two types of Entities in the domain:

#### Root Entities
- have independent lifecycle
- can exist on their own
- are accessed directly via services
- define aggregate boundaries

#### Dependent Entities
- have identity
- belong to a parent Entity (aggregate)
- do not have an independent lifecycle
- cannot exist outside their parent
- are created, modified, and removed through the parent Entity

A Dependent Entity must not be accessed directly from outside its aggregate.

All interactions must go through the owning Entity.

---

### Rule: Aggregates Define Ownership Boundaries

An aggregate is composed of:
- one Root Entity
- zero or more Dependent Entities
- zero or more Value Objects

The Root Entity is responsible for:
- enforcing invariants
- controlling access to Dependent Entities
- coordinating modifications

External code must never manipulate Dependent Entities directly.

---

### Rule: Avoid Primitive Obsession
Do not overuse raw primitives when a domain concept deserves its own type.

Prefer domain types instead of loosely passing:
- plain integers
- plain strings
- plain dictionaries
- unstructured tuples

For example, if the domain repeatedly uses concepts like range, coordinates, resource cost, unit category, terrain modifier, or combat bonus, consider creating explicit value objects.

---

## Naming Rules

### Rule: No Helpers / No Utils
Never create modules or classes named:
- `helper`
- `helpers`
- `util`
- `utils`
- `common`
- `misc`
- `base_helper`
- any vague equivalent

Every component must have a clear architectural or domain identity.

If something appears “shared,” decide what it actually is:
- entity
- value object
- domain service
- policy
- validator
- serializer
- mapper
- gateway
- repository
- factory
- specification
- adapter

Do not hide uncertainty under vague names.

---

### Rule: Explicit Naming Only
Names must reveal either:
- domain meaning
- technical responsibility

Prefer:
- `DamagePolicy`
- `MovementCost`
- `BattlefieldSerializer`
- `UnitValidator`
- `HttpBattleGateway`

Avoid vague names like:
- `Helper`
- `Manager`
- `Processor`
- `Handler`
- `Thing`
- `DataUtils`

Unless the term has a very clear, domain-specific meaning, do not use it.

---

### Rule: Naming Conventions
Use consistent naming patterns:

- validators: `SomethingValidator`
- serializers: `SomethingSerializer`
- policies: `SomethingPolicy`
- services: `SomethingService`
- gateways: `SomethingGateway`
- repositories: `SomethingRepository`
- factories: `SomethingFactory` only when the domain meaning truly requires a factory object

Prefer factory **methods** over factory **classes** unless a dedicated factory class adds real clarity.

---

### Rule: Prefer Enums To Value Objects When Simplicity Is Enough

If a concept:
- has a fixed, limited set of possible values
- does not require behavior
- does not enforce invariants beyond enumeration

Prefer using an Enum instead of creating a Value Object.

Use Value Objects only when:
- behavior is required
- validation/invariants are needed
- the concept carries domain logic

Favor simplicity (KISS) when appropriate.

---

### Rule: Avoid Name Collisions Across Layers

Avoid using the same method names across different layers when they represent different responsibilities.

Names should reflect:
- the layer
- the intent
- the context

---

### Rule: Layer-Based Naming Conventions

#### API Layer
- Use gerund form
- Examples:
    - getting_unit
    - creating_battle
    - calculating_damage

#### Service Layer
- Use gerund + indefinite article when appropriate
- Examples:
    - getting_a_unit
    - creating_a_battle
    - calculating_a_damage

#### Domain Layer (forge)
- Use present tense, direct action
- Examples:
    - get_unit
    - create_battle
    - calculate_damage

---

### Rule: Prefer Clarity To Strict Rules

If naming becomes awkward or unclear:
- propose alternatives
- prioritize clarity and domain meaning over rigid patterns

---

### Rule: Naming Rules Are Guidelines, Not Constraints

Naming conventions must improve clarity.

If a naming rule makes the code:
- harder to read
- unnatural in English
- confusing in context

Then propose a better alternative and justify it.

---

## Public API Rules

### Rule: The API Layer Is a Contract
Because StratForge is a library, the `api` layer represents a contract with its consumers.

Do not:
- rename public API classes casually
- break signatures without need
- move public entry points without a strong reason
- leak infrastructure details into the API

Prefer backward-compatible changes whenever possible.

---

### Rule: Thin API, Rich Domain
Business rules belong in `forge`, not in `api`.

The API layer should:
- validate
- adapt
- serialize
- coordinate entry and exit

It must not become the primary home of engine behavior.

---

## Error Handling Rules

### Rule: Custom Exceptions Live in `strat_forge.exceptions`
All reusable custom exceptions for the library must be declared in `src/strat_forge/exceptions.py`.

Use this module for:
- shared architectural exceptions
- domain exceptions
- API-facing library exceptions
- infrastructure exceptions that are part of the library contract

Do not scatter custom exception declarations across unrelated modules unless a very strong reason is documented.

---

### Rule: Domain Errors May Inherit From the Shared Exceptions Module
Exceptions that represent domain rule violations may be defined in `forge` only when they build on the shared exception hierarchy from `strat_forge.exceptions`.

Examples:
- invalid game state
- invalid action according to rules
- impossible domain transition
- broken invariant

---

### Rule: API Translates Errors for Consumers
The `api` layer may translate domain/internal errors into user-facing error structures.

Do not bury domain exceptions inside infrastructure code.

---

### Rule: No Silent Fallbacks
Do not hide architectural or domain errors behind silent fallback behavior unless the fallback is explicitly part of the domain design.

Fail clearly.

---

## Testing Rules

### Test Structure

#### Rule: Tests Must Be Class-Based
All tests must be organized inside test classes.

Do not write standalone test functions.

Prefer:

    class TestCreatingChar(BaseTest):
        def test_should_have_a_char_class_defined(self):
            ...

Tests must be grouped by behavior or responsibility inside clearly named test classes.

---

### BDD Test Naming

#### Rule: Tests Must Follow BDD Naming Style
Tests must follow a behavior-driven naming style.

Test class names should describe the behavior or use case being tested.

Examples:
- `TestCreatingChar`
- `TestCalculatingDamage`
- `TestGettingUnitPosition`

Test method names must describe the expected behavior in a clear BDD style.

Preferred pattern:

    test_should_<expected_behavior>

Example:

    def test_should_have_a_char_class_defined(self):
        ...

Test names must describe behavior, not implementation details.

Avoid vague names such as:
- `test_char`
- `test_combat_1`
- `test_method`

---

### Test Directory Layout

#### Rule: Tests Must Be Organized by Test Type First
The `tests` directory must be organized first by test type.

The first-level test directories must be:

- `tests/unit`
- `tests/functional`

---

#### Rule: Tests Must Mirror Project Structure
Inside each test type directory, tests must mirror the structure of the project source tree as closely as possible.

Examples:

- `tests/unit/test_package.py`
  tests the root file:
- `package.py`

- `tests/functional/strat_forge/forge/test_combat.py`
  tests the source file:
- `src/strat_forge/forge/combat.py`

This structure is mandatory.

The goal is to make it immediately clear which test file corresponds to which production file.

---

#### Rule: Test Files Must Map Clearly to Production Files
Each test file must correspond clearly to a production module.

Prefer naming test files as:

    test_<module_name>.py

Examples:
- `test_combat.py`
- `test_character.py`
- `test_movement.py`

Avoid unclear or grouped file names unless the tested behavior genuinely spans multiple modules.

---

#### Rule: Unit and Functional Tests Must Not Be Mixed
Unit tests and functional tests must remain separated.

Do not place:
- functional tests inside `tests/unit`
- unit tests inside `tests/functional`

If uncertain:
- unit tests verify isolated behavior
- functional tests verify behavior across component boundaries

--- 

### Rule: Development Is Always TDD
All feature development must follow TDD.

Mandatory cycle:
1. write a failing test
2. implement the minimum code needed
3. make the test pass
4. refactor safely

Do not start by writing large blocks of production code first.

---

### Rule: Tests Come Before New Behavior
If behavior does not yet exist, the test must come first.

If the test already exists and is failing, use it as the driver.

---

### Rule: Follow Newly Discovered Requirements Through TDD
While implementing one feature, the agent may discover that another method or class must also be introduced or changed.

When that happens:
1. explicitly recognize the discovered requirement
2. write the failing test for that requirement
3. implement it
4. make that test pass
5. return to the original failing test
6. continue until the original feature is complete

Do not hack around missing collaborators.

---

### Rule: No Partial TDD
Do not leave the codebase with:
- untested behavior
- half-created collaborators
- “temporary” direct instantiation
- TODO-based architectural gaps used to bypass design

---

### Rule: Prefer Unit Tests First
Default to focused unit tests first.

Add integration-style tests when necessary to cover:
- layer interaction
- infrastructure wiring
- serialization boundaries
- end-to-end library flows

---

## Project Structure Rules

Preferred top-level structure:

- `api/`
- `forge/`
- `infrastructure/`
- `services.py`
- `exceptions.py`
- `tests/`

If the project grows, subpackages should preserve layer meaning.

Do not create folders that weaken the architecture.

Examples of bad additions:
- `shared/`
- `common/`
- `helpers/`
- `misc/`

unless they are explicitly defined with a clear and justified architectural meaning.

---

## Testing and Quality Commands

The agent should prefer the following commands when validating work, if these tools are configured in the repository.

### Tests
    pytest

### Lint
    ruff check .

### Format
    ruff format .

If the repository later defines different commands, follow the repository-defined commands.

---

## Change Safety Rules

### Do Not Break Architecture

- respect layers
- respect services
- respect factories

---

### Small Changes

Prefer small, controlled changes.

---

### No Shortcuts

Never break rules just to pass tests.

---

## Coding Style

### Explicit Code

- avoid magic
- prefer clarity

---

### Small Methods

- one responsibility
- clear naming

---

### Rich Domain

- business logic stays in forge
- api is thin
- infrastructure supports only

---
### Rule: Do Not Break Method Signatures Across Multiple Lines

Method and function definitions must not split parameters across multiple lines.

Even if the line exceeds typical length limits (e.g., 80 or 100 characters), keep the full signature on a single line.

Preferred:

    def create(cls, name: str, governing_attribute: SkillAttribute, difficulty: SkillDifficulty, category: SkillCategory) -> Self:

Avoid:

    def create(
        cls,
        name: str,
        governing_attribute: SkillAttribute,
        difficulty: SkillDifficulty,
        category: SkillCategory,
    ) -> Self:

This rule exists to:
- improve readability
- keep method signatures compact and scannable
- maintain consistency across the codebase

Line length limits must not override this rule.

---

### Rule: Formatting Tools Must Respect Project Style

Automatic formatters (e.g., ruff format) must not override project-specific style rules.

If a formatter conflicts with these rules:
- adjust the formatter configuration
- or avoid applying formatting that breaks project conventions

---

### Rule: Do Not Enforce PEP 8 Line Length Limits

The project does NOT enforce the PEP 8 line length recommendation (e.g., 79/80/100/120 characters).

Long lines are acceptable when they improve:
- readability
- cohesion
- code clarity

Do NOT:
- break lines artificially to satisfy line length limits
- split method signatures, function calls, or expressions solely to fit within a character limit

Line breaks must be driven by readability, not by arbitrary limits.

Modern development environments provide horizontal scrolling and wide displays, making strict line length limits unnecessary.

This rule overrides any formatter or tool default related to line length.

---

### Rule: Prefer Readability To Formatter Conventions

If a formatting tool suggests changes that reduce readability in order to enforce style rules (such as line wrapping), those changes must be ignored.

Project-specific readability rules always take precedence over generic style conventions.

---

## Import Rules

### Rule: Always Import Modules, Never Classes or Functions Directly

All imports must be module-level.

Do NOT import classes, functions, or objects directly from modules.

Forbidden:

    from strat_forge.services import RollService

Required:

    from strat_forge import services

Usage must always be qualified through the module:

    services.RollService

Exception:

    from strat_forge import classproperty

`classproperty` is the only approved direct object import for this rule while it remains exposed as a package-level descriptor instead of a dedicated module.

---

### Rule: Do Not Use Redundant Module Aliases

Do not alias a module to the same generic name it already exposes at the end of its path when that alias adds no clarity.

Forbidden:

    import strat_forge.exceptions as exceptions

Required:

    from strat_forge import exceptions

Use aliases only when they introduce real disambiguation or improve clarity in a meaningful way.

---

### Rule: Use Module Names as Namespaces

Modules must act as explicit namespaces.

All access to classes, functions, or constants must be done through the module.

Good:

    services.RollService
    forge.Unit
    infrastructure.HttpClient

Avoid:

    RollService
    Unit
    HttpClient

---

### Rule: Do Not Flatten Imports

Do not reduce import verbosity by importing internal symbols directly.

Explicit module access improves:

- readability
- traceability
- architectural clarity
- consistency across the codebase

---

### Rule: Preserve Layer Visibility Through Imports

Imports must reflect the architectural layer being accessed.

Example:

    from strat_forge import services

This makes the dependency explicit and aligned with the architecture.

Avoid hiding the origin of a dependency through direct symbol imports.

---

### Rule: Avoid Ambiguous Symbol Origins

Code must make it immediately clear where a symbol comes from.

A reader must be able to identify the source module without searching for the import.

Explicit module-qualified access is mandatory.

---

## Implementation Checklist

Before finishing a task, the agent must verify all of the following:

1. the correct layer was identified
2. dependency direction remains legal
3. tests were written first or updated first through TDD
4. the implementation is object-oriented
5. every relevant class exposes a factory method
6. no class directly instantiates its collaborators
7. collaborator access happens through service classes
8. no helper/utils/common dumping ground was introduced
9. naming is explicit and domain-driven
10. business rules remain in `forge`
11. infrastructure does not own domain logic
12. public API changes are deliberate and safe
13. tests pass
14. lint passes

---

## Forbidden Patterns

The following patterns are forbidden unless explicitly requested:

- direct instantiation of collaborators
- layer boundary shortcuts
- helper/utils/common dumping-ground modules
- business logic in infrastructure
- business rules in serializers
- business rules in validators
- ad-hoc service locator behavior outside the `services` layer
- silent fallback behavior that hides errors
- procedural orchestration spread across unrelated modules
- anemic domain objects when behavior belongs in the domain
- introducing third-party dependencies into `forge`

---

## When Unsure

If the correct solution is unclear, prefer the option that:

- preserves architectural boundaries
- keeps the domain rich
- centralizes dependency resolution in services
- reduces coupling
- improves naming clarity
- strengthens testability
- keeps the public API stable

If uncertainty remains, leave a short note explaining the architectural tradeoff instead of taking a shortcut.

---

## Definition of Done

A task is complete only when all of the following are true:

- tests were written or updated first through TDD
- the architecture is respected
- dependency directions are legal
- no direct collaborator instantiation exists
- all relevant classes expose factory methods
- services mediate object resolution
- no helpers/utils/common dumping grounds were introduced
- names are explicit and meaningful
- business logic remains in the domain
- tests pass
- lint passes

---
