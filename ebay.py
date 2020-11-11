import requests
import time
import bs4
from bs4 import BeautifulSoup

#computer case
#download first 10 webpage results for a search term of my choice
keyword = 'computer+case'
#page_num = 
#url = 'https://raw.githubusercontent.com/mikeizbicki/cmc-csci040/2020fall/README.md'
#url = 'https://raw.githubusercontent.com/mikeizbicki/cmc-csci040/2020fall/READ'
#url = 'https://github.com/mikeizbicki/cmc-csci040/blob/2020fall/READ'
#url = 'githubasdhgvhjgvjgjgccjvcjcj.com/mikeizbicki/cmc-csci040/blob/2020fall/READ'
#url = 'https://github.com/ytdl-org/youtube-dl/'
#url = 'https://www.reddit.com/r/csci040temp/.json'
#url = 'https://izbicki.me'
# reddit can temporarily ban people based on their "user agent"
# the user agent is like the "name" of your web browser

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
results = []
for i in range(10):
    try:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword+'&_sacat=0&_pgn='+ str(i+1)
        #r = requests.get(url)
        r = requests.get(url, headers=headers)
        r.status_code       # debugging information
        r.text              # contains the actual text of the webpage; 

        print('r.status_code=',r.status_code)
        #print('r.text=',r.text[:20])

        if r.status_code==200:
            with open('webpage.html','wt') as f:
                f.write(r.text)

            soup = BeautifulSoup(r.text, 'html.parser')
            boxes = soup.select('.clearfix.s-item__info')
            for box in boxes:
                print('===========')
                result = {}
                names = box.select('.s-item__title')
                for name in names:
                    #print('name=', name.text)
                    result['name']= name.text
                prices = box.select('.s-item__price')
                for price in prices:
                    #print('prices=',price.text)
                    result['price']= price.text
                statuses = box.select('.SECONDARY_INFO') 
                for status in statuses:
                    #print('status=', status.text)
                    result['status']= status.text
                print('results loop'+str(i)+'=', result)
                results.append(result)
            print(len(results))
            '''
            a_tags = soup.select('a')
            for a_tag in a_tags:
                print('a_tag=',a_tag)
            '''
            '''
            if 'izbicki' in r.text.lower():
                print('contains izbicki')
            else:
                print('does not contain izbicki')
            # know that r.text contains the webpage's information
            '''
        else:
            if r.status_code==429: # try again later
                time.sleep(500)
                r = requests.get(url)
            # handle whatever bad thing happened
        # if r.status_code == 200, then everything worked correctly
        # every other status code means something "bad" happened

    except requests.exceptions.ConnectionError:
        print('bad url, url=',url)

    except requests.exceptions.InvalidSchema:
        print('invalid schema in url, url=',url)

    except requests.exceptions.MissingSchema:
        print('the url needs a schema, url=',url)

# use bs4 to extract al litems returned in the search results


#creates a python list of extracted items, where each entry in the list is a dictionary with 3 keys
#name
# price
#status, brand new, refurbished, pre-owned etc.
#save the list as a json file named items.json



# upload everything to github with my python items.json readme
import json
j = json.dumps(results)
with open ('items.json', 'w') as f:
    f.write(j)
print('j=', j)