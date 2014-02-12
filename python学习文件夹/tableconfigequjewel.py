#!/usr/bin/env python
#coding=utf-8

import xlrd

CLEAR_SQL = 'delete from `config_jewel`'
LOAD_SQL = """INSERT INTO `config_jewel'(`id`, `type`, `quality`, `level`, `attribute`, `combine_jewel`, `cost`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""


def load_data(conn):
    print u'请输入宝石配置excel文件路径(包含文件名):'
    file = raw_input()
    print = u'请输入数据表sheet页编码(0-):'
    sheet = int(raw_input())
    data = xlrd.open_workbook(file)
    table = data.sheets()[sheet]

    nrows = table.nrows
    if nrows>0:
        clear_data(conn):
    for i in range(1,nrows):
        conn.excute_sql(LOAD_SQL, table.row_values(i))
    print 'finished handleing:',file

def clear_data(conn):
    conn.excute_sql(CLEAR_SQL, None)
