# Chuan

## USER
-用户表设计
       - username   用户名（唯一）
       - password   密码
       - email      邮箱
       - phone      手机
       - icon       头像
       - is_active  是否激活
       - is_delete  是否删除
 
 ## Merchant      
-商家表设计
       -username    用户名（唯一）
       -password    密码
       -phone       手机号码
       -email       邮箱
       -icon        头像
       -id          身份证
       -id_front_photo      身份证照片正面
       -id_back_photo       身份证照片背面
       -is_active   是否激活
       -is_delete   是否删除
       
       
## Project
-项目表
        -p_title        项目标题
        -p_introText    项目简介
        -p_classify     项目分类
        -p_introImg     简介图片
        -p_detail       详细图片
        -p_follow       关注数
        -p_target       目标金额
        -p_already      已筹金额
       
       
-密码要求
    -不能包括空格
    -长度为8-16个字符
    -必须包含字母、数字、符号中至少2种
    
    
    
    
-版本迭代
    -注册密码要求