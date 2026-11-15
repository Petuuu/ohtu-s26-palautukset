# Copilot instructions

## Project overview

This is a Python 3.14 Flask login/registration exercise. The application is started from
`src/index.py` and exposes the routes implemented in `src/app.py`; Jinja templates live
under `src/templates/`. User behavior is split into:

- `src/services/user_service.py`: validation, registration, and credential checks.
- `src/repositories/user_repository.py`: the process-local in-memory user store.
- `src/entities/user.py`: the `User` data object.

The repository is deliberately in-memory: restarting the Flask process or calling
`POST /tests/reset` clears users. The acceptance tests use `src/AppLibrary.py` to reset
that state and create users through the HTTP API, then use Browser/Playwright to exercise
the rendered UI. Keep the application running on port 5001 when running those tests.

## Environment and commands

Use the checked-in `uv.lock` and the project virtual environment:

```bash
uv sync
source .venv/bin/activate
```

Start the application from the project root:

```bash
uv run python src/index.py
```

Run all Robot Framework acceptance tests in a second terminal (application must be running):

```bash
uv run robot src/tests
```

Run one test case by name:

```bash
uv run robot -t "Login With Correct Credentials" src/tests/login.robot
```

The Browser tests default to a visible Chromium browser (`${HEADLESS}` is `false` in
`src/tests/resource.robot`). Set that variable to `true` for headless execution, for
example:

```bash
uv run robot -v HEADLESS:true src/tests
```

There is no build step or configured Python linter in this project. Generated Robot
outputs (`output.xml`, `log.html`, `report.html`, and browser logs) are ignored by Git.

## Testing conventions

Robot suites share browser setup, URLs, selectors, and application helper keywords
through `src/tests/resource.robot`. Each suite opens one browser in suite setup and
closes it in suite teardown. Test setup resets the in-memory repository before arranging
the user and page needed by that suite.

Prefer stable element IDs and visible button/link text, matching the existing Browser
library style. Add reusable UI actions and shared URLs to `resource.robot`; keep
assertions and scenario-specific setup in the suite that owns the behavior. Use the
existing `AppLibrary` keywords for state reset and API-level user creation rather than
duplicating `requests` calls in Robot files.

The Flask handlers report validation/authentication failures by flashing the exception
message and redirecting back to the relevant form. Preserve the user-facing messages
asserted by the Robot suites when changing service validation or route behavior.

## Source conventions

Keep the service/repository boundary intact: route handlers call `user_service`, and the
service calls the injected repository. The module-level `user_repository` and
`user_service` instances are the application defaults, while the repository constructor
supports injection for lower-level tests.

Imports assume `src` is on Python's import path, which is why the supported application
command runs `src/index.py` as a script. Templates should continue to use the base
`layout.html` and its `title`/`body` blocks.
