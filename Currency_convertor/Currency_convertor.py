#Author - Sneha Malik
#Date - 13-11-2021
#Currency Convertor

while True:
    try:
        amount=float(input("Enter the amount in INR you want to convert into another currency: "))

    except:
        print("\nPlease enter the amount here\n")
        continue

    with open("currency_Convertor.txt") as f:
        #reading data in currency_convertor
        lines=f.readlines()
        list_of_data=[]
        #d : dictionary of country names as keys and values are their currency amount for 1 INR
        d=dict()
        for line in lines:
            list_of_data.append(line.split("\t"))

        for i in list_of_data:
            d[i[0]]=i[1]

        for i in d:
            print(f" {i}")


        name_of_country = input("\nEnter the name of currency you want your amount to convert to : ")

        if name_of_country in d.keys():
            print(f"{amount} INR rupees are equal to {amount*float(d[name_of_country])} {name_of_country} ")
            break

        else:
            print("\nInvalid choice Please select from the options given\n")
            continue







