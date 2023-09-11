Requirement:
Create Spreadsheet with arithmentic operations +,-,/,*,(,)
setCellValue(String cellId, Object value)
getCellValue(String cellId)

Output:
Dictionary with the RowName its corresponding Value
Run script locally
python3 spreadsheet.py

Approach#1 
split the string based on expression and compute
Failed for Test cases- A1*A2-A3 Expected 19, got -5

Approach#2
Build binary tree based on infix operator
Failed for Test case - (A1+A2)*A3

Futute prospects
- Handling Float/decimal (With seprator .)
- Handling '^','{', '}'
- Table format for spreadsheet using dictoinary
- unittest for each test cases