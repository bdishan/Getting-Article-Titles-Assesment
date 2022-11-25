import requests
import json


def getJsonFromPage(pageNumber):
    url = "https://jsonmock.hackerrank.com/api/articles"

    querystring = {"page": str(pageNumber)}

    result = requests.get(url, params=querystring)

    responseData = json.loads(result.text)
    return responseData


responseData = getJsonFromPage(1)
totalArticles = responseData['total']
totalPages = responseData['total_pages']
# data = responseData['data']

articleNameDict = {}


def buildDict(data):
    for article in data:
        if article['num_comments'] and (article['title'] or article['story_title']):
            if article['title']:
                # print(str(article['num_comments']) + " : " + str(article['title']))
                articleNameDict.update(
                    {article['title'].lstrip('\“'): article['num_comments']})

            elif article['story_title']:
                # print(str(article['num_comments']) +
                #       " : " + str(article['story_title']))
                articleNameDict.update(
                    {article['story_title']: article['num_comments']})


for i in range(totalPages, 0, -1):
    buildDict(responseData['data'])
    responseData = getJsonFromPage(i)

# ? Sorting dictionary by value (number of comments) first in lambda and then by key (title)
# print(sorted(articleNameDict.items(),
#       key=lambda v: (v[1], v[0]), reverse=True))

n = int(input("\nEnter the number of titles you want to see: "))
print("\n")

topArticleTitles = []

for key, value in sorted(articleNameDict.items(), key=lambda v: (v[1], v[0]), reverse=True):
    if len(topArticleTitles) <= n:
        topArticleTitles.append(key)
        print(key)
        print("\n")

# ! topArticleTitles is list to be returned
# print(topArticleTitles)
