student_id <- "202257-351303"  
student_id <- gsub("-", "", student_id)
x <- as.numeric(unlist(strsplit(student_id, "")))

y <- x
y[length(y)] <- NA

m1 <- cbind(x, y)

m1[12, 2] <- 500

avg_m1 <- apply(m1, 2, mean, na.rm = TRUE)
print(avg_m1)

