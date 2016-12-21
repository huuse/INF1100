#interest_rate_loop.py


initial_amount = 100

p = 5.5		# interest rate
amount = initial_amount
years = 0

while amount <= 1.5*initial_amount:
		amount += p/100*amount
		years += 1
		print years
		print amount

print years
