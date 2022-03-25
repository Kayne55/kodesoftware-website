import operator
import re
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'message': 'Welcome to the Word Counter'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlistnochars = re.sub('[!@#$%^&*()_+-={}\[\];\'\\\|~`<>?,./]', '', fulltext)
    wordlist = wordlistnochars.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #Add to Dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'wordlistnochars':wordlistnochars, 'count':len(wordlist), 'sortedwords':sortedwords})