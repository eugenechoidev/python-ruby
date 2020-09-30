input_id = input("아이디를 입력해주세요.\n")
members = ['eugene', 'choi', 'chungha']

for member in members:
    if member == input_id:
        print('hello, '+member)
        import sys
        sys.exit()
print('who are you?')
