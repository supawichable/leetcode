'''
1710. Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/
'''


import heapq


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        boxNow, unitNow = 0, 0
        i = 0
        while boxNow < truckSize and i < len(boxTypes):
            [numBox, numUnit] = boxTypes[i]
            unitNow += min(truckSize - boxNow, numBox) * numUnit
            boxNow += numBox
            i += 1
        return unitNow


# priority queue
class Solution2:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        heapq.heapify(heap)
        k = 0
        for boxType in boxTypes:
            heapq.heappush(heap, (boxType[1], boxType[0]))
            k += boxType[0]
            while k > truckSize:
                poppedUnit, poppedBox = heapq.heappop(heap)
                if poppedBox > k - truckSize:
                    heapq.heappush(heap, (poppedUnit, poppedBox - (k-truckSize)))
                    k = truckSize
                else:
                    k -= poppedBox
        return sum([x[1] * x[0] for x in heap])