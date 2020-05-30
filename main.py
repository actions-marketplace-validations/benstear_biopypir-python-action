#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:09:37 2020

@author: stearb
"""

# read biopypir_log
# get name date, run id, and info
# and check if anything is different, only change 'last checked' if everything same   
import os
import time
import json
import pandas as pd

import tabulate as tb

import glob
import numpy as np

local_path= '/Users/stearb/desktop/temp_biop/logs/*.json'
logs_path = "logs/*.json"


all_logs = glob.glob(logs_path) 
#all_logs = glob.glob(local_path) 
print('Total Logs found: '+str(len(all_logs)))

new = 1

if new:
    for i in range(0,1): #len(all_logs)):
        with open(all_logs[i]) as f:
                data = json.load(f)

#log1 =  json.loads(data)
    

#def create_table(log_path_list):

    
df = pd.DataFrame([data['Package'],'Gold','TaylorLab'])#,columns=['Package','Badge'])
df.to_csv('table1.csv',sep='\t')  

print("::set-output name=table_output::{df}")

'''
def main():
    
    repo_name = os.environ["INPUT_MYREPO"]
    python_version = os.environ["INPUT_PYTHON_VERSION"]
    os = os.environ["INPUT_OS"]
    lint = os.environ["INPUT_LINT"]
    package_name = os.environ["INPUT_PACKAGE_NAME"]
    
    
    print(os.system('echo $PWD'))
    
    print(os.system('ls -a'))
    
    #my_output = str(my_input)
    #print(f"::set-output name=myOUTPUT::{my_output}")
    print(f"www.github.com/{my_input}")
'''

if __name__ == "__main__":
    main()
    print("www.github.com/benstear")
    
