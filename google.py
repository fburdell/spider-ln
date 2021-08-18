from googlesearch import search 

from config import Config
from user import User

class Google(User, Config):

    def __init__(self): 
        User.__init__(self)
        Config.__init__(self)

        self.query = self.args.k + " site:linkedin.com/in"

        self.urls = search(self.query, 
                lang="en", 
                num_results=self.args.n)



if __name__ == "__main__": 
    G = Google()

