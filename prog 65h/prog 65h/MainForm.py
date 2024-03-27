import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Cyan
		self._button1.Location = System.Drawing.Point(147, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 76)
		self._button1.TabIndex = 0
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cyan
		self._button2.Location = System.Drawing.Point(270, 14)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(111, 76)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Cyan
		self._button3.Location = System.Drawing.Point(147, 94)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(234, 78)
		self._button3.TabIndex = 2
		self._button3.Text = "Cauclate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkBlue
		self._label1.ForeColor = System.Drawing.Color.Coral
		self._label1.Location = System.Drawing.Point(12, 14)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 59)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 94)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		self._textBox1.Text = "Pound"
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(12, 120)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		self._textBox2.Text = "Shillings "
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(12, 146)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		self._textBox3.Text = "Pence "
		self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CornflowerBlue
		self.ClientSize = System.Drawing.Size(393, 177)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog 65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		pound = self._textBox1.Text
		shillings = (float(self._textBox2.Text)
		* 5 / 100)
		pence = (float(self._textBox3.Text)
		/ 2.4 / 100)
		mod = float(pound + shillings + pence)
		
		self._label1.Text = str(mod)
		
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = "Pound"
		self._textBox2.Text = "Shillings"
		self._textBox3.Text = "Pence"
		self._label1.Text = ""

	def Button1Click(self, sender, e):
		Application.Exit()