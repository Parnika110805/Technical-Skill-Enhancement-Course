"""4. The "Range Performance Monitor" (Segment Trees)
○ Problem: Design a system for a stock exchange that handles two operations:
update(index, value) for a stock price and queryMax(L, R) to find the highest price in
a time range.
○ Complexity Requirement: Both operations must be O(\log N).
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        self.build(arr, 2 * node + 1, l, mid)
        self.build(arr, 2 * node + 2, mid + 1, r)
        self.tree[node] = max(
            self.tree[2 * node + 1],
            self.tree[2 * node + 2]
        )

    def update(self, idx, val, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1

        if l == r:
            self.tree[node] = val
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(idx, val, 2 * node + 1, l, mid)
        else:
            self.update(idx, val, 2 * node + 2, mid + 1, r)

        self.tree[node] = max(
            self.tree[2 * node + 1],
            self.tree[2 * node + 2]
        )

    def query_max(self, ql, qr, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1

        if ql <= l and r <= qr:
            return self.tree[node]
        if r < ql or l > qr:
            return float('-inf')

        mid = (l + r) // 2
        return max(
            self.query_max(ql, qr, 2 * node + 1, l, mid),
            self.query_max(ql, qr, 2 * node + 2, mid + 1, r)
        )

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)

    print(st.query_max(1, 4))  # max between index 1 and 4
    st.update(2, 10)
    print(st.query_max(1, 4))