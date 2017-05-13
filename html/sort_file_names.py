with open("file_paths.txt", "r") as f:
    content = f.readlines()
content.sort()

f_new = open("sorted_file_paths.txt", "w")
for line in content:
	f_new.write(line)
f_new.close()