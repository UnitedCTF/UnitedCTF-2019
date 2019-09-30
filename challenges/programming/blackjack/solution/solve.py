import requests
from collections import Counter
import pandas
import matplotlib.pyplot as plt

from hand import Hand
SERVER_URL = "https://blackjack-server.unitedctf.ca/"

s = requests.Session() # all cookies received will be stored in the session object

def deal(bet=50):
    return s.post(SERVER_URL + "deal", { "bet": bet }).json()

def hit():
    return s.post(SERVER_URL + "hit").json()

def hold():
    return s.post(SERVER_URL + "hold").json()

def flag():
    return s.get(SERVER_URL + "flag").text

def reset_session():
    s.cookies.clear()

def running_count(seen_cards):
    count = 0
    for c in seen_cards:
        if c["rank"] in ["2", "3", "4", "5", "6"]:
            count += 1
        if c["rank"] in ["10", "J", "Q", "K", "A"]:
            count -= 1
    return count

def play_hand(seen_cards=[]):
    count = running_count(seen_cards)
    bet = 0
    if count > 0:
        bet = 50

    r = deal(bet)
    while r["state"] == "IN_GAME":
        dealer_hand = Hand(r["dealerHand"])
        player_hand = Hand(r["playerHand"])
        if player_hand.value < 12:
            r = hit()
        elif player_hand.value == 12 and dealer_hand.value < 4:
            r = hit()
        elif player_hand.value == 12 and dealer_hand.value < 7:
            r = hold()
        elif player_hand.value == 12:
            r = hit()
        elif player_hand.value < 17 and dealer_hand.value < 7:
            r = hold()
        elif player_hand.value < 17:
            r = hit()
        else:
            r = hold()
    return r

def play():
    seen_cards = []
    while True:
        r = play_hand(seen_cards=seen_cards)
        print(str(r["cash"])+"$, ", end="")
        print("count: " + str(running_count(seen_cards)))
        if r["cash"] < 1000:
            reset_session()
        if r["cash"] >= 2000:
            print(flag())
            break

        seen_cards += r["dealerHand"]
        seen_cards += r["playerHand"]
        seen_cards = seen_cards[-20:]

# L'histogramme resultant indique que 66% du temps, 
# On retrouve la meme carte après ~30 piges
def recon():
    seen_cards = {}
    time_till_seen = []
    for _ in range(500):
        r = play_hand()
        for c in r["dealerHand"] + r["playerHand"]:
            key = (c["rank"], c["suit"])
            time_last_seen = seen_cards.get(key, 0)
            if time_last_seen != 0:
                time_till_seen.append(time_last_seen)
            seen_cards[key] = 0
            for k,v in seen_cards.items():
                seen_cards[k] = v + 1
    count = Counter(sorted(time_till_seen))
    df = pandas.DataFrame.from_dict(count, orient='index')
    df.plot(kind='bar')
    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(time_till_seen, bins=50, density=True, histtype='step', cumulative=True)
    ax.grid(True)
    plt.show()

# recon()
play()
