# hesong-ipsc-busnetcli

IPSC专用的消息总线客户端的 Python 包装。

它用于向 Python 开发者提供SmartBus的客户端功能。

## 说明

这个项目可用于个人学习：

1. 如何编写一个使用 ctypes 调用原生代码的 Python Library
1. 如何使用 setuptools 构建 Python Package 项目

版权和许可信息详见 [LICENSE](LICENSE.txt) 文件

## Features

- 直接封装 `IPSC Data Bus` 的 `C` 语言客户端库 [ipsc-bus-client][]
- 采用 Python 标准库的 `ctypes` 进行 `C` 语言动态/共享库的封装。所以安装时不需要进行编译，理论上同时支持多种Python（如 `pypy`, `ironpython`, `jython`）运行时（只要该 Python_ 实现的标准库支持 `ctypes`）
- 完整的客户端功能包装,其功能基本上与 `C` 语言实现的客户端一对一。

> **Note:**
>
> [ipsc-bus-client][] 目前只提供了 `Linux-x86_64` 支持。

## Install

- 通过 [pip][] 安装

  ```sh
  pip install hesong-ipsc-busnetcli
  ```

- 从源代码安装

  ```sh
  git clone https://bitbucket.org/hesong-opensource/ipsc-bus-client-python.git
  cd ipsc-bus-client-python
  python setup.py install
  ```

[pip]: http://pip.pypa.io/
[ipsc-bus-client]: http://bitbucket.org/hesong-opensource/ipsc-bus-client
