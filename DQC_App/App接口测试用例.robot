*** Settings ***
Resource                数据库操作.txt
Resource                登录相关.txt
Resource                配置相关.txt
Resource                客户相关.txt
Resource                订单相关.txt
Resource                产品相关.txt

*** Test Cases ***
用户自定义变量
          #环境
          Set Global Variable          ${host}          192.168.8.170
          Set Global Variable          ${port}          8775
          Set Global Variable          ${auth}          \          #调试用鉴权码
          Set Global Variable          ${orderid}          \          #调试用订单编号
          Set Global Variable          ${phone}          18781972711
          #手机参数配置
          Set Global Variable          ${channel}          IOS
          Set Global Variable          ${appVersion}          1.01          #app版本
          Set Global Variable          ${imei}          666666          #手机唯一识别码
          Set Global Variable          ${model}          E80
          Set Global Variable          ${systemVersion}          8.0          #系统版本
          #数据库配置
          Set Global Variable          ${db_host}          192.168.8.170
          Set Global Variable          ${db_port}          3306
          Set Global Variable          ${username}          root
          Set Global Variable          ${password}          123456

用户登录
          #用户登录
          发送登录短信验证码          ${phone}
          数据库查询指定手机验证码          earth_house_dev_third          ${phone}
          登录App          ${phone}

修改绑定手机号
          #修改绑定手机号
          数据库查询指定手机验证码          earth_house_dev_third          ${phone}
          修改手机号          ${phone}          您未发送短信验证码或者短信验证码已过期

提交意见建议—>查询意见建议
          #添加/查询建议
          添加客户意见&建议          提个锤子建议
          根据登录客户获取意见&建议分页数据

修改客户资料
          #客户相关
          获取客户信息详情          #姓名          昵称          个性签名          生日          性别：0女 1男
          登录客户修改资料          肖战          肖战战          你看个锤捶子          1995-04-03 00:00:00          1

新增预订人—>修改预订人
          #新增常用预订人信息
          Comment          新增常用预订人信息          张涵          18781972711          513030199303221719
          获取当前登录客户的常用预订人列表
          #修改常用预订人信息
          修改常用预订人信息          ${bookpeoid}          张涵          18781972711          513030199303221719

解绑微信
          #解绑微信
          数据库查询指定手机号用户customerId          earth_house_dev_customer          ${phone}
          解绑微信          ${customerid }

查询配置相关
          #配置相关
          根据客户登录状态获取app配置
          根据key值获取相应配置          ${keyy}
          根据渠道获取当前最新app版本

查询产品相关
          #产品相关
          获取指定酒店的酒店信息          558226357476610048
          获取首页产品分页列表
          获取产品详情          557965286039629824
          查询指定产品评论列表分页数据          557965286039629824
          查询评论详情          1266194643251425282
          #收藏
          收藏产品          557965286039629824
          取消收藏产品          557965286039629824
          查询用户产品收藏分页列表
          判定用户是否收藏指定产品          557965286039629824
          #酒店相关
          查询指定酒店的所有房间类型          558226357476610048
          查询指定酒店房间列表          558226357476610048
          查询指定酒店指定日期内的可用房间          558226357476610048          2020-09-26          2020-09-27
          #房间相关
          查询房间详情          594128879029620736
          查询指定房间的特定日期价格          594128879029620736          2020-09-26          2020-09-27

查询订单相关
          #订单相关
          获取订单分页列表          3
          查询客户未支付订单
          Comment          获取订单详情          ${orderid}
          Comment          猜你想去          ${orderid}
          Comment          获取订单房间列表          ${orderid}
          Comment          获取订单付款列表          ${orderid}
          Comment          获取订单消费列表          ${orderid}

创建订单—>预订取消
          #创建订单          酒店id          产品id          房间id          预定渠道          入住时间          离店时间
          创建订单          558226357476610048          557965286039629824          608746640812040192          0          2020-06-24          2020-06-25
          ...          xxy          18781972711          513436200009249409          王一博          18781972714          2020-06-24
          ...          2          500          0
          #取消订单
          判断订单有无责任          ${orderid}
          取消订单          ${orderid}          ${dutyFlag}          就想取消

创建订单—>支付取消
          #创建订单          酒店id          产品id          房间id          预定渠道          入住时间          离店时间
          创建订单          558226357476610048          557965286039629824          608746640812040192          0          2020-06-24          2020-06-25
          ...          xxy          18781972711          513436200009249409          王一博          18781972714          2020-06-24
          ...          2          500          0
          #支付订单
          数据库执行操作          earth_house_dev_hotel_system          UPDATE `order` SET stauts = 1 WHERE id = '${orderid}'
          #取消订单
          判断订单有无责任          ${orderid}
          取消订单          ${orderid}          ${dutyFlag}          就想取消

创建订单—>完成订单—>评论/投诉—>删除订单
          #创建订单          酒店id          产品id          房间id          预定渠道          入住时间          离店时间
          创建订单          558226357476610048          557965286039629824          608747422682931200          0          2020-06-24          2020-06-25
          ...          xxy          18781972711          513436200009249409          王一博          18781972714          2020-06-24
          ...          2          500          0
          #完成订单
          数据库执行操作          earth_house_dev_hotel_system          UPDATE `order` SET stauts = 4 WHERE id = '${orderid}'
          #评论订单          风景评分          服务评分          周边评分          住宿评分
          评论订单          ${orderid}          4          3          5          2          不安逸
          查询订单评论详情          ${orderid}
          #投诉订单
          订单投诉          ${orderid}          不安逸
          #删除订单
          删除订单          ${orderid}

退出登录
          退出登录App
