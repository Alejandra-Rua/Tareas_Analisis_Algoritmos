from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        filas = len(grid)
        columnas = len(grid[0])
        islas = 0

        def dfs(fila, columna):

            if (
                fila < 0
                or fila >= filas
                or columna < 0
                or columna >= columnas
                or grid[fila][columna] == "0"
            ):
                return

            grid[fila][columna] = "0"

            dfs(fila - 1, columna)
            dfs(fila + 1, columna)
            dfs(fila, columna - 1)
            dfs(fila, columna + 1)

        for fila in range(filas):
            for columna in range(columnas):

                if grid[fila][columna] == "1":
                    islas += 1
                    dfs(fila, columna)

        return islas