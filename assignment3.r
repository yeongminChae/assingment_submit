var_Murder <- var(USArrests$Murder) 
print(var_Murder)

var_Assault <- var(USArrests$Assault) 
print(var_Assault)

var_UrbanPop <- var(USArrests$UrbanPop) 
print(var_UrbanPop)

var_Rape <- var(USArrests$Rape) 
print(var_Rape)

write.csv(USArrests, file = "USArrests.csv", row.names = TRUE)