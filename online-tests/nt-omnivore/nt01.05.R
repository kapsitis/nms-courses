yy <- rep(0, times=200)

#zz <- c(1,3,4,5,6,7,8,9)

zz <- c(1,3,5,7,9,11,13,15)

for (i in 1:20000) {
  xx <- sample(zz, size=2)
  px <- prod(xx)
  sx <- sum(xx) %% 3
  if (sx == 0 & yy[px] < 2) {
    yy[px] <- yy[px] + 2
  } else if (sx > 0 & yy[px] %% 2 == 0) {
    yy[px] <- yy[px] + 1
  }
}

which(yy == 3)


## Der c(1,3,4,5,6,7,8,9)
## Der c()


