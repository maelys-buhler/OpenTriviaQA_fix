import os
import pandas as pd
import numpy as np
def txt_to_csv(path): 
  """
  The csv Generarted will be such:
    |Questions | Correct | A | B | C | D |
  0 |  myQ     |    X    | a | X | c | d |  
  """   
  questions=[]
  key=[]
  dist1=[]
  dist2=[]
  dist3=[]
  dist4=[]
  options=[[],[],[],[]]
  with open(path, errors='ignore',mode="r") as file1:
      files = file1.readlines()
      i=0
      for i in range(len(files)):
        if files[i][0]=='\n':
          if len(files) == i + 1:
            continue
          #avoid questions begginning with #, which break the pattern
          if len(files[i+1]) >= 3 and files[i+1][3]=='#':
            continue   
          
          try:
            #QUESTION'S TEXT
            j = 1
            question_text = ""
            while files[i+j][0] != '^':   
              question_text += files[i+j]
              j += 1
            #remove #Q on the beginning
            question_text = question_text[3:len(question_text)-1]
            question_text = question_text.replace('\n', ' ')
            questions.append(question_text)
        
            #QUESTION'S ANSWER
            answer_text = ""
            while files[i+j][0] != 'A':   
              answer_text += files[i+j]
              j += 1
            #remove ^ on the beginning
            answer_text = answer_text[2:len(answer_text)-1]
            answer_text = answer_text.replace('\n', ' ')
            key.append(answer_text)

            #QUESTION'S OPTIONS
            options_letters = ['B', 'C', 'D', '\n']
            nb_options_found = 0
            option_text = ""
            while files[i+j][0] != '#' and nb_options_found < 4:
              if files[i+j][0] == options_letters[nb_options_found] or files[i+j][0] == '\n':
                #remove letter on the beginning             
                option_text = option_text[2:len(option_text)-1]
                option_text = option_text.replace('\n', ' ')
                options[nb_options_found].append(option_text)
                option_text = ""
                nb_options_found += 1
              else:
                option_text += files[i+j]
                j += 1
            for k in range(0, len(options)):
              if len(options[k]) != len(options[0]):
                options[k].append(np.nan)
          except IndexError:
            pass

  bank={}
  bank["Questions"]=questions
  bank["Correct"]=key
  bank["A"]=options[0]
  bank["B"]=options[1]
  bank["C"]=options[2]
  bank["D"]=options[3]
  df=pd.DataFrame(bank)
  return df

def parse_files(sourcePath='/content/drive/MyDrive/Colab Notebooks/Data_trivial/',destination='/content/drive/MyDrive/Colab Notebooks/Data_trivial_csv/'):
  """
  Input SourcePath and Destination Path to trverse through the files and convert them into csv
  Requirement Python 3.x , Numpy , os , Pandas
  or run this in Google Colab as it is
  """
  filenames=sourcePath
  for files in os.listdir(filenames):
     path=filenames+files
     data=txt_to_csv(path)
     data.to_csv(destination+files+'.csv')

if __name__ == "__main__":
    print(' Input SourcePath and Destination Path to trverse through the files and convert them into csv \n  Requirement Python 3.x , Numpy , os , Pandas \n  or run this in Google Colab as it is')
    parse_files(sourcePath=input('SourcePath'),destination=input('Destination Path'))