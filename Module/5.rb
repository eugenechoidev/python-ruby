require_relative 'Auth'
puts("아이디를 입력해주세요")
input_id = gets.chomp()
if Auth.login(input_id)
  puts('hello, '+input_id)
else
  puts('who are you?')
end
