#
# Financial Data Class
#
import pandas as pd
from pylab import plt
plt.style.use('seaborn-v0_8')

url = 'https://certificate.tpq.io/eoddata.csv'

class FinancialData:
    def __init__(self, url):
        self.url = url
        self.retrieve_data()
        self.prepare_data()
    def retrieve_data(self):
        self.raw = pd.read_csv(self.url, index_col=0, parse_dates=True)
    def prepare_data(self):
        self.prices = self.raw.dropna()
        self.returns = self.prices.pct_change()
    def plot_prices(self, cols=None):
        if cols is None:
            cols = self.prices.columns[0]
        self.prices[cols].plot(title=cols)

if __name__ == '__main__':
    url = 'https://certificate.tpq.io/eoddata.csv'
    fd = FinancialData(url)
    print(fd.returns.head())
