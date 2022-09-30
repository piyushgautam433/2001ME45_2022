#HareKrishna
import pandas as pd #panda is imported
df = pd.read_excel(r"input_octant_transition_identify.xlsx")#input csv file imported
#print(df)

mod = 5000
temp = mod #temp variable to store values of mod

avgu = df['U'].mean()  
avgv = df['V'].mean()
avgw = df['W'].mean()
#avf of all values in U, V, W
#print(avgu)
#print(avgv)
#print(avgw)

df['U Avg']= '' #new column created
df['V Avg']= '' #new column created
df['W Avg']= '' #new column created

df.loc[0,['U Avg']] = avgu 
df.loc[0,['V Avg']] = avgv
df.loc[0,['W Avg']] = avgw


df['U1_avg'] = df['U']-avgu  #subtracting cell value with avg U
df['V1_avg'] = df['V']-avgv  #subtracting cell value with avg V
df['W1_avg'] = df['W']-avgw  #subtracting cell value with avg W



#print(df)
#categorising values in different octants
df.loc[((df.U1_avg>0) & (df.V1_avg>0) & (df.W1_avg>0)),"octant"] = "+1"
df.loc[((df.U1_avg>0) & (df.V1_avg>0) & (df.W1_avg<0)),"octant"] = "-1"
df.loc[((df.U1_avg<0) & (df.V1_avg>0) & (df.W1_avg>0)),"octant"] = "+2"
df.loc[((df.U1_avg<0) & (df.V1_avg>0) & (df.W1_avg<0)),"octant"] = "-2"
df.loc[((df.U1_avg<0) & (df.V1_avg<0) & (df.W1_avg>0)),"octant"] = "+3"
df.loc[((df.U1_avg<0) & (df.V1_avg<0) & (df.W1_avg<0)),"octant"] = "-3"
df.loc[((df.U1_avg>0) & (df.V1_avg<0) & (df.W1_avg>0)),"octant"] = "+4"
df.loc[((df.U1_avg>0) & (df.V1_avg<0) & (df.W1_avg<0)),"octant"] = "-4"

#print(df)
################################################################ preprocessing done
p1=0 #initialising value
n1=0 #initialising value
p2=0 #initialising value
n2=0 #initialising value
p3=0 #initialising value
n3=0 #initialising value
p4=0 #initialising value
n4=0 #initialising value

#for loop to counting the values
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

#empty column is created
df[''] = ''

df.loc[1,['']] = 'user input'


df['Octant_id']= '' #column created
df['+1']= '' #column created
df['-1']= '' #column created
df['+2']= '' #column created
df['-2']= '' #column created
df['+3']= '' #column created
df['-3']= '' #column created
df['+4']= '' #column created
df['-4']= '' #column created

df.loc[1,['Octant_id']] = 'mod ' + str(temp)

df.loc[0,['Octant_id']] = ['total count']

df.loc[0,['+1']] = p1 #inserting values in dataframe
df.loc[0,['-1']] = n1 #inserting values in dataframe
df.loc[0,['+2']] = p2 #inserting values in dataframe
df.loc[0,['-2']] = n2 #inserting values in dataframe
df.loc[0,['+3']] = p3 #inserting values in dataframe
df.loc[0,['-3']] = n3 #inserting values in dataframe
df.loc[0,['+4']] = p4 #inserting values in dataframe
df.loc[0,['-4']] = n4 #inserting values in dataframe

#print(df)
############################################################ task 1 competed