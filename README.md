Requirement:
Create Spreadsheet with arithmentic operations +,-,/,*,(,)
setCellValue(String cellId, Object value)
getCellValue(String cellId)

Output:
Dictionary with the RowName its corresponding Value

Run script locally
``` 
Install python3 https://www.python.org/downloads/

python3 spreadsheet.py
```

Run unit tests using docker container
```
docker build -t python-spreadsheet . 
docker run python-spreadsheet
```

Approach
Build binary tree based on infix operator


Futute prospects
- Handling Float/decimal (With seprator .)
- Handling '^','{', '}'