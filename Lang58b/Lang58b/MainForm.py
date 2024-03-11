import math
import System.Drawing
import System.Windows.Forms

from math import *  
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(877, 420)
		self.Name = "MainForm"
		self.Text = "Lang58b"
		self.ResumeLayout(False)

