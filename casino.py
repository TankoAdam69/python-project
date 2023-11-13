import random

#Coin Flip

def coin_flip():
    return random.choice(["1", "2"])

def casino(egyenleg):
    max_input = 2000

    if egyenleg <= 0 or egyenleg > max_input:
        print("Kérlek adj meg egy számot 1-től 2000-ig")
        return egyenleg

    felrakott = int(input(f"Mennyi pénzt akarsz feltenni (1-{egyenleg})? "))

    if felrakott <= 0 or felrakott > egyenleg:
        print(f"Kérlek 1 és {egyenleg} közötti számot adj meg.")
        return egyenleg

    choice = input("Fej (1) vagy írás (2) ? ").lower()

    if choice not in ["1", "2"]:
        print("Rossz választás '1' vagy '2?")
        return egyenleg

    result = coin_flip()

    if result == choice:
        print(f"Nyertél! A pénzed dupláját kaptad vissza.")
        egyenleg += felrakott
    else:
        print(f"Vesztettél...")
        egyenleg -= felrakott

    return egyenleg

egyenleg = 1000

while egyenleg > 0:
    print(f"\nEgyenleged: {egyenleg}")
    egyenleg = casino(egyenleg)

print("Nincs elég pénzed.")

#Roll the dice

kocka_kinezet = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

kocka = []
osszesKocka = 0
szam_kocka = int(input("Mennyi kockára akarsz fogadni? "))

for die in range(szam_kocka):
    kocka.append(random.randint(1, 6))

# PRINT VERTICALLY
#for die in range(szam_kocka):
#   for line in kocka_kinezet.get(kocka[die]):
#      print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in kocka:
        print(kocka_kinezet.get(die)[line], end="")
    print()

for die in kocka:
    osszesKocka += die
print(f"Összesen: {osszesKocka}")