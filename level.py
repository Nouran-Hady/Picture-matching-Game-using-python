from tkinter import *
import random
from tkinter import messagebox

top = Tk()
top.iconbitmap('test.ico')
top.geometry("700x600")
top.title("MEMORY TILE GAME")
top.pack_slaves()
top.configure(bg='#f8edeb')

img = PhotoImage(file="images.png")
lab = Label(top, text="HELLO TO OUR GAME", font=("helvetica", 20, "bold italic"), bg='#f8edeb')
lab.pack(side=TOP)
lab["compound"] = LEFT
lab["image"] = img


def contact():
    label = Label(top, text=("N.Hady@nu.edu.eg", "M.Alsayed@nu.edu.eg"), font=("helvetica", 20, "bold italic"))
    label.pack(side=BOTTOM)
    label.config()


buuttoon = Button(text="start", font=("helvetica", 20, "bold italic"), height=2, width=6, bg='#e5989b',
                  activeforeground="#eaac8b", activebackground="#001427", command=lambda: all_levels(), relief="raised", borderwidth=5).pack(pady=100, side=TOP)
buuttoon2 = Button(text="contact us", font=("helvetica", 20,  "italic"), height=1, width=8, bg='#e5989b', activeforeground="#eaac8b",
                   activebackground="#001427", command=lambda: contact(), relief="raised", borderwidth=5).pack(pady=100, side=BOTTOM)


count = 0
check = winner = 0
score = 0
answer_list = []
answer_dict = {}


def all_levels():
    top.destroy()
    # creating the window
    window_all_levels = Tk()
    window_all_levels.geometry("700x600")
    window_all_levels.title("Welcome to memory tile game")
    window_all_levels.configure(bg='#f8edeb')
    my_frame = Frame(window_all_levels)
    my_frame.pack(pady=10)

    b0 = Button(my_frame, text="level 1", font=('halvetica', 14, 'bold'), height=11, width=16, command=lambda: level1(), bg="#8d99ae",
                fg="red", relief="raised", borderwidth=3)
    b1 = Button(my_frame, text="level 2", font=('halvetica', 14, 'bold'), height=11, width=16, command=lambda: level2(window_all_levels), bg="#2b2d42",
                fg="red", relief="raised", borderwidth=3)
    b2 = Button(my_frame, text="level 3", font=('halvetica', 14, 'bold'), height=11, width=16, command=lambda: level3(window_all_levels), bg="#8d99ae",
                fg="red", relief="raised", borderwidth=3)
    b3 = Button(my_frame, text="level 4", font=('halvetica', 14, 'bold'), height=11, width=16, command=lambda: level4(window_all_levels), bg="#2b2d42",
                fg="red", relief="raised", borderwidth=3)
    b4 = Button(my_frame, text="level 5", font=('halvetica', 14, 'bold'), height=11, width=16, command=lambda: level5(window_all_levels), bg="#8d99ae",
                fg="red", relief="raised", borderwidth=3)
    b5 = Button(my_frame, text="level 6", font=('halvetica', 14, 'bold'), height=11, width=16, command=lambda: level6(window_all_levels), bg="#2b2d42",
                fg="red", relief="raised", borderwidth=3)
    # Griding Buttons
    b0.grid(row=0, column=0)
    b1.grid(row=0, column=1)
    b2.grid(row=0, column=2)
    b3.grid(row=1, column=0)
    b4.grid(row=1, column=1)
    b5.grid(row=1, column=2)

    def level1():

        window_all_levels.destroy()

        # creating the window
        window_level1 = Tk()
        window_level1.iconbitmap('test.ico')
        window_level1.geometry("850x700")
        window_level1.title("Welcome to memory tile game")
        window_level1.configure(bg='#f8edeb')

        # Create button frame
        my_frame = Frame(window_level1)
        my_frame.pack(pady=20)

        image1 = PhotoImage(file=r"test4.png")
        image2 = PhotoImage(file=r"test6.png")
        image3 = PhotoImage(file=r"test7.png")
        # image credits :http://clipart-library.com/cartoon-png.html
        matches = [image1, image1, image2, image2, image3, image3]

        random.shuffle(matches)

        # variables to be used in functions
        count = 0
        winner = 0
        score = 0
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
                b["image"] = matches[number]
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
                            key['image'] = photo
                        answer_dict = {}
                # check if the game has ended
                if winner == 3:
                    def win():
                        label.config(text='well done!')
                        b9 = Button(text="next level", height=4, width=6, command=lambda: level2(window_level1),
                                    relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                    borderwidth=5).pack(padx=0, pady=0, side=RIGHT)

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
        b0 = Button(my_frame, image=photo, height=220, font=("helvetica", 20, "bold italic"), width=190, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
        b1 = Button(my_frame,  image=photo, height=220, font=("helvetica", 20, "bold italic"), width=190, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
        b2 = Button(my_frame, image=photo, height=220, font=("helvetica", 20, "bold italic"), width=190, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
        b3 = Button(my_frame,  image=photo, height=220, font=("helvetica", 20, "bold italic"), width=190, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
        b4 = Button(my_frame,  image=photo, height=220, font=("helvetica", 20, "bold italic"), width=190, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
        b5 = Button(my_frame,  image=photo, height=220, font=("helvetica", 20, "bold italic"), width=190, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)

        # Griding Buttons
        b0.grid(row=1, column=0)
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=2, column=0)

        b4.grid(row=2, column=1)
        b5.grid(row=2, column=2)

        # making quit button
        buttton = Button(window_level1, text="Exit the game",bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=window_level1.destroy)
        buttton.pack(pady=5)
        window_level1.mainloop()


    def level2(b):

        try:
            window_all_levels.destroy()
        except:
            b.destroy()

        # creating the window
        window_level2 = Tk()
        window_level2.iconbitmap('test.ico')
        window_level2.geometry("700x600")
        window_level2.title("Welcome to memory tile game")
        window_level2.configure(bg='#f8edeb')

        # Create button frame
        my_frame = Frame(window_level2)
        my_frame.pack(pady=20)

        matches = ["#003049", "#003049", "#d62828", "#d62828", "#f77f00", "#f77f00", "#fcbf49", "#fcbf49"]
        random.shuffle(matches)

        # variables to be used in functions
        count = 0
        winner = 0

        score = 0
        answer_list = []
        answer_dict = {}

        # to check if the image choices are right or not

        def button_click(b, number):
            global count, answer_dict, answer_list, winner, score
            # to check the number of clicked buttons
            if count < 2:
                # numbers , words  =text #doaa
                # colors=bg#doaa
                # images =image #nouran
                b["bg"] = matches[number]
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
                            key['bg'] = "#0077b6"
                        answer_dict = {}
                # check if the game has ended
                if winner == 7:
                    def win():
                        label.config(text='well done!')
                        b9 = Button(text="next level", height=5, width=6, command=lambda: level3(window_level2),
                                    relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                    borderwidth=5).pack(padx=0, pady=0, side=RIGHT)

                        b10 = Button(text="quit", height=5, width=6, command=lambda: window_level2.destroy,
                                     relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                     borderwidth=5).pack(padx=0, pady=0, side=LEFT)

                        label.config(text='CONGRATULATIONS DEAR')
                        label1.config(text="your final score is:")
                        label2.config(text=str(score))
                    win()

        # some labels
        label = Label(window_level2, font=("Helvetica", 10, "bold italic"), text=" ")
        label.pack()
        label1 = Label(window_level2, font=("Helvetica", 10, "bold"), text=" ")
        label1.pack()
        label2 = Label(window_level2, font=("Helvetica", 10, "bold"), text=" ")
        label2.pack()
        label3 = Label(window_level2, font=("Helvetica", 10, "bold italic"), text=" ")
        label3.pack()

        # adding buttons
        b0 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
        b1 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
        b2 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
        b3 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
        b4 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
        b5 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)
        b6 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b6, 6), relief="raised", borderwidth=5)
        b7 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
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
        buttton = Button(window_level2, text="Exit the game",bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=window_level2.destroy)
        buttton.pack(pady=5)
        window_level2.mainloop()

    def level3(m):
        try:
            window_all_levels.destroy()
        except:
            m.destroy()
        # creating the window
        window_level3 = Tk()
        window_level3.iconbitmap('test.ico')
        window_level3.geometry("700x600")
        window_level3.title("Welcome to memory tile game")
        window_level3.configure(bg='#f8edeb')

        # Create button frame
        my_frame = Frame(window_level3)
        my_frame.pack(pady=20)
        matches = [11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]
        random.shuffle(matches)

        # variables to be used in functions
        count = 0
        winner = 0
        score = 0
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
                            key['text'] = ""
                        answer_dict = {}
                # check if the game has ended
                if winner == 13:
                    def win():
                        label.config(text='well done!')
                        b9 = Button(text="next level", height=5, width=6, command=lambda: level4(window_level3),
                                    relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                    borderwidth=5).pack(side=RIGHT)

                        b10 = Button(text="quit", height=5, width=6, command=lambda: ring_quit(),
                                     relief="raised",bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                     borderwidth=5).pack(side=LEFT)
                        label.config(text='CONGRATULATIONS DEAR')
                        label1.config(text="your final score is:")
                        label2.config(text=str(score))
                    win()
        # some labels
        label = Label(window_level3, font=("Helvetica", 10, "bold italic"), text=" ")
        label.pack()
        label1 = Label(window_level3, font=("Helvetica", 10, "bold"), text=" ")
        label1.pack()
        label2 = Label(window_level3, font=("Helvetica", 10, "bold"), text=" ")
        label2.pack()
        label3 = Label(window_level3, font=("Helvetica", 10, "bold italic"), text=" ")
        label3.pack()

        # adding buttons
        b0 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
        b1 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
        b2 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
        b3 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
        b4 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
        b5 = Button(my_frame,  text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)
        b6 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b6, 6), relief="raised", borderwidth=5)
        b7 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b7, 7), relief="raised", borderwidth=5)
        b8 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b8, 8), relief="raised", borderwidth=5)
        b9 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b9, 9), relief="raised", borderwidth=5)
        b10 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b10, 10), relief="raised", borderwidth=5)
        b11 = Button(my_frame, text=' ', height=4, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b11, 11), relief="raised", borderwidth=5)

        # Griding Buttons
        b0.grid(row=1, column=0)
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)

        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=2, column=3)

        b8.grid(row=3, column=0)
        b9.grid(row=3, column=1)
        b10.grid(row=3, column=2)
        b11.grid(row=3, column=3)

        # function to ring when quit
        def ring_quit():
            def ring():
                b0.bell()

            window_level3.quit()

        # making quit button
        buttton = Button(window_level3, text="Exit the game", bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=ring_quit)
        buttton.pack(pady=5)

        window_level3.mainloop()

    def level4(n):
        try:
            window_all_levels.destroy()
        except:
            n.destroy()
        # creating the window
        window_level4 = Tk()
        window_level4.iconbitmap('test.ico')
        window_level4.geometry("700x600")
        window_level4.title("Welcome to memory tile game")
        window_level4.configure(bg='#f8edeb')

        # Create button frame
        my_frame = Frame(window_level4)
        my_frame.pack(pady=20)
        matches = ["SMILE", "SMILE", "HAPPY", "HAPPY", "CHEERFUL", "CHEERFUL", "JOYFUL", "JOYFUL", "PEACEFUL",
                   "PEACEFUL", "DELIGHTED", "DELIGHTED", "GLAD", "GLAD", "GOOD DAY", "GOOD DAY"]
        random.shuffle(matches)

        # variables to be used in functions
        count = 0
        winner = 0
        score = 0
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
                            key['text'] = ""
                        answer_dict = {}
                # check if the game has ended
                if winner == 21:
                    def win():
                        label.config(text='well done!')
                        b9 = Button(text="next level", height=5, width=6, command=lambda: level5(window_level4),
                                    relief="raised",bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                    borderwidth=5).pack(side=RIGHT)

                        b10 = Button(text="quit", height=5, width=6, command=lambda: window_level4.destroy(),
                                     bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                     relief="raised", borderwidth=5).pack(side=LEFT)
                        conger = Label(window_level4, image=PhotoImage(file=r"cong.jpg")).pack(side=BOTTOM)
                        conger.config()
                        label.config(text='CONGRATULATIONS DEAR')
                        label1.config(text="your final score is:")
                        label2.config(text=str(score))

                    win()

        # some labels
        label = Label(window_level4, font=("Helvetica", 10, "bold italic"), text=" ")
        label.pack()
        label1 = Label(window_level4, font=("Helvetica", 10, "bold"), text=" ")
        label1.pack()
        label2 = Label(window_level4, font=("Helvetica", 10, "bold"), text=" ")
        label2.pack()
        label3 = Label(window_level4, font=("Helvetica", 10, "bold italic"), text=" ")
        label3.pack()

        # adding buttons
        b0 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
        b1 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
        b2 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
        b3 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
        b4 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
        b5 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)
        b6 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b6, 6), relief="raised", borderwidth=5)
        b7 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b7, 7), relief="raised", borderwidth=5)
        b8 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b8, 8), relief="raised", borderwidth=5)
        b9 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b9, 9), relief="raised", borderwidth=5)
        b10 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b10, 10), relief="raised", borderwidth=5)
        b11 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b11, 11), relief="raised", borderwidth=5)
        b12 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b12, 12), relief="raised", borderwidth=5)
        b13 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b13, 13), relief="raised", borderwidth=5)
        b14 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b14, 14), relief="raised", borderwidth=5)
        b15 = Button(my_frame, text=' ', height=4, font=("helvetica", 10, "bold italic"), width=9, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b15, 15), relief="raised", borderwidth=5)

        # Griding Buttons
        b0.grid(row=1, column=0)
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)

        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=2, column=3)

        b8.grid(row=3, column=0)
        b9.grid(row=3, column=1)
        b10.grid(row=3, column=2)
        b11.grid(row=3, column=3)

        b12.grid(row=4, column=0)
        b13.grid(row=4, column=1)
        b14.grid(row=4, column=2)
        b15.grid(row=4, column=3)

        # making quit button
        buttton = Button(window_level4, text="Exit the game", bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=window_level4.quit)
        buttton.pack(pady=5)

        window_level4.mainloop()

    def level5(d):
        try:
            window_all_levels.destroy()
        except:
            d.destroy()
        # creating the window
        window_level5 = Tk()
        # window_level5.iconbitmap('test.ico')
        window_level5.geometry("700x600")
        window_level5.title("Welcome to memory tile game")
        window_level5.configure(bg='#f8edeb')

        # Create button frame
        my_frame = Frame(window_level5)
        my_frame.pack(pady=20)
        matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,10, 10]
        random.shuffle(matches)

        # variables to be used in functions
        count = 0
        winner = 0
        score = 0
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
                if winner == 31:
                    def win():
                        label.config(text='well done!')
                        b9 = Button(text="next level", height=5, width=6, command=lambda: level6(window_level5),
                                    relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                    borderwidth=5).pack(side=RIGHT)

                        b10 = Button(text="quit", height=5, width=6, command=lambda: window_level5.destroy(),
                                     relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                     borderwidth=5).pack(side=LEFT)
                        conger = Label(window_level5, image=PhotoImage(file=r"cong.jpg")).pack(side=BOTTOM)
                        conger.config()
                        label.config(text='CONGRATULATIONS DEAR')
                        label1.config(text="your final score is:")
                        label2.config(text=str(score))

                    win()

        # some labels
        label = Label(window_level5, font=("Helvetica", 10, "bold italic"), text=" ")
        label.pack()
        label1 = Label(window_level5, font=("Helvetica", 10, "bold"), text=" ")
        label1.pack()
        label2 = Label(window_level5, font=("Helvetica", 10, "bold"), text=" ")
        label2.pack()
        label3 = Label(window_level5, font=("Helvetica", 10, "bold italic"), text=" ")
        label3.pack()

        # adding buttons
        b0 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
        b1 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
        b2 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
        b3 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
        b4 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
        b5 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)
        b6 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b6, 6), relief="raised", borderwidth=5)
        b7 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b7, 7), relief="raised", borderwidth=5)
        b8 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b8, 8), relief="raised", borderwidth=5)
        b9 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b9, 9), relief="raised", borderwidth=5)
        b10 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b10, 10), relief="raised", borderwidth=5)
        b11 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b11, 11), relief="raised", borderwidth=5)
        b12 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b12, 12), relief="raised", borderwidth=5)
        b13 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b13, 13), relief="raised", borderwidth=5)
        b14 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b14, 14), relief="raised", borderwidth=5)
        b15 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b15, 15), relief="raised", borderwidth=5)
        b16 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b16, 16), relief="raised", borderwidth=5)
        b17 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b17, 17), relief="raised", borderwidth=5)
        b18 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b18, 18), relief="raised", borderwidth=5)
        b19 = Button(my_frame, text=' ', height=3, font=("helvetica", 20, "bold italic"), width=6, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b19, 19), relief="raised", borderwidth=5)

        # Griding Buttons
        b0.grid(row=1, column=0)
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)
        b4.grid(row=1, column=4)

        b5.grid(row=2, column=0)
        b6.grid(row=2, column=1)
        b7.grid(row=2, column=2)
        b8.grid(row=2, column=3)
        b9.grid(row=2, column=4)

        b10.grid(row=3, column=0)
        b11.grid(row=3, column=1)
        b12.grid(row=3, column=2)
        b13.grid(row=3, column=3)
        b14.grid(row=3, column=4)

        b15.grid(row=4, column=0)
        b16.grid(row=4, column=1)
        b17.grid(row=4, column=2)
        b18.grid(row=4, column=3)
        b19.grid(row=4, column=4)

        # function to ring when quit
        def ring_quit():
            def ring():
                b0.bell()

            window_level5.quit()

        # making quit button
        buttton = Button(window_level5, text="Exit the game", bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=ring_quit)
        buttton.pack(pady=5)

        window_level5.mainloop()

    def level6(d):
        try:
            window_all_levels.destroy()
        except:
            d.destroy()
        # creating the window
        window_level6 = Tk()
        # window_level6.iconbitmap('test.ico')
        window_level6.geometry("700x600")
        window_level6.title("Welcome to memory tile game")
        window_level6.configure(bg='#f8edeb')

        # Create button frame
        my_frame = Frame(window_level6)
        my_frame.pack(pady=20)

        image1 = PhotoImage(file=r"test1.png")
        image2 = PhotoImage(file=r"test2.png")
        image3 = PhotoImage(file=r"test3.png")
        image4 = PhotoImage(file=r"test4.png")
        image5 = PhotoImage(file=r"test5.png")
        image6 = PhotoImage(file=r"test6.png")
        image7 = PhotoImage(file=r"test7.png")
        image8 = PhotoImage(file=r"test8.png")
        image9 = PhotoImage(file=r"test9.png")
        image10 = PhotoImage(file=r"test10.png")
        image11 = PhotoImage(file=r"test11.png")
        image12 = PhotoImage(file=r"test12.png")





        # image credits :http://clipart-library.com/cartoon-png.html
        matches = [image1, image1, image2, image2, image3, image3, image4,image4,image5,image5,
                   image6,image6,image7,image7,image8,image8,image9,image9,image10,image10,image11,image11,image12,image12]

        random.shuffle(matches)

        # variables to be used in functions
        count = 0
        winner = 0
        score = 0
        answer_list = []
        answer_dict = {}

        # to check if the image choices are right or not

        def button_click(b, number):
            global count, answer_dict, answer_list, winner, score
            count5 =0
            # to check the number of clicked buttons
            if count < 2:
                # numbers , words  =text
                # colors=bg
                # images =image
                b["image"] = matches[number]
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
                        winner +=1
                        count5+=1
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
                            key['image'] = photo
                        answer_dict = {}
                # check if the game has ended
                if winner == 43 or winner==12:
                    def win():
                        label.config(text='well done!')
                        b10 = Button(text="quit", height=5, width=6, command=lambda: window_level6.destroy(),
                                     relief="raised", bg='#e5989b', activeforeground="#eaac8b", activebackground="#001427",
                                     borderwidth=5).pack(side=LEFT)
                        conger = Label(window_level6, image=PhotoImage(file=r"cong.jpg")).pack(side=BOTTOM)
                        label.config(text='CONGRATULATIONS DEAR')
                        label1.config(text="your final score is:")
                        label2.config(text=str(score))

                    win()

        # some labels
        label = Label(window_level6, font=("Helvetica", 10, "bold italic"), text=" ")
        label.pack()
        label1 = Label(window_level6, font=("Helvetica", 10, "bold"), text=" ")
        label1.pack()
        label2 = Label(window_level6, font=("Helvetica", 10, "bold"), text=" ")
        label2.pack()
        label3 = Label(window_level6, font=("Helvetica", 10, "bold italic"), text=" ")
        label3.pack()

        # image of the buttons
        photo = PhotoImage(file=r"python.png")

        # adding buttons
        b0 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b0, 0), relief="raised", borderwidth=5)
        b1 = Button(my_frame,image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b1, 1), relief="raised", borderwidth=5)
        b2 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b2, 2), relief="raised", borderwidth=5)
        b3 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b3, 3), relief="raised", borderwidth=5)
        b4 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b4, 4), relief="raised", borderwidth=5)
        b5 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b5, 5), relief="raised", borderwidth=5)
        b6 = Button(my_frame,image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b6, 6), relief="raised", borderwidth=5)
        b7 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b7, 7), relief="raised", borderwidth=5)
        b8 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b8, 8), relief="raised", borderwidth=5)
        b9 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                    fg="#fdfffc", command=lambda: button_click(b9, 9), relief="raised", borderwidth=5)
        b10 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b10, 10), relief="raised", borderwidth=5)
        b11 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b11, 11), relief="raised", borderwidth=5)
        b12 = Button(my_frame,image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b12, 12), relief="raised", borderwidth=5)
        b13 = Button(my_frame,image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b13, 13), relief="raised", borderwidth=5)
        b14 = Button(my_frame,image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b14, 14), relief="raised", borderwidth=5)
        b15 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b15, 15), relief="raised", borderwidth=5)
        b16 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b16, 16), relief="raised", borderwidth=5)
        b17 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b17, 17), relief="raised", borderwidth=5)
        b18 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b18, 18), relief="raised", borderwidth=5)
        b19 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b19, 19), relief="raised", borderwidth=5)
        b20 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b20, 20), relief="raised", borderwidth=5)
        b21 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b21, 21), relief="raised", borderwidth=5)
        b22 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b22, 22), relief="raised", borderwidth=5)
        b23 = Button(my_frame, image=photo, height=140, font=("helvetica", 20, "bold italic"), width=150, bg="#0077b6",
                     fg="#fdfffc", command=lambda: button_click(b23, 23), relief="raised", borderwidth=5)

        # Griding Buttons
        b0.grid(row=1, column=0)
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)
        b4.grid(row=1, column=4)
        b5.grid(row=1, column=5)

        b6.grid(row=2, column=0)
        b7.grid(row=2, column=1)
        b8.grid(row=2, column=2)
        b9.grid(row=2, column=3)
        b10.grid(row=2, column=4)
        b11.grid(row=2, column=5)

        b12.grid(row=3, column=0)
        b13.grid(row=3, column=1)
        b14.grid(row=3, column=2)
        b15.grid(row=3, column=3)
        b16.grid(row=3, column=4)
        b17.grid(row=3, column=5)

        b18.grid(row=4, column=0)
        b19.grid(row=4, column=1)
        b20.grid(row=4, column=2)
        b21.grid(row=4, column=3)
        b22.grid(row=4, column=4)
        b23.grid(row=4, column=5)


        # making quit button
        buttton = Button(window_level6, text="Exit the game", bg='#e5989b', activeforeground="#eaac8b",
                         activebackground="#001427", command=window_level6.destroy)
        buttton.pack(pady=5)

        window_level6.mainloop()
    window_all_levels.mainloop()
top.mainloop()
