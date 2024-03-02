import random
from pprint import *
def s_box(lis:list,dic:dict):
    h=bin_to_dec(lis)
    r=dic[h]
    re=hex_dec(r)
    s=dec_to_binary(re)
    l=[int(x) for x in s]
    return l
def hex_dec(h:str):
    con_dic:dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,'F':15}
    return con_dic[h]
def dec_to_binary(min_term:int,no_bits:int=4):
    res_term=min_term
    if(min_term<0):
        return None
    res=''
    while(min_term!=0):
        res+=str(min_term%2)
        min_term=min_term//2
    r=[x for x in res]
    while len(r)<no_bits:
        r.append('0')
    r.reverse()
    res=''
    for i in r:
        res+=i
    return res
def com(l:list,b:str):
    temp_lis=[]
    for i,j in enumerate(l):
        temp_lis.append(int(bool(j)^bool(b[3])))
    return temp_lis
def bin_to_dec(bin:list):#binary to hexa
    a:int=0
    bin.reverse()
    for i,j in enumerate(bin):
        a+=(2**i)*(int(j))
    return hex(a)
def xor(a:list,b:list):
    t_lis=[]
    for i,j in enumerate(a):
        t_lis.append(int(bool(j)^bool(b[i])))
    return t_lis
choi_lis:list=[0,1]
#lis:list=[random.choice(choi_lis) for x in range(128)]
st:str=input("Enter cypher(Binary)")
print(st)
lis:list=list(st)
print("Initial Key:\nBinary=",end='')
for i in lis:
    print(i,end='')
print('\nHexa=',bin_to_dec(lis))
#lis=[int(x) for x in lis]
s_b_dic={'0x0': 'C', '0x1': '5', '0x2': '6', '0x3': 'B', '0x4': '9', '0x5': '0', '0x6': 'A', '0x7': 'D', '0x8': '3', '0x9': 'E', '0xa': 'F', '0xb': '8', '0xc': '4', '0xd': '7', '0xe': '1','0xf':'2'}
ans:dict={}
for t in range(32):
    j:int=0
    temp_lis:list=[]
    sh_lis:list=lis[len(lis)-67:len(lis)]
    sh_lis.extend(lis[0:len(lis)-67])
    for i in range(2):
        temp_lis=[sh_lis[i+j] for i in range(4)]
        temp_lis=s_box(temp_lis,s_b_dic)
        for x,y in enumerate(temp_lis):
            sh_lis[x+j]=temp_lis[x]
        j+=3
    lis=sh_lis
    bin_t=dec_to_binary(t,5)
    temp_lis=lis[-67:-62]
    temp_lis=com(temp_lis,bin_t)
    j=-67
    for i in range(4):
        lis[i+j]=temp_lis[i]
    ans[t+1]=lis[:int(len(lis))]
ans_lis=[]
for i,j in enumerate(ans.values()):
    if i==0:
        ans_lis=j
    else:
        ans_lis=xor(ans_lis,j)

decimal=bin_to_dec(ans_lis)
print("\n\nCipher Text:\nBinary= ",end='')
for i in ans_lis:
    print(i,end='')
print("\nHexa",decimal)
print('\ns_box:')
pprint(s_b_dic)