import pandas as pd
import psycopg2
from queries import run_function,count_function,drop_table,create_audit_table,get_audit_table
from helpers import rename_column

class  AuditTableOperator:

	def __init__(self,user,db,host,password,port):
		self.user = user
		self.db = db
		self.host = host
		self.password = password

	def connectdb(self):
		conn = psycopg2.connect(user= self.user,
								password= self.password,
								host= self.host,
								database= self.db)
		cursor = conn.cursor()
		return cursor

	def create_audit_table(self,schema):
		curr = self.connectdb()
		query = create_audit_table(schema)
		curr.execute(query)
		curr.close()

	def create_audit_function(self,schema):
		curr = self.connectdb()
		query = count_function(schema)
		curr.execute(query)
		curr.close()


	def run_audit_function(self,schema):
		curr = self.connectdb()
		query = run_function(schema)
		curr.execute(query)
		curr.close()
	
	def create_audit_df(self,schema):
		curr = self.connectdb()
		query = get_audit_table(schema)
		curr.execute(query)
		df = pd.DataFrame(curr.fetchall())
		df.columns = ['table_name','row_counts']
		return df
		

	def drop_audit_table (self,schema):
		curr = self.connectdb()
		query = drop_table(schema)
		curr.execute(query)
		curr.close()
		return print('Audit table created and dropped...')