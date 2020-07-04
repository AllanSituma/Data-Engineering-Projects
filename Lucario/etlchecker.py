import numpy as np
import pandas as pd
from helpers import rename_column,EmailTextCreator
from dbcredentials import DbCredentials
from audittablecreator import AuditTableOperator


class ComparisonDf:

	def __init__(self,production_table,analytics_table):
		self.production = production_table
		self.analytics = analytics_table

	def createdf(self):
		df1 = self.production
		df2 = self.analytics
		df_compare = pd.merge(df1,df2, how='outer',on='table_name')
		df_compare.columns=['table_name','x_rows','y_rows']
		df_compare['RowMatch'] = np.where(df_compare['x_rows'] < df_compare['y_rows'],'MISSING ROWS','UPDATED')
		df_compare['Missing Rows'] = df_compare['x_rows'].sub(df_compare['y_rows'],axis = 0) 
		return df_compare


class GenerateDf(AuditTableOperator):
	
	def __init__(self,user,db,host,password,port,schema):
		super().__init__(user,db,host,password,port)
		self.schema = schema
		
	def return_df(self):
		self.create_audit_table(self.schema)
		self.create_audit_function(self.schema)
		self.run_audit_function(self.schema)
		df = self.create_audit_df(self.schema)
		return df

	def drop_table(self):
		self.drop_audit_table(self.schema)

	

class CheckOperator(DbCredentials):
	def __init__(self,*args):
		super().__init__(*args)


	def compare_df(self):
		df1 = GenerateDf(self.prod_user,
						self.prod_db,
						self.prod_host,
						self.prod_pass,
						self.prod_port,
						self.prod_schema)
		df2 = GenerateDf(self.analytics_user,
						self.analytics_db,
						self.analytics_host,
						self.analytics_pass,
						self.analytics_port,
						self.analytics_schema)
		production = df1.return_df()
		df1.drop_table()
		analytics = df2.return_df()
		df2.drop_table()
		result = ComparisonDf(production,analytics)
		df = result.createdf()
		return df

	def generate_alert(self):
		compare_df = self.compare_df()
		html_df = compare_df.to_html()

		if len(compare_df[compare_df['RowMatch']=='MISSING ROWS'])==0:
			draft = EmailTextCreator('Lucario: SUCCESS ANALYTICS DB UP TO DATE',
										'Nothing to worry about :)',
										html_df)
			email = draft.email_generator()

		else:
			draft = EmailTextCreator('Lucario: WARNING ANALYTICS DB NOT UP TO DATE',
										'Check the tables with missing rows',
										html_df)
			email = draft.email_generator()
		return email 



