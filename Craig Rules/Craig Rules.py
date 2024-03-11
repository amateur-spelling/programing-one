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
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSlateGray
		self._label1.ForeColor = System.Drawing.Color.CornflowerBlue
		self._label1.Location = System.Drawing.Point(256, 81)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(346, 47)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.Highlight
		self._button1.ForeColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(256, 167)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Cheer"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.Highlight
		self._button2.ForeColor = System.Drawing.Color.Coral
		self._button2.Location = System.Drawing.Point(527, 167)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkCyan
		self.ClientSize = System.Drawing.Size(928, 439)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Craig Rules"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = " Go Cougars! "

	def Button2Click(self, sender, e):
		Application.Exit()