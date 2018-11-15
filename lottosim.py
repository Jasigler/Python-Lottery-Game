#A simple exercise in the futility of the lotter
import random


tickets = 10000000
wins = 0
winnum = random.sample(range(0, 75), 5)
print "The winning number is: %s" % winnum

print "Matching %s against %s tickets......." % (winnum, tickets)

while tickets > 0:
    ticket = random.sample(range(0, 75), 5)
    if ticket == winnum:
        wins += 1
        tickets -= 1
    else:
        tickets -= 1
    


print "There were %s matches" % wins
