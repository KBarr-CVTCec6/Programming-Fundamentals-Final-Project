#!/usr/bin/env python3


import db

from datetime import date, datetime, timedelta
from objects import full_build


MONTHS = ("January-Garnet", "February-Amethyst", "March-Aquamarine", "April-Diamond", "May-Emerald", "June-Pearl",
         "July-Ruby", "August-Peridot", "September-Sapphire", "October-Opal", "November-Topaz", "December-Turquoise")

METALS = ("GOLD", "SILVER", "PLATINUM")

JEWELRY = ("BRACELET", "NECKLACE", "RING")

def add_build(build_history):
    month = get_month()
    metal = get_metal()
    jewelry  = get_jewelry()
    

    full_build = build_history(month, metal, jewelry )
    build_history.apend(Build)
    db.make_Build(build_history)
    print (f"{build} was added to history.\n")
  
      

def get_month():
    while True:
        try:
            month = int(input("Enter the month number you would like to add a birthstone for? "))
            if 1 <= month <= 12:        
                return MONTHS[month-1]
            else:
                print("Invalid month. Please try again.")
        except ValueError:
            print("Please enter a month number between 1 and 12.")



def get_metal():
    while True:
        metal = input("Choose the type of metal and type it in (Gold, Silver, Platinum): ").upper()
        if metal in METALS:
            return metal
        else:
            print("Invalid metal. Please try again")

def get_jewelry():
    while True:
        jewelry = input("Choose the type of jewelry to create and type it in (Bracelet, Necklace, Ring): " ).upper()
        if jewelry in JEWELRY:
            return jewelry
        else:
            print("Invalid jewelry type. Please try again")


def display_read_build_history (build_history):
    if build_history == None:
        print ("There are currently not any jewelry builds on file.")
    else:
        for i, full_build in enumerate(build_history, start=1):
            print(f"{i}.{full_build.month_stone}{full_build.metal} {full_build.jewelry}")

    print()


            



def display_title():
    print("                              Birthstone Jewelry Builder")



def display_dates():
    print()

    date_format = "%Y-%m-%d"
    now = datetime.now()    
    current_date = datetime(now.year, now.month, now.day)
    print(f"CURRENT DATE:    {current_date.strftime(date_format)}")

    while True:
        build_date_str = input("Start build date (same format as CURRENT DATE):       ")
        if build_date_str == "":
            print()
            return

        try:
            build_date = datetime.strptime(build_date_str, date_format)
        except ValueError:
            print("Incorrect date format. Please try again.")
            continue
        
        ship_time = build_date + timedelta(days=10)
        time_span = ship_time - build_date

        if time_span.days > -1:
            print(f"Days to ship: {time_span.days}")
        print()
        break


def display_menu():
    print("Menu Options")
    print("1-Add Build")
    print("2-Display Build History")
    print("3-Exit program")


def main():
    display_title()
    display_dates()
    display_menu()

    db.connect()

    full_build = db.get_Build()

    while True:
        try:
            option = int(input("Menu option: "))
        except ValueError:
            option = -1    
        if option == 1:
            add_build(build_history)
        elif option == 2:
            display_full_build(build_history)
        elif option == 3:
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()

if __name__ == "__main__":
    main()
    









          
