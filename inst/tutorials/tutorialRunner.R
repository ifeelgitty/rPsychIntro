# Use "remotes::install_github(“rstudio/gradethis”)" in console!


setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
getwd()


rmarkdown::run("./1-helloR/1-helloR.Rmd")
