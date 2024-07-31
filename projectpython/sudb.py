# import mysql.connector
# #
# # #
# dbconfig = {
#     'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'ich_edit'
# }
# user = input('Введите название таблицы: ')
# try:
# connection = mysql.connector.connect(**dbconfig)
# cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM {user}")
#     result = cursor.fetchall()
#     print(result)
#     cursor.close()
#     connection.close()
# except mysql.connector.errors.ProgrammingError:
#     print(f'Таблицы {user}, не существует, повторите попытку')
#
# connection = mysql.connector.connect(**dbconfig)
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM users')
# result = cursor.fetchall()
# for i in result:
#     print(i)
# into = input('Введите имя человека что бы просмотреть его заказы: ')
# cursor.execute('SELECT Alena FROM users')
# cursor.close()
# connection.close()
#


