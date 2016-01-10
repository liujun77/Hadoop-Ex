#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

prev_show          = "  "                #initialize previous word  to blank string
abc_found          =False
line_cnt           = 0  #count input lines
total              = 0
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split(' ')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    #note: for simple debugging use print statements, ie:  
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    #-----------------------------------------------------
    # Check if its a new word and not the first line 
    #   (b/c for the first line the previous word is not applicable)
    #   if so then print out list of dates and counts
    #----------------------------------------------------
    
    

    if curr_show != prev_show:

        # -----------------------     
	#now write out the join result, but not for the first line input
        # -----------------------
        if line_cnt>1:
	    if abc_found:
	        print('{0} {1}'.format(prev_show,total))
            #now reset list
            total = 0
            abc_found = False
        prev_show         =curr_show  #set up previous word for the next set of input lines

	
    if value_in == 'ABC':
        abc_found = True
    else:
        total = total + int(value_in)


# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------
if abc_found:
    print('{0} {1}'.format(curr_show,total))
	
