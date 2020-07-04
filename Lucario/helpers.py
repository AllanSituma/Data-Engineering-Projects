import re 

def rename_column(column_name):
    new_name = column_name.replace('public_','')
    return new_name

def sub_columns(df):
    return df[1] - df[2]


class EmailTextCreator:
    def __init__(self,alert,header,html_df):
        self.email_subject = alert
        self.email_body = html_df
        self.header = header
    
    
    def html_body(self):
        html = """
                <html>
                <head></head>
                <body>
                    <p>{}<br>
                    List of tables<br>
                    {}
                    </p>
                </body>
                </html>
                """.format(self.header,self.email_body)
        return html
        
    def email_generator(self):
        email_body = self.html_body()
        email = {'subject':self.email_subject,
                'body':email_body}
        return email

