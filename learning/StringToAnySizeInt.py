anysizeint_base = 2**4  ## 2**32
digits = []

number_str = "341"  # "987654321098765432109876543210"
number_str_rev = number_str[::-1]
number = int(number_str)
print(f"{number:,}")
acum = 0
pwr = 0
for j in range(len(number_str_rev)):
    acum = int(number_str_rev[j]) * (10**pwr) + acum
    pwr += 1
    if acum >= anysizeint_base:
        q, r = divmod(acum, anysizeint_base)
        digits.append(r)
        acum = q * anysizeint_base
        pwr = 1


obtained = 0
for d in digits:
    obtained = obtained * anysizeint_base + d

print(f"Expected: {number:,} {'=' if number == obtained else '!='} {obtained:,}")
