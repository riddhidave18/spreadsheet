import pytest
from spreadsheet import Spreadsheet


def test_infixtopostfix():
    sheet1 = Spreadsheet()
    assert sheet1.infixToPostfix(['5', '*', '6']) == ['5', '6', '*']

def test_infixtopostfix1():
    sheet1 = Spreadsheet()
    assert sheet1.infixToPostfix(['5', '/', '6', '*', '1', '+', '11']) == ['5', '6', '/', '1', '11', '+', '*']


def test_getCellValue():
    sheet1 = Spreadsheet()
    sheet1.setCellValue("A2",'2')
    assert sheet1.getCellValue("A2") == 2


def test_getCellValue1():
    sheet1 = Spreadsheet()
    sheet1.setCellValue("A1",'2')
    sheet1.setCellValue("A2",'2')
    sheet1.setCellValue("A3",'A1+A2')
    assert sheet1.getCellValue("A3") == 4

def test_setCellValue2():
    sheet1 = Spreadsheet()
    sheet1.setCellValue("A1",'5')
    sheet1.setCellValue("A2",'6')
    sheet1.setCellValue("B2",'1')
    sheet1.setCellValue("A3",'A1+A2')
    sheet1.setCellValue("A7",'((A1/A2)*B2)+A3')
    assert int(sheet1.getCellValue("A7")) == 10


