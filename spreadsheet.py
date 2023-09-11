import re
import math
import logging

class Node:
    def __init__(self,key):
        """ init Node tree class """
        self.left = None
        self.right = None
        self.val = key

    def isOperator(self,c):
        """checks the function """
        if ( c=='+' or c == '-' or c == '*' or c == '/'):
            return True
        else:
            return False

    def constructTree(self,postfixCellValue):
        """Input: list of postfix expression
            Output: Tree """
        stack = []
        try:
            for char in postfixCellValue:
                t = Node(char)
                if self.isOperator(char):  
                    t1 = stack.pop()
                    t2 = stack.pop()
                    t.right = t1
                    t.left = t2    
                stack.append(t)
            t = stack.pop()
            return t
        except Exception as e:
            print(e)
            raise

    def computeCells(self,root):
        """recursive call to calculate tree"""

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return int(root.val)  
        left_sum =self.computeCells(root.left)
        right_sum = self.computeCells(root.right)
        
        if root.val == '+':
            return left_sum + right_sum

        if root.val == '-':
            return left_sum - right_sum

        if root.val == '*':
            return left_sum * right_sum

        if root.val == '/':
            return left_sum / right_sum
        
        
class Spreadsheet:
    def __init__(self):
        """Initialize main spreadsheet class """
        self.spreadsheet_dict = {}
        self.newOperator = set(['+', '-', '*', '/', '(', ')'])  # collection of Operators
        self.priority = {'+':3, '-':3, '*':2, '/':2,'(':1, ')':1} # dictionary having priorities of Operators
    
    def infixToPostfix(self,infixList):
        """Convert Infix list to PostFix List""" 

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
            self.spreadsheet_dict[cellName]=cellValue
        else:
            value = self.process_cellValue(cellValue)
            self.spreadsheet_dict[cellName]=value
        print(self.spreadsheet_dict)
        return True


    def getCellValue(self,cellName):
        """Get cell Value from dict"""
        return( self.spreadsheet_dict.get(cellName))

if __name__ == '__main__':
    sheet1 = Spreadsheet()
    sheet1.setCellValue("A1",'5') 
    sheet1.setCellValue("A2",'6')
    sheet1.setCellValue("B2",'1')
    print(sheet1.getCellValue("B2") ) #1
    sheet1.setCellValue("A7",'A1*(A2+0)') #{'A1': '5', 'A2': '6', 'B2': '1', 'A7': 30}
    sheet1.setCellValue( "A8",'A1*(A2+B2)') # {'A1': '5', 'A2': '6', 'B2': '1', 'A7': 30, 'A8': 35}
    # sheet1.setCellValue("A3",'A1+A9') #raise Exception 
    # sheet1.setCellValue("A4",'A1*(A2+5.0)') #raise Exception
    sheet1.setCellValue("A5",'(A1/A2)')



