def build_profile(first, last, **user_info):
    """create a user"""
    user_info['first_name'] = first 
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='Montana',
                             feild='physics')
print(user_profile)