---
layout: default
title: "Horizon Summary: 2026-07-20 (ZH)"
date: 2026-07-20
lang: zh
---

> 从 53 条内容中筛选出 18 条重要资讯。

---

1. [SRE 用 1600 美元的 ESP32 替代 12 万美元保龄球评分系统](#item-1) ⭐️ 8.0/10
2. [ESP32 广告拦截器仅用 50KB 内存屏蔽 53.7 万个广告域名](#item-2) ⭐️ 7.5/10
3. [我国人形机器人整机产品超全球半数](#item-3) ⭐️ 7.3/10
4. [Meshy 完成近 4 亿美元 B 轮融资](#item-4) ⭐️ 7.3/10
5. [Claude Code 从 Zig 迁移到 Rust，现采用 Bun 运行时](#item-5) ⭐️ 7.0/10
6. [Minecraft Java 版在最新快照中从 SDL2 迁移至 SDL3](#item-6) ⭐️ 7.0/10
7. [阿里发布 Qwen 3.8：2.4 万亿参数开源权重大模型](#item-7) ⭐️ 7.0/10
8. [腾讯云 ADP 4.0 海外版发布，企业级智能体平台出海](#item-8) ⭐️ 6.3/10
9. [8 点 1 氪丨长鑫科技中签号出炉：共约 770.22 万个；西班牙 1-0 战胜阿根廷，夺得本届世界杯冠军；月之暗面有望最快 6 个月内赴港上市](#item-9) ⭐️ 6.3/10
10. [工信部：将加快出台人工智能+软件行动方案](#item-10) ⭐️ 6.3/10
11. [工信部：将印发算力标准体系建设指南，推动建立算力市场化定价等标准](#item-11) ⭐️ 6.3/10
12. [中国智能算力规模突破 2185 EFLOPS](#item-12) ⭐️ 6.3/10
13. [销售 2,500 台 MIDI 录音设备的经验：硬件其实没那么难](#item-13) ⭐️ 6.0/10
14. [AMD Medusa Point 十核 APU 刷新 Geekbench 跑分记录](#item-14) ⭐️ 5.5/10
15. [Zilog Z80 迎来 50 周年，开源替代品即将进入 DIP40 硅片 —— 这款标志性的 8 位 CPU 于 1976 年 7 月推出，并于 2024 年停产](#item-15) ⭐️ 5.5/10
16. [Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’](#item-16) ⭐️ 5.5/10
17. [俄罗斯无人机被发现使用螺丝固定的磁性指南针作为导航辅助——卫星通信中断时机载摄像头可下倾核查方位](#item-17) ⭐️ 5.5/10
18. [MSI 在 Computex 预览液冷 AMD EPYC Venice 双路服务器](#item-18) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [SRE 用 1600 美元的 ESP32 替代 12 万美元保龄球评分系统](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

一位 SRE 购买了一座废弃的 8 车道保龄球馆，自行开发了名为 OpenLaneLink 的系统，使用 ESP32 微控制器、ESPNow 网状网络、RS485 备用链路以及运行 Redis 的树莓派作为中间件，替代了价值六位数的 2008 年商用评分系统。 这是一个引人注目的真实案例，展示了廉价的现代嵌入式硬件和开源软件如何取代价格虚高且存在供应商锁定的传统工业系统，有望为小企业主节省巨额资本支出，同时赋予他们完全的数据所有权和定制自由。 该系统采用 ESP32 节点配合继电器、光耦和红外对射传感器，以星型拓扑网状网络通过 UART 连接至树莓派；每对球道总成本约 200 美元（升级版 400 美元），而供应商的替换零件每对高达 4000 美元，且整套球道更换只需不到 10 分钟——作者计划将整个技术栈开源。

hackernews · section33 · 7月19日 14:41

**背景**: 保龄球馆依赖自动置瓶器（通常是已有数十年历史的机械设备），并由电子评分系统控制，该系统通过摄像头检测球瓶、追踪球速、运行犯规检测、驱动头顶显示器并为计分屏制作动画。ESP32 是乐鑫科技推出的低成本 Wi-Fi/蓝牙微控制器，在物联网和嵌入式项目中广受欢迎。ESPNow 是乐鑫的一种无连接协议，允许 ESP32 芯片在无 Wi-Fi 路由器的情况下进行点对点通信，适用于简单的网状网络架构；而 RS485 是一种稳健的有线工业总线标准，常用作抗噪备用链路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>
<li><a href="https://www.espressif.com/en/products/socs/esp32">ESP32 Wi-Fi & Bluetooth SoC | Espressif Systems</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极且充满专业见解：另一位拥有基于 1970 年 Intel D8749H 评分系统的保龄球道业主证实了继电器控制模式；一位嵌入式改造从业者分享了改造老旧机床的类似经历；一位在保龄球机旁长大的评论者印证了其背后的机械现实；作者则概述了未来计划，包括 DMX 灯光控制、LED 追逐灯效动画以及自助 kiosk 支付。

**标签**: `#ESP32`, `#embedded-systems`, `#retrofit`, `#hardware-hacking`, `#Show-HN`

---

<a id="item-2"></a>
## [ESP32 广告拦截器仅用 50KB 内存屏蔽 53.7 万个广告域名](https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds) ⭐️ 7.5/10

一位硬件黑客为一款 5 美元的 ESP32 加密狗编写了固件，仅使用约 50KB 内存和 4MB 闪存，即可存储和查询包含 53.7 万个广告与追踪域名的屏蔽列表，并在约 10 毫秒内响应被屏蔽域名的 DNS 查询。 该项目证明全网络广告屏蔽并不需要树莓派这类昂贵的单板计算机，使得隐私保护和广告拦截可以在极其廉价、低功耗的嵌入式硬件上实现，适合 DIY 家庭网络和安全爱好者。 其核心技巧在于采用节省空间的高效哈希方案（很可能是布隆过滤器的变体），将域名成员数据压缩至可放入仅 4MB 闪存中，查询延迟约 10 毫秒；该方法以牺牲一定的精确性为代价换取极致的内存效率，整套硬件成本约为 5 美元。

rss · Tom's Hardware · 7月19日 10:00

**背景**: ESP32 是乐鑫科技（Espressif Systems）推出的低成本、内置 Wi-Fi 和蓝牙的微控制器系列，广泛用于物联网项目。传统的全网络广告拦截方案（如 Pi-hole）通常运行在支持 Linux 的开发板上，需要数十甚至数百兆字节内存。为了将包含 53.7 万条目的域名列表压缩到仅有约 50KB 内存的设备中，该项目几乎可以确定使用了布隆过滤器（Bloom filter）——一种由 Burton Howard Bloom 于 1970 年发明的概率型数据结构，通过多个哈希函数以极少的内存判断集合成员关系，代价是可能产生少量误报（错误屏蔽列表中不存在的域名）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.espressif.com/en/products/socs/esp32">ESP 32 Wi-Fi & Bluetooth SoC | Espressif Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bloom_filter">Bloom filter - Wikipedia</a></li>
<li><a href="https://www.digikey.com/es/maker/blogs/2024/a-guide-for-the-esp32-microcontroller-series">A Guide for the ESP 32 Microcontroller Series</a></li>

</ul>
</details>

**标签**: `#embedded-systems`, `#ESP32`, `#ad-blocking`, `#DNS`, `#hardware-hacking`

---

<a id="item-3"></a>
## [我国人形机器人整机产品超全球半数](https://36kr.com/newsflashes/3903383107110785?f=rss) ⭐️ 7.3/10

中国工业和信息化部报告称，我国生产了全球半数以上的人形机器人整机产品（400 多种型号）以及全球约 70%的四足机器人销量，彰显了中国机器人产业的快速发展。

rss · 36氪 · 7月20日 02:46

**标签**: `#humanoid-robots`, `#robotics`, `#china-tech`, `#industry-stats`, `#MIIT`

---

<a id="item-4"></a>
## [Meshy 完成近 4 亿美元 B 轮融资](https://36kr.com/newsflashes/3903365138270088?f=rss) ⭐️ 7.3/10

AI 3D 生成公司 Meshy 完成创纪录的 B 轮融资，融资约 4 亿美元，估值超 14 亿美元，资金将用于多模态模型研发和全球扩张。

rss · 36氪 · 7月20日 02:28

**标签**: `#AI`, `#3D generation`, `#funding`, `#multimodal models`, `#venture capital`

---

<a id="item-5"></a>
## [Claude Code 从 Zig 迁移到 Rust，现采用 Bun 运行时](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/) ⭐️ 7.0/10

Anthropic 将 Claude Code 的运行时从 Zig 重写为 Rust，新版本内置了 Bun v1.4.0——该版本领先于最新的公开版本（v1.3.14），表明 Anthropic 在收购 Bun 项目后正在发布一个预览分支。 这一决策凸显了生产级 AI 代理工具在系统级语言选型上的现实权衡，同时也引发了关于开源治理的担忧——Bun 被 Anthropic 收购后，其作为独立开源项目的未来走向令人关切。 Bun 本身也是用 Rust 编写的，并采用 Safari 的 JavaScriptCore 引擎，不同于使用 V8 的 Node.js 和 Deno。核心工程动机在于 Rust 的自动内存管理机制消除了团队在使用 Zig 时因手动追踪内存生命周期而遇到的整类 bug。

hackernews · tosh · 7月19日 10:03 · [社区讨论](https://news.ycombinator.com/item?id=48966569)

**背景**: Claude Code 是 Anthropic 推出的终端 AI 编程代理工具，可帮助开发者编辑代码、运行命令并管理 Git 工作流。Bun 是一个集 JavaScript 运行时、包管理器和测试运行器于一体的快速工具，旨在替代 Node.js，最初由 Jarred Sumner 创建。Zig 是一门类似 C 的底层系统语言，要求开发者手动管理并显式释放内存；而 Rust 通过编译期的所有权和借用检查器自动保证内存安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test ...</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：部分人支持切换到 Rust，认为这消除了 Zig 实现中手动内存管理带来的 bug；另一些人则严厉批评围绕 Bun 收购的沟通方式，担心开源 Bun 项目实际上正在消亡。一个反复出现的声音质疑：终端 UI（TUI）为何要基于 React/JavaScript 并通过 Bun 运行？怀疑者认为完全用原生语言重写会更便宜、更简单。

**标签**: `#claude-code`, `#rust`, `#bun`, `#anthropic`, `#engineering-decisions`

---

<a id="item-6"></a>
## [Minecraft Java 版在最新快照中从 SDL2 迁移至 SDL3](https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4) ⭐️ 7.0/10

Minecraft Java 版快照 26-3 snapshot 4 已通过更新的 LWJGL3 绑定将其底层多媒体层从 SDL2 迁移至 SDL3。发布说明承认存在已知问题，包括在 Windows 上（尤其是使用多显示器时）以及在 Wayland 上进入独占全屏模式时会导致游戏崩溃。 SDL3 带来了现代化的 API、改进的平台支持（包括原生 Wayland 处理）以及更好的性能特性，这些都将有助于 Minecraft 的长期可维护性和跨平台稳定性。由于 Minecraft 是全球使用最广泛的 Java 应用程序之一，此次迁移堪称 SDL3 和 LWJGL3 成熟度的一次重要实战验证。 促成此次迁移的 LWJGL3 绑定由来自 GTNH（GregTech: New Horizons）整合包团队的贡献者编写，继续延续了模组生态改进回馈至原版 Minecraft 的传统。社区指出独占全屏模式下的 Bug 可能会成为正式版发布的阻碍因素。

hackernews · ObviouslyFlamer · 7月19日 11:48 · [社区讨论](https://news.ycombinator.com/item?id=48967256)

**背景**: SDL（Simple DirectMedia Layer，简易直接媒体层）是一个跨平台 C 语言库，用于抽象对图形（OpenGL、Direct3D、Vulkan、Metal）、音频和输入硬件的访问；SDL3 于 2025 年 1 月发布 v3.2.0，是其最新主版本。LWJGL（Lightweight Java Game Library，轻量级 Java 游戏库）为 Java 提供对 OpenGL、Vulkan 和 SDL 等原生库的绑定，是 Minecraft Java 版与底层系统 API 交互的桥梁。此次迁移得益于 LWJGL3 对 SDL3 的官方支持，使 Java 程序能够使用 SDL3 现代化的功能集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer">Simple DirectMedia Layer - Wikipedia</a></li>
<li><a href="https://www.lwjgl.org/">LWJGL - Lightweight Java Game Library</a></li>
<li><a href="https://en.wikipedia.org/wiki/LWJGL">LWJGL - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对这一里程碑整体持积极态度，但对未解决的全屏崩溃问题表示担忧。评论者强调了模组社区与原版之间循环往复的贡献关系（LWJGL3 的 SDL3 绑定来自 GTNH 整合包团队成员），分享了 Ryan 'Icculus' Gordon 关于将 Doom 移植到 SDL3 的视频作为相关参考，并指出 Minecraft 正日益演变为通用游戏引擎，而不仅仅是一款游戏。

**标签**: `#minecraft`, `#sdl3`, `#game-development`, `#graphics`, `#lwjgl`

---

<a id="item-7"></a>
## [阿里发布 Qwen 3.8：2.4 万亿参数开源权重大模型](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) ⭐️ 7.0/10

阿里巴巴发布了 Qwen 3.8，这是一款拥有 2.4 万亿参数的开源权重大语言模型，似乎是对 Moonshot AI 近日发布 2.8 万亿参数 Kimi K3 的直接回应。此次公告本身仅包含一个指向 Qwen Cloud 定价页面的链接，完整的架构细节和基准测试结果尚未公布。 此次发布加剧了中国 AI 实验室之间在最大开源权重前沿模型方面的激烈竞争，阿里巴巴和 Moonshot AI 如今都提供能够与 OpenAI 和 Anthropic 等美国顶级系统相媲美的万亿参数级模型。这种规模的开源权重发布使前沿 AI 能力更加普及，惠及全球能够微调和自托管模型的研究人员、开发者和企业。 该公告内容明显薄弱——仅分享了一个定价链接——模型架构、基准测试结果和确切发布时间表均不明确。值得注意的是，开发者 Simon Willison 报告称由于其邮箱地址被标记而无法向阿里云付款，这凸显了国际用户在使用商业 API 时可能面临的支付和访问障碍。

hackernews · nh43215rgb · 7月19日 08:44 · [社区讨论](https://news.ycombinator.com/item?id=48966120)

**背景**: Qwen 是阿里巴巴的大语言模型系列，Qwen3 系列引入了混合'思考'和'非思考'模式，允许用户在深度推理输出和快速响应输出之间切换。'开源权重'（open weights）意味着训练好的模型参数被公开发布以供推理和微调，但这与完全开源不同——训练数据和代码通常不包含在内。Moonshot AI 于 2026 年 7 月发布的 Kimi K3 是一款拥有 2.8 万亿参数、原生多模态的模型，具有 100 万 token 的上下文窗口，而 Qwen 3.8 显然定位为同一万亿参数级别的直接竞争对手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html">China's Moonshot AI unveils Kimi K3 that rivals OpenAI, Anthropic China’s Moonshot AI releases Kimi K3, the largest open-source ... Kimi K3: Moonshot AI’s 2.8T Open-Weight Model — Release ... Moonshot AI Kimi K3 Release: Specs, Pricing, API & When to Switch China's Moonshot AI claims Kimi K3 can rival OpenAI and ... Kimi K3: Moonshot AI's Open-Source Flagship, Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models: Open Source vs Open Weights vs ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪活跃但褒贬不一。用户普遍认识到阿里巴巴和 Moonshot AI 之间的竞争态势，一位评论者指出'在这种大模型竞争中，我们都是赢家'。然而，质量方面的担忧依然存在——一位开发者报告称 Qwen 3.7 Pro 在软件工程任务上与 DeepSeek 相比'完全不可用'，原因是浪费时间且成本高昂。本地部署爱好者希望阿里巴巴发布较小的模型变体，而 Simon Willison 则指出了阿里云阻止他付费使用的问题。

**标签**: `#llm`, `#qwen`, `#alibaba`, `#open-weights`, `#ai-competition`

---

<a id="item-8"></a>
## [腾讯云 ADP 4.0 海外版发布，企业级智能体平台出海](https://36kr.com/p/3901396207584902?f=rss) ⭐️ 6.3/10

2026 年 7 月 18 日，在世界人工智能大会（WAIC）上，腾讯云正式发布了智能体开发平台 ADP 4.0 海外版，同步升级智能工作台、Claw 模式和 Skill 广场三大核心模块，新增 LINE、Telegram 等海外社交渠道接入、多语言自动响应，并深度集成 Google Workspace、Confluence、Jira 等海外主流 SaaS 应用。 此次发布是腾讯云将国内打磨成熟的企业级智能体能力向全球市场输出的关键一步，标志竞争从 Token 层上升到应用层。平台强调可信、可控、全链路可观测与审计，与个人级智能助手形成差异化，主要瞄准印尼等东南亚市场，腾讯云在当地已有私有化部署项目。 核心架构创新是 Agent 与 Workflow 双向互调：开放性任务由 Agent 处理，确定性流程由 Workflow 执行，以减少 Token 消耗。产品负责人吴运声透露，ADP 客户数较去年至少翻倍增长，主要得益于 Agent Loop 能力增强和企业教育成本降低；落地案例显示某医疗集团效率提升 50%、某运营商应用开发效率提升 70%以上。

rss · 36氪 · 7月20日 01:30

**背景**: ADP（Agent Development Platform，智能体开发平台）是面向企业的 AgentOps 平台，覆盖智能体的构建、分发和治理全生命周期。AgentOps 是近年兴起的新学科，专注于在生产环境中运行 AI 智能体，强调治理、可观测性、工具控制、人工监督和成本管理。文中提到的 Claw 模式是 ADP 的核心功能之一，支持智能体跨多渠道部署。吴运声还澄清了 WorkBuddy（腾讯的个人 AI 助手）与 ADP 的定位差异：WorkBuddy 类似员工个人智能助手，对管理者不可见；ADP 则是云端一体化方案，智能体使用情况对企业完全透明可控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/news/28683">Tencent Cloud ADP 4.0 Launch: Claw Mode Enables Agents to Be...</a></li>
<li><a href="https://eu.36kr.com/en/p/3846786158086665">Tencent 's Determination to Regain Ground in the Agent Field</a></li>
<li><a href="https://www.uipath.com/blog/ai/agent-ops-operationalizing-ai-agents-for-enterprise">AgentOps and operationalizing AI agents for the enterprise ...</a></li>

</ul>
</details>

**标签**: `#Tencent Cloud`, `#enterprise AI`, `#agent platform`, `#ADP`, `#WAIC 2026`

---

<a id="item-9"></a>
## [8 点 1 氪丨长鑫科技中签号出炉：共约 770.22 万个；西班牙 1-0 战胜阿根廷，夺得本届世界杯冠军；月之暗面有望最快 6 个月内赴港上市](https://36kr.com/p/3903220264404608?f=rss) ⭐️ 6.3/10

一档每日中国科技与商业新闻摘要，重点关注月之暗面可能赴港上市、长鑫科技 IPO 中签结果、世界杯决赛战况以及其他商业与经济资讯。

rss · 36氪 · 7月20日 00:05

**标签**: `#Moonshot AI`, `#IPO`, `#CXMT`, `#semiconductors`, `#China tech`

---

<a id="item-10"></a>
## [工信部：将加快出台人工智能+软件行动方案](https://36kr.com/newsflashes/3903399623542657?f=rss) ⭐️ 6.3/10

中国工业和信息化部宣布将加快出台"人工智能+软件"行动方案，推动智能软件开发、AI 驱动的软件产品与服务以及 AI 智能体软件生态建设。

rss · 36氪 · 7月20日 03:03

**标签**: `#China policy`, `#AI policy`, `#software development`, `#AI agents`, `#government announcement`

---

<a id="item-11"></a>
## [工信部：将印发算力标准体系建设指南，推动建立算力市场化定价等标准](https://36kr.com/newsflashes/3903384861771649?f=rss) ⭐️ 6.3/10

中国工业和信息化部宣布计划发布算力标准体系建设指南，推动建立算力市场化定价标准，并在 AI 需求激增的背景下优化算力基础设施布局。

rss · 36氪 · 7月20日 02:48

**标签**: `#China`, `#compute infrastructure`, `#AI policy`, `#regulation`, `#smart computing`

---

<a id="item-12"></a>
## [中国智能算力规模突破 2185 EFLOPS](https://36kr.com/newsflashes/3903375424522113?f=rss) ⭐️ 6.3/10

2025 年 7 月 20 日，工业和信息化部信息通信管理局局长谢存在国新办新闻发布会上宣布，截至 2025 年 6 月底，我国智能算力规模已达 2185 EFLOPS，全国算力设施整体上架率达到 71.4%。过去两年围绕国家算力枢纽节点已建成超 70 条算力大通道，枢纽节点间网络性能提升 10%。 这是迄今为止官方发布的最清晰的中国 AI 算力规模衡量指标之一，凸显了中国在人工智能基础设施投资方面的全球领先地位。71.4%的上架率表明已部署的大部分硬件已投入实际使用，说明算力供给与需求匹配良好，而非过度建设闲置。 1 EFLOPS 等于每秒 10^18 次（即百亿亿次）浮点运算，2185 EFLOPS 属于超大规模（exascale）级别。71.4%的"上架率"指的是已完成上架调试并对外提供服务的服务器占已安装服务器的比例。超 70 条算力大通道是连接"东数西算"工程八个已批复国家枢纽节点的全国骨干网络。

rss · 36氪 · 7月20日 02:38

**背景**: EFLOPS（每秒百亿亿次浮点运算）是衡量超级计算性能的标准单位，1 EFLOPS 等于每秒 10^18 次浮点运算。"智能算力"特指面向 AI 工作负载（如模型训练与推理）优化的计算资源，与通用算力有所区别。"东数西算"工程于 2022 年 2 月正式启动，规划在京津冀、长三角、粤港澳大湾区、成渝、内蒙古、贵州、甘肃、宁夏等 8 地建设国家算力枢纽节点，并配套 10 个国家数据中心集群，旨在将东部密集的数据处理需求引导至土地更廉、气候更凉爽、能源更充裕的西部地区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Floating_point_operations_per_second">Floating point operations per second - Wikipedia</a></li>
<li><a href="https://www.gov.cn/zhengce/zhengceku/202401/content_6924596.htm">关于深入实施“东数西算”工程加快构建全国一体化算力网的实施意见_国务...</a></li>
<li><a href="https://www.iii.tsinghua.edu.cn/info/1121/2978.htm">“东数西算”工程正式全面启动，一图读懂 “东数西算”工程核心要点</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#China tech`, `#compute capacity`, `#government policy`, `#data centers`

---

<a id="item-13"></a>
## [销售 2,500 台 MIDI 录音设备的经验：硬件其实没那么难](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard) ⭐️ 6.0/10

一位硬件创业者分享了销售 2,500 台 MIDI 录音设备（JamCorders）的经验，认为硬件创业比人们普遍认为的更容易上手，但社区讨论中也有声音对这种过于简化的观点提出了反驳。

hackernews · chipweinberger · 7月19日 10:34 · [社区讨论](https://news.ycombinator.com/item?id=48966713)

**标签**: `#hardware`, `#entrepreneurship`, `#startup`, `#maker`, `#product-development`

---

<a id="item-14"></a>
## [AMD Medusa Point 十核 APU 刷新 Geekbench 跑分记录](https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test) ⭐️ 5.5/10

AMD 即将推出的十核 Medusa Point 移动 APU 的最新 Geekbench 跑分泄露，显示该芯片创下迄今最高分数，据称在单核测试中超越了所有其他 x86 移动处理器。这是该特定 SKU 第三次出现在跑分数据库中，每次泄露的分数都优于此前泄露的 Gorgon Point 和 Strix Point 产品。 如果这些泄露的成绩能在最终量产芯片中得到验证，Medusa Point 将成为 AMD 近年来在移动端最显著的性能飞跃，可能改变与英特尔 x86 移动产品线的竞争格局。对于笔记本电脑消费者和 OEM 厂商来说，这意味着轻薄本和主流笔记本的高单核性能将在下一代产品周期中实现大幅提升。 泄露的型号是 Ryzen AI 500（Medusa Point）家族中的一款十核 SKU，基于 Zen 6 架构，采用 FP10 插槽，提供 28W 和 45W 两种 TDP 配置。据称 Medusa Point 采用混合核心设计，集成显卡规模有所缩减，其前代为 Gorgon Point（Ryzen AI 400），而 Gorgon Point 本身在很大程度上只是 Strix Point 和 Krackan Point 芯片的 refresh 版本。

rss · Tom's Hardware · 7月19日 14:35

**背景**: APU（加速处理器单元）是 AMD 对将 CPU 和集成显卡集成在同一芯片上的处理器的称呼，广泛用于笔记本电脑和预算型台式机。Medusa Point 是 AMD 下一代移动 APU 产品线（Ryzen AI 500 系列）的代号，基于 Zen 6 架构，是 Strix Point 和 Gorgon Point 家族的继任者。Geekbench 是一款广泛使用的跨平台基准测试工具，用于衡量单核和多核 CPU 性能，但其针对未发布硬件的跑分并非官方数据，测试结果受驱动、散热和功耗配置等因素影响，可能与零售产品存在差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test">AMD's next-gen 10-core 'Medusa Point' APU shows up on ...</a></li>
<li><a href="https://www.techpowerup.com/343682/amd-zen-6-based-medusa-point-apu-comes-in-28-w-and-45-w-tdps">AMD Zen 6-Based "Medusa Point" APU Comes in 28 W and 45 W ...</a></li>
<li><a href="https://videocardz.com/newz/amd-next-gen-medusa-point-zen6-apu-with-high-and-low-tdp-settings-spotted-in-shipping-manifest">AMD next-gen "Medusa Point" Zen6 APU with High and Low TDP ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#CPUs`, `#benchmarks`, `#mobile-computing`, `#leaks`

---

<a id="item-15"></a>
## [Zilog Z80 迎来 50 周年，开源替代品即将进入 DIP40 硅片 —— 这款标志性的 8 位 CPU 于 1976 年 7 月推出，并于 2024 年停产](https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon) ⭐️ 5.5/10

Zilog Z80 庆祝其 50 周年纪念，同时一款开源的即插即用替代品即将进入 DIP40 硅片。

rss · Tom's Hardware · 7月19日 14:12

**标签**: `#retro-computing`, `#open-source-hardware`, `#Z80`, `#computing-history`, `#CPU`

---

<a id="item-16"></a>
## [Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’](https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation) ⭐️ 5.5/10

SK Group chairman acknowledges abnormally high RAM prices and considers building a US semiconductor plant to increase supply and stabilize the memory market.

rss · Tom's Hardware · 7月19日 13:55

**标签**: `#semiconductors`, `#RAM`, `#supply-chain`, `#hardware`, `#industry-news`

---

<a id="item-17"></a>
## [俄罗斯无人机被发现使用螺丝固定的磁性指南针作为导航辅助——卫星通信中断时机载摄像头可下倾核查方位](https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost) ⭐️ 5.5/10

俄罗斯无人机被观察到使用廉价的磁性指南针作为备用导航辅助设备，当卫星通信中断时，摄像头会下倾以核对方位。

rss · Tom's Hardware · 7月19日 12:05

**标签**: `#drones`, `#navigation`, `#electronic-warfare`, `#GPS-denied-environment`, `#military-technology`

---

<a id="item-18"></a>
## [MSI 在 Computex 预览液冷 AMD EPYC Venice 双路服务器](https://www.servethehome.com/msi-slyly-shows-off-an-upcoming-dlc-amd-epyc-venice-platform-with-cd182-s6091-x2-servers-and-racks/) ⭐️ 5.5/10

在 Computex 上，微星低调展出了即将推出的 CD182-S6091-X2（DLC），这是一款采用 1OU2N 规格、配备直接液冷散热的双路服务器节点，基于 AMD 下一代 EPYC Venice 平台打造。 这是服务器 OEM 厂商首批公开展示 Venice 平台的案例之一，表明 AMD 基于 Zen 6 架构的服务器芯片已接近可用于超大规模和企业部署的阶段。双路密度与直接液冷的组合，预示着面向 AI 和云端工作负载的高核心数服务器设计的演进方向。 1OU2N 规格将两个计算节点集成在单个 1U 机箱中，最大化机架密度；DLC（直接液冷）设计表明该平台专为应对 Venice 核心数增加所带来的更高热设计功耗而打造。展会期间未披露核心数、内存通道数或功耗等详细规格。

rss · ServeTheHome · 7月19日 18:00

**背景**: AMD EPYC Venice 是基于 Zen 6 架构的 AMD 下一代服务器处理器代号，采用台积电 N2（2nm 级别）工艺制造，据报道核心数最高可达 256 颗。它将使用全新的 SP7 和 SP8 插槽平台，支持最多 16 通道内存和 128 条 PCIe 6.0 通道。直接液冷（DLC）正迅速成为高密度数据中心服务器的标准方案，因为传统风冷已无法有效应对现代数百瓦 CPU 和加速器产生的热量。1OU2N 规格指在一个 1OU（开放 U）机箱中容纳两个独立服务器节点，这种设计在超大规模环境中颇受欢迎，可最大化每机架单元的计算密度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/newsroom/press-releases/2026-5-20-amd-announces-production-ramp-of-next-generation-a.html">AMD Announces Production Ramp of Next-Generation AMD EPYC ...</a></li>
<li><a href="https://wccftech.com/amd-sp7-sp8-platforms-epyc-venice-verano-cpus-12800-mtps-16-channel-memory-128-pcie-6-0-lanes/">AMD SP7 & SP8 Platforms For Next-Gen EPYC “Venice” & “Verano ...</a></li>
<li><a href="https://www.computacenter.com/en-us/who-we-are/blogs/direct-liquid-cooling--the-new-gold-standard-for-data-centers">Direct Liquid Cooling: The new gold standard for data centers</a></li>

</ul>
</details>

**标签**: `#AMD`, `#EPYC`, `#servers`, `#data-center`, `#hardware`

---