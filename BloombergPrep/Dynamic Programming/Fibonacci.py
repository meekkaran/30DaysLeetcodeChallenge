#three ways to solve
#RECURSION

def fib(n):
	if n ==1 or n == 2:
		result = 1
	else:
		result = fib(n-1) + fib(n-2)
	return result

#MEMOIZATION

def fib(n,memo):
	if memo(n) != null: #thismeans we've seen the value n
		return memo[n]
	if n == 1 or n == 2:
		result = 1
	else:
		result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
		memo[n] = result #store the result in the memo array
	return result

def fib_memo(n):
	memo = [none] * n + 1
	return fib(n,memo)
	

	
#BOTTOM-UP

def fib(n):
	if n == 1 or n == 2:
		return 1
	bottom_up = [none] * n + 1
	bottom_up[1] = 1
	bottom_up[2] = 2
	
	for i in range(3,n+1):
		 bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
	return bottom_up[n]
