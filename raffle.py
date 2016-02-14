#!/usr/bin/env pythgn 
import sys
import random
import json
from collections import deque


def file_to_json(full_file_path):
    with open(full_file_path, 'r') as f:
        return json.loads(f.read())


def pretty_print(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


def pick_winners(entries, stock):
    random_names = deque(entries.keys())
    random.SystemRandom().shuffle(random_names)
    winners = []
    while len(random_names) > 0 and len(stock) > 0:
        name = random_names.popleft()
        entry = entries[name]
        items = []
        for choice in entry:
            in_stock = stock.get(choice, None)
            if in_stock:
                items.append(choice)
                if in_stock == 1:
                    del stock[choice]
                else:
                    stock[choice] -= 1
        if len(items) > 0:
            winners.append({name: items})
    with open("results.json", 'w') as f:
        f.write(pretty_print({"winners": winners, "remaining stock": stock}))
    return winners, stock


if __name__ == "__main__":
    entries = file_to_json(sys.argv[1])
    stock = file_to_json(sys.argv[2])
    winners, stock = pick_winners(entries, stock)
    print("Wrote to 'results.json'")
    print("Winners:", winners)
    print("Remaining stock:", stock)
