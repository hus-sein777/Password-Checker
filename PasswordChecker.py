password = input("Enter a password: ")
score = 0
if len(password) >=8:
    score = score + 1

if any(c.isdigit() for c in password):
    score = score + 1

if any(c.isupper() for c in password):
    score = score + 1

if any(c.islower() for c in password):
    score = score + 1

if score == 4:
    print ("Strong password")
else:
    print ("Weak Password")
print("Score:", score)