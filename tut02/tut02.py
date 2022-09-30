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
    #storing values in different locations
    df.loc[i+1,['+1']] = p1_2
    df.loc[i+1,['-1']] = n1_2
    df.loc[i+1,['+2']] = p2_2
    df.loc[i+1,['-2']] = n2_2
    df.loc[i+1,['+3']] = p3_2
    df.loc[i+1,['-3']] = n3_2
    df.loc[i+1,['+4']] = p4_2
    df.loc[i+1,['-4']] = n4_2   
    


    ##################################################### task2 completed
    ####### task-3 starts here ##############

### calculating overall transition count #####

def trans(first,end,mac):
    rows, cols = (9,9)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for pop in range(first,end-1) : 
        arr[int(df["octant"][pop])+4][int(df["octant"][pop+1])+4]=arr[int(df["octant"][pop])+4][int(df["octant"][pop+1])+4]+1
    z=5    
    for i in range(8) :
        if(i%2==0) :
            df['+1'][i+mac]=arr[z][5]            # count of +1 - +1 is stored in arr[4+1][4+1]   [adding 4 to each index +1,-1,+2,-2,+3,-3,+4,-4]
        if(i%2!=0) :                             # count of +1 - -1 is stored in arr[4+1][4-1]
            z=8-z                                # count of +1 - +2 is stored in arr[4+1][2+4]
            df['+1'][i+mac]=arr[z][5]            # count of +1 - -2 is stored in arr[1+4][-2+4]
            z=8-z                                # count of +1 - +3 is stored in arr[4+1][3+4]
            z=z+1                                # count of +1 - -3 is stored in arr[4+1][-3+4]
    z=5                                          # count of +1 - +4 is stored in arr[4+1][4+4]
    for i in range(8) :                          # count of +1 - -4 is stored in arr[4+1][-4+4]
        if(i%2==0) :
            df['-1'][i+mac]=arr[z][3]
        if(i%2!=0) :                             # count of +2 - +1 is stored in arr[4+2][1+4]
            z=8-z                                # count of +2 - -1 is stored in arr[4+2][-1+4]
            df["-1"][i+mac]=arr[z][3]            # count of +2 - +2 is stored in arr[4+2][2+4]
            z=8-z                                # count of +2 - -2 is stored in arr[4+2][-2+4]
            z=z+1                                # count of +2 - +3 is stored in arr[4+2][3+4]
    z=5                                          # count of +2 - -3 is stored in arr[4+2][-3+4]
    for i in range(8) :                          # count of +2 - +4 is stored in arr[4+2][4+4]
        if(i%2==0) :                             # count of +2 - -4 is stored in arr[4+2][-4+4]
            df["+2"][i+mac]=arr[z][6]
        if(i%2!=0) :
            z=8-z
            df["+2"][i+mac]=arr[z][6]            # count of +3 - +1 is stored in arr[4+3][1+4]
            z=8-z                                # count of +3 - -1 is stored in arr[4+3][-1+4]
            z=z+1                                # count of +3 - +2  is stored in arr[4+3][2+4]
    z=5                                          # count of +3 - -2  is stored in arr[4+3][-2+4]
    for i in range(8) :                          # count of +3 - +3  is stored in arr[4+3][3+4]
        if(i%2==0) :                             # count of +3 - -3  is stored in arr[4+3][-3+4]
            df["-2"][i+mac]=arr[z][2]            # count of +3 - +4  is stored in arr[4+3][4+4]
        if(i%2!=0) :                             # count of +3 - -4  is stored in arr[4+3][-4+4]
            z=8-z
            df["-2"][i+mac]=arr[z][2]
            z=8-z
            z=z+1

    z=5                                          # count of +4 - +1  is stored in arr[4+4][1+4]
    for i in range(8) :                          # count of +4 - -1  is stored in arr[4+4][-1+4]
        if(i%2==0) :                             # count of +4 - +2  is stored in arr[4+4][2+4]
            df["+3"][i+mac]=arr[z][7]            # count of +4 - -2  is stored in arr[4+4][-2+4]
        if(i%2!=0) :                             # count of +4 - +3  is stored in arr[4+4][3+4]
            z=8-z                                # count of +4 - -3  is stored in arr[4+4][-3+4]
            df["+3"][i+mac]=arr[z][7]            # count of +4 - +4  is stored in arr[4+4][4+4]
            z=8-z                                # count of +4 - -4  is stored in arr[4+4][-4+4]
            z=z+1

    z=5
    for i in range(8) :
        if(i%2==0) :
            df["-3"][i+mac]=arr[z][1]
        if(i%2!=0) :
            z=8-z
            df["-3"][i+mac]=arr[z][1]
            z=8-z
            z=z+1
    z=5
    for i in range(8) :
        if(i%2==0) :
            df["+4"][i+mac]=arr[z][8]
        if(i%2!=0) :
            z=8-z
            df["+4"][i+mac]=arr[z][8]
            z=8-z
            z=z+1
    z=5
    for i in range(8) :
        if(i%2==0) :
            df["-4"][i+mac]=arr[z][0]
        if(i%2!=0) :
            z=8-z
            df["-4"][i+mac]=arr[z][0]
            z=8-z
            z=z+1

df.loc[13,['']] = ['overall Transition Count']
df.loc[14,['+1']] = ['To']
df.loc[15,['Octant_id']] = ['count']
df.loc[16,['Octant_id']] = ['+1']
df.loc[17,['Octant_id']] = ['-1']
df.loc[18,['Octant_id']] = ['+2']
df.loc[19,['Octant_id']] = ['-2']
df.loc[20,['Octant_id']] = ['+3']
df.loc[21,['Octant_id']] = ['-3']
df.loc[22,['Octant_id']] = ['+4']
df.loc[23,['Octant_id']] = ['-4']
df.loc[15,['+1']] = ['+1']
df.loc[15,['-1']] = ['-1']
df.loc[15,['+2']] = ['+2']
df.loc[15,['-2']] = ['-2']
df.loc[15,['+3']] = ['+3']
df.loc[15,['-3']] = ['-3']
df.loc[15,['+4']] = ['-4']
df.loc[15,['-4']] = ['+4']
trans(0,len-1,16)
#### creating a 9 x 9 matrix to store the values of transition values
###  [adding 4 to each index +1,-1,+2,-2,+3,-3,+4,-4]


 

    
mod_i = mod
mac = 27
i=1
start = 0
last = mod_i

while last<= len:

    ### making mod trasition table using while loop as did before
    df.loc[mac,['']] = ['mod Transition Count']
    df.loc[mac+1,['Octant_id']] = str(start)+'-'+str(last-1)
    df.loc[mac+1,['+1']] = ['To']
    df.loc[mac+2,['Octant_id']] = ['count']
    df.loc[mac+3,['Octant_id']] = ['+1']
    df.loc[mac+4,['Octant_id']] = ['-1']
    df.loc[mac+5,['Octant_id']] = ['+2']
    df.loc[mac+6,['Octant_id']] = ['-2']
    df.loc[mac+7,['Octant_id']] = ['+3']
    df.loc[mac+8,['Octant_id']] = ['-3']
    df.loc[mac+9,['Octant_id']] = ['+4']
    df.loc[mac+10,['Octant_id']] = ['-4']
    df.loc[mac+2,['+1']] = ['+1']
    df.loc[mac+2,['-1']] = ['-1']
    df.loc[mac+2,['+2']] = ['+2']
    df.loc[mac+2,['-2']] = ['-2']
    df.loc[mac+2,['+3']] = ['+3']
    df.loc[mac+2,['-3']] = ['-3']
    df.loc[mac+2,['+4']] = ['-4']
    df.loc[mac+2,['-4']] = ['+4']  
    trans(start,last,mac+3)



    mac = mac + 13
    start = last
    i=i+1
    last = mod_i*i

if last>len:
    df.loc[mac,['']] = ['mod Transition Count']
    df.loc[mac+1,['Octant_id']] = str(start)+'-'+str(len-1)
    df.loc[mac+1,['+1']] = ['To']
    df.loc[mac+2,['Octant_id']] = ['count']
    df.loc[mac+3,['Octant_id']] = ['+1']
    df.loc[mac+4,['Octant_id']] = ['-1']
    df.loc[mac+5,['Octant_id']] = ['+2']
    df.loc[mac+6,['Octant_id']] = ['-2']
    df.loc[mac+7,['Octant_id']] = ['+3']
    df.loc[mac+8,['Octant_id']] = ['-3']
    df.loc[mac+9,['Octant_id']] = ['+4']
    df.loc[mac+10,['Octant_id']] = ['-4']
    df.loc[mac+2,['+1']] = ['+1']
    df.loc[mac+2,['-1']] = ['-1']
    df.loc[mac+2,['+2']] = ['+2']
    df.loc[mac+2,['-2']] = ['-2']
    df.loc[mac+2,['+3']] = ['+3']
    df.loc[mac+2,['-3']] = ['-3']
    df.loc[mac+2,['+4']] = ['-4']
    df.loc[mac+2,['-4']] = ['+4']
    ## using trans function to count trasition count and insrt values into dataframe
    ##  please ignore warning "setting with copy "
    trans(start,len,mac+3)
