f <- function(x) { return (x^2 - 7*x + 10)}
g <- function(x) { return (x - 4)}

x <- seq(-0.5, 7.5, by=0.01)

plot(x,f(x), type="l", col="red", ylim=c(-4,11), ylab="", asp=1)
points(x,g(x), type="l", col="blue")
#grid(ny=15, nx=8)
abline(v = 0:8, col="#cccccc", lty="dotted")
abline(h = -4:11, col="#cccccc", lty="dotted")
#abline(h=0, v=0, col="black", lwd=1.5)
arrows(x0 = 0, x1 = 0,
       y0 = -4.2, y1 = 11.3,
       length = 0.1,
       angle = 20)  
arrows(x0 = -0.5, x1 = 7.5,
       y0 = 0, y1 = 0,
       length = 0.1,
       angle = 20)  
