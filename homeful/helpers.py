import csv
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()


def MultiFamilyCSVload():
    with open('data/MULTIFAMILY_PROPERTIES.csv') as csvfile:
        multi_family_db_data = []  
        multi_family_db_header = []
        header = True
        tablename='MF_dataTable'
        for row in csv.reader(csvfile):
            if header:
                header = False
                multi_family_db_header=row
                sql = "CREATE TABLE %s (%s)" % (tablename,
                          ", ".join([ "%s text" % column for column in row ]))
                cur.execute(sql)
                for column in row:
                    if (column=="MF_dataTable" or column=="STD_ZIP5"):
                        index = "%s__%s" % ( tablename, column )
                        sql = "CREATE INDEX %s on %s (%s)" % ( index, tablename, column )
                        cur.execute(sql)
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename,
                            ", ".join([ "?" for column in row ]))
                rowlen = len(row)
            else:
		multi_family_db_data.append(row)
                if len(row) == rowlen:
                    cur.execute(insertsql, row)
        conn.commit()

