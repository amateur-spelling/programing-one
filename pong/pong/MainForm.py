﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False
		
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lbltitle = System.Windows.Forms.Label()
		self._left_score = System.Windows.Forms.Label()
		self._right_score = System.Windows.Forms.Label()
		self._lblBall = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.Color.White
		self._lbltitle.Location = System.Drawing.Point(12, 15)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# left_score
		# 
		self._left_score.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._left_score.ForeColor = System.Drawing.Color.White
		self._left_score.Location = System.Drawing.Point(78, 96)
		self._left_score.Name = "left_score"
		self._left_score.Size = System.Drawing.Size(166, 109)
		self._left_score.TabIndex = 1
		self._left_score.Text = "0"
		self._left_score.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# right_score
		# 
		self._right_score.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._right_score.ForeColor = System.Drawing.Color.White
		self._right_score.Location = System.Drawing.Point(734, 96)
		self._right_score.Name = "right_score"
		self._right_score.Size = System.Drawing.Size(166, 109)
		self._right_score.TabIndex = 2
		self._right_score.Text = "0"
		self._right_score.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblBall
		# 
		self._lblBall.BackColor = System.Drawing.Color.White
		self._lblBall.Location = System.Drawing.Point(479, 304)
		self._lblBall.Name = "lblBall"
		self._lblBall.Size = System.Drawing.Size(20, 20)
		self._lblBall.TabIndex = 3
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.Color.White
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 4
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 5
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(988, 607)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._lblBall)
		self.Controls.Add(self._right_score)
		self.Controls.Add(self._left_score)
		self.Controls.Add(self._lbltitle)
		self.Location = System.Drawing.Point(12, 25)
		self.Name = "MainForm"
		self.Text = "pong"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.Click += self.MainFormClick
		self.DoubleClick += self.MainFormDoubleClick
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		# make 3 cheats/secerts
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
	
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True:
			pdl.Top += 5
		else:
			pdl.Top -= 5
		if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
			tmr.Enabled = False

	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += 8 * self.balld
		
		if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4,5)
		elif ball.Left >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4,5)
			
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
		elif ball.Bottem <= 0:
			self.balld = 1
			ball.Top += 5 * self.balld
			self.ballup *= -1
		
		if ball.Location.X <= 0 or (ball.Location.X < lpdl.Left - 20 and ball.Location.Y < lpdl.Top):
			rscore += 1
			ball.Right = self.Width // 2
			ball.Top = self.Height // 2
			self._leftscore.Text = str(rscore)
		if ball.Lcation.X >= slef.Width or (ball.Location.X > rpdl.Right + 20 and ball.Location.Y . rpdl.Top):
			lscore += 1
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._leftscore.Text = str(lscore)
			
		if lscore == 10:
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to restart"
		if rscore == 10:
			self.TimerballTick.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Right Player Wins! Press R to restart"
		
		if self._timerboolean.Enabled == True:
			lpdl.Top = ball.Top - 20 

	def MainFormDoubleClick(self, sender, e):
		pass

	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)
	
	def LblballClick(self, sender, e):
		self._lblball.BackColor = Color.Red
		self.BackColor = Color.Green 

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width // 2
		self._lblball.Top = self.Height // 2
		self._lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width

	def MainFormClick(self, sender, e):
		pass

	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblBall
		lbleft = self._lblright
		title = self._lbltitle 
		
		def reset():
			title.Visible = True
			title.Text = "Press Enter to start or M to start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height // 2) - 100 + lblf.Height
			lblrt.Top = (self.Height // 2) - 100 + lbrt.Height
			bl.BackColor = Color.White
			
		if e.KeyCode == Keys.R:
			reset()
			
		if e.KeyCode == Keys.Enter:
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			if tmult.Enabled:
				tbool.Enabled = False
			title.Visible = False
			
		if e.KeyCode == Keys.M:
			reset()
			title.Visible = True
			title.Text = "Use W and S to move the left paddle; hit Enter to start"
			tmult.Enabled = True
			
		if tdum.Enabled:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enable = True
			elif e.KeyCode == Keys.Down:
				self.flafleft = False
				tright.Enable = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
		
		if tmult.Enabled and tball.Enabled:
			if e.KeyCode == Keys.W:
				pass
			elif e.KeyCode == keys.S:
				pass
			