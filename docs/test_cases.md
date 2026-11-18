# Test Cases & Results Log — Robot Grid Navigator

| Test # | Input Command | Expected Outcome | Actual Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `FFRF` | Ends at `(1, 2)` facing East[cite: 1] | `Moved to (0, 1)`<br>`Moved to (0, 2)`<br>`Moved to (1, 2)`<br>`Final Position: (1, 2); facing East` | Pass |
| **2** | `FFFFFF` | Ends at `(0, 4)` facing North with 2 edge warnings[cite: 1] | `Moved to (0, 1)` to `(0, 4)`<br>`Warning: Blocked at edge (0, 4); facing North` (x2)<br>`Final Position: (0, 4); facing North` | Pass |
| **3** | `LLFF` | Ends at `(0, 0)` facing South with 2 edge warnings[cite: 1] | `Warning: Blocked at edge (0, 0); facing South` (x2)<br>`Final Position: (0, 0); facing South` | Pass |
| **4** | `FXR` | Warns about invalid character `X`, ends at `(0, 1)` facing East[cite: 1] | `Moved to (0, 1)`<br>`Invalid character 'X' entered.`<br>`Final Position: (0, 1); facing East` | Pass |