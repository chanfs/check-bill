#!/usr/local/bin/python
#Author: CHAN Fook Sheng
# 17 May 2020
# This script will compute the total amount for your credit card bill. 
# Just run it and past the bill items on the screen, press Enter and Ctrl-D and the script will read it from standard output
# The script will read each line and assume the last item is the amount you paid 
# It will detect credit return, e.g, 12.00CR will be treated as -12
# It will also remove commas (like 1,200 will become 1200) so that casting into float will work properly

import sys
#define a list
l = []
#read from standard input
for line in sys.stdin:
    #print(line)
    #get the last item from each line we read from the stdin
    s = line.split(' ')[-1]
    #print (s)
    #remove comma if any
    s = s.replace(',', '')
    #if s contains CR, it is credit return
    #cr = s.endswith('CR')  this dont work bcos our s is just one word? 
    #print('printing s[-3:]')
    #print (s[-3:])
    # it is so important to add \n   so much time wasted trouble shooting this
    if (s[-3:] == 'CR\n'):
      #print ("detected CR")
      #remove last 3 characters CR and \n 
      s = s[:-3]
      #cast it to float
      s = float(s)
      #make it negative
      s = 0 - s
    else:
      #cast it to float
      s = float(s)
    #append it to the list
    l.append(s)
print("\nTotal: ")    
print(sum(l))
print("\n") 