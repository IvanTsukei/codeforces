user_input = input()
uppercase, lowercase = sum(1 for x in user_input if x.isupper()), sum(1 for x in user_input if x.islower())
if uppercase == lowercase or uppercase < lowercase: print(user_input.lower())
else: print(user_input.upper())
