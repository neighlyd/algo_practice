class TrieNode():

    def __init__(self):
        # Create a dictionary for children, where letter = link to new TrieNode()
        self.children = {}
        self.endOfWord = False

    def all_words(self, prefix):
        """
            Recursive generator to perform a BFS for all words beginning with a specific prefix. Hooks from
            Trie.all_words_beginning_with_prefix().
        :param prefix: String of characters (added to recursively)
        :return: Yields the final word found.
        """
        if self.endOfWord:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)


class Trie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
            Inserts a word into the Trie, terminating the last letter with an endOfWord = True.
        :param word: String of characters
        :return: None
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children.get(char)
        cur.endOfWord = True

    def search(self, word):
        """
            Lets us know whether a completed word exists in the Trie.
        :param word: String of characters
        :return: Boolean - True if last char is an endOfWord, False if no char or endOfWord is False.
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children.get(char)
        return cur.endOfWord

    def starts_with(self, prefix):
        """
            Lets us know if there are any words that begin with a particular prefix, inclusive
            (i.e. 'tree' will return true for 'tree')
        :param prefix: String of chars to search
        :return: Boolean
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children.get(char)
        return True

    def all_words_beginning_with_prefix(self, prefix):
        """
            A generator that returns a list of all words that begin with a specific prefix.
            Hooks into TrieNode.all_words()
        :param prefix: String of characters
        :return: List of strings (or empty if none found).
        """
        cur = self.root
        # Need to iterate and set cur to bottom character, so that we begin our yield from the right place.
        # I.E. if we were to just self.search(prefix) we would start at root node.
        for char in prefix:
            cur = cur.children.get(char)
            if cur is None:
                # If the Trie doesn't have a child node with a letter in the prefix, yield nothing
                return
        yield from cur.all_words(prefix)
