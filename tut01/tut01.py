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
################################################################ task 1 completed
