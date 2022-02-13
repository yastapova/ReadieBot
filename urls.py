"""Take user input and turns it into search links."""

import re

supported_sites = ["gr", "sg"]

names = {
    "gr": "Goodreads",
    "sg": "StoryGraph"
}

url_prefixes = {
    "gr": "https://www.goodreads.com/search?q=",
    "sg": "https://app.thestorygraph.com/browse?search_term="
}

url_joins = {
    "gr": "+",
    "sg": "+"
}


def create_search_url(terms:str, sites:list=supported_sites):
    """Creates a search url for the given sites."""
    terms = terms.split()
    results = dict()

    for site in sites:
        url = url_prefixes[site] + url_joins[site].join(terms)
        results[site] = url
    
    return results


def clean_input(text:str):
    """Cleans user input and identifies search terms."""
    matches = re.findall(r">([^>]+)<", text)
    matches = [m.strip() for m in matches if m.strip() != ""]
    
    return matches


def iterate_search(search_terms:list):
    results = dict()

    for t in search_terms:
        results[t] = create_search_url(t)

    return results


def pretty_msg(search_results:dict):

    if len(search_results) == 0:
        msg = "Sorry, I wasn't able to read any search terms in your request! Please try again."
        return msg
    else:
        msg = "I think I found something, here you go!\n"

    for terms, result in search_results.items():
        msg += "\nLooking for: '" + terms + "'"
        
        if len(result) == 0:
            msg +="\nSorry, I couldn't do anything for this!\n"
            continue

        for site, url in result.items():
            msg += "\nSearch on " + names[site] + ": " + url
        
        msg += "\n"
    
    msg += "\nEnjoy!"
    return msg


if __name__ == "__main__":
    search_terms = input("Enter book title and/or author name: ")
    search_terms = clean_input(search_terms)

    results = iterate_search(search_terms)
    print(pretty_msg(results))
