import json
import numpy_financial as npf
import urllib.parse
from http.server import BaseHTTPRequestHandler

def current_lifestyle_pmt(
    current_monthly_expenses,
    annual_inflation,
    saving_years,
    saving_annual_return,
    retirement_years,
    retirement_annual_return,
    initial_investment):

    retirement_monthly_return = ((1 + retirement_annual_return) ** (1 / 12)) - 1
    saving_monthly_return = ((1 + saving_annual_return) ** (1 / 12)) - 1
    monthly_inflation = ((1 + annual_inflation) ** (1 / 12)) - 1

    real_retirement_pmt = npf.fv(
        rate=monthly_inflation, pv=-current_monthly_expenses,
        nper=(saving_years * 12), pmt=0)

    retirement_fund = npf.pv(
        rate=retirement_monthly_return-monthly_inflation,
        nper=(retirement_years * 12),
        pmt=real_retirement_pmt)

    saving_payment = npf.pmt(
        rate=saving_monthly_return-monthly_inflation,
        nper=(saving_years * 12),
        pv=initial_investment,
        fv=retirement_fund)

    return {
        'real_retirement_pmt': real_retirement_pmt,
        'retirement_fund': -retirement_fund,
        'saving_payment': saving_payment
    }

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(url.query)

        clpmt = current_lifestyle_pmt(
            current_monthly_expenses = float(query_params['current_monthly_expenses'][0]),
            annual_inflation = float(query_params['annual_inflation'][0]) / 100,
            saving_years = int(query_params['saving_years'][0]),
            saving_annual_return = float(query_params['saving_annual_return'][0]) / 100,
            retirement_years = int(query_params['retirement_years'][0]),
            retirement_annual_return = float(query_params['retirement_annual_return'][0]) / 100,
            initial_investment = float(query_params['initial_investment'][0]))

        self.wfile.write(json.dumps(clpmt).encode())
        return
