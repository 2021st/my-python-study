worker = ['liulei','zhuyongrui','hujiale','zhangfeifan']
worker.sort(reverse=True)   #.后面的操作之后可以跟一个括号里面加入参数#
print (worker)
print (sorted(worker,reverse=False))    #sorted是一个函数？目前认为这样，因为不能打印work.sort，但是单独的sorted在之后的打印中没有显示#
print (len(worker))
newper='hu1'
worker.insert(6,newper)
print(worker)
worker.reverse()
print (worker)
worker.insert(7,"nn")   ##这种等于直接将变量运算##
print(worker)
print(sorted(worker,reverse=True))
print(worker)
sorted(worker,reverse=True)
print(worker)   #可以看到，这里的打印根本没有体现上一个运算，sorted可能是个函数，没有赋值#
worker=sorted(worker,reverse=False)
print(worker)
#思考：在前面的比如sorted是函数，需要赋值，不然只是运算，不修改变量？
# 在后面的就是赋值运算？那为什么不能放在print里面？
#sorted确实是函数。


