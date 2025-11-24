#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from financial_researcher.crew import FinancialResearcher

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    print("Enter your company for research:")
    user_company = input()
    inputs = {
        'company': user_company,
    }

    try:

        # Create and run the crew
        result = FinancialResearcher().crew().kickoff(inputs=inputs)

        # Print the result
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)

        print("\n\nReport has been saved to output/report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()