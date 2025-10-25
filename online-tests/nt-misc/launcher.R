library(knitr)
library(Cairo)
library(cairoDevice)
library(rmarkdown)
install.packages("ggplot2")

setwd("/Users/kapsitis/workspace/ddgatve-problems/imo-numbertheory/slides/multiple-choice/")
#Sys.setenv(TEXINPUTS=getwd(),
#           BIBINPUTS=getwd(),
#           BSTINPUTS=getwd())
parRegNum <- as.character(commandArgs(TRUE)[1])

id <- "000001" 

render("report.Rmd", encoding="UTF8")

