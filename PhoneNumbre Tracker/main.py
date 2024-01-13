import phonenumbers as pn
from phonenumbers import geocoder,carrier,timezone

def check_number(number):
    Carrier =  carrier.name_for_number(number,"en")
    Region =  geocoder.description_for_number(number,"en")
    Time_zone = timezone.time_zones_for_number(number)
    details = {
        "carrier":Carrier,
        "region":Region,
        "time_zone":Time_zone
    }
    return details

def run():
    phone_number = input("Enter the Phone number with country code(+xx): ")
    try:
        number_data = pn.parse(phone_number)
        if pn.is_valid_number(number_data) and pn.is_possible_number(number_data):
            details = check_number(number_data)
            print(f"""
                Phone Number : {phone_number} 
                Carrier : {details['carrier']} 
                Region : {details['region']}
                Time-Zone : {details['time_zone']}
                """)
            print(f"""
                  1. Search other number
                  0. Exit 
                  """)
            choice = input(">> ")
            if choice == "1":
                run()
            elif choice == "0":
                print("Thanks for Using !!")
                exit()
            else:
                print("Something wrong!")
        else:
            print("Enter a valid Number !!")
    except Exception as e:
        print("Enter  Number in right order (+xx xxxxxxxxxx)")
        run()

run()
    
    

