fav_lang = "\tpython"
print(f"String = ({fav_lang})")
left_lang = f"{fav_lang.lstrip()}"
print(f"String = ({left_lang})\n")

fav_lang2 = "python\t"
print(f"String = ({fav_lang})")
right_lang = f"{fav_lang2.rstrip()}"
print(f"String = ({right_lang})\n")

fav_lang3 = "\tpython\t"
print(f"String = ({fav_lang3})")
whole_lang = f"{fav_lang3.strip()}"
print(f"String = ({whole_lang})")

