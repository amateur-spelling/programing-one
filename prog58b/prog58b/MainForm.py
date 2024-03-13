import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(72, 129)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "A"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.ForeColor = System.Drawing.SystemColors.ControlText
		self._label2.Location = System.Drawing.Point(345, 129)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "B"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.ForeColor = System.Drawing.SystemColors.ControlText
		self._label3.Location = System.Drawing.Point(640, 129)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "C"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(72, 189)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(345, 189)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(640, 189)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button1.Location = System.Drawing.Point(214, 256)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button2.Location = System.Drawing.Point(519, 256)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Blue
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(359, 334)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkCyan
		self._label4.ForeColor = System.Drawing.Color.Coral
		self._label4.Location = System.Drawing.Point(308, 241)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(95, 21)
		self._label4.TabIndex = 9
		self._label4.Text = "Root"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkCyan
		self._label5.ForeColor = System.Drawing.Color.Coral
		self._label5.Location = System.Drawing.Point(398, 272)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(95, 21)
		self._label5.TabIndex = 10
		self._label5.Text = "Root"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkCyan
		self.ClientSize = System.Drawing.Size(838, 425)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._label4.Text = "Root"
		self._label5.Text = "Root"
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""

	def Button1Click(self, sender, e):
		A = int(self._textBox1.Text)
		B = int(self._textBox2.Text)
		C = int(self._textBox3.Text)
		Root1 = -B + math.sqrt(B**2 - (4 * A * C)) / (2 * A)
		Root2 = -B - math.sqrt(B**2 - (4 * A * C)) / (2 * A)
		
		self._label4.Text = str(Root1)
		self._label5.Text = str(Root2)

	def Button3Click(self, sender, e):
		Application.Exit()