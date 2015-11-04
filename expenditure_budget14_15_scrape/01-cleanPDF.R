library(dplyr)
library(magrittr)
library(stringr)
##### convert raw csv to readable format
csvdir <- "~/Documents/datakind/cbga/"
setwd(csvdir)

dat <- read.csv("ag_coop_14-15_raw.csv",stringsAsFactors = F, header = F)
t1<-dat[dat$V2=="",-2]
t2<-dat[-as.numeric(rownames(t1)),-15]
names(t1)<-paste0("V",1:14)->names(t2)
t3<-rbind(t1,t2)
t3 <- t3[order(as.numeric(rownames(t3))),]


#aa <- "19.01 National Food Security 2401"
#strsplit(dat[,1],"\\d{4}")[1]
######## work with rows with Total- or major head in 1st col
sub1 <-t3[c(grep("\\d{4}",t3[,1]),grep("^Total",t3[,1])),]
sub_nochange<-sub1[sub1$V2=="",]
sub_change<-sub1[sub1$V2!="",-14]
sub_change <- cbind(sub1[,1],V2="",sub1[,2:13],stringsAsFactors=F)
names(sub_change)<-names(sub_nochange)
t3[as.numeric(rownames(sub_change)),]<-sub_change
t3[as.numeric(rownames(sub_nochange)),]<-sub_nochange

#str_extract(t3[,2],"[^0-9]*|\\d+\\.*\\d*")
#str_extract(t3[,2],"(?=\\d{1})\\d")
#####
change_ind<- unique(c(grep("[A-Za-z]*\\d{4}",t3[,2]),grep("^Total-",t3[,2]),
                      grep("[:alpha:]",t3[,2])))
txtToExtract<-t3[unique(c(grep("[A-Za-z]*\\d{4}",t3[,2]),grep("^Total-",t3[,2]),
            grep("[:alpha:]",t3[,2]))),]


#unlist(lapply(txtToExtract[,2],function(x){ strsplit(x,"\\d{4}")[[1]][1]}))

t3[change_ind,1] %<>% paste0(
             unlist(lapply(txtToExtract[,2],function(x){ strsplit(x,"\\d{4}")[[1]][1]})))


t3[,2]<-str_extract(t3[,2], "^Total\\s|\\d{4}")
t3[,2]<-gsub("Total ","Total",t3[,2])



numToExtract <- t3[grep("[A-Za-z]*\\d{4}",t3[,2]),]

t3[grep("[A-Za-z]\\s\\d{4}",t3[,2]),2] <-unlist(
  lapply(numToExtract[,2],function(x){ strsplit(x,"\\d{4}")[[1]][2]}))




