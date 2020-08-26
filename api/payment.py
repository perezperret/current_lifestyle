import json
import numpy_financial as npf
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

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
                rate=monthly_inflation, pv=-2000, nper=(saving_years * 12), pmt=0)

            retirement_fund = npf.pv(
                rate=retirement_monthly_return-monthly_inflation,
                nper=(retirement_years * 12),
                pmt=real_retirement_pmt)

            saving_payment = npf.pmt(
                rate=saving_period_monthly_return-monthly_inflation,
                nper=(saving_years * 12),
                pv=initial_investment,
                fv=retirement_fund)

            return {
                'real_retirement_pmt': real_retirement_pmt,
                'retirement_fund': -retirement_fund,
                'saving_payment': saving_payment
            }

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        clpmt = current_lifestyle_pmt(
            current_monthly_expenses = 2000,
            annual_inflation = 0.02,
            saving_years = 35,
            saving_annual_return = 0.05,
            retirement_years = 25,
            retirement_annual_return = 0.03,
            initial_investment = 0)

        self.wfile.write(json.dumps(clpmt).encode())
        return
