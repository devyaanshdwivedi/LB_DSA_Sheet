from collections import deque
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        #Code here
        q = deque()
        q.append((startWord,1))
        vis = set()
        vis.add(startWord)
        res = 0
        while q:
            word, dist = q.popleft()
            if word == targetWord: return dist
            for i in range(len(word)):
                for j in range(26):
                    newchar = chr(j+97)
                    new_word = word[:i] + newchar + word[i+1:]
                    if new_word in wordList and new_word not in vis:
                        vis.add(new_word)
                        q.append((new_word,dist+1))
        return 0
        #Code here


#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends