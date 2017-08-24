
with open('xyj.txt', 'r', encoding='utf-8') as fr:
	for line in fr.readlines():
		line=line.strip()
		characters=[]
		stat={}
		
		if len(line)==0:
			continue
		for x in range(0,len(line)):
			if not line[x] in characters:
				characters.append(line[x])
			if not line[x] in stat.keys():
				stat[line[x]]=0
			stat[line[x]]+=1
			


					
		
				
			







