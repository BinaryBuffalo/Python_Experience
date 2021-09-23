def format_location(cityll, countryll):
    """Return city & location format"""
    fmatt = f"{cityll.title()}, {countryll.title()}"
    return fmatt

ms1 = input("\n   City ~> ")
ms2 = input("\nCountry ~> ")
hawk = format_location(ms1, ms2)
print(f"\n$ IE -> {hawk}")