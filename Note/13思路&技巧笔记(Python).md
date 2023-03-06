# 13思路&技巧笔记(Python)

[toc]



---

## Python内置堆、栈、队列及其使用

*   [相关文章](https://www.jianshu.com/p/9b94651534c3)



---

-   ```python
    import collections
    a = '12321314'
    a = [4, 324, 576, 5]
    temp = collections.Counter(a)
    ```

    -   collections中的Counter函数能将对象统计后返回词频字典

-   ```python
    s = 'absdsagervd'
    res = sorted(s, key = lambda x:ord(x))
    ```

    -   内置函数指定较简单的比较器

-   python内置进制转换

    -   `int(C, <目标进制>)`
    -   可以用指定进制抓换n，是字符
    -   如果要用数值转进制则要使用函数`bin(), otc(), hex()`
    -   python数值进制表示前缀`ob1011, 0o1571, 0x1a12b`

-   ```python
    path = path.lstrip('/') # 删除指定前导字符
    ```

-   
