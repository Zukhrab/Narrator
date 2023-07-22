import extractor
from tkinter import *
from tkvideo import tkvideo
import glob

filename = "Baron_En.pdf" # Replace with the filename you want to find
directory = "../Narrator" # Replace with the path of the directory you want to search in

filepaths = glob.glob(f"{directory}/**/{filename}", recursive=True)
print(filepaths)

###############################
# file_name = "Baron_En.pdf"
# file_path = extractor.os.getcwd()

# pdfFileObj = open(file_name, 'rb')
# pdfReader = extractor.pdf2.PdfReader(pdfFileObj)

# #print(pdfReader.numPages)
# print(len(pdfReader.pages))

# # pageObj = pdfReader.pages[18]
# # print(pageObj.extract_text())

# print(extractor.Extractor.num_of_pages(pdfReader.pages))

# class Intro:
    
#     def __init__(self):
#         wind = Tk()
#         wind.title("The Narrator")
#         wind.geometry("900x1440")

#         lblvideo = Label(wind)
#         lblvideo.pack()

#         player = tkvideo("intro.mp4", lblvideo, loop = 1, size = (900, 1440))
#         player.play()
#         wind.mainloop()