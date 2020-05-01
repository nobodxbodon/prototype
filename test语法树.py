import unittest
import ast
from 数分析器 import 语法分析器, 分词器

class test语法树(unittest.TestCase):

    def test_行列号(self):
        节点 = self.生成语法树("2")
        expr节点 = self.取子节点(节点, "body", 0)  # module 节点下可有多个节点
        constant子节点 = self.取子节点(expr节点, "value")
        self.assertEqual(constant子节点.lineno, 1)
        self.assertEqual(constant子节点.col_offset, 1)

        节点 = self.生成语法树("1/0")
        #print(ast.dump(节点, True, True))
        for module子节点 in ast.iter_fields(节点):
            if module子节点[0] == "body":
                expr节点 = module子节点[1][0]  # module 节点下可有多个节点
                for expr子节点 in ast.iter_fields(expr节点):
                    if expr子节点[0] == "value":
                        call节点 = expr子节点[1]
                        for call子节点 in ast.iter_fields(call节点):
                            if call子节点[0] == "func":
                                name节点 = call子节点[1]
                                self.assertEqual(name节点.lineno, 1)
                                self.assertEqual(name节点.col_offset, 2)

        # 运算位置
        节点 = self.生成语法树("1+0")
        #print(ast.dump(节点, True, True))
        for module子节点 in ast.iter_fields(节点):
            if module子节点[0] == "body":
                expr节点 = module子节点[1][0]  # module 节点下可有多个节点
                for expr子节点 in ast.iter_fields(expr节点):
                    if expr子节点[0] == "value":
                        binop节点 = expr子节点[1]
                        self.assertEqual(binop节点.lineno, 1)
                        self.assertEqual(binop节点.col_offset, 1)

        # TODO: 第二行

    def 生成语法树(self, 源码):
        各词 = 分词器.lex(源码)
        分析器 = 语法分析器().创建()
        return 分析器.parse(各词)

    def 取子节点(self, 节点, 子节点名, 索引 = -1):
        for 子节点 in ast.iter_fields(节点):
            if 子节点[0] == 子节点名:
                if isinstance(子节点[1], list):
                    return 子节点[1][索引]
                else:
                    return 子节点[1]

if __name__ == '__main__':
    unittest.main()