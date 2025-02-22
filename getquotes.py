#!/usr/bin/env python3
import requests

response = requests.get( "https://www.azquotes.com/top_quotes.html?p=2" )
print(vars(response))
