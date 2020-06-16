import urllib.request

def longest_word(url):
    
    response =  urllib.request.urlopen(url)
    
    html = response.read().decode()
    
    words = html.split()
    
    lengt = 0
    
    wordlist = []
    
    longes = ""
    
    file = open("words")
    
    dictionary = file.readlines()
    for line in dictionary:
        wordlist += line.split()
    wordset = set(wordlist)
    for word in words:
        if word in wordset:
            if len(word) > lengt:
                lengt = len(word)
                longes = word
    return longes