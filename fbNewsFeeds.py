# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:13:12 2014

@author: abigail
"""
import time
start = time.time()

#def newsFeeds():

from pattern.web import Facebook, NEWS, SEARCH, FRIENDS

fb = Facebook(license='CAAEuAis8fUgBALDf0mJZAQrXiOCN01f3DmCoz9vtGmpgt7qYtMeIDwDRC9yPSxZBFg53HPLd9hVQuU6YmWvk0HDYIayKla2RTgIkk50dbsENw6n9KvLZCqwUWG2PrvCXy8fp2KHZCcKYUefAFO4CsTufwlWPmSzo1Pm9e5ywmWdRxaSBS5e5')
me = fb.profile()
#print me

my_friends = fb.search(me['id'], type=FRIENDS, count=100)

#result_ids = ['51903148', '500224184', '500331038', '500491857', '500915419', '501539308', '502215901', '503117562', '503482064', '503525848', '503598716', '503612001', '503795590', '503946675', '504570954', '505155592', '505219069', '505301520', '507739090', '509548423', '510268573', '510983529', '512858974', '513391195', '514153226', '514499433', '515474180', '517715547', '518082669', '518624114', '520069392', '521425712', '523243610', '525918735', '527123221', '527377645', '528835234', '529225509', '532865317', '533147424', '533513254', '534142834', '534892159', '535450021', '537276306', '537737982', '537960899', '538241303', '538251432', '538689702', '538971524', '539610327', '541816476', '541960760', '542538547', '544130598', '547351423', '547955592', '549901320', '550923436', '552073454', '552669116', '553271470', '557729366', '559224810', '560881275', '562042262', '563975426', '565023020', '565146441', '566414817', '566432568', '567325493', '567834534', '567849387', '568330261', '569550655', '573626897', '575231316', '575742532', '576515585', '576557656', '577032027', '579159177', '580981060', '581021945', '581730919', '582322564', '585321930', '585405968', '587953032', '591929898', '592249400', '592294158', '592731069', '593550706', '595397164', '595510549', '598737673']
result_ids = [friend.id.encode('utf-8') for friend in my_friends] #condensed version of code shown below

#result_ids = []
#for friend in my_friends:
#    result_ids = friend.id.encode('utf-8')
#    print result_ids

#print result_ids
print len(my_friends)

for friend in my_friends:
    friend_news = fb.search(friend.id, type=NEWS, count=100)

    for news in friend_news:
#        key_list = ['listed','BIRTHDAY','Birthday','birthday', 'invited', 'updated','event','tagged', 'timeline','changed', 'added', 'likes', 'shared', 'commented']        
        if 'listed' not in news.text or 'BIRTHDAY' not in news.text or 'Birthday' not in news.text or 'birthday' not in news.text or 'invited' not in news.text or 'updated' not in news.text or 'likes' not in news.text or 'shared' not in news.text or 'commented' not in news.text or 'event' not in news.text or 'tagged' not in news.text or 'timeline' not in news.text or 'changed' not in news.text or 'added' not in news.text or news.author != friend:
#        for keywords in key_list:
#            if any (keywords) in news.text == 0:
            News = news.text.encode('utf-8')
            results = (News, news.author[1])
            print results
#        else:
            
#print len(key_list)        

                
    if start+50<time.time():
        break

word_counter = {}
for text in news:
    News = news.text.encode('utf-8')
    if text in News:
        word_counter[text] += 1
    else:
        word_counter[text] = 1
    
    pop_words = sorted(word_counter, key = word_counter.get, reverse = True)
    
    top_5 = pop_words[:5]  
    print top_5
#
#           
##likes, shared, commented, event, tagged, invited, updated, timeline, changed, news.author == friend