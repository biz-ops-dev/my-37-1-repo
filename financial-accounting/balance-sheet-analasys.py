from dataclasses import dataclass
import json
from datetime import date

class PublicCompany():
    
    source_folder_base = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/market data/public companies/json/'

    def __init__(self, ticker: str):
        self.ticker = ticker
        self.BalanceSheet = self.BalanceSheet(self)
        self.IncomeStatement = self.IncomeStatement(self)
        self.KeyRatios = self.KeyRatios(self)
     
    class BalanceSheet:

        def __init__(self, parent):
            self.parent = parent
            self.source_folder = f'{PublicCompany.source_folder_base}/{self.parent.ticker}'
            self.report = (json.load(open(f'{self.source_folder}/{self.parent.ticker}-BALANCE_SHEET-av.json')))
            self.annualReports = self.report['annualReports']
            self.quarterlyReports = self.report['quarterlyReports']
            self.mostRecentReportDate = self.report['quarterlyReports'][0]['fiscalDateEnding']
            
        def generate_report(self, report, report_index = 0):
            "NEXT: Make method of class not BalanceSheet"
            if report == 'quarterly':
                return self.quarterlyReports[report_index]
            if report == 'annual':
                return self.annualReports[report_index]
            else:
                return "Please chose 'annual' or 'quarterly' as report options."
           
        def get_line_item(self, line_item, report, report_index):
            if report == 'quarterly':
                if line_item in self.quarterlyReports[report_index]:
                    return self.quarterlyReports[report_index][line_item]
                else:
                    return f'{line_item} is not included in this quarterly report.'
            if report == 'annual':
                if line_item in self.annualReports[report_index]:
                    return self.annualReports[report_index][line_item]
                else:
                    return f'{line_item} is not included in this annual report.'
            else:
                return "Please chose 'annual' or 'quarterly' as report options."
          
        def get_totalAssets(self, report='quarterly', report_index=0):
            return self.get_line_item('totalAssets', report, report_index)

        def get_totalLiabilities(self, report='quarterly', report_index=0):
            return self.get_line_item('totalLiabilities', report, report_index)

        def get_totalEquity(self, report='quarterly', report_index=0):
            return self.get_line_item('totalShareholderEquity', report, report_index)   

    class IncomeStatement:

        def __init__(self, parent):
            self.parent = parent
            self.source_folder = f'{PublicCompany.source_folder_base}/{self.parent.ticker}'
            self.report = (json.load(open(f'{self.source_folder}/{self.parent.ticker}-INCOME_STATEMENT-av.json')))
            self.annualReports = self.report['annualReports']
            self.quarterlyReports = self.report['quarterlyReports']
            self.mostRecentReportDate = self.report['quarterlyReports'][0]['fiscalDateEnding']

        def generate_report(self, report, report_index = 0):
            "NEXT: Make method of class not BalanceSheet"
            if report == 'quarterly':
                return self.quarterlyReports[report_index]
            if report == 'annual':
                return self.annualReports[report_index]
            else:
                return "Please chose 'annual' or 'quarterly' as report options."
            
        def get_line_item(self, line_item, report, report_index):
            "NEXT: Make method of class not report"
            if report == 'quarterly':
                if line_item in self.quarterlyReports[report_index]:
                    return self.quarterlyReports[report_index][line_item]
                else:
                    return f'{line_item} is not included in this quarterly report.'
            if report == 'annual':
                if line_item in self.annualReports[report_index]:
                    return self.annualReports[report_index][line_item]
                else:
                    return f'{line_item} is not included in this annual report.'
            else:
                return "Please chose 'annual' or 'quarterly' as report options."
            
        def get_ebit(self, report='quarterly', report_index=0):
            return self.get_line_item('ebit', report, report_index)
        def get_interest_expense(self, report='quarterly', report_index=0):
            return self.get_line_item('ebit', report, report_index)
            
    class KeyRatios:
        def __init__(self, parent):
            self.parent = parent
            self.income_statement = parent.IncomeStatement
            self.balance_sheet = parent.BalanceSheet
            
        def get_asset_turnover(self, report='quarterly', report_index=0):

            if report == 'quarterly':
                revenue = self.income_statement.quarterlyReports[report_index]['totalRevenue']
                avg_asset = (
                    (int(self.balance_sheet.quarterlyReports[report_index]['totalAssets']) 
                    +
                    int(self.balance_sheet.quarterlyReports[report_index-1]['totalAssets']))
                    /
                    2)

            elif report == 'annual':
                revenue = self.income_statement.annualReports[report_index]['totalRevenue']
                avg_asset = (
                    (int(self.balance_sheet.annualReports[report_index]['totalAssets']) 
                    +
                    int(self.balance_sheet.annualReports[report_index-1]['totalAssets']))
                    /
                    2)
            else:
                raise ValueError("Invalid report type")

        # Calculate asset turnover
            asset_turnover = round(int(revenue) / int(avg_asset),2)
            return asset_turnover

        def get_debt_equity(self, report='quarterly', report_index=0):
            '''
            high => more risk
            low ==> not taking advantage of debt financing to grow
            '''

            if report == 'quarterly':
                debt=self.balance_sheet.quarterlyReports[report_index]['totalLiabilities']
                equity = self.balance_sheet.quarterlyReports[report_index]['totalShareholderEquity']
            if report == 'annual':
                debt=self.balance_sheet.annualReports[report_index]['totalLiabilities']
                equity = self.balance_sheet.annualReports[report_index]['totalShareholderEquity']

            debt = int(debt)
            equity = int(equity)
            return round(debt / equity,2)
        
        def get_interest_coverage(self, report='quarterly', report_index=0):
            "sticking to annual reports only for now"
            total_liabilities = int(self.balance_sheet.annualReports[report_index]['totalLiabilities'])
            interest_expense = int(self.income_statement.annualReports[report_index]['interestExpense'])
            percent_interest = interest_expense / total_liabilities
            total_interest_payable = total_liabilities * percent_interest
            EBIT =  int(self.income_statement.annualReports[report_index]['ebit'])
            TIE_ratio = EBIT / total_interest_payable
            return TIE_ratio


"""
workday = PublicCompany('WDAY')
print(f'Ticker: {workday.ticker}')
print(f'Total Assets: {int(workday.BalanceSheet.get_totalAssets()):,}')
print(f'Asset Turnover Ratio: {workday.KeyRatios.get_asset_turnover()}')
print(f'Debt to equity: {workday.KeyRatios.get_debt_equity()}')

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
    print(f'Debt to Equity Ratio: {(company.KeyRatios.get_debt_equity())}')
    print(f'Asset Turnover Ratio: {(company.KeyRatios.get_asset_turnover())}')

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
        'Debt to Equity Ratio': company.KeyRatios.get_debt_equity(),
        'Asset Turnover Ratio' : company.KeyRatios.get_asset_turnover(),
        'Total Assets': int(company.BalanceSheet.get_totalAssets()),
        'Total Liabilities': int(company.BalanceSheet.get_totalLiabilities()),
        'Total Equity': int(company.BalanceSheet.get_totalEquity()),
    }
    
    company_data.append(data)

# Use tabulate to format and print the table with headers and labels
table = tabulate(company_data, headers="keys", tablefmt="pretty")

# Print the formatted table
print(table)
"""

ADP = PublicCompany('ADP')
ADP_BS = ADP.BalanceSheet.generate_report('quarterly')
ADP_IS = ADP.IncomeStatement.generate_report('quarterly')
#for key, value in ADP_BS.items():
#    print(key)

#for key, value in ADP_BS.items():
#    print(key)

print(ADP.KeyRatios.get_interest_coverage())