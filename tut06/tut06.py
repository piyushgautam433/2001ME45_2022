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
