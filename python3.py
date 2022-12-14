
from collections import Counter
from typing import List
import random
import heapq
from collections import Counter
def topkvalue(arr: List[int], k: int) -> List[int]: 
        if k == len(arr):
            return arr
        # Создание хэш таблицы: пары значение и как часто оно встречается
        # O(N) 
        count = Counter(arr)   
        # Cоздание кучи из верхних k частых элементов и преобразование ее в выходной массив
        # O(N log k)
        return heapq.nlargest(k, count.keys(), key=count.get)

print(topkvalue([1,1,1,2,2,3],2))
