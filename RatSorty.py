'''
rat data converter for the Neuro Lab at WSU (commissioned by Damien Lybrand) 
- goal: convert file of delimited data to a sorted and readable version 
- current version: prototype
- current capabilities: sort data for one rat 
- future tasks: input checking, error handling for incomplete files, sort several rats' data for multiple days. 

'''

import openpyxl
import pandas as pd

# initial practice sorting with panda, initial structure of sorting program 

def sort_excel_data(input_file, output_file):
    # Load the Excel file
    workbook = openpyxl.load_workbook(input_file)
    
    # Assume the first sheet in the workbook
    sheet = workbook.active

    found_box = False 
    box_num = 0 # box numbering starts at one, so setting this to zero serves as an error flag. 

    # Extract all values from the sheet
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.extend(row)

    # Iterate through each cell in the original sheet
    for row in sheet.iter_rows(values_only=True):
        for cell_value in row:
            # If 'box' is found, set the flag to True
            if cell_value is not None and 'Box:' in str(cell_value):
                found_box = True
                box_num += 1 # if box is found, increment box num. 

            # If 'box' has been found, append the value to the new sheet
            if found_box:
                new_sheet.append([cell_value])

    # Save the new workbook to the output file
    new_workbook.save(output_file)

    # Create a DataFrame and sort the data
    df = pd.DataFrame(data, columns=['Data'])
    df_sorted = df.sort_values(by='Data')

    # Create a new workbook and sheet
    new_workbook = openpyxl.Workbook()
    new_sheet = new_workbook.active

    # Write the sorted data to the new sheet in a single column
    for value in df_sorted['Data']:
        new_sheet.append([value])

    # Save the new workbook to the output file
    new_workbook.save(output_file)

if __name__ == "__main__":
    # Provide the input and output file paths
    print(" Hello, Welcome to RatSort! ")
    print(" RatSort will require an input file path and return the path of the updated file.")
    
    input_file_path = input('paste or type input file path here: ')

    
    #input_file_path = "input_data.xlsx"  # Change this to your input file
    output_file_path = "sorted_data.xlsx"  # Change this to your desired output file

    # Call the function to sort the data
    sort_excel_data(input_file_path, output_file_path)

    print(f"Data has been sorted and saved to {output_file_path}")
