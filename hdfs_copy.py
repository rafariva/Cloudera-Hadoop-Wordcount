import time
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

file_size = os.path.getsize(local_file)/1000000
start_time = time.time()
hdfs_response = os.system("hdfs dfs -put %s %s" % (local_file,hdfs_path))
end_time = time.time()
load_time = end_time - start_time

if hdfs_response == 0:
	print("File successfully copy to hdfs (%.2f MB in %.2f seconds)" % (file_size,load_time))
elif hdfs_response == 256:
	print("File already exists. Not copied")
else:
	print("ERROR. please check your syntax")
