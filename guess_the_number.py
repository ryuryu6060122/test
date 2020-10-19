import random

while True:
    try:
        maxn = int(input('choise maxn number : '))
    except ValueError:
    	print('please enter number')
    else:
    	if maxn == 0:
    		print('please enter non-zero number')
    	else:
    		break

print(f'guess the number from 1 to {maxn}')
answer = random.randint(1,maxn)

while True:
    while True:
        val = input('your try : ')
        try:
        	d = int(val)
        except ValueError:
        	print('please enter number')
        	continue
        else:
            if not 1 <= d <= maxn:
        	    print(f'please number from 1 to {maxn}')
        	    continue
            else:
            	break
    
    if d == answer:
    	print('congrats, you won!')
    	break
    elif d < answer:
	    print('too low')
	    continue
    elif d > answer:
	    print('too big')
	