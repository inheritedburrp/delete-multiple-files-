import os

for root, dirs, files in os.walk("/home/anuj/Downloads"):
    for currentFile in files:
        print "processing file: " + currentFile
        exts=('.torrent', '.exe','.run')
        if any(currentFile.lower().endswith(ext) for ext in exts):
            os.remove(os.path.join(root, currentFile))
