import csv #importing important libraries

import pandas as pd

from datetime import datetime #import calender
import openpyxl
starting_time = datetime.now()

def attendance_report(): #function 
    try:
        inp_file = pd.read_csv('input_attendance.csv') #attendence file important
        inp = inp_file.fillna("Random") #Random in empty rows
    except:
        print("File not found")  
    
    
    try:
        rollno_inp=pd.read_csv('input_registered_students.csv')  #registered students file
    except:
        print('File containing name of all students is missing!')

     # mr = sheet_input.max_row
    mc=sum(1 for row in open("input_registered_students.csv"))  #mc variable is sum in registered studets
    mc_consolidated=sum(1 for row in open("input_attendance.csv")) #for input attendence csv
    total_dates=list()
    for j in range(0,mc_consolidated-1): #split year, month, day
        day=inp.at[j,'Timestamp'].split()[0].split('-')[0]
        month=inp.at[j,'Timestamp'].split()[0].split('-')[1]
        year=inp.at[j,'Timestamp'].split()[0].split('-')[2]
        date=datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d").date()  #finding day according to day
        day_name=date.strftime("%A")
        if day_name=="Monday" or day_name=="Thursday": 
            if inp.at[j,'Timestamp'].split()[0] not in total_dates: #considering monday and thrusday only in total dates
                total_dates.append(inp.at[j,'Timestamp'].split()[0])
    # max_att=0
    # max_roll=""
    fileName_consolidated=".\output\\attendance_report_consolidated.xlsx" #putting in output file

    output_file=openpyxl.Workbook() #output file
    output=output_file.active
    output_file.save(fileName_consolidated) #saving in consolidated file
