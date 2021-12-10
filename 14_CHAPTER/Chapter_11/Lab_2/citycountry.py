def geosaver(first, last):
    state_country = None
    if last:
        state_country = f"{first} {last}"
    else:
        state_country = first
    return state_country