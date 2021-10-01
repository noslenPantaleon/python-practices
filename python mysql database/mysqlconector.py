import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime

class MysqlConector:
	
	def __init__(self,host,usuario,password):
		self.host_local= host
		self.usuario = usuario
		self.password_de_msql= password
		self.Conectarse("database_name")
	def Conectarse(self,BaseDeDatos):
		try:
			self.connection = mysql.connector.connect(host= self.host_local ,user= self.usuario , passwd= self.password_de_msql, database= BaseDeDatos )
			self.cursor = self.connection.cursor()
			print (" conexión establecida")
		 
		except Exception as e:		
			print("Exeception occured:{}".format(e))	
		finally:		
			pass
	
	def UsarTabla(self,BaseDeDatos, Tabla, Seleccion):
		self.cursor.execute(f"SELECT {Seleccion} FROM {Tabla}")
		salida = self.cursor.fetchall()
		print (salida) 

