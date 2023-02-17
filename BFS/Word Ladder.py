class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue=deque()
        wordList=set(wordList)
        if endWord not in wordList:
            return 0 
        queue.append((beginWord,1))
        while queue:
            word,l=queue.popleft()
            if word==endWord:
                return l
            word=list(map(str,word))
            for j in range(len(word)):
                for i in range(97,123):
                    new_word=word.copy()
                    #print(word)
                    new_word[j] = chr(i)
                    n_w=''.join(new_word)
                    #print(n_w)
                    if n_w in wordList:
                        queue.append((n_w,l+1))
                        #print(n_w)
                        wordList.remove(n_w)

        return 0



                    
