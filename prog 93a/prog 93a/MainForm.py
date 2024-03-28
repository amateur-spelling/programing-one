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
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkKhaki
		self._button1.Location = System.Drawing.Point(414, 104)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 28)
		self._button1.TabIndex = 0
		self._button1.Text = "Calcaute "
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkKhaki
		self._button2.Location = System.Drawing.Point(385, 52)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(96, 46)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkKhaki
		self._button3.Location = System.Drawing.Point(502, 52)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(87, 46)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label1.Location = System.Drawing.Point(23, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Base Rate"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label2.Location = System.Drawing.Point(23, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Surcharge"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label3.Location = System.Drawing.Point(23, 115)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Citytax"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(442, 26)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label4.Location = System.Drawing.Point(159, 29)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label5.Location = System.Drawing.Point(159, 75)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label6.Location = System.Drawing.Point(159, 114)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 9
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._label7.Location = System.Drawing.Point(23, 151)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(254, 10)
		self._label7.TabIndex = 10
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label8.Location = System.Drawing.Point(23, 181)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "Total"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label9.Location = System.Drawing.Point(23, 228)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 12
		self._label9.Text = "Total + Late fees"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label10.Location = System.Drawing.Point(159, 181)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 13
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label11.Location = System.Drawing.Point(159, 228)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 14
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.BurlyWood
		self.ClientSize = System.Drawing.Size(640, 347)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog 93a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		cost = round(float(self._textBox1.Text) * .0475,2)
		taxSu = round(cost * 0.10,2)
		taxC = round(cost * 0.03,2)
		
		self._label4.Text = str(cost)
		self._label5.Text = str(taxSu)
		self._label6.Text = str(taxC)
		
		total = cost + taxSu + taxC
		Lfee = round(total * 0.04,2)
		totalL = total + Lfee
		
		self._label10.Text = str(total)
		self._label11.Text = str(totalL)

	def TextBox1TextChanged(self, sender, e):
		pass