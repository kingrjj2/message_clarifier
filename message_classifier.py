

p_words = ["brilliant", "awesome", "smart"]

n_words = ["stupid", "dork", "dumb"]

UserMessage = input("Type a message!").lower()

pwc = 0
nwc = 0

for word in UserMessage.split() :
    if word in p_words:
        pwc += 1
    elif word in n_words:
        nwc += 1


if pwc > nwc :
    print("message positive")
elif nwc > pwc :
    print("message negative")
else: print("message neutral")
