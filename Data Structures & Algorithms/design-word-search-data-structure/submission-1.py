class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        def searchFrom(temp, idx):
            if idx == len(word):
                return temp.isLeaf
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for child in temp.children:
                        if child and searchFrom(child, i + 1):
                            return True
                    return False
                else:
                    ind = ord(c) - ord('a')
                    if temp.children[ind] is None:
                        return False
                    temp = temp.children[ind]
            return temp.isLeaf
        return searchFrom(self.root, 0)

