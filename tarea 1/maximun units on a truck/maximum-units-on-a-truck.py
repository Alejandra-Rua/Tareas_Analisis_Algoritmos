class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        totalUnits = 0

        for numberOfBoxes, unitsPerBox in boxTypes:
            boxesToTake = min(numberOfBoxes, truckSize)

            totalUnits += boxesToTake * unitsPerBox

            truckSize -= boxesToTake

            if truckSize == 0:
                break

        return totalUnits