# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
import googletrans
from googletrans import Translator

translator = Translator()

def filet(filename,lang,to_lang): 
    # Path of the pdf 
    fild = filename
    PDF_file = "/home/root99/Silfra/"+filename
      
    ''' 
    Part #1 : Converting PDF to images 
    '''
      
    # Store all the pages of the PDF in a variable 
    pages = convert_from_path(PDF_file, 500) 
      
    # Counter to store images of each page of PDF to image 
    image_counter = 1
      
    # Iterate through all the pages stored above 
    for page in pages: 
      
        # Declaring filename for each page of PDF as JPG 
        # For each page, filename will be: 
        # PDF page 1 -> page_1.jpg 
        # PDF page 2 -> page_2.jpg 
        # PDF page 3 -> page_3.jpg 
        # .... 
        # PDF page n -> page_n.jpg 
        filename = "page_"+str(image_counter)+".jpg"
          
        # Save the image of the page in system 
        page.save(filename, 'JPEG') 
      
        # Increment the counter to update filename 
        image_counter = image_counter + 1
      
    ''' 
    Part #2 - Recognizing text from the images using OCR 
    '''
        
    # Variable to get count of total number of pages 
    filelimit = image_counter-1
    
    
    fild= fild.rsplit( ".", 1 )[ 0 ] 
    
    
    # Creating a text file to write the output 
    outfile = "/home/root99/Silfra/"+fild+".txt"
      
    # Open the file in append mode so that  
    # All contents of all images are added to the same file 
    f = open(outfile, "a") 
      
    # Iterate from 1 to total number of pages 
    for i in range(1, filelimit + 1): 
      
        # Set filename to recognize text from 
        # Again, these files will be: 
        # page_1.jpg 
        # page_2.jpg 
        # .... 
        # page_n.jpg 
        filename = "page_"+str(i)+".jpg"
              
        # Recognize the text as string in image using pytesserct 
        text = str(((pytesseract.image_to_string(Image.open(filename),lang=lang)))) 
      
        # The recognized text is stored in variable text 
        # Any string processing may be applied on text 
        # Here, basic formatting has been done: 
        # In many PDFs, at line ending, if a word can't 
        # be written fully, a 'hyphen' is added. 
        # The rest of the word is written in the next line 
        # Eg: This is a sample text this word here GeeksF- 
        # orGeeks is half on first line, remaining on next. 
        # To remove this, we replace every '-\n' to ''. 
        text = text.replace('-\n', '')     
      
        # Finally, write the processed text to the file. 
        f.write(text) 
      
    # Close the file after writing all the text. 
    f.close()
    
#filet("d.pdf")
    
    newfile = '/home/root99/Silfra/'+fild+"new.txt"
    new_file = open(newfile,"w")
    f = open(outfile,"r")
    f1 = f.readlines()
    i=1
    for x in f1:
        if not x.strip():
            continue
        
        translation = translator.translate(x,src=lang,dest=to_lang).text

        new_file.write("\n")
        new_file.write(translation)
        
        
        
    new_file.close()
    f.close()
    
    
    
    
    '''
    print(googletrans.LANGUAGES)
{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
'''
