"""
You are given n words. 
Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.

Input Format:
The first line contains the integer n.
The next n lines each contains a word.

Output:
Output two lines
Lin one is the number of distinct words from the input
Line two outputs the number of occurrences for each distinct word according to their appearnace in the input.
"""

from collections import Counter, OrderedDict

wordList = []
wordDict = OrderedDict()
    
if __name__ == '__main__':
    size = int(input())
    for i in range(size):
        word = input().strip()
        wordList.append(word)
        wordDict[i] = word
    wordCnt = Counter(wordList)
    print(len(set(wordList)))
    for k,v in wordCnt.items():
        print(v, end = ' ')


# Another Soulution: HOw to use classes with collections
# notice this answer creates a class to account for the two imports, but doesn't actually do anything. Just need to understand this

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())