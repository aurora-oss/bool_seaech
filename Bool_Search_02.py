from Bool_Search import searcher


class tom(object):
    def __init__(self):
        self.searcher = searcher()

    def run(self):
        try:
            while 1:
                choice = eval(input("请输入查询类型：\n1------双单词and链接请按1------：\n2------进行模糊查询请按2-------"
                                    "：\n3------退出请按0--------------：\n"))
                if choice == 1:
                    self.searcher.andsearch()
                elif choice == 2:
                    self.searcher.re_search()
                elif choice ==0:
                    break
        except TypeError as e:
            print("请输入正确的数字\n")


def main():
    bob = tom()
    bob.run()


if __name__=='__main__':
    main()