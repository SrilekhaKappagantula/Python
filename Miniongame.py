def minion_game(string):
    stuart_words=list(input("Stuart: Enter your words:").split())
    kevin_words=list(input("Kevin: Enter your words:").split())
    vowels="aeiouAEIOU"
    stuart_count=0
    kevin_count=0
    for word in stuart_words:
        if word[0] not in vowels:
            if word in string:
                stuart_count+=string.count(word)
            else:
                stuart_count
    for word in kevin_words:
        if word[0] in vowels:
            if word in string:
                kevin_count+=string.count(word)
            else:
                kevin_count
    if stuart_count>kevin_count:
        print("Stuart",stuart_count)
    elif stuart_count<kevin_count:
        print("Kevin",kevin_count)
    else:
        print("Both are equal",stuart_count)
minion_game("banana")