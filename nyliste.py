#coding=utf-8
with open("idtermer.txt") as file:
	for line in file:
		sys.stdout.write(line)
		if line.startswith("te="):
			sys.stdout.write(line.replace("te=", "en="))
