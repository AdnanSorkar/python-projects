### Test Cases & Results Log — Robot Grid Navigator

This document outlines the test cases, expected behaviors, and verification results for the robot simulator application.

## Test Scenarios

| Test # | Input Command | Expected Outcome | Actual Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `FFRF` | Navigates steps, ends at `(1, 2)` facing East | `Moved to (0, 1); facing North`<br>`Moved to (0, 2); facing North`<br>`Moved to (1, 2); facing North`<br>`Moved to (1, 2); facing East`<br>`Final position: (1, 2); facing East` | Pass |
| **2** | `FFFFFF` | Hits top edge, triggers warnings, prints edge warning count | `Moved to (0, 1) ... (0, 4)`<br>`Warning: Blocked at edge (0, 4); facing North` (x2)<br>`Final position: (0, 4) North, 2 edge warning(s)` | Pass |
| **3** | `LLFF` | Turns South, hits bottom edge, triggers warnings | `Moved to (0, 0); facing West`<br>`Moved to (0, 0); facing South`<br>`Warning: Blocked at edge (0, 0); facing South` (x2)<br>`Final position: (0, 0) South, 2 edge warning(s)` | Pass |
| **4** | `FXR` | Handles invalid character `X` gracefully | `Moved to (0, 1); facing North`<br>`Invalid character 'X' entered.`<br>`Moved to (0, 1); facing East`<br>`Final position: (0, 1); facing East` | Pass |