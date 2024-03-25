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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button1.Location = System.Drawing.Point(12, 218)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 65)
		self._button1.TabIndex = 0
		self._button1.Text = "Calulate "
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGreen
		self._label1.Location = System.Drawing.Point(12, 109)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(186, 106)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(99, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 33)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(80, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Speed limit"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 71)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(80, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Vehicle speed"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button2.Location = System.Drawing.Point(119, 218)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(70, 31)
		self._button2.TabIndex = 6
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button3.Location = System.Drawing.Point(119, 248)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(70, 35)
		self._button3.TabIndex = 7
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(99, 33)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 9
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkKhaki
		self.ClientSize = System.Drawing.Size(325, 428)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog 82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox3TextChanged(self, sender, e):
		pass
	
	def TextBox1TextChanged(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		self.textbox3.Text = ""
		self.TextBox1.Text = ""
		self.label1.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		lim = int(self._textBox3.Text)
		speed = int(self._textBox1.Text)
		points = float(speed - lim) 
		cost = float(round(20.00 + (points * 5.00)))
		
		if points <= 0:
			self._label1.Text = "No ticket"
		else:
			self._label1.Text = str(cost)
