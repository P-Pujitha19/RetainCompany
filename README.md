# CHANGES.md

## Refactoring Summary

This document outlines the key changes made to the original `messy-migration` backend project to improve its quality, maintainability, and security.

---

## 🧱 Project Structure Changes

**Before:**
- Single-file Flask app (`app.py`)
- Mixed concerns: routing, logic, database in one file

**After:**
- Modular structure:
  - `app.py` – Entry point
  - `routes/` – All Flask route definitions
  - `services/` – Business logic
  - `models/` – Database interaction
  - `utils/` – Utilities (e.g., validation, hashing)
  - `config.py` – Centralized config

---

## 🔐 Security Improvements

- ✅ **Password hashing** using `werkzeug.security`
- ✅ **Validation of input** to prevent malformed data and injection
- ✅ **Error hiding**: No sensitive info in error messages
- ✅ **Parametrized SQL queries** to prevent SQL Injection

---

## 🧪 Functionality Tested

Manually tested these endpoints using `curl`:
- `POST /register`
- `POST /login`
- All working with appropriate response messages and codes

---

## ⚙️ Best Practices Applied

- ✅ Used `@app.errorhandler` for global error responses
- ✅ Used proper HTTP status codes (200, 201, 400, 401, 404)
- ✅ Clear naming and function responsibilities
- ✅ Avoided code duplication (e.g., reused validators)
- ✅ Structured logs with clear error reporting

---

## 🧪 Minimal Tests

- Manual tests for registration and login using `curl`
- JWT/token generation can be added if API protection is needed

---

## ❗ Major Issues Identified

| Issue | Fix |
|-------|-----|
| No password hashing | Used `generate_password_hash` & `check_password_hash` |
| SQL Injection risk | Switched to parameterized queries |
| Poor structure | Separated into routes/services/models |
| No validation | Added input validation with error responses |
| No status codes | Proper HTTP codes added |
| Sensitive error leaks | Custom error messages added |

---

## 🚧 Assumptions & Trade-Offs

- Assumed SQLite for simplicity; PostgreSQL can be added later.
- Kept login session simple (no token-based auth yet).
- No Docker setup — can be added if scaling is needed.
- Did not add rate limiting / brute-force protection for login.

---

## ⏳ What I'd Do With More Time

- Add JWT token-based authentication & protect routes
- Set up a Docker container with PostgreSQL
- Add unit + integration tests with `pytest`
- Set up CI/CD (e.g., GitHub Actions)
- Write API documentation with Swagger/OpenAPI

---

## 🤖 AI Usage

- Tool: ChatGPT (OpenAI)
- Used for: Refactoring guidance,validation logic
