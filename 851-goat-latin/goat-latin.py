class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words=sentence.split(" ")
        index=0

        for i in range(len(words)):
            word=words[i]
            index+=1
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                word=word+"ma"+"a"*index
            else:
                word=word[1::]+word[0]+"ma"+"a"*index
            words[i]=word
        return " ".join(words)