#!/usr/bin/python
import pandas as pd
import numpy
import pymysql;
from sqlalchemy import create_engine;

try:
# Open database connection
	connection = pymysql.connect(host="35.193.90.243",user="guest", db="products", password="03022018", charset="utf8", cursorclass=pymysql.cursors.DictCursor)
	engine = create_engine('mysql+pymysql://guest:03022018@35.193.90.243:3306/products', echo=False);
	dataset = pd.read_csv('products.csv',  names=['productID', 'price', 'length', 'width', 'height', 'weight']);
	dataset.to_sql(name='entries', con=engine, if_exists='append', index=False);

	#with connection.cursor() as cursor:
		#sql = """INSERT INTO entries (productID, price, length, width, height, weight) VALUES (111, 40, 10, 15, 10, 7)"""
		#cursor.execute(sql)
		#connection.commit()


	#with connection.cursor() as cursor:
		#sql = "SELECT length, price FROM entries WHERE productID=111"
		#cursor.execute(sql)
		#result = cursor.fetchone()
		#print(result)
except:
	raise

finally:
	connection.close()