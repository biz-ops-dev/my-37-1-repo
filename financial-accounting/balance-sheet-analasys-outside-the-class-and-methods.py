
WorkDay = PublicCompany('WDAY')
ADP = PublicCompany('ADP')

company_tickers = 'ADP WDAY CDAY'.split()
print(company_tickers)
print('\n')
for ticker in company_tickers:
    company = PublicCompany(ticker)
    
    print(f'Ticker: {company.ticker}')
    print(f'Report Date: {company.BalanceSheet.mostRecentReportDate}')
    print(f'Total Assets: {int(company.BalanceSheet.get_totalAssets()):,}')
    print(f'Total Liabilities: {int(company.BalanceSheet.get_totalLiabilities()):,}')
    print(f'Total Equity: {int(company.BalanceSheet.get_totalEquity()):,}')
    print(f'Debt to Equity Ratio: {(company.BalanceSheet.get_ratio_debt_equity())}')
    print('\n')

from tabulate import tabulate

# Create a list to store data for each company
company_data = []

for ticker in company_tickers:
    company = PublicCompany(ticker)
    
    # Store data for each company in a dictionary with labels
    data = {
        'Ticker': company.ticker,
        'Report Date': company.BalanceSheet.mostRecentReportDate,
        'Debt to Equity Ratio': company.BalanceSheet.get_ratio_debt_equity(),
        'Total Assets': int(company.BalanceSheet.get_totalAssets()),
        'Total Liabilities': int(company.BalanceSheet.get_totalLiabilities()),
        'Total Equity': int(company.BalanceSheet.get_totalEquity()),
    }
    
    company_data.append(data)

# Use tabulate to format and print the table with headers and labels
table = tabulate(company_data, headers="keys", tablefmt="pretty")

# Print the formatted table
print(table)



