# Last updated: 11/2/2025, 8:22:24 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        
        row = len(image) #Number of rows 
        col = len(image[0]) #Number of cols 
        start = image[sr][sc] #Starting Pixel 
        if start == color: #If the pixel is already the new color 
            return image
            
        def dfs(r, c):
            if image[r][c] == start: 
                image[r][c] = color
                if r >= 1: #Up 
                    dfs(r-1, c)
                if r+1 < row: #Down
                    dfs(r+1, c)
                if c >= 1: #Left 
                    dfs(r, c-1)
                if c+1 < col: #Right 
                    dfs(r, c+1)

        dfs(sr, sc)

        return image
