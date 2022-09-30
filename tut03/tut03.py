# import pandas as pd and csv module
import pandas as pd #panda is imported
data = pd.read_excel(r"input_octant_longest_subsequence.xlsx")#input csv file imported
#print(df)
#avg of all values in U, V, W
u_avg=data['U'].mean()
v_avg=data['V'].mean()
w_avg=data['W'].mean()


data.at[0,'U_avg']=u_avg #location where avg value is stored
data.at[0,'V_avg']=v_avg #location where avg value is stored
data.at[0,'W_avg']=w_avg #location where avg value is stored
row=0

# initializing octant values
#p denotes positive and n denotes negative
count_p1=0 
count_n1=0
count_p2=0
count_n2=0
count_p3=0
count_n3=0
count_p4=0
count_n4=0
string=""
# making average columns 
for ele in data['V']:
    x=data.at[row,"U'=U-Uavg"]=data.at[row,'U']-u_avg
    y=data.at[row,"U'=U-Vavg"]=data.at[row,'V']-v_avg
    z=data.at[row,"U'=U-Wavg"]=data.at[row,'W']-w_avg
#assigning different values for different data according to its value
    try:
        if x>0:
            if y>0:
                if z>0:
                    data.at[row,'octant']='+1'
                    count_p1=count_p1+1 
                else:
                    data.at[row,'octant']="-1"
                    count_n1=count_n1+1
            else:
                if z>0:
                    data.at[row,'octant']='+4'
                    count_p4=count_p4+1
                else:
                    data.at[row,'octant']='-4'
                    count_n4=count_n4+1
        else:
            if y>0:
                if z>0:
                    data.at[row,'octant']='+2'
                    count_p2=count_p2+1
                else:
                    data.at[row,'octant']='-2'
                    count_n2=count_n2+1
            else:
                if z>0:
                    data.at[row,'octant']='+3'
                    count_p3=count_p3+1
                else:
                    data.at[row,'octant']='-3'
                    count_n3=count_n3+1
    except:
        print("octant can't be created")
    string+=data.at[row,'octant']
    row=row+1
    octant=data['octant'].tolist()
length=row
dict={'-4':0,'-3':0,'-2':0,'-1':0,'+1':0,'+2':0,'+3':0,'+4':0}
#subarray
#ction for longest continuous subarray
def subarray(n):
    c=0
    mx=0
    for i in range(length):
        x=data.at[i,'octant']
        if(x==n):
            c+=1
        else:
            mx=max(mx,c)
            c=0
    return mx
dict['-1']=subarray('-1')
dict['+1']=subarray('+1')
dict['-2']=subarray('-2')
dict['-3']=subarray('-3')
dict['-4']=subarray('-4')
dict['+2']=subarray('+2')
dict['+3']=subarray('+3')
dict['+4']=subarray('+4')

count_dict={'-4':1,'-3':1,'-2':1,'-1':1,'+1':1,'+2':1,'+3':1,'+4':1}

#using string count the number of longest continuous subarray
count_dict['-4']=string.count('-4'*dict['-4'])
count_dict['-3']=string.count('-3'*dict['-3'])
count_dict['-2']=string.count('-2'*dict['-2'])
count_dict['-1']=string.count('-1'*dict['-1'])
count_dict['+1']=string.count('+1'*dict['+1'])
count_dict['+2']=string.count('+2'*dict['+2'])
count_dict['+3']=string.count('+3'*dict['+3'])
count_dict['+4']=string.count('+4'*dict['+4'])
j=-4
i=0
k=""
#write the count and length in dataframe
while i<8:
    if(j>0):k='+'+str(j)
    else:k=str(j)
    if(j==0):
        j+=1
        continue
    data.at[i,"Value"]=k
    data.at[i,"Longest Subsequence Length"]=dict[k]
    data.at[i,"Count"]=count_dict[k]
    i+=1
    j+=1