import os ,shutil

folder_dict={
    'pngs_extion':('.png',),
    'jgss_extion':('.jpg',),
}

folderpath=r'C:\Users\moham\OneDrive\Desktop\New folder\code\python\has'




def file_finder(folder_path , extention):
    files=[]
    for file in os.listdir(folder_path):
        file=f'{file}'
        for ext in extention:
            if file.endswith(ext):
                files.append(file)
    return files

for ext_type,ext_tuple in folder_dict.items():
    folder_name=ext_type.split('_')[0]+'files'
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,ext_tuple):
        itempath=os.path.join(folderpath,item)
        itemnewpath=os.path.join(folder_path,item)
        shutil.move(itempath,itemnewpath)
    
