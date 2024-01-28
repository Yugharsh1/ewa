from tkinter import *

root=Tk()
root.title("Fibonacci")
root.geometry("500x500")
enter_number=Entry(root)
label1=Label(root, text="Fibonacci series: ")
label2=Label(root, text="Fibonacci sum: ")
def Fibonacci():
    input=int(enter_number.get())
    first_number=0
    second_number=1
    sum=0
    counter=1
    sum2=0
    while(counter <= input):
        label1["text"]+=str(sum)+" "
        label2["text"]="Fibonacci sum: "+str(sum2)
        counter=counter+1
        first_number=second_number
        second_number=sum
        sum=first_number+second_number
        sum2=sum2+sum
enter_number.pack()
btn=Button(root, text="show fibonacci series", command=Fibonacci,bg='Brown', fg='Yellow')
btn.pack()
label1.pack()
label2.pack()
root.mainloop()