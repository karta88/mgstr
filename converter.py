def fahrenheitToCelsius(fcTemp):
    return ((fcTemp - 32) * 5 / 9)


def celsiusToFahrenheit(cfTemp):
    return ((cfTemp * 9) / 5) + 32


def kalvinToCelsius(kcTemp):
    return (kcTemp - 273)


def celsiumToKalvin(ckTemp):
    return (ckTemp + 273)


def fahrenheitToKalvin(fkTemp):
    return ((fkTemp - 32) * 5 / 9) + 273


def kalvinToFahrenheit(kfTemp):
    return ((kfTemp - 273) * 9 / 5) + 32


def grammToLb(gfWeight):
    return (gfWeight / 453.592)


def lbToGramm(fgWeight):
    return (fgWeight * 453.592)


def grammToPood(gpWeight):
    return (gpWeight / 16380.687)


def poodToGramm(pgWeight):
    return (pgWeight * 16380.687)


def lbToPood(lpWeihgt):
    return (lpWeihgt / 36.113)


def poodToLb(plWeight):
    return (plWeight * 36.113)


def meterToMile(mmlLenght):
    return (mmlLenght / 1609.344)


def mileToMeter(mlmLenght):
    return (mlmLenght * 1609.344)


def meterToVerst(mvLenght):
    return (mvLenght / 1066.8)


def verstToMeter(vmLenght):
    return (vmLenght * 1066.8)


def mileToVerst(mlvLenght):
    return (mlvLenght * 1.509)


def verstToMile(vmlLenght):
    return (vmlLenght / 1.509)


while True:
    print "1 - Temperature"
    print "2 - Weight"
    print "3 - Lenght"
    print "4 - Exit"

    choise = raw_input("Enter menu entry ")

    if choise == "1":

        while (1):
            choice = raw_input("""

        1. Fahrenheit to Celsius
        2. Celsius to Fahrenheit
        3. Kalvin to Celsius
        4. Celsius to Kalvin
        5. Fahrenheit to Kalvin
        6. Kalvin to Fahrenheit
        7. Exit program

        Please select item : """)

            if choice == "7":
                break
            elif choice == "1":
                # fahrenheit to celsius
                try:
                    fcTemp = float(raw_input("Please enter degrees Fahrenheit: "))
                    print("%.1f degrees Fahrenheit equals %.1f degrees Celsius" % (fcTemp, fahrenheitToCelsius(fcTemp)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "2":
                # celsius to fahrenheit
                try:
                    cfTemp = float(raw_input("Please enter degrees Celsius: "))
                    print("%.1f degrees Celsius equals %.1f degrees Fahrenheit" % (cfTemp, celsiusToFahrenheit(cfTemp)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "3":
                # kalvin to celsius
                try:
                    kcTemp = float(raw_input("Please enter degrees Kalvin: "))
                    print("%.1f degrees Kalvin equals %.1f degrees Celsius" % (kcTemp, kalvinToCelsius(kcTemp)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "4":
                # celsius to kalvin
                try:
                    ckTemp = float(raw_input("Please enter degrees Celsius: "))
                    print("%.1f degrees Celsius equals %.1f degrees Kalvin" % (ckTemp, celsiumToKalvin(ckTemp)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "5":
                # fahrenheit to kalvin
                try:
                    fkTemp = float(raw_input("Please enter degrees Fahrenheit: "))
                    print("%.1f degrees Fahrenheit equals %.1f degrees Kalvin" % (fkTemp, fahrenheitToKalvin(fkTemp)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "6":
                # kalvin to fahrenheit
                try:
                    kfTemp = float(raw_input("Please enter degrees Kalvin: "))
                    print("%.1f degrees Kalvin equals %.1f degrees Fahrenheit" % (kfTemp, kalvinToFahrenheit(kfTemp)))
                    break
                except:
                    print("Invalid entry.\n")
            else:
                print('That input is not valid')

    elif choise == "2":

        while (1):
            choice = raw_input("""

        1. Gramm to Lb
        2. Lb to Gramm
        3. Gramm to Pood
        4. Pood to Gramm
        5. Lb to Pood
        6. Pood to Lb
        7. Exit program

        Please select item : """)

            if choice == "7":
                break
            elif choice == "1":
                # gramm to lb
                try:
                    gfWeight = float(raw_input("Please enter value Gramm: "))
                    print("%.1f Gramm equals %.1f Lb" % (gfWeight, grammToLb(gfWeight)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "2":
                # lb to gramm
                try:
                    fgWeight = float(raw_input("Please enter value Lb: "))
                    print("%.1f Lb equals %.1f Gramm" % (fgWeight, lbToGramm(fgWeight)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "3":
                # gramm to poods
                try:
                    gpWeight = float(raw_input("Please enter value Gramm: "))
                    print("%.1f Gramm equals %.1f Pood" % (gpWeight, grammToPood(gpWeight)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "4":
                # pood to gramm
                try:
                    pgWeight = float(raw_input("Please enter value Pood: "))
                    print("%.1f Pood equals %.1f Gramm" % (pgWeight, poodToGramm(pgWeight)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "5":
                # lb to pood
                try:
                    lpWeihgt = float(raw_input("Please enter value Lb: "))
                    print("%.1f Lb equals %.1f Pood" % (lpWeihgt, lbToPood(lpWeihgt)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "6":
                # pood to lb
                try:
                    plWeihgt = float(raw_input("Please enter value Pood: "))
                    print("%.1f Pood equals %.1f Gramm" % (plWeihgt, poodToLb(plWeihgt)))
                    break
                except:
                    print("Invalid entry.\n")
            else:
                print('That input is not valid')

    elif choise == "3":
        while (1):
            choice = raw_input("""

        1. Meter to Mile
        2. Mile to Meter
        3. Meter to Verst
        4. Verst to Meter
        5. Mile to Verst
        6. Verst to Mile
        7. Exit program

        Please select item : """)

            if choice == "7":
                break
            elif choice == "1":
                # meter to mile
                try:
                    mmlLenght = float(raw_input("Please enter value Meter: "))
                    print("%.1f Meter equals %.1f Mile" % (mmlLenght, meterToMile(mmlLenght)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "2":
                # mile to meter
                try:
                    mlmLenght = float(raw_input("Please enter value Mile: "))
                    print("%.1f Mile equals %.1f Meter" % (mlmLenght, mileToMeter(mlmLenght)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "3":
                # meter to verst
                try:
                    mvLenght = float(raw_input("Please enter value Meter: "))
                    print("%.1f Meter equals %.1f Verst" % (mvLenght, meterToVerst(mvLenght)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "4":
                # verst to meter
                try:
                    vmLenght = float(raw_input("Please enter value Verst: "))
                    print("%.1f Verst equals %.1f Meter" % (vmLenght, verstToMeter(vmLenght)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "5":
                # mile to verst
                try:
                    mlvLenght = float(raw_input("Please enter value Mile: "))
                    print("%.1f Lb equals %.1f Pood" % (mlvLenght, mileToVerst(mlvLenght)))
                    break
                except:
                    print("Invalid entry.\n")
            elif choice == "6":
                # verst to mile
                try:
                    vmlLenght = float(raw_input("Please enter value Verst: "))
                    print("%.1f Pood equals %.1f Gramm" % (vmlLenght, verstToMile(vmlLenght)))
                    break
                except:
                    print("Invalid entry.\n")
            else:
                print('That input is not valid')
    else:
        break