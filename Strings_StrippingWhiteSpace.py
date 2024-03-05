# Paramahansa Yogananda was my Guru's Guru
# Dan Walk
# Some Date

fname = "  Paramahansa  "
lname = "  Yogananda  "
fullname = f"{fname} {lname}"
fullnamel = f"{fname.lstrip()} {lname.lstrip()}"
fullnamer = f"{fname.rstrip()} {lname.rstrip()}"
fullnames = f"{fname.strip()} {lname.strip()}"
satsang = '"You may control a mad elephant;\nYou may shut the mouth of the bear and the tiger;\nRide the lion and play with the cobra;\nBy alchemy you may learn your livelihood;\nYou may wander through the universe incognito;\nMake vassals of the gods;\nbe ever youthful;\nYou may walk in water and live in fire;\nBut control of the mind is better and more difficult."'

print(fullname, "\t", fullnames, "\t", fullnamel, "\t", fullnamer)
print(fullnames)
print(fullnamel)
print(fullnamer)
print()
print(fullnames.title(), "once said,\n\t", satsang)
