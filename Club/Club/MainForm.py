import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.Desktop
		self._button1.ForeColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(268, 264)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkRed
		self._label1.ForeColor = System.Drawing.Color.Cyan
		self._label1.Location = System.Drawing.Point(268, 155)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(316, 50)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.Desktop
		self._button2.ForeColor = System.Drawing.Color.Coral
		self._button2.Location = System.Drawing.Point(508, 264)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Crimson
		self.ClientSize = System.Drawing.Size(925, 444)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Club"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		self._label1.Text = "World Building Club"