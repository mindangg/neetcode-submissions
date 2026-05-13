class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    result.append(count)
                    break
            else:
                result.append(0)
        return result