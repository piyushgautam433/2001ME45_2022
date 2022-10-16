
try:
   import pandas as pd
   import math
   def octant_longest_subsequence_count_with_range():
    try:
       df = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx")  #read input excel file
       df.head()
       df.loc[0,"Uavg"] = df["U"].mean()     #average for coloumns U,V,W 
       df.loc[0,"Vavg"] = df["V"].mean()
       df.loc[0,"Wavg"] = df["W"].mean()
       df["U1"] = df["U"]-df["U"].mean() #new columns for U1,V1,W1 
       df["V1"] = df["V"]-df["V"].mean()
       df["W1"] = df["W"]- df["W"].mean() 

       
       #creation of octant column
       df.loc[((df.U1 > 0) & (df.V1 > 0) & (df.W1 >0)), "Octant"] = "+1" 
       df.loc[((df.U1 > 0) &(df.V1 > 0) & (df.W1 <0)), "Octant" ] = "-1"
       df.loc[((df.U1 < 0) &(df.V1 > 0) & (df.W1 >0)), "Octant" ] = "+2"
       df.loc[((df.U1 < 0) &(df.V1 > 0) & (df.W1 <0)), "Octant" ] = "-2"    
       df.loc[((df.U1 < 0) &(df.V1 < 0) & (df.W1 >0)), "Octant" ] = "+3"
       df.loc[((df.U1 < 0) &(df.V1 < 0) & (df.W1 <0)), "Octant" ] = "-3"
       df.loc[((df.U1 > 0) &(df.V1 < 0) & (df.W1 >0)), "Octant" ] = "+4"
       df.loc[((df.U1 > 0) &(df.V1 < 0) & (df.W1 <0)), "Octant" ] = "-4"
       df.loc[0," "]=" "
       df.loc[0,"  "]="  "
       df.loc[0,"octant"]="+1"    # creating a column Count for +1
       df.loc[1,"octant"]="-1"    # creating a column Count for -1
       df.loc[2,"octant"]="+2"    # creating a column Count for +2
       df.loc[3,"octant"]="-2"    # creating a column Count for -2
       df.loc[4,"octant"]="+3"    # creating a column Count for +3
       df.loc[5,"octant"]="-3"    # creating a column Count for -3
       df.loc[6,"octant"]="+4"    # creating a column Count for +4
       df.loc[7,"octant"]="-4"    # creating a column Count for -4
       a=[]   #creating a array a for counting sequence (+1,+1 -1,-1 ........ +4,+4 -4,-4)
       for i in range(9) : 
          a.append(0)    # all elements to 0's in a a[]array 
       b=[]   # creating b array for storing maximum length of each subsequence for (+1,+1 -1,-1 ........ +4,+4 -4,-4)
       for i in range(9) : 
          b.append(0)     # inserting all elements to 0's in a b[]array
       c=[]    # creating c array for storing count of for maximum length of each subsequence for (+1,+1 -1,-1 ........ +4,+4 -4,-4)
       for i in range(9) : 
          c.append(0)  # inserting all elements to 0's in a c[]array
       mod=29744
       for i in range(mod) :
          a[int(df["Octant"][i])+4]=a[int(df["Octant"][i])+4]+1 # incrementing count for each part of subsequene
          if a[int(df["Octant"][i])+4] != a[int(df["Octant"][i+1])+4]:
             if(a[int(df["Octant"][i])+4]>b[int(df["Octant"][i])+4]):
               b[int(df["Octant"][i])+4]=max(a[int(df["Octant"][i])+4],b[int(df["Octant"][i])+4])#finding max length of each subsequence
               c[int(df["Octant"][i])+4]=1 
               a[int(df["Octant"][i])+4] =0
             else :
               if(a[int(df["Octant"][i])+4]==b[int(df["Octant"][i])+4]):
                  c[int(df["Octant"][i])+4] += 1 # incrementing count for each subsequence of maximum length
                  a[int(df["Octant"][i])+4] =0
               if (a[int(df["Octant"][i])+4]<b[int(df["Octant"][i])+4]):
                   a[int(df["Octant"][i])+4] =0