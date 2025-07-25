---
audio: false
generated: false
image: true
lang: zh
layout: post
title: Mesh 路由器
translated: true
---

## TP-Link AX3000 - TL-XDR 3050

2023年，我开始使用网状路由器。我购买了一套TP-Link AX3000系统，包含两个网状路由器：一个主路由和一个卫星路由。当时花费了大约484元人民币，而现在在京东上仅售395元。

最初，我在大房子里使用这套系统，后来将其搬到了父母家。

## ZTE AC1200

2025年春节期间，有几天家人住在大房子里，再次遭遇了WiFi网络质量不佳的问题。为了解决这个问题，我购买了另一款网状路由器——ZTE AC1200，价格大约108元人民币。

沃尔玛上类似的产品包括TP-Link WiFi网状路由器、Eero双频网状路由器和NetGear Nighthawk AX3000。这些产品大多价格在50美元到200美元之间。

对于ZTE AC1200网状路由器，我可以只购买一个，并使用桥接模式，让它接收WiFi信号后再发射自己的WiFi信号。效果非常好。原本路由器的域名地址是192.168.5.1。启用桥接模式后，这个IP地址就无法访问了。相反，192.168.1.1会重定向到家庭网络中的主路由器。此时，你可以通过访问http://zte.home进入路由器的控制中心。

如果你能访问主路由器，就能看到连接的设备及其IP地址。然后，你可以尝试访问每个设备，以确定哪个是子路由器。在我的情况下，它是192.168.1.23，这是ZTE AC1200网状路由器的地址。

对于在家中移动的手机，最好使用2.4 GHz频段，因为它更稳定。对于通常在卧室或书房使用的笔记本电脑或台式电脑，最好使用5 GHz频段，因为它速度更快。

使用几天后，我发现它的性能稍差一些。速度或信号比TL-XDR 3050差。

{: .centered }
![](assets/images/cable-tester/zte.jpg){: .responsive }
*来源：京东*{: .caption }

{: .centered }
![](assets/images/cable-tester/netgear.jpg){: .responsive }
*来源：沃尔玛*{: .caption }

## 路由器的12V电源

可以使用USB升压线通过移动电源为路由器供电。

然而，在某些情况下，移动电源的升压线可能无法正确设置路由器。路由器可能会不断重启。

{: .centered }
![](assets/images/cable-tester/12v.jpg){: .responsive }
*来源：京东*{: .caption }

## 帮助子路由器找到主路由器的两种方法

有时，当信号较弱时，子路由器不容易找到主路由器。

如果我们不得不将子路由器放置在远离主路由器的地方，我想知道是否先在附近位置连接它，然后再将其移远，会比直接在远处尝试连接更快。

在附近保持连接可以让它们相互通信。我发现这种方法更有效。