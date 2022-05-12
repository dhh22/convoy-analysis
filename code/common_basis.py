import sqlalchemy
import keyring
import getpass

pwd = None
try:
    pwd = keyring.get_password("dhh22-db", "convoy")
except keyring.errors.NoKeyringError:
    pass

if pwd is None:
    pwd = getpass.getpass("Database password: ")
    con = sqlalchemy.create_engine(
        "mariadb+pymysql://convoy:" + pwd + "@vm1788.kaj.pouta.csc.fi/convoy?charset=utf8mb4")
    con.execute("SELECT 1")
    try:
        keyring.set_password("dhh22-db", "convoy", pwd)
    except keyring.errors.NoKeyringError:
        pass

con = sqlalchemy.create_engine("mariadb+pymysql://convoy:" + pwd + "@vm1788.kaj.pouta.csc.fi/convoy?charset=utf8mb4")

del pwd
