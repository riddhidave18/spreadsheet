class Spreadsheet:
    def __init__(self):
        self.spreadsheet_dict = {}

    def process_cellValue(self,cellValue):
        for value in cellValue:
            print("value",value)

    def setCellValue(self,cellName,cellValue):
        """
        Updates spreadsheet_dict with new value if cellValue is int 
        else sends cellValue for process
        """
        # self.spreadsheet_dict[cellName]=cellValue
        if cellValue.isnumeric():
            print("riddhi")
            self.spreadsheet_dict[cellName]=cellValue
            print("true")
        else:
            self.process_cellValue(cellValue)
        print(self.spreadsheet_dict)
        return True


    def getCellValue(self,cellName):
        print(cellName)
        # print(self.spreadsheet_dict)
        return( self.spreadsheet_dict.get(cellName))

if __name__ == '__main__':
    sheet1 = Spreadsheet()
    sheet1.setCellValue("A1",'h+')
    # print(sheet1.getCellValue("A1"))


