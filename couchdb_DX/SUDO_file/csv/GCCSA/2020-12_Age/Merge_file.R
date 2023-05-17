# 要合并的 CSV 文件列表
csv_files <- c("C:\Users\Sunny\Desktop\csv\GCCSA\1.csv", "2.csv", "3.csv", "4.csv", "5.csv")

# 创建一个空的数据框
merged_data <- data.frame()

# 循环读取并合并每个 CSV 文件
for (file in csv_files) {
  # 读取 CSV 文件并将其添加到合并的数据框中
  data <- read.csv(file, header = TRUE, encoding = "UTF-8")
  merged_data <- rbind(merged_data, data)
}

# 输出合并后的数据框
print(merged_data)

read.csv("3.csv", header = TRUE, encoding = "UTF-8")

