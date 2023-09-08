import calendar
yr=int( input( "enter year"))
if calendar.isleap(yr):
  print(yr, "Is a leap year")
else:
  print(yr, "Is not a leap year")