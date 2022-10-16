
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

       