import sys
import os

try:
	local_file = sys.argv[1]
	hdfs_path = sys.argv[2]
except Exception:
	exit("No args. Please give <source file> and <hdfs destination path>")

if not os.path.isfile(local_file):
	print("source file not exits")
	exit()

hdfs_response = os.system("hdfs dfs -put %s %s" % (local_file,hdfs_path))

if hdfs_response == 0:
	print("File successfully copy to hdfs")
elif hdfs_response == 256:
	print("File already exists. Not copied")
else:
	print("ERROR. please check your syntax")
