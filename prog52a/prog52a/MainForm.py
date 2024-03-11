import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 123)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "width:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightGreen
		self._label2.Location = System.Drawing.Point(13, 22)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "length:"
		self._label2.Click += self.Label2Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox1.Location = System.Drawing.Point(189, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox2.Location = System.Drawing.Point(189, 123)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SpringGreen
		self._label3.ForeColor = System.Drawing.SystemColors.ControlText
		self._label3.Location = System.Drawing.Point(13, 216)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "area:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label4.Location = System.Drawing.Point(189, 216)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SpringGreen
		self._label5.Location = System.Drawing.Point(13, 275)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "Perimeter:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label6.Location = System.Drawing.Point(189, 275)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		self._label6.Click += self.Label6Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSeaGreen
		self._button1.Location = System.Drawing.Point(12, 313)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 35)
		self._button1.TabIndex = 8
		self._button1.Text = "exit"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSeaGreen
		self._button2.Location = System.Drawing.Point(167, 312)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(170, 36)
		self._button2.TabIndex = 9
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightSeaGreen
		self._button3.Location = System.Drawing.Point(12, 354)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(325, 42)
		self._button3.TabIndex = 10
		self._button3.Text = "calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkCyan
		self.ClientSize = System.Drawing.Size(345, 408)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		length = int(self._textBox1.Text)
		width  = int(self._textBox2.Text)
		area   = length * width 
		perimeter = 2 * length + 2 * width
		self._label4.Text = str(area)
		self._label6.Text = str(perimeter)
		# + - * / % ** pow  // divide & round down
		
	def Label4Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		self._label6.Text = ""

	def Button1Click(self, sender, e):
		Application.Exit()