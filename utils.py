def create_grid(input_string):
    grid_size = 4
    grid = []
    for i in range(0, len(input_string), grid_size):
        grid.append(list(input_string[i:i + grid_size]))
    return grid


def sort_words(words):
    # return sorted(words, key=lambda w: (-len(w), w))
    return sorted(words, key=lambda w: (len(w), w))


def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = set(word.strip().upper() for word in file if len(word.strip()) >= 3)
    return dictionary


def find_words(grid, dictionary):
    rows, cols = len(grid), len(grid[0])
    found_words = set()

    prefixes = set()
    for word in dictionary:
        for i in range(1, len(word)):
            prefixes.add(word[:i])

    def dfs(row, col, path, visited):
        if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in visited):
            return
        path += grid[row][col]
        if path not in prefixes and path not in dictionary:
            return
        if path in dictionary:
            found_words.add(path)
        visited.add((row, col))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    dfs(row + dr, col + dc, path, visited)
        visited.remove((row, col))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, '', set())
    return found_words


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def build_trie(dictionary):
    root = TrieNode()
    for word in dictionary:
        node = root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        node.is_word = True
    return root


def find_words_with_trie(grid, trie_root):
    rows, cols = len(grid), len(grid[0])
    found_words = set()

    def dfs(row, col, node, path, visited):
        if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in visited):
            return
        letter = grid[row][col]
        if letter not in node.children:
            return
        visited.add((row, col))
        node = node.children[letter]
        path += letter
        if node.is_word:
            found_words.add(path)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    dfs(row + dr, col + dc, node, path, visited)
        visited.remove((row, col))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, trie_root, '', set())
    return found_words
