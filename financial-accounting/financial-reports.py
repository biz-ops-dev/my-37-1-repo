from dataclasses import dataclass
import json

@dataclass
class PublicCompany():
    """
    Base dataclass to hold information about publicly traded companies
    """

    ticker: str
    source_folder: str = f'/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/market data/public companies/json/'
    
    def __post_init__(self):
        self.AnnualReports = {
            'balanceSheet' : (json.load(open(self.source_folder + self.ticker + '-BALANCE_SHEET-av.json'))['annualReports']),
            'incomeStatement' : (json.load(open(self.source_folder + self.ticker + '-INCOME_STATEMENT-av.json'))['annualReports']),
            }
        self.QuarterlyReports = {
            'balanceSheet' : (json.load(open(self.source_folder + self.ticker + '-BALANCE_SHEET-av.json'))['quarterlyReports']),
            'incomeStatement' : (json.load(open(self.source_folder + self.ticker + '-INCOME_STATEMENT-av.json'))['quarterlyReports']),
            }

    def get_10K_item(self, item:str, report:str, period:int = 0) -> int:
        """Obtain and print a line item from annual report

        Args:
            item (str): line item to obtain
            report (str): financial report from which to obtain it
            period (int, optional): report index. Defaults to 0, most recent.

        Returns:
            int: line item value
        """
        item_value = int(self.AnnualReports[report][period][item])
        report_date = self.AnnualReports[report][period]["fiscalDateEnding"]
        print(f'{report_date}\t10-K\t{report}\t{item}\t{item_value:,}')
        return item_value
        



adp = PublicCompany('adp')
#print(type(adp.AnnualReports['balanceSheet']))
#print((adp.AnnualReports['balanceSheet'][0]))
print(adp.QuarterlyReports['incomeStatement'][0])