'''
rat data converter for the Neuro Lab at WSU (commissioned by Damien Lybrand) 
- goal: convert file of delimited data to a sorted and readable version 
- current version: prototype
- current capabilities: sort data for one rat 
- future tasks: input checking, error handling for incomplete files, sort several rats' data for multiple days. 

'''

import openpyxl
import pandas as pd


def sort_excel_data(input_file, output_file):
    # Load the Excel file
    workbook = openpyxl.load_workbook(input_file)# Assume the first sheet in the workbook
    sheet = workbook.active
    
    found_box = False  # for debugging
    found_right_lever = False # for debugging
    found_left_lever = False
    start_extracting = False
    # box numbering starts at one, so setting this to zero serves as an error flag.
    box_num = 0

    ''' discard all data before the box number is encountered. 
    Then discard all data between box and first lever press delimiter.
    Keep all data attached to lever press delimiters.  '''

    # Create a new workbook and sheet
    new_workbook = openpyxl.Workbook()
    new_sheet = new_workbook.active

    left_lever_data = []
    right_lever_data = []
    # Iterate through each cell in the original sheet: First idenfity 'box' delimiter
    for row in sheet.iter_rows(values_only=True):
        
        for cell_value in row:
            if 'Box:' in str(cell_value):
                found_box = True
                box_num += 1  # if box is found, increment box num.
                new_sheet.append([cell_value]) # append value of box num to the new sheet
                new_sheet.append([box_num]) # incremented to keep track
            if found_box:
                if 'L:' in str(cell_value):
                    found_left_lever = True
                    new_sheet.append([cell_value]) 
                    start_extracting = True
                    continue                         
                if 'R:' in str(cell_value):
                    #new_sheet.append([cell_value]) 
                    found_right_lever = True
                    start_extracting = False
                    
                if start_extracting and isinstance(cell_value, (int, float)) and ':' not in str(cell_value):
                        left_lever_data.append(cell_value)
                        
                if found_right_lever and isinstance(cell_value, (int, float)) and ':' not in str(cell_value):
                        right_lever_data.append(cell_value)
                        
                        
    for value in left_lever_data: 
        new_sheet.append([value]) 
        
    new_sheet.append(["R:"])
    
    for value in right_lever_data:
        new_sheet.append([value])
        
    # Insert single-cell data lists for each lever so Damien can copy-paste into Matlab
    new_sheet.append(["L:"])
    left_lever_cell = ', '.join(map(str, left_lever_data))
    new_sheet.append([left_lever_cell])
    
    new_sheet.append(["R:"])
    right_lever_cell = ', '.join(map(str, right_lever_data))
    new_sheet.append([right_lever_cell])
        
        
                        
    # TODO: make second column: running total
    
    # TODO: make third column: running total / 60 
    

    
    

    #    Print messages outside the loop based on the results
    if not found_left_lever:
        print(
            "Left Lever press delimiter [ L: ] not found! Unable to parse file.")
    if not found_right_lever:
        print(
            "Right Lever press delimiter [ R: ] not found! Unable to parse file.")

    # Save the new workbook to the output file
    new_workbook.save(output_file)


if __name__ == "__main__":
    # Provide the input and output file paths
    print(" Hello, Welcome to RatSort! ")
    print(" RatSort will require an input file path and return the path of the updated file.")

    input_file_path = input("paste or type input file path here: ")

    # input_file_path = "input_data.xlsx"
    output_file_path = "sorted_data.xlsx"

    # Call the function to sort the data
    sort_excel_data(input_file_path, output_file_path)

    print(f"Data has been sorted and saved to {output_file_path}")
    print("Check the folder of this program for your sorted Data. ")
