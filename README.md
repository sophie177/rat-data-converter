## README: Rat Data Converter 

Voluntary exercise: raw data to csv string converter for Dr. Brown's Neuroscience lab at WSU. Comissioned by Damien Lybrand.


---

## Table of Contents
- [README: Rat Data Converter](#readme-rat-data-converter)
- [Table of Contents](#table-of-contents)
  - [Usage Instructions](#usage-instructions)
  - [Capabilities (Development Log)](#capabilities-development-log)


<!--
| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
| Data Converter |2023-11-19 |Prototype | 0.0        |
|           |           |          |        |
|      |      |         |         |

Table of contents: 
Instructions for Lab Workers
Current / Future Capabilites
Development Notes / Resources used -->


### Usage Instructions 

NOTE: The step-by-step video instructions to set-up and use this program can be obtained from Damien. 

This project is dependent on the openpyxl and panda libraries. 
If you have python installed, use  `pip install openpyxl pandas`  before running this program. If you don't have python installed, you can install it or wait for the next update (likely Tuesday, Nov 21 2023) 

<!-- warning that this only works for windows/linux -->
<!-- todo: add more detail / pictures. -->

1. Convert your text file using MED-PC to `.xlxs` format using the 'delimited' option. 
2. Download RatSorty.py and ensure it is saved to your machine as a `.py` file. Save the file to your desktop. 
3. In the Windows Command Prompt (or linux terminal), write `cd desktop`. If you saved RatSorty to a folder, use `cd <folder name>`. 
4. Hit enter, then type `python RatSort.py`. 
5. Follow the prompts given to your terminal to ensure input and output file names will be correct. The sorted file will appear in the same location that you saved RatSorty to, but a path will also be given in the terminal. 
   


### Capabilities (Development Log) 
`2023-11-19`: Must be able to sort data from `MED-PC` which converts from delimited `.txt` to `.xlxs`. 

- all initial data (Subject, Experiment, Start Date, etc) will be discarded. 
- 'Box' indicator will not be discarded, and box number will be written to the new file of organized data.  
- 'L' and 'R' data indicate left vs right lever presses. Lever press data will be preserved and sorted into arrays with running totals and presses per minute. 
  
Initial prototype: Discard uneccessary data, identify box number and sort lever press data into 3-by-n arrays. The first array column will be the raw data, the second column is the running total, and the third is the running total divided by 60.  

Current limitations: only expecting one box. 
