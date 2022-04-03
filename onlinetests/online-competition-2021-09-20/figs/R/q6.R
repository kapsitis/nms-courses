require(gmp)

fact <- function(n) {
  result <- as.bigz(1)
  if (n == 0) { 
    return(result) 
  }
  else {
    for (i in 1:n) {
      result <- result*i
    }
    return(result)
  }
}

count <- 0
for (j in 0:2020) {
  if (j %% 20 == 0) {
    print(sprintf("Processed %d", j))
  }
  comb <- fact(2020) %/% (fact(j)*fact(2020-j))
  if (comb %% 2020 == 0) {
    count <- count + 1
  }
}


ff <- function(x) {
  return((x*x + x + 356)/2)
}


