import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label9 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkGray
		self._label9.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label9.Location = System.Drawing.Point(174, 221)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(85, 23)
		self._label9.TabIndex = 27
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label9.Click += self.Label9Click
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(256, 93)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 26
		self._label8.Text = "money given"
		self._label8.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(75, 93)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 25
		self._label7.Text = "cost"
		self._label7.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkGray
		self._label6.Location = System.Drawing.Point(625, 326)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 24
		self._label6.Text = "Pennies"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkGray
		self._label5.Location = System.Drawing.Point(625, 282)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 23
		self._label5.Text = "Nickels"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGray
		self._label4.Location = System.Drawing.Point(625, 232)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 22
		self._label4.Text = "Dimes"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGray
		self._label3.Location = System.Drawing.Point(625, 186)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 21
		self._label3.Text = "Quarters"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkGray
		self._label2.Location = System.Drawing.Point(625, 137)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 20
		self._label2.Text = "Dollars"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(174, 165)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(75, 23)
		self._label1.TabIndex = 19
		self._label1.Text = "change"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(272, 282)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 18
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(174, 282)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 17
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(75, 282)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 16
		self._button1.Text = "pay"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(256, 125)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 15
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(75, 125)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 14
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGoldenrod
		self.ClientSize = System.Drawing.Size(800, 442)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "lang58t"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label9.Text = ""
		self._label2.Text = "Dollars"
		self._label3.Text = "Quarters"
		self._label4.Text = "Dimes"
		self._label5.Text = "Nickels"
		self._label6.Text = "Pennies"

	def Label2Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		cost = float(self._textBox2.Text)
		pay = float(self._textBox1.Text)
		change = cost - pay
		self._label9.Text = str(change)
		Dollars = int(change) // 1
		self._label2.Text = str(Dollars)
		Quarters = float(change - float(Dollars)) // 0.25
		self._label3.Text = str(Quarters)
		Dimes = float(change - float(Dollars) - (float(Quarters) * 0.25)) // 0.1
		self._label4.Text = str(Dimes)
		Nickels = float(change - float(Dollars) - (float(Quarters) * 0.25) - (float(Dimes) * 0.1)) // 0.05
		self._label5.Text = str(Nickels)
		Pennies = float(change - float(Dollars) - (float(Quarters) * 0.25) - (float(Dimes) * 0.1) - (float(Nickels) * 0.05)) // 0.01
		self._label6.Text = str(Pennies)
			
			# int, str, float
	def TextBox1TextChanged(self, sender, e):
		pass

	def Label9Click(self, sender, e):
		pass