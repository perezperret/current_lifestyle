import json
import urllib.parse
from http.server import BaseHTTPRequestHandler
from lib.calculator import current_lifestyle_pmt

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
