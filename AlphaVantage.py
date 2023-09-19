
import requests
import json
import os
import time
from datetime import date


alphaVantge_api_key='RFFQ1M9VBKOQF9KV'
folder = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/market data/public companies/1-json'


def get_company_report_options(symbols, report_options):
    """ 
    args:
    company is ticker
    report_options is the type of report_options you want to get from the api
    """

    counter = 1

    for symbol in symbols:
        for report in report_options:
            url = f'https://www.alphavantage.co/query?function={report}&symbol={symbol}&apikey={alphaVantge_api_key}'
            r = requests.get(url)
            company_data = r.json()
            print(f"Downloading {symbol}-{report} files.")

            if not os.path.exists(f'{folder}/{symbol}'):
                os.makedirs(f'{folder}/{symbol}')

            with open(f'{folder}/{symbol}/{date.today()}-{report}.json', 'w') as outfile:
                json.dump(company_data, outfile)

        print(f"{symbol} files downloaded.")
        if counter < len(symbols):
            next_symbol = symbols[counter]
            counter += 1
            print(f"In 60 seconds will continue with {next_symbol}")
            time.sleep(90)
        else:
            print("All files downloaded.")



def main():
    """Define main"""
    report_options = {
        'Overview': 'OVERVIEW',
        'Income statement': 'INCOME_STATEMENT',
        'Balance sheet': 'BALANCE_SHEET',
        'Cash flow statement': 'CASH_FLOW',
        'Earnings report': 'EARNINGS',
    }
    
    ticker = input("Enter ticker(s): ")
    ticker = [symbol.strip() for symbol in ticker.split(',') for symbol in symbol.split()]
    print('\n')
    for i in enumerate(report_options, start=1):
        print(*i)
    print("0 all")
    report_selection = input(f"What report_options would you like to download? ")
    report_selection = [int(choice.strip()) for choice in report_selection.split(',') for choice in choice.split()]
    print(report_selection)
    
    if report_selection == [0]:
        get_company_report_options(ticker, list(report_options.values()))
    else:
        selected_keys = [list(report_options.keys())[choice - 1] for choice in report_selection]
        get_company_report_options(ticker, selected_keys)

if __name__ == '__main__':
    main()

def get_realGDP():
    """ Get real GDP data from the alpha vantage api and write to a json file """
    url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey='+alphaVantge_api_key
    r = requests.get(url)
    realGDP_data = r.json()
    
    with open(f'/Users/alexandercarnevale/My_Applications/get_data/get_financial_report_options/realGDP.json', 'w') as outfile:
        outfile.write(str(realGDP_data))
    return(realGDP_data)


""" Changes to make to this include:
1. error checking
    api call
    file writing
2. Vlidation checking
    api call data is passedd
    data is written to file
    valid options selected

"""


# More report_options : https://www.alphavantage.co/documentation/
# not could have made all one function with a parameter for the report call type

import requests
import json
import os
import time
from datetime import date


alphaVantge_api_key='RFFQ1M9VBKOQF9KV'
folder = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/market data/public companies/1-json'


def get_company_report_options(symbols, report_options):
    """ 
    args:
    company is ticker
    report_options is the type of report_options you want to get from the api
    """

    counter = 1

    for symbol in symbols:
        for report in report_options:
            url = f'https://www.alphavantage.co/query?function={report}&symbol={symbol}&apikey={alphaVantge_api_key}'
            r = requests.get(url)
            company_data = r.json()
            print(f"Downloading {symbol}-{report} files.")

            if not os.path.exists(f'{folder}/{symbol}'):
                os.makedirs(f'{folder}/{symbol}')

            with open(f'{folder}/{symbol}/{date.today()}-{report}.json', 'w') as outfile:
                json.dump(company_data, outfile)

        print(f"{symbol} files downloaded.")
        if counter < len(symbols):
            next_symbol = symbols[counter]
            counter += 1
            print(f"In 60 seconds will continue with {next_symbol}")
            time.sleep(90)
        else:
            print("All files downloaded.")



def main():
    """Define main"""
    report_options = {
        'Overview': 'OVERVIEW',
        'Income statement': 'INCOME_STATEMENT',
        'Balance sheet': 'BALANCE_SHEET',
        'Cash flow statement': 'CASH_FLOW',
        'Earnings report': 'EARNINGS',
    }
    
    ticker = input("Enter ticker(s): ")
    ticker = [symbol.strip() for symbol in ticker.split(',') for symbol in symbol.split()]
    print('\n')
    for i in enumerate(report_options, start=1):
        print(*i)
    print("0 all")
    report_selection = input(f"What report_options would you like to download? ")
    report_selection = [int(choice.strip()) for choice in report_selection.split(',') for choice in choice.split()]
    print(report_selection)
    
    if report_selection == [0]:
        get_company_report_options(ticker, list(report_options.values()))
    else:
        selected_keys = [list(report_options.keys())[choice - 1] for choice in report_selection]
        get_company_report_options(ticker, selected_keys)

if __name__ == '__main__':
    main()

def get_realGDP():
    """ Get real GDP data from the alpha vantage api and write to a json file """
    url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey='+alphaVantge_api_key
    r = requests.get(url)
    realGDP_data = r.json()
    
    with open(f'/Users/alexandercarnevale/My_Applications/get_data/get_financial_report_options/realGDP.json', 'w') as outfile:
        outfile.write(str(realGDP_data))
    return(realGDP_data)


""" Changes to make to this include:
1. error checking
    api call
    file writing
2. Vlidation checking
    api call data is passedd
    data is written to file
    valid options selected

"""


# More report_options : https://www.alphavantage.co/documentation/
# not could have made all one function with a parameter for the report call type
