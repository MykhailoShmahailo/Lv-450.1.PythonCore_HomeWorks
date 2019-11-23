def areYouPlayingBanjo(name):
    if name[0] == "r" or name[0] == "R":
        return "{} plays banjo".format(name)
    else:
        return "{} does not play banjo".format(name)

print(areYouPlayingBanjo("Rikki"))
#print(areYouPlayingBanjo("Martin"))