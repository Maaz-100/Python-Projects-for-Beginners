while True:

    current_currency = input("What do you have enter usd/eur/cad ")
    if current_currency == "usd" or current_currency == "eur" or current_currency == "cad":

        convert_currecny = input("What do you want to convert to usd / eur / cad ")

        if convert_currecny == "usd" or convert_currecny == "eur" or convert_currecny == "cad":

            if convert_currecny != current_currency:
                break
            else:
                print("Try again and enter diffrent currecny ")


        else:
            print("Enter usd cad or eur in lowercase ")



    else:
        print("Enter usd cad or eur in lowercase ")

if current_currency == "usd" and convert_currecny == "eur":
    conversion_rate = 0.96

elif current_currency == "usd" and convert_currecny == "cad":
    conversion_rate = 1.44

elif current_currency == "eur" and convert_currecny == "cad":
    conversion_rate = 1.49

elif current_currency == "eur" and convert_currecny == "usd":
    conversion_rate = 1.04

elif current_currency == "cad " and convert_currecny == "eur":
    conversion_rate = 0.67

elif current_currency == "cad" and convert_currecny == "usd":
    conversion_rate = 0.7

else:
    print("Error")

money_ammount= float(input("How much of the prescribed currency do you have? "))


print("You have ", money_ammount, "in", current_currency, "and by converting it into ", convert_currecny,
      " you will have: ",money_ammount * conversion_rate , convert_currecny)
