print("Hello World!")

"""
1. Iterate over array of states
2. For each state, call an API endpoint
3. Retrive the data and store it in a new array.
  - The values are name, summary, link
4. Print result
"""

import json
import wikipedia
import csv
import re

# https://stackoverflow.com/a/37538815/8014660
def remove_text_between_parens(text):
    n = 1  # Run at least once
    while n:
        text, n = re.subn(
            r"\([^()]*\)", "", text
        )  # Remove non-nested/flat balanced parts
        text = re.sub("\s{2,}", " ", text) ## Remove remaining extra double-space
    return text


with open("data/states.json", "r") as f:
    _states = json.load(f)

states_data = []

for state in _states:
    state_data = {}

    article = wikipedia.page(state)
    state_data["name"] = state
    state_data["summary"] = remove_text_between_parens(article.summary)
    state_data["link"] = article.url
    state_data["image"] = article.images[0]

    states_data.append(state_data)

if not states_data:
    raise ValueError("No states returned from API")

keys = states_data[0].keys()
with open("scripts/states.csv", "w", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(states_data)
