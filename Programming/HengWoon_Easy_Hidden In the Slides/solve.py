import glob, os
rootdir = os.path.dirname(os.path.realpath(__file__))

for filename in glob.glob(os.path.join(rootdir, "**/*.xml"), recursive=True):
    with open(filename, "rb") as f:
        content = f.read().decode('utf-8')
        check = content.find("YCEP")
        if check != -1:
            i = check
            flag = ""
            while content[i] != "}":
                flag = flag + content[i]
                i += 1
            print(flag+'}')