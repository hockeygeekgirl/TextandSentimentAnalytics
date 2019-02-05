# This code example uses Azure Cognitive Service Text Analytics to analyze positive vs negative sentiment for a string of text
# This is very useful for something like determining if reviews are positive or negative
# Check out the Quickstart on Docs.Microsoft.Com https://docs.microsoft.com/en-us/azure/cognitive-services/Text-Analytics/quickstarts/python
# this code assumes you have created a Text Analytics service on Azure
# you will need to replace teh subscription key and the text Analytics base url with values for your own Text Analytics service


#Import the requests library to simplify sending the HTTP request to the text analytics service
import requests

#Set the subscription key and text_analytics_base_url to the key and url from the text analytics Cognitive Service you create
subscription_key = "3eeb229c488941a384c697adc22295df"
text_analytics_base_url = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"

#Text Analytics can perform different tasks such as key phrase extraction and language detection
#We want to analyze sentiment so modify the URL to call sentiment
sentiment_api_url = text_analytics_base_url + "sentiment"

#Create a JSON string containing the text to analyze
#The text shown here are reviews from Trip Advisor of Cathedral Notre Dame in Montreal, Quebec, Canada
documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'Fascinating building. Churches aren’t normally my thing. This one, however, is an architectural marvel, ' \
    + 'well worth the price of admission and the time to take the tour. We are planning to go to a service and listen to the organ and choir. 1700 pipes in the organ. Unreal.' \
      + 'The craftsmanship of the whole building had to be seen to be appreciated.'},
  {'id': '2', 'language': 'en', 'text': 'When in Montréal you can’t miss this iconic landmark and must pay a visit. ' \
    + 'Cost is $8 per adult admission but well worth the price. We spent about an hour exploring the church and marveling ' \
      + 'at the intricate wood carvings, painted ceilings and many stained glass windows. Even if you’re not Catholic,' \
        + 'or religious at all, this building is incredible in its own right'},  
  {'id': '3', 'language': 'fr', 'text': 'déception c est interdit d entrée sans payé lorsque j y suis allée j étais en tres grande ' \
    + 'difficulté et en pleure et ont me refuse l acces si je paye pas pour entrée et me mettre a genoux pour une prière ' \
      + 'c est un endroit magnifique chez nous pourquoi devoir payé pour y avoir acces'},  
  {'id': '4', 'language': 'fr', 'text': 'Vraiment une très belle endroit à voir ... l’architecture et Le jeux de lumière WoW!!!' \
    + 'Un trésors du patrimoine religieux du Québec'},
  {'id': '5', 'language': 'fr', 'text': 'Il est absolument révoltant de faire payer l''entrée d''un lieu de culte !!' \
    + 'De tous mes voyages, je n''avais encore jamais vu ça, hormis le Vatican mais la basilique de Montréal ne peut tout ' \
      + 'de même pas s,y comparer.....Scandaleux !'}
]}

#Set up the headers and parameters for your HTTP Post to call the text analytics API
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
#Print the raw JSON returned by the API call
print("JSON returned by API Call \n")
print(sentiments)


print("\n Original text analyzed \n")
#Print out the text you are analyzing for display purposes
for doc in documents["documents"]:
  print(str(doc["id"]) + " " + str(doc["language"]) + ": " + str(doc["text"]))

print("\n Summary of results \n ")
print("")
#Print out the sentiment analysis results for the text analyzed
for document in sentiments["documents"]:
  print (str(document["id"]) +": " + str(document["score"]))
input()

#Sample JSON Output for sentiment anlaysis
#The closer to 1.0 the more positive the sentiment
# {'documents': 
# [{'id': '1', 'score': 0.9283617734909058}, 
# {'id': '2', 'score': 0.8887353539466858}, 
# {'id': '3', 'score': 0.3214285671710968}, 
# {'id': '4', 'score': 0.9166666865348816}, 
# {'id': '5', 'score': 0.2781077027320862}], 
# 'errors': []}
