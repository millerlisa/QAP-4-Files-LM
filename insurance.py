# Program to enter and calculate new insurance policy information for customers.
# Written by Lisa Miller
# Date: 2023-11-17 to 2023-11-20

# Import required libraries
import datetime
import formatValues as fv

# CONSTANTS
AREA_CODE = 3
NUMBER_SPLIT = 6
BASIC_PREMIUM_RATE = 869.00
MULTI_CAR_DISCOUNT_RATE = 0.25
EXTRA_LIABILITY_RATE = 130.00
GLASS_COVERAGE_RATE = 86.00
LOANER_CAR_COVERAGE_RATE = 58.00
HST_RATE = 0.15
PROCESSING_FEE_RATE = 39.99

# Variables
cars = 0
carsInsured = 0
discountPremium = 0
downPayment = 0
HST = 0
payment = ""
paymentAmount = 0
paymentDetails = ""
paymentLst = ["F", "M", "D"]
paymentType = ""
phoneNumber = ""
policyNumber = 1944 
premium = 0
prov = ""
province = ""
provLst = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]

# Functions
def formatTelephone(phoneNumber):
    assert len(phoneNumber) == 10
    phoneNumber = (f"({phoneNumber[:AREA_CODE]}) {phoneNumber[AREA_CODE:NUMBER_SPLIT]}-{phoneNumber[NUMBER_SPLIT:]}")
    return phoneNumber

def validateProvince(province): 
    while True:
        province = input("Please enter customer's province (XX): ").upper()
        if province == "":
            print("Error. Province is required. Please enter a valid two-character province code.")
        elif len(province) != 2:
            print("Error. Please enter a valid two-character province code.")
        elif province not in provLst:   
            print("Error. Not a valid province code. Please re-enter.")
        else:
            break
    return province

def numCarsInsured(carsInsured):
    carsInsured = 0
    while True:
        try:
            carsInsured = int(input("Please enter the number of cars to be insured: "))
        except:
            print("Error. Please enter a valid integer.")
        else:
            if carsInsured < 1:
                print("Error. At least 1 car must be insured. Please re-enter.")
            else:
                break
    return carsInsured

def calcPremium(carsInsured):
    premium = 0
    discountPremium = 0
    if carsInsured == 1:
        premium = BASIC_PREMIUM_RATE
    elif carsInsured > 1:
        discountPremium = BASIC_PREMIUM_RATE - (BASIC_PREMIUM_RATE * MULTI_CAR_DISCOUNT_RATE)
        premium = BASIC_PREMIUM_RATE + (discountPremium * (carsInsured - 1))
    return premium

def calcDiscountPremium(carsInsured):
    discountPremium = 0
    if carsInsured > 1:
        discountPremium = BASIC_PREMIUM_RATE - (BASIC_PREMIUM_RATE * MULTI_CAR_DISCOUNT_RATE)
    return discountPremium

# Main program
while True:
    policyNumber += 1

    # Inputs
    firstName = input("Please enter customer's first name: ").title()
    lastName = input("Please enter customer's last name: ").title()
    address = input("Please enter customer's address: ").title()
    city = input("Please enter customer's city: ").title()
    province = validateProvince(province)   
    postalCode = input("Please enter customer's postal code (X#X#X#): ").upper()
    while True:
        try:
            phoneNumber = input("Please enter customer's phone number (##########): ")
        except:
            print("Error. Please enter a valid 10 digit phone number.")
        else:
            if phoneNumber == "":
                print("Error. Phone number is required. Please enter a valid 10 digit phone number.")
            elif len(phoneNumber) != 10:
                print("Error. Please enter a valid 10 digit phone number.")
            else:
                break
    phoneNumber = formatTelephone(phoneNumber)
    carsInsured = numCarsInsured(carsInsured)
    extraLiability = input("Does the customer require extra liability coverage, upto $1,000,000? (Y/N): ").upper()
    glassCoverage = input("Does the customer require glass coverage? (Y/N): ").upper()
    loanerCarCoverage = input("Does the customer require loaner car coverage? (Y/N): ").upper()
    while True:
        payment = input("Will the customer pay in Full, Monthly or Down-Pay (F/M/D): ").upper()
        if payment == "":
            print("Error. Payment type is required. Please enter 'F' for Payment-in-Full, 'M' for Monthly-Installments or 'D' for Down-Payment.")
        elif payment not in paymentLst:
            print("Error. Please enter F/M/D.")
        else:
            if payment == "D":
                downPayment = float(input("Please enter the down payment amount: "))
            else:
                break
        break

    #  Previous claims
    prevClaimAmountLst = []
    prevClaimDateLst = []
    while True:
        try:
            prevClaimAmount = float(input("Enter the amount of the previous claim (or press Enter to end): "))
        except: 
            break
        prevClaimDate = input("Enter the date of the previous claim (YYYY-MM-DD): ")
        prevClaimDate = datetime.datetime.strptime(prevClaimDate, "%Y-%m-%d")   
        prevClaimAmountLst.append(prevClaimAmount)
        prevClaimDateLst.append(prevClaimDate)
    
    # Calculating insurance premiums
    premium = calcPremium(carsInsured)
    discountPremium = calcDiscountPremium(carsInsured) 
    totalDiscountPremium = discountPremium * (carsInsured - 1)
        
    # Calculating extra costs    
    totalExtraCosts = 0
    totalExtraPerCar = 0
    if carsInsured == 1:
        if extraLiability == "Y":
            totalExtraCosts += EXTRA_LIABILITY_RATE
        if glassCoverage == "Y":
            totalExtraCosts += GLASS_COVERAGE_RATE
        if loanerCarCoverage == "Y":
            totalExtraCosts += LOANER_CAR_COVERAGE_RATE
    elif carsInsured > 1:
        if extraLiability == "Y":
            extraLiabilityCosts = (EXTRA_LIABILITY_RATE * carsInsured)
            totalExtraCosts += (EXTRA_LIABILITY_RATE * carsInsured)
            totalExtraPerCar += (EXTRA_LIABILITY_RATE)
        if glassCoverage == "Y":
            extraGlassCosts = (GLASS_COVERAGE_RATE * carsInsured)
            totalExtraCosts += (GLASS_COVERAGE_RATE * carsInsured)
            totalExtraPerCar += (GLASS_COVERAGE_RATE)
        if loanerCarCoverage == "Y":
            extraLoanerCarCosts = (LOANER_CAR_COVERAGE_RATE * carsInsured)
            totalExtraCosts += (LOANER_CAR_COVERAGE_RATE * carsInsured)
            totalExtraPerCar += (LOANER_CAR_COVERAGE_RATE)

    # Calculating total cost
    totalInsurancePremium = premium + totalExtraCosts
    HST = (premium) *  HST_RATE
    totalCost = totalInsurancePremium + HST

    # Calculating payments
    if payment == "F":
        paymentAmount = totalCost
        paymentDetails = "Payment-in-Full"
    elif payment == "M":
        paymentAmount = (totalCost + PROCESSING_FEE_RATE) / 8
        paymentDetails = "Monthly-Installments"
    elif payment == "D":
        paymentAmount = (totalCost - downPayment + PROCESSING_FEE_RATE) / 8
        paymentDetails = "Down-Payment"
    
    # Calculating payment dates
    invoiceDate = datetime.datetime.now()
    firstPaymentDate = invoiceDate + datetime.timedelta(days=30)

# Outputs
    print()
    print()
    print(f"                         --------------------------")
    print(f"                         One Stop Insurance Company")
    print(f"                               99 Main Street")
    print(f"                               St. John's, NL")
    print(f"                                  A1B 2C3")
    print()
    print(f"                               (709) 555-1234")
    print(f"                         --------------------------")
    print()
    print(f"                           Auto Insurance Invoice")
    print()
    print()
    print(f"                                            Policy Number:           {policyNumber:>5d}")
    print()
    print(f"                                            Invoice Date:       {invoiceDate.strftime('%Y-%m-%d'):<12s}")  
    print()              
    print(f"                                            First Payment Date: {firstPaymentDate.strftime('%Y-%m-%d'):<12s}")
    print()
    # Customer information
    print(f"   {firstName} {lastName}")
    print(f"   {address}")
    print(f"   {city}, {province}")
    print(f"   {postalCode}")
    print()
    print(f"   Phone: {phoneNumber}")
    print()
    print()
    # Insurance information
    print(f"   Number of cars insured: {carsInsured:<3d}")
    print()
    print(f"   Item Description                     Item Cost               Item Total") 
    print(f"   -----------------------------------------------------------------------")
    if carsInsured > 1:
        print(f"")
        print(f"   Basic Premium:                        {fv.FDollar2(BASIC_PREMIUM_RATE):<10s}                {fv.FDollar2(BASIC_PREMIUM_RATE):<10s}")
        print()
        print(f"   Multi-car Discount:                     {fv.FPercent(MULTI_CAR_DISCOUNT_RATE):<3s}")
        print()
        print(f"   Premium per additional car:           {fv.FDollar2(discountPremium):<8s}                  {fv.FDollar2(totalDiscountPremium):<10s}")   
        print(f"   -----------------------------------------------------------------------")
        print(f"                                                                {fv.FDollar2(premium):>10s}")
    else:
        print()
        print(f"   Basic Premium:                        {fv.FDollar2(BASIC_PREMIUM_RATE):<10s}             {fv.FDollar2(premium):>10s}")
        print(f"   -----------------------------------------------------------------------")
    print()
    print(f"   Additional Coverage")
    print(f"   -----------------------------------------------------------------------")
    print()
    if carsInsured == 1 and extraLiability == "N" and glassCoverage == "N" and loanerCarCoverage == "N":
        print(f"   No additional coverage required.")
    if carsInsured == 1 and extraLiability == "Y":
        print(f"   Extra Liability:                      {fv.FDollar2(EXTRA_LIABILITY_RATE):>6s}                   {fv.FDollar2(EXTRA_LIABILITY_RATE):>6s}")
    elif carsInsured > 1 and extraLiability == "Y":
        print(f"   Extra Liability:                      {fv.FDollar2(EXTRA_LIABILITY_RATE):>7s}                {fv.FDollar2(extraLiabilityCosts):>10s}")
    print()
    if carsInsured == 1 and glassCoverage == "Y":
        print(f"   Glass Coverage:                        {fv.FDollar2(GLASS_COVERAGE_RATE):>6s}                    {fv.FDollar2(GLASS_COVERAGE_RATE):>6s}")
    elif carsInsured > 1 and glassCoverage == "Y":
        print(f"   Glass Coverage:                        {fv.FDollar2(GLASS_COVERAGE_RATE):<9s}             {fv.FDollar2(extraGlassCosts):>10s}")
    print()
    if carsInsured == 1 and loanerCarCoverage == "Y":
        print(f"   Loaner Car Coverage:                 {fv.FDollar2(LOANER_CAR_COVERAGE_RATE):>8s}                  {fv.FDollar2(LOANER_CAR_COVERAGE_RATE):>8s}")
    elif carsInsured > 1 and loanerCarCoverage == "Y":
        print(f"   Loaner Car Coverage:                   {fv.FDollar2(LOANER_CAR_COVERAGE_RATE):<6s}                {fv.FDollar2(extraLoanerCarCosts):>10s}")
    print(f"   -----------------------------------------------------------------------")
    if carsInsured == 1:
        print(f"                                      {fv.FDollar2(totalExtraCosts):>10s}                {fv.FDollar2(totalExtraCosts):>10s}")
    elif carsInsured > 1:
        print(f"                                         {fv.FDollar2(totalExtraPerCar):<9s}              {fv.FDollar2(totalExtraCosts):>10s}")
    print()
    print(f"                                                      Subtotal: {fv.FDollar2(totalInsurancePremium):>10s}")
    print(f"                                                      --------------------")
    print(f"                                                           HST: {fv.FDollar2(HST):>10s}")
    print(f"                                                    Total Cost: {fv.FDollar2(totalCost):>10s}")
    print()
    # Payment information
    print(f"   Payment Information")
    print(f"   -----------------------------------------------------------------------")
    print()
    if payment == "F":
        print(f"   Payment Type: {paymentDetails:<22s}")                 
        print(f"                                                Payment Amount: {fv.FDollar2(paymentAmount):>10s}")
    elif payment == "M":
        print(f"   Payment Type: {paymentDetails:<22s}            ")
        print(f"                                                Processing Fee: {fv.FDollar2(PROCESSING_FEE_RATE):>10s}")
        print(f"                                        Monthly Payment Amount: {fv.FDollar2(paymentAmount):>10s}")
    elif payment == "D":
        print(f"   Payment Type: {paymentDetails:<22s}")
        print(f"                                                Processing Fee: {fv.FDollar2(PROCESSING_FEE_RATE):>10s}")
        print(f"                                           Down Payment Amount: {fv.FDollar2(downPayment):>10s}")
        print(f"                                        Monthly Payment Amount: {fv.FDollar2(paymentAmount):>10s}")
    print()
    print()
    # Previous claims
    print(f"   Previous Claims")
    print(f"   -----------------------------------------------------------------------")
    print()
    print(f"                    Claim #     Claim Date       Amount")
    print(f"                  ---------------------------------------")
    print()
    for i in range(len(prevClaimAmountLst)):
        prevClaimNum = i + 1
        print(f"                      {prevClaimNum}.        {(prevClaimDateLst[i]).strftime('%Y-%m-%d'):<10s}    {fv.FDollar2(prevClaimAmountLst[i]):>10s}")
    print()
    print(f"                  ---------------------------------------")
    print()
    print()
    anotherPolicy = input("Do you want to prepare another invoice? (Y/N): ").upper()
    if anotherPolicy == "N":
        break