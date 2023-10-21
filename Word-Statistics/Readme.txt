## Project Description

This code is designed to collect and organize word count data for native English text files and English translated text files.
It also provides summary statistics regarding the word counts in these files. 
The results are saved in Excel files and a text file for further analysis and reporting.

## Prerequisites

Ensure that you have the following packages installed:
- openpyxl

## Instructions

1. Install the necessary packages using the following commands:
   pip install openpyxl

2. Update the following variables in the code to point to the appropriate directories:
   'p1'   : This should point to the directory containing the Native English text documents
   'p2'   : This should point to the directory containing the Translated English text documents

3. Run the code, and it will generate two Excel files, "Word-count-native-english.xlsx" and "Word-count-translated.xlsx," which will contain word count data for the respective files.
   Additionally, the code will calculate total word count, minimum and maximum word counts, median, and mean values and save them in a text file named "stats.txt."

  
