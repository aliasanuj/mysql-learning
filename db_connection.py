import cx_oracle
conn = cx_oracle.connect('ABC')#connection part
cur=conn.cursor()
cur.execute("select * from abc")
for line in cur:
    print(line)
cur.close()
conn.close()

