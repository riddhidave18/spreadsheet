import re
import math
import logging
# import spreadsheetUtility as utility
from spreadsheetUtility import Node

class Spreadsheet:
    def __init__(self):
        """Initialize main spreadsheet class """
        self.spreadsheet_dict = {}
        self.newOperator = set(['+', '-', '*', '/', '(', ')'])  # collection of Operators
        self.priority = {'+':3, '-':3, '*':2, '/':2,'(':1, ')':1} # dictionary having priorities of Operators
    
    def infixToPostfix(self,infixList):
        """Convert Infix list to PostFix List""" 
        print(infixList)
        stack = []
        postfixList = [] 
        for character in infixList:
            if character not in self.newOperator:  # if an operand append in postfix expression
                postfixList.append(character)
            elif character=='(':  # else Operators push onto stack
                stack.append('(')
            elif character==')':
                while stack and stack[-1]!= '(':
                    postfixList.append(stack.pop())
                stack.pop()
            else: 
                while stack and stack[-1]!='(' and self.priority[character]<=self.priority[stack[-1]]:
                    postfixList.append(stack.pop())
                stack.append(character)
        while stack:
            postfixList.append(stack.pop())
        print(postfixList)
        return postfixList

    def process_cellValue(self,cellValue):
        infix = []
        cells = re.split(r'([-+/*()^])',cellValue)
        try:
            for cell in cells:
                if cell in self.spreadsheet_dict.keys():
                    infix.append(str(self.getCellValue(cell)))
                elif cell.isdigit():
                    infix.append(int(cell))
                elif cell == '+' or cell == '-' or cell == '/' or cell == '*':
                    infix.append(cell)

            n = Node(self) # Initialize Node class
            cellTree = n.constructTree(self.infixToPostfix(infix))
            return n.computeCells(cellTree)
        except Exception as e:
            print("Poblem computing. Please check imput")
            raise

        except IndexError as err:
            print("Please check imput")
            raise



    def setCellValue(self,cellName,cellValue):
        """
        Updates spreadsheet_dict with new value if cellValue is int 
        else sends cellValue for process 
        Updates value in spreadsheetdict
        """
        if cellValue.isnumeric():
            self.spreadsheet_dict[cellName]=int(cellValue)
        else:
            value = self.process_cellValue(cellValue)
            self.spreadsheet_dict[cellName]=int(value)
        print(self.spreadsheet_dict)
        return True


    def getCellValue(self,cellName):
        """Get cell Value from dict"""
        if cellName in self.spreadsheet_dict:
            return( int(self.spreadsheet_dict.get(cellName)))
        else:
            print(self.spreadsheet_dict)
            print("Value does not exits. Please enter data first")
            exit(0)

if __name__ == '__main__':
    sheet1 = Spreadsheet()
    run_flag=True
    while run_flag:
        print("Enter 1 or 2:", "\n","1: for set value to row","\n","2: for get value from row","\n","ctrl+c to exit")
        action = input()
        if action == '1':
            rowName = input("Enter Row Name(E.g. A1/B1/C2):")
            rowValue = input("Enter Row Value:(E.g. 5/7/ A1+A2)")
            sheet1.setCellValue(rowName, rowValue)
        elif action == '2':
            rowName = input("Enter Row Name:")
            print(sheet1.getCellValue(rowName))
        else:
            print("Error: Please select 1 or 2")
            run_flag=False



    # sheet1.setCellValue("A1",'5') 
    # sheet1.setCellValue("A2",'6')
    # sheet1.setCellValue("B2",'1')
    # sheet1.setCellValue("A3",'A1+A2')
    # print(sheet1.getCellValue("B2") ) #1
    # sheet1.setCellValue("A7",'A1*(A2+0)') #{'A1': '5', 'A2': '6', 'B2': '1', 'A7': 30}
    # sheet1.setCellValue( "A8",'A1*(A2+B2)') # {'A1': '5', 'A2': '6', 'B2': '1', 'A7': 30, 'A8': 35}
    # sheet1.setCellValue("A3",'A1+A9') #raise Exception 
    # sheet1.setCellValue("A4",'A1*(A2+5.0)') #raise Exception
    # sheet1.setCellValue("A5",'((A1/A2)*B2)+A3')



