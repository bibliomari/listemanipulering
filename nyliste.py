#coding=utf-8
with open("idtermer.txt") as file:
	for line in file:
		print line,
		if line.startswith("te="):
			print line.replace("te=", "en="),
