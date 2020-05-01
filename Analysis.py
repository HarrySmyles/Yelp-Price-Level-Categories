"""The Goal of this project is to predict the success (rating and popularity)
of a business if franchised in another city.  It will utilize predicitive
analytics by training from businesses of high popularity
(whether good or bad rating) in a specific city and determine popularity of
input business."""

import json
file = 'business.json'

with open(file, 'r', encoding='utf8', errors='ignore') as f:
    data = json.loads("[" +
        f.read().replace("}\n{", "},\n{") + "]")
    print(data[0])