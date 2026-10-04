class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        resultado = []

        for intervalo in intervals:
            if not resultado or intervalo[0] > resultado[-1][1]:
                resultado.append(intervalo)
            else:
                resultado[-1][1] = max(
                    resultado[-1][1],
                    intervalo[1]
                )

        return resultado