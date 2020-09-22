i=input()
thriller=["dark","money heist","war","mindhunter","parasite","inception","insidious","interstellar","prison break","jack ryan"]
comedy=["friends","the big bang theory","3 idiots","brooklyn 99","how i met your mother","rick and morty","the office","space force"]

if i.lower() in thriller :
	print("It is a thriller")
elif i.lower() in comedy :
	print("It is a comedy")
else :
	print("It's neither thriller nor comedy")  
