<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/xiaoyu2018/Amadeus">
    <img src="https://raw.githubusercontent.com/xiaoyu2018/Best-README-Template/master/images/1.png" width="260" height="260">
  </a>

  <h3 align="center"><font size="6">Amadeus</font></h3>

  <p align="center">
    One qqbot based on <a href="https://github.com/nonebot/nonebot2"> nonebot2 </a> and <a href="https://github.com/Mrs4s/go-cqhttp" >go-cqhttp</a>！
    <br />
    <br />
  </p>
</div>


<!-- 修改url -->
<div align="center">
  <a href="https://github.com/xiaoyu2018/Amadeus/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/xiaoyu2018/Amadeus.svg?style=for-the-badge">
  </a>  
  <a href="https://github.com/xiaoyu2018/Amadeus/stargazers">
    <img src="https://img.shields.io/github/stars/xiaoyu2018/Amadeus.svg?style=for-the-badge">
  </a>  
  <a href="https://github.com/xiaoyu2018/Amadeus/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/xiaoyu2018/Amadeus.svg?style=for-the-badge">
  </a>  
</div>
<br />

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Catalogue</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Amadeus是一个基于异步机器人框架 **nonebot2** 和OneBot-v11协议的golang实现   **go-cqhttp** 编写的自用qq聊天机器人。  
项目目前仍在积极建设中...


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
0. 在安装本项目之前，强烈建议你创建一个新的pyhton虚拟环境，并且请确保你的 Python 版本 >= 3.7.3，此外如果你之前安装过nonebot1，请在安装 NoneBot v2 之前卸载 NoneBot v1。
1. 在新创建的python环境中安装<a href="./requirements.txt" >requestment</a>中提供的全部依赖
    ```python
    pip install -r requirements.txt
    ```
    完成这一步之后，你便已经安装好了nonebot2框架、驱动器（FastAPI）、适配器（OneBot V11）以及现有插件所需的其他所有依赖。
2. 修改 .env.dev.bak 文件名为 .env.dev ，在.env.dev中更改配置信息并记录PORT
3. 在<a href="https://github.com/Mrs4s/go-cqhttp/releases/tag/v1.0.0-rc1" >这里</a>下载go-cqhttp，并参照<a href="https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B" >文档</a>使用go-cqhttp进行反向代理，于配置文件 config.yml 反向ws设置中`universal: ws://127.0.0.1:PORT/onebot/v11/ws`（PORT与 .env.dev 中PORT保持一致）
4. 运行go-cqhttp
5. 在Amadeus目录下运行bot
    ```python
    nb run
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
+ Amadeus目前实现了以下几个插件：  
  1. 爬取百度热搜榜前三十
  2. 聊天调教
  3. 字母缩写含义查询
  4. 计算器
  5. 每日提醒
  6. 有道翻译

+ 以下功能需要其他插件支持，请自行安装：
  1. 定时任务 <a href="https://github.com/nonebot/plugin-apscheduler"> nonebot_plugin_apscheduler </a>
  2. 在线运行代码 <a href="https://github.com/yzyyz1387/nonebot_plugin_code"> nonebot_plugin_code </a>
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
+ <a href="https://github.com/nonebot/nonebot2"> NoneBotv2 </a>：NoneBot2 是一个现代、跨平台、可扩展的 Python 聊天机器人框架，它基于 Python 的类型注解和异步特性，能够为你的需求实现提供便捷灵活的支持。
+ <a href="https://github.com/nonebot/nonebot2"> go-cqhttp </a>：cqhttp的golang实现，轻量、原生跨平台，go-cqhttp 兼容 OneBot-v11 绝大多数内容，并在其基础上做了一些扩展。
+ <a href="https://lab.magiconch.com/nbnhhsh/"> 能不能好好说话？ </a>：拼音首字母缩写释义工具
+ <a href="https://top.baidu.com/board?tab=realtime"> 百度热搜 </a>：百度热搜榜
+ <a href="https://www.youdao.com/"> 有道 </a>：有道翻译

<p align="right">(<a href="#top">back to top</a>)</p>



