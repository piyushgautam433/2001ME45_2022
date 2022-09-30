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