# 学习笔记
## 布隆过滤器(Bloom Filter)的原理和实现
+ 在网络爬虫里，一个网址是否被访问过
+ 字处理软件中，需要检查一个英语单词是否拼写正确
+ yahoo, gmail等邮箱垃圾邮件过滤功能
+ 特点：有误判，速度特别快
+ 与哈希表相比只能判断存在与否，判否必否，判是未必
+ 可以用bitarray实现
## LRU Cache缓存：
+ 实用性较强
+ python使用有序字典collections.OrderedDict实现
+ 计算机Cache实现算法不止LRU,https://en.wikipedia.org/wiki/Cache_replacement_policies
## 排序：
+ O(n^2): 冒泡、插入、选择、希尔(最坏)
+ O(nlog(n)): 归并、快排、堆排序
## 高级排序
+ 计数、桶排序、基数