#
# Markowitz Portfolio Class
#
import math
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from data import FinancialData


class Portfolio(FinancialData):
    def __init__(self, url, assets, rf=0.0):
        super().__init__(url)
        self.assets = assets
        self.rf = rf
        self.noa = len(assets)
        self.weights = np.array(self.noa * [1 / self.noa])
        self.ereturns = self.returns[self.assets].mean() * 252
    def portfolio_return(self, weights=None):
        if weights is None:
            weights = self.weights
        return np.dot(weights, self.ereturns)
    def portfolio_variance(self, weights=None):
        if weights is None:
            weights = self.weights
        return weights @ self.returns[self.assets].cov() * 252 @ weights
    def portfolio_volatility(self, weights=None):
        if weights is None:
            weights = self.weights
        return math.sqrt(self.portfolio_variance(weights))
    def sharpe_ratio(self, weights=None):
        if weights is None:
            weights = self.weights
        sharpe = ((self.portfolio_return(weights) - self.rf) /
                  self.portfolio_volatility(weights))
        return sharpe
    def minimum_variance(self):
        bnds = self.noa * [(0, 1)]
        cons = {'type': 'eq', 'fun': lambda weights: weights.sum() - 1}
        opt = minimize(self.portfolio_volatility, self.weights,
                       bounds=bnds, constraints=cons)
        return opt
    def maximum_sharpe(self):
        bnds = self.noa * [(0, 1)]
        cons = {'type': 'eq', 'fun': lambda weights: weights.sum() - 1}
        opt = minimize(lambda x: -self.sharpe_ratio(x), self.weights,
                       bounds=bnds, constraints=cons)
        return opt

