#List of functions here

#Calculate Subtotal
def calculate_subtotal(total, discount):
    return float("{0:.2f}".format(total - discount))

#Calculate Sales Tax
def calculate_sale_tax_amt(sub_total,tax_rate):
    return float("{0:.2f}".format(sub_total * (tax_rate / 100)))
    
#Calculate Grand Total
def calculate_grand_total(sub_total,sale_tax_amt):
    return float("{0:.2f}".format(sub_total + sale_tax_amt))