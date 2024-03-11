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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(296, 205)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(472, 176)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 52)
		self._button2.TabIndex = 1
		self._button2.Text = "Caluclate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(663, 205)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label1.Location = System.Drawing.Point(36, 48)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Sum"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label2.Location = System.Drawing.Point(36, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Difference"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label3.Location = System.Drawing.Point(36, 123)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Product"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(372, 135)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(560, 135)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label4.Location = System.Drawing.Point(36, 162)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Average"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label5.Location = System.Drawing.Point(36, 196)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Distance"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label6.Location = System.Drawing.Point(36, 260)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "Max"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.BlanchedAlmond
		self._label7.Location = System.Drawing.Point(36, 296)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "Min"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGoldenrod
		self.ClientSize = System.Drawing.Size(927, 440)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog88"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		Pro = num1 * num2
		Average = (num1 * num2) / 2
		Distance = abs(Diff)
		Max = num1 >= num2 
		Min = num1 <  num2
		
		self._label1.Text = str(Sum)
		self._label2.Text = str(Diff)
		self._label3.Text = str(Pro)
		self._label4.Text = str(Average)
		self._label5.Text = str(Distance)
		self._label6.Text = str(Max)
		self._label7.Text = str(Min)

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass