﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.Bturn = True
		self.Rturn = False
		self.bch1  = False
		self.bch2  = False
		self.bch3  = False
		self.bch4  = False
		self.bch5  = False
		self.bch6  = False
		self.bch7  = False
		self.bch8  = False
		self.bch9  = False
		self.bch10 = False
		self.bch11 = False
		self.bch12 = False 
		self.rch13 = False
		self.rch14 = False
		self.rch15 = False
		self.rch16 = False
		self.rch17 = False
		self.rch18 = False
		self.rch19 = False
		self.rch20 = False
		self.rch21 = False
		self.rch22 = False
		self.rch23 = False
		self.rch24 = False
		self.Mcr = False
		self.Mcl = False
		self.Mcb = False
		self.McU = True
		
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._label17 = System.Windows.Forms.Label()
		self._label18 = System.Windows.Forms.Label()
		self._label19 = System.Windows.Forms.Label()
		self._label20 = System.Windows.Forms.Label()
		self._label21 = System.Windows.Forms.Label()
		self._label22 = System.Windows.Forms.Label()
		self._label23 = System.Windows.Forms.Label()
		self._label24 = System.Windows.Forms.Label()
		self._label25 = System.Windows.Forms.Label()
		self._label26 = System.Windows.Forms.Label()
		self._label27 = System.Windows.Forms.Label()
		self._label28 = System.Windows.Forms.Label()
		self._label29 = System.Windows.Forms.Label()
		self._label30 = System.Windows.Forms.Label()
		self._label31 = System.Windows.Forms.Label()
		self._label32 = System.Windows.Forms.Label()
		self._label33 = System.Windows.Forms.Label()
		self._label34 = System.Windows.Forms.Label()
		self._label35 = System.Windows.Forms.Label()
		self._label36 = System.Windows.Forms.Label()
		self._label37 = System.Windows.Forms.Label()
		self._label38 = System.Windows.Forms.Label()
		self._label39 = System.Windows.Forms.Label()
		self._label40 = System.Windows.Forms.Label()
		self._label41 = System.Windows.Forms.Label()
		self._label42 = System.Windows.Forms.Label()
		self._label43 = System.Windows.Forms.Label()
		self._label44 = System.Windows.Forms.Label()
		self._label45 = System.Windows.Forms.Label()
		self._label46 = System.Windows.Forms.Label()
		self._label47 = System.Windows.Forms.Label()
		self._label48 = System.Windows.Forms.Label()
		self._label49 = System.Windows.Forms.Label()
		self._label50 = System.Windows.Forms.Label()
		self._label51 = System.Windows.Forms.Label()
		self._label52 = System.Windows.Forms.Label()
		self._label53 = System.Windows.Forms.Label()
		self._label54 = System.Windows.Forms.Label()
		self._label55 = System.Windows.Forms.Label()
		self._label56 = System.Windows.Forms.Label()
		self._label57 = System.Windows.Forms.Label()
		self._label58 = System.Windows.Forms.Label()
		self._label59 = System.Windows.Forms.Label()
		self._label60 = System.Windows.Forms.Label()
		self._label61 = System.Windows.Forms.Label()
		self._label62 = System.Windows.Forms.Label()
		self._label63 = System.Windows.Forms.Label()
		self._label64 = System.Windows.Forms.Label()
		self._Bc1 = System.Windows.Forms.Button()
		self._Bc8 = System.Windows.Forms.Button()
		self._Bc12 = System.Windows.Forms.Button()
		self._Bc7 = System.Windows.Forms.Button()
		self._Bc11 = System.Windows.Forms.Button()
		self._Bc3 = System.Windows.Forms.Button()
		self._Bc6 = System.Windows.Forms.Button()
		self._Bc5 = System.Windows.Forms.Button()
		self._Bc2 = System.Windows.Forms.Button()
		self._Bc9 = System.Windows.Forms.Button()
		self._Bc10 = System.Windows.Forms.Button()
		self._Bc4 = System.Windows.Forms.Button()
		self._Rc1 = System.Windows.Forms.Button()
		self._Rc5 = System.Windows.Forms.Button()
		self._Rc9 = System.Windows.Forms.Button()
		self._Rc6 = System.Windows.Forms.Button()
		self._Rc10 = System.Windows.Forms.Button()
		self._Rc7 = System.Windows.Forms.Button()
		self._Rc11 = System.Windows.Forms.Button()
		self._Rc12 = System.Windows.Forms.Button()
		self._Rc8 = System.Windows.Forms.Button()
		self._Rc4 = System.Windows.Forms.Button()
		self._Rc3 = System.Windows.Forms.Button()
		self._Rc2 = System.Windows.Forms.Button()
		self._BTt = System.Windows.Forms.Timer(self._components)
		self._RTt = System.Windows.Forms.Timer(self._components)
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(43, 390)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(63, 51)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(107, 390)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(63, 51)
		self._label2.TabIndex = 1
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(357, 390)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(63, 51)
		self._label3.TabIndex = 3
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(295, 390)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(63, 51)
		self._label4.TabIndex = 2
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(232, 390)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(63, 51)
		self._label5.TabIndex = 5
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(170, 390)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(63, 51)
		self._label6.TabIndex = 4
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Black
		self._label7.Location = System.Drawing.Point(481, 390)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(63, 51)
		self._label7.TabIndex = 7
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(419, 390)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(63, 51)
		self._label8.TabIndex = 6
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Black
		self._label9.Location = System.Drawing.Point(43, 339)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(63, 51)
		self._label9.TabIndex = 11
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.White
		self._label10.Location = System.Drawing.Point(107, 339)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(63, 51)
		self._label10.TabIndex = 10
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(170, 339)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(63, 51)
		self._label11.TabIndex = 13
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.White
		self._label12.Location = System.Drawing.Point(232, 339)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(63, 51)
		self._label12.TabIndex = 12
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Black
		self._label13.Location = System.Drawing.Point(295, 339)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(63, 51)
		self._label13.TabIndex = 15
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.White
		self._label14.Location = System.Drawing.Point(357, 339)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(63, 51)
		self._label14.TabIndex = 14
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.Black
		self._label15.Location = System.Drawing.Point(419, 339)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(63, 51)
		self._label15.TabIndex = 17
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.White
		self._label16.Location = System.Drawing.Point(481, 339)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(63, 51)
		self._label16.TabIndex = 16
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.Color.Black
		self._label17.Location = System.Drawing.Point(107, 288)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(63, 51)
		self._label17.TabIndex = 19
		# 
		# label18
		# 
		self._label18.BackColor = System.Drawing.Color.White
		self._label18.Location = System.Drawing.Point(43, 288)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(63, 51)
		self._label18.TabIndex = 18
		# 
		# label19
		# 
		self._label19.BackColor = System.Drawing.Color.Black
		self._label19.Location = System.Drawing.Point(232, 288)
		self._label19.Name = "label19"
		self._label19.Size = System.Drawing.Size(63, 51)
		self._label19.TabIndex = 21
		# 
		# label20
		# 
		self._label20.BackColor = System.Drawing.Color.White
		self._label20.Location = System.Drawing.Point(170, 288)
		self._label20.Name = "label20"
		self._label20.Size = System.Drawing.Size(63, 51)
		self._label20.TabIndex = 20
		# 
		# label21
		# 
		self._label21.BackColor = System.Drawing.Color.Black
		self._label21.Location = System.Drawing.Point(357, 288)
		self._label21.Name = "label21"
		self._label21.Size = System.Drawing.Size(63, 51)
		self._label21.TabIndex = 23
		# 
		# label22
		# 
		self._label22.BackColor = System.Drawing.Color.White
		self._label22.Location = System.Drawing.Point(295, 288)
		self._label22.Name = "label22"
		self._label22.Size = System.Drawing.Size(63, 51)
		self._label22.TabIndex = 22
		# 
		# label23
		# 
		self._label23.BackColor = System.Drawing.Color.Black
		self._label23.Location = System.Drawing.Point(481, 288)
		self._label23.Name = "label23"
		self._label23.Size = System.Drawing.Size(63, 51)
		self._label23.TabIndex = 25
		# 
		# label24
		# 
		self._label24.BackColor = System.Drawing.Color.White
		self._label24.Location = System.Drawing.Point(419, 288)
		self._label24.Name = "label24"
		self._label24.Size = System.Drawing.Size(63, 51)
		self._label24.TabIndex = 24
		# 
		# label25
		# 
		self._label25.BackColor = System.Drawing.Color.Black
		self._label25.Location = System.Drawing.Point(43, 237)
		self._label25.Name = "label25"
		self._label25.Size = System.Drawing.Size(63, 51)
		self._label25.TabIndex = 27
		# 
		# label26
		# 
		self._label26.BackColor = System.Drawing.Color.White
		self._label26.Location = System.Drawing.Point(107, 237)
		self._label26.Name = "label26"
		self._label26.Size = System.Drawing.Size(63, 51)
		self._label26.TabIndex = 26
		# 
		# label27
		# 
		self._label27.BackColor = System.Drawing.Color.Black
		self._label27.Location = System.Drawing.Point(170, 237)
		self._label27.Name = "label27"
		self._label27.Size = System.Drawing.Size(63, 51)
		self._label27.TabIndex = 29
		# 
		# label28
		# 
		self._label28.BackColor = System.Drawing.Color.White
		self._label28.Location = System.Drawing.Point(232, 237)
		self._label28.Name = "label28"
		self._label28.Size = System.Drawing.Size(63, 51)
		self._label28.TabIndex = 28
		# 
		# label29
		# 
		self._label29.BackColor = System.Drawing.Color.Black
		self._label29.Location = System.Drawing.Point(295, 237)
		self._label29.Name = "label29"
		self._label29.Size = System.Drawing.Size(63, 51)
		self._label29.TabIndex = 31
		# 
		# label30
		# 
		self._label30.BackColor = System.Drawing.Color.White
		self._label30.Location = System.Drawing.Point(357, 237)
		self._label30.Name = "label30"
		self._label30.Size = System.Drawing.Size(63, 51)
		self._label30.TabIndex = 30
		# 
		# label31
		# 
		self._label31.BackColor = System.Drawing.Color.Black
		self._label31.Location = System.Drawing.Point(419, 237)
		self._label31.Name = "label31"
		self._label31.Size = System.Drawing.Size(63, 51)
		self._label31.TabIndex = 33
		# 
		# label32
		# 
		self._label32.BackColor = System.Drawing.Color.White
		self._label32.Location = System.Drawing.Point(481, 237)
		self._label32.Name = "label32"
		self._label32.Size = System.Drawing.Size(63, 51)
		self._label32.TabIndex = 32
		# 
		# label33
		# 
		self._label33.BackColor = System.Drawing.Color.Black
		self._label33.Location = System.Drawing.Point(481, 186)
		self._label33.Name = "label33"
		self._label33.Size = System.Drawing.Size(63, 51)
		self._label33.TabIndex = 41
		# 
		# label34
		# 
		self._label34.BackColor = System.Drawing.Color.White
		self._label34.Location = System.Drawing.Point(419, 186)
		self._label34.Name = "label34"
		self._label34.Size = System.Drawing.Size(63, 51)
		self._label34.TabIndex = 40
		self._label34.Click += self.Label34Click
		# 
		# label35
		# 
		self._label35.BackColor = System.Drawing.Color.Black
		self._label35.Location = System.Drawing.Point(232, 186)
		self._label35.Name = "label35"
		self._label35.Size = System.Drawing.Size(63, 51)
		self._label35.TabIndex = 39
		# 
		# label36
		# 
		self._label36.BackColor = System.Drawing.Color.White
		self._label36.Location = System.Drawing.Point(170, 186)
		self._label36.Name = "label36"
		self._label36.Size = System.Drawing.Size(63, 51)
		self._label36.TabIndex = 38
		# 
		# label37
		# 
		self._label37.BackColor = System.Drawing.Color.Black
		self._label37.Location = System.Drawing.Point(357, 186)
		self._label37.Name = "label37"
		self._label37.Size = System.Drawing.Size(63, 51)
		self._label37.TabIndex = 37
		# 
		# label38
		# 
		self._label38.BackColor = System.Drawing.Color.White
		self._label38.Location = System.Drawing.Point(295, 186)
		self._label38.Name = "label38"
		self._label38.Size = System.Drawing.Size(63, 51)
		self._label38.TabIndex = 36
		# 
		# label39
		# 
		self._label39.BackColor = System.Drawing.Color.Black
		self._label39.Location = System.Drawing.Point(107, 186)
		self._label39.Name = "label39"
		self._label39.Size = System.Drawing.Size(63, 51)
		self._label39.TabIndex = 35
		# 
		# label40
		# 
		self._label40.BackColor = System.Drawing.Color.White
		self._label40.Location = System.Drawing.Point(43, 186)
		self._label40.Name = "label40"
		self._label40.Size = System.Drawing.Size(63, 51)
		self._label40.TabIndex = 34
		# 
		# label41
		# 
		self._label41.BackColor = System.Drawing.Color.Black
		self._label41.Location = System.Drawing.Point(419, 135)
		self._label41.Name = "label41"
		self._label41.Size = System.Drawing.Size(63, 51)
		self._label41.TabIndex = 49
		# 
		# label42
		# 
		self._label42.BackColor = System.Drawing.Color.White
		self._label42.Location = System.Drawing.Point(481, 135)
		self._label42.Name = "label42"
		self._label42.Size = System.Drawing.Size(63, 51)
		self._label42.TabIndex = 48
		# 
		# label43
		# 
		self._label43.BackColor = System.Drawing.Color.Black
		self._label43.Location = System.Drawing.Point(295, 135)
		self._label43.Name = "label43"
		self._label43.Size = System.Drawing.Size(63, 51)
		self._label43.TabIndex = 47
		# 
		# label44
		# 
		self._label44.BackColor = System.Drawing.Color.White
		self._label44.Location = System.Drawing.Point(357, 135)
		self._label44.Name = "label44"
		self._label44.Size = System.Drawing.Size(63, 51)
		self._label44.TabIndex = 46
		# 
		# label45
		# 
		self._label45.BackColor = System.Drawing.Color.Black
		self._label45.Location = System.Drawing.Point(170, 135)
		self._label45.Name = "label45"
		self._label45.Size = System.Drawing.Size(63, 51)
		self._label45.TabIndex = 45
		# 
		# label46
		# 
		self._label46.BackColor = System.Drawing.Color.White
		self._label46.Location = System.Drawing.Point(232, 135)
		self._label46.Name = "label46"
		self._label46.Size = System.Drawing.Size(63, 51)
		self._label46.TabIndex = 44
		# 
		# label47
		# 
		self._label47.BackColor = System.Drawing.Color.Black
		self._label47.Location = System.Drawing.Point(43, 135)
		self._label47.Name = "label47"
		self._label47.Size = System.Drawing.Size(63, 51)
		self._label47.TabIndex = 43
		# 
		# label48
		# 
		self._label48.BackColor = System.Drawing.Color.White
		self._label48.Location = System.Drawing.Point(107, 135)
		self._label48.Name = "label48"
		self._label48.Size = System.Drawing.Size(63, 51)
		self._label48.TabIndex = 42
		# 
		# label49
		# 
		self._label49.BackColor = System.Drawing.Color.Black
		self._label49.Location = System.Drawing.Point(481, 84)
		self._label49.Name = "label49"
		self._label49.Size = System.Drawing.Size(63, 51)
		self._label49.TabIndex = 57
		# 
		# label50
		# 
		self._label50.BackColor = System.Drawing.Color.White
		self._label50.Location = System.Drawing.Point(419, 84)
		self._label50.Name = "label50"
		self._label50.Size = System.Drawing.Size(63, 51)
		self._label50.TabIndex = 56
		# 
		# label51
		# 
		self._label51.BackColor = System.Drawing.Color.Black
		self._label51.Location = System.Drawing.Point(232, 84)
		self._label51.Name = "label51"
		self._label51.Size = System.Drawing.Size(63, 51)
		self._label51.TabIndex = 55
		# 
		# label52
		# 
		self._label52.BackColor = System.Drawing.Color.White
		self._label52.Location = System.Drawing.Point(170, 84)
		self._label52.Name = "label52"
		self._label52.Size = System.Drawing.Size(63, 51)
		self._label52.TabIndex = 54
		# 
		# label53
		# 
		self._label53.BackColor = System.Drawing.Color.Black
		self._label53.Location = System.Drawing.Point(357, 84)
		self._label53.Name = "label53"
		self._label53.Size = System.Drawing.Size(63, 51)
		self._label53.TabIndex = 53
		# 
		# label54
		# 
		self._label54.BackColor = System.Drawing.Color.White
		self._label54.Location = System.Drawing.Point(295, 84)
		self._label54.Name = "label54"
		self._label54.Size = System.Drawing.Size(63, 51)
		self._label54.TabIndex = 52
		# 
		# label55
		# 
		self._label55.BackColor = System.Drawing.Color.Black
		self._label55.Location = System.Drawing.Point(107, 84)
		self._label55.Name = "label55"
		self._label55.Size = System.Drawing.Size(63, 51)
		self._label55.TabIndex = 51
		# 
		# label56
		# 
		self._label56.BackColor = System.Drawing.Color.White
		self._label56.Location = System.Drawing.Point(43, 84)
		self._label56.Name = "label56"
		self._label56.Size = System.Drawing.Size(63, 51)
		self._label56.TabIndex = 50
		# 
		# label57
		# 
		self._label57.BackColor = System.Drawing.Color.Black
		self._label57.Location = System.Drawing.Point(419, 33)
		self._label57.Name = "label57"
		self._label57.Size = System.Drawing.Size(63, 51)
		self._label57.TabIndex = 65
		# 
		# label58
		# 
		self._label58.BackColor = System.Drawing.Color.White
		self._label58.Location = System.Drawing.Point(481, 33)
		self._label58.Name = "label58"
		self._label58.Size = System.Drawing.Size(63, 51)
		self._label58.TabIndex = 64
		# 
		# label59
		# 
		self._label59.BackColor = System.Drawing.Color.Black
		self._label59.Location = System.Drawing.Point(295, 33)
		self._label59.Name = "label59"
		self._label59.Size = System.Drawing.Size(63, 51)
		self._label59.TabIndex = 63
		# 
		# label60
		# 
		self._label60.BackColor = System.Drawing.Color.White
		self._label60.Location = System.Drawing.Point(357, 33)
		self._label60.Name = "label60"
		self._label60.Size = System.Drawing.Size(63, 51)
		self._label60.TabIndex = 62
		# 
		# label61
		# 
		self._label61.BackColor = System.Drawing.Color.Black
		self._label61.Location = System.Drawing.Point(170, 33)
		self._label61.Name = "label61"
		self._label61.Size = System.Drawing.Size(63, 51)
		self._label61.TabIndex = 61
		# 
		# label62
		# 
		self._label62.BackColor = System.Drawing.Color.White
		self._label62.Location = System.Drawing.Point(232, 33)
		self._label62.Name = "label62"
		self._label62.Size = System.Drawing.Size(63, 51)
		self._label62.TabIndex = 60
		# 
		# label63
		# 
		self._label63.BackColor = System.Drawing.Color.Black
		self._label63.Location = System.Drawing.Point(43, 33)
		self._label63.Name = "label63"
		self._label63.Size = System.Drawing.Size(63, 51)
		self._label63.TabIndex = 59
		# 
		# label64
		# 
		self._label64.BackColor = System.Drawing.Color.White
		self._label64.Location = System.Drawing.Point(107, 33)
		self._label64.Name = "label64"
		self._label64.Size = System.Drawing.Size(63, 51)
		self._label64.TabIndex = 58
		# 
		# Bc1
		# 
		self._Bc1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc1.Location = System.Drawing.Point(48, 291)
		self._Bc1.Name = "Bc1"
		self._Bc1.Size = System.Drawing.Size(53, 45)
		self._Bc1.TabIndex = 92
		self._Bc1.UseVisualStyleBackColor = False
		self._Bc1.Click += self.Bc1Click
		# 
		# Bc8
		# 
		self._Bc8.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc8.Location = System.Drawing.Point(488, 342)
		self._Bc8.Name = "Bc8"
		self._Bc8.Size = System.Drawing.Size(53, 45)
		self._Bc8.TabIndex = 93
		self._Bc8.UseVisualStyleBackColor = False
		self._Bc8.Click += self.Bc8Click
		# 
		# Bc12
		# 
		self._Bc12.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc12.Location = System.Drawing.Point(426, 393)
		self._Bc12.Name = "Bc12"
		self._Bc12.Size = System.Drawing.Size(53, 45)
		self._Bc12.TabIndex = 94
		self._Bc12.UseVisualStyleBackColor = False
		self._Bc12.Click += self.Bc12Click
		# 
		# Bc7
		# 
		self._Bc7.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc7.Location = System.Drawing.Point(360, 342)
		self._Bc7.Name = "Bc7"
		self._Bc7.Size = System.Drawing.Size(53, 45)
		self._Bc7.TabIndex = 95
		self._Bc7.UseVisualStyleBackColor = False
		self._Bc7.Click += self.Bc7Click
		# 
		# Bc11
		# 
		self._Bc11.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc11.Location = System.Drawing.Point(301, 393)
		self._Bc11.Name = "Bc11"
		self._Bc11.Size = System.Drawing.Size(53, 45)
		self._Bc11.TabIndex = 96
		self._Bc11.UseVisualStyleBackColor = False
		self._Bc11.Click += self.Bc11Click
		# 
		# Bc3
		# 
		self._Bc3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc3.Location = System.Drawing.Point(301, 291)
		self._Bc3.Name = "Bc3"
		self._Bc3.Size = System.Drawing.Size(53, 45)
		self._Bc3.TabIndex = 97
		self._Bc3.UseVisualStyleBackColor = False
		self._Bc3.Click += self.Button6Click
		# 
		# Bc6
		# 
		self._Bc6.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc6.Location = System.Drawing.Point(236, 342)
		self._Bc6.Name = "Bc6"
		self._Bc6.Size = System.Drawing.Size(53, 45)
		self._Bc6.TabIndex = 98
		self._Bc6.UseVisualStyleBackColor = False
		self._Bc6.Click += self.Bc6Click
		# 
		# Bc5
		# 
		self._Bc5.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc5.Location = System.Drawing.Point(112, 342)
		self._Bc5.Name = "Bc5"
		self._Bc5.Size = System.Drawing.Size(53, 45)
		self._Bc5.TabIndex = 99
		self._Bc5.UseVisualStyleBackColor = False
		self._Bc5.Click += self.Bc5Click
		# 
		# Bc2
		# 
		self._Bc2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc2.Location = System.Drawing.Point(176, 291)
		self._Bc2.Name = "Bc2"
		self._Bc2.Size = System.Drawing.Size(53, 45)
		self._Bc2.TabIndex = 100
		self._Bc2.UseVisualStyleBackColor = False
		self._Bc2.Click += self.Bc2Click
		# 
		# Bc9
		# 
		self._Bc9.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc9.Location = System.Drawing.Point(48, 393)
		self._Bc9.Name = "Bc9"
		self._Bc9.Size = System.Drawing.Size(53, 45)
		self._Bc9.TabIndex = 101
		self._Bc9.UseVisualStyleBackColor = False
		self._Bc9.Click += self.Bc9Click
		# 
		# Bc10
		# 
		self._Bc10.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc10.Location = System.Drawing.Point(176, 393)
		self._Bc10.Name = "Bc10"
		self._Bc10.Size = System.Drawing.Size(53, 45)
		self._Bc10.TabIndex = 102
		self._Bc10.UseVisualStyleBackColor = False
		self._Bc10.Click += self.Bc10Click
		# 
		# Bc4
		# 
		self._Bc4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._Bc4.Location = System.Drawing.Point(577, 39)
		self._Bc4.Name = "Bc4"
		self._Bc4.Size = System.Drawing.Size(53, 45)
		self._Bc4.TabIndex = 103
		self._Bc4.UseVisualStyleBackColor = False
		self._Bc4.Click += self.Bc4Click
		# 
		# Rc1
		# 
		self._Rc1.BackColor = System.Drawing.Color.Crimson
		self._Rc1.Location = System.Drawing.Point(111, 36)
		self._Rc1.Name = "Rc1"
		self._Rc1.Size = System.Drawing.Size(53, 45)
		self._Rc1.TabIndex = 104
		self._Rc1.UseVisualStyleBackColor = False
		self._Rc1.Click += self.Rc1Click
		# 
		# Rc5
		# 
		self._Rc5.BackColor = System.Drawing.Color.Crimson
		self._Rc5.Location = System.Drawing.Point(48, 87)
		self._Rc5.Name = "Rc5"
		self._Rc5.Size = System.Drawing.Size(53, 45)
		self._Rc5.TabIndex = 105
		self._Rc5.UseVisualStyleBackColor = False
		self._Rc5.Click += self.Rc5Click
		# 
		# Rc9
		# 
		self._Rc9.BackColor = System.Drawing.Color.Crimson
		self._Rc9.Location = System.Drawing.Point(112, 138)
		self._Rc9.Name = "Rc9"
		self._Rc9.Size = System.Drawing.Size(53, 45)
		self._Rc9.TabIndex = 106
		self._Rc9.UseVisualStyleBackColor = False
		self._Rc9.Click += self.Rc9Click
		# 
		# Rc6
		# 
		self._Rc6.BackColor = System.Drawing.Color.Crimson
		self._Rc6.Location = System.Drawing.Point(176, 87)
		self._Rc6.Name = "Rc6"
		self._Rc6.Size = System.Drawing.Size(53, 45)
		self._Rc6.TabIndex = 107
		self._Rc6.UseVisualStyleBackColor = False
		self._Rc6.Click += self.Rc6Click
		# 
		# Rc10
		# 
		self._Rc10.BackColor = System.Drawing.Color.Crimson
		self._Rc10.Location = System.Drawing.Point(236, 138)
		self._Rc10.Name = "Rc10"
		self._Rc10.Size = System.Drawing.Size(53, 45)
		self._Rc10.TabIndex = 108
		self._Rc10.UseVisualStyleBackColor = False
		self._Rc10.Click += self.Rc10Click
		# 
		# Rc7
		# 
		self._Rc7.BackColor = System.Drawing.Color.Crimson
		self._Rc7.Location = System.Drawing.Point(301, 87)
		self._Rc7.Name = "Rc7"
		self._Rc7.Size = System.Drawing.Size(53, 45)
		self._Rc7.TabIndex = 109
		self._Rc7.UseVisualStyleBackColor = False
		self._Rc7.Click += self.Rc7Click
		# 
		# Rc11
		# 
		self._Rc11.BackColor = System.Drawing.Color.Crimson
		self._Rc11.Location = System.Drawing.Point(577, 374)
		self._Rc11.Name = "Rc11"
		self._Rc11.Size = System.Drawing.Size(53, 45)
		self._Rc11.TabIndex = 110
		self._Rc11.UseVisualStyleBackColor = False
		self._Rc11.Click += self.Rc11Click
		# 
		# Rc12
		# 
		self._Rc12.BackColor = System.Drawing.Color.Crimson
		self._Rc12.Location = System.Drawing.Point(488, 138)
		self._Rc12.Name = "Rc12"
		self._Rc12.Size = System.Drawing.Size(53, 45)
		self._Rc12.TabIndex = 111
		self._Rc12.UseVisualStyleBackColor = False
		self._Rc12.Click += self.Button9Click
		# 
		# Rc8
		# 
		self._Rc8.BackColor = System.Drawing.Color.Crimson
		self._Rc8.Location = System.Drawing.Point(422, 87)
		self._Rc8.Name = "Rc8"
		self._Rc8.Size = System.Drawing.Size(53, 45)
		self._Rc8.TabIndex = 112
		self._Rc8.UseVisualStyleBackColor = False
		self._Rc8.Click += self.Rc8Click
		# 
		# Rc4
		# 
		self._Rc4.BackColor = System.Drawing.Color.Crimson
		self._Rc4.Location = System.Drawing.Point(488, 36)
		self._Rc4.Name = "Rc4"
		self._Rc4.Size = System.Drawing.Size(53, 45)
		self._Rc4.TabIndex = 113
		self._Rc4.UseVisualStyleBackColor = False
		self._Rc4.Click += self.Rc4Click
		# 
		# Rc3
		# 
		self._Rc3.BackColor = System.Drawing.Color.Crimson
		self._Rc3.Location = System.Drawing.Point(364, 36)
		self._Rc3.Name = "Rc3"
		self._Rc3.Size = System.Drawing.Size(53, 45)
		self._Rc3.TabIndex = 114
		self._Rc3.UseVisualStyleBackColor = False
		self._Rc3.Click += self.Rc3Click
		# 
		# Rc2
		# 
		self._Rc2.BackColor = System.Drawing.Color.Crimson
		self._Rc2.Location = System.Drawing.Point(239, 36)
		self._Rc2.Name = "Rc2"
		self._Rc2.Size = System.Drawing.Size(53, 45)
		self._Rc2.TabIndex = 115
		self._Rc2.UseVisualStyleBackColor = False
		self._Rc2.Click += self.Rc2Click
		# 
		# BTt
		# 
		self._BTt.Enabled = True
		self._BTt.Tick += self.BTtTick
		# 
		# RTt
		# 
		self._RTt.Enabled = True
		self._RTt.Tick += self.RTtTick
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(577, 132)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(67, 51)
		self._button2.TabIndex = 116
		self._button2.Text = "Move Left"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(577, 266)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(67, 56)
		self._button3.TabIndex = 118
		self._button3.Text = "Move Right"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(560, 337)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(105, 31)
		self._button4.TabIndex = 119
		self._button4.Text = "Reset"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(560, 199)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(105, 23)
		self._button1.TabIndex = 120
		self._button1.Text = "Move Up"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(560, 237)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(105, 23)
		self._button5.TabIndex = 121
		self._button5.Text = "Move Down"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Goldenrod
		self.ClientSize = System.Drawing.Size(677, 493)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._Rc2)
		self.Controls.Add(self._Rc3)
		self.Controls.Add(self._Rc4)
		self.Controls.Add(self._Rc8)
		self.Controls.Add(self._Rc12)
		self.Controls.Add(self._Rc11)
		self.Controls.Add(self._Rc7)
		self.Controls.Add(self._Rc10)
		self.Controls.Add(self._Rc6)
		self.Controls.Add(self._Rc9)
		self.Controls.Add(self._Rc5)
		self.Controls.Add(self._Rc1)
		self.Controls.Add(self._Bc4)
		self.Controls.Add(self._Bc10)
		self.Controls.Add(self._Bc9)
		self.Controls.Add(self._Bc2)
		self.Controls.Add(self._Bc5)
		self.Controls.Add(self._Bc6)
		self.Controls.Add(self._Bc3)
		self.Controls.Add(self._Bc11)
		self.Controls.Add(self._Bc7)
		self.Controls.Add(self._Bc12)
		self.Controls.Add(self._Bc8)
		self.Controls.Add(self._Bc1)
		self.Controls.Add(self._label57)
		self.Controls.Add(self._label58)
		self.Controls.Add(self._label59)
		self.Controls.Add(self._label60)
		self.Controls.Add(self._label61)
		self.Controls.Add(self._label62)
		self.Controls.Add(self._label63)
		self.Controls.Add(self._label64)
		self.Controls.Add(self._label49)
		self.Controls.Add(self._label50)
		self.Controls.Add(self._label51)
		self.Controls.Add(self._label52)
		self.Controls.Add(self._label53)
		self.Controls.Add(self._label54)
		self.Controls.Add(self._label55)
		self.Controls.Add(self._label56)
		self.Controls.Add(self._label41)
		self.Controls.Add(self._label42)
		self.Controls.Add(self._label43)
		self.Controls.Add(self._label44)
		self.Controls.Add(self._label45)
		self.Controls.Add(self._label46)
		self.Controls.Add(self._label47)
		self.Controls.Add(self._label48)
		self.Controls.Add(self._label33)
		self.Controls.Add(self._label34)
		self.Controls.Add(self._label35)
		self.Controls.Add(self._label36)
		self.Controls.Add(self._label37)
		self.Controls.Add(self._label38)
		self.Controls.Add(self._label39)
		self.Controls.Add(self._label40)
		self.Controls.Add(self._label31)
		self.Controls.Add(self._label32)
		self.Controls.Add(self._label29)
		self.Controls.Add(self._label30)
		self.Controls.Add(self._label27)
		self.Controls.Add(self._label28)
		self.Controls.Add(self._label25)
		self.Controls.Add(self._label26)
		self.Controls.Add(self._label23)
		self.Controls.Add(self._label24)
		self.Controls.Add(self._label21)
		self.Controls.Add(self._label22)
		self.Controls.Add(self._label19)
		self.Controls.Add(self._label20)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._label18)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "phase checkers"
		self.Load += self.MainFormLoad
		self.DragDrop += self.MainFormDragDrop
		self.KeyDown += self.MainFormKeyDown
		self.MouseDown += self.MainFormMouseDown
		self.ResumeLayout(False)



# buttons 1-12 are blue.13-24 is red
	def MainFormLoad(self, sender, e):
		pass

	def MainFormKeyDown(self, sender, e):
		pass
			
	def MainFormMouseDown(self, sender, e):
		pass

	def MainFormDragDrop(self, sender, e):
		pass

	def PictureBox6Click(self, sender, e):
		pass

	def PictureBox7Click(self, sender, e):
		pass

	def PictureBox10Click(self, sender, e):
		pass
	
	def Label65Click(self, sender, e):
		if self.Mcr == True:
			self._Label65.Visible = True
			
	def PictureBox1Click(self, sender, e):
		pass

	def Button6Click(self, sender, e):
		self.pieceMoveB(self._Bc3, self.bch3)
		
		self.pieceTakeB(self._Bc3, self._Rc2)
		self.pieceTakeB(self._Bc3, self._Rc3)
		self.pieceTakeB(self._Bc3, self._Rc4)
		self.pieceTakeB(self._Bc3, self._Rc5)	
		self.pieceTakeB(self._Bc3, self._Rc6)
		self.pieceTakeB(self._Bc3, self._Rc7)
		self.pieceTakeB(self._Bc3, self._Rc8)
		self.pieceTakeB(self._Bc3, self._Rc9)
		self.pieceTakeB(self._Bc3, self._Rc10)
		self.pieceTakeB(self._Bc3, self._Rc11)
		self.pieceTakeB(self._Bc3, self._Rc12)

	def Button9Click(self, sender, e):
		self.pieceMoveR(self._Rc12, self.rch24)
		
		self.pieceTakeR(self._Rc12, self._Bc1)
		self.pieceTakeR(self._Rc12, self._Bc2)
		self.pieceTakeR(self._Rc12, self._Bc3)
		self.pieceTakeR(self._Rc12, self._Bc4)
		self.pieceTakeR(self._Rc12, self._Bc5)
		self.pieceTakeR(self._Rc12, self._Bc6)
		self.pieceTakeR(self._Rc12, self._Bc7)
		self.pieceTakeR(self._Rc12, self._Bc8)
		self.pieceTakeR(self._Rc12, self._Bc9)
		self.pieceTakeR(self._Rc12, self._Bc10)
		self.pieceTakeR(self._Rc12, self._Bc11)
		self.pieceTakeR(self._Rc12, self._Bc12)

	def Bc2Click(self, sender, e):
		self.pieceMoveB(self._Bc2, self.bch2)
		
		self.pieceTakeB(self._Bc2, self._Rc1)
		self.pieceTakeB(self._Bc2, self._Rc2)
		self.pieceTakeB(self._Bc2, self._Rc3)
		self.pieceTakeB(self._Bc2, self._Rc4)
		self.pieceTakeB(self._Bc2, self._Rc5)	
		self.pieceTakeB(self._Bc2, self._Rc6)
		self.pieceTakeB(self._Bc2, self._Rc7)
		self.pieceTakeB(self._Bc2, self._Rc8)
		self.pieceTakeB(self._Bc2, self._Rc9)
		self.pieceTakeB(self._Bc2, self._Rc10)
		self.pieceTakeB(self._Bc2, self._Rc11)
		self.pieceTakeB(self._Bc2, self._Rc12)
		
	def RTtTick(self, sender, e):
		if self._Rc1.Top >= 378:
			self.rch13 = True
		if self._Rc2.Top >= 378:
			self.rch14 = True
		if self._Rc3.Top >= 378:
			self.rch15 = True
		if self._Rc4.Top >= 378:
			self.rch16 = True
		if self._Rc5.Top >= 378:
			self.rch17 = True
		if self._Rc6.Top >= 378:
			self.rch18 = True
		if self._Rc7.Top >= 378:
			self.rch19 = True
		if self._Rc8.Top >= 378:
			self.rch20 = True
		if self._Rc9.Top >= 378:
			self.rch21 = True
		if self._Rc10.Top >= 378:
			self.rch22 = True
		if self._Rc11.Top >= 378:
			self.rch23 = True
		if self._Rc12.Top >= 378:
			self.rch24 = True
		

	def BTtTick(self, sender, e):
		if self._Bc1.Top <= 41:
			self.bch1 = True
		if self._Bc2.Top <= 41:
			self.bch2 = True
		if self._Bc3.Top <= 41:
			self.bch3 = True
		if self._Bc4.Top <= 41:
			self.bch4 = True
		if self._Bc5.Top <= 41:
			self.bch5 = True
		if self._Bc6.Top <= 41:
			self.bch6 = True
		if self._Bc7.Top <= 41:
			self.bch7 = True
		if self._Bc8.Top <= 41:
			self.bch8 = True
		if self._Bc9.Top <= 41:
			self.bch9 = True
		if self._Bc10.Top <= 41:
			self.bch10 = True
		if self._Bc11.Top <= 41:
			self.bch11 = True
		if self._Bc12.Top <= 41:
			self.bch12 = True
		
			
	
	def pieceMoveB(self, piece, king):
		if self.Mcr == True and self.Bturn == True and self.McU == True:
			piece.Top += -51
			piece.Left += 64
			self.Bturn = False
			self.Rturn = True
		if self.Mcr == False and self.Bturn == True and self.McU == True:
			piece.Top += -51
			piece.Left += -64
			self.Bturn = False
			self.Rturn = True
		if self.Mcr == True and self.Bturn == True and self.McU == False and king == True:
			piece.Top += 51
			piece.Left += 64
			self.Bturn = False
			self.Rturn = True
		if self.Mcr == False and self.Bturn == True and self.McU == False and king == True:
			piece.Top += 51
			piece.Left += -64
			self.Bturn = False
			self.Rturn = True
	
	def pieceMoveR(self, piece, king):
		if self.Mcr == True and self.Rturn == True and self.McU == True:
			piece.Top += 51
			piece.Left += 61
			self.Bturn = True
			self.Rturn = False
		if self.Mcr == False and self.Rturn == True and self.McU == True:
			piece.Top += 51
			piece.Left += -61
			self.Bturn = True
			self.Rturn = False
		if self.Mcr == True and self.Rturn == True and self.McU == False and king == True:
			piece.Top += -51
			piece.Left += 61
			self.Bturn = True
			self.Rturn = False
		if self.Mcr == False and self.Rturn == True and self.McU == False and king == True:
			piece.Top += -51
			piece.Left += -61
			self.Bturn = True
			self.Rturn = False
	
	def pieceTakeB(self, taker, piece):
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == True and self.McU == True :
			piece.Top = 374
			piece.Left = 577
			taker.Top += -51
			taker.Left += 64
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == False and self.McU == True :
			piece.Top = 374
			piece.Left = 577
			taker.Top += -51
			taker.Left += -64
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == True and self.McU == False :
			piece.Top = 374
			piece.Left = 577
			taker.Top += 51
			taker.Left += 64
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == False and self.McU == False :
			piece.Top = 374
			piece.Left = 577
			taker.Top += 51
			taker.Left += -64
			
	def pieceTakeR(self, taker, piece):
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == True and self.McU == True :
			piece.Left = 577
			piece.Top = 39
			taker.Top += 51
			taker.Left += 61
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == False and self.McU == True :
			piece.Top = 374
			piece.Left = 577
			taker.Top += 51
			taker.Left += -64
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == True and self.McU == False :
			piece.Top = 374
			piece.Left = 577
			taker.Top += -51
			taker.Left += 64
		if taker.Left >= piece.Left - 10 and taker.Right <= piece.Right + 10 and taker.Top >= piece.Top - 10 and abs(taker.Top - piece.Top) <= 10 and self.Mcr == False and self.McU == False :
			piece.Top = 374
			piece.Left = 577
			taker.Top += -51
			taker.Left += -64
	
	def Button2Click(self, sender, e):
		self.Mcr = False

	def Button3Click(self, sender, e):
		self.Mcr = True

	def Button4Click(self, sender, e):
		def reset():
			self._Bc1.Top   = 291
			self._Bc1.Left  = 48
			self._Bc2.Top   = 291
			self._Bc2.Left  = 176
			self._Bc3.Top   = 291
			self._Bc3.Left  = 301
			self._Bc4.Top   = 291
			self._Bc4.Left  = 422
			self._Bc5.Top   = 342
			self._Bc5.Left  = 112
			self._Bc6.Top   = 342
			self._Bc6.Left  = 236
			self._Bc7.Top   = 342
			self._Bc7.Left  = 360
			self._Bc8.Top   = 342
			self._Bc8.Left  = 488
			self._Bc9.Top   = 393
			self._Bc9.Left  = 48
			self._Bc10.Top  = 393
			self._Bc10.Left = 176
			self._Bc11.Top  = 393
			self._Bc11.Left = 301
			self._Bc12.Top  = 393
			self._Bc12.Left = 426
			# Red Checkers start here			
			self._Rc1.Top   = 36
			self._Rc1.Left  = 111
			self._Rc2.Top   = 36
			self._Rc2.Left  = 239
			self._Rc3.Top   = 36
			self._Rc3.Left  = 364
			self._Rc4.Top   = 36
			self._Rc4.Left  = 488
			self._Rc5.Top   = 87
			self._Rc5.Left  = 48
			self._Rc6.Top   = 87
			self._Rc6.Left  = 176
			self._Rc7.Top   = 87
			self._Rc7.Left  = 301
			self._Rc8.Top   = 87
			self._Rc8.Left  = 422
			self._Rc9.Top   = 138
			self._Rc9.Left  = 112
			self._Rc10.Top  = 138
			self._Rc10.Left = 236
			self._Rc11.Top  = 138
			self._Rc11.Left = 364
			self._Rc12.Top  = 138
			self._Rc12.Left = 488
		reset()

	def Rc9Click(self, sender, e):
		self.pieceMoveR(self._Rc9, self.rch21)
		
		self.pieceTakeR(self._Rc9, self._Bc1)
		self.pieceTakeR(self._Rc9, self._Bc2)
		self.pieceTakeR(self._Rc9, self._Bc3)
		self.pieceTakeR(self._Rc9, self._Bc4)
		self.pieceTakeR(self._Rc9, self._Bc5)
		self.pieceTakeR(self._Rc9, self._Bc6)
		self.pieceTakeR(self._Rc9, self._Bc7)
		self.pieceTakeR(self._Rc9, self._Bc8)
		self.pieceTakeR(self._Rc9, self._Bc9)
		self.pieceTakeR(self._Rc9, self._Bc10)
		self.pieceTakeR(self._Rc9, self._Bc11)
		self.pieceTakeR(self._Rc9, self._Bc12)

	def Rc10Click(self, sender, e):
		self.pieceMoveR(self._Rc10, self.rch22)
		
		self.pieceTakeR(self._Rc10, self._Bc1)
		self.pieceTakeR(self._Rc10, self._Bc2)
		self.pieceTakeR(self._Rc10, self._Bc3)
		self.pieceTakeR(self._Rc10, self._Bc4)
		self.pieceTakeR(self._Rc10, self._Bc5)
		self.pieceTakeR(self._Rc10, self._Bc6)
		self.pieceTakeR(self._Rc10, self._Bc7)
		self.pieceTakeR(self._Rc10, self._Bc8)
		self.pieceTakeR(self._Rc10, self._Bc9)
		self.pieceTakeR(self._Rc10, self._Bc10)
		self.pieceTakeR(self._Rc10, self._Bc11)
		self.pieceTakeR(self._Rc10, self._Bc12)

	def Rc11Click(self, sender, e):
		self.pieceMoveR(self._Rc11, self.rch23)
		
		self.pieceTakeR(self._Rc11, self._Bc1)
		self.pieceTakeR(self._Rc11, self._Bc2)
		self.pieceTakeR(self._Rc11, self._Bc3)
		self.pieceTakeR(self._Rc11, self._Bc4)
		self.pieceTakeR(self._Rc11, self._Bc5)
		self.pieceTakeR(self._Rc11, self._Bc6)
		self.pieceTakeR(self._Rc11, self._Bc7)
		self.pieceTakeR(self._Rc11, self._Bc8)
		self.pieceTakeR(self._Rc11, self._Bc9)
		self.pieceTakeR(self._Rc11, self._Bc10)
		self.pieceTakeR(self._Rc11, self._Bc11)
		self.pieceTakeR(self._Rc11, self._Bc12)

	def Rc11Click(self, sender, e):
		self.pieceMoveR(self._Rc11, self.rch23)
		
		self.pieceTakeR(self._Rc11, self._Bc1)
		self.pieceTakeR(self._Rc11, self._Bc2)
		self.pieceTakeR(self._Rc11, self._Bc3)
		self.pieceTakeR(self._Rc11, self._Bc4)
		self.pieceTakeR(self._Rc11, self._Bc5)
		self.pieceTakeR(self._Rc11, self._Bc6)
		self.pieceTakeR(self._Rc11, self._Bc7)
		self.pieceTakeR(self._Rc11, self._Bc8)
		self.pieceTakeR(self._Rc11, self._Bc9)
		self.pieceTakeR(self._Rc11, self._Bc10)
		self.pieceTakeR(self._Rc11, self._Bc11)
		self.pieceTakeR(self._Rc11, self._Bc12)

	def Rc5Click(self, sender, e):
		self.pieceMoveR(self._Rc5, self.rch17)
		
		self.pieceTakeR(self._Rc5, self._Bc1)
		self.pieceTakeR(self._Rc5, self._Bc2)
		self.pieceTakeR(self._Rc5, self._Bc3)
		self.pieceTakeR(self._Rc5, self._Bc4)
		self.pieceTakeR(self._Rc5, self._Bc5)
		self.pieceTakeR(self._Rc5, self._Bc6)
		self.pieceTakeR(self._Rc5, self._Bc7)
		self.pieceTakeR(self._Rc5, self._Bc8)
		self.pieceTakeR(self._Rc5, self._Bc9)
		self.pieceTakeR(self._Rc5, self._Bc10)
		self.pieceTakeR(self._Rc5, self._Bc11)
		self.pieceTakeR(self._Rc5, self._Bc12)

	def Rc6Click(self, sender, e):
		self.pieceMoveR(self._Rc6, self.rch18)
		
		self.pieceTakeR(self._Rc6, self._Bc1)
		self.pieceTakeR(self._Rc6, self._Bc2)
		self.pieceTakeR(self._Rc6, self._Bc3)
		self.pieceTakeR(self._Rc6, self._Bc4)
		self.pieceTakeR(self._Rc6, self._Bc5)
		self.pieceTakeR(self._Rc6, self._Bc6)
		self.pieceTakeR(self._Rc6, self._Bc7)
		self.pieceTakeR(self._Rc6, self._Bc8)
		self.pieceTakeR(self._Rc6, self._Bc9)
		self.pieceTakeR(self._Rc6, self._Bc10)
		self.pieceTakeR(self._Rc6, self._Bc11)
		self.pieceTakeR(self._Rc6, self._Bc12)

	def Rc1Click(self, sender, e):
		self.pieceMoveR(self._Rc1, self.rch13)
		
		self.pieceTakeR(self._Rc1, self._Bc1)
		self.pieceTakeR(self._Rc1, self._Bc2)
		self.pieceTakeR(self._Rc1, self._Bc3)
		self.pieceTakeR(self._Rc1, self._Bc4)
		self.pieceTakeR(self._Rc1, self._Bc5)
		self.pieceTakeR(self._Rc1, self._Bc6)
		self.pieceTakeR(self._Rc1, self._Bc7)
		self.pieceTakeR(self._Rc1, self._Bc8)
		self.pieceTakeR(self._Rc1, self._Bc9)
		self.pieceTakeR(self._Rc1, self._Bc10)
		self.pieceTakeR(self._Rc1, self._Bc11)
		self.pieceTakeR(self._Rc1, self._Bc12)

	def Rc2Click(self, sender, e):
		self.pieceMoveR(self._Rc2, self.rch14)
		
		self.pieceTakeR(self._Rc2, self._Bc1)
		self.pieceTakeR(self._Rc2, self._Bc2)
		self.pieceTakeR(self._Rc2, self._Bc3)
		self.pieceTakeR(self._Rc2, self._Bc4)
		self.pieceTakeR(self._Rc2, self._Bc5)
		self.pieceTakeR(self._Rc2, self._Bc6)
		self.pieceTakeR(self._Rc2, self._Bc7)
		self.pieceTakeR(self._Rc2, self._Bc8)
		self.pieceTakeR(self._Rc2, self._Bc9)
		self.pieceTakeR(self._Rc2, self._Bc10)
		self.pieceTakeR(self._Rc2, self._Bc11)
		self.pieceTakeR(self._Rc2, self._Bc12)

	def Rc3Click(self, sender, e):
		self.pieceMoveR(self._Rc3, self.rch15)
		
		self.pieceTakeR(self._Rc3, self._Bc1)
		self.pieceTakeR(self._Rc3, self._Bc2)
		self.pieceTakeR(self._Rc3, self._Bc3)
		self.pieceTakeR(self._Rc3, self._Bc4)
		self.pieceTakeR(self._Rc3, self._Bc5)
		self.pieceTakeR(self._Rc3, self._Bc6)
		self.pieceTakeR(self._Rc3, self._Bc7)
		self.pieceTakeR(self._Rc3, self._Bc8)
		self.pieceTakeR(self._Rc3, self._Bc9)
		self.pieceTakeR(self._Rc3, self._Bc10)
		self.pieceTakeR(self._Rc3, self._Bc11)
		self.pieceTakeR(self._Rc3, self._Bc12)

	def Rc4Click(self, sender, e):
		self.pieceMoveR(self._Rc4, self.rch16)
		
		self.pieceTakeR(self._Rc4, self._Bc1)
		self.pieceTakeR(self._Rc4, self._Bc2)
		self.pieceTakeR(self._Rc4, self._Bc3)
		self.pieceTakeR(self._Rc4, self._Bc4)
		self.pieceTakeR(self._Rc4, self._Bc5)
		self.pieceTakeR(self._Rc4, self._Bc6)
		self.pieceTakeR(self._Rc4, self._Bc7)
		self.pieceTakeR(self._Rc4, self._Bc8)
		self.pieceTakeR(self._Rc4, self._Bc9)
		self.pieceTakeR(self._Rc4, self._Bc10)
		self.pieceTakeR(self._Rc4, self._Bc11)
		self.pieceTakeR(self._Rc4, self._Bc12)

	def Rc7Click(self, sender, e):
		self.pieceMoveR(self._Rc7, self.rch19)
		
		self.pieceTakeR(self._Rc7, self._Bc1)
		self.pieceTakeR(self._Rc7, self._Bc2)
		self.pieceTakeR(self._Rc7, self._Bc3)
		self.pieceTakeR(self._Rc7, self._Bc4)
		self.pieceTakeR(self._Rc7, self._Bc5)
		self.pieceTakeR(self._Rc7, self._Bc6)
		self.pieceTakeR(self._Rc7, self._Bc7)
		self.pieceTakeR(self._Rc7, self._Bc8)
		self.pieceTakeR(self._Rc7, self._Bc9)
		self.pieceTakeR(self._Rc7, self._Bc10)
		self.pieceTakeR(self._Rc7, self._Bc11)
		self.pieceTakeR(self._Rc7, self._Bc12)

	def Rc8Click(self, sender, e):
		self.pieceMoveR(self._Rc8, self.rch20)
		
		self.pieceTakeR(self._Rc8, self._Bc1)
		self.pieceTakeR(self._Rc8, self._Bc2)
		self.pieceTakeR(self._Rc8, self._Bc3)
		self.pieceTakeR(self._Rc8, self._Bc4)
		self.pieceTakeR(self._Rc8, self._Bc5)
		self.pieceTakeR(self._Rc8, self._Bc6)
		self.pieceTakeR(self._Rc8, self._Bc7)
		self.pieceTakeR(self._Rc8, self._Bc8)
		self.pieceTakeR(self._Rc8, self._Bc9)
		self.pieceTakeR(self._Rc8, self._Bc10)
		self.pieceTakeR(self._Rc8, self._Bc11)
		self.pieceTakeR(self._Rc8, self._Bc12)

	def Bc1Click(self, sender, e):
		self.pieceMoveB(self._Bc1, self.bch1)
		
		self.pieceTakeB(self._Bc1, self._Rc2)
		self.pieceTakeB(self._Bc1, self._Rc3)
		self.pieceTakeB(self._Bc1, self._Rc4)
		self.pieceTakeB(self._Bc1, self._Rc5)	
		self.pieceTakeB(self._Bc1, self._Rc6)
		self.pieceTakeB(self._Bc1, self._Rc7)
		self.pieceTakeB(self._Bc1, self._Rc8)
		self.pieceTakeB(self._Bc1, self._Rc9)
		self.pieceTakeB(self._Bc1, self._Rc10)
		self.pieceTakeB(self._Bc1, self._Rc11)
		self.pieceTakeB(self._Bc1, self._Rc12)

	def Bc4Click(self, sender, e):
		self.pieceMoveB(self._Bc4, self.bch4)
		
		self.pieceTakeB(self._Bc4, self._Rc2)
		self.pieceTakeB(self._Bc4, self._Rc3)
		self.pieceTakeB(self._Bc4, self._Rc4)
		self.pieceTakeB(self._Bc4, self._Rc5)	
		self.pieceTakeB(self._Bc4, self._Rc6)
		self.pieceTakeB(self._Bc4, self._Rc7)
		self.pieceTakeB(self._Bc4, self._Rc8)
		self.pieceTakeB(self._Bc4, self._Rc9)
		self.pieceTakeB(self._Bc4, self._Rc10)
		self.pieceTakeB(self._Bc4, self._Rc11)
		self.pieceTakeB(self._Bc4, self._Rc12)

	def Bc5Click(self, sender, e):
		self.pieceMoveB(self._Bc5, self.bch5)
		
		self.pieceTakeB(self._Bc5, self._Rc2)
		self.pieceTakeB(self._Bc5, self._Rc3)
		self.pieceTakeB(self._Bc5, self._Rc4)
		self.pieceTakeB(self._Bc5, self._Rc5)	
		self.pieceTakeB(self._Bc5, self._Rc6)
		self.pieceTakeB(self._Bc5, self._Rc7)
		self.pieceTakeB(self._Bc5, self._Rc8)
		self.pieceTakeB(self._Bc5, self._Rc9)
		self.pieceTakeB(self._Bc5, self._Rc10)
		self.pieceTakeB(self._Bc5, self._Rc11)
		self.pieceTakeB(self._Bc5, self._Rc12)

	def Bc6Click(self, sender, e):
		self.pieceMoveB(self._Bc6, self.bch6)
		
		self.pieceTakeB(self._Bc6, self._Rc2)
		self.pieceTakeB(self._Bc6, self._Rc3)
		self.pieceTakeB(self._Bc6, self._Rc4)
		self.pieceTakeB(self._Bc6, self._Rc5)	
		self.pieceTakeB(self._Bc6, self._Rc6)
		self.pieceTakeB(self._Bc6, self._Rc7)
		self.pieceTakeB(self._Bc6, self._Rc8)
		self.pieceTakeB(self._Bc6, self._Rc9)
		self.pieceTakeB(self._Bc6, self._Rc10)
		self.pieceTakeB(self._Bc6, self._Rc11)
		self.pieceTakeB(self._Bc6, self._Rc12)

	def Bc7Click(self, sender, e):
		self.pieceMoveB(self._Bc7, self.bch7)
		
		self.pieceTakeB(self._Bc7, self._Rc2)
		self.pieceTakeB(self._Bc7, self._Rc3)
		self.pieceTakeB(self._Bc7, self._Rc4)
		self.pieceTakeB(self._Bc7, self._Rc5)	
		self.pieceTakeB(self._Bc7, self._Rc6)
		self.pieceTakeB(self._Bc7, self._Rc7)
		self.pieceTakeB(self._Bc7, self._Rc8)
		self.pieceTakeB(self._Bc7, self._Rc9)
		self.pieceTakeB(self._Bc7, self._Rc10)
		self.pieceTakeB(self._Bc7, self._Rc11)
		self.pieceTakeB(self._Bc7, self._Rc12)

	def Bc8Click(self, sender, e):
		self.pieceMoveB(self._Bc8, self.bch8)
		
		self.pieceTakeB(self._Bc8, self._Rc2)
		self.pieceTakeB(self._Bc8, self._Rc3)
		self.pieceTakeB(self._Bc8, self._Rc4)
		self.pieceTakeB(self._Bc8, self._Rc5)	
		self.pieceTakeB(self._Bc8, self._Rc6)
		self.pieceTakeB(self._Bc8, self._Rc7)
		self.pieceTakeB(self._Bc8, self._Rc8)
		self.pieceTakeB(self._Bc8, self._Rc9)
		self.pieceTakeB(self._Bc8, self._Rc10)
		self.pieceTakeB(self._Bc8, self._Rc11)
		self.pieceTakeB(self._Bc8, self._Rc12)

	def Bc9Click(self, sender, e):
		self.pieceMoveB(self._Bc9, self.bch9)
		
		self.pieceTakeB(self._Bc9, self._Rc2)
		self.pieceTakeB(self._Bc9, self._Rc3)
		self.pieceTakeB(self._Bc9, self._Rc4)
		self.pieceTakeB(self._Bc9, self._Rc5)	
		self.pieceTakeB(self._Bc9, self._Rc6)
		self.pieceTakeB(self._Bc9, self._Rc7)
		self.pieceTakeB(self._Bc9, self._Rc8)
		self.pieceTakeB(self._Bc9, self._Rc9)
		self.pieceTakeB(self._Bc9, self._Rc10)
		self.pieceTakeB(self._Bc9, self._Rc11)
		self.pieceTakeB(self._Bc9, self._Rc12)

	def Bc10Click(self, sender, e):
		self.pieceMoveB(self._Bc10, self.bch10)
		
		self.pieceTakeB(self._Bc10, self._Rc2)
		self.pieceTakeB(self._Bc10, self._Rc3)
		self.pieceTakeB(self._Bc10, self._Rc4)
		self.pieceTakeB(self._Bc10, self._Rc5)	
		self.pieceTakeB(self._Bc10, self._Rc6)
		self.pieceTakeB(self._Bc10, self._Rc7)
		self.pieceTakeB(self._Bc10, self._Rc8)
		self.pieceTakeB(self._Bc10, self._Rc9)
		self.pieceTakeB(self._Bc10, self._Rc10)
		self.pieceTakeB(self._Bc10, self._Rc11)
		self.pieceTakeB(self._Bc10, self._Rc12)

	def Bc11Click(self, sender, e):
		self.pieceMoveB(self._Bc11, self.bch11)
		
		self.pieceTakeB(self._Bc11, self._Rc2)
		self.pieceTakeB(self._Bc11, self._Rc3)
		self.pieceTakeB(self._Bc11, self._Rc4)
		self.pieceTakeB(self._Bc11, self._Rc5)	
		self.pieceTakeB(self._Bc11, self._Rc6)
		self.pieceTakeB(self._Bc11, self._Rc7)
		self.pieceTakeB(self._Bc11, self._Rc8)
		self.pieceTakeB(self._Bc11, self._Rc9)
		self.pieceTakeB(self._Bc11, self._Rc10)
		self.pieceTakeB(self._Bc11, self._Rc11)
		self.pieceTakeB(self._Bc11, self._Rc12)

	def Bc12Click(self, sender, e):
		self.pieceMoveB(self._Bc12, self.bch12)
		
		self.pieceTakeB(self._Bc12, self._Rc2)
		self.pieceTakeB(self._Bc12, self._Rc3)
		self.pieceTakeB(self._Bc12, self._Rc4)
		self.pieceTakeB(self._Bc12, self._Rc5)	
		self.pieceTakeB(self._Bc12, self._Rc6)
		self.pieceTakeB(self._Bc12, self._Rc7)
		self.pieceTakeB(self._Bc12, self._Rc8)
		self.pieceTakeB(self._Bc12, self._Rc9)
		self.pieceTakeB(self._Bc12, self._Rc10)
		self.pieceTakeB(self._Bc12, self._Rc11)
		self.pieceTakeB(self._Bc12, self._Rc12)

	def Button1Click(self, sender, e):
		self.McU = True
#		if self.McU == True:
#			MessageBox.Show("on")

	def Button5Click(self, sender, e):
		self.McU = False
#		if self.McU == False:
#			MessageBox.Show("off")

	

	def Label34Click(self, sender, e):
		pass