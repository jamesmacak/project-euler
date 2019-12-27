import time
start_time = time.time()

def phi(n):
    phi_n = n
    prime_factor = 2

    while prime_factor * prime_factor <= n:
        if n % prime_factor == 0: # is prime_factor indeed a prime factor
            while n % prime_factor == 0:
                n = n // prime_factor
            phi_n = phi_n * (1 - (1 / prime_factor))
        prime_factor += 1
    
    if n > 1: # n has prime factor > sqrt(n)
        phi_n = phi_n * (1 - (1 / n))

    return phi_n

n = 2
n_phi_n = {}

while n <= 1_000_000:
    if n % 2 == 0:
        n_phi_n[n / phi(n)] = n
    n += 1

max_n_phi_n = max(n_phi_n.keys())
print(n_phi_n[max_n_phi_n], max_n_phi_n)
print("%s seconds" % (time.time() - start_time))