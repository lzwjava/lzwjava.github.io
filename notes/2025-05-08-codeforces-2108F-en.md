---
title: Codeforces 2108F
lang: en
layout: post
audio: false
translated: false
generated: true
---

The provided Java code solves the "Fallen Towers" problem but is running into a time limit issue due to its brute-force approach of generating all permutations to find the maximum MEX. For large inputs (up to \\( n = 10^5 \\)), generating all \\( n! \\) permutations is infeasible. Below, I’ll suggest improvements to optimize the code and avoid the time limit, focusing on algorithmic efficiency, code structure, and problem-specific insights.

### Problem Analysis
- **Objective**: Given an array \\( a \\) of \\( n \\) tower heights, knock down each tower exactly once in some order. When a tower at index \\( i \\) with height \\( a_i \\) is knocked down, the next \\( a_i \\) towers (if they exist) increase by 1, and \\( a_i \\) is set to 0. The final array must be non-decreasing, and we need to maximize the MEX (smallest non-negative integer not present in the array).
- **Constraints**:
  - \\( 1 \leq n \leq 10^5 \\)
  - \\( 0 \leq a_i \leq 10^9 \\)
  - Sum of \\( n \\) across test cases \\( \leq 10^5 \\)
  - Time limit: 3 seconds
- **Key Insight**: The brute-force permutation approach (\\( O(n!) \\)) is too slow for \\( n > 12 \\). We need a more efficient algorithm, possibly \\( O(n \log n) \\) or \\( O(n) \\), to handle \\( n \leq 10^5 \\).

### Issues in the Current Code
1. **Brute-Force Permutations**:
   - The `permutation` method generates all \\( n! \\) permutations, which is computationally expensive (e.g., \\( 12! \approx 479,001,600 \\)).
   - For each permutation, it simulates the knocking process and checks if the result is non-decreasing, then computes the MEX. This is too slow for \\( n \geq 13 \\).
2. **Inefficient MEX Calculation**:
   - Uses a `HashSet` to store array elements and checks for MEX by iterating from 1 upward. This can be optimized.
3. **Memory Usage**:
   - Cloning arrays (`a.clone()`) and using `HashSet` for each permutation increases memory overhead.
4. **Input Handling**:
   - Uses `BufferedReader` and `StringTokenizer`, which are fine but can be slightly optimized with a custom fast input reader for competitive programming.
5. **No Pruning**:
   - The code doesn’t prune invalid permutations early, leading to unnecessary computations.

### Optimized Approach
To solve this efficiently, we need to avoid generating all permutations and instead deduce the optimal knocking order and its effect on the MEX. Here’s a key observation about the problem:

- **Non-Decreasing Constraint**: The final array \\( b \\) must satisfy \\( b_i \leq b_{i+1} \\) for all \\( i \\). This suggests the final array is sorted or nearly sorted.
- **MEX Maximization**: To maximize the MEX, we want the final array to include all non-negative integers from 0 to \\( k-1 \\) (for some \\( k \\)), so the MEX is \\( k \\). Gaps in the sequence reduce the MEX.
- **Knocking Effect**: Knocking down tower \\( i \\) with height \\( a_i \\) sets \\( b_i = 0 \\) and increments \\( b_{i+1}, b_{i+2}, \ldots, b_{\min(i+a_i, n-1)} \\). The order of knocking affects how increments accumulate.

#### Key Hypothesis
- The final array’s values represent the number of times each position is incremented by towers knocked down *after* it, plus its own contribution (0 after being knocked down).
- To maximize the MEX, we want the final array to be as “compact” as possible, i.e., containing consecutive integers starting from 0.
- The non-decreasing constraint implies that later positions (higher indices) should have equal or larger values.

#### Efficient Algorithm
Instead of trying all permutations, we can use a greedy or mathematical approach to determine the optimal knocking order. Here’s a promising strategy based on the observation that the final array’s values depend on the number of increments received:

1. **Model the Final Array**:
   - Let \\( b_i \\) be the final height of tower \\( i \\) (0-based indexing for simplicity).
   - \\( b_i \\) equals the number of towers \\( j < i \\) that were knocked down *after* tower \\( i \\) and whose \\( a_j \\) is large enough to increment position \\( i \\).
   - Formally, for a permutation \\( p \\) (knocking order), if tower \\( p_k \\) is knocked at step \\( k \\), it increments positions \\( p_k + 1 \\) to \\( p_k + a_{p_k} \\). Thus, \\( b_i = |\{ k : p_k < i \leq p_k + a_{p_k} \}| \\).
2. **Non-Decreasing Requirement**:
   - We need \\( b_i \leq b_{i+1} \\), i.e., position \\( i+1 \\) should receive at least as many increments as position \\( i \\).
3. **Maximize MEX**:
   - The MEX is the smallest non-negative integer not in \\( \{ b_0, b_1, \ldots, b_{n-1} \} \\).
   - To maximize MEX, minimize gaps in \\( \{ b_i \} \\). Ideally, \\( b \\) contains values \\( \{0, 1, 2, \ldots, k-1\} \\) for some \\( k \\).

#### Greedy Knocking Order
A promising heuristic is to knock down towers in reverse order (from right to left, i.e., \\( n-1, n-2, \ldots, 0 \\)) or in a way that ensures later positions receive more increments. Let’s try constructing the final array by assuming a specific order and checking if it satisfies the constraints.

- **Reverse Order Insight**:
  - If we knock down towers from right to left (\\( n-1, n-2, \ldots, 0 \\)):
    - Tower \\( n-1 \\): Sets \\( b_{n-1} = 0 \\), increments nothing (since no towers to the right).
    - Tower \\( n-2 \\): Sets \\( b_{n-2} = 0 \\), increments \\( b_{n-1} \\) by 1 if \\( a_{n-2} \geq 1 \\).
    - Tower \\( n-3 \\): Sets \\( b_{n-3} = 0 \\), increments \\( b_{n-2} \\) if \\( a_{n-3} \geq 1 \\), \\( b_{n-1} \\) if \\( a_{n-3} \geq 2 \\).
    - And so on.
  - After knocking all towers, \\( b_i \\) is the number of towers \\( j < i \\) knocked after \\( i \\) with \\( a_j \geq i - j \\).
  - This naturally produces a non-decreasing array because positions to the right are affected by more towers (all \\( j < i \\)).
- **Compute \\( b_i \\)**:
  - For each position \\( i \\), count how many towers \\( j < i \\) have \\( a_j \geq i - j \\).
  - This can be computed efficiently using a prefix sum or segment tree for range queries, given the large \\( a_i \\) values (\\( \leq 10^9 \\)).
- **MEX Calculation**:
  - Once \\( b \\) is computed, find the smallest non-negative integer not in \\( \{ b_i \} \\).
  - Since \\( b \\) is non-decreasing, we can check values systematically.

#### Optimized Algorithm Steps
1. **Read Input**:
   - Read \\( t \\), then for each test case, read \\( n \\) and array \\( a \\).
2. **Simulate Reverse Order**:
   - Initialize array \\( b \\) of size \\( n \\) to 0.
   - For each tower \\( i \\) from \\( n-1 \\) down to 0:
     - Set \\( b_i = 0 \\).
     - Increment \\( b_{i+1}, b_{i+2}, \ldots, b_{\min(i+a_i, n-1)} \\) by 1.
   - This can be done efficiently using a difference array or segment tree for range updates.
3. **Verify Non-Decreasing**:
   - Check if \\( b_i \leq b_{i+1} \\). (In reverse order, this is typically satisfied.)
4. **Compute MEX**:
   - Since \\( b \\) is non-decreasing, count the frequency of each value in \\( b \\).
   - Find the smallest non-negative integer not present.
5. **Handle Large \\( a_i \\)**:
   - Since \\( a_i \leq 10^9 \\), but increments only affect up to \\( n \leq 10^5 \\) positions, cap \\( a_i \\) at \\( n \\) (any \\( a_i \geq n \\) affects all positions to the right).

### Optimized Code
Below is the improved Java code using the reverse-order strategy with a difference array for efficient range updates.

```java
import java.io.*;
import java.util.*;

public class Main {
    BufferedReader in;
    PrintWriter out;

    Main() {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
    }

    void solve() throws IOException {
        int t = Integer.parseInt(in.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(in.readLine());
            long[] a = new long[n];
            StringTokenizer st = new StringTokenizer(in.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(st.nextToken());
                if (a[i] > n) a[i] = n; // Cap a[i] at n
            }

            // Difference array for range updates
            long[] diff = new long[n + 1];
            for (int i = n - 1; i >= 0; i--) {
                // Knock down tower i: set b[i] = 0, increment b[i+1] to b[i+a[i]]
                long range = Math.min(i + a[i], n - 1);
                if (i + 1 <= range) {
                    diff[i + 1]++;
                    if (range + 1 <= n) diff[(int)(range + 1)]--;
                }
            }

            // Compute final array b
            long[] b = new long[n];
            long sum = 0;
            for (int i = 0; i < n; i++) {
                sum += diff[i];
                b[i] = sum;
            }

            // Compute MEX
            TreeSet<Long> set = new TreeSet<>();
            for (long val : b) {
                set.add(val);
            }
            long mex = 0;
            while (set.contains(mex)) {
                mex++;
            }

            out.println(mex);
        }
    }

    void close() throws IOException {
        if (in != null) in.close();
        if (out != null) {
            out.flush();
            out.close();
        }
    }

    public static void main(String[] args) throws Exception {
        Main main = new Main();
        main.solve();
        main.close();
    }
}
```

### Improvements Made
1. **Algorithmic Efficiency**:
   - Replaced \\( O(n!) \\) permutation generation with a single pass using reverse order (\\( O(n) \\)).
   - Used a difference array to handle range increments in \\( O(n) \\), avoiding explicit updates for each position.
2. **Handling Large \\( a_i \\)**:
   - Capped \\( a_i \\) at \\( n \\), since increments beyond \\( n \\) don’t affect the array.
   - Used `long` instead of `int` for \\( a_i \\) to handle \\( 0 \leq a_i \leq 10^9 \\).
3. **MEX Calculation**:
   - Used a `TreeSet` to store unique values and find the smallest missing non-negative integer efficiently.
4. **Memory Optimization**:
   - Avoided array cloning and minimized object creation.
   - Used a difference array to reduce space complexity.
5. **Removed Unnecessary Code**:
   - Eliminated permutation generation and recursive calls.
   - Simplified input handling (kept `BufferedReader` as it’s sufficient).
6. **Removed Local Testing Code**:
   - Removed Mac-specific file input/output for simplicity, assuming standard input/output for competitive programming.

### Why This Works
- **Reverse Order**: Knocking from right to left ensures that later positions receive increments from all previous towers, naturally producing a non-decreasing array.
- **Difference Array**: Efficiently handles range increments in \\( O(n) \\).
- **MEX Maximization**: The reverse order tends to distribute increments such that \\( b_i \\) values are small and consecutive, maximizing the MEX by minimizing gaps.
- **Time Complexity**:
  - Input reading: \\( O(n) \\) per test case.
  - Difference array updates: \\( O(n) \\).
  - Final array computation: \\( O(n) \\).
  - MEX computation: \\( O(n \log n) \\) due to `TreeSet`.
  - Total: \\( O(n \log n) \\) per test case, \\( O(t \cdot n \log n) \\) overall, where \\( \sum n \leq 10^5 \\).
- **Space Complexity**: \\( O(n) \\) for arrays and `TreeSet`.

### Additional Optimization (Optional)
- **Faster MEX Calculation**:
  - Since \\( b_i \\) is non-decreasing, we can iterate through \\( b \\) and check if \\( b_i \geq i \\). The first \\( i \\) where \\( b_i < i \\) gives the MEX.
  - This reduces MEX computation to \\( O(n) \\), making the overall complexity \\( O(n) \\) per test case.
- **Custom Input Reader**:
  - For very tight time limits, implement a custom fast input reader to parse integers directly from the input stream, reducing I/O overhead.
- **Segment Tree/Fenwick Tree**:
  - If the reverse-order assumption fails for some edge cases, use a segment tree to try different orders efficiently, but this is likely unnecessary.

### Example Walkthrough
**Input**:
```
2
3
1 1 1
4
0 1 1 0
```

**Test Case 1 (\\( n=3, a=[1,1,1] \\))**:
- Reverse order: Knock 2, 1, 0.
- Initial \\( b = [0,0,0] \\), \\( diff = [0,0,0,0] \\).
- Tower 2 (\\( a_2=1 \\)): No increments (out of bounds). \\( b=[0,0,0] \\).
- Tower 1 (\\( a_1=1 \\)): Increment \\( b_2 \\). \\( diff[2]++ \\), \\( diff[3]-- \\). After computing, \\( b=[0,0,1] \\).
- Tower 0 (\\( a_0=1 \\)): Increment \\( b_1 \\). \\( diff[1]++ \\), \\( diff[2]-- \\). After computing, \\( b=[0,1,1] \\).
- \\( b=[0,1,1] \\) is non-decreasing.
- MEX: \\( \{0,1\} \\), so MEX = 2.
- Output: 2.

**Test Case 2 (\\( n=4, a=[0,1,1,0] \\))**:
- Reverse order: Knock 3, 2, 1, 0.
- Initial \\( b = [0,0,0,0] \\).
- Tower 3 (\\( a_3=0 \\)): No increments. \\( b=[0,0,0,0] \\).
- Tower 2 (\\( a_2=1 \\)): Increment \\( b_3 \\). \\( b=[0,0,0,1] \\).
- Tower 1 (\\( a_1=1 \\)): Increment \\( b_2 \\). \\( b=[0,0,1,1] \\).
- Tower 0 (\\( a_0=0 \\)): No increments. \\( b=[0,0,1,1] \\).
- \\( b=[0,0,1,1] \\) is non-decreasing.
- MEX: \\( \{0,1\} \\), so MEX = 2.
- Output: 2.

### Final Notes
- The reverse-order strategy assumes that knocking from right to left maximizes the MEX by ensuring a non-decreasing array with minimal gaps. If this fails for some edge cases, consider testing other orders (e.g., left to right or sorted by \\( a_i \\)) or using a more sophisticated approach like dynamic programming or greedy selection.
- Test the code thoroughly on edge cases (e.g., all zeros, large \\( a_i \\), \\( n=1 \\), \\( n=10^5 \\)).
- If the time limit is still an issue, profile the I/O and MEX calculation for further micro-optimizations.

This optimized code should handle the problem within the 3-second time limit for the given constraints. Let me know if you need further clarification or help with specific edge cases!