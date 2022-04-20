# 倒排索引的建立
import re


class Search(object):

    index_file = "C:\\Users\\Administrator\\Desktop\\学习笔记\\智能信息检索\\项目合集\\布尔检索\\index.txt"
    object_file_initial = "C:\\Users\\Administrator\\Desktop\\学习笔记\\智能信息检索\\布尔检索\\text_"
    re_punctuation = r'[a-zA-Z]+'
    tmp_list = []

    def __init__(self):
        """
        倒排索引的建立
        """
        self.word_list()
        self.stringArraySort_Bubbl()
        file = open(self.index_file,'w+',encoding='utf-8')
        for i in range(len(self.tmp_list)):
            file.write(str(self.tmp_list[i])+"\n")
        print("布尔检索建立成功")

    def getmatch(self,content,word,number):     # 测试无误
        """
        :param content: 待匹配文本   类型为字典元素
        :param word: 字典的键
        :param number: 文章的id
        :return: 文本中含有返回 True反之则为False
        """
        id_list = content[word]     # 取文章id
        for i in range(len(id_list)):
            if number == id_list[i]:
                return True

    def compareStrings(self,word1, word2):
        for i in range(min(len(word1),len(word2))):
            if ord(word1[i]) != ord(word2[i]):
                return ord(word1[i]) - ord(word2[i])
        if len(word1) != len(word2):
            return len(word1) - len(word2)
        else:
            return 0

    def stringArraySort_Bubbl(self):
        # 构建一个列表，便于获取索引值
        a = []
        for j in range(len(self.tmp_list)):
            for key in self.tmp_list[j]:
                a.append(key)
        # 进行排序
        for i in range(len(self.tmp_list)-1):
            for j in range(i+1,len(self.tmp_list)):
                if self.compareStrings(a[i],a[j])>0:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp
                    temp = self.tmp_list[i]
                    self.tmp_list[i] = self.tmp_list[j]
                    self.tmp_list[j] = temp

    def word_(self,content):
        # 在tmp_list查找content 查到了相同值，
        for i in range(len(self.tmp_list)):
            for key in self.tmp_list[i]:
                if key == content:
                    return key

    def word_index(self,content):
        for j in range(len(self.tmp_list)):
            for key in self.tmp_list[j]:
                if key == content:
                    return self.tmp_list[j]

    def word_list(self):
        """
        function：读入待索引文件建立一个表
        :return:
        """
        for i in range(20):
            a=[]
            object_file = self.object_file_initial+str(i)+".txt"
            file = open(object_file, 'r', encoding='iso8859-1')
            content_initial = file.read()
            file.close()
            content = re.findall(self.re_punctuation, content_initial)    # 匹配了所有的英文单词
            for j in range(len(content)):           # 大写改小写
                x = content[j].lower()
                a.append(x)
            content = a         # 进行复制
            for j in range(len(content)):
                if self.word_(content[j]) == content[j]:          # 在字典中找到该元素
                    dec = self.tmp_list.index(self.word_index(content[j]))      # 在列表中找到该元素对应的id
                    if self.getmatch(self.tmp_list[dec],self.word_(content[j]),i):  # 不是这篇文章中第一次出现
                        x = self.tmp_list[dec][content[j]][len(self.tmp_list[dec][content[j]])-1]  # 仅给最后的元素加一
                        x = x + 1
                        self.tmp_list[dec][content[j]][len(self.tmp_list[dec][content[j]])-1] = x
                    else:           # 在该篇文章中是首次出现 增加文章id 注意在倒数第二处增加
                        self.tmp_list[dec][content[j]].insert(-1, i)
                        x = self.tmp_list[dec][content[j]][len(self.tmp_list[dec][content[j]]) - 1]  # 仅给最后的元素加一
                        x = x + 1
                        self.tmp_list[dec][content[j]][len(self.tmp_list[dec][content[j]]) - 1] = x
                else: # 如果在字典中没有查到该英文单词
                    temp = {}
                    temp[content[j]] = []
                    temp[content[j]].append(i)
                    temp[content[j]].append(1)          # 即出现了1次       最后以为表示词频
                    self.tmp_list.append(temp)


class searcher(Search):
    def andsearch(self):
        word_1 = input("请输入查询的第一个单词：\n")
        word_2 = input("请输入查询的第二个单词：\n")
        file = open(self.index_file, 'r', encoding='utf-8')
        content_init = file.read()
        content = content_init.split('\n')
        index_1 = -1
        index_2 = -1
        for i in range(len(content)-1):
            temp = eval(content[i])
            for key in temp:
                if word_1 == key:
                    index_1 = i
                if word_2 == key:
                    index_2 = i
        if index_2 != -1 and index_1 != -1:
            print("查到的单词为：\n"+content[index_1]+"\n"+content[index_2])
            search_id = []
            word_1_list = eval(content[index_1])[word_1]
            word_2_list = eval(content[index_2])[word_2]
            for i in range(len(word_2_list)-1):
                for j in range(len(word_1_list)-1):
                    if word_2_list[i] == word_1_list[j]:
                        search_id.append(word_2_list[i])
            print("在同一文章的有："+str(search_id))
        else:
            print("两者没有在相同文章中出现。")

    def re_search(self):
        answer = set([])
        re_str = input("2- - - - - -请输入你想查询的单词：")
        re_match = ('(^%s|%s$|.*%s.*|%s)' %(re_str,re_str,re_str,re_str))       # 构造查询的英语单词
        file = open(self.index_file, 'r', encoding='utf-8')
        content_init = file.read()
        content = content_init.split('\n')
        for i in range(len(content) - 1):
            temp = eval(content[i])
            for key in temp:
                match = re.findall(re_match,key)
                if len(match) !=0 and match[0] not in answer:
                    answer.add(match[0])
        if len(answer)!=0:
            print(answer)
        else:
            print("没有类似的单词")