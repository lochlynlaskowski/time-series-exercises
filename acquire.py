import requests
import numpy as np
import pandas as pd
import os


def get_all(endpoint):
    """ Read all records on all pages """
    
    if endpoint not in ["sales", "items", "stores"]:
        return "Not available from this API. Check the documentation"
    
    host = "https://python.zgulde.net/"
    api = "api/v1/"

    url = host + api + endpoint

    response = requests.get(url)

    if response.ok:
        payload = response.json()["payload"]

        # endpoint should be "items", "sales", or "stores"
        contents = payload[endpoint]

        # Make a dataframe of the contents
        df = pd.DataFrame(contents)

        next_page = payload["next_page"]

        while next_page:
            # Append the next_page url piece
            url = host + next_page
            response = requests.get(url)

            payload = response.json()["payload"]

            next_page = payload["next_page"] 
            
            print(f'\rGetting page {payload["page"]} of {payload["max_page"]}: {url}', end='')      
            
            contents = payload[endpoint]

            df = pd.concat([df, pd.DataFrame(contents)])

            df = df.reset_index(drop=True)
            
            return df



def merge_data():
    'Takes acquired api data from get_all() and merges the dataframes and saves to csv'
    sales = get_all('sales')
    stores = get_all('stores')
    items = get_all('items')
    sales_stores = pd.merge(sales,stores, how= 'inner', left_on='store' ,right_on='store_id')
    total = pd.merge(sales_stores,items,how= 'inner', left_on='item' ,right_on='item_id')
    #save it as a csv
    total.to_csv("total_sales_data.csv",index=False)
    return df


def get_new_opsd_data():
    '''Gets OPSD from csv and saves as a csv'''
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv("opsd.csv",index=False)
    return df


