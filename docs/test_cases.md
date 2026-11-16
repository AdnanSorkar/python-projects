# Test Cases - Password Strength Checker CLI

This document outlines the test cases, expected behaviors, and verification results for the `p02-password-strength-checker` application.

## Test Scenarios

| Test Case ID | Input Scenario | Expected Behavior / Output | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | `abc` | Scores `1/5 (Weak)` and lists missing requirements (`Use uppercase letter`, `Use digit`, `Use special symbol`). | Matches expected | Passed |
| **TC-02** | `Password123!` | Scores `5/5 (Strong)` with no error/suggestion messages. | Matches expected | Passed |
| **TC-03** | *Blank Enter* (`""`) | Displays `"Password cannot be empty."` and re-prompts the user without crashing. | Matches expected | Passed |
| **TC-04**| *Spaces only* (`"   "`) | Catched by `.strip()`, displays `"Password cannot be empty."`, and re-prompts. | Matches expected | Passed |
| **TC-05** | `password123` | Scores `4/5 (Medium)` and requests the missing special symbol. | Matches expected | Passed |
| **TC-06** | `'exit'` (or `EXIT`) | Terminates loop gracefully, prints the session summary (e.g., total checked passwords), and exits. | Matches expected | Passed |

## Session Tracking Verification
- **Counter Test**: Verified `total_checked` increments per password and terminates correctly on `'exit'`.