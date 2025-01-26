# -*- coding: utf-8 -*-

# Fergus Leen, Cardiff,  Dec 2024

import argparse
import sys

def calculate_pension_credit_with_attendance_allowance(income_per_week, savings, is_single=True, attendance_allowance_rate=0):
    # Pension Credit thresholds for 2023/2024
    single_threshold = 201.05
    couple_threshold = 306.85
    
    # Calculate weekly income threshold based on single/couple status
    if is_single:
        income_threshold = single_threshold
    else:
        income_threshold = couple_threshold
    
    # Calculate savings adjustment (if savings are above 10,000)
    if savings > 10000:
        savings_adjustment = ((savings - 10000) // 500) * 1
    else:
        savings_adjustment = 0

    # Adjusted income threshold after considering savings
    adjusted_income_threshold = income_threshold - savings_adjustment
    
    # Add attendance allowance to the income (not means-tested)
    adjusted_income_threshold += attendance_allowance_rate

    # Determine if the applicant qualifies for Pension Credit
    if income_per_week < adjusted_income_threshold:
        return f"Qualifies for Pension Credit. Income below threshold by £{adjusted_income_threshold - income_per_week:.2f}."
    else:
        return f"Does not qualify for Pension Credit. Income exceeds threshold by £{income_per_week - adjusted_income_threshold:.2f}."

def get_attendance_allowance_rate(level):
    # Attendance Allowance rates for 2023/2024
    lower_rate = 68.10
    higher_rate = 101.75
    
    if level == "lower":
        return lower_rate
    elif level == "higher":
        return higher_rate
    else:
        return 0

def main():
    parser = argparse.ArgumentParser(description="UK Pension Credit and Attendance Allowance Calculator")

    # Define CLI arguments
    parser.add_argument("--income", type=float, required=True, help="Weekly income in GBP")
    parser.add_argument("--savings", type=float, required=True, help="Total savings in GBP")
    parser.add_argument("--single", action='store_true', help="Indicate if you are single")
    parser.add_argument("--attendance-allowance", choices=["none", "lower", "higher"], default="none", help="Attendance Allowance level (none/lower/higher)")
    
    # If no arguments are passed, display help
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Parse arguments
    args = parser.parse_args()

    # Determine Attendance Allowance rate
    attendance_allowance_rate = get_attendance_allowance_rate(args.attendance_allowance)

    # Calculate and print the result
    result = calculate_pension_credit_with_attendance_allowance(args.income, args.savings, args.single, attendance_allowance_rate)
    print(result)

if __name__ == "__main__":
    main()
