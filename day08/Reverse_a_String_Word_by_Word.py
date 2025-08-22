class reverseword:
    def revstring(self,str)->str:
        word=str.strip().split()
        word.reverse()
        return " ".join(word)

str="the sky is blue"
print(reverseword().revstring(str))
