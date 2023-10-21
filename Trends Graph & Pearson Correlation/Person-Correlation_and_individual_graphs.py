import os
import re
import numpy as np
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import re

## Storing the name of the Directory to traverse and identify files##
p1 = "PII_WORD_STATISTICS/CODE/combined_files/"

path = "PII_WORD_STATISTICS/Categories in Text Files/"

# File names of 14 categroies of terms 
category_files = ['finance.txt', 'work.txt', 'health.txt', 'biometric.txt', 'genetic.txt', 'bio-demographic.txt', 'race-ethinicity.txt', 'belief.txt', 'technology.txt', 'tracking_ID.txt', 'govt-personal-ID.txt', 'location.txt', 'contact.txt', 'misc.txt']

### There are 14 categories of PII data, and each category of terms is in a text file (14 .txt files in total)

### Appending .txt filename to the path 
category_files_1 = []
for i in category_files:
    category_files_1.append(str(path)+str(i))


multi_list = [[]]  ## Empty multidimensional list 


### opening each text file and storing the terms in a temporary list. Appending this list to the multi_list to create a Multi-dimensional list
for i in category_files_1:
    with open(i,"r") as file:
        lines = [" "+line.rstrip()+" " for line in file] 
    # print(lines)
    #print(len(lines))
    multi_list.append(lines)
    #print("######End of file######\n\n\n")
multi_list.pop(0)   ## Popping out the 1st sub-list of the multi_list as it is an empty list


#### Getting the count of the category with the maximum number of words
max_value = 0
for i in multi_list:
    temp = len(i)
    if temp > max_value:
        max_value = temp

#### Adding None Keyword to make all the sub-lists in multi_list equal in size
## Getting length of each sublist and finding difference between max_value and the length. Then the the "None" keyword is added until the difference

for i in range(14):
    length = len(multi_list[i])
    difference = max_value - length
    for j in range(difference):
        multi_list[i].append(None)

## Converting multi_list into an np array
keywords1 = np.array(multi_list)

## Getting names of all files present in the directories ##
dir_list_1=os.listdir(p1)
len1 = len(dir_list_1) 
result = np.zeros((14,max_value), dtype= int)

## Converting the caetgory names into dictionary ## This will be used for storing the count values

category = ['finance', 'work', 'health', 'biometric', 'genetic', 'bio-demographic', 'race-ethinicity', 'belief', 'technology', 'tracking_ID', 'govt-personal-ID', 'location', 'contact', 'misc']
category_dict = dict()
for i in category:
    category_dict[str(i)] = 0
print(category_dict)


lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower()) # lowercase and tokenize
    tokens = [token for token in tokens if re.match(r'^[a-zA-Z]+$', token)] #and token not in stop_words] # remove stopwords and non-alphabetic characters
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # lemmatize words
    a = " ".join(tokens)
    return a

# Create file-year mapping
df = pd.read_excel("PII_WORD_STATISTICS/Category_based_graph/Data_for_graph.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Key Law Corpus Identifier']) 
list2 = list(df['First Privacy Law'])


p1 = "PII_WORD_STATISTICS/CODE/combined_files/"

file_year_map = {}

for file,year in zip(list1,list2):
    if isinstance(year,int):
        file_year_map[file] = year

#print(file_year_map)


pii_data = {'finance': [], 'work': [], 'health': [], 'biometric': [], 'genetic': [], 'bio-demographic': [], 'race-ethinicity': [], 'belief': [], 'technology': [], 'tracking_ID': [], 'govt-personal-ID': [], 'location': [], 'contact': [], 'misc': []}
year_category_map = {}

### Native & Translated English Documents
for i in range(0,len1):
    path_1 = p1 + dir_list_1[i]
    #print(path_1)
    file_cont = None
    if list1[i] not in file_year_map:
        continue
    file_year = file_year_map[list1[i]]
    with open(path_1, "r",encoding="utf-8",errors="ignore") as file:
        data = file.read()
        data = data.lower()
        file_cont = preprocess_text(data)

    for j, cat_name in enumerate(category):
        temp_sum = 0
        for k in range(max_value):
            count = 0   
            word = keywords1[j][k]
            if word != None and word in file_cont:
                count = count + 1
            if count >= 1:
                result[j][k] = result[j][k] + 1
                temp_sum+=1
        
        pii_data[cat_name].append(temp_sum)
        if file_year not in year_category_map:
            year_category_map[file_year] = {}
        
        if cat_name not in year_category_map[file_year]:
                year_category_map[file_year][cat_name] = 0
        
        if temp_sum > 0:
            year_category_map[file_year][cat_name] += 1
        
print(year_category_map)

##### Graph Generation Code (5 per row)
#####################

import matplotlib.pyplot as plt
import numpy as np

data = year_category_map

# Get unique categories
categories = set(category for year_data in data.values() for category in year_data.keys())

# Calculate the number of rows and columns for the subplots
num_plots = len(categories)
num_cols = 5
num_rows = (num_plots + num_cols - 1) // num_cols  # Round up to the nearest integer

# Increase the width of each graph
fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, 6*num_rows), squeeze=False)
plt.subplots_adjust(hspace=0.52, wspace=0.23)  # Adjust hspace and wspace for spacing

# Define colors for the graphs
colors = plt.cm.rainbow(np.linspace(0, 1, num_plots))

# Define the years you want to display on the X-axis
years_to_display = [1960, 1990, 2020]  # Updated list

# Plot each category
for i, category in enumerate(categories):
    row = i // num_cols
    col = i % num_cols

    x = list(data.keys())
    y = [year_data.get(category, 0) for year_data in data.values()]

    # Compute cumulative sum for evenly increasing line graph
    y_cumulative = [sum(y[:i+1]) + i for i in range(len(y))]

    # Find the index corresponding to the years
    start_indices = [x.index(year) for year in years_to_display]

    ax = axes[row, col]
    ax.fill_between(x[start_indices[0]:], y_cumulative[start_indices[0]:], alpha=0.5, color=colors[i])
    ax.set_xlabel('Year', fontsize=25)
    ax.set_title(category, pad=20, fontsize=25)

    # Set custom tick positions and labels for the X-axis
    ax.set_xticks(years_to_display)  # Update the X-axis ticks
    ax.set_xticklabels([str(year) for year in years_to_display], fontsize=25)  # Adjust fontsize for X-axis labels

    # Increase font size of tick labels
    ax.tick_params(axis='both', which='major', labelsize=25)
    ax.tick_params(axis='both', which='minor', labelsize=25)

    # Only show Y-axis labels on the first graph in each row
    if col == 0:
        ax.set_ylabel('No. of Documents', fontsize=25, labelpad=-11)
        ax.set_ylim([0, 1000])
        ax.yaxis.set_major_locator(plt.MultipleLocator(200))  # Set Y-axis labels with an interval of 200
    else:
        ax.set_yticklabels([])  # Remove Y-axis labels for other graphs in the same row

# Remove unused subplots if necessary
for i in range(num_plots, num_rows * num_cols):
    row = i // num_cols
    col = i % num_cols
    fig.delaxes(axes[row, col])

# Add a title to the graph
fig.suptitle('Trend for individual categories of terms across documents over a period of time', fontsize=25, y=0.95)

# Save the image in high quality
plt.savefig('Multi_Graph.png', dpi=300)

# Display the plot
plt.show()



##### Pearson Correlation Matrix
#####################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame(pii_data)

cor_mat = df.corr()

mask = np.triu(np.ones_like(cor_mat, dtype=bool))

fig, ax = plt.subplots(figsize=(10, 8))  # Adjust the figure size as per your preference

sns.heatmap(cor_mat, cmap='YlOrRd', mask=mask, ax=ax)

plt.title('Pairwise Correlation', fontsize=19)  # Increase the font size of the title
plt.xticks(rotation=80, fontsize=19)  # Increase the font size of the x-axis tick labels
plt.yticks(rotation=0, fontsize=19)  # Increase the font size of the y-axis tick labels

plt.tight_layout()

# Save the image in high quality
plt.savefig('correlation_matrix.png', dpi=300)

plt.show()

