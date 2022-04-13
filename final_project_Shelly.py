import tkinter as tk
from tkinter import *
import math, pyperclip 
import os
from tkinter.messagebox import *



""" Create Tkinter """
root = tk.Tk()
root.geometry("800x600+30+30")
strChoose = StringVar()
root.title("Shelly")
root.resizable(width=FALSE, height=FALSE)



##################################################################


""" Functions for display text on screen """

""" 1)encryption """
def Onscreen_encrypt():
    text = str(textBox.get("1.0", "end-1c"))
    key = int(textBox1.get("1.0", "end-1c"))
    x = encryptMessage(text,key)
   

    result = askquestion("ImageEditor1.0","Display result on screen(Yes)/ create new file result(No)")
    if (result == "yes"):
         encrypt(x)
         
    if (result == "no"):
         save_file_encryption()
         showinfo("About ImageEditor1.0","The encrypted file is saved!")





""" 2)decryption """ 
def Onscreen_decrypt():
    cipher = str(textBox.get("1.0", "end-1c"))
    key = int(textBox1.get("1.0", "end-1c"))
    x = decryptMessage(cipher,key)

    result = askquestion("ImageEditor1.0","Display result on screen(Yes) / create new file result(No)")
    if (result == "yes"):
         decrypt(x)

         
    if (result == "no"):
         save_file_decryption()
         showinfo("About ImageEditor1.0","The decrypted file is saved!")






""" 3)decryption without key - brute force """ 
def Onscreen_brute_force():
    message = str(textBox.get("1.0", "end-1c"))
   

    result = askquestion("ImageEditor1.0","Display result on screen (Yes) / create new file result (No)")
    if (result == "yes"):
        brute_force(message)

         
    if (result == "no"):
         save_file_No_Key(message)
         showinfo("About ImageEditor1.0","The decrypted file (without the key) is saved!")



#############################################################################################


""" Functions to read from file and display on screen """

""" 1)encryption """
def Read_from_file_encrypt():
    text = open_file_text()
    key = open_file_key()
    x = encryptMessage(text,key)
    
    result = askquestion("ImageEditor1.0","Display result on screen (yes) / create new file result (no)")
    if (result == "yes"):
         encrypt(x)

    if (result == "no"):
         file=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
         f = open(file,'w')
         f.write(x)
         showinfo("About ImageEditor1.0","The encrypted file is saved!")
         f.close()
        

   

""" 2)decryption """ 
def Read_from_file_decrypt():
    cipher = open_file_text()
    key = open_file_key()
    x = decryptMessage(cipher,key)
    
    result = askquestion("ImageEditor1.0","Display result on screen (yes) / create new file result (no)")
    if (result == "yes"):
         decrypt(x)
     
    if (result == "no"):
         file=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
         f = open(file,'w')
         f.write(x)
         showinfo("About ImageEditor1.0","The decrypted file is saved!")
         f.close()
        



""" 3)decryption without key - brute force """
def Read_from_file_brute_force():
    showinfo("About ImageEditor1.0","Open text file!")
    file = root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    with open(file,'r') as x:
     text = x.read()
    
    result = askquestion("ImageEditor1.0","Display result on screen (yes) / create new file result (no)")
    if (result == "yes"):
         brute_force(text)
     
    if (result == "no"):
         save_file_No_Key(text)
        
         


##################################################################

""" 1. Encryption - Function for performing the encryption """
def encryptMessage(text,key):


     rail = [['\n' for i in range(len(text))]
                   for j in range(key)]
       
    # to find the direction
     dir_down = False
     row, col = 0, 0
       
     for i in range(len(text)):
          
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
         if (row == 0) or (row == key - 1):
             dir_down = not dir_down
          
        # fill the corresponding alphabet
         rail[row][col] = text[i]
         col += 1
          
        # find the next row using
        # direction flag
         if dir_down:
             row += 1
         else:
             row -= 1
    # now we can construct the cipher 
    # using the rail matrix
     result = []
     for i in range(key):
         for j in range(len(text)):
             if rail[i][j] != '\n':
                 result.append(rail[i][j])
     return("" . join(result))



#################################################################


""" 2. Deciphering - Function to perform the decoding """
def decryptMessage(cipher,key):

    rail = [['\n' for i in range(len(cipher))] 
                  for j in range(key)]
      
    # to find the direction
    dir_down = None
    row, col = 0, 0
      
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
          
        # place the marker
        rail[row][col] = '*'
        col += 1
          
        # find the next row 
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
              
    # now we can construct the 
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
          
    # now read the matrix in 
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
          
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
              
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
              
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))



#################################################################


""" 3. Keyless decryption  - Function for performing the decryption without a key """

def brute_force(msg):

    newWindow = Tk()
    newWindow.title("brute_force")
    newWindow.geometry("320x500")
    
    T = Text(newWindow, height = 26, width = 52)
    T.pack()
    
    z = tk.Button(newWindow,bg="ForestGreen",fg="white",font="none 10",text = "Exit",command =newWindow.destroy).pack()
    
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(letters)):


        translated = ''

        for symbol in msg:

             if symbol in letters:

                num = letters.find(symbol) # get the number of the symbol

                num = num - key


                if num < 0:

                  num = num + len(letters)
              
              
                translated = translated + letters[num]


             else:
                translated = translated + symbol

        T.insert(tk.END, 'key #')
        T.insert(tk.END, key)
        T.insert(tk.END,' ' )
        T.insert(tk.END, translated)
        T.insert(tk.END,'\n')



##################################################################



""" Function responsible for displaying the encryption on the screen """
def encrypt(x):
    res["text"]= x
    

""" Function responsible for displaying the decoding on the screen """
def decrypt(x):
    res["text"]= x




#################################################################



""" Function responsible for transferring the encryption to the file  """
def File_encryption():
    text = str(textBox.get("1.0", "end-1c"))
    key = int(textBox1.get("1.0", "end-1c"))
    x = encryptMessage(text,key)
    return x


""" Function responsible for transferring the decoding to a file """
def File_Decoding():
    cipher = str(textBox.get("1.0", "end-1c"))
    key = int(textBox1.get("1.0", "end-1c"))
    x = decryptMessage(cipher,key)
    return x


""" Function responsible for transferring the decoding (without key) to a file """
def File_Decoding_No_Key():
    cipher = str(textBox.get("1.0", "end-1c"))
    x = brute_force(cipher)
    return x


""" Function responsible for transferring the key to a file """
def File_Key():
    key = int(textBox1.get("1.0", "end-1c"))
    return str(key)



#################################################################


""" Function for saving encrypted content in a file """
def save_file_encryption():  
    file=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
    f = open(file,'w')
    f.write(File_encryption())
    f.close()

    result = askyesno("TextEditor1.0","Do you want to save the key?")
    if (result==1):
       file1=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
       f1 = open(file1,'w')
       f1.write(File_Key())
       f1.close()



""" Function for saving decoded content in a file """
def save_file_decryption():  
    file=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
    f = open(file,'w')
    f.write(File_Decoding())
    f.close()

    result = askyesno("TextEditor1.0","Do you want to save the key?")
    if (result==1):
       file1=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
       f1 = open(file1,'w')
       f1.write(File_Key())
       f1.close()




""" Function for saving decoded content (without key) in a file """
def save_file_No_Key(msg):  
    file_save_res=root.call("tk_getSaveFile",'-initialdir','c:\\','-title', 'Save a file')
    f_r = open(file_save_res,'w')

    
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(letters)):


        translated = ''

        for symbol in msg:

             if symbol in letters:

                num = letters.find(symbol) # get the number of the symbol

                num = num - key


                if num < 0:

                  num = num + len(letters)
              
              
                translated = translated + letters[num]


             else:
                translated = translated + symbol
                
        f_r.write("key # " + str(key) + " " + str(translated) + "\n")

    f_r.close()


#################################################################


""" Read from file - text """
def open_file_text():
    showinfo("About ImageEditor1.0","Open text file!")
    file = root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    with open(file,'r') as x:
     text = x.read()
     return str(text)


""" Read from file - key """
def open_file_key():
    showinfo("About ImageEditor1.0","Open key file!")
    file = root.call("tk_getOpenFile",'-initialdir','c:\\','-title', 'Open a file')
    with open(file,'r') as x:
     key = x.read()
     return int(key)



#################################################################


""" Error handling - check text and key - encryption """
def check_text_and_key_encrypt():
    text = textBox.get("1.0", "end-1c")
    key = textBox1.get("1.0", "end-1c")

    
    if len(text) < 1 and len(key) < 1:
       res["text"]="You need to input text and key!"
       return

    elif len(text) < 1:
         res["text"]="You need to input some text!"
         return

    elif len(key) < 1:
         res["text"]="You need to input some digit!"
         return

    elif text.isdigit() and key.isalpha():
         res["text"]="Both inputs are invalid.. They must be repaired!"
         return 

    elif text.isdigit():
         res["text"]="You need to write here some text! (input 1)"
         return 
        
    elif key.isalpha():
         res["text"]="You need to write here some digits! (input 2)"
         return
   
    else:
       res["text"]=" "
       Onscreen_encrypt()






""" Error handling - check text and key - decryption """
def check_text_and_key_decrypt():
    text = textBox.get("1.0", "end-1c")
    key =  textBox1.get("1.0", "end-1c")


    if len(text) < 1 and len(key) < 1:
       res["text"]="You need to input text and key!"
       return

    elif len(text) < 1:
         res["text"]="You need to input some text!"
         return

    elif len(key) < 1:
         res["text"]="You need to input some digit!"
         return

    elif text.isdigit() and key.isalpha():
         res["text"]="Both inputs are invalid.. They must be repaired!"
         return 

    elif text.isdigit():
         res["text"]="You need to write here some text! (input 1)"
         return 
        
    elif key.isalpha():
         res["text"]="You need to write here some digits! (input 2)"
         return
    
    else:
       res["text"]=" "
       Onscreen_decrypt()






""" Error handling - check text without key - decryption """
def check_text_No_key_decrypt():
    text = textBox.get("1.0", "end-1c")
    key = textBox1.get("1.0", "end-1c")

    if len(text) < 1:
         res["text"]="You need to input some text!"
         return

    elif text.isdigit():
         res["text"]="You need to write here some text! (input 1)"
         return

    elif len(key) > 0:
         res["text"]="You can`t input key! please delete the key.. (input 2)"
         return

        
    else:
       res["text"]=" "
       Onscreen_brute_force()
       

##################################################################


""" A function that interprets the software """
def refresh():
    
    result = askquestion("ImageEditor1.0","Do you want to exit (Yes) or refresh the program (No) ?")
    if (result == "yes"):
        root.destroy()
         
    if (result == "no"):
        root.destroy()
        os.popen("final_project_Shelly.py")

   

##################################################################
        
""" Function for selecting user options """
def list_box_options(item):

    w = item.widget
    index = int(w.curselection()[0])
    
    if index == 0:
        showinfo("About ImageEditor1.0","Please input some text and key!")
        optionsRadio1()
    
        
    elif index == 2:
        optionsRadio2()
      
    
##################################################################

""" Options Radios """
  

""" Points to choose from - on screen display (input text and key) """
def optionsRadio1():
    strChoose.set("some text")
    rb1=Radiobutton(root, text="Encryption", variable=strChoose, value="Encryption", command=check_text_and_key_encrypt)#  הצפנה
    rb1.pack()
    rb2=Radiobutton(root, text="Deciphering", variable=strChoose, value ="Deciphering", command=check_text_and_key_decrypt)# פענוח
    rb2.pack()
    rb3=Radiobutton(root, text="brute force", variable=strChoose, value ="brute force", command=check_text_No_key_decrypt)# ניסיון לפענוח ללא מפתח
    rb3.pack()



""" Points to choose from - on screen display (Read from file) """
def optionsRadio2():
    strChoose.set("some text")
    rb1=Radiobutton(root, text="Encryption", variable=strChoose, value="Encryption", command=Read_from_file_encrypt)#  הצפנה
    rb1.pack()
    rb2=Radiobutton(root, text="Deciphering", variable=strChoose, value ="Deciphering", command=Read_from_file_decrypt)# פענוח
    rb2.pack()
    rb3=Radiobutton(root, text="brute force", variable=strChoose, value ="brute force", command=Read_from_file_brute_force)# ניסיון לפענוח ללא מפתח
    rb3.pack()



##################################################################

""" Like Main """
    
""" Main Title """
main = tk.Label(root,font="none 17 bold",pady=20,fg="ForestGreen",text="Encryption and decryption: ")
main.pack()


option = tk.Label(root,font="none 13",pady=10,text='Choose ONE option: ')
option.pack()


""" here we create listBox + fuction to choice what you need = how much words or letters or spaces """
listBox = Listbox(root, height=3, width=84, font="none 10 bold", fg="white", bg="ForestGreen")
listBox.insert(0, '1) Type a message and key and print the result on the screen / create a new file.  (Text+Key)')
listBox.insert(1, '--------------------------------------------------------------------------------------------------------------------------------------------------------')
listBox.insert(2, '2) Receive a message from a file and display it on the screen / create a new file.  (Text+Key)')
listBox.pack()
listBox.bind('<<ListboxSelect>>',list_box_options)




""" Title input 1 """
inputText = tk.Label(root,font="none 11",pady=9,text="Type text for encryption or decryption: ")
inputText.pack()

""" Input 1 - Cipher / Decryption """
textBox=tk.Text(root,height = 4,width=40)
textBox.pack()

        
""" Title 2 """
inputKey = tk.Label(root,font="none 11",pady=9,text='Type a key: (In digits) ')
inputKey.pack()


""" Input 2 - Key """
textBox1=tk.Text(root,height = 4, width=40)
textBox1.pack()



        
""" show results """

""" Result title """
resultTitle = tk.Label(root,font="none 11",pady=12,text='Result: ')
resultTitle.pack()


res=Label(root,bg="LightCoral",width=42,pady=5,fg="white",font='none 11 bold')
res.pack()


""" space between """
space = tk.Label(root,pady=2)
space.pack()


""" click to button for exit or refresh the program """
exitOrRef = tk.Button(root,text = "Exit / Refresh the program",font="none 10 bold",command = refresh,bg="ForestGreen",fg="white")
exitOrRef.pack()


""" space between """
space1 = tk.Label(root,pady=1)
space1.pack()


root.mainloop()
