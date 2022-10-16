
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