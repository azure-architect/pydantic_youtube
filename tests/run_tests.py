# tests/run_tests.py
import pytest
import os
import sys

def run_tests():
    """Run all tests for the YouTube Transcript Analyzer"""
    print("Running YouTube Transcript Analyzer tests...")
    
    # Add the project root to the path
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    # Create output directory if it doesn't exist
    os.makedirs('test_outputs', exist_ok=True)
    
    # Run pytest with appropriate arguments
    pytest_args = [
        '-v',                  # Verbose output
        '--asyncio-mode=auto', # Handle asyncio tests
        'tests/'               # Test directory
    ]
    
    exit_code = pytest.main(pytest_args)
    
    # Print summary
    if exit_code == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ Tests failed with exit code {exit_code}")
    
    return exit_code

if __name__ == "__main__":
    sys.exit(run_tests())