# Mouse Clicker Android APK 自动生成

本项目使用 **GitHub Actions** 自动构建鼠标点击器安卓应用，无需本地配置即可生成APK文件。

## 🚀 快速开始

### 方法一：使用我的预构建项目（最简单）

1. **访问 [GitHub仓库模板](https://github.com/yourusername/mouseclicker-android)** (需要替换为实际仓库地址)
2. **点击 "Use this template"** 创建你自己的仓库
3. **推送代码到你的仓库**
4. **等待Actions自动构建完成**
5. **下载生成的APK文件**

### 方法二：fork现有分支

1. **Fork这个项目到你的GitHub账户**
2. **在Actions标签页中，启用工作流程**
3. **手动触发构建或推送更改**
4. **下载已生成的APK**

## 📱 应用功能

- ✅ **自定义坐标点击**
- ✅ **设置点击间隔**
- ✅ **设置点击次数** 
- ✅ **开始/停止控制**
- ✅ **状态显示**
- ✅ **实时反馈**

## 🔧 GitHub Actions 工作流程说明

### 触发方式：
- **自动触发**：推送到 main/master 分支时
- **手动触发**：在Actions页面点击"Run workflow"
- **PR触发**：创建Pull Request时

### 构建环境：
```
- Ubuntu 最新版本
- Python 3.10
- Android SDK + NDK
- Buildozer
- 8GB Swap空间
```

### 构建输出：
- **APK文件**：bin/MouseClicker.apk
- **构建日志**：详细构建过程
- **构建物**：可直接下载的APK文件

## 📋 准备构建

### 必要文件结构：
```
mouse-clicker-android/
├── .github/
│   └── workflows/
│       └── build-android.yml       ← 构建工作流
├── mouse_clicker_android.py        ← 主程序代码
├── buildozer.spec                  ← 构建配置（可选）
├── README.md                       ← 此文档
└── requirements.txt                ← Python依赖
```

### 更新应用信息：

1. **修改应用标题**：
   ```python
   # mouse_clicker_android.py 第24行
   title = '我的点击器'
   ```

2. **修改包名**（在buildozer.spec中）：
   ```ini
   package.name = myclicker
   package.domain = com.myapp
   ```

3. **修改版本号**：
   ```ini
   version = 1.0.1
   ```

## 🎯 使用步骤

### 步骤1：获取APK文件

1. 在GitHub仓库页面点击 **Actions** 标签
2. 选择最新的构建工作流运行
3. 等待构建完成（通常需要15-30分钟）
4. 在 **Artifacts** 部分下载 APK 文件

### 步骤2：安装到安卓手机

1. **传输APK文件到手机**
   - 通过USB数据线
   - 通过蓝牙
   - 通过微信/QQ等应用

2. **安装APK文件**
   ```
   1. 在手机文件管理器中找到APK文件
   2. 点击安装
   3. 开启"允许安装未知来源应用"权限（如果需要）
   4. 完成安装
   ```

### 步骤3：运行应用

1. **启动应用**：在应用列表中找到Mouse Clicker
2. **授权权限**：
   - 允许浮窗权限（必需）
   - 允许振动权限（可选）
3. **开始使用**：
   - 输入目标坐标(X,Y)
   - 设置点击间隔
   - 设置点击次数
   - 点击"开始点击"

## ⚙️ 高级配置

### 自定义构建参数

在 `buildozer.spec` 中你可以修改：

```ini
[app]
# 应用信息
title = 新的应用名称
package.name = customname
package.domain = com.customdomain
version = 2.0.0

# 权限配置
[app:android]
android.permissions = 
    SYSTEM_ALERT_WINDOW,  # 必需：浮窗权限
    VIBRATE,             # 可选：振动反馈
    WAKE_LOCK,           # 可选：保持唤醒
    
# 构建配置
requirements = 
    python,kivy
    # 可以添加其他依赖
    # requests, pillow等
```

### 添加图标

将图标文件 `icon.png` 放在根目录，Buildozer 会自动使用。
- 推荐尺寸：512x512 像素
- 格式：PNG

## 🛠️ 故障排除

### 常见构建问题

#### 问题1：内存不足 (buildozer)
```
解决方法：自动配置中已包含8GB swap空间
```

#### 问题2：下载失败
```
解决方法：尝试重新运行工作流
```

#### 问题3：依赖安装失败
```
解决方法：检查buildozer.spec中的requirements设置
```

### 常见安装问题

#### 问题1：无法安装APK
```
解决方案：
1. 确保开启"安装未知应用"权限
2. 检查APK文件完整性
3. 确认Android版本兼容（>= Android 5.0）
```

#### 问题2：应用权限不足
```
解决方案：
1. 手动授予浮窗权限
2. 在应用管理中找到应用
3. 启用"显示浮窗"权限
```

## 🔄 自动化建议

### 定期构建：
你可以添加定时构建触发器：

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'  # 每周日午夜构建
```

### 发布标签构建：

```yaml
on:
  release:
    types: [created]  # 创建新发布时构建
```

## 📞 获取帮助

### 构建状态检查：
1. 访问 GitHub Actions 页面
2. 查看最新运行的 Jobs
3. 检查输出日志查找错误信息

### 功能需求：
如果你想添加新功能，可以修改 `mouse_clicker_android.py`：
- 添加新功能
- 修改用户界面
- 增加配置选项

### 技术问题：
- 确保所有文件都在根目录
- 检查Python代码语法
- 验证buildozer.spec配置

## 📝 许可证

MIT License - 你可以自由使用此项目

## 🌟 为结果点赞

如果这个自动化工具对你有帮助：
1. **给项目加星** ⭐
2. **分享给需要的朋友** 📤
3. **反馈使用体验** 💬

---

**享受你的自动点击器！** 🚀