import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		# 
		# MainForm
		# 
		self.Name = "MainForm"
		self.Text = "prog 122c"

<<<<<<< HEAD
=======

	def Button1Click(self, sender, e):
		for num1 in range (2,12,2):
			line1 = " " + str(num1)
			self._listBox1.Items.Add(line1)
		
		for num2 in range (3,13,2):
			line2 = "\t" + str(num2)
			self._listBox1.Items.Add(line2)
			
		for num3 in range (4,24,4):
			line3 = "\t\t" + str(num3)
			self._listBox1.Items.Add(line3)
		
		for num4 in range (12,,8)
		
>>>>>>> 0b8ba250d9aaabcd7017c40f9c12b2159ee639f7
