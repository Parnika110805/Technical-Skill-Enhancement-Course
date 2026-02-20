"""5. The "Optimal Resource Allocation" (Bitmask DP)
○ Problem: You have N tasks and N workers (where N < 20). Each worker has a specific
cost for each task. Assign exactly one worker to each task such that the total cost is
minimized.
○ Complexity Requirement: Improve upon the O(N!) brute force to O(2^N . N^2) using
state compression.
"""

def assign_tasks(cost):
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        task = bin(mask).count('1')
        if task >= n:
            continue

        for worker in range(n):
            if not (mask & (1 << worker)):
                new_mask = mask | (1 << worker)
                dp[new_mask] = min(
                    dp[new_mask],
                    dp[mask] + cost[task][worker]
                )

    return dp[(1 << n) - 1]

if __name__ == "__main__":
    cost = [
        [9, 2, 7],
        [6, 4, 3],
        [5, 8, 1]
    ]

    print(assign_tasks(cost))