# PokéFinder 中文版

本仓库为 PokéFinder 的中文翻译版，由 [xDHHzz](https://github.com/xDHHzz) 进行中文翻译与整理。

原项目：[Admiral-Fish/PokeFinder](https://github.com/Admiral-Fish/PokeFinder)

你可以加入 PokéFinder Discord 服务器讨论开发并参与贡献。

[![PokéFinder](https://discordapp.com/assets/07dca80a102d4149e9736d4b162cff6f.ico)](https://discord.gg/XmgQF9X)

PokéFinder 是一款面向第三至第八世代宝可梦正作游戏的跨平台 RNG 工具。目前支持第三/第四世代，以及第五/第八世代的部分内容。

# 下载

[最新官方版本](https://github.com/Admiral-Fish/PokeFinder/releases/latest)

[最新夜间构建](https://github.com/Admiral-Fish/PokeFinder/actions)

# 功能

第三世代
- 蛋
- GameCube
- ID
- 定点
- 野生

第四世代
- 蛋
- 配信
- ID
- 定点
- 野生

第五世代
- AR 搜寻器
- 蛋
- 配信
- 隐藏洞穴
- ID
- 定点
- 野生

第八世代
- 蛋
- 配信
- ID
- 巢穴
- 定点
- 地下大洞窟
- 野生

# 支持平台

Windows
- Windows 10
- Windows 11

macOS
- macOS Sonoma
- macOS Sequoia
- macOS Tahoe

Linux
- Ubuntu 22.04
- Ubuntu 24.04

Qt
- 6.10 或更新版本

# 安装

Windows
- 安装 [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- 从 [releases 页面](https://github.com/Admiral-Fish/PokeFinder/releases/latest) 下载 Windows zip 压缩包
- 从 zip 压缩包中解压 PokéFinder

macOS
- 从 [releases 页面](https://github.com/Admiral-Fish/PokeFinder/releases/latest) 下载 macOS zip 压缩包
- 从 zip 压缩包中解压 PokéFinder

Linux
- 安装 Qt 6
  - [Qt 官网](https://www.qt.io/download)
  - `sudo apt install qt6-base-dev`
- 从 [releases 页面](https://github.com/Admiral-Fish/PokeFinder/releases/latest) 下载 Linux zip 压缩包
- 从 zip 压缩包中解压 PokéFinder

# 构建

Windows
- 安装依赖
  - [Qt 6](https://www.qt.io/download)
  - [Build tools for Visual Studio](https://visualstudio.microsoft.com/downloads/)
  - [Python 3.14](https://www.python.org/downloads/)
- 构建
  - `git submodule update`
  - `mkdir build`
  - `cd build`
  - `cmake -G"NMake Makefiles" -DCMAKE_BUILD_TYPE=RELEASE ../`
  - `cmake --build .`
- 打包
  - `mk PokeFinder-windows`
  - `move release\PokeFinder.exe PokeFinder-windows\PokeFinder.exe`
  - `windeployqt --release --no-translations --no-angle --no-plugins --no-opengl-sw PokeFinder.exe`
  - `xcopy /I "QTPath"\plugins\platforms\qwindows.dll PokeFinder-windows\platforms\`
  - `xcopy /I "QTPath"\plugins\styles\qwindowsvistastyle.dll PokeFinder-windows\styles\`

macOS
- 安装依赖
  - Qt 6（可使用 [brew](https://formulae.brew.sh/formula/qt) 或 [Qt 官网](https://www.qt.io/download)）
  - [Python 3.14](https://www.python.org/downloads/)
- 构建
  - `git submodule update`
  - `mkdir build`
  - `cd build`
  - `PATH="PATH=$PATH:$HOME/Qt/6.10/macos/bin" cmake -G"Unix Makefiles" -DCMAKE_BUILD_TYPE=RELEASE ../`
    - 请根据实际 Qt 路径/版本调整
  - `cmake --build .`
- 打包
  - `macdeployqt PokeFinder.app -dmg -verbose=2`

Linux
- 安装依赖
  - Qt 6
    - [Qt 官网](https://www.qt.io/download)
    - `sudo apt install qt6-base-dev qt6-tools-dev qt6-tools-dev-tools qt6-l10n-tools`
  - [Python 3.14](https://www.python.org/downloads/)
  - `sudo apt install build-essential libgl1-mesa-dev`
- 构建
  - `git submodule update`
  - `mkdir build`
  - `cd build`
  - `cmake -G"Unix Makefiles" -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_PREFIX_PATH=$HOME/Qt/6.10/gcc_64 ../`
    - 请根据实际 Qt 路径/版本调整
  - `cmake --build .`

# 致谢（排名不分先后）

- Bill Young、Mike Suleski 和 Andrew Ringer，感谢他们开发 [RNG Reporter](https://github.com/Slashmolder/RNGReporter)
- chiizu，感谢其开发 [PPRNG](https://github.com/chiizu/PPRNG)
- wwwwwwzx，感谢其开发 [3DSRNG Tool](https://github.com/wwwwwwzx/3DSRNGTool)
- PokemonRNG 团队，感谢他们的各类贡献与研究：[zaksabeast](https://github.com/zaksabeast)、[EzPzstreamz](https://github.com/SteveCookTU)、[Shiny_Sylveon](https://github.com/ShinySylveon04)、[Vlad](https://github.com/RichardPaulAstley)、[Real96](https://github.com/Real96)
- 其他在帮助和研究方面作出贡献的人：[OmegaDonut](https://github.com/OmegaDonut)、[Bond697](https://github.com/Bond697)、[Kaphotics](https://github.com/kwsch)、[SciresM](https://github.com/SciresM)、Zari、amab、Marin、[Lean](https://github.com/Leanny) 等
- Sans，感谢其提供初始 GUI 设计
