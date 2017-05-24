hesong-ipsc-busnetcli
#####################
IPSC专用的消息总线客户端的Python包装。

它用于向Python开发者提供SmartBus的客户端功能。

features
********

* 直接封装SmartBus的C语言实现客户端
* 采用Python标准库的ctypes进行C语言动态/共享库的封装。所以安装时不需要进行编译，理论上同时支持多种Python（如pypy,ironpython,jython）运行时（只要目标Python运行时支持ctypes）
* 完整的SmartBus客户端功能包装。其功能基本上与C语言实现客户端一对一。

.. attention::

    在安装好 Python 程序包之后，还需要下载目标平台的 ``ipsc-bus-client`` 动态/共享库，并将DLL或者SO文件复制到系统搜索路径。
