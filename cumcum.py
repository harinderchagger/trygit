a = [2,3,2,3,4,5,6,4,5,5,4,3,5,5,6,7,7,8]
def cum_sum(n):
	lis = []
	lis1=[]
	lis.append(n[0])
	print(lis)
	for i in range(1,len(n)):
		lis.append(lis[i-1]+n[i])
		lis1.append(lis[i])
	print(lis)
cum_sum(a)
		
		
		
		
		
