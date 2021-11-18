import psycopg2
import configparser

dbconfig = configparser.ConfigParser()
dbconfig.read("dbconfig.ini")

if "db" not in dbconfig:
	print("error ! config file not fount !")
	# return # for function or class


connection = psycopg2.connect(
host=dbconfig['db']['host'],
database=dbconfig['db']['database'],
user=dbconfig['db']['user'],
password=dbconfig['db']['password'])

connection.set_session(autocommit=True)


# with connection.cursor() as cursor:
#     cursor.execute('SELECT COUNT(*) FROM mytest12')
#     result = cursor.fetchone()
# print(result)





def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                mytest12
            WHERE
                username = '%s'
        """ % username)
        result = cursor.fetchone()

    if result is None:
        # User does not exist
        return False

    admin, = result
    return admin

print(is_admin("haki"))
print(is_admin("';\n select true; --"))  # sql injection 
