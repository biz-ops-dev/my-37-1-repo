from dataclasses import dataclass
import json
from datetime import date

today = date.today()


@dataclass
class PublicCompany():
    '''
    Access and perform operations/comparisons on downloaded json data
    for publicly traded companies

    init method used 
    '''

    ticker: str

    def __init__(self, ticker: str):
        self.ticker = ticker
        self.source_folder = f'/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/market data/public companies/json/{self.ticker}'
        
        self.secondbalancesheeet = self.SecondBalanceSheeet
        # Reports
        self.balance_sheet = (json.load(open(f'{self.source_folder}/{self.ticker}-BALANCE_SHEET-av.json')))
        self.income_statement = (json.load(open(f'{self.source_folder}/{self.ticker}-INCOME_STATEMENT-av.json')))
        self.cash_flow = (json.load(open(f'{self.source_folder}/{self.ticker}-CASH_FLOW-av.json')))
        self.earnings = (json.load(open(f'{self.source_folder}/{self.ticker}-EARNINGS-av.json')))

        # Administration

        ## define dates

        self.lastBSQreportDate = self.balance_sheet['quarterlyReports'][0]["fiscalDateEnding"]
        self.lastINSQreportDate = self.income_statement['quarterlyReports'][0]["fiscalDateEnding"]
        self.lastCFQreportDate = self.cash_flow['quarterlyReports'][0]["fiscalDateEnding"]
        #earnings reports not quarterl

        ## Test Date
        self.q_date_test = self.lastBSQreportDate == self.lastINSQreportDate == self.lastCFQreportDate


        # Ratios
        #self.DebtEquity = round(self.totalLiabilities / self.totalShareholderEquity, 2)

        @dataclass
        class SecondBalanceSheeet:
            def __init__(self):
                self.name = BalanceSheet

    def some_line_items(self):
        # Line Items
        self.totalLiabilities = int(self.balance_sheet['quarterlyReports'][0]['totalLiabilities'])
        self.totalShareholderEquity = int(self.balance_sheet['quarterlyReports'][0]['totalShareholderEquity'])

   
    @property
    def balance_sheet_magic(self, report='quarterlyReports', report_index=0) -> dict:
        """
        Returns balance sheet
        report options: quarterlyReports, annualReports
        """       
        report = self.balance_sheet[report][report_index]
        date_ending = report["fiscalDateEnding"]
        return report, date_ending
    

# Payroll Companies

WorkDay = PublicCompany('WDAY')
ADP = PublicCompany('ADP')
Paychex = PublicCompany('PAYX')
Paycom = PublicCompany('PAYC')
Ceridian = PublicCompany('CDAY')

print(f'{WorkDay.lastBSQreportDate}\t{WorkDay.lastCFQreportDate}\t{WorkDay.lastINSQreportDate}')
print(WorkDay.q_date_test)

#print('{:,}'.format(WorkDay.totalLiabilities))


'''
print('Debt to Equity Ratio')
print(f'{WorkDay.lastQreportDate}\t{WorkDay.DebtEquity}\tWorkDay')
print(f'{ADP.lastQreportDate}\t{ADP.DebtEquity}\tADP')
print(f'{Paychex.lastQreportDate}\t{Paychex.DebtEquity}\tPaychex')
print(f'{Paycom.lastQreportDate}\t{Paycom.DebtEquity}\tPaycom')
print(f'{Ceridian.lastQreportDate}\t{Ceridian.DebtEquity}\tCeridian')



'''
    


    
"""    

for key in earnings['annualEarnings'][0]:
    value = earnings['annualEarnings'][0][key]
    try:
        value = f'{int(value):,}'
    except ValueError:
        pass
    print(f"{key:25}:\t{value:>10}")
    """







#print(Paychex.balance_sheet_lineItems)
#print(Paychex.latest_balance_sheet_annual)
#print(Company.balance_sheet_magic['totalLiabilities'])
#print(Company.balance_sheet_magic['totalShareholderEquity'])
#ratio = (int(Company.balance_sheet_magic['totalLiabilities'])) / (int(Company.balance_sheet_magic['totalShareholderEquity']))
#print(round(ratio,2))

#print(wdayde)


'''
removed:
        for key in report:
            value = report[value]/1_000_000
            print(f"{key:25}:\t{value:>10}")

More removed:
    @property
    def income_statement_lineItems(self):
        accounts = list(self.income_statement['quarterlyReports'][0])
        return f'\nIncome Statement Accounts: \n{set(accounts)}'
    
    @property
    def earnings_statement(self):
        earnings = self.earnings
        return earnings
    
    @property
    def capital_structure(self):
        totalLiabilities = 5

    @property
    def balance_sheet_lineItems(self):
        accounts = list(self.balance_sheet['quarterlyReports'][0])
        return f'\nBalance Sheet Accounts: \n{set(accounts)}'
        '''

        #print(f'{self.ticker}: Balance Sheet: Ending {report["fiscalDateEnding"]}:')
        #print(report)
        #print(f'report type: {type(report)}')
