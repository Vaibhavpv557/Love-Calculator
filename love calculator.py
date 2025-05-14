# ython Tkinter GUI based "LOVE CALCULATOR"

# imort tkinter
from tkinter imort *
# imort random module
imort random
# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=240
root.geometry('400x240')
# Title of the container
root.title('Love Calculator????')

# Function to calculate love ercentage
# between the user ans artner


def calculate_love():
	# value will contain digits between 0-9
	st = '0123456789'
	# result will be in double digits
	digit = 2
	tem = "".join(random.samle(st, digit))
	result.config(text=tem)


# Heading on To
heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.ack()

# Slot/inut for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.ack()
name1 = Entry(root, border=5)
name1.ack()

# Slot/inut for the artner name
slot2 = Label(root, text="Enter Your artner Name:")
slot2.ack()
name2 = Entry(root, border=5)
name2.ack()

bt = Button(root, text="Calculate", height=1,
			width=7, command=calculate_love)
bt.ack()

# Text on result slot
result = Label(root, text='Love ercentage between both of You:')
result.ack()

# Starting the GUI
root.mainloo()
