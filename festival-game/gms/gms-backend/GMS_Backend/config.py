db = {
    'user'     : '[user name]',
    'password' : '[password]',
    'host'     : '[host name]',
    'port'     : '[port name]',
    'database' : '[database name]'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"