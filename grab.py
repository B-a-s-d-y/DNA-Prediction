def extract_lines(input_file, output_file, start_line):
    # 因为Python是零索引，所以要减去1
    end_line = start_line+29
    start_line -= 1  
    end_line -= 1  

    with open(input_file, 'r') as infile:
        lines = infile.readlines()  # 读取所有行

    # 提取指定行
    selected_lines = lines[start_line:end_line + 1]
    if('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\n' in selected_lines):
        return
    with open(output_file, 'a') as outfile:
        outfile.writelines(selected_lines)  # 将选定行写入新文件

# 示例调用
input_F = 'q:/GE/test set/X.txt'  # 源文件名
output_file = 'q:/GE/test set/training_set.txt'  # 目标文件名

for i in [1,2,3,5,6,7,8,9,10]:
    input_file = input_F.replace("X",str(i))
    for j in range(2000):
        #100000行，每50行
        extract_lines(input_file, output_file,2+50*j)
