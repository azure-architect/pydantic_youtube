# run_all_tests.py
import asyncio
import subprocess
import sys
import time

async def run_test(script_name, description):
    """Run a test script and report results"""
    print(f"\n{'='*80}")
    print(f"RUNNING TEST: {description}")
    print(f"{'='*80}")
    
    try:
        # First check if Ollama is running
        try:
            import requests
            response = requests.get("http://localhost:11434/api/version")
            if response.status_code != 200:
                print("⚠️ Ollama may not be running. Please start Ollama first.")
                return False
        except:
            print("⚠️ Unable to connect to Ollama at http://localhost:11434")
            print("Please make sure Ollama is running before continuing.")
            proceed = input("Continue anyway? (y/n): ")
            if proceed.lower() != 'y':
                return False
        
        # Run the test script
        start_time = time.time()
        result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
        elapsed_time = time.time() - start_time
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("ERRORS:")
            print(result.stderr)
        
        success = result.returncode == 0 and "test failed" not in result.stdout.lower()
        print(f"\n{'✅ PASSED' if success else '❌ FAILED'} in {elapsed_time:.2f} seconds")
        return success
        
    except Exception as e:
        print(f"Error running test: {e}")
        return False

async def main():
    """Run all tests in sequence"""
    tests = [
        ("test_ollama_pydantic_integration.py", "Basic Ollama + PydanticAI Integration"),
        ("test_ollama_tools.py", "Ollama + PydanticAI Tool Calling"),
        ("test_ollama_graph.py", "Ollama + PydanticAI + Graph Workflow"),
        ("test_ollama_pydantic_db.py", "Ollama + PydanticAI + Database Storage")
    ]
    
    results = []
    
    for script, description in tests:
        success = await run_test(script, description)
        results.append((script, success))
    
    # Print summary
    print("\n" + "="*80)
    print("TEST RESULTS SUMMARY")
    print("="*80)
    all_passed = True
    for script, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        all_passed = all_passed and success
        print(f"{status}: {script}")
    
    print("\nOVERALL STATUS: " + ("✅ ALL TESTS PASSED" if all_passed else "❌ SOME TESTS FAILED"))

if __name__ == "__main__":
    asyncio.run(main())