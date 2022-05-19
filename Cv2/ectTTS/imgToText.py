import PyPDF2
import pyttsx3
import speech_recognition as sr
import cv2
import pytesseract as pt


def pdfToText(pdfFile, page, pageCount=False):
    pdfFileObj = open(pdfFile, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pageObj = pdfReader.getPage(page) 
    text = str(pageObj.extractText()) 
    pdfFileObj.close()
    if pageCount == True:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
        print(pdfReader.numPages) 
    pdfFileObj.close()
    return text

def speakText(text, voice, saveName, speak=True, saveToFile=True):    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    if saveToFile == True:
        engine.save_to_file(text, saveName)
    if speak == True:
        engine.say(text)
    engine.runAndWait()
    engine.stop()

def micCheck():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        text = r.recognize_google(audio)
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text

def imgToText(img, read=False):
    img = cv2.imread(img)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    pt.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\Tesseract.exe'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()
    file = open("Cv2\ectTTS\Recognized.txt", "w+", encoding='utf-8')
    file.write("")
    file.close()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        file = open("Cv2\ectTTS\Recognized.txt", "a", encoding='utf-8')
        text = pt.image_to_string(cropped)
        file.write(text)
        file.write("\n")
        file.close
    if read == True:
        speakText(text, 1, 'Cv2\ectTTS\Testoration.wav')    
    cv2.imshow('Image', im2)
    cv2.waitKey(0)

pdfPath = 'Cv2\ectTTS\example.pdf'
imgPath = 'Cv2\ectTTS\Testpage.jpg'
imgToText(imgPath, read=True)