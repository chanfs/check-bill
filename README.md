Author: CHAN Fook Sheng
17 May 2020
This script will compute the total amount for your credit card bill. 
Just run it and past the bill items on the screen, press Enter and Ctrl-D and the script will read it from standard output
The script will read each line and assume the last item is the amount you paid 
It will detect credit return, e.g, 12.00CR will be treated as -12
It will also remove commas (like 1,200 will become 1200) so that casting into float will work properly
