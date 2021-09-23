import time
albumbs = {}
def texit(qq):
    if(qq == "q"):
        print("\n[+] Exiting\n")
        time.sleep(1)
        exit(0)
def bnnrr():
    """Current List of albums"""
    i = 0
    while i < 20:
        print("\n\n\n")
        i += 1    
    print("\tCurrent Playlist")
    print("[+]========================[+]\n")
    for key1, value1 in albumbs.items():
        print(f"{key1} -> {value1}")
    print("\n[+]========================[+]")
print("\t[+] Welcome ")
loop = 0
ll = False
while(1):
    loop += 1
    desc1 = "Artist"
    desc2 = "Title"
    if ll:
        bnnrr()
        jock = len(albumbs) / 2 
        zipp = int(jock)
        if(zipp == 1):
            print(f"You have {zipp} albumb")
        else:
            print(f"You have {zipp} albumbs")
    msg1 = input("  ARTIST NAME ~> ")
    texit(msg1)
    msg2 = input(" ALBUMB TITLE ~> ")
    texit(msg2)
    print("Adding Albumb Content")
    print("[+] Loading ...")
    ttutt = msg1
    nnunn = msg2
    mop1 = f"{desc1}{loop}"
    mop2 = f"{desc2}{loop}"
    albumbs[mop1] = ttutt
    albumbs[mop2] = nnunn
    print("[+] Done ...")
    ll = True