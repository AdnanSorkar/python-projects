# Test Cases — Fuel Efficiency Calculator

> **Safety Note:** Only valid test inputs and expected calculation metrics were used for verification.

### TC-01: Efficient Fuel Consumption

- **Input:** `450 km`, `30 L`, `120 TK`
- **Expected:** `15.0 km/L`, `8.00/km`, `L/100 km: 6.67`
- **Actual:** `15.00 km/L`, `8.00/km`, `L/100 km: 6.67`
- **Status:** Pass

### TC-02: Average Fuel Consumption

- **Input:** `100 km`, `10 L`, `120 TK`
- **Expected:** `10.0 km/L`, `12.00/km`, `L/100 km: 10.00`
- **Actual:** `10.00 km/L`, `12.00/km`, `L/100 km: 10.00`
- **Status:** Pass

### TC-03: Zero Fuel Input

- **Input:** `450 km`, `0 L`, `120 TK`
- **Expected:** Friendly message, no crash
- **Actual:** Friendly message, no crash
- **Status:** Pass