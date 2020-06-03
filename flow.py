"""
title: This file contains functions that emulate the conditions of
deicison flow chart by NODT
author: Akshay Kale
"""
import os
import csv
from tqdm import tqdm
import numpy as np

__author__ = 'Akshay Kale'
__copyright__ =  'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

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
        for row in tqdm(csvReader):
            print(row)
    return header

def main():
    directory ='../data/nbi/'
    csvFileName = '06-20-19-thesis-dataset_allstates_allstates.csv'
    filename = directory + csvFileName
    print(flow_chart(filename))

if __name__ == '__main__':
    main()
