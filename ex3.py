import pathlib
filename=input("Enter the filename")
ext_txt = pathlib.Path(filename).suffix
print(ext_txt)
