# https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3
# 전략: Two Pointer

# 예시1: abccab -> 'abc', [1, 3]
# 예시2: aabcca -> 'abc', [2, 4]
# aabc -> abc
# 예시3: abbcba -> 'cba', [4, 6]
# abbc -> bbcba -> bcba -> cba
# 예시4: aabbccab -> 'cab', [5, 7]
# aabbc -> abbc -> bbcca -> bcca -> ccab -> cab
# 예시5: abbcbbb -> 'aabc' [1, 4]
# abbc(이게 최적) -> bbcb -> bbcbb -> bbcbbb

class HashMap:
    def __init__(self):
        self.hm = dict()
        self.start = 0
        self.end = -1

    def diversity(self):
        return len(self.hm)

    def len(self):
        return self.end - self.start + 1

    def range(self):
        return [self.start+1, self.end+1]

    def add(self, gem):
        self.end += 1
        if gem in self.hm:
            self.hm[gem] += 1
        else:
            self.hm[gem] = 1

    def remove(self, gem):
        self.start += 1
        if self.hm[gem] > 1:
            self.hm[gem] -= 1
        else:
            del self.hm[gem]

def solution(gems):
    gem_set = set({ gem for gem in gems })
    gem_diversity = len(gem_set)
    hashMap = HashMap()

    for gem in gems:
        hashMap.add(gem)
        if hashMap.diversity() == gem_diversity:
            break

    min_length = hashMap.len()
    answer = hashMap.range()

    if min_length == gem_diversity:
        return answer

    for i in range(1, len(gems)-gem_diversity+1):
        hashMap.remove(gems[i-1])

        if hashMap.diversity() == gem_diversity:
            if hashMap.len() < min_length:
                min_length = hashMap.len()
                answer = hashMap.range()
                if min_length == gem_diversity:
                    break
        else:
            j = hashMap.end
            while True:
                j += 1
                if j >= len(gems):  # 범위를 넘어갈 경우
                    break
                hashMap.add(gems[j])
                if hashMap.diversity() == gem_diversity:
                    if hashMap.len() < min_length:  # 
                        min_length = hashMap.len()
                        answer = hashMap.range()
                        if min_length == gem_diversity:
                            i = len(gems)
                    break

    return answer