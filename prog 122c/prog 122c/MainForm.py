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
		self._listBox2 = System.Windows.Forms.ListBox()
		self._listBox3 = System.Windows.Forms.ListBox()
		self._listBox4 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(619, 22)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(168, 140)
		self._button1.TabIndex = 0
		self._button1.Text = "Calulate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 46)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 199)
		self._listBox1.TabIndex = 1
		# 
		# listBox2
		# 
		self._listBox2.FormattingEnabled = True
		self._listBox2.Location = System.Drawing.Point(163, 46)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(120, 199)
		self._listBox2.TabIndex = 2
		# 
		# listBox3
		# 
		self._listBox3.FormattingEnabled = True
		self._listBox3.Location = System.Drawing.Point(324, 46)
		self._listBox3.Name = "listBox3"
		self._listBox3.Size = System.Drawing.Size(120, 199)
		self._listBox3.TabIndex = 3
		# 
		# listBox4
		# 
		self._listBox4.FormattingEnabled = True
		self._listBox4.Location = System.Drawing.Point(471, 46)
		self._listBox4.Name = "listBox4"
		self._listBox4.Size = System.Drawing.Size(120, 199)
		self._listBox4.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(799, 252)
		self.Controls.Add(self._listBox4)
		self.Controls.Add(self._listBox3)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog 122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(2,12,2):
			line = num
			self._listBox1.Items.Add(line)
		for num2 in range(3,13,2):
			line2 = num2
			self._listBox2.Items.Add(line2)
		for num3 in range(4,24,4):
			line3 = num3
			self._listBox3.Items.Add(line3)
		exnum = 0 
		for num4 in range(4,44,8):
			exnum += num4
			line4 = exnum
			self._listBox4.Items.Add(line4)