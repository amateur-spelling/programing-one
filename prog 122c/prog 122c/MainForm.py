import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(669, 148)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(156, 103)
		self._button1.TabIndex = 0
		self._button1.Text = "calulate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.YellowGreen
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 18
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(609, 364)
		self._listBox1.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGreen
		self.ClientSize = System.Drawing.Size(931, 427)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog 122c"
		self.ResumeLayout(False)


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
		
		exnum = 0
		for num4 in range (
		