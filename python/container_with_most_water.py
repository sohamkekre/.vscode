def max_area (hieght):
# this code is optimal than the below as it has no for loopes
	res = 0
	l,r= 0,len(hieght)-1

	while l < r :
		area = (r-l) * min(hieght[l],hieght[r])
		res=max(area,res)
		if hieght[l] < hieght[r]:
			l += 1
		else:
			r -= 1
	print(res)

# this code takes more time because it has 2 for loopes thats why has big time complexity    
	# res = 0
	# for l in range (len(hieght)):
	# 	for r in range (l+1,len(hieght)):
	# 		area = (r-l) * min(hieght[l],hieght[r])
	# 		res = max(area,res)
	# print(res)

max_area([1,8,6,2,5,4,8,3,7])