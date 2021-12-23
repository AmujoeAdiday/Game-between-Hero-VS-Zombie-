import random


# Part 1: the initial settings
size = 2

#health of Zombie and Hero
health = [10,10]
#treasure of Zombie and Hero respectively
treasure = [5,5]
#
# bots: initial 2D positions (x, y)
Zombie = [random.choice(range(1, 3)) for i in range(0, size)]

# protagonists: initial 2D positions (x, y)
Hero = [random.choice(range(1, 3)) for j in range(0, size)]

# portal: the secret location of the treasure
portal = [random.choice(range(1, 3)) for k in range(0, size)]
# print (portal)


# Part 2: the function definitions



# compute the distance between players
def vecDistance(vecA, vecB) :
    dist = ((vecA[0] - vecB[0]) ** 2 + (vecA[1] - vecB[1]) ** 2)
    dist = dist ** (0.5)
    return dist

# dot product to assign health or to assign a score
def vecDot(vecA, vecB) :
    dot = 0
    for i in range(size) :
        dot += vecA[i] * vecB[i]
    return dot



# the length of the vector
def vecLength(vec) :
    norm = vec[0] ** 2 + vec[1] ** 2
    norm = norm ** (1.0 / 2.0 )
    return norm

# determine player's position
def whereAmI(player, vecA) :
    msg = "player position: " + player
    print (msg, "(", vecA[0], ",", vecA[1], ")")

#function to give additional wealth--> can apply to extra health and treasure
def cloakingMode():
    extra_wealth = random.randint(0,10)
    return extra_wealth



# Part 3: the game play
count = 0
while True:
    count+=1

# the starting locations
    whereAmI("Zombie", Zombie)
    whereAmI("Hero", Hero)
    whereAmI("portal", portal)
    print("\n************************************************************")

# distances between players and the portal
    zombieDist = vecDistance(Zombie, portal)
    heroDist = vecDistance(Hero, portal)
    zom_Hero_dist = vecDistance(Zombie, Hero)

    print ("Zombie is", format(zombieDist, "0.1f"), "from  Portal")
    print("------------------------------------------------------------")
    print("Hero is", format(heroDist, "0.1f"), "from  Portal")
    print("------------------------------------------------------------")

    print("Hero is", format(zom_Hero_dist, "0.1f"), "from  Zombie")
    print("------------------------------------------------------------")

    # assign health to Zombie and Hero

    # in case Hero is getting closer to a Zombie zone, it will lose the health point


    vecDot(Hero, portal)
    vecDot(Zombie, portal)
    #store the value to cloak variable
    cloak = cloakingMode()
    print("Hero vec dot is ",vecDot(Hero, portal))
    print("Zombie vec dot is ",vecDot(Zombie, portal))
    print("Cloakingmode is ", cloak)
    if vecDot(Zombie, portal) - vecDot(Hero, portal) > 0:
        health[1] -= vecDot(Hero, portal)
    # at particular position, Hero will gain additional health point
    elif Hero == [2,2]:
        health[1]+= cloak


    print("**********  Health of Zombie and Hero  *******************")
    print("Health of Hero is ", health[1])
    print("Health of Zombie is ", health[0])

    #if the Hero reaches the portal, it will gain extra treasure point from the cloakingmode function
    #if the Zombie reaches the portal, it will gain extra treasure point from vecLength function
    if Hero == portal:
        treasure[1]+= cloak
    elif Zombie == portal:
        treasure[0] + vecLength(Zombie)
    print("**********  Treasure of Zombie and Hero  *******************")
    print("The treasure of Hero is ", treasure[1])
    print("The treasure of Zombie is ", treasure[0])
    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if (Zombie == Hero) and health[0] > health[1]:
        print("Hero has been defeated")
        break
    elif (Zombie == portal and Hero != portal):
        print("The zombie has won.")
        break
    elif (Hero == portal):
        print("The hero has won. The portal point is (",portal[0],",",portal[1],")")
        break
    elif health[1] <= 0:
        print("Health of Hero is too low to find the portal.\n\nThus, the Zombie has won.")
        break
    elif health[0] <= 0:
        print("Zombie lost all energy!\n\nThus, the Hero has won.")
        break

    elif health[0] <= 0 and health[1] <= 0 :
        print("Both fighters are too weak to go on in the game.")
        break



    Zombie = [random.choice(range(1, 3)) for i in range(0, size)]

        # protagonists: initial 2D positions (x, y)
    Hero = [random.choice(range(1, 3)) for i in range(0, size)]


print(count)
print()

