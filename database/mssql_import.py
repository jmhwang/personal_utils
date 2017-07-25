# -*-coding:cp949-*-
# vim: set et:ts=4:sw=4
import pyodbc

def import_table(file, table):
    connection = pyodbc.connect(
        r'DRIVER={SQL Server};'
        r'SERVER=127.0.0.1\instance;'
        r'DATABASE=database;'
        r'UID=id;'
        r'PWD=passwd')

    with open (file, 'r') as f:
        lines = f.readlines()
        cursor = connection.cursor()
        for line in lines[1:]: # 1st line skip
            line = line.replace('\n', '')
            query = 'insert into ' + table + ' values ({0})'.decode('cp949')
            query = query.format(line.decode('cp949'))
            #print(query)
            cursor.execute(query)
        cursor.commit()
    
    print "%d 건 완료" % (len(lines)-1,)

import sys
import os.path

if len(sys.argv) < 2 :
    print u'파일명을 입력하세요'.encode('cp949')
    print u'파일명에 적힌 테이블로 데이터를 입력합니다'.encode('cp949')
    print u'사용법 :\n\timport.exe  db_name..tablename.csv'.encode('cp949')
    sys.exit(0)

file = sys.argv[1]
tbl = os.path.splitext(os.path.basename(file))[0]
# print file # ".\db_name..tablename.csv"
# print tbl # "db_name..tablename"
import_table(file, tbl.decode('cp949'))
