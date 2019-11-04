### 解决matplot在画图模式下的中文乱码问题

-----



##### 1.下载simhei字体文件
##### 2.打开python运行环境，执行以下代码

```	  python
import matplotlib
matplotlib.matplotlib_fname() #将会获得matplotlib包所在文件夹
```

然后进入C:\Anaconda64\Lib\site-packages\matplotlib\mpl-data该文件夹下就能看到matplotlibrc配置文件。（这里的路径是你的安装目录，视个人情况而定）

2.1）打开该配置文件，找到下面这两行：

    #font.serif          : DejaVu Serif, Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
    #font.sans-serif     : DejaVu Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

然后将开头的两个注释符删掉。并在前方加入你的字体名称，例如我加入的是SimHei

```markdown
#font.serif          : <font color=red>SimHei</font>, DejaVu Serif, Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
#font.sans-serif     : <font color=red>SimHei</font>, DejaVu Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
```

#axes.unicode_minus  : True    # use unicode for the minus symbol

该处是为了能够使坐标轴上的负号正常显示，同样将开头的注释符#去掉，然后将True改为False：

axes.unicode_minus  : False    # use unicode for the minus symbol

2.2）找中文字体放到matplotlib字体库中。
在Windows下载文件夹下：复制该字体（例如此处我复制的为：楷体 常规（文件名为SimHei.ttf。注意要看下字体的属性，须复制后缀名为ttf的）），然后粘贴到C:\Anaconda64\Lib\site-packages\matplotlib\mpl-data\fonts\ttf（这里依然是安装目录）文件夹。

注明：这一步的作用其实就是将matplotlib中一个默认的字体替换为我们复制过来的中文字体，将这个中文字体命名改为matplotlib中有的字体名。

2.3） 找到.matplotlib/cache里面的两个缓存字体文件

删除fontList.json，重启
