""" A calculator that can deal with different bases and ASCII.
    Now supports fractions/decimal places.
    All python3 operators that use symbols that are not alphanumeric should
    work. This includes everything from common mathematic to bitwise operators.
    Author: Marc Katzef
    Date: 20/4/2016
"""

from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Button

BACKGROUND_COLOUR = '#e7e7e7' # Suitable for MacOS, looks a bit off on Windows.
ALPHANUMCHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
LETTER_TO_NUMBER = {}
NUMBER_TO_LETTER = {}


for i in range(len(ALPHANUMCHARS)):
    NUMBER_TO_LETTER[i] = ALPHANUMCHARS[i]
    LETTER_TO_NUMBER[ALPHANUMCHARS[i]] = i
    
    
class Maingui:
    """Builds the gui in a given window or frame"""
    def __init__(self, window):
        """Places all of the GUI elements in the given window/frame, and
        initializes the variables that are needed for this GUI to do anything"""
        self.base1 = StringVar()
        self.base2 = StringVar()
        self.tick_var1 = IntVar()
        self.tick_var2 = IntVar()
        options = ['ASCII'] + ['Base ' + str(base) for base in range(2, len(ALPHANUMCHARS) + 1)]
        self.base1.set('ASCII')
        self.base2.set('Base 2')
        self.tick_var1.set(0)
        self.tick_var2.set(1)
        
        h1 = 0.51
        w1 = 0.49
        w1a = w1 / 2
        w1b = 4/5 * (w1 - w1a)
        
        top_height = 25
        padding = 5
        
        check_h = 23
        check_w = 20
        
        # The frame for the row of options at the top of the window
        top_row = Frame(window, bg=BACKGROUND_COLOUR)
        top_row.place(y=padding, relwidth=1, height=top_height)
        
        # The base selection box on the left
        base1_selection = Combobox(top_row, textvariable=self.base1, values=options, state='readonly')
        base1_selection.place(x=padding, relx=0, y=OFFSET1, relwidth=w1a, height=check_h)
        self.base1.trace('w', lambda *args: self.update(2))

        # The update button on the left
        self.update_button1 = Button(top_row, text='Update', command=lambda x=2: self.update(x, True))
        self.update_button1.place(x=padding, relx=w1a, y=0, relwidth=w1b, height=check_h+OFFSET2)
        
        # The auto-update tick box on the left
        self.update_tickbox1 = Checkbutton(top_row, variable=self.tick_var1)
        self.update_tickbox1.place(x=padding-check_w/2, relx=(w1+(w1a+w1b))/2, width=check_w, y=OFFSET2, height=check_h)
        
        # The base selection box on the right
        base2_selection = Combobox(top_row, textvariable=self.base2, values=options, state='readonly')
        base2_selection.place(x=-padding/2, relx=h1, y=OFFSET1, relwidth=w1a, height=check_h)
        self.base2.trace('w', lambda *args: self.update(1))   
        
        # The update button on the right
        self.update_button2 = Button(top_row, text='Auto', command=lambda x=1: self.update(x, True))
        self.update_button2.place(relx=h1+w1a, y=0, x=-padding/2, relwidth=w1b, height=check_h+OFFSET2)
        
        # The auto-update tick box on the right
        self.update_tickbox2 = Checkbutton(top_row, variable=self.tick_var2)
        self.update_tickbox2.place(x=-(check_w+padding)/2, relx=h1+(w1+(w1a+w1b))/2, width=check_w, y=OFFSET2, relheight=1)
        
        # The row that holds the text windows which hold the numbers
        business_row = Frame(window)
        business_row.config(background=BACKGROUND_COLOUR)
        business_row.place(x=padding, y=top_height+2*padding, relwidth=1, relheight=1, width=-padding, height=-(top_height+3*padding))
        
        # Text box on the left
        self.string1_entry = Text(business_row)
        self.string1_entry.place(relx=0, y=0, relwidth=w1, relheight=1)   
        self.string1_entry.config(highlightbackground='#d1d1d1') # Needed on OSX / MacOS
        self.string1_entry.bind('<KeyRelease>', lambda event: self.update(1))
        
        # Text box on the right
        self.string2_entry = Text(business_row)
        self.string2_entry.place(relx=h1, y=0, relwidth=w1, relheight=1, x=-padding)
        self.string2_entry.config(highlightbackground='#d1d1d1') # Needed on OSX / MacOS
        self.string2_entry.bind('<KeyRelease>', lambda event: self.update(2))
        
        self.tick_var1.trace('w', lambda *args: self.toggle_button(1)) 
        self.tick_var2.trace('w', lambda *args: self.toggle_button(2))        
            
            
    def toggle_button(self, which_one):
        if which_one == 1:
            status = self.tick_var1.get()
            if status:
                self.update_button1['text'] = 'Auto' 
            else:
                self.update_button1['text'] = 'Update'           
        else:            
            status = self.tick_var2.get()            
            if status:
                self.update_button2['text'] = 'Auto' 
            else:
                self.update_button2['text'] = 'Update' 


    def update(self, which_one, from_button=False):
        """Collects the appropriate information from the user input, then 
        retrieves the appropriate output, and places it in the appropriate text 
        field, appropriately"""
        if which_one == 1 and (self.tick_var2.get() or from_button) == 1:      # Uses info from string 1, to update string 2 
            current_base = self.base1.get()
            wanted_base = self.base2.get()
            input_string = self.string1_entry.get('1.0', 'end-1c')
            output_string = whatever_to_whatever(input_string, current_base, wanted_base)
            self.string2_entry.delete('1.0', END)
            self.string2_entry.insert(END, output_string)

        elif which_one == 2 and (self.tick_var1.get() == 1 or from_button):
            current_base = self.base2.get()
            wanted_base = self.base1.get()
            input_string = self.string2_entry.get('1.0', 'end-1c')

            output_string = whatever_to_whatever(input_string, current_base, wanted_base)
            self.string1_entry.delete('1.0', END)
            self.string1_entry.insert(END, output_string)


def dec_to_whatever(input_string, base):
    """Converts a base 10 input number (as a string) into any user-selected
    base. Returns the number in a new base (as a string)"""
    if input_string.startswith('-'):
        input_string = input_string[1:]
        sign = '-'
    else:
        sign = ''
    
    if '.' in input_string:
        input_float = float(input_string) # Translates possible scientific notation, loses accuracy for big ints
        value = int(input_float)
        frac_value = input_float % 1
    else:
        value = int(input_string)
        frac_value = 0.0
    
    result = ''
    while value > 0:
        result = NUMBER_TO_LETTER[value % base] + result
        value //= base
        
    if len(result) == 0:
        result = '0'
        
    if '.' in input_string:
        result += '.'
        
        counter = 0
        while frac_value > 0 and counter < 15:
            frac_value *= base
            column_value = int(frac_value)
            result += NUMBER_TO_LETTER[column_value]
            frac_value -= column_value
            counter += 1
    
        counter = len(result) - 1    
        while result[counter] == '0':
            counter -= 1
        result = result[:counter + 1]
        
    return sign + result
    
    
def whatever_to_dec(input_string, base):
    """Converts a given number (as a string) of any user-specified base into a
    number of base 10. Returns the number in base 10 as a string"""
    if input_string.startswith('-'):
        input_string = input_string[1:]
        sign = '-'
    else:
        sign = ''
        
    if '.' in input_string:
        counter = input_string.find('.') - 1
    else:
        counter = len(input_string) - 1

    result = 0
    for digit in input_string:
        if digit == '.':
            continue
        else:
            dec_digit = LETTER_TO_NUMBER[digit]
            result += dec_digit * base ** counter
            counter -= 1
    
    return sign + str(result)


def convert_to_ascii(input_number):
    """Converts an input number (base 10) to binary, breaks the resulting binary
    string into bytes, then converts each byte to a base 10 number to get the
    utf-8 character. Returns the string made up of the utf-8 characters"""
    input_number = str(input_number)
    if '.' in input_number:
        input_number = input_number[:input_number.find('.')]
    
    byte_string = dec_to_whatever(input_number, 2)
    byte_string = (8 - len(byte_string) % 8) * '0' + byte_string
    
    resulting_string = ''
    for byte_index in range(int(len(byte_string) / 8)):
        byte = byte_string[byte_index * 8: byte_index * 8 + 8]
        byte_dec_value = whatever_to_dec(byte, 2)
        resulting_string += chr(int(byte_dec_value))
    
    return resulting_string


def convert_to_number(input_string):
    """Converts each letter to the base 10 equivalent then that number to bytes
    (base 2). These bytes are then strung together and the resulting number
    is converted to base 10. Returns the base 10 number as a string"""
    input_string = str(input_string)
    
    byte_string = ''
    for character in input_string:
        dec_value = ord(character)
        byte = dec_to_whatever(str(dec_value), 2)
        if len(byte) % 8 != 0:
            byte = (8 - len(byte) % 8) * '0' + byte
        byte_string += byte
    
    resulting_number = whatever_to_dec(byte_string, 2)
    return resulting_number


def whatever_to_whatever(input_string, current_base, wanted_base):
    """Converts a number of base whatever to any base, using the functions 
    whatever_to_dec then dec_to_whatever. Returns the converted number as a 
    string"""
    if input_string == '':
        output_string = ''
        
    else:    
        is_valid, comment = input_parser(input_string, current_base)
        if is_valid and len(comment) != 0:
            input_string = comment
			
        if is_valid:
            if current_base == 'ASCII':
                input_number = convert_to_number(input_string)
            else:
                base_number = int(current_base[5:])
                input_number = whatever_to_dec(input_string, base_number)

            if wanted_base == 'ASCII':
                output_string = convert_to_ascii(input_number)
            elif wanted_base == 'Base 2' and current_base == 'ASCII':
                output_string = dec_to_whatever(input_number, 2)
                if len(output_string) % 8 != 0:
                    output_string = (8 - len(output_string) % 8) * '0' + output_string
            else:
                base_number = int(wanted_base[5:])
                output_string = dec_to_whatever(input_number, base_number)
        
        else:
            output_string = comment
            
    return output_string
    
    
def input_parser(input_string, current_base):
    """Verifies that the input string is a valid number in the current base.
    Returns a tuple made up of (True/False, Error Messages or evaluated
    expression)"""
    is_valid = True
    comment = '\n'
    
    if current_base == 'ASCII':
        return (is_valid, comment[2:])
    
    current_base = int(current_base[5:])
    allowable_characters = ALPHANUMCHARS[:current_base] + '.'
    
    for digit in input_string:
        if digit not in allowable_characters:
            is_valid = False
            comment += '\nError: Invalid Character: \'{}\' '.format(digit)
            
            if digit in LETTER_TO_NUMBER:
                comment += '(Wrong Base)'
            else:
                comment += '(Unrecognised)'
            
    eval_string = ''
    number_string = ''
    if 'Wrong' not in comment:
        for digit in input_string:    
            if digit not in allowable_characters:
                if len(number_string) > 0:
                    number_string = whatever_to_dec(number_string, current_base)
                    eval_string += number_string
                    number_string = ''
                eval_string += digit
    
            else:
                number_string += digit            
    
        if len(number_string) > 0:
            number_string = whatever_to_dec(number_string, current_base)
            eval_string += number_string
        
        try:
            actual_number = eval(eval_string)
            comment = '  ' + dec_to_whatever(str(actual_number), current_base)
            is_valid = True
        except SyntaxError:
            comment += '\nError: Invalid Expression'
            is_valid = False
        
    return (is_valid, comment[2:])
    
    
def main():
    """Sets everything in motion"""
    window = Tk()
    window.title('Inter-base Calculator')
    window.minsize(400, 200)
    window.config(background=BACKGROUND_COLOUR)
    Maingui(window)
    window.mainloop()


if __name__ == '__main__':
    import sys
    cur_platform = sys.platform
    
    # The combobox and checkbutton aren't level with the button without this horrible hack
    if cur_platform == 'darwin': # Mac
        OFFSET1 = 1
        OFFSET2 = 0
    elif cur_platform == 'win32': # Windows
        OFFSET1 = 1
        OFFSET2 = 2
    else:
        OFFSET1 = 0
        OFFSET2 = 0
        
    main()
