## Project Description

This code is designed to read and process text documents(laws) to identify and count Personally Identifiable Information (PII) terms within various categories. 
It also visualizes the distribution of PII categories across the documents using a bar chart. 
This chart provides insights into the most prevalent categories of PII data in the analyzed documents.

## Prerequisites

Ensure that you have the following packages installed:

- numpy
- nltk
- matplotlib

## Instructions

1. Install the necessary packages using the following commands:
   pip install numpy
   pip install nltk
   pip install matplotlib

2. Update the following variables in the code to point to the appropriate directories:
   'path': This should point to the directory containing the 14 text files (each file contains a list of terms related to a specific PII category).
   'p1'  : This should point to the directory containing the text documents (The documents in this folder are only in English, including documents written originally in English and translations).

3. Run the code, and it will generate the desired output.

Note: The functionality of the code relies on the correct setup of file paths and directories. Make sure to adjust these paths to match your specific file locations and directory structures.
