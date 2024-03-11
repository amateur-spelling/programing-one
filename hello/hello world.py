import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkCyan
		self._label1.Location = System.Drawing.Point(253, 176)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(172, 68)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.ForeColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(131, 298)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.ForeColor = System.Drawing.Color.Coral
		self._button2.Location = System.Drawing.Point(301, 298)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.ForeColor = System.Drawing.Color.Coral
		self._button3.Location = System.Drawing.Point(450, 298)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Cornsilk
		self.ClientSize = System.Drawing.Size(950, 450)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._label1.Text = " Hello, world! "

	def Button2Click(self, sender, e):
		self._label1.Text = ""