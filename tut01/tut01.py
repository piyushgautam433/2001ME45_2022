#HareKrishna
import pandas as pd #panda is imported
df = pd.read_csv(r"octant_input.csv") 
#print(df)

mod = 5000
temp = mod

avgu = df['U'].mean()
avgv = df['V'].mean()
avgw = df['W'].mean()

#print(avgu)
#print(avgv)
#print(avgw)

df['U Avg']= ''
df['V Avg']= ''
df['W Avg']= ''

df.loc[0,['U Avg']] = avgu 
df.loc[0,['V Avg']] = avgv
df.loc[0,['W Avg']] = avgw


df['U1_avg'] = df['U']-avgu
df['V1_avg'] = df['V']-avgv
df['W1_avg'] = df['W']-avgw



#print(df)

df.loc[((df.U1_avg>0) & (df.V1_avg>0) & (df.W1_avg>0)),"octant"] = "+1"
df.loc[((df.U1_avg>0) & (df.V1_avg>0) & (df.W1_avg<0)),"octant"] = "-1"
df.loc[((df.U1_avg<0) & (df.V1_avg>0) & (df.W1_avg>0)),"octant"] = "+2"
df.loc[((df.U1_avg<0) & (df.V1_avg>0) & (df.W1_avg<0)),"octant"] = "-2"
df.loc[((df.U1_avg<0) & (df.V1_avg<0) & (df.W1_avg>0)),"octant"] = "+3"
df.loc[((df.U1_avg<0) & (df.V1_avg<0) & (df.W1_avg<0)),"octant"] = "-3"
df.loc[((df.U1_avg>0) & (df.V1_avg<0) & (df.W1_avg>0)),"octant"] = "+4"
df.loc[((df.U1_avg>0) & (df.V1_avg<0) & (df.W1_avg<0)),"octant"] = "-4"

#print(df)
########################################################### task 1 started


p1=0
n1=0
p2=0
n2=0
p3=0
n3=0
p4=0
n4=0


for i in df['octant']:
    if i=="+1":
        p1 = p1 +1
    elif i == "-1":
        n1 = n1 + 1
    elif i == "+2":
        p2 = p2 + 1
    elif i == "-2":
        n2 = n2 + 1
    elif i == "+3":
        p3 = p3 + 1
    elif i == "-3":
        n3 = n3 + 1
    elif i == "+4":
        p4 = p4 + 1
    elif i == "-4":
        n4 = n4 + 1
'''
print(p1)
print(n1)
print(p2)
print(n2)
print(p3)
print(n3)
print(p4)
print(n4)
'''
df[''] = ''

df.loc[1,['']] = 'user input'


df['Octant_id']= ''
df['+1']= ''
df['-1']= ''
df['+2']= ''
df['-2']= ''
df['+3']= ''
df['-3']= ''
df['+4']= ''
df['-4']= ''

df.loc[1,['Octant_id']] = 'mod ' + str(temp)

df.loc[0,['Octant_id']] = ['total count']

df.loc[0,['+1']] = p1
df.loc[0,['-1']] = n1
df.loc[0,['+2']] = p2
df.loc[0,['-2']] = n2
df.loc[0,['+3']] = p3
df.loc[0,['-3']] = n3
df.loc[0,['+4']] = p4
df.loc[0,['-4']] = n4

#print(df)
############################################################ task 1 competed

#temp = input("enter the value of mod : ")


#max_l = 30000

len = len(df)
i = 1
begin = 0
end = temp

while end<= len:
    df['Octant_id'][i+1] = str(begin) + "-" + str(end-1)
    l_1p=0
    l_1n=0
    l_2p=0
    l_2n=0
    l_3p=0
    l_3n=0
    l_4p=0
    l_4n=0    
    for j in range(begin,end): 
        if df['octant'][j]=="+1":
            l_1p = l_1p +1
        elif df['octant'][j] == "-1":
            l_1n = l_1n + 1
        elif df['octant'][j] == "+2":
            l_2p = l_2p + 1
        elif df['octant'][j] == "-2":
            l_2n = l_2n + 1
        elif df['octant'][j] == "+3":
            l_3p = l_3p + 1
        elif df['octant'][j] == "-3":
            l_3n = l_3n + 1
        elif df['octant'][j] == "+4":
            l_4p = l_4p + 1
        elif df['octant'][j] == "-4":
            l_4n = l_4n + 1
    df.loc[i+1,['+1']] = l_1p
    df.loc[i+1,['-1']] = l_1n
    df.loc[i+1,['+2']] = l_2p
    df.loc[i+1,['-2']] = l_2n
    df.loc[i+1,['+3']] = l_3p
    df.loc[i+1,['-3']] = l_3n
    df.loc[i+1,['+4']] = l_4p
    df.loc[i+1,['-4']] = l_4n
    begin = end
    i=i+1
    end = temp*i

#print(len)

if end>len:
    df['Octant_id'][i+1] = str(begin) + "-" + str(len-1)
    p_1p=0
    p_1n=0
    p_2p=0
    p_2n=0
    p_3p=0
    p_3n=0
    p_4p=0
    p_4n=0
    for j in range(begin,len):
        if df['octant'][j]=="+1":
            p_1p = p_1p +1
        elif df['octant'][j] == "-1":
            p_1n = p_1n + 1
        elif df['octant'][j] == "+2":
            p_2p = p_2p + 1
        elif df['octant'][j] == "-2":
            p_2n = p_2n + 1
        elif df['octant'][j] == "+3":
            p_3p = p_3p + 1
        elif df['octant'][j] == "-3":
            p_3n = p_3n + 1
        elif df['octant'][j] == "+4":
            p_4p = p_4p + 1
        elif df['octant'][j] == "-4":
            p_4n = p_4n + 1     
    df.loc[i+1,['+1']] = p_1p
    df.loc[i+1,['-1']] = p_1n
    df.loc[i+1,['+2']] = p_2p
    df.loc[i+1,['-2']] = p_2n
    df.loc[i+1,['+3']] = p_3p
    df.loc[i+1,['-3']] = p_3n
    df.loc[i+1,['+4']] = p_4p
    df.loc[i+1,['-4']] = p_4n   
     
