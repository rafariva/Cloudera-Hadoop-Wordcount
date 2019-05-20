# Cloudera Hadoop Wordcount

## First Steps ##
1. [Download](https://www.cloudera.com/downloads/quickstart_vms.html) from Cloudera, the Hadoop Virtual Machine (select platform VirtualBox)
2. [Download](https://www.virtualbox.org/wiki/Downloads) and install Oracle VM VirtualBox
2.a) create a New VM machine, and select the virtualdisk downloaded from Cloudera (from Step 1)
2.b) In case of error running VM Machine, maybe the CPU virtual has to be enabled. [See this tutorial](https://helpdeskgeek.com/how-to/enable-virtualization-in-the-bios/)
3. Download a long test file with a lot of words (i.e. Plain Text Ebook ["Pride and Prejudice" by Jane Auseten](http://www.gutenberg.org/ebooks/1342)) or use the [same file](pride.txt) provided in this repository.

Use virtual machine now on...

## python script ##
For comparsion reason, create a [python file](wordcount.py) for wordcount.

For running script, from terminal write: "python wordcount.py pride.txt". Expected result: 127765 words (6961 unique words), time arround half second (may vary)

## Hadoop WordCount ##
[video tutorial](https://www.youtube.com/watch?v=kF-63_2e1Kk)


--create folders on hdfs

hdfs dfs -mkir <folderpath>

  
--copy file into hdsf

hdfs dfs -put <filesystempath> <hdfs path>
  
-- run jar
hadoop jar /home/cloudera/wordcount.jar WordCount /user/cloudera/input/novel.txt /output_new
