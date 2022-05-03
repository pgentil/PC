from unicodedata import name


dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf','H': 'Hotel', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

def natoTranslate(string: str) -> str:
    """Function that converts a message into a NATO encrypted message
    Arguments:
    
    string -- message that will be converted into NATO encrypted message
    """
    new_message = []
    for i in string:
        if i.upper() not in dictionary.keys():
            new_message.append(i.upper())
        else:
            new_message.append(dictionary[i.upper()])
    return " ".join(new_message)

if __name__ == "__main__":
    print(natoTranslate("Hello World!"))