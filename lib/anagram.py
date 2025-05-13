

class Anagram:
    
    def __init__(self,word = 'listen'):
        self.word = word
        pass

    def match(self, list):
        sorted_word = sorted(self.word)

        matches = []

        for word in list:

            if sorted(word) == sorted_word:
                matches.append(word)

        return matches

        

        pass

word = Anagram('enlist')