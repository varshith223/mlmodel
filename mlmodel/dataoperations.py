import csv
with open('/content/names.csv', newline = '', encoding = 'utf-8-sig') as csv_file:
  dataset = list(csv.reader(csv_file, ))

# Remove the header row
dataset = dataset[1:]
# Create a copy for sorting
dataset_sorted = dataset.copy()
'''
Sort the copied dataset with names, i.e., with the column Name which is at
index 0 in every row
'''
dataset_sorted.sort(key = lambda row : row[0])

# The name that appears last in the alphabet
print('The name that appears last in the alphabet:', dataset_sorted[-1][0])

# The name that appears first in the alphabet
print('The name that appears first in the alphabet:', dataset_sorted[0][0])

# The names at certain indexes
print('At 40:', dataset[40][0])
print('At 400:', dataset[400][0])
print('At 9274:', dataset[9274][0])
print('At 12279:', dataset[12279][0])
print('At 15239:', dataset[15239][0])