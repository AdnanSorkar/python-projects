# Test Cases - Password Strength Checker

**Note:** Only fake/dummy passwords were used for testing. No real passwords were entered.

| Test ID | Input Password | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | `abc` | `1/5 Weak` (only lowercase met) | `1/5 Weak` | Pass |
| TC-02 | `Password1` | `4/5 Medium` (missing symbol) | `4/5 Medium` | Pass |
| TC-03 | `Dhaka2026!` | `5/5 Strong` (all 5 rules met) | `5/5 Strong` | Pass |
| TC-04 | *(empty)* | Prompts again without crashing | Prompts again | Pass |