[app]
# 应用名称
title = Mouse Clicker

# 包名
package.name = mouseclicker

# 包域名
package.domain = com.mouseclicker

# 源码目录
source.dir = .

# 包含文件类型
source.include_exts = py,png,jpg,kv,atlas,json,txt

# 应用版本
version = 1.0.0

# 应用描述
requirements = python,kivy

# 应用入口文件
source.main = mouse_clicker_android.py

# 安卓特定设置
[app:android]

# 权限
android.permissions = SYSTEM_ALERT_WINDOW,VIBRATE,WAKE_LOCK

# 应用的API级别
android.api = 30

# 最小API级别
android.minapi = 21

# 安装到SD卡
android.presplash.filename = %(source.dir)s/presplash.png

# 图标
android.icon.filename = %(source.dir)s/icon.png

# 应用需要的主Activity类
android.activity_class = org.kivy.android.PythonActivity

[app:ios]

# iOS特定设置
ios.kivy_ios_dir = /path/to/kivy-ios
ios.ios_deploy_dir = /path/to/ios_deploy

[bdist]
# 打包通用设置

[buildozer]
# Buildozer配置
log_level = 2
warn_on_root = 1

# 安卓SDK和NDK路径
# android.sdk_path = /path/to/android-sdk
# android.ndk_path = /path/to/android-ndk
# android.ndk_version = 21.4.7075529