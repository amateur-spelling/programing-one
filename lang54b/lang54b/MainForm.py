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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkTurquoise
		self._button1.Location = System.Drawing.Point(293, 126)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkTurquoise
		self._button2.Location = System.Drawing.Point(381, 125)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 53)
		self._button2.TabIndex = 1
		self._button2.Text = "Calutate"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkTurquoise
		self._button3.Location = System.Drawing.Point(503, 125)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkCyan
		self._label1.Location = System.Drawing.Point(79, 207)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkCyan
		self._label2.Location = System.Drawing.Point(79, 256)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "label2"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkCyan
		self._textBox1.Location = System.Drawing.Point(79, 74)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkCyan
		self._textBox2.Location = System.Drawing.Point(79, 101)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkCyan
		self._textBox3.Location = System.Drawing.Point(79, 128)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 8
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.DarkCyan
		self._textBox4.Location = System.Drawing.Point(79, 155)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSeaGreen
		self.ClientSize = System.Drawing.Size(918, 442)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		Var1 = int(self._textBox1.Text)
		Var2 = int(self._textBox2.Text)
		Var3 = int(self._textBox3.Text)
		Var4 = int(self._textBox4.Text)
		Sum = Var1 + Var2 + Var3 + Var4
		Average = float(Sum / 4.0)
		
		self._label1.Text = str(Sum)
		self._label2.Text = str(Average)

	def Button1Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = "" 
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		

	def Button3Click(self, sender, e):
		Application.Exit()