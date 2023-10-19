import os
import re
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import re

## Storing the name of the Directory to traverse and identify files##
p1 = "F://PII_WORD_STATISTICS/CODE/combined_files/"
path = "F://PII_WORD_STATISTICS/Categories in Text Files/"

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
#print(dir_list_1)
#print(len1)

result = np.zeros((14,max_value), dtype= int)

## Converting the caetgory names into dictionary ## This will be used for storing the count values

category = ['finance', 'work', 'health', 'biometric', 'genetic', 'bio-demographic', 'race-ethinicity', 'belief', 'technology', 'tracking-ID', 'govt-personal-ID', 'location', 'contact', 'misc']
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

for i in range(0, len1):
    path_1 = p1 + dir_list_1[i]
    # print(path_1)
    file_cont = None
    with open(path_1, "r", encoding="utf-8", errors="ignore") as file:
        data = file.read()
        data = data.lower()
        file_cont = preprocess_text(data)

    for j in range(0, 14):
        for k in range(max_value):
            count = 0
            word = keywords1[j][k]
            if word is not None and word in file_cont:
                count += 1
                result[j][k] += 1  # Increment result[j][k] since a match is found
                break  # Exit the inner loop once a match is found

            if count >= 1:
                break  # Exit the outer loop since a match is found

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Calculate the category sums and create a dictionary
category_dict = {}
for i, category_name in enumerate(category):
    sum = 0
    for j in range(max_value):
        sum = result[i][j] + sum
    category_dict[category_name] = sum

# Sort the categories and corresponding values in descending order
sorted_data = sorted(category_dict.items(), key=lambda x: x[1], reverse=True)
sorted_categories, sorted_values = zip(*sorted_data)

# Calculate the total number of documents
total = len1

# Calculate the final percentage values
final_graph_list = [(value / total) * 100 for value in sorted_values]

# Set the figure background color
fig, ax = plt.subplots(figsize=(8, 7))
fig.set_facecolor('white')  # Set background color to white

# Plot the bar chart
bars = ax.bar(
    x=sorted_categories,
    height=final_graph_list,
    width=0.5,
    align='center',
    color='deepskyblue'  # Change the bar color to light blue
)

ax.set_xticks(range(len(sorted_categories)))  # Set the x-axis tick positions
ax.set_xlabel('Categories of PII', fontsize=18)  # Adjust the fontsize for x-axis label
ax.set_ylabel('Percentage of Documents', fontsize=18)  # Adjust the fontsize for y-axis label
ax.set_xticklabels(
    labels=sorted_categories,
    rotation=70,
    ha='right',
    fontsize=20  # Adjust the fontsize for x-axis tick labels
)
ax.yaxis.set_major_locator(ticker.FixedLocator(ax.get_yticks()))  # Set the y-axis tick positions

# Set the fontsize for y-axis tick labels
ax.tick_params(axis='y', labelsize=20)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# Remove the grid
ax.grid(False)

# Find the index and value of each bar
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f'{int(height)}',
        ha='center',
        va='bottom',
        color='black',
        fontsize=18.7
    )

# Add a title with adjusted fontsize
ax.set_title('Percentage of Documents Containing Different PII Data', fontsize=20, y=1.05)  # Adjust the fontsize for the title

# Format the y-axis tick labels as integers
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x)}"))

plt.tight_layout()

# Save the image
plt.savefig('Percentage of Documents Containing Different PII Data.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
