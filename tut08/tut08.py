import os #importing libraries
import math
from datetime import datetime #importing date and time
start_time = datetime.now()

os.system('cls')

def get_fall(element):  #defining a function named element
    index_no = int(element[:element.index('-')])  
    return(index_no)
