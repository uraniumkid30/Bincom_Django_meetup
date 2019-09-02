import string
import random
import json
from nltk.corpus import words as wn
from PyBincom_v1.settings import BASE_DIR
class UniqueIdentifiers:

    @classmethod
    def createToken(cls,a,b):
        SEQ = string.ascii_uppercase + string.digits
        def shake(seq,n):
            randomstr = (','.join(random.choice(seq) for _ in range(n))).split(',')
            for i in range(n):
                random.shuffle(randomstr)
            return''.join(randomstr)

        def main(pattern_no,str_len):
            keygen = lambda: ''.join(shake(SEQ,pattern_no) for _ in range(str_len))
            return keygen()
        return main(a,b)

    @classmethod
    def createId(cls,n1,n2,text):
        STRSEQ = string.ascii_uppercase
        NUMSEQ = string.digits
        def main(n1,n2,text):
            str1 = text
            str2 = (''.join(random.choice(STRSEQ) for _ in range(n1)))
            str3 = (''.join(random.choice(NUMSEQ) for _ in range(n2)))
            return (str1 + str2 +str3)
        return main(n1,n2,text)

class WordGame:
    def __init__(self,word):
        with open('dictionary.json') as jf:
            json_data = json.load(jf)
            self.dic_words = list(json_data.keys())
        self.dict_words = {i.lower() for i in self.dic_words}
        self.nltk_words = set(list(wn.words()))
        self.word = word.lower()

    def newguy(self,l, newword=[]):
        holder = []
        word2 = list(l)
        if newword:
            for r in newword:
                counter = [i for i in r]
                for j in counter:
                    word2.remove(j)
                for jj in word2:
                    holder.append(r + jj)
                word2 = (list(l))
        else:
            for a in range(len(l)):
                word2.remove(l[a])
                for i in word2:
                    holder.append(l[a] + i)
                word2 = list(l)
        return holder

    def allwords(self):

        self.finalwords = []
        for i in range(len(self.word) - 1):
            if i == 0:
                newword = self.newguy(self.word)
            else:
                newword = self.newguy(self.word, newword)
            for i in newword:
                self.finalwords.append(i)

    def actualwords(self):
        print(self.finalwords)
        td2 = sorted(set(self.finalwords).intersection(self.nltk_words))
        y, z = min(map(len, td2)), max(map(len, td2)) + 1
        self.bank2 = {i: (lambda i: [j for j in td2 if len(j) == i])(i) for i in range(y, z)}

