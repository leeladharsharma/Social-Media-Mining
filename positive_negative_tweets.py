
import nltk

posWords = "/home/leeladhar/Desktop/pos.wn"
negWords = "/home/leeladhar/Desktop/neg.wn"
posTweets = "/home/leeladhar/Desktop/posTweets.txt"
negTweets = "/home/leeladhar/Desktop/negTweets.txt"

pwfile = open(posWords, 'r') #positive word file
nwfile = open(negWords, 'r') #negative word file

#print pwfile.read()

ptfile = open(posTweets, 'r') #positive tweets file
ntfile = open(negTweets, 'r') #negative tweet file

pwlist = []
nwlist = []
ptlist= []
ntlist= []

#getting file content in lists
for pw in pwfile:
    pw.replace("_", " ")
    pwlist.append(pw)

for nw in nwfile:
    nw.replace("_", " ")
    nwlist.append(nw)

for pt in ptfile:
    ptlist.append(pt)

for nt in ntfile:
    ntlist.append(nt)

print pwlist
print nwlist
print ptlist
print ntlist

pwcount=0
nwcount=0
totpwcount=0
totnwcount=0


for pt in ptlist:
    for pw in pwlist:
        if pw in pt:
            pwcount += 1
            totpwcount += 1
    for nw in nwlist:
        if nw in pt:
            totnwcount +=1

for nt in ntlist:
    for nw in nwlist:
        if nw in nt:
           nwcount += 1
           totnwcount += 1
    for pw in pwlist:
        if pw in nt:
           totpwcount +=1

numpt= len(ptlist)
numpw= len(pwlist)
numnw= len(nwlist)
numnt= len(ntlist)

print "No of positive tweets is %d" %numpt
print "No of negative tweets is %d" %numnt
print "No of positive words is %d" %numpw
print "No of negative words is %d" %numnw

print "Positive words in positive tweets is %d" %pwcount
print "Negative words in negative tweets is %d" %nwcount
print "Total positive words in both positive and negative tweets is %d" %totpwcount
print "Total negative words in both positive and negative tweets is %d" %totnwcount

