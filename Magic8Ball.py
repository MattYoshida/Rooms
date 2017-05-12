import random

answers = ["It is certain", "Go away, I do not wish to answer at this time!", "Without a doubt", "Ask Again Later", "Better not tell you now", "Dont count on it", "Outlook not so good"]

question = raw_input("Hi im the Magic 8 Ball, ask me a question >> ")

rand = random.randint(0,len(answers)-1)
print answers[rand]
