arr = [1, 7, 15, 19, 21, 28, 31, 42]
arr.delete_if() do |item|
  item > 7
end
puts arr
