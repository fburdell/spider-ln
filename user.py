import os 
import ast

class User: 
    def __init__(self): 
        user = ast.literal_eval(os.environ['CREDS_LN'])
        self.email = user['email']
        self.password = user['password']
