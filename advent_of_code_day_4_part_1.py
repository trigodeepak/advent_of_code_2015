#this is is for 6 zeros it will take approx 5 mins to execute
import hashlib
n = 0
while(True):
    result =  hashlib.md5('yzbqklnj'+str(n)).hexdigest()
    if result.startswith('000000'):
        print n,result
        break
    n+=1
