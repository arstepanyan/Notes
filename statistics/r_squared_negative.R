## R-squared can, mathematically, be negative.
## It will happen when we are fitting the data really badly.
## An example code for the plot of such scenario is shown below.
setwd("path where you want to save the plot")

png(filename="negative_r_squared.png")

set.seed(1234)
x = rnorm(100, mean=1, sd=1)
eps = rnorm(100, mean=0, sd=1)
y = 2+4*x+eps

plot(x, y, col = rgb(0.5,0.8,0.6), pch = 19)
abline(h = mean(y), col= rgb(0, 0.6, 0.3), lwd=4, lty=2)
text(2.8, mean(y)+1.2, " mean(y)", col =rgb(0, 0.6, 0.3), cex=1.7 )

set.seed(1234)
y_hat = 9 - 3 * x
lines(x, y_hat, col = "red", lwd = 4)
text(2.7, -0.2, "Bad Fit", col = "red", srt = -33, cex=1.7)

dev.off() 
