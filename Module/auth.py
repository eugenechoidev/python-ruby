def login(_id):
    members = ['eugene', 'choi', 'chungha']
    for member in members:
        if member == _id:
            return True
    return False
