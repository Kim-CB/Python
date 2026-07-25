def prime_factors(num):
    factors = []
    factor = 2

    while (num >= 2):
        if (num % factor == 0):
            factors.append(factor)
            num = num / factor
        else:
            factor += 1
    return factors

# print(prime_factors(12))
# print(prime_factors(42))

def is_prime(num):
    if num <= 1:
        return False
    else:
        prime = True
        # Para descobrir se um número é primo, você só precisa tentar dividi-lo por números que vão de 2 até a raiz quadrada desse número.
        for i in range(2, int(num**0.5) + 1):
            print(i)
            if num % i == 0:
                prime = False
                break
        return prime

#print(is_prime(73))

# Modifying Global Scope

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
GOOGLE_URL= "www.google.com"
