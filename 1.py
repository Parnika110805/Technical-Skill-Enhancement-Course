"""1. The "Global Autocomplete" System (Tries)
○ Problem: Build a Trie-based system that stores 1 million strings. Implement a
function that returns the top 5 most frequent suggestions for a given prefix.
○ Complexity Requirement: The prefix search must be O(L), where L is the length of
the prefix, regardless of the dictionary size.
"""

import heapq
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.top5 = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_freq = defaultdict(int)

    def _update_top5(self, node, word):
        freq = self.word_freq[word]

        for i, (_, w) in enumerate(node.top5):
            if w == word:
                node.top5[i] = (freq, word)
                heapq.heapify(node.top5)
                return

        heapq.heappush(node.top5, (freq, word))
        if len(node.top5) > 5:
            heapq.heappop(node.top5)

    def insert(self, word):
        self.word_freq[word] += 1

        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            self._update_top5(node, word)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        return [w for _, w in sorted(node.top5, reverse=True)]

if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "approach", "app", "apple", "apply", "appreciate", "application"]

    for word in words:
        trie.insert(word)

    print(trie.autocomplete("app"))