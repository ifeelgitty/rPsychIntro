# Empty current environment
rm(list = ls())
# Import Data
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
getwd()

raw_user <- read.csv("data//user_dat.csv", sep = ";")
raw_creat <- read.csv("data//creat_task.csv", sep = ";")

# Show raw data

class(raw_user)
head(raw_user)

head(raw_creat)

dat <- merge(raw_user, raw_creat, by="id")

# Check summary

head(dat)
summary(dat)

nrow(dat)
ncol(dat)
dim(dat)
# Convert Sex to Factor and Analyse

## Access a data frame column

dat$sex
dat[1,]
dat[,2]
dat[1:10,2]

summary(dat$sex)

dat$sex <- as.factor(dat$sex)

summary(dat$sex)
levels(dat$sex) 

length(dat$sex)
length(levels(dat$sex))

# Do the same analysis for education!

summary(dat$education)

dat$education <- as.factor(dat$education)

summary(dat$education)
levels(dat$education) 

length(dat$education)
length(levels(dat$education))

# Distribution of IQ

hist(dat$iq)

library(ggplot2)
iq_hist <- ggplot(dat, aes(iq)) + geom_histogram()
iq_hist

summary(dat$iq)

shapiro.test(dat$iq)

install.packages("car")
library(car)
leveneTest(dat$iq)
qqplot()

install.packages("moments")
library(moments)

skewness(dat$iq)
kurtosis(dat$iq)

# Check Distribution of 

hist(dat$schizo_Score)
skewness(dat$schizo_Score)

hist(sqrt(dat$schizo_Score))
skewness(sqrt(dat$schizo_Score))

library(yarrr)
pirateplot(formula = iq ~ education, data = dat)
pirateplot(formula = creative_task ~ sex, data = dat)
t.test(creative_task ~ sex, data = dat[dat$sex %in% c("M", "F"),])

m1 <- lm(creative_task ~ sex, data=dat)
summary(m1)

pirateplot(formula = creative_task ~ gaming, data = dat)
pirateplot(formula = creative_task ~ sex * gaming, data = dat)


m2 <- lm(creative_task ~ gaming * sex, data=dat)
summary(m2)



# 

m3 <- lm(creative_task ~ schizo_Score, data=dat)
summary(m3)
ggplot(dat, aes(schizo_Score, creative_task)) + geom_smooth(method=lm)
ggplot(dat, aes(schizo_Score, creative_task)) + geom_smooth(method=loess)


library(mgcv)
m4 <- gam(creative_task ~ s(schizo_Score), data=dat)
summary(m4)
m5 <- gam(creative_task ~ s(schizo_Score, bs="cr"), data=dat)
summary(m5)
anova(m5, m4)

# Aggregate (Dunno where to put it yet), creativity by gender by 

genderized_insights <- aggregate(formula=creative_task ~ sex + gaming, data=dat, subset = sex %in% c("M", "F"),FUN=mean)
genderized_insights

# Plot

plot(dat$creative_task, dat$iq)

ggplot(dat, aes(iq,creative_task)) + geom_point() + geom_smooth(method=lm)

ggplot(dat, aes(iq,creative_task)) + geom_point() + geom_smooth(method=loess)


# Complex GLMM Model?

