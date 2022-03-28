#Import Module
import functions

#Header
print("Department Store Sales Tax and Grand Total Application")

#Data Entry
while(True):
    #Instructions for user
    print("\nData Entries: Enter 0 to end your input")
    
    #Initialize Variable
    total = 0
    
    #Add cost of items
    while(True):
        c = float(input("Cost of item: "))
        if c == 0:
            print("All items total: ${:.2f}\n".format(total))
            break
        #New total after adding all items
        total += c
    
    #Tax Rate
    tax_rate = int(input("Sales tax rate (%): "))
    
    #Checking user inputted tax rate
    while(True):
        if not (tax_rate >= 6 and tax_rate <= 10):
            print("Tax rate should be from 6 to 10")
            tax_rate = int(input("Sales tax rate (%): "))
        else:
            break
        
    #Validating discounts
    #Starting with promo codes
    if total < 100:
        promo_code = int(input("Promotion code: "))
        while(True):
            flag = True
            if promo_code == 123:
                discount_amt = 1
            elif promo_code == 456:
                discount_amt = 2
            elif promo_code == 789:
                discount_amt = 3
            elif promo_code == 0:
                discount_amt = 0
            else:
                print("Invalid promotion code. Try again")
                promo_code = int(input("Promotion code: "))
                flag = False     
            if flag:
                break
    #For when the total is more than 100
    if total > 100:
        discount_amt = total*10/100 
    print("\nDiscount amount: ${:.2f}".format(discount_amt))
    
    #Calling functions from module
    subtotal = functions.calculate_subtotal(total,discount_amt)
    sales_tax_amt = functions.calculate_sale_tax_amt(subtotal,tax_rate)
    grandtotal = functions.calculate_grand_total(subtotal,sales_tax_amt)
    
    #Print results
    print("Subtotal: ${}".format(subtotal))
    print("Sales tax amount: ${}".format(sales_tax_amt))
    print("Grandtotal: ${:.2f}".format(grandtotal))
    
    #User inputted choice to continue to run
    ch = input("\nContinue? y/Y/n/N: ")
    if ch == 'n' or ch == 'N':
        break
    
#When Finished
print("\nProgram is terminated")   