from alpha_vantage.timeseries import TimeSeries
from .models import Stock, StockData
from django.utils import timezone

def fetch_stock_data(symbol, start_date):
    try:
        api_key = 'KSNJ717L394SWAOM'
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

        # Check if data is fetched correctly
        if data is None or data.empty:
            raise ValueError(f"No data fetched from Alpha Vantage for the given symbol and date range: {symbol}")

        # Assume the company name is the symbol itself as Alpha Vantage does not provide company overview
        company_name = symbol
    except Exception as e:
        print(f"Error fetching data for symbol {symbol}: {str(e)}")
        raise

    return data, company_name

def save_stock_data(symbol, data, company_name):
    try:
        stock, created = Stock.objects.get_or_create(symbol=symbol, defaults={'name': company_name})
        # print(f"Stock: {stock}, Created: {created}")
        
        for date, row in data.iterrows():
            StockData.objects.update_or_create(
                stock=stock,
                date=date,
                defaults={
                    'open': row['1. open'],
                    'high': row['2. high'],
                    'low': row['3. low'],
                    'close': row['4. close'],
                    'volume': row['5. volume'],
                }
            )
    except Exception as e:
        print(f"Error saving data for symbol {symbol} on date {date}: {str(e)}")
        raise