class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = {}
        
        for w in words:
            node = trie
            for letter in w:
                node = node.setdefault(letter, {})
            node['$'] = True
        
        result = list()
        visited = set()
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        
        def backtrack(r, c, node, prefix):
            letter = board[r][c]
            if letter in node:
                visited.add((r, c))
                node = node[letter]
                if '$' in node:
                    result.append(prefix + letter)
                    del node['$']
                
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited:
                        backtrack(x, y, node, prefix + letter)
                visited.remove((r, c))
                
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie, '')
        return result     
        