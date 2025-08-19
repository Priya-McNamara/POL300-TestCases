#!/usr/bin/env python3
import unittest
import json
import sys
import io
import os

# Folder containing test files
TEST_FOLDER = '/autograder/tests'

# Redirect stdout to capture test print statements
old_stdout = sys.stdout
sys.stdout = mystdout = io.StringIO()

# Discover all tests
loader = unittest.TestLoader()
suite = loader.discover(TEST_FOLDER, pattern='*.py')

# Custom TestResult to track passes
class GradescopeResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.successes = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append(test)

# Run tests
runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2, resultclass=GradescopeResult)
result = runner.run(suite)

# Restore stdout
sys.stdout = old_stdout
test_output = mystdout.getvalue()

# Prepare Gradescope JSON
gradescope_results = {"tests": []}

# Add passing tests
for test in result.successes:
    gradescope_results["tests"].append({
        "name": str(test),
        "score": 1,
        "max_score": 1,
        "output": "Pass"
    })

# Add failed tests
for test, err in result.failures + result.errors:
    gradescope_results["tests"].append({
        "name": str(test),
        "score": 0,
        "max_score": 1,
        "output": err
    })

# Ensure results folder exists
os.makedirs('/autograder/results', exist_ok=True)

# Write JSON
with open('/autograder/results/results.json', 'w') as f:
    json.dump(gradescope_results, f, indent=2)

# Also save full text output for debugging
with open('/autograder/results/results.txt', 'w') as f:
    f.write(test_output)
