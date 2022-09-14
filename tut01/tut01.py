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