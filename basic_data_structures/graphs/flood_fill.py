class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        orig_col = image[sr][sc]
        if orig_col ==color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        # Flood fill starting at (sr, sc) with the new color; return the updated image.
        def dfs(r: int,c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] !=orig_col:
                return
            
            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr,sc)    
        return image

import unittest

class TestFloodFill(unittest.TestCase):
    s = Solution()
    def twoPixelFill(self):
        self.assertEqual(s.floodFill([[0,0,0],[0,1,1]],1,1,5), [[0,0,0],[0,5,5]])
    def singleCell(self):
        self.assertEqual(s.floodFill([[1,2],[3,4]], 0, 0, 9), [[9,2],[3,4]])
            
    
if __name__ == "__main__":
    unittest.main()
    