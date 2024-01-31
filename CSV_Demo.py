import csv

with open('utilities/loan_data.csv') as csvReaderFile:
    csv_reader = csv.reader(csvReaderFile, delimiter=',')
    names_list = []
    status_list = []
    #print(list(csv_reader))
   # next(csv_reader) to get the first row-headers
    for row in csv_reader:
        names_list.append(row[0])
        status_list.append(row[1])
    print(names_list)
    print(status_list)
    #to get the status of Hanuman
    assert status_list[names_list.index('Hanuman')] == 'Approved'
#csv_reader is the reader, can be convereted to list - list(csv_reader)

#Writing/Appending data to the csv file, newline=''(to avoid adding extra blank line)
with open('utilities/loan_data.csv','a',newline='') as csvWriterFile:
    csv_writer = csv.writer(csvWriterFile)
    #writerow method takes input as list
    csv_writer.writerow(["Bharath","Pending"])



