student_id <- "202257-351303"  
student_id <- gsub("-", "", student_id)
x <- as.numeric(unlist(strsplit(student_id, ""))) 

print(x)

avg <- mean(x) 
variance <- var(x) 
median_val <- median(x) 

print(paste("평균: ", avg))
print(paste("분산: ", variance))
print(paste("중앙값: ", median_val))

y <- x
y[length(y)] <- NA

print(y)


# NA 값을 0으로 대체
x[is.na(x)] <- 0
y[is.na(y)] <- 0

sum_xy <- x + y
diff_xy <- x - y

cat("합:\n")
for(i in 1:length(sum_xy)) {
    cat(sum_xy[i], "\t")
}

cat("\n차:\n")
for(i in 1:length(diff_xy)) {
    cat(diff_xy[i], "\t")
}

avg_y <- mean(y, na.rm = TRUE) 
variance_y <- var(y, na.rm = TRUE) 
median_val_y <- median(y, na.rm = TRUE) 

print(paste("평균: ", avg_y))
print(paste("분산: ", variance_y))
print(paste("중앙값: ", median_val_y))

