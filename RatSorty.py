'''
rat data converter for the Neuro Lab at WSU (commissioned by Damien Lybrand) 
- goal: convert file of delimited data to a sorted and readable version 
- current version: prototype
- current capabilities: sort data for one rat 
- future tasks: input checking, error handling for incomplete files, sort several rats' data for multiple days. 

'''

import openpyxl
import pandas as pd


def sort_excel_data(input_file, output_file, start_delimiter = 'L:', end_delimiter = 'R:'):
    # Load the Excel file
    workbook = openpyxl.load_workbook(input_file)

    # Assume the first sheet in the workbook
    sheet = workbook.active

    found_box = False
    found_right_lever = False
    found_left_lever = False
    # box numbering starts at one, so setting this to zero serves as an error flag.
    box_num = 0

    ''' discard all data before the box number is encountered. 
    Then discard all data between box and first lever press delimiter.
    Keep all data attached to lever press delimiters.  '''

    # Create a new workbook and sheet
    new_workbook = openpyxl.Workbook()
    new_sheet = new_workbook.active

    # Iterate through each cell in the original sheet: First idenfity 'box' delimiter
    for row in sheet.iter_rows(values_only=True):
        for cell_value in row:
            # If 'box' is found, set the flag to True
            if 'Box 1:' in str(cell_value):
                found_box = True
                box_num += 1  # if box is found, increment box num.
                
                if found_box:
                 new_sheet.append([cell_value]) # append value of box num to the new sheet
                 # will only append once
                else:  # elif not found_box? 
                 print(" Box number not found - please wait for file parsing.")

    # TODO: discard all data between box value and L: delimiter. 
            if 'L:' in str(cell_value):
                new_sheet.append([cell_value])
                found_left_lever = True
                if ':' not in str(cell_value) and type(cell_value) != int: #int not in str(cell_value):
                   # new_sheet.append([cell_value]) # append values that aren't timestamps.
                   sorted_column.append(cell.value)
 
                        
            if 'R:' in str(cell_value):
                    new_sheet.append([cell_value])
                    found_right_lever = True
                    if ':' not in str(cell_value) and type(cell_value) != int: #and int not in str(cell_value):
                       # new_sheet.append([cell_value]) # append values that aren't timestamps. 
                        sorted_column.append(cell.value)

    # next sort all numerical data into columns. 
    sorted_column = []

    for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
        for cell in row:

            # Check if the cell contains a numeric value
            if isinstance(cell.value, (int, float)):
                sorted_column.append(cell.value)

    # Sort the numeric values
    sorted_column = sorted(sorted_column)
    
    # TODO: make second column: running total
    
    # TODO: make third column: running total / 60 
    

    # Write the sorted numeric values to the new sheet
    for value in sorted_column:
        new_sheet.append([value])
    
    

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

    # if

    # input_file_path = "input_data.xlsx"
    output_file_path = "sorted_data.xlsx"

    # Call the function to sort the data
    sort_excel_data(input_file_path, output_file_path)

    print(f"Data has been sorted and saved to {output_file_path}")
    print("Check the folder of this program for your sorted Data. ")
