from googlesearch import search 
import pandas as pd

user = 'fburdelliv@gmail.com'
pwd = 'frankeb4'
urlLn = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
num_queries = 25

df = pd.read_csv('queries.csv')

def get_urls(queries):

    urls = []

    for q in queries:

        qurls = search(query=q, tld='co.in', lang='en', stop=num_queries)

        urls.append(qurls)
        
    return urls


def get_query(df):
    import numpy as np

    df.replace(np.nan, " ", inplace=True)

    df['q'] = df['site'] + " " + df['company'] + " " + df['term'] + " " + df['edu'] + df['location']

    qs = [x for x in df['q']]

    return qs

queries = get_query(df)
urls = get_urls(queries)
