# Plots performance stats for below ports
# Worker HTTP 7443

a <- read.csv("./head.csv")
b <- read.csv("./data.csv")
names(b) <- names(a)
b$datetime <- as.POSIXct(b$datetime, format = "%Y-%m-%d %H:%M:%S")
x <- b[b$datetime>=format(Sys.Date() - 32),]
#x <- b[b$datetime>=paste(format(Sys.Date()),"07:01:11"),]
#x<-b

options(scipen=999)

rpl <- function(data,y,l=TRUE,header=y){
  plot(x=data[['datetime']], y=data[[y]], col='red', type='h', xlab = "time", main=header, ylab="")
  if (l) {
     lines(lowess(data[['datetime']], data[[y]],f=0.04),lty=11,col='lightgray')
     lines(lowess(data[['datetime']], data[[y]]),lty=11,col='blue')
  }
}

pdf(file = "Rplots.pdf", width=14, height=203 ,bg="white",pointsize=20)
#png(filename = "Rplot%03d.png", width = 480, height = 5480, units = "px", pointsize = 12, bg = "white")
par(mfrow=c(5,1))
rpl(data=x,y='errorCountconnector_http.nio.7443',header="Error Count Connector HTTP 7443")
rpl(data=x,y='maxTimeconnector_http.nio.7443',header="Max Time Connector HTTP 7443")
rpl(data=x,y='processingTimeconnector_http.nio.7443',header="Processing Time Connector HTTP 7443")
rpl(data=x,y='requestCountconnector_http.nio.7443',header="Request Count Connector HTTP 7443")
rpl(data=x,y='workersconnector_http.nio.7443',header="Worker HTTP 7443")
dev.off()


