from tkinter import *
import random
from tkinter import messagebox

# creating the window
window_level1 = Tk()
window_level1.iconbitmap('test.ico')
window_level1.geometry("850x700")
window_level1.title("Welcome to memory tile game")
window_level1.configure(bg='#f8edeb')

# Create button frame
my_frame = Frame(window_level1)
my_frame.pack(pady=20)
# image1 = PhotoImage(file=r"test4.png")
# image2 = PhotoImage(file=r"test6.png")
# image3 = PhotoImage(file=r"test7.png")
# # image credits :http://clipart-library.com/cartoon-png.html
matches = ["x", "x", "x", "x","o","o",'o', "o"]

random.shuffle(matches)

# variables to be used in functions
count = winner = score = 0
answer_list = []
answer_dict = {}
# to check if the image choices are right or not

def button_click(b, number):
            global count, answer_dict, answer_list, winner, score
            # to check the number of clicked buttons
            if count < 2:
                # numbers , words  =text #doaa
                # colors=bg#doaa
                # images =image
                b["text"] = matches[number]
                # appending answers to list to compare between answers
                answer_list.append(number)
                answer_dict[b] = matches[number]
                # updating our counter
                count += 1

                # checking the answers
                if count == 2:
                    if matches[answer_list[0]] == matches[answer_list[1]]:
                        label.config(text="correct!")
                        score += 5
                        winner += 1
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        for key in answer_dict:
                            key['state'] = 'disabled'
                        label1.config(text="your score :")
                        label2.config(text=str(score))

                    else:
                        label.config(text='try again!!')
                        messagebox.showinfo("wrong!")
                        count = 0
                        answer_list = []
                        for key in answer_dict:
                            # reset the key['text'] value in answer_dict to play again
                            key['text'] = " "
                        answer_dict = {}
                # check if the game has ended
                if winner == 3:
                    def win():
                        label.config(text='well done!')

                        b10 = Button(text="quit", height=4, width=6, command=lambda: window_level1.quit(),
                                     relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                     borderwidth=5).pack(padx=0, pady=0, side=LEFT)

                        label.config(text='CONGRATULATIONS DEAR')
                        label1.config(text="your final score is:")
                        label2.config(text=str(score))

                    win()

# image of the buttons
photo = PhotoImage(file=r"python.png")

# some labels
label = Label(window_level1, font=("Helvetica", 10, "bold italic"), text=" ")
label.pack()
label1 = Label(window_level1, font=("Helvetica", 10, "bold"), text=" ")
label1.pack()
label2 = Label(window_level1, font=("Helvetica", 10, "bold"), text=" ")
label2.pack()
label3 = Label(window_level1, font=("Helvetica", 10, "bold italic"), text=" ")
label3.pack()

# adding buttons
b0 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
b1 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
b2 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
b3 = Button(my_frame,  text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
b4 = Button(my_frame,  text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
b5 = Button(my_frame,  text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)
b6 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b6, 6), relief="raised", borderwidth=5)
b7 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b7, 7), relief="raised", borderwidth=5)


# Griding Buttons
b0.grid(row=1, column=0)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=2, column=3)

        # making quit button
buttton = Button(window_level1, text="Exit the game",bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=window_level1.destroy)
buttton.pack(pady=5)
window_level1.mainloop()

