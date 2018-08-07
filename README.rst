hesong-ipsc-busnetcli
#####################
IPSC专用的消息总线客户端的Python包装。

它用于向 Python_ 开发者提供SmartBus的客户端功能。

Features
********

* 直接封装 `IPSC Data Bus` 的 `C` 语言客户端库 ipsc-bus-client_
* 采用 Python_ 标准库的 `ctypes` 进行 `C` 语言动态/共享库的封装。所以安装时不需要进行编译，理论上同时支持多种Python（如 `pypy`, `ironpython`, `jython`）运行时（只要该 Python_ 实现的标准库支持 `ctypes`）
* 完整的客户端功能包装,其功能基本上与 `C` 语言实现的客户端一对一。

.. warning::
    ipsc-bus-client_ 目前只提供了 ``Linux-x86_64`` 支持。

Install
*******

* 通过 pip_ 安装

  使用 pip_ 工具从 PyPI_ 安装

  .. code:: sh

    pip install --user hesong-ipsc-busnetcli

* 从源代码安装

  .. code:: sh

    git clone https://bitbucket.org/hesong-opensource/ipsc-bus-client-python.git
    cd ipsc-bus-client-python
    python setup.py install

.. _Python: http://www.python.org/
.. _PyPI: http://pypi.python.org/
.. _pip: http://pip.pypa.io/
.. _ipsc-bus-client: http://bitbucket.org/hesong-opensource/ipsc-bus-client
