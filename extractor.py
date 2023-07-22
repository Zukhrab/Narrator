import os
import PyPDF2 as pdf2

class Extractor():

    def __init__(self) -> None:
        pass

    def num_of_pages(rdrFile) -> int:
        return len(rdrFile)
    

class File():

    file_name_src = str
    file_path_src = str

    def __init__(self, file_name_dst):
        self.file_name = file_name_dst
        
