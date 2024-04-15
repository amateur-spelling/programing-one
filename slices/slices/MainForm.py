import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(92, 94)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "slices"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		list1 = [1, 2, 3, 4, 5,]
		list2 = list1[0:3] 
		print(list2)
		list3 = list1[3:len(list1)] # [3:]
		print(list3)
		print((list2 + list3) == list1)
		
		strHi = "Hello, world!"
		substr = strHi [:5] 
		print (substr)
		print (strHi[-1])
		print (strHi[-6:-1])
		print (strHi[::-1])
		print (strHi == strHi [::-1])
		
		
		input()