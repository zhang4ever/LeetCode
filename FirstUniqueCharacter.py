def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    for x in range(0, len(s)):
        if s.count(s[x]) == 1:
            return x
    return -1


def deleteAll(x, l):
    for i in range(l.count(x)):
        l.remove(x)


def firstUniqChar2(s):
    ss = [i for i in s if s.count(i) > 1]
    print(ss)
    string = [i for i in s]
    print(string)
    for i in ss:
        deleteAll(i, string)
    if len(string) == 0:
        return -1
    return s.index(string[0])


def firstUniqChar3(s):
    ss = [i for i in s]
    for i in range(len(ss)):
        if ss[i] not in ss[:i] and ss[i] not in ss[i + 1:]:
            return i
    return -1


def firstUniqChar4(s):
    import collections
    d = collections.Counter(s)
    ans = -1
    for x, c in enumerate(s):
        if d[c] == 1:
            ans = x
            break
    return ans

    
print(firstUniqChar4('klkleei'))