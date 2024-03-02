from pprint import *
import random
def s_box_sub(lis:list,dic:dict):
    lis1:list=[]
    temp_lis:list=[]
    for i in range(8):
        lis1=lis[int(i*len(lis)/8):int((i+1)*len(lis)/8)]
        h=bin_to_dec(lis1)
        r=dic[h]
        #re=hex_dec(r)
        s=dec_to_binary(r)
        l=[int(x) for x in s]
        temp_lis.extend(l)
    return temp_lis
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
def xor_lis(a:list,b:list):
    t_lis=[]
    for i,j in enumerate(a):
        t_lis.append(int(bool(j)^bool(b[i])))
    return t_lis
def gen_s_box():
    lis1:list=[x for x in range(0x20)]
    lis2:list=[]
    temp_lis=[]
    dic:dict={}
    while(len(lis2)<32):    
        lis2.append(random.choice(lis1))
        lis2=set(lis2)
        lis2=list(lis2)
    for i in lis1:
        temp_lis.append(hex(i))
    lis1=temp_lis    
    for i,j in enumerate(lis1):
        dic[j]=lis2[i]
    return dic
def xor(a:bool,b:bool):
    return a^b



inp_lis:list=[random.choice([0,1]) for i in range(128)]
phi:list=[random.choice([0,1]) for i in range(32)]
s_box:dict=gen_s_box()
ans:dict={}

for t in range(32):
    if (t==0):
        l1:list=inp_lis[:int(len(inp_lis)/4)]
        l2:list=inp_lis[int(len(inp_lis)/4):int(len(inp_lis)/2)]
        l3:list=inp_lis[int(len(inp_lis)/2):int(3*len(inp_lis)/4)]
        l4:list=inp_lis[int(3*len(inp_lis)/4):int(len(inp_lis))]
    else:
        l1:list=lis[:int(len(inp_lis)/4)]
        l2:list=lis[int(len(inp_lis)/4):int(len(inp_lis)/2)]
        l3:list=lis[int(len(inp_lis)/2):int(3*len(inp_lis)/4)]
        l4:list=lis[int(3*len(inp_lis)/4):int(len(inp_lis))]    
    temp_lis:list=[]
    #phi 
    for i,j in enumerate(l1):
        temp_lis.append(xor(j,phi[i]))
    l1=temp_lis
    temp_lis=[]

    #s_box
    l2=s_box_sub(l2,s_box)


    #l3
    for i,j in enumerate(l3):
        temp_lis.append(xor(j,l2[i]))
    temp_lis.reverse()
    l3=temp_lis
    temp_lis=[]
    #l4
    for i,j in enumerate(l4):
        temp_lis.append(xor(j,l1[i]))
    temp_lis.reverse()
    l4=temp_lis

    lis:list=l1+l2+l3+l4
    
    j:int=0
    temp_lis:list=[]
    sh_lis:list=lis[len(lis)-67:len(lis)]
    sh_lis.extend(lis[0:len(lis)-67])
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
        ans_lis=xor_lis(ans_lis,j)
print("Initial Key:\nBinary=",end='')
for i in inp_lis:
    print(i,end='')
print('\nHexa=',bin_to_dec(inp_lis))
decimal=bin_to_dec(ans_lis)
print("\n\nCipher Text:\nBinary=",end='')
for i in ans_lis:
    print(i,end='')
print("\nHexa",decimal)

print("sbox:")
pprint(s_box)
print("phi\nBinary=",end='')
for i in phi:
    print(i,end='')
print('\nHexa=',bin_to_dec(phi))