import cx_Oracle
# Replace with your Oracle Database credentials
dsn_tns = cx_Oracle.makedsn("invvmpr01", "1521", service_name="XEPDB1")
conn = cx_Oracle.connect(user="INFA_REPO", password="password1234", dsn=dsn_tns)
print(conn)
cu_for_fetch=conn.cursor()
cu_for_fetch.execute("select * from BW_POS")
for i in cu_for_fetch.fetchall():
    print(i)