#time complexity O(m^2 *n) - m = dequeued word , n is size of word list
#space complexity = O(m * n) m = no.of char in string n = size of wordList

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        #since its bfs, it automatically returns shortest path

        #inutialise both queue and set with 1st word = beginword
        queue = deque([beginWord])  #to keep track of string we've already added in the queue
        visited = set([beginWord]) #not to store already visited chars and avoid repetition
        changes = 1 #to update the total output
        wordList = set(wordList)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        #base case
        if endWord not in wordList:
            return 0

        while queue:
            for l in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return changes

                for i in range(len(curr_word)):
                    prefix = curr_word[:i]
                    suffix = curr_word[i+1:]
                    for al in alphabet:
                        w = prefix + al + suffix
                        if w in wordList and w not in visited:
                            queue.append(w)
                            visited.add(w)
            changes += 1
        return 0

        
