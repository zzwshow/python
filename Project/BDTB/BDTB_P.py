#coding=utf-8
#爬去百度贴吧
import requests
import re

class Bdtb:
	
	#初始化。传入基本url,时候只看楼主
	def __init__(self,base_url,see_lz):
		self.base_url=base_url
		self.see_lz='?see_lz='+str(see_lz)
		self.tool=Tool()  #调用Tool类
		#self.file=open('tb.txt','w')
		
		

	#传入页码，获取该页帖子的代码
	def getPage(self,pageNum):
		try:
			url=self.base_url+self.see_lz+'&pn='+str(pageNum)
			response=requests.get(url)
			return response.text
			
		except Exception as e:
			print('连接失败',e)
			return None
	
	#进一步获取源码中的标题
	def getTitle(self):
		page=self.getPage(1) #获取第一页的源代码
		pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S) #定义正则
		result = re.search(pattern,page) #从源码中搜索匹配值
		if result:
			#print(result.group(1)) #
			return result.group(1).strip()
		else:
			return None
	
	#提取梯子页数
	def getPageNum(self):
		page=self.getPage(1)
		pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result=re.search(pattern,page)
		return result.group(1).strip()
	
	
	#提取没一层的内容！
	def getContext(self,page):
		pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items=re.findall(pattern,page)
		floor=1
		for item in items:
			print('\n',floor,u"楼---------------------------")
			print(self.tool.replace(item))
			floor += 1
		
			
			

class Tool:
	# 去除img标签,7位长空格
	removeImg = re.compile('<img.*?>| {7}|')
	# 删除超链接标签
	removeAddr = re.compile('<a.*?>|</a>')
	# 把换行的标签换为\n
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	# 将表格制表<td>替换为\t
	replaceTD = re.compile('<td>')
	# 把段落开头换为\n加空两格
	replacePara = re.compile('<p.*?>')
	# 将换行符或双换行符替换为\n
	replaceBR = re.compile('<br><br>|<br>')
	# 将其余标签剔除
	removeExtraTag = re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg, "", x)
		x = re.sub(self.removeAddr, "", x)
		x = re.sub(self.replaceLine, "\n", x)
		x = re.sub(self.replaceTD, "\t", x)
		x = re.sub(self.replacePara, "\n    ", x)
		x = re.sub(self.replaceBR, "\n", x)
		x = re.sub(self.removeExtraTag, "", x)
		# strip()将前后多余内容删除
		return x.strip()





baseURL = 'https://tieba.baidu.com/p/3138733512'
r=Bdtb(baseURL,1)
r.getContext(r.getPage(5))







