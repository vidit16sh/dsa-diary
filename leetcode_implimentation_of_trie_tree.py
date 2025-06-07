# -------------------------------
# 📘 TRIE (Prefix Tree)
# -------------------------------
# Q1: How do you insert a word into a Trie?
# Q2: How do you check if a word exists in the Trie?
# Q3: How do you check if any word starts with a given prefix?
#
# 🧪 TEST CASES:
# trie.insert("cat")
# trie.insert("car")
# trie.insert("care")
# trie.search("cat")       -> True
# trie.search("car")       -> True
# trie.search("ca")        -> False
# trie.search("care")      -> True
# trie.search("careful")   -> False
# trie.startsWith("ca")    -> True
# trie.startsWith("dog")   -> False
# trie.insert("dog")
# trie.search("dog")       -> True
# trie.startsWith("do")    -> True
# -------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}  # Maps each character to a TrieNode
        self.end_of_word = False  # True if this node marks the end of a complete word


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end_of_word = True

    def search(self, word):
        """
        Returns True if the word exists in the Trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end_of_word

    def startsWith(self, prefix):
        """
        Returns True if there is any word in the Trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True
