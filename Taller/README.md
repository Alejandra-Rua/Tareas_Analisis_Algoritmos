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