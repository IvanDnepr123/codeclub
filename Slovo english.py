import random
import re
year = 1
vz = ["And you?", "Yes!", "No!", "You're so annoying", "I'm not interesting in it.", "Let's go!", "Not very", "Not right it.", "HAHAHAhaha...!", "Not funny", "This is amazing!", "You need it!.", "No way!!", "Maybe", "Oh yeah!"]
a = ["I'm so cute", "I don't say it", "I don't know", "Me also!", "I am happy", "Really?", "I don't believe to you!", "Are you serious?",
     "Yeah, I am!", "It is delisious!", "I haven't nothing to say!", "I'm listerning to you", "Oups...!",
     "Not Possible!", "Who are you?", "Everything!", "You are smart", "Mhhhhmhh..", "What?",
     "Who?", "Are you happy?", "I see!", "Sorry!"]
print("Good day! Welcome to our program: SmartInteligence")
print("Version 2.3.1")
tvoje_slovo = input("Write something here:")
while True:
    reply_a = random.choice(a)
    reply_vz = random.choice(vz)
    if "?" in tvoje_slovo:
        print(reply_vz)
        a.append(tvoje_slovo)
    elif "YOUR AGE" in tvoje_slovo.upper() or "OLD ARE YOU" in tvoje_slovo.upper() or "HOW OLD ARE YOU" in tvoje_slovo.upper():
        print("I'm ", year, " years old.")
    elif "Who made you" in tvoje_slovo.lower() or "your creator" in tvoje_slovo.lower() or "who write you" in tvoje_slovo.lower() or "your writer" in tvoje_slovo.lower() or "made you" in tvoje_slovo.lower():
        print("My creator is Ivan Romaniuta!")
    elif "shit" in tvoje_slovo.lower() or "stupid" in tvoje_slovo.lower() or "wtf" in tvoje_slovo.lower() or "dumb" in tvoje_slovo.lower() or "debil" in tvoje_slovo.lower() or "stupit" in tvoje_slovo.lower():
        print("Please do not use bad words!!!")
    elif "ton nom" in tvoje_slovo.lower() or "name of you" in tvoje_slovo.lower() or "your name" in tvoje_slovo.lower():
        print("My name is Kompik.")
    elif "your birth day" in tvoje_slovo.lower() or "your birthday" in tvoje_slovo.lower():
        print("My birthday is 13.02.2023.")
        a.append(tvoje_slovo)
    elif "hi" in tvoje_slovo.lower() or "hello" in tvoje_slovo.lower() or "good morning" in tvoje_slovo.lower() or "good afternoon" in tvoje_slovo.lower() or "good evening" in tvoje_slovo.lower() or "good night" in tvoje_slovo.lower():
        print("Hi! How can I help you?")
    elif "goodbye" in tvoje_slovo.lower() or "bye" in tvoje_slovo.lower():
        print("See you soon!")
    elif "how are you doing" in tvoje_slovo.lower() or "how are you" in tvoje_slovo.lower() or "ako sa mas" in tvoje_slovo.lower():
        print("I am OK!")
    elif "0" in tvoje_slovo or "1" in tvoje_slovo or "2" in tvoje_slovo or "3" in tvoje_slovo or "4" in tvoje_slovo or "5" in tvoje_slovo or "6" in tvoje_slovo or "7" in tvoje_slovo or "8" in tvoje_slovo or "9" in tvoje_slovo or "+" in tvoje_slovo or "-" in tvoje_slovo or "=" in tvoje_slovo or "*" in tvoje_slovo or "/" in tvoje_slovo:
        numbers = re.findall(r'\d+', tvoje_slovo)
        operators = re.findall(r'[+\-*/]', tvoje_slovo)

        result = float(numbers[0])
        for i in range(len(operators)):
            if operators[i] == '+':
                result += float(numbers[i + 1])
            elif operators[i] == '-':
                result -= float(numbers[i + 1])
            elif operators[i] == '*':
                result *= float(numbers[i + 1])
            elif operators[i] == '/':
                result /= float(numbers[i + 1])

        # Виводимо результат
        print("Result ", result)




    else:
        if tvoje_slovo not in a:
            a.append(tvoje_slovo)
        print(reply_a)

    tvoje_slovo = input(": ")
    year += 1