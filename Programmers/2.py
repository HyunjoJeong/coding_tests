# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 단어변환

from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    
    word_size = len(begin)
    words = [begin] + words
    words_length = len(words)
    similarity = [[0 for _c in range(words_length)] for _r in range(words_length)]

    for r in range(words_length):
        for c in range(r + 1, words_length):
            s = 0
            for i in range(word_size):
                if words[r][i] == words[c][i]:
                    s += 1
            similarity[r][c] = similarity[c][r] = s
            
    visited = [False for _ in range(words_length)]
    stack = [(0, 0)] # (node, count)

    while stack:
        node, count = stack.pop()

        if visited[node]: continue
        if node == words.index(target): return count
        
        visited[node] = True

        for i in range(words_length):
            if similarity[node][i] == word_size - 1 and not visited[i]:
                stack.append((i, count + 1))
    
    return 0