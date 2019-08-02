import string
import random

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