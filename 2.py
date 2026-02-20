"""The "Streaming Max" Analytics (Deques/Monotonic Queue)
○ Problem: You are receiving a stream of server latency data. Given a window size K,
calculate the maximum latency in every window.
○ Complexity Requirement: You must process each incoming data point in amortized
O(1) time.
"""

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing order
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(max_sliding_window(nums, k))