# Simple and Linear Regressions

## The data we'll use

Having __pull / clone__ this proyect, you could find the data on your data folder. Please go to the [original source](https://www.gov.uk/government/statistics/graduate-outcomes-for-all-subjects-by-university) for more information. Open RStudio.

## R

Reading the database:

```r
data <- read.csv("../sfr18_2017.csv", header=TRUE, sep=",")
```

Review variables:

```r
names(data)
```

List of variable names and their description:

__UKPRN__ UK Provider Reference Number.

__subject__ Subject studied.

__sex__ Sex of graduate.

__yearsAfterGraduation__		Number of years after graduation.

__grads__				Number of graduates included in calculations.

__unmatched__			Percentage of graduates that have been classed as unmatched.

__matched__				Number of graduates that have been classed as matched.

__activityNotCaptured__		Percentage of matched graduates whose activity could not be captured.

__noSustDest__			Percentage of matched graduates with an unsustained destination.

__sustEmpOnly__			Percentage of graduates with a record or sustained employment only.

__sustEmp__				Percentage of graduates with a record or sustained employment (these graduates may or may not have a further study record in addition to a sustained employment record).

__sustEmpFSorBoth__			Percentage of graduates with a record or sustained employment, a record of further study, or both.

__earningsInclude__			Number of matched graduates included in earnings calculations.

__lowerAnnEarn__			Annualised earnings lower quartile.

__medianAnnEarn__			Median annualised earnings.

__upperAnnEarn__			Annualised earnings upper quartile.

__POLARGrpOne__			Percentage of graduates in POLAR group 1 (of those eligible to be included in POLAR calculations).

__POLARGrpOneIncluded__		Percentage of graduates included in POLAR calculations.

__prAttBand__			Prior attainment band.

__prAttIncluded__			Percentage of graduates included in prior attainment calculations.


### Plotting regressions


```r
attach(data)
plot(var1, var2)
abline(lm(y ~ x1))      #  y es la variable exógena, x1 es la variable endógena.
title("Regression")
detach(data)
```
----------------------------------------------------------------------------------------

Rename variables:

The `plyr` package has a `rename()` function that’s useful for altering the
names of variables. The `plyr` package isn’t installed by default, so you’ll need to install it on first use using the `install.packages("plyr")` command.

The format of the `rename()` function is `rename(dataframe, c(oldname="newname", oldname="newname",...))`

Here’s an example with the leadership data:

```r
library(plyr)
data <- rename(data, c(oldname="newname"...))
```

Subseting data:

The `subset()` function is probably the easiest way to select variables and observations. Here are two examples:

```
newdata <- subset(leadership, age >= 35 | age < 24, select = c(q1, q2, q3, q4))                       #  q1, q2... son column names
```
----------------------------------------------------------------------------------------

### Regression!!!!!

`-` Separates response variables on the left from the explanatory variables on the right. For
example, a prediction of y from x, z, and w would be coded y ~ x + z + w.

`+` Separates predictor variables.

`:` Denotes an interaction between predictor variables. A prediction of y from x, z, and the
interaction between x and z would be coded y ~ x + z + x:z.

`*` A shortcut for denoting all possible interactions. The code y ~ x * z * w expands to
y ~ x + z + w + x:z + x:w + z:w + x:z:w.

`^` Denotes interactions up to a specified degree. The code y ~ (x + z + w)^2 expands
to y ~ x + z + w + x:z + x:w + z:w.

`.` A placeholder for all other variables in the data frame except the dependent variable. For
example, if a data frame contained the variables x, y, z, and w, then the code y ~ .
would expand to y ~ x + z + w.

`-` A minus sign removes a variable from the equation. For example, y ~ (x + z + w)^2
– x:w expands to y ~ x + z + w + x:z + z:w.

`-1` Suppresses the intercept. For example, the formula y ~ x -1 fits a regression of y on
x, and forces the line through the origin at x=0.

function Mathematical functions can be used in formulas. For example, log(y) ~ x + z + w
would predict log(y) from x, z, and w.

----------------------------------------------------------------------------------------

### Examples!!!:


----------------------------------------------------------------------------------------

Correlation Matrix:

cor(df)
----------------------------------------------------------------------------------------


Multiple linear regression


> states <- as.data.frame(state.x77[,c("Murder", "Population",
"Illiteracy", "Income", "Frost")])

> fit <- lm(Murder ~ Population + Illiteracy + Income + Frost,
data=states)

> summary(fit)


----------------------------------------------------------------------------------------

Multiple linear regression with interactions

> fit <- lm(mpg ~ hp + wt + hp:wt, data=mtcars)

> summary(fit)


You can see from the Pr(>|t|) column that the interaction between horsepower and
car weight is significant. What does this mean? A significant interaction between two
predictor variables tells you that the relationship between one predictor and the
response variable depends on the level of the other predictor

----------------------------------------------------------------------------------------

Confident intervals

> confint (df)

95% confident that the interval...


----------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------

GLM

Syntax:

glm(Y~X1+X2+X3, family=gaussian(link="identity"), data=mydata)


Functions that support glm():

summary()

coefficients(), coef()

confint()

residuals()

anova()

predict()     --> Cross validation!, uses fitter model to predict response values for a         new dataset


A common  diagnostic:

plot(predict(model, type="response"),
residuals(model, type= "deviance"))

----------------------------------------------------------------------------------------

Logistic

Dicotomic vars:
> Affairs$ynaffair[Affairs$affairs > 0] <- 1
> Affairs$ynaffair[Affairs$affairs == 0] <- 0

> fit.full <- glm(ynaffair ~ gender + age + yearsmarried + children +
religiousness + education + occupation +rating,
data=Affairs, family=binomial())
> summary(fit.full)


----------------------------------------------------------------------------------------
