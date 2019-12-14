from configparser import ConfigParser

c=ConfigParser()
c["Settings"]={
    "debug":'true',
    "secret _key" : '123',
    " log_path":"fileLocation"
}
c["DB"]={
    "Db_type":"RDBMS",
    "db_port":8888,
    "db_name":"mysql"
}
f=open("configFile.ini","w")

c.write(f)
f.close()

