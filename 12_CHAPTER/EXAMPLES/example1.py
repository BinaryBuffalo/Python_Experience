class dog:
    """Simple model dog |name|-var |age|-INT |shots|->BOOL"""
    def __init__(self, name, age, shots):
        self.name  = name
        self.age   = age
        self.shots = shots
    
    def health(self):
        if(self.shots == True):
            yas = "yes"
        else:
            yes = "no"
        return yas

    def sit(self):
        """Dog sits"""
        print(f"{self.name} is sitting!")
    
    def roll(self):
        """DOG ROLLS OVER"""
        print(f"{self.name} rolled over")

def desc_dog(nii):
    print(f"My dogs name is {nii.name}")
    print(f"My dogs age is {nii.age}")
msg1 = input("$ (name)   ~> ")
msg2 = input("$ (age)    ~> ")
msg3 = input("$ (shots)  ~> ")
my_dog = dog(msg1, msg2, msg3)
desc_dog(my_dog)
my_dog.sit()
shots = str(my_dog.health())
print(f"Does {my_dog.name} have shots -> {shots}")