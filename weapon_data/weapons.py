base_path = "../weapon_data/text_files/"

file = open(base_path + "weapons.txt", "r")
temp = file.readlines()

weapons = [line.strip() for line in temp]
temp = []

file = open(base_path + "barrel.txt", "r")
temp = file.readlines()

barrels = [line.strip() for line in temp]
temp = []

file = open(base_path + "muzzle.txt", "r")
temp = file.readlines()

muzzles = [line.strip() for line in temp]
temp = []

file = open(base_path + "ammo.txt", "r")
temp = file.readlines()

ammo = [line.strip() for line in temp]
temp = []

file = open(base_path + "laser.txt", "r")
temp = file.readlines()

lasers = [line.strip() for line in temp]
temp = []

file = open(base_path + "magazine.txt", "r")
temp = file.readlines()

magazines = [line.strip() for line in temp]
temp = []

file = open(base_path + "rear_grip.txt", "r")
temp = file.readlines()

rear_grips = [line.strip() for line in temp]
temp = []

file = open(base_path + "stock.txt", "r")
temp = file.readlines()

stocks = [line.strip() for line in temp]
temp = []

file = open(base_path + "optic.txt", "r")
temp = file.readlines()

optics = [line.strip() for line in temp]
temp = []

file = open(base_path + "underbarrel.txt", "r")
temp = file.readlines()

underbarrels = [line.strip() for line in temp]

attachments = {
    "barrels": barrels,
    "muzzles": muzzles,
    "rear_grips": rear_grips,
    "underbarrels": underbarrels,
    "optics": optics,
    "ammo": ammo,
    "magazines": magazines,
    "stocks": stocks,
    "lasers": lasers
}
