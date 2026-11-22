# Test Cases — Student Marks Analyzer

| Test ID | Inputs | Expected Outcome | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | `85`, `72`, `35`, `exit` | Average `64.0`, Highest `85.0`, Lowest `35.0`, Passed `2` (`66.67 %`), Grades `A`, `B`, `Fail` | Matches expected | Pass |
| **TC-02** | `40`, `exit` | Average `40.0`, Highest `40.0`, Lowest `40.0`, Passed `1` (`100.0 %`), Grade `D` | Matches expected | Pass |
| **TC-03** | `exit` *(no marks)* | `"No student marks were entered."`, no crash | `"No student marks were entered."`, no crash | Pass |
| **TC-04** | `""`, `"abc"`, `-5`, `105`, `80`, `exit` | Rejects blank, non-numeric, and out-of-range inputs; records only `80.0` (`A`) | Matches expected | Pass |