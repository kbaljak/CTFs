import os

if os.path.exists("reverse.txt"):
    os.remove("reverse.txt");

res = b"";
rf = open("chal", "br");

group = [];
cur = b"";
ind = 0;
cnt = 0;

while (True):
    char = rf.read(1);
    if (not char): break;
    # flip groups of 8
    cur = cur + char;
    cnt += 1;
    if (cnt == 8):
        #print(cur[::-1])
        res = res + cur[::-1];
        cur = b"";
        cnt = 0;

rf.close();
wf = open("reverse.txt", "wb");
wf.write(res);
wf.close();
print("DONE");
