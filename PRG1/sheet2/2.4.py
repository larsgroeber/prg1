score = int(input("Please enter your hobby score: ")) % 256

if score < 0:
    print("ERROR")
    exit(-1)
if score == 0:
    print("Keine Hobbies")
    exit(0)

hobby_value = "{0:08b}".format(score)

HOBBIES = ["Schwimmen", "Brettspiele", "Angeln", "Kochen", "Laufen", "Fussball spielen", "Klavier spielen", "Naehen"]
HOBBIES.reverse()

hobbies = []

for index, number in enumerate(hobby_value):
    if number == "1":
        hobbies.append(HOBBIES[index])

hobbies.reverse()
print("\n".join(hobbies))
