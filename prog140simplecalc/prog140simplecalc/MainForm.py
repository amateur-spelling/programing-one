import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.addd = False
		self.subb = False
		self.muitt = False
		self.exx = False
		self.divv = False
		self.divD = False
		self.var1 = str(0)
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._results = System.Windows.Forms.Label()
		self._Calculate = System.Windows.Forms.Button()
		self._timerlab = System.Windows.Forms.Timer(self._components)
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(399, 54)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(42, 36)
		self._button1.TabIndex = 0
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Location = System.Drawing.Point(47, 56)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Number 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(198, 56)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Location = System.Drawing.Point(47, 142)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Operation:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(447, 98)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(42, 36)
		self._button2.TabIndex = 5
		self._button2.Text = "/"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(399, 98)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(42, 36)
		self._button3.TabIndex = 6
		self._button3.Text = "^"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(495, 54)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(42, 36)
		self._button4.TabIndex = 7
		self._button4.Text = "*"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(447, 54)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(42, 36)
		self._button5.TabIndex = 8
		self._button5.Text = "-"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(495, 98)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(42, 36)
		self._button6.TabIndex = 9
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Location = System.Drawing.Point(47, 236)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 11
		self._label3.Text = "Number 2:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(198, 238)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 13
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(408, 193)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(129, 39)
		self._button7.TabIndex = 14
		self._button7.Text = "Clear"
		self._button7.UseVisualStyleBackColor = True
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(408, 238)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(129, 39)
		self._button8.TabIndex = 15
		self._button8.Text = "Exit"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Location = System.Drawing.Point(47, 321)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 17
		self._label5.Text = "Result"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# results
		# 
		self._results.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._results.Location = System.Drawing.Point(198, 321)
		self._results.Name = "results"
		self._results.Size = System.Drawing.Size(100, 23)
		self._results.TabIndex = 18
		self._results.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# Calculate
		# 
		self._Calculate.Location = System.Drawing.Point(435, 141)
		self._Calculate.Name = "Calculate"
		self._Calculate.Size = System.Drawing.Size(75, 33)
		self._Calculate.TabIndex = 19
		self._Calculate.Text = "MOD"
		self._Calculate.UseVisualStyleBackColor = True
		self._Calculate.Click += self.Button9Click
		# 
		# timerlab
		# 
		self._timerlab.Enabled = True
		self._timerlab.Interval = 20
		self._timerlab.Tick += self.TimerlabTick
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label4.Location = System.Drawing.Point(225, 130)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(42, 35)
		self._label4.TabIndex = 20
		self._label4.Text = "label4"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(655, 483)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._Calculate)
		self.Controls.Add(self._results)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog140simpleCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	

	def Button8Click(self, sender, e):
		pass

	def Button9Click(self, sender, e):
		num = self.textBox1.Text
		
		
	
	def Button1Click(self, sender, e):
		addd = True
		subb = False
		muitt = False
		exx = False
		divv = False
		divD = False

	def Button5Click(self, sender, e):
		addd = False
		subb = True
		muitt = False
		exx = False
		divv = False
		divD = False

	def Button4Click(self, sender, e):
		addd = False
		subb = False
		muitt = True
		exx = False
		divv = False
		divD = False

	def Button3Click(self, sender, e):
		addd = False
		subb = False
		muitt = True
		exx = False
		divv = False
		divD = False

	def Button2Click(self, sender, e):
		addd = False
		subb = False
		muitt = False
		exx = False
		divv = True
		divD = False

	def Button6Click(self, sender, e):
		addd = False
		subb = False
		muitt = False
		exx = False
		divv = False
		divD = True

	def TimerlabTick(self, sender, e):
		if addd == True:
			var1 = "+"
		elif subb == True:
			var1 = "-"
		elif muitt == True:
			var1 = "*"
		elif exx == True:
			var1 = "**"
		elif divv == True:
			var1 = "/"
		elif divD == True:
			var1 = "//"