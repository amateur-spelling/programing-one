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
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CadetBlue
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label1.Cursor = System.Windows.Forms.Cursors.No
		self._label1.ImageAlign = System.Drawing.ContentAlignment.BottomCenter
		self._label1.Location = System.Drawing.Point(271, 80)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(239, 103)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Aquamarine
		self._button1.ForeColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(271, 266)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Aquamarine
		self._button3.Cursor = System.Windows.Forms.Cursors.Arrow
		self._button3.ForeColor = System.Drawing.Color.Coral
		self._button3.Location = System.Drawing.Point(435, 266)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Aqua
		self.ClientSize = System.Drawing.Size(913, 446)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Cursor = System.Windows.Forms.Cursors.Arrow
		self.Name = "MainForm"
		self.Text = "Name"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "Corbin LaVelle"
		
	def Button3Click(self, sender, e):
		Application.Exit()
		