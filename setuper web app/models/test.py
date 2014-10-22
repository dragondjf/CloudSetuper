from mongokit import Connection, Document
from basedocment import BaseDocment
import datetime
connection = Connection()

@connection.register
class User(BaseDocment):

    __collection__ = 'userCol'
    __database__ = 'setuperDB'

    structure = {
        'username': unicode,
        'email': unicode,
        'password': unicode,
        'date_creation': datetime.datetime,
    }
    required_fields = ['username', 'email', 'password']
    default_values = {
        'date_creation': datetime.datetime.utcnow
    }

user = connection.User()
objId = user.loadFromDict({
                'username': 'username',
                'email': 'email',
                'password': 'password'
            })

print objId