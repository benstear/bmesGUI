#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:23:21 2018

@author: dawnstear
"""


import numpy as np
import pandas as pd
#path = '/Users/dawnstear/desktop/scGUI/fake_data.csv'

class utilities(object):
    
    def __init__(self):
        pass
    
    def load(self, path):
        #pd.read_csv(path)
        return pd.read_excel(path)
    
    # function provided by ahmet
    def myselect(self,sql):
        cur.execute(sql);
        rows=cur.fetchall();
        if len(rows)==0:
            print('No results returned for SQL query.');
        else:
            df = DataFrame(rows)
            df.columns = [x[0] for x in cur.description]
            display(df)
    
    def create_db(self,data,dbname='database',tbname='table'):
        import sqlite3
        conn = sqlite3.connect(dbname);
        cur = conn.cursor();
        conn.execute("DROP TABLE IF EXISTS"+ tbname)
        # Get columnsnames if its a df
        if type(data) == pd.core.frame.DataFrame:
            dbcols = data.columns
        #for i in range(len(dbcols)):
        conn.execute("""CREATE TABLE IF NOT EXISTS""" +tbname+ """ (
                miRNA VARCHAR(30),
                gene_name VARCHAR(30), 
                score FLOAT); """);
        conn.commit();
        return conn, cur
        
    
    
u = utilities
l = u.load('/Users/dawnstear/desktop/scGUI/fake_data.csv')
c,cc = u.create_db(l,'mydatabase','mytable')


