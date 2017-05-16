#汇编

计算机当中的数字是以补码方式进行存储

## 位运算


### & 与运算

``` js
0001 0000
&
1111 1111
----------
0001 0000
```


### | 或运算

```js
  0001 0000
  1111 1111
| ----------
  1111 1111
```

### ^ 异或运算 (两个不相同时则为真)

```js
  0001 0000
  1111 1111
^ ----------
  1110 1111
```


### ~ 按位取反

```js
  0001 0000
~ ----------
  1110 1111
```

                
按位操作

向左位移
高位丢弃，低位补0

example

```js
0011 0001 << 2  ->  1100 0100
1111 1111 << 2  ->  1111 1100
```

向右位移
高位补0或补1，低位丢弃
汇编当中要自行决定

C语言当中则取决于该数是否有符号

```c 
unsigned int a = 10
// 10 -> 0000 1010
a >> 2 // -> 0000 0010

1000 0001 >> 2
```




计算机的减法
计算机当中的运算只有位运算，而没有传统意义上的加减乘除运算，其都是有位运算实现的


减法
减法可以看成是加法如 4-5 = 4+(-5)
则

4 原码 0000 0100, 补码 0000 0100

5 原码 1000 0101, 补码 1111 1010 (符号位不变，其他取反)

进行异或操作，计算非进位加法

``` js
  0000 0100
^ 1111 1011
-----------------
  1111 1111      // 0xFF
  
```

进行与操作，判断是否有进位, 非0则存在进位

```js

  0000 0100
& 1111 1011 
-----------------
  0000 0000
  
```

对补码结果求原码

手动运算

```js

1111 1111 - 0000 0001 = 1111 1110  // 得反码
1111 1110             = 1000 0001 （符号为不变，其他位取反）// 得原码

1111 1111 << 1 -> 1111 1110

``` 

#### 按位操作求补码
``` js
  1101 1111 // 原码
    
  1101 1111
  1000 0000
& ----------
  1000 0000 // 得符号位

  1101 1111 << 1   =>   1011 1110
  ~1011 1110       =>   0100 0001
  0100 0001 >> 1   =>   0010 0000
  
  0010 0000
  1000 0000 // 或符号位
| ----------
  1010 0000 // 反码
  
```

> 已知反码用按位运算求补码原理相同
  
  
#### 原码求补码的按位实现？
```js
原码 1101 1101 // 0xDD

  1101 1101
  1000 0000
& ------------
  1000 0000 // 得符号位

  1101 1101 << 1   =>   1011 1010 // 取非符号位
  ~1011 1010       =>   0100 0101 // 对非符号位取反
  0100 0101 >> 1   =>   0010 0010 // 得非符号位结果

  0010 0010 
  1000 0000
| -----------
  1010 0010 // 得反码

  1010 0010
  0000 0001
^ -----------
  1010 0011 // 加1

  1010 0010
  0000 0001
& -----------
  0000 0000 // 无进位
  
```

则补码为 `1010 0011`

按位运算时都是使用补码进行运算
