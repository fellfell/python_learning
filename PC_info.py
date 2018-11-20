from os import listdir

class PC:
    def __init__(self,name_s,name_l,model,serial_num):
        self.name_s = name_s
        self.name_l = name_l
        self.name = name_s.split('.')[0]
        self.model = model
        self.serial_num = serial_num

mypath = r"C:\Users\ho\Desktop\test"
allfiles = [f for f in listdir(mypath) ]

pclist = []

for filename in allfiles:
    fullname = mypath + "\\" + filename;
    with open(fullname, 'r',encoding="utf-16") as fin:
        content = fin.readlines()
    get_model = content[1][19:].replace('\n','')
    get_serial_num = content[1][:19].replace('\n','')
    pclist.append(PC(filename,fullname,get_model,get_serial_num))
    
pclist.sort(key=lambda x: x.serial_num, reverse=False)

for pc in pclist:
    print(pc.serial_num,pc.model,pc.name)
    
    

    

