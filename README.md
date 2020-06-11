**_注：本项目今后将在 OSChina 继续更新_**

## 项目目标

将逐步实现木兰编程语言与交互环境的所有功能。

将源程序转换为 Python 的中间表示（AST），可较便利地实现各种语法设计。这种实现方式值得探索和研究。

## 运行

如下运行源码（建议`.ul`后缀）。

```
$ python 中.py 测试/运算/四则运算.ul
4
```

下面[例程](测试/引用/草蟒_海龟.ul)调用了[草蟒](https://www.oschina.net/p/grasspy)的中文 API：
```javascript
using * in 海龟
颜色("黄色", "红色")
开始填充()
角数 = 0
while 角数 < 5 {
  前进(200)
  右转(144)
  角数 = 角数 + 1
}
结束填充()
主循环()
```

更多测试用例[在此](测试)。

## 开发环境

本人使用 Mac。其他系统下如有问题请提交。

Python 3.7。如使用 3.8，语法树测试将失败。

为提高开发维护效率，本项目中尽量使用中文标识符。包括语法规则、Python 代码等等。

## 已实现功能

随着项目推进，将同步[语法说明](文档/语法说明.md)。另外，为调试方便，对报错等等反馈信息进行了中文化。

## 测试

```
$ chmod +x 中.py
$ python 测试.py
$ python test语法树.py
```

## 待决问题

高优先在前

### 语法部分

- for 循环
- try catch

### 其他

- 自动测试木兰代码
- 项目搭建 CI, 包括单元和集成测试
- 基于例程和 API 文档的组织的开发环境

## 许可证

GNU GPLv3
