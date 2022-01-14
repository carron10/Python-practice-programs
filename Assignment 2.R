
Baseline=c(210,180,195,220,231,199,224)
Program.End=c(193,186,186,223,220,183,233)
my_data <- data.frame(Baseline,Program.End)
print(my_data)
res <- t.test(Baseline, Program.End, paired = TRUE)
res
