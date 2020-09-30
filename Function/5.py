input_id = input("아이디를 입력해주세요.\n")
def login(_id):
    members = ['eugene', 'choi', 'chungha']
    for member in members:
        if member == _id:
            return True
    return False
if login(input_id):
    print('hello, '+input_id)
else:
    print('who are you?')
