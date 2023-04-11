import sqlite3

con = sqlite3.connect("naverDB2")
cur = con.cursor()

cur.execute("create table userTable(id char(4), userName char(15), email char(15), birthYear int)")

cur.execute("insert into userTable values('lsy1','sang1','lsy1@naver.com', 1991)")
cur.execute("insert into userTable values('lsy2','sang2','lsy2@naver.com', 1992)")
cur.execute("insert into userTable values('lsy3','sang3','lsy3@naver.com', 1993)")
cur.execute("insert into userTable values('lsy4','sang4','lsy4@naver.com', 1994)")

con.commit()