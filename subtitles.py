import os 
import STT

def srtFile(folderName):
    t = ""
    for fragment in sorted(os.listdir(f"./{folderName}/fragments"), key=lambda x: int(x.split("-")[0])):
        t += fragment_info(f"./{folderName}/fragments/{fragment}")
    print(t)

def fragment_info(fragment_path):
    text = STT.STT(fragment_path)
    return text

if __name__ == "__main__":
    pass