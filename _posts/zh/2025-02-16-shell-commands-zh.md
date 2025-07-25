---
audio: false
generated: false
image: false
lang: zh
layout: post
title: macOS 命令行
translated: true
---

这里有200个常用的macOS shell命令，按类别分类以便更容易参考。这些命令对于导航文件系统、管理文件、系统监控等非常有用。

### 文件系统导航
- `ls` - 列出目录内容。
- `cd` - 更改当前目录。
- `pwd` - 打印当前工作目录。
- `tree` - 以树状显示目录（如果已安装）。

### 文件操作
- `cp` - 复制文件或目录。
- `mv` - 移动或重命名文件或目录。
- `rm` - 删除文件或目录。
- `touch` - 创建一个空文件或更新时间戳。
- `mkdir` - 创建一个新目录。
- `rmdir` - 删除一个空目录。
- `ln` - 创建硬链接和符号链接。
- `chmod` - 更改文件权限。
- `chown` - 更改文件所有者和组。
- `cat` - 连接并显示文件内容。
- `less` - 逐页查看文件内容。
- `more` - 逐页查看文件内容。
- `head` - 显示文件的前几行。
- `tail` - 显示文件的最后几行。
- `nano` - 编辑文本文件。
- `vi` - 编辑文本文件。
- `vim` - 编辑文本文件（`vi`的增强版）。
- `find` - 在目录层次结构中搜索文件。
- `locate` - 快速查找文件。
- `grep` - 使用模式搜索文本。
- `diff` - 逐行比较文件。
- `file` - 确定文件类型。
- `stat` - 显示文件或文件系统状态。
- `du` - 估算文件空间使用情况。
- `df` - 报告文件系统磁盘空间使用情况。
- `dd` - 转换并复制文件。
- `tar` - 在归档中存储、列出或提取文件。
- `gzip` - 压缩或解压缩文件。
- `gunzip` - 解压缩使用gzip压缩的文件。
- `zip` - 打包和压缩文件。
- `unzip` - 从ZIP归档中提取压缩文件。
- `rsync` - 远程文件和目录同步。
- `scp` - 安全地在主机之间复制文件。
- `curl` - 从或到服务器传输数据。
- `wget` - 从网络下载文件。

### 系统信息
- `uname` - 打印系统信息。
- `top` - 显示系统进程。
- `htop` - 交互式进程查看器（如果已安装）。
- `ps` - 报告当前进程的快照。
- `kill` - 向进程发送信号。
- `killall` - 按名称终止进程。
- `bg` - 在后台运行作业。
- `fg` - 在前台运行作业。
- `jobs` - 列出活动作业。
- `nice` - 以修改的调度优先级运行程序。
- `renice` - 更改正在运行的进程的优先级。
- `time` - 计时命令的执行。
- `uptime` - 显示系统运行时间。
- `who` - 显示登录的用户。
- `w` - 显示登录的用户及其正在做的事情。
- `whoami` - 打印当前用户名。
- `id` - 打印用户和组信息。
- `groups` - 打印用户所在的组。
- `passwd` - 更改用户密码。
- `sudo` - 以另一个用户的身份执行命令。
- `su` - 切换用户。
- `chroot` - 使用不同的根目录运行命令。
- `hostname` - 显示或设置系统的主机名。
- `ifconfig` - 配置网络接口。
- `ping` - 向网络主机发送ICMP ECHO_REQUEST。
- `traceroute` - 跟踪到网络主机的路径。
- `netstat` - 网络统计。
- `route` - 显示或操作IP路由表。
- `dig` - DNS查找实用程序。
- `nslookup` - 交互式查询Internet名称服务器。
- `host` - DNS查找实用程序。
- `ftp` - Internet文件传输程序。
- `ssh` - OpenSSH SSH客户端。
- `telnet` - TELNET协议的用户界面。
- `nc` - Netcat，任意TCP和UDP连接和监听。
- `iftop` - 显示接口的带宽使用情况（如果已安装）。
- `nmap` - 网络探索工具和安全/端口扫描器（如果已安装）。

### 磁盘管理
- `mount` - 挂载文件系统。
- `umount` - 卸载文件系统。
- `fdisk` - Linux的分区表操作工具。
- `mkfs` - 构建Linux文件系统。
- `fsck` - 检查和修复Linux文件系统。
- `df` - 报告文件系统磁盘空间使用情况。
- `du` - 估算文件空间使用情况。
- `sync` - 将缓存的写入同步到持久存储。
- `dd` - 转换并复制文件。
- `hdparm` - 获取/设置硬盘参数。
- `smartctl` - 控制和监控SMART启用的ATA/SCSI-3驱动器（如果已安装）。

### 包管理
- `brew` - Homebrew包管理器（如果已安装）。
- `port` - MacPorts包管理器（如果已安装）。
- `gem` - RubyGems包管理器。
- `pip` - Python包安装程序。
- `npm` - Node.js包管理器。
- `cpan` - Perl包管理器。

### 文本处理
- `awk` - 模式扫描和处理语言。
- `sed` - 流编辑器，用于过滤和转换文本。
- `sort` - 排序文本文件的行。
- `uniq` - 报告或省略重复行。
- `cut` - 从文件的每一行中删除部分。
- `paste` - 合并文件的行。
- `join` - 根据公共字段连接两个文件的行。
- `tr` - 翻译或删除字符。
- `iconv` - 将文本从一种编码转换为另一种编码。
- `strings` - 在文件中查找可打印的字符串。
- `wc` - 打印每个文件的换行符、单词和字节计数。
- `nl` - 编号文件的行。
- `od` - 以各种格式转储文件。
- `xxd` - 创建十六进制转储或执行反向操作。

### Shell脚本
- `echo` - 显示一行文本。
- `printf` - 格式化并打印数据。
- `test` - 评估表达式。
- `expr` - 评估表达式。
- `read` - 从标准输入读取一行。
- `export` - 设置环境变量。
- `unset` - 取消设置shell变量和函数的值和属性。
- `alias` - 为命令创建别名。
- `unalias` - 删除别名。
- `source` - 在当前shell中执行文件中的命令。
- `exec` - 执行命令。
- `trap` - 捕获信号和其他事件。
- `set` - 设置或取消设置shell选项和位置参数。
- `shift` - 移动位置参数。
- `getopts` - 解析位置参数。
- `type` - 描述命令。
- `which` - 定位命令。
- `whereis` - 定位命令的二进制文件、源文件和手册页文件。

### 开发工具
- `gcc` - GNU项目C和C++编译器。
- `make` - 目录导向的makefile处理器。
- `cmake` - 跨平台makefile生成器。
- `autoconf` - 生成configure脚本。
- `automake` - 生成Makefile.in文件。
- `ld` - GNU链接器。
- `ar` - 创建、修改和从归档中提取。
- `nm` - 列出对象文件中的符号。
- `objdump` - 显示对象文件的信息。
- `strip` - 丢弃对象文件中的符号。
- `ranlib` - 生成归档的索引。
- `gdb` - GNU调试器。
- `lldb` - LLVM调试器。
- `valgrind` - 用于构建动态分析工具的仪器框架（如果已安装）。
- `strace` - 跟踪系统调用和信号（如果已安装）。
- `ltrace` - 跟踪库调用（如果已安装）。
- `perf` - Linux的性能分析工具。
- `time` - 计时命令的执行。
- `xargs` - 从标准输入构建和执行命令行。
- `m4` - 宏处理器。
- `cpp` - C预处理器。
- `flex` - 快速词法分析器生成器。
- `bison` - Yacc兼容的解析器生成器。
- `bc` - 任意精度计算器语言。
- `dc` - 任意精度计算器。

### 版本控制
- `git` - 分布式版本控制系统。
- `svn` - Subversion版本控制系统。
- `hg` - Mercurial分布式版本控制系统。
- `cvs` - 并发版本系统。

### 杂项
- `man` - 格式化并显示在线手册页。
- `info` - 读取Info文档。
- `apropos` - 搜索手册页名称和描述。
- `whatis` - 显示一行手册页描述。
- `history` - 显示或操作历史记录列表。
- `yes` - 重复输出字符串，直到被杀死。
- `cal` - 显示日历。
- `date` - 显示或设置日期和时间。
- `sleep` - 延迟指定的时间。
- `watch` - 定期执行程序，显示输出全屏。
- `xargs` - 从标准输入构建和执行命令行。
- `seq` - 打印数字序列。
- `shuf` - 生成随机排列。
- `tee` - 从标准输入读取并写入标准输出和文件。
- `tput` - 初始化终端或查询terminfo数据库。
- `stty` - 更改和打印终端行设置。
- `clear` - 清除终端屏幕。
- `reset` - 将终端重置为合理状态。
- `script` - 创建终端会话的typescript。
- `wall` - 向所有用户发送消息。
- `write` - 向另一个用户发送消息。
- `mesg` - 控制对终端的写入访问。
- `talk` - 与另一个用户交谈。
- `ytalk` - 另一个talk程序（如果已安装）。
- `crontab` - 维护单个用户的crontab文件。
- `at` - 计划命令在稍后的某个时间执行一次。
- `batch` - 计划命令在批处理队列中执行。
- `nice` - 以修改的调度优先级运行程序。
- `renice` - 更改正在运行的进程的优先级。
- `time` - 计时命令的执行。
- `ulimit` - 设置或报告用户资源限制。
- `pr` - 将文本文件转换为打印。
- `lp` - 将文件发送到打印机。
- `lpr` - 打印文件。
- `lpq` - 显示打印机队列状态。
- `lprm` - 从打印机队列中删除作业。
- `enscript` - 将文本转换为PostScript、HTML或RTF，带有语法高亮（如果已安装）。
- `a2ps` - 任何到PostScript过滤器。
- `ps2pdf` - 将PostScript转换为PDF。
- `pdf2ps` - 将PDF转换为PostScript。
- `gs` - Ghostscript解释器。
- `convert` - 将图像格式转换（如果已安装）。
- `mogrify` - 调整、旋转和转换图像（如果已安装）。
- `exiftool` - 读取、写入和编辑文件的元信息（如果已安装）。
- `jpegoptim` - 优化JPEG文件（如果已安装）。
- `optipng` - 优化PNG文件（如果已安装）。

这些命令涵盖了广泛的功能，对于希望通过终端高效管理和与macOS系统交互的用户来说是必不可少的。