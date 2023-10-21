import random
import string
if __name__ == '__main__':
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation
    s5=string.hexdigits
    plen=int(input("enter password length\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    if(plen<5):
        print("your password should not be have less than 5 characters")
    else:
        print("".join(s[0:plen]))


