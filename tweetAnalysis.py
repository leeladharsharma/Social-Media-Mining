
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

def analysis(list):

    charfreq=[]
    wordfreq=[]
    lex_div=[]

    for tweet in list:
        characters = len(tweet)
        charfreq.append(characters)

        words = tweet.split(" ")
        ltwords = len(words)
        wordfreq.append(ltwords)

        ld = len(set(words)) / ltwords
        lex_div.append(ld)

    print "char frequency is %s: " % charfreq
    print "word frequency is %s" % wordfreq
    print "Lexical diversity is %s: " %lex_div

print "Statistics for postweets\n",analysis(ptlist)
print "Statistics for negtweets\n", analysis(ntlist)
