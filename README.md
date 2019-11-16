

### learn python

> 基础知识的记录，练习代码。

#### 环境

* 当前版本：`3.7.0`
* 所有示例都是写在文件中`.py`
* 参考教程：[Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
* 官网文档：[python 3.7](https://docs.python.org/3.7/index.html)
* 执行文件`python index.py`
* 所有的代码都在同一个文件`*.py`中，各部分引用变量一致。

#### 基础一 :one:

[Python基础](https://blog.csdn.net/heroboyluck/article/details/101848511)

1. 输入输出：`print() / input()`
2. 条件语句:`if...else...`
3. 数据类型:`整数、浮点数、字符串、布尔值、空值(True/False)`
4. 数据结构：`list、tuple元组 、dict字典 `
5. 循环：`for...in...  、  while`
6. 函数：`*`可变参数、`**`可选参数

#### 基础二 :two:

[Python基础二](https://blog.csdn.net/heroboyluck/article/details/101876162)

1. 切片特性，获取部分数据：`[start:end]`
2. 迭代：迭代数据`Iterable`,迭代对象`Iterator`
3. 生成器：`()`通过调用`next()`获取下一个值。
4. 函数：匿名函数`lambda`、装饰器`@`
5. 模块:`from...import...`导入某个模块功能 / `import...`导入整个模块
6. 正则表达式：字符串自身的转义`r""`.提前编译正则`re.compile()`

#### 基础三 :three:

[Python 基础三](https://blog.csdn.net/heroboyluck/article/details/102468872)

1. 面向对象类、实例；类的封装、继承、多态
2. 类属性、实例属性。动态操作
3. 类高级特性：`__slots__`/`@property`
4. 自定义对象实现系统内置方法并可调用,形如`__**__()`方法实现
5. 枚举类型
6. 使用元类，动态创建类，改变类的行为。


#### 基础四 :four:

[python 基础四](https://blog.csdn.net/heroboyluck/article/details/102513311)

**文件目录`four`:**
文件包括`four.py`,定义一个名称校验类`four_form.py`,用于测试校验`four_test.py`

1. 错误处理、捕获；自定义错误类型`BaseException`；
2. 调试：日志打印、断点调试`pdb`；
3. 单元测试`unittest`
4. 文档测试：注释中可执行代码，运行与命令行模式，`doctest`


#### 基础五 :five:

:dog:

#### 基础六 :six:
[python 基础六](https://blog.csdn.net/heroboyluck/article/details/102691412)

文件目录`six` ，包括图形化界面`tkinter`,自定义图形`turtle`; TCP/IP通信

1. `tkinter`图形化界面展示，`Entry/Label/Button`
2. `turtle`自定义绘制图形 ;
3. `socket`通信，服务端、客户端实例；

#### 基础七 :seven:

[python 基础七](https://blog.csdn.net/heroboyluck/article/details/102762792)

文件目录 `seven`, 发送邮件`SMTP`协议；接受邮件`POP3`协议

1. 邮件发送：文本、图片、附件；
2. 身份认证：指定邮箱、`SMTP`服务、授权码
3. 邮件接收：邮件消息结构、`as_string()`输出信息。

:star2: :star2: :star2:
> 邮件消息具体还在努力。。。