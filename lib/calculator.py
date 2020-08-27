import numpy_financial as npf

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
