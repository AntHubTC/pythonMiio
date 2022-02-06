# 学习使用python-miio控制小米设备

https://blog.csdn.net/linzhiji/article/details/118194526
https://python-miio.readthedocs.io/en/latest/index.html
https://cool-y.github.io/2018/12/15/miio-control/

## mihome binary protocol
协议https://github.com/OpenMiHome/mihome-binary-protocol/blob/master/doc/PROTOCOL.md

## 获取小米设备token
### 方式一： db文件方式获取token

此种方式需要root的手机或者使用android模拟器。
1. 安装米家app并登录账号
2. 添加设备到米家
3. 进入/data/data/com.xiaomi.smarthome/databases/
4. 拷贝miio2.db，下载到电脑+
5. 往网站（http://miio2.yinhh.com/ 或 https://homekit.loli.ren/docs/show/12），上传miio2.db，点击提交，即可获得token。

https://inloop.github.io/sqlite-viewer/

### 方式二： 给小米设备发送hellobyte消息

1. 在米家app中找到设备的ip地址；
2. 使用discover/hello_discovery.py

这个是网上的一种方法，但是我的小爱音响Play和小爱音响Pro都获取真正的token，返回的是“token: b'ffffffffffffffffffffffffffffffff'”，不知道最新的产品是不是小米封住了这个口子。

原因： 2017-02-23 更新：小米更新了设备固件，现在只有未初始化的设备会显示其令牌。

### 方式三： 使用python-miio提供的Discovery功能

使用discover/miio_discovery.py

没有发现我的音响。

### 方式四（推荐）： 使用小米账号，通过api方式获取米家中的所有设备信息

使用discover/token_extractor.py

输入用户名，密码，服务区域，就可以获取到的信息就包含设备token。

感谢：https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor 提供的方案


Yeelight 智能物联网平台

https://open-console.yeelight.com/open-platform-docs.html

## python-miio 命令

如果您已经拥有设备和设备类型的令牌，则可以直接开始使用miiocli工具。miiocli是从命令行执行命令的主要方式。

### help信息
~~~
miiocli --help

Usage: miiocli [OPTIONS] COMMAND [ARGS]...

Options:
  -d, --debug
  -o, --output [default|json|json_pretty]
  --version                       Show the version and exit.
  --help                          Show this message and exit.

Commands:
  airconditionermiot
  airconditioningcompanion
  airconditioningcompanionmcn02
  airconditioningcompanionv3
  airdehumidifier
  airdogx3
  airdogx5
  airdogx7sm
  airfresh
  airfresha1
  airfresht2017
  airfreshva4
  airhumidifier
  airhumidifierca1
  airhumidifiercb1
  airhumidifiercb2
  airhumidifierjsq
  airhumidifiermiot
  airhumidifiermjjsq
  airpurifier
  airpurifiermb4
  airpurifiermiot
  airqualitymonitor
  airqualitymonitorcgdn1
  alarmclock
  aqaracamera
  basicairpurifiermiot
  ceil
  chuangmicamera
  chuangmiir
  chuangmiplug
  cooker
  curtainmiot
  device
  discover                       Discover devices using both handshake...
  dreamevacuummiot
  fan
  fan1c
  fanleshow
  fanmiot
  fanp10
  fanp11
  fanp5
  fanp9
  fansa1
  fanv2
  fanza1
  fanza3
  fanza4
  fanza5
  g1vacuum
  gateway
  heater
  heatermiot
  huizuo
  huizuolampfan
  huizuolampheater
  huizuolampscene
  miotdevice
  petwaterdispenser
  philipsbulb
  philipseyecare
  philipsmoonlight
  philipsrwread
  philipswhitebulb
  plug
  plugv1
  plugv3
  powerstrip
  pwznrelay
  roborockvacuum
  roidmivacuummiot
  scisharecoffee
  toiletlid
  vacuum
  viomivacuum
  walkingpad
  waterpurifier
  waterpurifieryunmi
  wifirepeater
  wifispeaker
  yeelight
  yeelightdualcontrolmodule
~~~
如果需要了解进一步信息，可以使用
~~~
   miiocli 命令 --help
~~~


### 获取设备信息

您可以使用info命令从任何 miIO/MIoT 设备获取一些信息，包括其设备型号：

~~~
miiocli device --ip 192.168.43.184 --token 4d47743774574c6830706136746f5841 info
~~~
返回
~~~
Model: xiaomi.wifispeaker.lx06
Hardware version: Linux
Firmware version: 1.80.2
~~~

### API使用

所有功能都可以通过miio模块访问
~~~
from miio import Vacuum

vac = Vacuum("<ip address>", "<token>")
vac.start()
~~~
每个单独的设备类型都继承自miio.Device （如果是 MIoT 设备，则是miio.MiotDevice），它提供了一个通用 API。

每个命令调用将通过查询设备自动检测（并缓存）某些操作所需的设备模型。您可以通过手动指定模型来避免这种情况：

~~~
from miio import Vacuum

vac = Vacuum("<ip address>", "<token>", model="roborock.vacuum.s5")
~~~

[Miio API文档](https://python-miio.readthedocs.io/en/latest/api/miio.html)

### 支持的设备
* 小米米扫地机器人 V1、S4、S4 MAX、S5、S5 MAX、S6 Pure、M1S、S7
* 小米米家空调伴侣
* 小米智能空调A（xiaomi.aircondition.mc1、mc2、mc4、mc5）
* 小米空气净化器 2、3H、3C、Pro、Pro H、4 Pro（zhimi.airpurifier.m2、mb3、mb4、v7、vb2、va2）
* 小米空气（净化器）狗 X3、X5、X7SM（airdog.airpurifier.x3、airdog.airpurifier.x5、airdog.airpurifier.x7sm）
* 小米米空气加湿器
* 小米 Aqara 相机
* 小米Aqara网关（基本实现、报警、灯）
* 小米米家360 1080p
* 小米米家 STYJ02YM (Viomi)
* 小米米家 1C STYTJ01ZHM（梦）
* 小米米家（米家）G1扫地机器人MJSTG1
* 小米 Roidmi Eve
* 小米米智能WiFi插座
* 小米创米插头V1（1个插座，1个USB口）
* 小米创米插头V3（1个插座，2个USB接口）
* 小米智能电源板 V1 和 V2（WiFi，6 端口）
* 小米飞利浦护眼智能灯 2
* 小米飞利浦 RW 读取 (philips.light.rwread)
* 小米飞利浦 LED 吸顶灯
* 小米飞利浦 LED 球灯 (philips.light.bulb)
* 小米飞利浦 LED 球灯白色 (philips.light.hbulb)
* 小米飞利浦智睿智能LED灯泡E14蜡烛灯
* 小米飞利浦智睿卧室智能灯
* 华谊辉作灯具
* 小米万能红外遥控器（创米IR）
* 小米智能落地风扇V2、V3、SA1、ZA1、ZA3、ZA4、ZA5 1C、P5、P9、P10、P11
* 小米 Rosou SS4 呼吸机 (leshow.fan.ss4)
* 小米空气加湿器V1、CA1、CA4、CB1、MJJSQ、JSQ、JSQ1、JSQ001
* 小米米净水器（基本支持：开关机）
* 小米米净水器D1、C1（三重设置）
* 小米PM2.5空气质量监测仪V1、B1、S1
* 小米智能WiFi音箱
* 小米米 WiFi 中继器 2
* 小米米智能电饭煲
* 小米智米新风系统VA2（zhimi.airfresh.va2）、VA4（zhimi.airfresh.va4）、A1（dmaker.airfresh.a1）、T2017（dmaker.airfresh.t2017）
* Yeelight 灯（基本支持，我们推荐使用[python-yeelight](https://yeelight.readthedocs.io/en/latest/) ）
* 小米米空气除湿机
* 小米 Tinymu 智能马桶盖
* 小米16继电器模块
* 小米小爱智能闹钟
* 智米电暖器智能版（ZA1版）
* 小米米智能空间加热器
* 小米有品窗帘控制器（Wi-Fi）（lumi.curtain.hagl05）
* Xiaomi 小米米智能空间加热器 S (zhimi.heater.mc2)
* Xiaomi 小米米智能空间加热器 1S (zhimi.heater.za2)
* Yeelight 双控模块 (yeelink.switch.sw1)
* Scishare 咖啡机 (scishare.coffee.s1102)
* 清平空气监测器精简版（cgllc.airm.cgdn1）
* 小米Walkingpad A1 (ksmb.walkingpad.v3)
* 小米智能宠物饮水机 (mmgg.pet_waterer.s1, s4)
* 小米米智能加湿器 S (jsqs, jsq5)
