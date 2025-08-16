import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api

def solve_complex(problem, attempted_solutions=None, depth=0):
    if attempted_solutions is None:
        attempted_solutions = []
    
    print(f"\nDepth: {depth}")
    print(f"Attempting to solve: {problem}")
    print(f"Previous attempts: {len(attempted_solutions)}")
        
    solution = call_openrouter_api(
        f"You are a problem solver. Solve this problem or say 'WRONG' if your solution might be incorrect.\n\nProblem: {problem}\nPrevious attempts: {attempted_solutions}\nProvide a solution."
    )
    
    print(f"Got solution: {solution[:100]}...")
    
    if "WRONG" in solution:
        print("Solution marked as WRONG, trying again...")
        if len(attempted_solutions) > 5:
            print("Too many attempts, giving up")
            return "Failed to find solution after multiple attempts"
            
        return solve_complex(
            f"Previous solution was wrong. Try a different approach for: {problem}",
            attempted_solutions + [solution],
            depth + 1
        )
        
    print("\nVerifying solution...")
    verification = call_openrouter_api(
        f"You are a solution verifier. Verify if this solution is correct. Respond with 'CORRECT' or explain why it's wrong.\n\nProblem: {problem}\nProposed solution: {solution}\nIs this correct?"
    )
    
    print(f"Verification result: {verification}")
    
    if "CORRECT" in verification:
        print("Solution verified as CORRECT!")
        return solution
        
    print("Solution not verified, trying again...")
    return solve_complex(problem, attempted_solutions + [solution], depth + 1)

if __name__ == "__main__":
    question = "What is a minimal example of dependency injection in Python?"
    answer = solve_complex(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")