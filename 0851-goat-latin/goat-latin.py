class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        #beings with vowel append ma to end of the word => apple - applema
        # consonant =>goat => oatgma
        # I speak Goat Latin
        # Imaa peaksma|aa oatgma|aaa atinLmaaaa
        vowel = ['a', 'e', 'i', 'o','u', 'A', 'E','I', 'O','U']

        sentence = sentence.split()

        for i,word in enumerate(sentence):
            cur_char = word[0]
            if cur_char in vowel:
                temp = word + "ma"
            else:
                temp = word[1:] + word[0] + 'ma'
            
            temp += "a"*(i+1)

            sentence[i] = temp
        return ' '.join(sentence)