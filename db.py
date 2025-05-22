#!/usr/bin/env python3


import csv
from objects import full_build

import sqlite3
from contextlib import closing

from objects import full_build

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "build_history_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close()


def make_Build(row):
    return full_build(row["month"], row["metal"], row["jewelry"])
        


def get_Build():
    connect()
    query = '''SELECT month, metal,jewelry
                FROM Build'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        rows = c.fetchall()

        build_list = []
        for row in rows:
            Build = make_Build(row["month"], row["metal"], row["jewelry"])
            Build.add(full_build)
        return build_list
    

def save_build():
    sql - '''INSERT INTO full_build
                (month, metal, jewelry)
             VALUES
                 (?,?,?)'''
    for data in build_list:
        if data.id == 0:
            with closing(conn.cursor()):
                c.execute(sql, (data.month, data.metal, data.jewelry))
                conn.commit()
                

def already_imported(filename):
    try:
        query = '''SELECT fileName
                   FROM ImportedFiles
                   WHERE fileName = ?
                   '''
        with closing(conn.cursor()) as c:
            c.execute(query, (filename.name,))
            row = c.fetchone()

            if row:
                return True
            else:
                return False
    except sqlite3.OperationalError:
        return False

def add_imported_file(filename):
    sql = '''INSERT INTO ImportedFiles (fileName
             VALUES (?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (filename.name,))
        conn.commit()
              






    




