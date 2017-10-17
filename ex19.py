def cheese_and_chickens(boxes_of_pizza, no_of_burgers):
  print "You have %d cheeses!" % boxes_of_pizza
  print "You have %d boxes of chickens!" % no_of_burgers
  print "that's enough for a party!"
  print "enjoy tonight .\n"


print "We can just give numbers directly:"
cheese_and_chickens(20, 30)

print "OR, we can use variables from our script:"
amount_of_pizza = 10
amount_of_burger = 50

cheese_and_chickens(amount_of_pizza, amount_of_burger)

print "We can even do math inside too"
cheese_and_chickens(10 + 20, 5 + 6)


print "we can combine both variables and math:"
cheese_and_chickens(amount_of_pizza + 100, amount_of_burger + 1000)