#Author: Samuel DeLaughter
#A frivolous 12-line program that prints the full lyrics to 12 Days of Christmas

gifts=['A Partridge in a Pear Tree', 'Two Turtle Doves, and', 'Three French Hens', 'Four Calling Birds', 'Five Golden Rings', 'Six Geese-a-Laying', 'Seven Swans-a-Swimming', 'Eight Maids-a-Milking', 'Nine Ladies Dancing', 'Ten Lords-a-Leaping', 'Eleven Pipers Piping', 'Twelve Drummers Drumming']
ordinal=['st', 'nd', 'rd'] + ['th']*9
for day in range(12):
  print('On the ' + str(day+1) + str(ordinal[day]) + ' day of Christmas, my true love sent to me...')
  gift=day
  while gift >= 0:
    print(str(gifts[gift]))
    gift-=1
  print('\n')
