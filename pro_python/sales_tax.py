TAX_RATE_BY_STATE = {
    'MT': 1.03
}

def add_sales_tax(total, state):
    tax_rate = TAX_RATE_BY_STATE[state]
    return total * tax_rate