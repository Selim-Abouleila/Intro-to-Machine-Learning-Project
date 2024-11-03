# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:12:57 2024

@author: raphael
"""

import csv


def prepare_data(input_file, output_file):
    with open(input_file, "r") as infile:
        reader = csv.reader(infile)
        
        with open(output_file, "w", newline='') as outfile:
            writer = csv.writer(outfile)
            
            for row in reader:
                if row[1] == "M":
                    row[1] = "1"
                elif row[1] == "F":
                    row[1] = "2"
                
                if row[2] == "HIGH":
                    row[2] = "3"
                elif row[2] == "NORMAL":
                    row[2] = "2"
                elif row[2] == "LOW":
                    row[2] = "1"
                    
                if row[3] == "HIGH":
                    row[3] = "3"  
                elif row[3] == "NORMAL":
                    row[3] = "2"  
                elif row[3] == "LOW":
                    row[3] = "1"
                
                if row[5] == "drugA":
                    row[5] = "1"  
                elif row[5] == "drugB":
                    row[5] = "2" 
                elif row[5] == "drugC":
                    row[5] = "3"
                elif row[5] == "drugX":
                    row[5] = "4" 
                elif row[5] == "drugY":
                    row[5] = "5"
                
                
                writer.writerow([','.join(row)])
    print ("data ready for work")

input_file = 'drug200.csv'  
output_file = 'drug200_modified.csv'  
prepare_data(input_file, output_file)