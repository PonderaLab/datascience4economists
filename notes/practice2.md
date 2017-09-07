#Token_inegi API=> llamado a ciertas bibliotecas.
http://www3.inegi.org.mx/sistemas/api/denue/v1/tokenVerify.aspx

Token: 0201002c-76de-4d09-a2a0-9c7f3cb88b59-

Not working...


## R

1) Reading the database:

```r
data <- read.csv("../sfr18_2017.csv", header=TRUE, sep=",")
```

alternativamente:
> library(readr)
> sfr18_2017 <- read_csv("~/Desktop/github/datascience4economists/data/sfr18_2017.csv")


1.1) Data for practice2

install.packages("AER")

library(AER)

data("CASchools")

names(CASchools)

head(CASchools)

----------------------------------------------------------------------------------------

2) Review variables:


2.1) CASchools vars:

district: character. District code.

school: character. School name.

county:factor indicating county.

grades: factor indicating grade span of district.

students: Total enrollment.

teachers: Number of teachers.

calworks: Percent qualifying for CalWorks (income assistance).

lunch: Percent qualifying for reduced-price lunch.

computer: Number of computers.

expenditure: Expenditure per student.

income: District average income (in USD 1,000).

english: Percent of English learners.

read: Average reading score.

math: Average math score.



2.2) CASchools renaming vars:

install.packages("plyr")

library(plyr)

df <- rename(CASchools, c(students="total_students", county="region", calworks="pub_assist", lunch="perc_lunch", computer="num_computers", expenditure="exp_perstud", income="income_av", english="perc_english", read="read_average", math="math_average"))

head(df)


2.3) Creating variables:

df$stratio <- with(df, total_students/teachers)
df$score <- with(df, (math_average + read_average)/2)
df$income_av2 <-with(df, (income_av)*1000)


2.4) Dummies:

df$dum[df$grades == 'KK-08'] <- 1
df$dum[df$grades == 'KK-06'] <- 0


2.5) Interactions:

df$int_exp_comp <- df$dum*df$pub_assist

----------------------------------------------------------------------------------------

3) Correlation

cor.test(df$total_students, df$income_av2, method=c("pearson", "kendall", "spearman"))


cor.test(df$total_students, df$income_av2, method=c("kendall"))

Pearson: If the p-value is < 5%, then the correlation between x and y is significant.

4) Shapiro-Wilk normality test:

shapiro.test(df$income_av2) 

shapiro.test(df$math_average) 

output >= 0.05 we can assume normality



----------------------------------------------------------------------------------------

4) Subseting data for correlation matrix:

The `subset()` function is probably the easiest way to select variables and observations. Here are two examples:

```
newdata <- subset(leadership, age >= 35 | age < 24, select = c(q1, q2, q3, q4))                       #  q1, q2... son column names
```


 or alternative:

df_subset <- subset(df, select = c(int_dum_pubassist, stratio, dum, num_computers, perc_lunch, math_average, read_average,pub_assist))

----------------------------------------------------------------------------------------

5) Correlation Matrix:

cor(df_subset)
plot(df$read_average,df$math_average)

----------------------------------------------------------------------------------------

### Regression details!!!

`~` Separates response variables on the left from the explanatory variables on the right. For
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
### Plotting regressions (optional)


```r
attach(data)
plot(var1, var2)
abline(lm(y ~ x1))      #  y es la variable exógena, x1 es la variable endógena.
title("Regression")
detach(data)
```


----------------------------------------------------------------------------------------


6) Multiple linear regression


fit <- lm(math_average ~ num_computers + perc_lunch + stratio ,
data=df_subset)

summary(fit)


----------------------------------------------------------------------------------------

7) Multiple linear regression with interactions

fit <- lm(math_average ~ num_computers + perc_lunch + stratio + int_dum_pubassist  ,
data=df_subset)

summary(fit)


You can see from the Pr(>|t|) column that the interaction between horsepower and
car weight is significant. What does this mean? A significant interaction between two
predictor variables tells you that the relationship between one predictor and the
response variable depends on the level of the other predictor

----------------------------------------------------------------------------------------

8) Confident intervals

> confint (fit)

95% confident that the interval...


----------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------

9) GLM

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

10) Logistic

Dicotomic vars:
> Affairs$ynaffair[Affairs$affairs > 0] <- 1
> Affairs$ynaffair[Affairs$affairs == 0] <- 0

> fit.full <- glm(ynaffair ~ gender + age + yearsmarried + children +
religiousness + education + occupation +rating,
data=Affairs, family=binomial())
> summary(fit.full)


----------------------------------------------------------------------------------------
