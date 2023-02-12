import os,re,socket
from collections import Counter

count=0
top_3_words=[]
with open("/home/data/IF.txt",'r') as f:
    count+=sum([len(line.split()) for line in f.readlines()])
    f.seek(0)
    text=f.read()
    text = re.sub(r'[^\w\s]', '', text)
    word_counts = Counter(text.lower().split())
    top_3_words = word_counts.most_common(3)

with open("/home/data/Limerick.txt") as f:
    count+=sum([len(line.split()) for line in f.readlines()])

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

with open("/home/output/results.txt",'w') as f:
    f.write("List of files in directory /home/data: " + str(os.listdir("/home/data/")) + "\n")
    f.write("Total number of words in two files is " + str(count) + "\n")
    f.write("Top 3 words: " + str(top_3_words) + "\n")
    f.write("IP address of the machine is " + get_ip_address())