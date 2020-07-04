import os

class DbCredentials:

    def __init__(self,params):
        self.prod_db = params.get('db_production')
        self.analytics_db = params.get('db_analytics')
        self.prod_user = params.get('prod_user')
        self.analytics_user = params.get('analytics_user')
        self.prod_pass = params.get('prod_pass')
        self.analytics_pass = params.get('analytics_pass')
        self.prod_host = params.get('prod_host')
        self.analytics_host = params.get('analytics_host')
        self.prod_schema = params.get('prod_schema')
        self.analytics_schema = params.get('analytics_schema')
        self.prod_port = params.get('prod_port')
        self.analytics_port = params.get('analytics_port')


def cred_dict():
    credentials = { "db_production": os.environ.get('PROD_POSTGRES_DATABASE') ,
                "db_analytics": os.environ.get('STG_POSTGRES_DATABASE'),
                "prod_user": os.environ.get('PROD_POSTGRES_USER'),
                "analytics_user": os.environ.get('STG_POSTGRES_USER'),
                "prod_pass": os.environ.get('PROD_POSTGRES_PASSWORD'),
                "analytics_pass": os.environ.get('STG_POSTGRES_PASSWORD'),
                "prod_host": os.environ.get('PROD_POSTGRES_HOST'),
                "analytics_host": os.environ.get('STG_POSTGRES_HOST'),
                "prod_schema": os.environ.get('PROD_POSTGRES_SCHEMA'),
                "analytics_schema": os.environ.get('STG_POSTGRES_SCHEMA'),
                "prod_port": os.environ.get('PROD_POSTGRES_PORT'),
                "analytics_port": os.environ.get('STG_POSTGRES_PORT')
                }
    return credentials


def lucario_email():
    logins = {'sender':os.environ.get('LUCARIO_EMAIL'),
                'receiver':os.environ.get('RECEIVER_EMAIL'),
                'password':os.environ.get('LUCARIO_PASS')
            }
    return logins