def candestroy():

    
    blocklist = []
    item = str(input("Item: "))
    t = True
    while t:
        add = str(input("Can Destroy: "))
        blocklist.append(add)
        if add == "DONE":
            blocklist.pop(len(blocklist) - 1 )
            t = False
    output = ','.join(f"minecraft:{add}" for add in blocklist)
    print("/give @s minecraft:" + item + "{CanDestroy:[" + output + "]}")
    choix()

def canplaceon():
    blocklist = []
    item = str(input("Item: "))
    t = True
    while t:
        add = str(input("Can Be Placed On: "))
        blocklist.append(add)
        if add == "DONE":
            blocklist.pop(len(blocklist) - 1 )
            t = False
    output = ','.join(f"minecraft:{add}" for add in blocklist)
    print("/give @s minecraft:" + item + "{CanPlaceOn:[" + output + "]}")
    choix()




def choix():
    s = True 
    while s:
        choice = str(input("CanDestroy (1) / CanPlaceOn (2) / QUIT (3) "))
        if choice == "1":
            candestroy()
            s = False
        elif choice == "2":
            canplaceon()
            s = False
        elif choice == "3":
            s = False
choix()
