import sqlalchemy
import keyring
import getpass

if keyring.get_password("dhh22-db", "convoy") is None:
    keyring.set_password("dhh22-db", "convoy", getpass.getpass())

con = sqlalchemy.create_engine("mariadb+pymysql://convoy:"+keyring.get_password("dhh22-db", "convoy")+"@vm1788.kaj.pouta.csc.fi/convoy?charset=utf8mb4")
