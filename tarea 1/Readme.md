# Tarea 1 · Algoritmos greedy en LeetCode

## 860. Lemonade Change

**Enlace al problema:**  
https://leetcode.com/problems/lemonade-change/

### Criterio greedy

La estrategia consiste en atender a los clientes en el orden en que llegan y entregar el cambio de manera que se conserven los billetes de $5 siempre que sea posible.

Cuando un cliente paga con $20, se intenta primero entregar un billete de $10 y uno de $5. Si esto no es posible, se entregan tres billetes de $5. Esta decisión permite conservar los billetes pequeños, que son necesarios para poder dar cambio a los siguientes clientes.

Si en algún momento no es posible entregar el cambio exacto, se retorna `False`.

### Rendimiento

- **Complejidad de tiempo:** O(n), donde n es la cantidad de clientes, ya que se recorre el arreglo una sola vez.
- **Complejidad de espacio:** O(1), porque únicamente se utilizan variables para almacenar la cantidad de billetes de $5 y $10.

### Evidencia
<img width="1901" height="906" alt="01_lemonade-change" src="https://github.com/user-attachments/assets/34557ed0-fd3d-4544-b316-7c0190446399" />
<img width="1906" height="912" alt="02_lemonade-change-runtime" src="https://github.com/user-attachments/assets/aba3e572-482b-4cf5-b0d2-c2d07b6cb047" />
<img width="1902" height="910" alt="03_lemonade-change-memory" src="https://github.com/user-attachments/assets/f7002dc4-f99f-4e05-ac92-90d3487787ef" />

## 455. Assign Cookies

**Enlace al problema:**  
https://leetcode.com/problems/assign-cookies/

### Criterio greedy

La estrategia consiste en ordenar los niños según su nivel de gula y las galletas según su tamaño, ambos de menor a mayor.

Para cada niño se busca la galleta más pequeña que sea suficiente para satisfacerlo. Si una galleta es demasiado pequeña, se descarta y se prueba la siguiente. Cuando una galleta satisface al niño actual, se asigna y se continúa con el siguiente niño.

De esta manera se evita utilizar una galleta más grande de lo necesario y se maximiza la cantidad de niños satisfechos.

### Rendimiento

- **Complejidad de tiempo:** O(n log n + m log m), debido al ordenamiento de los niños y las galletas. Después se realiza un recorrido lineal.
- **Complejidad de espacio:** O(1) de espacio auxiliar, sin considerar la memoria interna utilizada por el método de ordenamiento.

### Evidencia
<img width="1902" height="907" alt="01_assign-cookies" src="https://github.com/user-attachments/assets/7acbdd28-115a-4fee-ab62-b9de476a4378" />
<img width="1902" height="911" alt="02_assign-cookies-runtime" src="https://github.com/user-attachments/assets/ce7bdd31-e4f8-4d92-9bef-30b3b67bd4c7" />
<img width="1902" height="907" alt="03_assign-cookies-memory" src="https://github.com/user-attachments/assets/a1e89f5c-27a9-403b-9b8d-1d152b0dc036" />




