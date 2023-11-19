## README: Rat Data Converter 

Voluntary exercise: raw data to csv string converter for Dr. Brown's Neuroscience lab at WSU. 


---

## Table of Contents
- [README: Rat Data Converter](#readme-rat-data-converter)
- [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
  - [Usage Instructions](#usage-instructions)
  - [Capabilities (Development Log)](#capabilities-development-log)

<a name="revision-history"> </a>

### Document Revision History
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

This project is dependent on the openpyxl and panda libraries. 
If you have python installed, use  `pip install openpyxl pandas`  before running this program. 

<!-- warning that this only works for windows/linux -->
<!-- todo: add more detail / pictures. -->

1. Download RatSorty.py and ensure it is saved to your machine as a `.py` file. Save the file to your desktop. (Note: these instructions assume it's not in a folder.) 
2. In the Windows Command Prompt (or linux terminal), write `cd desktop`. 
3. Hit enter, then type `python RatSort.py`. 
4. Follow the prompts given to your terminal to ensure input and output file names will be correct. 


### Capabilities (Development Log) 
`2023-11-19`: Must be able to sort data from `MED-PC` which converts from delimited `.txt` to `.xlxs`. 
- all initial data (Subject, Experiment, Start Date, etc) will be discarded. 
- 'Box' indicator will not be discarded. In the event there are multiple boxes, their data will be sorted by ascending box number. 
- 'L' and 'R' data indicate left vs right lever presses.  
  
Initial prototype: Discard uneccessary data, identify box number and sort the data following the 'box' cell entry. 
