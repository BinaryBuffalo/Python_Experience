def make_pizza(*pizza):
    for name in pizza:
        print(name)

make_pizza('mushrooms', 'cheese')
dic1 = {}
def build_profile(first, last, **user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

kjj = build_profile('daddy', 'hanaka')
dic1.add(kjj)
print(dic1)