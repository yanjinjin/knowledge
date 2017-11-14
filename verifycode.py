# -*- coding:utf-8 -*-
import os
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
import StringIO

class Verifycode():
	def __init__(self):
		self.code =""
		self.width = 60 * 4
		self.height = 60
		self.image = Image.new('RGB', (self.width,self.height), (255,255,255));
		#创建font对象
		self.font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),'static/fonts/Arial.ttf'),36);
		
		#创建draw对象
		self.draw = ImageDraw.Draw(self.image)
	#返回随机字母
	def charRandom(self):
	    return chr((random.randint(65,90)))
	
	#返回随机数字
	def numRandom(self):
	    return random.randint(0,9)
	
	#随机颜色
	def colorRandom1(self):
	    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
	
	#随机长生颜色2
	def colorRandom2(self):
	    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
	
	def getcode(self):
		#填充每一个颜色
		#for x in range(self.width):
		#    for y in range(self.height):
		#        self.draw.point((x,y), fill=self.colorRandom1())
		        
		#输出文字
		for t in range(4):
		    charR=self.charRandom()
		    self.code = "".join((self.code , charR))
		    self.draw.text((60*t+10,10), charR,font=self.font, fill=self.colorRandom2())
		
		print self.code
		#模糊
		#self.image = self.image.filter(ImageFilter.BLUR)
		self.image.save(os.path.join(os.path.dirname(__file__),'static/img/verifycode.jpg'),'jpeg')
		return self.code 

