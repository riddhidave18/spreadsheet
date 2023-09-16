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