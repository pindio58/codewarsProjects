def disemvowel(string):
    for letter in string:
        if letter.lower() in ['a','e','i','o','u']:
            string=string.replace(letter,'')
    return string
    
print(disemvowel("This website is for losers LOL!"))