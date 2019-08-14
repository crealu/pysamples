import xlrd
workbook = xlrd.open_workbook('Sources.xlsx')       # open sources
sheet = workbook.sheet_by_name('Sheet1')            # specify sheet

companyNames = []         # company names array
cell = 1                  # row 2
numRows = sheet.nrows     # gets number of rows

# loop through column 5 (suppliers) and append each value to companyNames list
while (cell < numRows):
    companyNames.append(sheet.cell(cell, 5).value)
    cell += 1

# remove duplicates with list(set(listName))
filteredNames = list(set(companyNames))

# alphabetically sort names
finalList = sorted(filteredNames)

# get column title
colTitle = sheet.cell(0, 5).value

import pprint
pp = pprint.PrettyPrinter(indent=4)

# print company names
pp.pprint(finalList)
lenFL = len(finalList)
pp.pprint(lenFL)
import xlwt
newWorkbook = xlwt.Workbook()
newSheet = newWorkbook.add_sheet('companies')
newSheet.write(0, 0, colTitle)
c = 1
while (c < len(finalList)):
    newSheet.write(c, 0, finalList[c])
    c += 1
newWorkbook.save('test.xls')
