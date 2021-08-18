import os

class Config: 

    def __init__(self): 
        import argparse
        from datetime import datetime

        parser = argparse.ArgumentParser()
        parser.add_argument('-k', 
                type=str, 
                help="keywords to get links for")

        parser.add_argument('-n',
                type=int,
                help="number profiles to find")

        parser.add_argument('-g',
                type=str, 
                choices=['head', 'hless'],
                help="run webrowser driver with/out head")

        self.args = parser.parse_args()

        self.file_output_path =  "out/" + "-".join( self.args.k.split(" ") ) + ".csv"
        os.makedirs( "out/", exist_ok=True )

