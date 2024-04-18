import System.Drawing
import System.Windows.Forms
import math

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
		self._button1.BackColor = System.Drawing.Color.DarkCyan
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(713, 143)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(156, 104)
		self._button1.TabIndex = 0
		self._button1.Text = "Caulate "
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Aquamarine
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 25
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(695, 379)
		self._listBox1.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Cyan
		self.ClientSize = System.Drawing.Size(933, 420)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog 122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number \t\t Cube Root \t\t Cube"
		self._listBox1.Items.Add(heading)
		num = 0
		num1 = 0
		for num in range(-25, 25, 1):
			if num < 0:
				num1 = (num * -1)**0.3
			else:
				num1 = num**0.3
			Cube = int(num)**3
			line =  str(num) + "\t\t    " + str(num1) + "\t\t\t" + str(Cube)
			self._listBox1.Items.Add(line)