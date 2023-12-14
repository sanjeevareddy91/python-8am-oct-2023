# # First we have to download the library..

# # mysql - pymysql
# # postgres - psycopg2
# # oracle - oracle_cx
# # monogdb - pymongo
# # sqlite - sqlite

# # pip install pymysql

# import pymysql

# # conn_data = pymysql.connect(user='root',password='password') # This is connecting to the direct mysql server..

# conn_data = pymysql.connect(user='root',password='password',database='python_8am_dec') # This is connecting to the particular database in the server..
# cur_data = conn_data.cursor()

# # print(cur_data.execute('show databases'))

# # print(cur_data.fetchall())

# # cur_data.execute('create database python_8am_dec')
# # print(cur_data)
# # print(conn_data)


# # cur_data.execute("create table player_info(p_name varchar(20),p_franchasis varchar(4),p_role varchar(10))")

# # cur_data.execute("insert into player_info(p_name,p_franchasis,p_role) values('Dhoni','CSK','Batsmen')")

# # cur_data.execute("insert into player_info(p_name,p_franchasis,p_role) values('Kohli','RCB','Batsmen'),('Bumrah','MI','Bowler'),('Rohit','MI','Batsmen'),('Jadeja','CSK','Allrounder'),('Maxwell','RCB','Allrounder')")

# # print(cur_data.execute("select * from player_info"))

# # print(cur_data.fetchall())

# # cur_data.execute("select * from player_info where p_role='Batsmen'")


# # cur_data.execute("update player_info SET p_role='Batsmen' where p_name='Maxwell'")
# # print(cur_data.fetchall())

# # cur_data.execute("alter table player_info add p_price integer")

# # cur_data.execute("delete from player_info where p_name='Dhoni'")

# # cur_data.execute("truncate player_info")

# # cur_data.execute("drop table player_info")

# cur_data.execute("drop database python_8am_dec")


# conn_data.commit() # This will commit your changes to the DB.

