import re
import operator
class Spreadsheet:
    def __init__(self):
        self.operators = {'/':operator.truediv,'*':operator.mul,'+':operator.add,'-':operator.sub}
        self.spreadsheet_dict = {}

    def process_cellValue(self,cellValue):
        value=0
        for operator in self.operators.keys():
            if operator in cellValue:
                # print(re.findall('\w',cellValue))
                m = re.search(r'(\w+)' +re.escape(operator)+ r'(\w+)',cellValue)
                print("groups",m.groups())
                firstArgument = m.groups()[0]
                secondArgument = m.groups()[1]
                if firstArgument in self.spreadsheet_dict.keys() and secondArgument in self.spreadsheet_dict:
                    value = self.operators[operator](int(self.getCellValue(firstArgument)),int(self.getCellValue(secondArgument)))
                    print(value)
        return value


    def setCellValue(self,cellName,cellValue):
        """
        Updates spreadsheet_dict with new value if cellValue is int 
        else sends cellValue for process
        """
        if cellValue.isnumeric():
            print("riddhi")
            self.spreadsheet_dict[cellName]=cellValue
            print("true")
        else:
            value = self.process_cellValue(cellValue)
            self.spreadsheet_dict[cellName]=value

        print(self.spreadsheet_dict)
        return True


    def getCellValue(self,cellName):
        print(cellName)
        # print(self.spreadsheet_dict)
        return( self.spreadsheet_dict.get(cellName))

if __name__ == '__main__':
    sheet1 = Spreadsheet()
    sheet1.setCellValue("A1",'5')
    sheet1.setCellValue("A2",'6')
    sheet1.setCellValue("A3",'A1+A2')
    sheet1.setCellValue("A4",'A1*A2')
    sheet1.setCellValue("A5",'A1*A2-A3')
    # print(sheet1.getCellValue("A1"))


