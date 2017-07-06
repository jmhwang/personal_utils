# -*-coding:cp949-*-
# vim: set et:ts=4:sw=4
"""
FOR WINDOWS

exe 만들기
==========
    pyinstall --onefile mssql_export.py
    * 이때 한글경로가 있으면 안됨
    
사용법
======
    mssql_export.exe db_name..tablename
    * db_name..tablename.csv 파일로 결과 저장
"""


def export_table(table):
    import pyodbc
    import unicodecsv as csv

    cnxn = pyodbc.connect(
        r'DRIVER={SQL Server};'
        r'SERVER=127.0.0.1\instance;'
        r'DATABASE=master;'
        r'UID=id;'
        r'PWD=passwd')

    cursor = cnxn.cursor()

    script = u"select * from %s" % (table.decode('cp949'))

    cursor.execute(script)

    count = 0
    with open("%s.csv" % (table,), "wb") as outfile:
        writer = csv.writer(outfile, quotechar="'", quoting=csv.QUOTE_NONNUMERIC, encoding='cp949')
        
        columns =  [i[0] for i in cursor.description]
        writer.writerow(columns)
        
        with open("%s_structure.txt" % (table,), "ab") as stfile:
            stfile.write('\n-------------------------------\n')
            stfile.write('%s\n' % (script.encode('cp949')))
            stfile.write('%s\n' % (cursor.description,))
            
        while True:
            data = cursor.fetchmany(1000)
            count += len(data)
            if len(data) == 0 :
                break
                
            for row in data:
                writer.writerow(row)
    cursor.close()
    cnxn.close()
    
    print '%d 건 완료' %(count,)
    pass
    

import sys
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

if len(sys.argv) < 2 :
    print u'테이블명을 입력하세요'.encode('cp949')
    print u'사용법 :\n\texport.exe db_name..tablename'.encode('cp949')
    sys.exit(0)

tbl = sys.argv[1]
export_table(tbl)
