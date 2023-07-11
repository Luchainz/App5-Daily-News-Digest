import requests
from send_email import send_email

api_key = "fc6195987e514b00b98c9e0ba31eef7a"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-11&sortBy=publishedAt&apiKey=" \
      "fc6195987e514b00b98c9e0ba31eef7a"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
      if article["title"] is not None:
            body = body + article["title"] + "\n" + article['description'] + 2*"\n"

body = body.encode("utf=8")
send_email(message=body)

