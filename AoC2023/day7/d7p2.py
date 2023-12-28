from collections import Counter
import numpy as np


def get_type(hand):
    jokers = hand.count("J")
    hand = [c for c in hand if c != "J"]
    counts = sorted(Counter(hand).values(), reverse=True)
    if not counts:
        counts = [0]
    if counts[0] + jokers == 5:
        return 6
    if counts[0] + jokers == 4:
        return 5
    if counts[0] + jokers == 3 and counts[1] == 2:
        return 4
    if counts[0] + jokers == 3:
        return 3
    if counts[0] == 2 and (jokers or counts[1] == 2):
        return 2
    if counts[0] == 2 or jokers:
        return 1
    return 0


def tell_type(hand):
    c = Counter(hand)

    if "J" in c.keys():
        J_v = c["J"]
        del c["J"]

        if len(c) <= 1:
            return 7  # five of a kind
        if len(c) == 2:
            if J_v >= 2:
                return 6  # four of a kind
            if 3 in c.values():
                return 6  # four of a kind
            return 5  # full house
        if len(c) == 3:
            return 4  # three of a kind
        return 2  # one pair

    else:
        if len(c) == 1:
            return 7  # five of a kind
        if len(c) == 2:
            if 4 in c.values():
                return 6  # four of a kind
            return 5  # full house
        if len(c) == 3:
            if 3 in c.values():
                return 4  # three of a kind
            return 3  # two pair
        if len(c) == 4:
            return 2  # one pair
        return 1  # high card


def comp_hand(hand1, hand2):
    type1 = tell_type(hand1)
    type2 = tell_type(hand2)
    if type1 > type2:
        return True
    if type1 < type2:
        return False

    return comp_equal(hand1, hand2)


def comp_equal(hand1, hand2):
    cards = "AKQT98765432J"
    order = "fedcba9876543"
    c_map = {char1: char2 for char1, char2 in zip(cards, order)}

    v1 = int("".join([c_map[c] for c in hand1]), 16)
    v2 = int("".join([c_map[c] for c in hand2]), 16)
    return v1 > v2


with open("data2", "r") as file:
    lines = file.readlines()

f_ls = [l.strip().split() for l in lines]

ls_h = [h[0] for h in f_ls]
ls_b = [int(h[1]) for h in f_ls]

wins = np.zeros(len(ls_h))
for i in range(len(ls_h)):
    for j in range(i + 1, len(ls_h)):
        if comp_hand(ls_h[i], ls_h[j]):
            wins[i] += 1
        else:
            wins[j] += 1


ls_wins = np.multiply(wins + 1, ls_b)
# print(ls_wins)
print(np.sum(ls_wins))


tmy = [tell_type(h) for h in ls_h]
tsol = [get_type(h) for h in ls_h]
