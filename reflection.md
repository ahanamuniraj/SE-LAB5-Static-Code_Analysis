
1. WHICH ISSUES WERE THE EASIEST TO FIX, AND WHICH WERE THE HARDEST? WHY?
The easiest issues to fix were style and formatting problems such as missing docstrings, use of print() statements, and naming convention changes. These were mostly straightforward syntax or documentation edits that didn’t affect the logic of the code.
The hardest issues were those involving exception handling and data validation. Replacing broad except: blocks with specific exception types required understanding which errors could realistically occur. Implementing input validation and safely handling JSON and file operations also required careful thought to prevent new runtime errors.
2. DID THE STATIC ANALYSIS TOOLS REPORT ANY FALSE POSITIVES? IF SO, DESCRIBE ONE EXAMPLE.
Yes, Pylint flagged the use of the global statement in the load_data() function as a warning, even though it was necessary for updating the global stock_data dictionary. In this specific context, the use of global was intentional and safe, so this warning can be considered a false positive rather than a real issue.

3. HOW WOULD YOU INTEGRATE STATIC ANALYSIS TOOLS INTO YOUR ACTUAL SOFTWARE DEVELOPMENT WORKFLOW?
I would integrate Pylint, Bandit, and Flake8 into a Continuous Integration (CI) pipeline using platforms like GitHub Actions. This ensures that every code commit or pull request is automatically analyzed before merging. Locally, I would configure pre-commit hooks so that the tools run automatically before any code is pushed, helping maintain consistent quality and security standards throughout development.

4. WHAT TANGIBLE IMPROVEMENTS DID YOU OBSERVE IN THE CODE QUALITY, READABILITY, OR POTENTIAL ROBUSTNESS AFTER APPLYING THE FIXES?
After applying the fixes, the code became more readable, secure, and maintainable. Logging replaced print statements, improving traceability. Exception handling is now precise and meaningful, reducing the chance of hidden errors. The addition of docstrings and consistent naming conventions enhanced clarity, while proper input validation and safe file handling made the system significantly more robust and production-ready. Overall, the final version achieved a Pylint score of 10/10, reflecting clean, professional-grade Python code.
