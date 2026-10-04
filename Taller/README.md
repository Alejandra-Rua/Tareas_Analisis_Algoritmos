# Taller - Cinco familias en LeetCode

## 56. Merge Intervals

**Familia:** Ordenamiento

**Idea:**  
Primero se ordenan los intervalos por su extremo izquierdo. Luego se recorren y se comparan con el último intervalo agregado. Si existe solapamiento, se amplía el extremo derecho; de lo contrario, se agrega un nuevo intervalo.

**Complejidad temporal:**  
O(n log n), debido al ordenamiento de los intervalos.

**Complejidad espacial:**  
O(n), debido a la lista utilizada para almacenar los intervalos resultantes.

### Evidencia de Accepted

![Accepted - Merge Intervals](evidencias/merge-intervals-accepted.png)

### Evidencia de memoria

![Memory - Merge Intervals](evidencias/merge-intervals-memory.png)


## 200. Number of Islands

**Familia:** Grafos

**Idea:**  
Se recorre toda la matriz y cada vez que se encuentra una celda de tierra `"1"` que no ha sido visitada, se cuenta una nueva isla. Luego se utiliza DFS para recorrer todas las celdas conectadas de esa misma isla y marcarlas como visitadas.

**Modelo del grafo:**  
Cada celda de tierra representa un vértice. Existe una arista entre dos celdas de tierra cuando son vecinas horizontal o verticalmente. Cada isla corresponde a una componente conexa.

**Complejidad temporal:**  
O(m × n), porque cada celda de la matriz se visita como máximo una vez.

**Complejidad espacial:**  
O(m × n) en el peor caso, debido a la pila de llamadas recursivas de DFS.

### Evidencia de Runtime

![Runtime - Number of Islands](evidencias/number-of-islands-runtime.png)

### Evidencia de Memory

![Memory - Number of Islands](evidencias/number-of-islands-memory.png)


## 1143. Longest Common Subsequence

**Familia:** Programación dinámica

**Idea:**  
Se construye una tabla `dp` donde `dp[i][j]` representa la longitud de la subsecuencia común más larga entre los primeros `i` caracteres de `text1` y los primeros `j` caracteres de `text2`.

**Estado:**  
`dp[i][j]` = longitud de la subsecuencia común más larga entre `text1[0..i)` y `text2[0..j)`.

**Caso base:**  
Si uno de los textos está vacío, la longitud de la subsecuencia común es 0.

**Recurrencia:**  
Si `text1[i-1] == text2[j-1]`, se suma 1 al valor diagonal anterior.  
Si son diferentes, se toma el máximo entre ignorar un carácter de `text1` o uno de `text2`.

**Complejidad temporal:**  
O(n × m)

**Complejidad espacial:**  
O(n × m)

### Evidencia de Runtime

![Runtime - Longest Common Subsequence](evidencias/longest-common-subsequence-runtime.png)

### Evidencia de Memory

![Memory - Longest Common Subsequence](evidencias/longest-common-subsequence-memory.png)