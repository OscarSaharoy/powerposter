#!/usr/bin/env python3
import requests
import bs4
import json

quotes = []

for page in range(1, 11):
    response = requests.get(
        f"https://www.azquotes.com/top_quotes.html?p={page}"
    )
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    for q in soup.select( ".list-quotes .wrap-block" ):
        quote = q.select_one( "a.title" ).string
        author = q.select_one( "div.author a" ).string
        quotes.append( {
            "quote": quote,
            "author": author,
        } )

print( json.dumps(quotes, indent=4) )


