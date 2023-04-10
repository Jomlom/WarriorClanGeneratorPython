# imports

import time
import random
from random import randint

# clan generating function


def randomClan():

    # lists

    possibleClans = [
        "Dark",
        "Fog",
        "Light",
        "Snow",
        "Bush",
        "Moss",
        "Tree",
        "Swift",
        "Willow",
        "Forest",
        "Mountain",
        "Lake",
        "Blaze",
        "Breeze",
        "Bright",
        "Clear",
        "Dawn",
        "Drizzle",
        "Ice",
        "Fade",
        "Glow",
        "Rise",
        "Shine",
        "Torrent",
        "Current",
        "Berry",
        "Ash",
        "Bone",
        "Bleak",
        "Dark",
        "Dusk",
        "Fallen",
        "Mist",
        "Moon",
        "Night",
        "Sharp",
        "Slash",
        "Dead",
        "Smoke",
        "Vine",
        "Tree",
        "Cold",
        "Earth",
        "Fire",
        "Fog",
        "Freeze",
        "Frozen",
        "Marsh",
        "Rain",
        "Rock",
        "Slush",
        "Storm",
        "Hollow",
        "Echo",
        "Hidden",
        "Stray",
        "Thorn",
        "Blizzard",
        "Mud",
        "Swamp",
        "Dusk",
        "Shade",
        "Sun",
        "Meadow",
        "Stream",
        "Tundra",
        "Taiga",
        "Lava",
        "Volcano",
        "Barren",
        "Farm",
        "Cliff",
        "Sand",
        "Moor",
        "Field",
        "Shore",
        "Cove",
        "Waste",
        "Cave",
        "Snow",
        "Ridge",
        "Flood",
        "Bog",
        "Bush",
    ]
    possibleFirstHalfNames = [
        "Mint",
        "Beetroot",
        "Pea",
        "Sprout",
        "Onion",
        "Celery",
        "Pumpkin",
        "Melon",
        "Lemon",
        "Lime",
        "Apricot",
        "Quince",
        "Teasel",
        "Brindle",
        "Ant",
        "Beech",
        "Dark",
        "Smooth",
        "Speckle",
        "Muddle",
        "Forest",
        "Mushroom",
        "Fungi",
        "Laurel",
        "Murk",
        "Wax",
        "Russet",
        "Jagged",
        "Hazel",
        "Deep",
        "Big",
        "Swift",
        "Raven",
        "Bee",
        "Moss",
        "Fox",
        "Mouse",
        "Acorn",
        "Fire",
        "Flame",
        "Clear",
        "Glow",
        "Fallen",
        "Murky",
        "Ash",
        "Soot",
        "Rain",
        "Snow",
        "Marsh",
        "Nettle",
        "Sap",
        "Fern",
        "Berry",
        "Hazel",
        "Orchid",
        "Mallow",
        "Fog",
        "Twig",
        "Heather",
        "Chesnut",
        "Rose",
        "Wolf",
        "Robin",
        "Jay",
        "Thrush",
        "Ivy",
        "Feather",
        "Bear",
        "Cotton",
        "Adder",
        "Skull",
        "Bone",
        "Ant",
        "Apple",
        "Peach",
        "Ice",
        "Badger",
        "Squirrel",
        "Spider",
        "Dust",
        "Daisy",
        "Beetle",
        "Shell",
        "Blaze",
        "Little",
        "Log",
        "Bounce",
        "Bracken",
        "Briar",
        "Bubble",
        "Bush",
        "Icicle",
        "Shade",
        "Sharp",
        "Nut",
        "Wasp",
        "Stag",
        "Dream",
        "Sweet",
        "Deer",
        "Cow",
        "Milk",
        "Puddle",
        "Lost",
        "Whisper",
        "Flutter",
        "Venom",
        "Poison",
        "Frog",
        "Thicket",
        "Pale",
        "Storm",
        "Lion",
        "Tiger",
        "Leopard",
        "Puma",
        "Jaguar",
        "Panther",
        "Vole",
        "Pidgeon",
        "Sparrow",
        "Starling",
        "Finch",
        "Dog",
        "Magpie",
        "Dove",
        "Wren",
        "Crow",
        "Duck",
        "Goose",
        "Swan",
        "Pollen",
        "Petal",
        "Snake",
        "Worm",
        "Beetle",
        "Otter",
        "Hedgehog",
        "Moth",
        "Beaver",
        "Vole",
        "Eagle",
        "Hawk",
        "Buzzard",
        "Hornet",
        "Seed",
        "Sprig",
        "Sun",
        "Moon",
        "Mud",
        "Rabbit",
        "Cub",
        "Owl",
        "Cold",
        "Frozen",
        "Trout",
        "Carp",
        "Pike",
        "Snail",
        "Slug",
        "Cricket",
        "Fly",
        "Bat",
        "Fern",
        "Thistle",
        "Withered",
        "Cinder",
        "Spark",
        "Hollow",
        "Torn",
        "Quail",
        "Buck",
        "Rowan",
        "Cherry",
        "Plum",
        "Honey",
        "Holly",
        "Spindle",
        "Murky",
        "Web",
        "Garlic",
        "Thyme",
        "Mint",
        "Juniper",
        "Yarrow",
        "Tansy",
        "Comfrey",
        "Sorrel",
        "Alder",
        "Birch",
        "Root",
        "Mugwort",
        "Hare",
        "Hen",
        "Egg",
        "Grass",
        "Talon",
        "Pig",
        "Meadow",
        "Cress",
        "Rock",
        "Pebble",
        "Carrot",
        "Cabbage",
        "Wild",
        "Walnut",
        "Lettuce",
        "Sleek",
        "Grape",
        "Mallow",
        "Weed",
        "Primrose",
        "Hyacinth",
        "Skunk",
        "Peony",
        "Daffodil",
        "Lavender",
        "Flax",
        "Pine",
        "Fir",
        "Raddish",
        "Sheep",
        "Stone",
        "Yew",
        "Lime",
        "Clover",
        "Gorse",
        "Reed",
        "Bug",
        "Bog",
        "Heavy",
        "Boggy",
        "Chalk",
        "Chaffinch",
        "Chiffchaff",
        "Coal",
        "Cuckoo",
        "Dunnock",
        "Kestrel",
        "Long",
        "Tall",
        "Mistle",
        "Thrush",
        "Nightingale",
        "Osprey",
        "Kite",
        "Robin",
        "Rook",
        "Starling",
        "Swallow",
        "Tawny",
        "Tree",
        "Twig",
        "Wheat",
        "Wren",
        "Shrub",
        "Jackdaw",
        "Pheasant",
        "Ladybug",
        "Bumble",
        "Cinnamon",
        "Clear",
        "Cloud",
        "Dapple",
        "Dead",
        "Doe",
        "Dew",
        "Drizzle",
        "Echo",
        "Elder",
        "Wisp",
        "Fawn",
        "Ferret",
        "Fin",
        "Flash",
        "Freckle",
        "Hail",
        "Hill",
        "Hound",
        "Jump",
        "Scratch",
        "Lake",
        "Leaf",
        "Lightning",
        "Long",
        "Small",
        "Lynx",
        "Loud",
        "Silent",
        "Minnow",
        "Maple",
        "Misty",
        "Mumble",
        "Nectar",
        "Newt",
        "Tadpole",
        "Odd",
        "Night",
        "Oat",
        "One",
        "Patch",
        "Pear",
        "Olive",
        "Pod",
        "Pounce",
        "Prickle",
        "Hay",
        "Quick",
        "Rat",
        "Rook",
        "Ripple",
        "Rush",
        "Rye",
        "Sand",
        "Sandy",
        "Scorch",
        "Shadow",
        "Thunder",
        "Wind",
        "River",
        "Shattered",
        "Shrew",
        "Slate",
        "Slight",
        "Shy",
        "Snap",
        "Spike",
        "Stream",
        "Sunny",
        "Swamp",
        "Tangle",
        "Tiny",
        "Toad",
        "Turtle",
        "Vixen",
        "Weasel",
        "Whistle",
        "Eel",
        "Heavy",
        "Horse",
        "Lizard",
        "Adder",
        "Mink",
        "Shrew",
        "Sneeze",
        "Fidget",
        "Hop",
        "Mottle",
        "Sage",
        "Chickadee",
        "Bluebell",
        "Aster",
        "Iris",
    ]
    possibleSecondHalfNames = [
        "bite",
        "burst",
        "spot",
        "beam",
        "bright",
        "sight",
        "trail",
        "freckle",
        "rush",
        "veil",
        "drift",
        "scales",
        "wing",
        "flight",
        "flake",
        "back",
        "tail",
        "claw",
        "lake",
        "heart",
        "belly",
        "face",
        "nose",
        "ear",
        "leg",
        "stripe",
        "pool",
        "wing",
        "song",
        "sting",
        "whisker",
        "gaze",
        "leaf",
        "shine",
        "flower",
        "breeze",
        "jump",
        "hop",
        "skip",
        "snap",
        "strike",
        "foot",
        "bite",
        "fang",
        "watcher",
        "catcher",
        "snarl",
        "spirit",
        "sight",
        "fall",
        "whisper",
        "whisker",
        "stalk",
        "stream",
        "puddle",
        "snow",
        "cloud",
        "meadow",
        "dusk",
        "pelt",
        "fur",
        "flight",
        "storm",
        "feather",
        "dawn",
        "shade",
        "nibble",
        "bark",
        "bee",
        "berry",
        "blaze",
        "bloom",
        "branch",
        "bright",
        "burrow",
        "bush",
        "crawl",
        "dapple",
        "eye",
        "eyes",
        "patch",
        "fern",
        "fall",
        "fang",
        "fire",
        "spark",
        "frost",
        "flower",
        "hawk",
        "ice",
        "jaw",
        "mask",
        "muzzle",
        "mouse",
        "moon",
        "pad",
        "mouse",
        "petal",
        "puddle",
        "rose",
        "ripple",
        "scratch",
        "runner",
        "fever",
        "shade",
        "shell",
        "seed",
        "sky",
        "snout",
        "speck",
        "splash",
        "stem",
        "stream",
        "strike",
        "teeth",
        "tuft",
        "whistle",
        "wing",
        "wish",
        "willow",
        "raven",
        "roar",
        "screech",
        "drop",
        "dust",
        "bush",
        "toe",
        "thorn",
        "weed",
        "water",
        "wind",
        "snow",
        "dream",
        "feather",
        "blossom",
        "throat",
        "cry",
        "dash",
        "dove",
        "freckle",
        "wish",
        "fox",
        "fly",
        "raven",
        "scorch",
        "flake",
        "fin",
        "flutter",
        "frost",
        "flash",
        "glare",
        "growl",
        "hiss",
        "glint",
        "gust",
        "haze",
        "hollow",
        "honey",
        "mud",
        "lark",
        "legs",
        "lick",
        "moon",
        "nut",
        "orchid",
        "path",
        "run",
        "runner",
        "shadow",
        "skull",
        "slash",
        "sneeze",
        "spark",
        "sprig",
        "stare",
        "stride",
        "sun",
        "tangle",
        "tear",
        "thorn",
        "thistle",
        "thicket",
        "tooth",
        "trail",
        "twist",
        "tusk",
        "tongue",
        "iris",
        "crunch",
        "valley",
        "web",
        "worm",
        "wisp",
        "whisper",
        "yowl",
        "pounce",
        "rain",
        "hound",
        "quiver",
        "shatter",
        "briar",
        "grin",
        "seeker",
        "fig",
        "bud",
        "fluff",
        "grass",
        "run",
        "chest",
        "nettle",
        "mane",
        "lily",
        "zip",
        "burst",
        "flare",
        "light",
        "crouch",
        "chirp",
        "stomp",
        "flick",
        "flow",
    ]

    currentQuirks = []
    currentNames = []

    # other values

    lenClans = len(possibleClans) - 1
    lenFirstHalfNames = len(possibleFirstHalfNames) - 1
    lenSecondHalfNames = len(possibleSecondHalfNames) - 1

    # generation

    clanName = possibleClans[randint(0, lenClans)] + "clan"

    firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
    secondName = "star"
    while firstName.lower() == secondName.lower():
        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
    leader = firstName + secondName

    while leader in currentNames:
        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = "star"
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        leader = firstName + secondName

    currentNames.append(leader)

    firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
    secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
    while firstName.lower() == secondName.lower():
        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
    deputy = firstName + secondName

    while deputy in currentNames:
        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        deputy = firstName + secondName

    currentNames.append(deputy)

    firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
    secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
    while firstName.lower() == secondName.lower():
        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
    medicineCat = firstName + secondName

    while medicineCat in currentNames:
        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        medicineCat = firstName + secondName

    currentNames.append(medicineCat)

    warriors = []
    numWarriors = randint(6, 10)
    for i in range(numWarriors):

        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        warrior = firstName + secondName

        while warrior in currentNames:
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
            while firstName.lower() == secondName.lower():
                firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
                secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
            warrior = firstName + secondName

        currentNames.append(warrior)
        warriors.append(warrior)

    apprentices = []
    numApprentices = randint(1, 4)
    for i in range(numApprentices):

        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = "paw"
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        apprentice = firstName + secondName

        while apprentice in currentNames:
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = "paw"
            while firstName.lower() == secondName.lower():
                firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            apprentice = firstName + secondName

        currentNames.append(apprentice)
        apprentices.append(apprentice)

    queens = []
    numQueens = randint(1, 3)
    for i in range(numQueens):

        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        queen = firstName + secondName

        while queen in currentNames:
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
            while firstName.lower() == secondName.lower():
                firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
                secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
            queen = firstName + secondName

        currentNames.append(queen)
        queens.append(queen)

    kits = []
    numKits = randint(1, 4)
    for i in range(numKits):

        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = "kit"
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        kit = firstName + secondName

        while kit in currentNames:
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = "kit"
            while firstName.lower() == secondName.lower():
                firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            kit = firstName + secondName

        currentNames.append(kit)
        kits.append(kit)

    elders = []
    numElders = randint(1, 3)
    for i in range(numElders):

        firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
        secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        while firstName.lower() == secondName.lower():
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
        elder = firstName + secondName

        while elder in currentNames:
            firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
            secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
            while firstName.lower() == secondName.lower():
                firstName = possibleFirstHalfNames[randint(0, lenFirstHalfNames)]
                secondName = possibleSecondHalfNames[randint(0, lenSecondHalfNames)]
            elder = firstName + secondName

        currentNames.append(elder)
        elders.append(elder)

    # putting it together

    clan = "\n\n\n\n\n\n\n" + clanName + "\n\n"
    clan = clan + "Leader: \n\n" + leader + " - " + randomCat("no", False) + "\n\n"
    clan = clan + "Deputy: \n\n" + deputy + " - " + randomCat("no", False) + "\n\n"
    clan = (
        clan
        + "Medicine Cat: \n\n"
        + medicineCat
        + " - "
        + randomCat("no", False)
        + "\n\n"
    )
    clan = clan + "Warriors: \n\n"
    for i in range(numWarriors):
        num = i - 1
        clan = clan + warriors[i] + " - " + randomCat("no", False) + "\n"
    clan = clan + "\n"
    clan = clan + "Apprentices: \n\n"
    for i in range(numApprentices):
        num = i - 1
        clan = clan + apprentices[i] + " - " + randomCat("no", False) + "\n"
    clan = clan + "\n"
    clan = clan + "Queens: \n\n"
    for i in range(numQueens):
        num = i - 1
        clan = clan + queens[i] + " - " + randomCat("female", False) + "\n"
    clan = clan + "\n"
    clan = clan + "Kits: \n\n"
    for i in range(numKits):
        num = i - 1
        clan = clan + kits[i] + " - " + randomCat("no", True) + "\n"
    clan = clan + "\n"
    clan = clan + "Elders: \n\n"
    for i in range(numElders):
        num = i - 1
        clan = clan + elders[i] + " - " + randomCat("no", False) + "\n"
    clan = clan + "\n"

    return clan

# cat generating function


def randomCat(fixedGender, isKit):

    # lists

    possibleDescriptors = [
        "persistant",
        "strange",
        "secretive",
        "bold",
        "abnormally large",
        "charasmatic",
        "stubborn",
        "creative",
        "empathetic",
        "friendly",
        "elegant",
        "compassionate",
        "humble",
        "enthusiatic",
        "ambitious",
        "intoverted",
        "adventurous",
        "admirable",
        "calm",
        "confident",
        "daring",
        "dignified",
        "dramatic",
        "energetic",
        "fair",
        "gentle",
        "kind",
        "aggresive",
        "rude",
        "protective",
        "selfless",
        "witty",
        "reserved",
        "aloof",
        "antisocial",
        "blunt",
        "brutal",
        "cowardly",
        "cruel",
        "disloyal",
        "dishonest",
        "dull",
        "fickle",
        "fiery",
        "gloomy",
        "gullible",
        "hostile",
        "ignorant",
        "hesitant",
        "insecure",
        "irritable",
        "malicious",
        "miserable",
        "odd",
        "paranoid",
        "petty",
        "silly",
        "timid",
        "weak",
        "honest",
        "lithe",
        "nimble",
        "scrawny",
        "mysterious",
        "fierce",
        "cunning",
        "alert",
        "anxious",
        "moody",
        "naughty",
        "needy",
        "likable",
        "affectionate",
        "amusing",
        "bossy",
        "caring",
        "chill",
        "pampered",
        "chubby",
        "clumsy",
        "courageous",
        "picky",
        "playful",
        "crafty",
        "protective",
        "pretty",
        "curious",
        "crazy",
        "quiet",
        "quirky",
        "devoted",
        "demanding",
        "daring",
        "rebellious",
        "entertaining",
        "faithful",
        "relaxed",
        "sensitive",
        "foolish",
        "sleepy",
        "smart",
        "fun",
        "graceful",
        "stubborn",
        "greedy",
        "handsome",
        "sweet",
        "tempermental",
        "timid",
        "tough",
        "jolly",
        "intelligent",
        "lazy",
        "laidback",
        "keen",
        "unique",
        "small",
        "tall",
        "broad-shouldered",
        "thin",
        "tiny",
        "lean",
        "muscly",
        "round",
        "well-built",
        "skinny",
        "lanky",
        "stocky",
    ]
    possiblePatterns = [
        "dappled",
        "speckled",
        "spotted tabby",
        "marbled tabby",
        "mackeral tabby",
        "classic tabby",
        "mackeral tabby",
        "classic tabby",
        "sokoke tabby",
        "oceloid tabby",
        "ticked tabby",
        "rosetted tabby",
    ]
    possibleFurColours = [
        "yellow",
        "fawn",
        "lilac",
        "cinnamon",
        "chocolate",
        "black",
        "dark grey",
        "orange",
        "red",
        "silver",
        "blue",
        "light brown",
        "brown",
        "cream",
        "dark blue",
        "warm blue",
        "light grey",
        "grey",
        "dark brown",
        "dark red",
        "ginger",
        "gold",
        "apricot",
        "dark ginger",
    ]
    possibleCommonFurDescriptors = ["short", "medium-length", "long"]
    possibleRareFurDescriptors = [
        "wavy",
        "shiny",
        "fluffy",
        "slick",
        "very short",
        "very long",
        "course",
        "silky",
        "thick",
        "unkept",
        "sleek",
        "tidy",
        "wild",
        "spiky",
        "thin",
        "scruffy",
        "soft",
        "curly",
        "glossy",
    ]
    possibleQuirks = [
        "a special connection to starclan",
        "webbed paws",
        "a whip-like tail",
        "a short muzzle",
        "scarred muzzle",
        "small paws",
        "an angular face",
        "a short tail",
        "dark eyebags",
        "long eyelashes",
        "droopy ears",
        "a square face",
        "scarred pelt",
        "scarred legs",
        "darker paws",
        "darker chest flecks",
        "a round face",
        "cheek fluff",
        "ear tufts",
        "a tufted tail",
        "rounded ears",
        "darker tipped ears",
        "curled ears",
        "a bobtail",
        "a curly tail",
        "polydactyl mutation",
        "shredded ears",
        "a nose scar",
        "a back leg scar",
        "a shoulder scar",
        "an eye scar",
        "a lip scar",
        "a long scar",
        "a scar shaped like an X",
        "scars from being struck by lightning",
        "long legs",
        "a scarred tail",
        "darker paws",
        "darker flecks",
        "a darker face",
        "a speckled nose",
        "a blind eye",
        "bad vision",
        "lots of scars",
        "a pink nose",
        "a twisted limb",
        "a back scar",
        "a nose scar",
        "wild neck fur",
        "slashed eyes",
        "ear fluff",
        "a few scars",
        "a missing eye",
        "a torn ear",
        "five toes on one foot",
        "a snaggle tooth",
        "large fangs",
        "small fangs",
        "a missing limb",
        "a broken tail",
        "a flat face",
        "folded ears",
        "a freakishly large tail",
        "a folded ear",
        "small ears",
        "tall ears",
        "crooked whiskers",
        "a scarred face",
        "a long tail",
        "long whiskers",
        "short legs",
        "a fluffy tail",
        "large paws",
        "dangerous claws",
        "a scarred throat",
        "burn scars",
        "a torn ear",
        "a bullet hole in one ear",
        "back scars",
        "a dark back stripe",
    ]
    possibleEyeColours = [
        "blue",
        "icy-blue",
        "emerald-green",
        "ruby-red",
        "olive-green",
        "brown",
        "bright blue",
        "bright green",
        "green",
        "pale yellow",
        "yellow",
        "amber",
        "orange",
        "hazel",
        "copper",
        "red",
        "turquoise",
        "gold",
        "bronze",
        "pale blue",
        "gold",
        "pale green",
        "purple-blue",
        "silver",
    ]
    possibleSpecials = [
        "seal lynx-point",
        "chocolate lynx-point",
        "cinnamon lynx-point",
        "flame lynx-point",
        "blue lynx-point",
        "lilac lynx-point",
        "fawn lynx-point",
        "cream lynx-point",
        "seal colour-point",
        "chocolate colour-point",
        "cinnamon colour-point",
        "flame colour-point",
        "blue colour-point",
        "lilac colour-point",
        "fawn colour-point",
        "cream colour-point",
        "white",
        "black and tan underbelly",
        "brown and tan underbelly",
        "black and white swirled",
        "brown and white swirled",
        "black and white brindled bicolour",
        "black and white skunk stripe",
        "cream, red and brown calico",
        "cream, orange and black calico",
        "cream, orange and brown calico",
        "cream, black and brown calico",
        "cream, blue and silver calico",
        "black smoke,",
        "brown smoke",
        "white shaded",
        "golden shaded",
        "grey shaded",
        "black and white vitilago",
        "white",
        "white, red and brown calico",
        "white, orange and black calico",
        "white, orange and brown calico",
        "white, orange and cream calico",
        "white, grey and cream calico",
        "white, cream and brown calico",
        "white, black and brown calico",
        "white, silver and grey calico",
        "white, blue and silver calico",
        "red and brown tortie",
        "orange and black tortie",
        "orange and brown tortie",
        "orange and cream tortie",
        "grey and cream tortie",
        "cream and brown tortie",
        "black and red tortie",
        "silver and dark grey tortie",
        "blue and silver tortie",
        "cream, red and brown caliby",
        "cream, orange and black caliby",
        "cream, orange and brown caliby",
        "cream, black and brown caliby",
        "cream, blue and silver caliby",
        "white",
        "white, red and brown caliby",
        "white, orange and black caliby",
        "white, orange and brown caliby",
        "white, orange and cream caliby",
        "white, grey and cream caliby",
        "white, cream and brown caliby",
        "white, black and brown caliby",
        "white, silver and grey caliby",
        "white, blue and silver caliby",
        "red and brown tortorbie",
        "orange and black torbie",
        "orange and brown torbie",
        "orange and cream torbie",
        "grey and cream torbie",
        "cream and brown torbie",
        "black and red torbie",
        "silver and dark grey torbie",
        "blue and silver torbie",
    ]
    possibleWhites = [
        "white van",
        "white harlequin",
        "white tuxedo",
        "white bicolour",
        "white mitted",
    ]
    possibleCoolEyeColours = ["red", "blue", "green", "orange", "yellow"]
    possibleCoolEyes = ["dichromid", "heterochromia"]

    # other values

    lenDescriptors = len(possibleDescriptors) - 1
    lenCommonFurDescriptors = len(possibleCommonFurDescriptors) - 1
    lenRareFurDesriptors = len(possibleRareFurDescriptors) - 1
    lenPatterns = len(possiblePatterns) - 1
    lenFurColours = len(possibleFurColours) - 1
    lenQuirks = len(possibleQuirks) - 1
    lenEyeColours = len(possibleEyeColours) - 1
    lenSpecials = len(possibleSpecials) - 1
    lenWhites = len(possibleWhites) - 1
    lenCoolEyeColours = len(possibleCoolEyeColours) - 1
    lenCoolEyes = len(possibleCoolEyes) - 1

    # rolling attributes

    random1 = randint(1, 100)
    if random1 > 0 and random1 < 51:
        patterned = True
    else:
        patterned = False

    if fixedGender == "female":
        gender = "she-cat"
    elif fixedGender == "male":
        gender = "tom"
    else:
        random2 = randint(1, 101)
        if random2 > 0 and random2 < 51:
            gender = "tom"
        else:
            gender = "she-cat"

    random3 = randint(1, 100)
    if random3 > 0 and random3 < 61:
        furDescriptor = possibleCommonFurDescriptors[
            randint(0, lenCommonFurDescriptors)
        ]
    else:
        furDescriptor = possibleRareFurDescriptors[randint(0, lenRareFurDesriptors)]

    descriptor = possibleDescriptors[randint(0, lenDescriptors)]
    if descriptor[0] in "aeiou":
        start = "an "
    else:
        start = "a "

    random4 = randint(1, 100)
    if random4 > 0 and random4 < 41:
        quirked = True
    else:
        quirked = False

    random5 = randint(1, 100)
    if random5 > 0 and random5 < 26:
        whited = True
    else:
        whited = False

    random6 = randint(1, 100)
    if random6 > 0 and random6 < 26:
        specialed = True
    else:
        specialed = False

    random7 = randint(1, 100)
    if random7 > 0 and random7 < 3:
        coolEyed = True
    else:
        coolEyed = False

    colour = possibleFurColours[randint(0, lenFurColours)]
    pattern = possiblePatterns[randint(0, lenPatterns)]
    special = possibleSpecials[randint(0, lenSpecials)]
    quirk = possibleQuirks[randint(0, lenQuirks)]
    eyeColour = possibleEyeColours[randint(0, lenEyeColours)]
    eyeColour1 = possibleCoolEyeColours[randint(0, lenCoolEyeColours)]
    eyeColour2 = possibleCoolEyeColours[randint(0, lenCoolEyeColours)]
    while eyeColour2 == eyeColour1:
        eyeColour2 = possibleCoolEyeColours[randint(0, lenCoolEyeColours)]
    white = possibleWhites[randint(0, lenWhites)]
    coolEye = possibleCoolEyes[randint(0, lenCoolEyes)]

    # making the cat

    if specialed == False:
        description = start
        if isKit == False:
            description = description + descriptor + " "
        description = description + colour + " "
        if whited == True:
            description = description + "and " + white + " "
        if patterned == True:
            description = description + pattern + " "
        description = description + gender + " with " + furDescriptor + " fur"
        if quirked == True and isKit == False:
            description = description + ", " + quirk
        description = description + " and "
        if coolEyed == False:
            description = description + eyeColour
        elif coolEyed == True:
            description = description + eyeColour1 + "/" + eyeColour2 + " " + coolEye
        description = description + " eyes"

    else:
        description = start
        if isKit == False:
            description = description + descriptor + " "
        description = description + colour + " "
        description = description + special + " "
        description = description + gender + " with " + furDescriptor + " fur"
        if quirked == True and isKit == False:
            description = description + ", " + quirk
        description = description + " and "
        if coolEyed == False:
            description = description + eyeColour
        elif coolEyed == True:
            description = description + eyeColour1 + "/" + eyeColour2 + " " + coolEye
        description = description + " eyes"

    # returning the description

    return description


# main script

flag1 = True
while flag1 == True:
    answer = input("Generate new clan? (yes or no)\n")
    while answer.lower() != "yes" and answer.lower() != "no":
        answer = input("That's not an option.\nGenerate new clan? (yes or no)\n")
    if answer.lower() == "no":
        flag1 = False
        flag2 = True
        break
    elif answer.lower() == "yes":
        print("\n" + randomClan())
while flag2 == True:
    time.sleep(1)
