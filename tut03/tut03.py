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