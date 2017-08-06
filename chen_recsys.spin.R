# discretization finantial data -------------------------------------------
data <- read.csv("./data/基金会财务信息年分权重后结果统计（分类后）.csv", encoding = "utf-8")
cols <- colnames(data)
choiceCol <- cols[c(7, 12, 11, 22, 23)]
dataTrain <- data[choiceCol]

# to make shou ru, zhi chu, fei yong smaller than 1
dataTrain[2] <- dataTrain[2] / dataTrain[1]
dataTrain[3] <- dataTrain[3] / dataTrain[1]
dataTrain[4] <- dataTrain[4] / dataTrain[1]

# 
head(dataTrain, n = 2)

# disc 
library(discretization)
dataTrain$label <- as.factor(dataTrain$label)
res <- disc.Topdown(dataTrain, method = 1)
res$Disc.data  

# still too many intervals left we need to find a better discretization methodres
library(arules)
library(plyr)
fnDisc <- function(X, method){
  return (discretize(X, method, categories = 3, labels=c(0,1,2)))
}
# 
x <- dataTrain[, 1]
xEqualFreq <- discretize(x, method = 'frequency', categories = 3, labels = c(0, 1, 2)) 
Y <- dataTrain$label
# 
XEqualFreq <- colwise(fnDisc)(dataTrain[c(1:3)], method='frequency')
XEqualInterval <- colwise(fnDisc)(dataTrain[1:3], method='interval')
XCluster <- colwise(fnDisc)(dataTrain[1:3], method='cluster')

# classification to choose which type of discretization that we are going to use
library(caret)
split = 0.6
trainIndex <- createDataPartition(dataTrain$label, p = split, list=FALSE) 
fnClf <- function(X, Y){
  
  
  
}


