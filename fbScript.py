# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 09:45:10 2014

@author: abigail
"""

import time # import package
start = time.time() #start keeps track of time

#import pickle

from pattern.web import Facebook, NEWS, LIKES, FRIENDS # import pattern from Facebook API

fb = Facebook(license='CAAEuAis8fUgBALDf0mJZAQrXiOCN01f3DmCoz9vtGmpgt7qYtMeIDwDRC9yPSxZBFg53HPLd9hVQuU6YmWvk0HDYIayKla2RTgIkk50dbsENw6n9KvLZCqwUWG2PrvCXy8fp2KHZCcKYUefAFO4CsTufwlWPmSzo1Pm9e5ywmWdRxaSBS5e5')
# put in my license key for Facebook
me = fb.profile() # takes information from my profile

my_friends = fb.search(me['id'], type=FRIENDS, count=100) #creates a list of my friends' ids
#print my_friends

result_ids = [friend.id.encode('utf-8') for friend in my_friends] #removed the u' from the ids
#print result_ids
word_counter = {} # created a word counter - initialized as an empty array
for friend in my_friends:
    news = fb.search(friend['id'], type=NEWS, count=100) # gets newsfeeds from all my friends
    for post in news:

        feed = post.text.lower() #made the entire newsfeed lowercase
#        print post.text.split()
#        print feed
        if post.likes > 0: #when the likes for posts is more than 0, print the post
            if 'event' in feed or 'added' in feed or 'changed' in feed or 'birthday' in feed or 'shared' in feed or 'tagged' in feed or 'updated' in feed:
                print " " #excludes all lines with these words in newsfeeds - not relevant
            else:
                print repr(post.text) #prints posts that are relevant
                print '%i likes' % post.likes #prints the number of likes that each post receives
                print [r.author for r in fb.search(post.id, type=LIKES)] #prints who likes the posts
                               
                for words in feed.split(): #split the sentences into string of words to find most common words
                    
                    if words not in word_counter: # if not added to the counter, add word to counter
#                        print words
                        word_counter[words.encode('utf-8')] = 1 

#                        print word_counter
                    else: # increases the word count if it exists in the word count already
                        word_counter[words.encode('utf-8')] += 1
#                        print word_counter
                    
                    pop_words = sorted(word_counter, key = word_counter.get, reverse = True) #sorts out all the popular words
        
                    top_5 = pop_words[:5] #takes only the top 5 popular words
#                    print top_5
                    
        if time.time()>start+50: # after a period of time, print the word count for each word
            for items in word_counter.items(): # organizes the words and their counts
#                print k, v
                wordCount = sorted(word_counter.items(), key = lambda item: item[1], reverse = True)
                print wordCount
            
            


