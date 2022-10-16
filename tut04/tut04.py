
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
       df.loc[0,"length of longest subsequence"] = b[5]           # storing maximum length of subsequence +1 in b[5]
       df.loc[1,"length of longest subsequence"] = b[3]           # storing maximum length of subsequence -1 in b[3]
       df.loc[2,"length of longest subsequence"] = b[6]           # storing maximum length of subsequence +2 in b[6]
       df.loc[3,"length of longest subsequence"] = b[2]           # storing maximum length of subsequence -2 in b[2]
       df.loc[4,"length of longest subsequence"] = b[7]           # storing maximum length of subsequence +3 in b[7]
       df.loc[5,"length of longest subsequence"] = b[1]           # storing maximum length of subsequence -3 in b[2]
       df.loc[6,"length of longest subsequence"] = b[8]           # storing maximum length of subsequence +4 in b[8]
       df.loc[7,"length of longest subsequence"] = b[0]           # storing maximum length of subsequence -4 in b[0] 
       df.loc[0,"count"] = c[5]                                # storing count of maximum length of subsequence +1 in c[5]
       df.loc[1,"count"] = c[3]                                # storing count of maximum length of subsequence -1 in c[3]
       df.loc[2,"count"] = c[6]                                # storing count of maximum length of subsequence +2 in c[6]   
       df.loc[3,"count"] = c[2]                                # storing count of maximum length of subsequence -2 in c[2]     
       df.loc[4,"count"] = c[7]                                # storing count of maximum length of subsequence +3 in c[7]   
       df.loc[5,"count"] = c[1]                                # storing count of maximum length of subsequence +2 in c[1]   
       df.loc[6,"count"] = c[8]                                # storing count of maximum length of subsequence +2 in c[8]   
       df.loc[7,"count"] = c[0]                                # storing count of maximum length of subsequence +2 in c[0] 
       df.loc[0,"   "]=""
       v=1
       w=0
       for i in range(8) :
           df.loc[w,"OCTANT"]=df["octant"][i] #copying data in octant to OCTANT coiumn
           df.loc[w,"length of longest subsequence"]=df["length of longest subsequence"][i] #copying data in length of longest subsequence  to length of longest subsequence coiumn
           df.loc[w,"Frequency"]=df["count"][i] #copying data in count to Frequency coiumn
           df.loc[v,"OCTANT"]="TIME"#inserting time in OCTANT Column for each value of v
           df.loc[v,"length of longest subsequence"]="From"#inserting FROM in length of longest subsequence Column for each value of v
           df.loc[v,"Frequency"]="To"#inserting To in Frequency  Column for each value of v
           v=v+2+df["count"][i]
           w=w+2+df["count"][i]
       rows, cols = (9, 4)
       begin = [[0 for i in range(cols)] for j in range(rows)]#assiging 0'sto each and every row and column of 2d list begin
       rows, cols = (9, 4)
       end = [[0 for i in range(cols)] for j in range(rows)]#assiging 0'sto each and every row and column of 2d list end
       arr=[]
       for i in range(9) : 
          arr.append(0)    #assiging 0'sto each element 1d list arr
       empty=[]
       for i in range(9) : 
          empty.append(0) #assiging 0'sto each element 1d list empty
       begin[int(df["Octant"][0])+4][empty[int(df["Octant"][0])+4]]=float(df["Time"][0])#assigning begin to 1st value of Time coloumn 
       for i in range(29745) : 
           arr[int(df["Octant"][i])+4]=arr[int(df["Octant"][i])+4]+13 #incrementing count of each value of octant 
           if(i==29744) :
             if arr[int(df["Octant"][i])+4]!=b[int(df["Octant"][i])+4] :
                begin[int(df["Octant"][i])+4][empty[int(df["Octant"][i])+4]]=0 #increment
                continue
           if df["Octant"][i]!=df["Octant"][i+1] : 
                  if arr[int(df["Octant"][i])+4]==(b[int(df["Octant"][i])+4]) :#count of each octant is equal to max of count of each octant
                    end[int(df["Octant"][i])+4][empty[int(df["Octant"][i])+4]]=float(df["Time"][i])#updating end to lqst value of particular octant
                    empty[int(df["Octant"][i])+4]= empty[int(df["Octant"][i])+4]+1# incrementing empty list 
                    arr[int(df["Octant"][i])+4]=0# making arr list to 0
                    begin[int(df["Octant"][i+1])+4][empty[int(df["Octant"][i+1])+4]]=float(df["Time"][i+1])
                  else :
                    begin[int(df["Octant"][i])+4][empty[int(df["Octant"][i])+4]]=0#updating begin to 0
                    arr[int(df["Octant"][i])+4]=0
                    begin[int(df["Octant"][i+1])+4][empty[int(df["Octant"][i+1])+4]]=float(df["Time"][i+1])
       u=2
       j1=0             
       for i in range(8) :
          for j in range(int(df["count"][j1]))  :
             df.loc[u,"length of longest subsequence"]=begin[int(df["octant"][i])+4][j]# inserting values of begin and end to length of longest subsequence and frequency repectively
             df.loc[u,"Frequency"]=end[int(df["octant"][i])+4][j]
             u=u+1
          u=u-df["count"][j1]
          u=u+2+df["count"][i]
          j1=j1+1
       df.to_excel("output_octant_longest_subsequence_with_range.xlsx",index=False) #output file
    except :
       print("the input file does not exists/or any error")   #writing except condition
   octant_longest_subsequence_count_with_range()
except :
    print("install pandas,math and import it")    
       
       