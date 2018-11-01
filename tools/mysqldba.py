import pymysql.cursors
import configparser

# Connect to the database
conn = None

def open(host,port,user,pwd,db):
    global conn
    conn = pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=pwd,
                           db=db,
                           # charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
def opencf(cf):
    cf.read("../application.conf", encoding='utf-8')

    host = cf.get("tmysql", "host")
    port = cf.getint("tmysql", "port")
    user = cf.get("tmysql", "user")
    pwd = cf.get("tmysql", "pwd")
    open(host, port, user, pwd, 'sys')

def execute(sql):
    assert  conn is not None
    cursor = conn.cursor()
    cursor.execute(sql)

def fetch_one(sql):
    assert  conn is not None
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchone()

def fetch_all(sql,*args):
    assert conn is not None
    cursor = conn.cursor()
    cursor.execute(sql,args)
    return cursor.fetchall()

if __name__ == "__main__":
    cf = configparser.ConfigParser()
    cf.read("../application.conf", encoding='utf-8')

    opencf(cf)

    # t = fetch_one('select * from user')
    # print(t)
    print(fetch_dict("select * from user"))