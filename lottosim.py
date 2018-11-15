#A simple exercise in the futility of matching sets of random numbers (much like the lottery). 
import random


tickets = 10000000  #The number of times to play
wins = 0            #The number of games you've won
winnum = random.sample(range(0, 75), 5)  #Generate your winning array of numbers
print "The winning number is: %s" % winnum

print "Matching %s against %s tickets......." % (winnum, tickets)

while tickets > 0:
    ticket = random.sample(range(0, 75), 5) #Creates a ticket number
    if ticket == winnum: #Matches ticket against winning number
        wins += 1 #
        tickets -= 1
    else:
        tickets -= 1
    


print "There were %s matches" % wins   #Report the number of wins
