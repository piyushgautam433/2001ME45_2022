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
#temp = input("enter the value of mod : ")


#max_l = 30000

len = len(df) #to store total no. of rows
i = 1 #loop to calculate mod counts
begin = 0 #begin with zero
end = temp #temp variable created

while end<= len: #while loop started
    df['Octant_id'][i+1] = str(begin) + "-" + str(end-1)
    p1_1=0 #initialising value
    n1_1=0 #initialising value
    p2_1=0 #initialising value
    n2_1=0 #initialising value
    p3_1=0 #initialising value
    n3_1=0 #initialising value
    p4_1=0 #initialising value
    n4_1=0 #initialising value  
    for j in range(begin,end):
        #counting the values 
        if df['octant'][j]=="+1":
            p1_1 = p1_1 +1
        elif df['octant'][j] == "-1":
            n1_1 = n1_1 + 1
        elif df['octant'][j] == "+2":
            p2_1 = p2_1 + 1
        elif df['octant'][j] == "-2":
            n2_1 = n2_1 + 1
        elif df['octant'][j] == "+3":
            p3_1 = p3_1 + 1
        elif df['octant'][j] == "-3":
            n3_1 = n3_1 + 1
        elif df['octant'][j] == "+4":
            p4_1 = p4_1 + 1
        elif df['octant'][j] == "-4":
            n4_1 = n4_1 + 1
    #storing the values in different locations
    df.loc[i+1,['+1']] = p1_1
    df.loc[i+1,['-1']] = n1_1
    df.loc[i+1,['+2']] = p2_1
    df.loc[i+1,['-2']] = n2_1
    df.loc[i+1,['+3']] = p3_1
    df.loc[i+1,['-3']] = n3_1
    df.loc[i+1,['+4']] = p4_1
    df.loc[i+1,['-4']] = n4_1
    begin = end
    i=i+1
    end = temp*i

#print(len)

if end>len:
    df['Octant_id'][i+1] = str(begin) + "-" + str(len-1)
    p1_2=0 #initialising values
    n1_2=0 #initialising values
    p2_2=0 #initialising values
    n2_2=0 #initialising values
    p3_2=0 #initialising values
    n3_2=0 #initialising values
    p4_2=0 #initialising values
    n4_2=0 #initialising values
    for j in range(begin,len):
        #counting the values
        if df['octant'][j]=="+1":
            p1_2 = p1_2 +1
        elif df['octant'][j] == "-1":
            n1_2 = n1_2 + 1
        elif df['octant'][j] == "+2":
            p2_2 = p2_2 + 1
        elif df['octant'][j] == "-2":
            n2_2 = n2_2 + 1
        elif df['octant'][j] == "+3":
            p3_2 = p3_2 + 1
        elif df['octant'][j] == "-3":
            n3_2 = n3_2 + 1
        elif df['octant'][j] == "+4":
            p4_2 = p4_2 + 1
        elif df['octant'][j] == "-4":
            n4_2 = n4_2 + 1     