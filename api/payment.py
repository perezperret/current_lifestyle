from flask import Flask, Response, request, jsonify
from lib.calculator import current_lifestyle_pmt

app = Flask(__name__)

@app.route('/api/payment', methods=['POST'])
def get():
    clpmt = current_lifestyle_pmt(
        current_monthly_expenses = float(request.form['current_monthly_expenses']),
        annual_inflation = float(request.form['annual_inflation']) / 100,
        saving_years = int(request.form['saving_years']),
        saving_annual_return = float(request.form['saving_annual_return']) / 100,
        retirement_years = int(request.form['retirement_years']),
        retirement_annual_return = float(request.form['retirement_annual_return']) / 100,
        initial_investment = float(request.form['initial_investment']))

    return jsonify(clpmt)
