import os

path = "F://PII_WORD_STATISTICS/Categories in Text Files/"
category_files = ['finance.txt', 'work.txt', 'health.txt', 'biometric.txt', 'genetic.txt', 'bio-demographic.txt', 'race-ethinicity.txt', 'belief.txt', 'technology.txt', 'tracking_ID.txt', 'govt-personal-ID.txt', 'location.txt', 'contact.txt', 'misc.txt']

sum = 0

for i in range(len(category_files)):
    p1 = path+category_files[i]
    with open(p1,"r") as files:
        length = len(files.readlines())
        sum = sum + length
        print("sum of ",str(category_files[i]),"is",str(length))

print(sum)
