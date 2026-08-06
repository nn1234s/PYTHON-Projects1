import datetime
import calendar
city = input("Enter your city name ")
temp = float(input("Enter temprature in C "))
print("City Name",city)
print("Today's Temprature",temp)
if temp > 35:
    print("It's really hot!")
if temp > 27:
    print("Good day to go outside!")    
else:
    print("It might be raining")    
if temp > 35:
    print("Its very hot outside..")    
elif temp > 25:
    print("It's Sunny and Warm. Great day to play!") 
elif temp > 15:
    print("Cool and Breezy!") 
else:
    print("It's very cold. Make yourself warm!") 
now = datetime.datetime.now()    
print("Date n time",now)
print(calendar.calendar(now.year))