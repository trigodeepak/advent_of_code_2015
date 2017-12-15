#The answer is not correct maybe there is a problem in the code
a = '''fbpyzxdfmkrtfaeg
yzsmlbnftftgwadz'''
a = a.split('\n')
nau = ['ab','cd','pq','xy']
vowel = list('aeiou')
f = 0
n = 0
count = 0
for s in a:
    f =0
    for i in nau:
        if i in s:
            f = 1
            break
    if f == 0:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                n+=1
                count = 0
                break
            if s[i] in vowel:
                count+=1
                if count >=3:
                    n+=1
                    count = 0
                    break
        
        if s[len(s)-1] in vowel:
            count+=1
            if count >=3:
                n+=1
                count = 0
                continue
print n
