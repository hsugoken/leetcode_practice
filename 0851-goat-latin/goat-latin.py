class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        #consonants will have first character moved to the end
        #then add ma to its end
        #then add 'a' based on index of word in the sentence
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        sentence = sentence.split()
        # res = ""
        print(sentence)
        for i in range(len(sentence)):
            res = ""
            cur_word = sentence[i]
            if cur_word[0] not in vowels:
                res += cur_word[1:] + cur_word[0]
            else:
                res += cur_word
            res += "ma"
            res += "a"*(i+1)
            sentence[i] = res
        
        return ' '.join(sentence)

