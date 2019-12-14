from configparser import ConfigParser, ExtendedInterpolation

c=ConfigParser(interpolation=ExtendedInterpolation)
c.read("configFile.ini")
print(c.sections())
print(c.get("settings","secret_key"))
print(c.getint("DB","db_default_port",fallback=3309))
print(c.getboolean("settings","debug"))