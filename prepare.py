import pandas as pd

def prepare_sales_data(df):
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df = df.set_index('sale_date')
    df['month'] = df.index.strftime('%m-%b')
    df['day'] = df.index.strftime('%w-%a')
    df['sales_total'] = df.sale_amount * df.item_price
    return df


def prepare_opsd_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df['month'] = df.index.strftime('%m-%b')
    df['year'] = df.index.year
    df = df.fillna(0)
    return df