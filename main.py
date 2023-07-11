import requests

api_key = "fc6195987e514b00b98c9e0ba31eef7a"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-11&sortBy=publishedAt&apiKey=" \
      "fc6195987e514b00b98c9e0ba31eef7a"

request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
      print(article["title"])
      print(article["description"])