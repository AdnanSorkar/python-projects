# Test Cases — Student Marks Analyzer

| Test ID | Inputs | Expected Outcome | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | `85`, `72`, `35`, `exit` | Average: `64.0`<br>Highest: `85.0`<br>Lowest: `35.0`<br>Passed: `2` (`66.67 %`)<br>Grades: `A`, `B`, `Fail` | Average: `64.0`<br>Highest: `85.0`<br>Lowest: `35.0`<br>Passed: `2` (`66.67 %`)<br>Grades: `A`, `B`, `Fail` | Pass |
| **TC-02** | `40`, `exit` | Average: `40.0`<br>Highest: `40.0`<br>Lowest: `40.0`<br>Passed: `1` (`100.0 %`)<br>Grade: `D` | Average: `40.0`<br>Highest: `40.0`<br>Lowest: `40.0`<br>Passed: `1` (`100.0 %`)<br>Grade: `D` | Pass |
| **TC-03** | `exit` *(no marks)* | `"No student marks were entered."`<br>No crash | `"No student marks were entered."`<br>No crash | Pass |
| **TC-04** | `""`, `abc`, `-5`, `105`, `80`, `exit` | Rejects empty, non-numeric, and out-of-range inputs<br>Records `80.0` (`A`)<br>Passed: `1` (`100.0 %`) | Rejects empty, non-numeric, and out-of-range inputs<br>Records `80.0` (`A`)<br>Passed: `1` (`100.0 %`) | Pass |