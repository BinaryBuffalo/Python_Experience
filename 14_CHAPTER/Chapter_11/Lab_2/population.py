def geosaver(first, last, xxx):
    state_country = None
    if last:
        if xxx:
            state_country = f"{first} {last} {xxx}"
        else:
            state_country = f"{first} {last}"
            pass
    else:
        state_country = first
        pass
    return state_country