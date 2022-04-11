def anagrams(word, words):
    
    sort = sorted(word)
    
    return[i for i in words if sort == sorted(i)]
