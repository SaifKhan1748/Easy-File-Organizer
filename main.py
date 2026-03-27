import os

def arrange_files(files,ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    i=1
    for file in files_with_ext:
        os.rename(file,f"pdf - {i}.{ext}")
        i+=1
    if not(os.path.exists("pdf")):
        os.mkdir("pdf")

    for i,file in enumerate(files_with_ext):
        os.replace(file,f"pdf/{i+1}.{ext}")



if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files,"pdf")
