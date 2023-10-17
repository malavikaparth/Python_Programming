#Making an HTTP request
#pip install requests
import requests
"""
page: Current page of result
per_page : Max number of records returned per page
total : total number of records on all pages
total_pages : total number of pages with result
data : Array of objects containeng records of the reuslts """

#FINDING WHAT IS ALL IN THE DATA.
'''
{'title': 'A Message to Our Customers', 
'url': 'http://www.apple.com/customer-letter/', 
'author': 'epaga', 
'num_comments': 967, 
'story_id': None, 
'story_title': None, 
'story_url': None,  
'parent_id': None, 
'created_at': 1455698317}

'''
def topArticles(limit):
    article_data = [] #to sort title by num_comments
    for page_number in range(1, limit + 1):
        api_url =f"https://jsonmock.hackerrank.com/api/articles?page={page_number}"
        response = requests.get(api_url)
        data = response.json()["data"]
        for article in data:
                if article["title"]:
                    title = article["title"]
                elif article["story_title"]:
                    title = article["story_title"]
                else:
                    continue
                comment_count = article["num_comments"] or 0 #This 0 is added for sorting purposes. because if 0 is not present it
                                                            #will give error
                article_data.append((title,comment_count)) #storing both title and comment count as a set
        article_data.sort(key=lambda x: (-x[1], x[0])) #This is sorting this list based on the num_comments
                              #if the number of comments is same this will sort based on title alphabetically
        top_articles = [title for title, _ in article_data[:limit]]
    return top_articles

if __name__ == '__main__':
    print(topArticles(4))
#1.MAKING AN HTTP REQUEST
api_url ="https://jsonmock.hackerrank.com/api/articles?page=1"
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    for item in data:
        print(item)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
