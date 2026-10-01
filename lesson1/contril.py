
#gender=input(str("job for  men"))#
#loction=input(str("nairobi county"))
#if gender=="men in nairobi":
#    print("can get the job")
#elif gender=="women outside nairobi":
#    print("can't  get the job")


company = "Scam Job providers"

name = input(str("What are your full names? "))

location = input(str("Where are you located? "))

date = float(input("When do you want to start? "))

if location == "Nairobi":
    print("Welcome ", name, "to ", company, "you sart working at", date)
elif location == "Thika":
    print("Welcome ", name, "to ", company, "you sart working at", date)
else: print("Sorry ", name, "You did't qualify to get a position at", company, "your location", location, "Is not available")
