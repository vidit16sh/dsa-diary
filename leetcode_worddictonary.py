# ❓ QUESTION:
# Design a data structure that supports adding new words and searching for a string,
# where the search string can contain the '.' wildcard character that matches any letter.
#
# Implement the WordDictionary class:
# - void addWord(word): Adds a word into the data structure.
# - bool search(word): Returns true if there is any word in the data structure that matches
#   the search word, where '.' can match any letter.

# ✅ APPROACH:
# Use a Trie (Prefix Tree) to store the words.
# Each TrieNode keeps track of its children (dictionary) and whether it's the end of a word.
# For `addWord`, we insert each character into the Trie.
# For `search`, we use DFS to explore possibilities when encountering '.' by trying all children.

class TrieNode:
    def __init__(self):
        self.children = {}  # Key: character, Value: TrieNode
        self.is_end_of_word = False  # True if the path to this node is a complete word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create node if char not seen
            node = node.children[char]
        node.is_end_of_word = True  # Mark end of word

    def search(self, word):
        """
        Returns True if there is any word in the data structure that matches the given word,
        where '.' can represent any letter.
        :type word: str
        :rtype: bool
        """

        def dfs(index, node):
            if index == len(word):
                return node.is_end_of_word

            char = word[index]

            if char == '.':
                # Try all possible children (wildcard match)
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                # Normal character match
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)
