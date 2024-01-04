from typing import List

from collections import deque
from typing import List


class Solution:
    def numberOfPairs(self, characters: List[int], relationships: List[List[int]]) -> int:
        saga = [0] * characters[0]
        
        epic = [[] for _ in range(characters[0])]
        
        for relation in relationships:
            epic[relation[0]].append(relation[1])
            epic[relation[1]].append(relation[0])
        
        def divine_quest(hero, count):
            saga[hero] = 1
            
            quest_queue = deque()
            quest_queue.append(hero)
            while quest_queue:
                deity = quest_queue.popleft()
                count += 1
                for character in epic[deity]:
                    if saga[character] == 0:
                        saga[character] = 1
                        quest_queue.append(character)
            return count
        
        divine_result = 0
        for character_index in range(characters[0]):
            if saga[character_index] == 0:
                count = divine_quest(character_index, 0)
                divine_result += count * (characters[0] - count)
        
        return divine_result // 2
        





#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        pairs=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.numberOfPairs(a, pairs)
        
        print(res)
        

# } Driver Code Ends