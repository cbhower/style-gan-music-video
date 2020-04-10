import os

for dirpath, dirnames, filenames in os.walk('C:\\Users\\Christian\\Documents\\GitHub\\automatic-drum-transcription\\data'):
    print(dirnames)
    # print(filenames)
    for file in filenames:
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            # resizing logic
            pass