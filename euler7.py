target_prime_location = 10001
primes_count = 1
i = 2

while primes_count < target_prime_location:
    i += 1
    # check if i is even
    if i % 2 == 0:
        continue

    j = 2
    while j**2 <= i:
        if i % j == 0:
            break
        else:
            j += 1
    else:
        primes_count += 1
    
print(i)