"""
title: This file contains functions that emulate the conditions of
deicison flow chart by NDOT
author: Akshay Kale
"""
import os
import csv
from tqdm import tqdm
import numpy as np
from collections import defaultdict

__author__ = 'Akshay Kale'
__copyright__ =  'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

def condition1_1(records):
    """
    Description: filter all the records where pile condition < 3
    Args:
        record (list): list to the bridge attributes
    Returns:
        structures (list): a list of structures that satisfy the condition
    """
    structures = list()
    for record in records:
        if record['column'] < 3:
            structure.append(True)
        else:
            structure.append(False)
    return structures

def flow_chart(filename):
    """
    Description: takes in filename and performs conditional checks
    Args:
        filename (string): path to the nbi file
    Returns:
        structures (list): a list of structures that require maintenance
    """
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
<<<<<<< HEAD
        for row in tqdm(csvReader):
=======
        for row in csvReader:
>>>>>>> added condition1_1 in flow.py
            print(row)
    return header

def main():
    directory ='../data/nbi/'
    csvFileName = '06-20-19-thesis-dataset_allstates_allstates.csv'
    filename = directory + csvFileName
    print(flow_chart(filename))

if __name__ == '__main__':
    main()
