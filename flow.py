"""
title: This file contains functions that emulate the conditions of
deicison flow chart by NDOT
author: Akshay Kale

Notes:
     - TODO:
        Preprocess (Pipeline):
          1. (List) Extract all the necessary attribute
          2. Using if and else, create a pipeline, that takes in:
                      1. Args: (record, datastructure)
                      2. Returns: report (JSON datastructure)
          3. Run decision flow chart -> Create condition Report

        Datastructure ( Report ):
          1. {structure: {condition1: True,
                           condition2: False,
                           condition3: True,
                           condition4: False,
                           condition5: False
             }}

        Create Decision Flow Chart:
          1. For every record -> pipeline (preprocess) -> Report
          2. preprocess
"""
import csv
from collections import defaultdict

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
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
            structures.append(True)
        else:
            structures.append(False)
    return structures


def decision_flow_chart(listOfFields):
    """
    Description: takes in filename and performs conditional checks
    Args:
        filename (string): path to the nbi file
    Returns:
        structures (list): a list of structures that require maintenance
    """
    report = list()
    for record in listOfFields:
        # Extract fields
        # execute function with field
        print(record)
        break
        #fieldStat1_1 = condition1_1(field)

        #field1 = record[0]
        #if condition1_1(fieldStat1_1) is True:
        #    report.append(True)
        #elif condition1_2(field1) is True:
        #    report.append(False)
        #else:
        #    report.append(None)
    return report

def get_state_data(listOfAllField, state='31'):
    """
    Description: Get nebraska data.
    Args:
        - listOfAllFields: Inspection records of all states.
        - state: 'NE'.
    Return: data (list): list of inspection records from the state.
    """
    data = list()
    for record in listOfAllField:
        if record['State Code'] == state:
            data.append(record.values())
    return data


def read_csv(filename):
    """
    Description: takes in filename and performs conditional checks
    Args:
        filename (string): path to the nbi file
    Returns:
        structures (list): a list of structures that require maintenance
    """
    listOfFields = list()
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        header = next(csvReader)
        recordDict = defaultdict()
        for row in csvReader:
            recordDict = {head:val for head, val in zip(header[1:], row[1:])}
            listOfFields.append(recordDict)
    return header, listOfFields


def main():
    directory = '../data/nbi/'
    # need the raw nbi file
    csvFileName = '06-20-19-thesis-dataset-without-outliers_allstates.csv'
    filename = directory + csvFileName
    header, listOfFields = read_csv(csvFileName)
    stateData = get_state_data(listOfFields)
    print(stateData)
    #decision_flow_chart(listOfFields)


if __name__ == '__main__':

    main()
