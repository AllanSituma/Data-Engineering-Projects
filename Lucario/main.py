from etlchecker import CheckOperator
from dbcredentials import cred_dict,lucario_email
from emailsender import EmailSender


class EtlCheck(CheckOperator):
    def __init__(self,*args):
        super().__init__(*args)

    def run(self):
        message = self.generate_alert()
        details = lucario_email()
        build = {'sender_address':details['sender'],
                  'password':details['password'],
                  'receiver_address':details['receiver'],
                  'email_subject':message['subject'],
                  'mail_content':message['body']
                 }
        email = EmailSender(build)
        email.send_email()
        return print('Success,Email sent')


if __name__ == '__main__':
    check = EtlCheck(cred_dict())
    check.run()       
