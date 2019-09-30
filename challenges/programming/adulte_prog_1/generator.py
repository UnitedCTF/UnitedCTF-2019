a = ["LHGames",
"coveoBlitz",
"csGames",
"csawFinals",
"csawQuals",
"cunUHacks",
"geekSeekCTF",
"googleGames",
"hackatown",
"hackfestCTF",
"iHack",
"jdisGames",
"northsecCTF",
"picoCTF",
"qualifCSGames",
"ubisoftGameJam",
"unitedCTF"]

import itertools

b = [a for a in itertools.permutations(a, 2)]

import random
for ahah, yes in b:
    print(f"{random.randrange(1,500)} {ahah} {yes}")

