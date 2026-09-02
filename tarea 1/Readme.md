# Tarea 1 · Algoritmos greedy en LeetCode

## [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/description/)

### Criterio greedy:
La estrategia consiste en aprovechar primero los espacios del camión con las cajas que contienen más unidades. Para esto, se ordenan los tipos de cajas de mayor a menor según la cantidad de unidades que tiene cada caja.

Después del ordenamiento, se toma la mayor cantidad posible del tipo de caja actual sin superar el espacio disponible en el camión. Una vez seleccionadas estas cajas, no es necesario volver atrás, ya que los siguientes tipos contienen la misma cantidad o menos unidades por caja.

### Rendimiento:
- *Complejidad de tiempo:* O(n log n), donde n es la cantidad de tipos de cajas. El costo principal corresponde al ordenamiento; posteriormente se realiza un recorrido lineal O(n).
- *Complejidad de espacio:* O(1) de espacio auxiliar, sin considerar la memoria interna utilizada por el método de ordenamiento.

### Evidencia:
<img width="1902" height="907" alt="01_maximum" src="https://github.com/user-attachments/assets/909fbd08-9bc1-4a61-9f83-12f867df4438" />
<img width="1907" height="912" alt="02_maximun-rutine" src="https://github.com/user-attachments/assets/b7bd07dc-2b6e-4d55-8cdc-644492064c56" />
<img width="1897" height="905" alt="03_maximum-memory" src="https://github.com/user-attachments/assets/c72971dc-35b0-42e5-8a2b-3bf040b58738" />

## [55. Jump Game](https://leetcode.com/problems/jump-game/description/)

### Criterio greedy:
La estrategia consiste en mantener durante el recorrido la posición más lejana que se puede alcanzar. En cada índice se calcula hasta dónde sería posible llegar utilizando el salto disponible y se conserva el mayor alcance obtenido.

Si el índice que se está intentando visitar supera el máximo alcance conseguido, significa que esa posición no puede alcanzarse y se retorna falso. Si el alcance máximo llega o supera el último índice, se puede concluir inmediatamente que es posible llegar al final.

La decisión greedy consiste en conservar siempre el mejor alcance disponible hasta ese momento, sin necesidad de regresar a reconsiderar posiciones anteriores.

### Rendimiento:
- *Complejidad de tiempo:* O(n), donde n es la cantidad de elementos del arreglo, ya que se realiza como máximo un recorrido completo.
- *Complejidad de espacio:* O(1), porque únicamente se utiliza una variable para almacenar el máximo alcance y variables propias del recorrido.

### Evidencia:
<img width="1902" height="907" alt="01_jump-game" src="https://github.com/user-attachments/assets/02345f05-02b8-4bca-874d-f933b374f28c" />
<img width="1907" height="912" alt="02_jump-game-rutine" src="https://github.com/user-attachments/assets/dabffa1d-5633-4f57-b201-7203249e78f1" />
<img width="1902" height="906" alt="03_jum-game-memory" src="https://github.com/user-attachments/assets/3534e3d9-0f72-4aa8-bc45-84e57e19001d" />


