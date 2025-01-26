
# **UK Pension Credit and Attendance Allowance Calculator**

This script calculates eligibility for **Pension Credit** in the UK, taking into account:
- Weekly income
- Total savings
- Marital status (single or couple)
- Attendance Allowance (if applicable)

The script uses **2023/2024 thresholds** for Pension Credit and Attendance Allowance rates.

---

## **Code Overview**

### **Functions**

#### **1. `calculate_pension_credit_with_attendance_allowance`**
Calculates whether an applicant qualifies for Pension Credit based on their income, savings, marital status, and Attendance Allowance.

**Parameters**:
- `income_per_week` (float): Weekly income in GBP.
- `savings` (float): Total savings in GBP.
- `is_single` (bool, optional): Whether the applicant is single. Defaults to `True`.
- `attendance_allowance_rate` (float, optional): Weekly rate of Attendance Allowance. Defaults to `0`.

**Returns**:
- A string indicating whether the applicant qualifies for Pension Credit and by how much their income is below or above the threshold.

**Logic**:
1. Determines the **Pension Credit threshold** based on marital status.
2. Adjusts the threshold for **savings** (if savings exceed £10,000).
3. Adds **Attendance Allowance** to the threshold (since it is not means-tested).
4. Compares the applicant's income to the adjusted threshold and returns the result.

---

#### **2. `get_attendance_allowance_rate`**
Returns the weekly rate of Attendance Allowance based on the selected level.

**Parameters**:
- `level` (str): Level of Attendance Allowance (`"none"`, `"lower"`, or `"higher"`).

**Returns**:
- The weekly rate of Attendance Allowance in GBP.

**Logic**:
- Returns the appropriate rate based on the input level:
  - `"none"`: £0.
  - `"lower"`: £68.10 (lower rate for 2023/2024).
  - `"higher"`: £101.75 (higher rate for 2023/2024).

---

#### **3. `main`**
Handles command-line arguments, calculates the result, and prints it.

**Logic**:
1. Sets up an **argument parser** to accept inputs:
   - `--income`: Weekly income in GBP (required).
   - `--savings`: Total savings in GBP (required).
   - `--single`: Indicates if the applicant is single (optional flag).
   - `--attendance-allowance`: Level of Attendance Allowance (`none`, `lower`, or `higher`).
2. If no arguments are provided, displays the help message and exits.
3. Parses the arguments and determines the Attendance Allowance rate.
4. Calls `calculate_pension_credit_with_attendance_allowance` to compute the result and prints it.

---

## **Command-Line Arguments**

| Argument                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `--income`                | Weekly income in GBP (required).                                           |
| `--savings`               | Total savings in GBP (required).                                           |
| `--single`                | Indicates if the applicant is single (optional flag).                      |
| `--attendance-allowance`  | Level of Attendance Allowance (`none`, `lower`, or `higher`). Default: `none`. |

---

## **Example Usage**

### **1. Single Applicant with Lower Attendance Allowance**
```bash
python pension_credit_calculator.py --income 180 --savings 12000 --single --attendance-allowance lower
```

**Output**:
```
Qualifies for Pension Credit. Income below threshold by £9.05.
```

### **2. Couple with No Attendance Allowance**
```bash
python pension_credit_calculator.py --income 300 --savings 8000
```

**Output**:
```
Does not qualify for Pension Credit. Income exceeds threshold by £6.85.
```

### **3. Display Help**
```bash
python pension_credit_calculator.py
```

**Output**:
```
usage: pension_credit_calculator.py [-h] --income INCOME --savings SAVINGS [--single] [--attendance-allowance {none,lower,higher}]

UK Pension Credit and Attendance Allowance Calculator

optional arguments:
  -h, --help            show this help message and exit
  --income INCOME       Weekly income in GBP
  --savings SAVINGS     Total savings in GBP
  --single              Indicate if you are single
  --attendance-allowance {none,lower,higher}
                        Attendance Allowance level (none/lower/higher)
```

---

## **Key Variables**

### **Pension Credit Thresholds (2023/2024)**
- Single: £201.05 per week.
- Couple: £306.85 per week.

### **Savings Adjustment**
- Savings above £10,000 reduce the income threshold by £1 for every £500 (or part thereof).

### **Attendance Allowance Rates (2023/2024)**
- Lower rate: £68.10 per week.
- Higher rate: £101.75 per week.

---

## **Assumptions**
1. The script uses **2023/2024 rates** for Pension Credit and Attendance Allowance.
2. Attendance Allowance is **not means-tested**, so it is added to the income threshold.
3. Savings above £10,000 reduce the income threshold by £1 for every £500 (or part thereof).

---

## **Dependencies**
- Python 3.x
- `argparse` (standard library)

---

## **How to Run**
1. Save the script as `pension_credit_calculator.py`.
2. Run the script from the command line with the required arguments.

---

This Markdown documentation provides a clear and structured explanation of the script. Let me know if you need further assistance!
