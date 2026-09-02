# Tarea 1 · Algoritmos greedy en LeetCode

## [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/description/)

### Criterio greedy:
La estrategia consiste en aprovechar primero los espacios del camión con las cajas que contienen más unidades. Para esto, se ordenan los tipos de cajas de mayor a menor según la cantidad de unidades que tiene cada caja.

Después del ordenamiento, se toma la mayor cantidad posible del tipo de caja actual sin superar el espacio disponible en el camión. Una vez seleccionadas estas cajas, no es necesario volver atrás, ya que los siguientes tipos contienen la misma cantidad o menos unidades por caja.

### Rendimiento:
- *Complejidad de tiempo:* O(n log n), donde n es la cantidad de tipos de cajas. El costo principal corresponde al ordenamiento; posteriormente se realiza un recorrido lineal O(n).
- *Complejidad de espacio:* O(1) de espacio auxiliar, sin considerar la memoria interna utilizada por el método de ordenamiento.

### Evidencia:
- ![Statement and resolution code — Maximum Units on a Truck](evidencia/01_maximum.png)
- ![Accepted and runtime — Maximum Units on a Truck](evidencia/02_maximun-rutine.png)
- ![Accepted and memory — Maximum Units on a Truck](evidencia/03_maximum-memory.png)


## [55. Jump Game](https://leetcode.com/problems/jump-game/description/)

### Criterio greedy:
La estrategia consiste en mantener durante el recorrido la posición más lejana que se puede alcanzar. En cada índice se calcula hasta dónde sería posible llegar utilizando el salto disponible y se conserva el mayor alcance obtenido.

Si el índice que se está intentando visitar supera el máximo alcance conseguido, significa que esa posición no puede alcanzarse y se retorna falso. Si el alcance máximo llega o supera el último índice, se puede concluir inmediatamente que es posible llegar al final.

La decisión greedy consiste en conservar siempre el mejor alcance disponible hasta ese momento, sin necesidad de regresar a reconsiderar posiciones anteriores.

### Rendimiento:
- *Complejidad de tiempo:* O(n), donde n es la cantidad de elementos del arreglo, ya que se realiza como máximo un recorrido completo.
- *Complejidad de espacio:* O(1), porque únicamente se utiliza una variable para almacenar el máximo alcance y variables propias del recorrido.

### Evidencia:
- ![Statement and resolution code — Jump Game](evidencia/01_jump-game.png)
- ![Accepted and runtime — Jump Game](evidencia/02_jump-game-rutine.png)
- ![Accepted and memory — Jump Game](evidencia/03_jum-game-memory.png)