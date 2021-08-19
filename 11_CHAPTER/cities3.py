def desc_city(city, country):
    """Describes the city"""
    if(statell):
        print(f"The city {city}, {statell} is located in {country}")
while(desc_city):
    cityll  = input("\n\tCity    ~> ")
    statell = input("\n\tState   ~> ")
    ctryll  = input("\n\tCountry ~> ")
    desc_city(cityll, ctryll)

