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

# 
Y <- dataTrain$label
XEqualFreq <- colwise(fnDisc)(dataTrain[c(1:4)], method='frequency')
XEqualInterval <- colwise(fnDisc)(dataTrain[1:4], method='interval')
XCluster <- colwise(fnDisc)(dataTrain[1:4], method='cluster')
addY <- function(X, Y){
  X$target <- Y
  return(X)
}
X <- list()
X[[1]] <- addY(XEqualFreq, Y)
X[[2]] <- addY(XEqualInterval, Y)
X[[3]] <- addY(XCluster, Y)

# classification to choose which type of discretization that we are going to use
library(caret)
library(klaR)
library(e1071)
split = 0.6
trainIndex <- createDataPartition(dataTrain$label, p = split, list=FALSE) 
fnClf <- function(X, trainIndex){
  Xtrain <- X[trainIndex, ]
  Xtest <- X[-trainIndex, ]
  Ytrain <- Xtrain$target
  Ytest <- Xtest$target
  model <- NaiveBayes(target~., data = Xtrain)
  Ypred <- predict(model, Xtest)
  confusionMatrix(Ypred$class, Ytest)
}

# equal frequency
for (i in 1:3){
  cat("***** current list: ", i)
  print(fnClf(X[[i]], trainIndex))
}

# conclusion: we should cut the value based on equal frequency
# Overall Statistics
# 
# Accuracy : 0.5042          

dataFinal <- X[[1]]
dataFinal <- cbind(data[cols[1]], dataFinal)
write.csv(dataFinal, "./data/基金会财务信息年分权重后提取关键列（分类后）.csv")

# we can review
Xjinzichan <- cbind(dataFinal$净资产, dataTrain$净资产)
colnames(Xjinzichan) <- c('v1', 'v2')

# jing zi chan
aggregate(x = Xjinzichan[, 2], by = list(Xjinzichan[, 1]), FUN=mean)
# Group.1         x
# 1       1   8297497
# 2       2  32470654
# 3       3 618969282

# we can review
Zongshouru <- cbind(dataFinal$总收入, dataTrain$总收入)
colnames(Zongshouru) <- c('v1', 'v2')

# jing zi chan
aggregate(x = Zongshouru[, 2], by = list(Zongshouru[, 1]), FUN=mean)
# Group.1          x
# 1       1 -0.2825629
# 2       2  0.4333708
# 3       3  2.1088900

# we can review
Zongzhichu <- cbind(dataFinal$总收入, dataTrain$总支出)
colnames(Zongzhichu) <- c('v1', 'v2')

# Zong zhi chu
aggregate(x = Zongzhichu[, 2], by = list(Zongzhichu[, 1]), FUN=mean)
# Group.1          x
# 1       1 -0.2957747
# 2       2  0.3089209
# 3       3  1.8594327

# Zong fei yong

# we can review
Zongfeiyong<- cbind(dataFinal$费用合计, dataTrain$费用合计)
colnames(Zongfeiyong) <- c('v1', 'v2')

# Zong zhi chu
aggregate(x = Zongfeiyong[, 2], by = list(Zongfeiyong[, 1]), FUN=mean)
# Group.1          x
# 1       1 -0.3699025
# 2       2  0.2820554
# 3       3  1.9596298










