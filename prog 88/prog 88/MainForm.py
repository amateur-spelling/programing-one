import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkRed
		self._label1.ForeColor = System.Drawing.Color.Coral
		self._label1.Location = System.Drawing.Point(25, 18)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(60, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Pick a car"
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(91, 15)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkRed
		self._label2.ForeColor = System.Drawing.Color.Coral
		self._label2.Location = System.Drawing.Point(25, 59)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Miles"
		self._label2.Click += self.Label2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkRed
		self._label4.ForeColor = System.Drawing.Color.Coral
		self._label4.Location = System.Drawing.Point(25, 146)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "MPG"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkRed
		self._label3.ForeColor = System.Drawing.Color.Coral
		self._label3.Location = System.Drawing.Point(25, 101)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Gallons"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Crimson
		self._label5.Location = System.Drawing.Point(149, 59)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(74, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Crimson
		self._label6.Location = System.Drawing.Point(149, 101)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(74, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "label6"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Crimson
		self._label7.Location = System.Drawing.Point(149, 146)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(74, 23)
		self._label7.TabIndex = 8
		self._label7.Text = "label7"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(25, 192)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 52)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(131, 192)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(47, 23)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(131, 221)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(47, 23)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(246, 272)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog 88"
		self.ResumeLayout(False)



	def Button1Click(self, sender, e):
		miles = 0 
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286.
			gallons = 9.
		elif car == "1979 Firebird":
			miles = 412.
			gallons = 40.
		elif car == "1980 Subaru":
			miles = 361.
			gallons = 18.
		elif car == "1975 Cutlass":
			miles = 161.
			gallons = 11.
			
		
		mpg = miles / gallons
		mpg = round(mpg, 1)
		
		self._label5.Text = str(miles)
		self._label6.Text = str(gallons)
		self._label7.Text = str(mpg)
		

	def Button3Click(self, sender, e):
		Applications.Exit()