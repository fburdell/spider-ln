from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup as BS

from unidecode import unidecode

from google import Google

from multiprocessing import Pool

import pandas as pd

class Spider(Google): 

    def __init__(self): 
        Google.__init__(self)
        self.ln_login = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        self.chrome_options = Options()
        if self.args.g == 'hless': # if run with head 
            self.chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome('./chromedriver', 
                options=self.chrome_options)

        self.login()

        self.page_sources = self.get_sources()

        self.parsed_sources = pd.DataFrame.from_records( self.parse_sources(self.page_sources) )
        
        self.parsed_sources.to_csv( self.file_output_path )


    def login(self): 
        self.driver.get(self.ln_login)
        self.driver.find_element_by_id('username').send_keys(self.email)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@type="submit"]').click()

    def get_sources(self): 
        # for url
        #     go url
        #     get data
        #     store data
        #     close
        page_sources = []
        for u in self.urls: 
            self.driver.get(u)
            page_sources.append((u,self.driver.page_source))

        return page_sources

    def parse_sources(self, sources): 
    
        parsed_sources = []
        for u, source in sources: 
            soup = BS(source, features='lxml')
            
            parsed_sources.append( [u, self.get_edu(soup), self.get_exp(soup)] )
    
        return parsed_sources

    def get_edu(self, source): 
        edu = source.find("section", {"id" : "education-section"} )
        try: 
            edu = edu.text
        except AttributeError: 
            edu = ''
        return edu
        

    def get_exp(self, source): 
        exp = source.find("section", {"id" : "experience-section"} )
        try: 
            exp = exp.text
        except AttributeError: 
            exp = ''
        return exp






if __name__ == '__main__': 
    S = Spider()
    



