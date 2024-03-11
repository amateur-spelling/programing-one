import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkKhaki
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label1.Cursor = System.Windows.Forms.Cursors.No
		self._label1.Location = System.Drawing.Point(144, 25)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(594, 107)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button1.Cursor = System.Windows.Forms.Cursors.AppStarting
		self._button1.ForeColor = System.Drawing.Color.Coral
		self._button1.Location = System.Drawing.Point(796, 176)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button2.ForeColor = System.Drawing.Color.Coral
		self._button2.Location = System.Drawing.Point(105, 176)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Restaurant1"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button3.ForeColor = System.Drawing.Color.Coral
		self._button3.Location = System.Drawing.Point(292, 176)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Restaurant2"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button4.ForeColor = System.Drawing.Color.Coral
		self._button4.Location = System.Drawing.Point(485, 176)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 23)
		self._button4.TabIndex = 4
		self._button4.Text = "Restaurant3"
		self._button4.UseVisualStyleBackColor = False
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button5.ForeColor = System.Drawing.Color.Coral
		self._button5.Location = System.Drawing.Point(105, 240)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 23)
		self._button5.TabIndex = 5
		self._button5.Text = "button5"
		self._button5.UseVisualStyleBackColor = False
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button6.ForeColor = System.Drawing.Color.Coral
		self._button6.Location = System.Drawing.Point(292, 240)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 23)
		self._button6.TabIndex = 6
		self._button6.Text = "button6"
		self._button6.UseVisualStyleBackColor = False
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button7.ForeColor = System.Drawing.Color.Coral
		self._button7.Location = System.Drawing.Point(485, 240)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(75, 23)
		self._button7.TabIndex = 7
		self._button7.Text = "button7"
		self._button7.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGoldenrod
		self.ClientSize = System.Drawing.Size(918, 439)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Phone number"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass