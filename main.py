import requests
from send_email import send_email

topic = "tesla"

api_key = "fc6195987e514b00b98c9e0ba31eef7a"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=fc6195987e514b00b98c9e0ba31eef7a&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
                + "\n" + body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

