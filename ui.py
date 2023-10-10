import decimal

import customtkinter
import evaluate
import tkinter
from PIL import Image

WINDOW_DIMENSIONS = "450x700"
APP_NAME = "Calcu-LLama"
APP_BG_IMAGE = "llama.jpg"

SCREEN_WIDTH = 230
SCREEN_HEIGHT = 50
MAX_SCREEN_CHARS = 9
SCREEN_FONT = "PT Mono"
SCREEN_FONT_SIZE = 36
SCREEN_TEXT_COLOR = "light green"
SCREEN_FG_COLOR = "black"
SCREEN_BG_COLOR = "white"

BUTTON_HEIGHT = 50
BUTTON_WIDTH = 50
BUTTON_FONT = "PT Mono"
BUTTON_FONT_SIZE = 36
BUTTON_FG_COLOR = "black"
BUTTON_BG_COLOR = "white"
BUTTON_HOVER_COLOR = "#fb7289"


class Ui:

    def __init__(self):
        ctk = customtkinter.CTk()
        ctk.geometry(WINDOW_DIMENSIONS)
        ctk.title(APP_NAME)

        self.expression = ""
        self.screen_display = "0"
        self.brackets_open = 0

        llama = customtkinter.CTkImage(dark_image=Image.open(APP_BG_IMAGE), size=(450, 700))
        llama_label = customtkinter.CTkLabel(master=ctk, image=llama, width=450, height=700, text="", anchor=tkinter.NW)
        llama_label.place(x=0, y=0, anchor=tkinter.NW)

        self.screen = customtkinter.CTkLabel(master=ctk, text=self.screen_display,
                                             width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
                                             fg_color=SCREEN_FG_COLOR, bg_color=SCREEN_BG_COLOR, corner_radius=10,
                                             text_color=SCREEN_TEXT_COLOR,
                                             font=(SCREEN_FONT, SCREEN_FONT_SIZE),
                                             anchor=tkinter.E, )

        self.screen.place(x=115, y=140, anchor=tkinter.NW)

        zero_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                              text="0", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                              fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                              hover_color=BUTTON_HOVER_COLOR,
                                              command=self.enter_zero)

        zero_button.place(x=115, y=660, anchor=tkinter.SW)

        point_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text=".", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.enter_point)

        point_button.place(x=175, y=660, anchor=tkinter.SW)

        equals_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                text="=", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                                fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                                hover_color=BUTTON_HOVER_COLOR,
                                                command=self.calculate)

        equals_button.place(x=235, y=660, anchor=tkinter.SW)

        plus_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                              text="+", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                              fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                              hover_color=BUTTON_HOVER_COLOR,
                                              command=self.enter_plus)

        plus_button.place(x=295, y=660, anchor=tkinter.SW)

        one_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                             text="1", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                             fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                             hover_color=BUTTON_HOVER_COLOR,
                                             command=self.enter_one)

        one_button.place(x=115, y=600, anchor=tkinter.SW)

        two_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                             text="2", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                             fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                             hover_color=BUTTON_HOVER_COLOR,
                                             command=self.enter_two)

        two_button.place(x=175, y=600, anchor=tkinter.SW)

        three_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text="3", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.enter_three)

        three_button.place(x=235, y=600, anchor=tkinter.SW)

        minus_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text="-", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.enter_minus)

        minus_button.place(x=295, y=600, anchor=tkinter.SW)

        four_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                              text="4", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                              fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                              hover_color=BUTTON_HOVER_COLOR,
                                              command=self.enter_four)

        four_button.place(x=115, y=540, anchor=tkinter.SW)

        five_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                              text="5", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                              fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                              hover_color=BUTTON_HOVER_COLOR,
                                              command=self.enter_five)

        five_button.place(x=175, y=540, anchor=tkinter.SW)

        six_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                             text="6", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                             fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                             hover_color=BUTTON_HOVER_COLOR,
                                             command=self.enter_six)

        six_button.place(x=235, y=540, anchor=tkinter.SW)

        times_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text="x", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.enter_times)

        times_button.place(x=295, y=540, anchor=tkinter.SW)

        seven_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text="7", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.enter_seven)

        seven_button.place(x=115, y=480, anchor=tkinter.SW)

        eight_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text="8", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.enter_eight)

        eight_button.place(x=175, y=480, anchor=tkinter.SW)

        nine_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                              text="9", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                              fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                              hover_color=BUTTON_HOVER_COLOR,
                                              command=self.enter_nine)

        nine_button.place(x=235, y=480, anchor=tkinter.SW)

        divide_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                text="÷", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                                fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                                hover_color=BUTTON_HOVER_COLOR,
                                                command=self.enter_divide)

        divide_button.place(x=295, y=480, anchor=tkinter.SW)

        open_bracket_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                      text="(", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                                      fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                                      hover_color=BUTTON_HOVER_COLOR,
                                                      command=self.enter_open_bracket)

        open_bracket_button.place(x=115, y=420, anchor=tkinter.SW)

        close_bracket_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                                       text=")", font=(BUTTON_FONT, BUTTON_FONT_SIZE),
                                                       fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                                       hover_color=BUTTON_HOVER_COLOR,
                                                       command=self.enter_close_bracket)

        close_bracket_button.place(x=175, y=420, anchor=tkinter.SW)

        del_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                             text="del", font=(BUTTON_FONT, 20),
                                             fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                             hover_color=BUTTON_HOVER_COLOR,
                                             command=self.delete)

        del_button.place(x=235, y=420, anchor=tkinter.SW)

        clear_button = customtkinter.CTkButton(master=ctk, height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                               text="clear", font=(BUTTON_FONT, 12),
                                               fg_color=BUTTON_FG_COLOR, bg_color=BUTTON_BG_COLOR,
                                               hover_color=BUTTON_HOVER_COLOR,
                                               command=self.clear)

        clear_button.place(x=295, y=420, anchor=tkinter.SW)

        ctk.mainloop()

    def enter_one(self):
        if self.screen_display == "0":
            self.screen_display = "1"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "1"
        self.screen.configure(text=self.screen_display)

    def enter_two(self):
        if self.screen_display == "0":
            self.screen_display = "2"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "2"
        self.screen.configure(text=self.screen_display)

    def enter_three(self):
        if self.screen_display == "0":
            self.screen_display = "3"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "3"
        self.screen.configure(text=self.screen_display)

    def enter_four(self):
        if self.screen_display == "0":
            self.screen_display = "4"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "4"
        self.screen.configure(text=self.screen_display)

    def enter_five(self):
        if self.screen_display == "0":
            self.screen_display = "5"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "5"
        self.screen.configure(text=self.screen_display)

    def enter_six(self):
        if self.screen_display == "0":
            self.screen_display = "6"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "6"
        self.screen.configure(text=self.screen_display)

    def enter_seven(self):
        if self.screen_display == "0":
            self.screen_display = "7"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "7"
        self.screen.configure(text=self.screen_display)

    def enter_eight(self):
        if self.screen_display == "0":
            self.screen_display = "8"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "8"
        self.screen.configure(text=self.screen_display)

    def enter_nine(self):
        if self.screen_display == "0":
            self.screen_display = "9"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "9"
        self.screen.configure(text=self.screen_display)

    def clear(self):
        self.screen_display = "0"
        self.screen.configure(text=self.screen_display)
        self.brackets_open = 0

    def enter_zero(self):
        if self.screen_display != "0" and len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "0"
            self.screen.configure(text=self.screen_display)

    def delete(self):
        last_char_entered = self.screen_display[-1]
        if self.screen_display != "0":
            if last_char_entered == "(":
                self.brackets_open -= 1
            if len(self.screen_display) > 1:
                self.screen_display = self.screen_display[:-1]
            else:
                self.screen_display = "0"
            self.screen.configure(text=self.screen_display)

    def enter_plus(self):
        if self.screen_display[-1] in "+-x÷":
            self.screen_display = self.screen_display[:-1] + "+"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "+"
        self.screen.configure(text=self.screen_display)

    def enter_minus(self):
        if self.screen_display[-1] in "+-x÷":
            self.screen_display = self.screen_display[:-1] + "-"
        elif self.screen_display == "0":
            self.screen_display = "-"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "-"
        self.screen.configure(text=self.screen_display)

    def enter_times(self):
        if self.screen_display[-1] in "+-x÷":
            self.screen_display = self.screen_display[:-1] + "x"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "x"
        self.screen.configure(text=self.screen_display)

    def enter_divide(self):
        if self.screen_display[-1] in "+-x÷":
            self.screen_display = self.screen_display[:-1] + "÷"
        elif len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "÷"
        self.screen.configure(text=self.screen_display)

    def enter_open_bracket(self):
        if self.screen_display == "0":
            self.screen_display = "("
            self.brackets_open += 1

        elif self.screen_display[-1] in "(+-x÷" and len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "("
            self.brackets_open += 1

        self.screen.configure(text=self.screen_display)

    def enter_close_bracket(self):
        if self.brackets_open > 0 and self.screen_display[-1] not in "(+-x÷" and len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += ")"
            self.brackets_open -= 1
            self.screen.configure(text=self.screen_display)

    def enter_point(self):
        if self.screen_display[-1].isnumeric() and len(self.screen_display) < MAX_SCREEN_CHARS:
            self.screen_display += "."
            self.screen.configure(text=self.screen_display)

    def calculate(self):
        expression = self.screen_display.replace("x", "*").replace("÷", "/")
        try:
            result = evaluate.evaluate(expression)
            result = str(result)[:MAX_SCREEN_CHARS]
            self.screen_display = result

        except decimal.DivisionByZero:
            result = "INFINITY"
            self.screen_display = "0"

        except (IndexError, decimal.InvalidOperation):
            result = "ERROR"
            self.screen_display = "0"

        self.screen.configure(text=result)


