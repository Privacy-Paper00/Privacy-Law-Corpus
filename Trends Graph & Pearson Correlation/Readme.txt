## Project Description

This code loads PII category terms from text files, analyzes text documents(laws) to count PII terms in various categories over time across documents, and creates visualizations to represent trends in PII data.
It also generates a matrix for the pearson correlation between the occurrence of the PII types in the corpus.

## Prerequisites

Ensure that you have the following packages installed:

- numpy
- pandas
- nltk
- matplotlib
- seaborn

## Instructions

1. Install the necessary packages using the following commands:
  pip install numpy
  pip install pandas
  pip install nltk
  pip install matplotlib
  pip install seaborn

2. Update the following variables in the code to point to the appropriate directories:
   'df'   : This should point to the directory containing the 'Data_for_graph.xlsx' file
   'path' : This should point to the directory containing the 14 text files (each file contains a list of terms related to a specific PII category).
   'p1'   : This should point to the directory containing the text documents (The documents in this folder are only in English, including documents written
originally in English and translations).

3. Run the code, and it will generate two images: one containing multiple graphs and the other displaying the Pearson correlation matrix.


 
