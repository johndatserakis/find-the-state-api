from mediawiki import MediaWiki, DisambiguationError
import csv
import json
import re

wikipedia = MediaWiki()

# https://stackoverflow.com/a/37538815/8014660
def remove_text_between_parens(text):
    n = 1  # Run at least once
    while n:
        text, n = re.subn(
            r"\([^()]*\)", "", text
        )  # Remove non-nested/flat balanced parts
        text = re.sub("\s{2,}", " ", text)  ## Remove remaining extra double-space
    return text


with open("data/states.json", "r") as f:
    _states = json.load(f)

states_data = []

for state in _states:
    state_data = {}

    p = None

    try:
        p = wikipedia.page(state)
    except DisambiguationError as e:
        # In case of DisambiguationError try to look for a title with "state" in it
        for opt in e.options:
            if "state" in opt:
                p = wikipedia.page(opt)
                break

    if p is None:
        raise ValueError("No matching article")

    state_data["name"] = state
    state_data["summary"] = remove_text_between_parens(p.summary)
    state_data["link"] = p.url
    state_data["image"] = p.images[0]

    states_data.append(state_data)

if not states_data:
    raise ValueError("No states returned from API")

keys = states_data[0].keys()
with open("scripts/states.csv", "w", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(states_data)
