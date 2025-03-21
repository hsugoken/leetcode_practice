class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group_strings = collections.defaultdict(list)
        for i in range(len(strings)):
            cur_word = strings[i]
            if len(cur_word)==1:
                group_strings[(-1,)].append(cur_word)
                continue
            key = []
            for j in range(len(cur_word)-1):
                diff = ord(cur_word[j])-ord(cur_word[j+1])
                diff = diff%26
                key.append(diff)
            group_strings[tuple(key)].append(cur_word)
        return list(group_strings.values())

