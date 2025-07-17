
#---------------------------------------------------------------------------------

        #FULL NAME SPLIT + CAPITALISED
# persons_name = input("Please enter your full name: ")
# loc_space = persons_name.index(" ")
# f_name = persons_name[:loc_space]
# s_name = persons_name[(loc_space+1):]
# f_name = f_name.capitalize()
# s_name = s_name.capitalize()
# print(f_name)
# print(s_name)

#---------------------------------------------------------------------------------
        #BOOLEAN VALUE

# if grant == True:               #TRUE / FALSE MAKES THIS A BOOLEAN VALUE
#     print("Grant awarded")
# else:
#     print("No grant awarded")

#---------------------------------------------------------------------------------
        #USERNAME + PASSWORD

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# security = 0        #DEFAULT VALUE
#
# if username == "guest":
#    if password == "guest":
#     print("Access Granted, Welcome Guest 1.")
#     security = 1
#    else:
#        print(username, ", Your password is incorrect, please try again...")
#
# elif username == "M.Dawson":
#     if password == "nos123":
#         print("Access Granted, Welcome M.Dawson.")
#         security = 5
#     else:
#         print(username, ", Your password is incorrect, please try again...")
#
# else:
#     print("Access denied - Unknown user")
#
# print("Security level granted:", security)

#---------------------------------------------------------------------------------

        #SEAT PRICES + TICKETS SOLD
# ORCHESTRA = 40.00
# MEZZANINE = 30.00
# BALCONY = 15.00
#
# num_orchestra = 0
# num_mezzanine = 0
# num_balcony = 0
#
# print("1. Orchestra")
# print("2. Mezzanine")
# print("3. Balcony")
#
# seat = int(input("Please choose a seat: "))
#
# if seat == 1:
#     price = ORCHESTRA
#     num_orchestra += 1
#     print("Orchestra seat chosen costing €" + str(price))
# elif seat == 2:
#     price = MEZZANINE
#     num_mezzanine += 1
#     print("Mezzanine seat chosen costing €" + str(price))
# elif seat == 3:
#     price = BALCONY
#     num_balcony += 1
#     print("Balcony seat chosen costing €" + str(price))
# else:
#     price = 0
#     print("INVALID OPTION CHOSEN")
# print("Number of Orchestra tickets sold: ", num_orchestra)
# print("Number of Mezzanine tickets sold: ", num_mezzanine)
# print("Number of Balcony tickets sold: ", num_balcony)

#---------------------------------------------------------------------------------

        #EVENT TYPE / EVENT MANAGER
# PRIVATE = 1
# CORPORATE = 2
# event_type = int(input("Please enter event type: "))
# if event_type == PRIVATE:
#     event_manager = "C.Larman"
# elif event_type == CORPORATE:
#     event_manager = "Ken Bass"
# else:
#     event_manager = "Unknown - Invalid event type."
# print("Your event type is:", event_type, "Your manager is:", event_manager)

#---------------------------------------------------------------------------------

        #WOOD PRICES + AMOUNTS
# OAK_PRICE = 225.00
# PINE_PRICE = 100.00
# MAHOGANY_PRICE = 310.00
# print("\t\t FURNITURE STORE")
# print("1. \tOAK")
# print("2. \tPINE")
# print("3. \tMAHOGANY")
# choice = int(input("Enter your choice: "))
# if choice == 1:             #1/2/3 Is easier than OAK_PRICE to avoid errors in code.
#     price = OAK_PRICE
#     print("The current price is:", OAK_PRICE)
# elif choice == 2:
#     price = PINE_PRICE
#     print("The current price is:", PINE_PRICE)
# elif choice == 3:
#     price = MAHOGANY_PRICE
#     print("The current price is:", MAHOGANY_PRICE)
# else:
#     price = 0
#     print("Invalid table type chosen")
#
# if price != 0:
#     quantity = int(input("How many tables do you want? "))
#     total_cost = price * quantity
#     print("The total cost is:", total_cost)
# else:
#     print("Invalid table type chosen")

#---------------------------------------------------------------------------------

        #EXAM RESULT CALCULATOR
# mark = int(input("Mark: "))
# if mark < 35:
#     print("F")
# elif mark < 39:     #elif = else if. (MORE THAN 2 OPTIONS)
#     print("D")
# elif mark < 49:
#     print("C")
# elif mark < 54:
#     print("C+")
# elif mark < 59:
#     print("B-")
# elif mark < 69:
#     print("B")
# elif mark < 79:
#     print("B+")
# elif mark > 80:
#     print("A")

#---------------------------------------------------------------------------------

        #SECONDS - MINUTES - HOURS
# seconds = int(input("please enter how many seconds: " ))
# minute = (seconds * 1 / 60)
# hour = (minute * 1 / 60)
# print("Hours: ", hour)
# print("minutes: ", minute)
# print("seconds: ", seconds)

#---------------------------------------------------------------------------------

        #FILENAME UPDATE
# filename = input("Please enter the file you wish to update: ")
# result = (filename + '.py')
# print("Your new file name is: ", result)

#---------------------------------------------------------------------------------

        #MULTIPLING INPUT
# userword = str(input("please enter a word: "))
# usernumber = int(input("please enter a number: "))
# result = (userword + ' ') * usernumber
# print("your word selected was: ", userword)
# print("your final result is: ", result)

#---------------------------------------------------------------------------------

        #1ST 2 LETTERS + LAST 2
# userword = input("Please enter a word longer than 3 characters: ")
# newword = userword[:2] + userword[-2:]
# print("your word selected was", userword)
# print("your new word is", newword)

#---------------------------------------------------------------------------------

        #DETECT SYMBOL IN PASSWORD
# passcode = input("Please enter your password to continue: ")
# amount = len(passcode)
# symbol = '!' in passcode
# print("Your passcode is:", amount, ".Does it contain a (!)?", symbol)

#---------------------------------------------------------------------------------

        #HOURS + MINS + SECS INTO SECS
#seconds = int(input("Please enter amount of seconds."))
#minutes = int(input("Please enter amount of minutes."))
#hours = int(input("Please enter amount of hours."))
#number_of_seconds = (seconds + minutes * 60 + hours * 60 * 60)
#print(number_of_seconds)

#---------------------------------------------------------------------------------

        #AREA OF CIRCLE
# radius = int(input("Please enter the radius of a circle."))
# area_of_circle = (radius ** 2 * 3.14159)
# area_of_circle = round(area_of_circle, 3)
# print("The area is:", area_of_circle)

#---------------------------------------------------------------------------------

        #ACRONYMS
# i_one = input("Please enter the first word: ")
# i_two = input("Please enter the second word: ")
# i_three = input("Please enter the third word: ")
# acronym = i_one[0].upper() + i_two[0].upper() + i_three[0].upper()
# print("Your Acronym is:", acronym)

#---------------------------------------------------------------------------------

