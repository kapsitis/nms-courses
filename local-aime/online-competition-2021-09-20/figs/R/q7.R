require(gmp)

for (i in 1:100) {
  if (isprime(i) == 2 & i %% 4 == 3) {
    print(i)
  }
}