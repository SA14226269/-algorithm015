学习笔记

#本周主要学习递归分治回溯算法，难度感觉比前两周明显加大需要多投入时间练习，总结了比较实用的代码模板

#递归模板

def recursion(level,param1,param2,...):
	#recursion terminator
	if level > MAX_LEVEL:
		process_result
		return
	#process logic in current level
	process(level,data...)
	
	#drill down
	self.recursion(level+1,p1,...)
	# reverse the current level status
	
#分治模板
def divide_conquer(problem, param1,param2,...):
	# recursion terminator
	if problem is None:
		print_result
		return
	#process data
	data = prepare_data(problem)
	subproblems = split_problem(problem,data)
	#conquer subproblems
	subresult1 = self.divide_conquer(subproblems[0], p1, ...)
	subresult2 ...
	subresult3 ...
	...
	#process and generate the final result
	result = process_result(subresult1,subresult2,subresult3,...)
	