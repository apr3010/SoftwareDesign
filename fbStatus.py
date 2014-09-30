# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 08:32:09 2014

@author: abigail
"""

import time
start = time.time()

from pattern.web import Facebook, NEWS, SEARCH, FRIENDS #imports data from Facebook

fb = Facebook(license='CAAEuAis8fUgBALDf0mJZAQrXiOCN01f3DmCoz9vtGmpgt7qYtMeIDwDRC9yPSxZBFg53HPLd9hVQuU6YmWvk0HDYIayKla2RTgIkk50dbsENw6n9KvLZCqwUWG2PrvCXy8fp2KHZCcKYUefAFO4CsTufwlWPmSzo1Pm9e5ywmWdRxaSBS5e5')
me = fb.profile()
#orint me #check to see if fb was printing my info

my_friends = fb.search(me['id'], type=FRIENDS, count=100) #list of my friends ids

result_ids = []
for friend in my_friends:
    result_ids = friend.id.encode('utf-8')
    print result_ids #prints all ids of my friends

#result_ids = [friend.id.encode('utf-8') for friend in my_friends] #condensed version of code above

    friend_news = fb.search(friend.id, type=NEWS, count=100) #finds the newsfeeds of all my friends
    for news in friend_news:
        if 'listed' in news.text or 'BIRTHDAY' in news.text or 'Birthday' in news.text or 'birthday' in news.text or 'invited' in news.text or 'updated' in news.text or 'likes' in news.text or 'shared' in news.text or 'commented' in news.text or 'event' in news.text or 'tagged' in news.text or 'timeline' in news.text or 'changed' in news.text or 'added' in news.text:
# or news.author != friend 
            print " "
            # if any of the words appear, print nothing
        else:            
            News = news.text.encode('utf-8')
            results = (News, news.author[1])
            print results
            # otherwise, it prints mainly their statuses
    if start+30<time.time():
        break
        # after some time, stop the code and move to word_counter
word_counter = {}
words = results[1].split #split statuses into lists of strings
for text in words:
    if text in results:
        word_counter[text] += 1 #adds 1 every time the word is repeated
    else:
        word_counter[text] = 1
    
    pop_words = sorted(word_counter, key = word_counter.get, reverse = True) #calculates the most popular words
    
    top_5 = pop_words[:5] 
    print top_5 #only prints the top 5 words
