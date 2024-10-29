# add your code here for List Comprehension
fb = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
      "Fizz" if i % 3 == 0 else
      "Buzz" if i % 5 == 0
      else i for i in range(1, 101)]
for i in fb:
    print(i)
    
