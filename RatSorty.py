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
            if 'Box:' in str(cell_value):
                found_box = True
                box_num += 1  # if box is found, increment box num.

            # If 'box' has been found, append the value to the new sheet
            if found_box:
                new_sheet.append([cell_value])
            else:
                print(" Box number not found. Unable to parse file.")

    # Iterate through each cell in the sheet
    for row in sheet.iter_rows(values_only=True):
        for cell_value in row:
            if cell_value is not None:
                # Check for left lever
                if 'L:' in str(cell_value):
                    found_left_lever = True
                    # Stop appending when 'R:' is encountered
                    while not ('R:' in str(cell_value)):
                        # Discard timestamps
                        if ':' not in str(cell_value):
                            new_sheet.append([cell_value])
                        # Update cell_value for the next iteration
                        cell_value = next(row, None)
                    break  # Exit the loop after finding 'R:'

                # Check for right lever
                elif 'R:' in str(cell_value):
                    found_right_lever = True
                    # Append the value to the new sheet
                    if ':' not in str(cell_value):
                        new_sheet.append([cell_value])

    # Print messages outside the loop based on the results
    if not found_left_lever:
        print("Left Lever press delimiter [ L: ] not found! Unable to parse file.")
    if not found_right_lever:
        print("Right Lever press delimiter [ R: ] not found! Unable to parse file.")

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
