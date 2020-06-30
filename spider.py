import base_private as base

import pandas as pd

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from parsel import Selector

from unidecode import unidecode

def delAscii(text):
    return unidecode(str(text))

def getWorkHist(driver):

    try:
        work_history = driver.find_element_by_xpath('//*[@id="experience-section"]/ul').text
    except NoSuchElementException:
        work_history = ''
    if work_history:
        work_history = work_history.strip()
        work_history = delAscii(work_history)
    return work_history

def getEdu(driver):

    try:
        edu = driver.find_element_by_id('education-section').text
    except NoSuchElementException:
        edu = ""
    if edu:
        edu = edu.strip()
        edu = delAscii(edu)

    return edu

def crawl(fileName):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(base.urlLn)

    user = driver.find_element_by_id('username')
    user.send_keys(base.user)

    pwd = driver.find_element_by_id('password')
    pwd.send_keys(base.pwd)

    signIn = driver.find_element_by_xpath('//*[@type="submit"]')
    signIn.click()

    liWorkHist = []
    liEdu = []
    liUrl = []

    for _ in base.urls:
        for url in _:
            driver.get(url)

            sel = Selector(text=driver.page_source)

            workHist = getWorkHist(driver)
            edu = getEdu(driver)
    
            print(workHist, edu)

            liWorkHist.append(workHist)
            liEdu.append(edu)
            liUrl.append(url)

    dikt = {'work': liWorkHist,
        'edu': liEdu,
        'url': liUrl}

    df = pd.DataFrame(dikt)

    df.to_csv(rf'out\{fileName}.csv', index=False)

    return df

def parse_output(df): 
    """expects pandas dataframe""" 
    """optional build"""
    pass
    

crawl('analystInstitute - Analysts')


