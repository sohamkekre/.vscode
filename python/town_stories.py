def town_stories(string):
    len_str = len(string)
    new_str = ""
    if len_str > 2:
        for i in (string):
            if i == i.upper():
                new_str += i.lower()
            else:
                new_str += i.upper()
        print(new_str)
    else:
        string.lower()
        print(string)

town_stories("An")