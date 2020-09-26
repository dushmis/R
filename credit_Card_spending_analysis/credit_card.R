creditcard  <-  read.csv("./finance.csv",sep=';',comment.char="=")
creditcard$amount  <-  as.numeric(gsub(",","",creditcard$amount))
creditcard$date  <-  as.Date(creditcard$date,format="%d/%m/%Y")

e  <-  creditcard[creditcard$credit!='Cr',]


trans  <-  read.csv("./file_with_transactions.txt");
trans$Date  <-  as.Date(trans$Date,format="%d/%m/%y")

# trans.low  <-  lowess(trans$Date,trans$Closing.Balance,f=0.02)
# plot(trans$Date,trans$Closing.Balance,type='l',col='grey')
# lines(trans.low,type='l',col='red')

# trans.low  <-  lowess(trans$Date,trans$Debit.Amount)
# plot(trans$Date,trans$Debit.Amount,type='l',col='grey')
# lines(trans.low,type='l',col='red')


trans.low  <-  lowess(trans$Date,trans$Closing.Balance)


trans.lm <- lm(Closing.Balance ~ Date, data=trans)
added_days  <-  5000

trans.proj  <-  seq(max(trans$Date), max(trans$Date) + added_days,1)
trans.futuredate  <-  data.frame(Date=trans.proj)

trans.range <- seq(min(trans$Date),max(trans.proj),1)

sample(max(trans$Closing.Balance)*-1:max(trans$Closing.Balance),length(trans.range),rep=TRUE)

trans.rand <- data.frame(Date=trans.range,Closing.Balance=sample(0:max(trans$Closing.Balance),length(trans.range),rep=TRUE))
plot(trans.rand,type='n',col='grey')
lines(trans$Date,trans$Closing.Balance,type='l',col='grey')
lines(trans.low,type='l',col='red')

trans.conf_interval  <-  predict(trans.lm, newdata=trans.futuredate, interval="confidence",level=0.90)

lines(trans.futuredate$Date, trans.conf_interval[,2], col="blue", lty=11)

summary(trans);