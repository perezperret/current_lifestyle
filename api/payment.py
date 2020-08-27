from flask import Flask, Response, request, jsonify
from lib.calculator import current_lifestyle_pmt

app = Flask(__name__)

@app.route('/api/payment')
def get():
    clpmt = current_lifestyle_pmt(
        current_monthly_expenses = float(request.args.get('current_monthly_expenses')),
        annual_inflation = float(request.args.get('annual_inflation')) / 100,
        saving_years = int(request.args.get('saving_years')),
        saving_annual_return = float(request.args.get('saving_annual_return')) / 100,
        retirement_years = int(request.args.get('retirement_years')),
        retirement_annual_return = float(request.args.get('retirement_annual_return')) / 100,
        initial_investment = float(request.args.get('initial_investment')))

    return jsonify(clpmt)
