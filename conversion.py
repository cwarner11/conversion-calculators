def main ():


    while True:
        # Gets weight from user as float
        weight = float((input("Please enter weight: ")))

        # rounds weight to hundreths place
        weight = round(weight, 2)
        if weight > 0:
            break

        print("weight is not greater than zero(0), try again!")


    #repats the input of measure unit if not in right format
    while True:
        var1 = input("Is this in Pounds(lbs) or Kilograms(kgs)?: ").lower() #converts lettter from input to lower

        #kgs to lbs
        if (var1 == "kgs") or (var1 == "kilograms"):
            convert_to_lbs = round((weight * 2.2046),2)
            print(f"{weight}kg(s) is {convert_to_lbs}lb(s)")
            break

        #lbs to kgs
        elif (var1 == "lbs") or (var1 == "pounds"):
            convert_to_kgs = round((weight / 2.2046),2)
            print(f"{weight}lb(s) is {convert_to_kgs}kg(s)")
            break

main()
