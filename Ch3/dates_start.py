#
# Example file for working with date information
#
from datetime import date
# from datetime import time
from datetime import datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is", today)

  # print out the date's individual components
  print("Individual object goes like this : " ,today.day ,today.month , today.year)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print(today.weekday())

  days = ["monday","tuesday","wednesday","thursday","friday","saturday"]
  print("that 5th day is :" , days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("the current date and time is : ",today)

  
  # Get the current time
  t = datetime.time(datetime.now())
  print("current time is ",t)
  
 

  
if __name__ == "__main__":
  main();
  