---
layout: default
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> 从 34 条内容中筛选出 10 条重要资讯。

---

1. [Open-source AnyPS5 dumps emulation to run PlayStation 5 console games natively on PC](#item-1) ⭐️ 8.5/10
2. [Nvidia’s RTX Mega Geometry 2.0 streams ray-tracing geometry into VRAM on demand](#item-2) ⭐️ 8.5/10
3. [新型攻击降低破解教科书 RSA 所需的算力](#item-3) ⭐️ 8.5/10
4. [DeepSeek 发布 DSec 弹性计算系统以支持 AI 沙箱执行](#item-4) ⭐️ 8.0/10
5. [27 年前的《GTA 2》通过 RTX 重光照实现现代化改造](#item-5) ⭐️ 7.5/10
6. [Reladraw 引入支持 AI 代理和手动节点定位的文本图表语言](#item-6) ⭐️ 7.0/10
7. [Drawgent 让编码代理能够在实时 Excalidraw 画布上交互](#item-7) ⭐️ 6.0/10
8. [英特尔 PresentMon 2.6.0 降低 CPU 开销并添加游戏叠加层](#item-8) ⭐️ 5.5/10
9. [Sandisk Optimus GX Pro 850P 2TB SSD review: A PS5 SSD you recognize at a price you don’t](#item-9) ⭐️ 5.5/10
10. [PNY 拒保因电源线导致熔毁的 RTX 5090](#item-10) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Open-source AnyPS5 dumps emulation to run PlayStation 5 console games natively on PC](https://www.tomshardware.com/video-games/playstation/open-source-anyps5-dumps-emulation-to-run-playstation-5-console-games-natively-on-pc-amd-zen-2-architecture-enables-proton-like-binary-translation-for-windows-and-linux) ⭐️ 8.5/10

An open-source project called AnyPS5 is developing a compatibility layer that uses AMD Zen 2 architecture to natively translate PlayStation 5 executables for execution on Windows and Linux, moving beyond traditional hardware emulation methods.

rss · Tom's Hardware · 9月26日 13:59

**标签**: `#Emulation`, `#PlayStation 5`, `#Binary Translation`, `#AMD Zen 2`, `#Open Source`

---

<a id="item-2"></a>
## [Nvidia’s RTX Mega Geometry 2.0 streams ray-tracing geometry into VRAM on demand](https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-mega-geometry-2-0-streams-ray-tracing-geometry-into-vram-on-demand-nanite-inspired-design-drops-detail-instead-of-dropping-out) ⭐️ 8.5/10

Nvidia's RTX Mega Geometry 2.0 SDK enables on-demand streaming of ray-tracing geometry into VRAM, utilizing a detail-adjustment strategy similar to Unreal Engine's Nanite to handle large scenes efficiently.

rss · Tom's Hardware · 9月26日 12:30

**标签**: `#Nvidia`, `#Ray Tracing`, `#Graphics Programming`, `#Hardware`, `#Real-time Rendering`

---

<a id="item-3"></a>
## [新型攻击降低破解教科书 RSA 所需的算力](https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels) ⭐️ 8.5/10

研究人员发现了一种新的密码学攻击方法，使破解教科书 RSA 所需的计算能力大幅降低。 这一发现意义重大，因为它证明破解 RSA 加密密钥的可能性在计算层面已降至国家行为者可及的范围内。 该攻击方法在短期内尚不具备立即大规模利用的可行性，但可能会成为未来相关改进的基础。

rss · Tom's Hardware · 9月26日 12:00

**背景**: 教科书 RSA 是一种未采用标准安全填充方案的变体，由于安全性极低，在实际应用中几乎不被推荐使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels">Novel attack slashes computing power needed to crack textbook RSA cryptography — attacks within state-actor reach, could target Apple and Cloudflare privacy services | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#Cryptography`, `#RSA`, `#Cybersecurity`, `#Computer Science`, `#Security Research`

---

<a id="item-4"></a>
## [DeepSeek 发布 DSec 弹性计算系统以支持 AI 沙箱执行](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek 发布了一篇技术论文，介绍了名为 DSec 的新型弹性计算系统，旨在为 AI 开发环境处理大规模并发工作负载扩展。该系统设计用于在分布式基础设施上执行多达 380,000 个并发沙箱。 这一基础设施突破显著增强了 AI 智能体及代码执行流水线的可扩展性，使开发者能够高效运行大规模并行模拟或评估。它凸显了现代 AI 研究和部署生态系统中专用弹性计算资源日益增长的重要性。 该系统运行在基于 AMD EPYC 处理器的 160 台服务器节点上，以实现其高并发容量。该论文由 131 位研究员共同署名，表明基础设施开发背后有庞大的内部团队投入。

hackernews · shenli3514 · 9月26日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=49859112)

**背景**: 弹性计算是指可以根据需求动态扩展资源的 infrastructure，对于管理与训练和部署大型 AI 模型相关的可变工作负载至关重要。在 AI 开发的语境中，“沙箱”是隔离的环境，代码、智能体任务或模拟可以在其中安全地执行，而不会影响底层系统或其他用户。

**社区讨论**: 社区成员注意到异常高数量的作者（131 人）可能是一种资产保护策略，用于模糊具体的个人贡献。一些用户将 DSec 的架构与 Google 的开源分布式机器学习框架 Ax 进行了比较，而其他用户则询问其与智能体专用基底的联系。

**标签**: `#DeepSeek`, `#Elastic Compute`, `#Scalability`, `#Infrastructure`, `#AI`

---

<a id="item-5"></a>
## [27 年前的《GTA 2》通过 RTX 重光照实现现代化改造](https://www.tomshardware.com/video-games/pc-gaming/27-year-old-gta-2-gets-full-path-tracing-and-60-fps-frame-generation-via-rtx-remix-custom-direct3d-9-wrapper-modernizes-classic-with-custom-direct3d-9-bridge-unlocks-dynamic-lighting) ⭐️ 7.5/10

一位模组制作者利用 RTX Remix 框架，成功为《侠盗猎车手 2》添加了全路径追踪、动态光照和 60 帧图像生成技术。 这证明了 NVIDIA 的 RTX Remix 框架能够将传统软件与现代渲染技术相结合，让数十年的经典游戏也能体验最高质量的画质。 该模组依赖于定制的 Direct3D 9 桥接接口来解锁动态光照并实现路径追踪，特别需要 RTX Remix 工具包以及 NVIDIA RTX GPU 硬件支持。

rss · Tom's Hardware · 9月26日 15:10

**背景**: 《侠盗猎车手 2》于 1999 年发布，是最早采用 3D 图形的系列作品之一。NVIDIA RTX Remix 是一个开源平台，旨在让模组制作者将 RTX 路径追踪、DLSS 和 Reflex 技术注入旧游戏中。使用帧生成技术可以让现代 GPU 合成额外的帧，即使在性能要求很高的复古游戏上也能实现更高且更流畅的帧率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/geforce/rtx-remix/">RTX Remix | The Ultimate Modding Platform | NVIDIA</a></li>
<li><a href="https://www.nvidia.com/en-us/geforce/news/dlss4-multi-frame-generation-ai-innovations/">NVIDIA DLSS 4 Introduces Multi Frame Generation ...</a></li>

</ul>
</details>

**标签**: `#Graphics`, `#Path Tracing`, `#RTX`, `#Gaming`, `#Emulation`

---

<a id="item-6"></a>
## [Reladraw 引入支持 AI 代理和手动节点定位的文本图表语言](https://github.com/reladraw/reladraw) ⭐️ 7.0/10

Reladraw 是一种新的图表语言，允许用户使用相对坐标显式定义节点位置，同时保留类似 Mermaid 的文本定义方式。它专为人类和 AI 代理的高效操作而设计，弥补了自动布局引擎与手动编辑器之间的空白。 在 AI 辅助编程时代，开发者心智模型与代理理解之间的视觉对齐是维持复杂系统架构的关键瓶颈。Reladraw 提供了一个简化的文本接口，使 AI 代理无需传统 GUI 编辑器的开销，即可快速生成并迭代具有精确布局控制的图表。 该工具具备相对定位系统，用户发现其实用性足以替代更复杂的绝对坐标设置。早期社区反馈指出曲线边缘渲染可能不一致，该项目目前包含一种用于与 Claude 或其他代理集成的技能安装方法。

hackernews · jpwalsh234 · 9月26日 17:10 · [社区讨论](https://news.ycombinator.com/item?id=49858513)

**背景**: 图表绘制对于记录软件架构和沟通至关重要，Mermaid 和 Graphviz 因其基于文本的语法而广受欢迎。然而，这些工具完全依赖算法的自动布局，对于复杂或非标准图表往往导致混乱且难以阅读的结构。相反，像 Draw.io 这样的手动工具提供了完全的控制权，但对于 AI 代理来说，以编程方式操作它们效率极低，限制了其在现代自动化工作流中的使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.apportunity.xyz/mermaid-diagrams/mermaid-syntax">Mermaid Diagram Syntax | Apportunity Documentation Hub</a></li>
<li><a href="https://graphviz.org/">Graphviz</a></li>
<li><a href="https://mermaid.js.org/intro/syntax-reference.html">Diagram Syntax | Mermaid</a></li>

</ul>
</details>

**社区讨论**: 社区情绪高度积极，许多用户强调该工具解决了人类开发者与 AI 编码代理之间的关键对齐瓶颈。具体反馈赞扬了相对定位模型，并建议将拓扑定义与布局关注点解耦，以更好地支持 C4 模型。一位用户报告了一个关于曲线箭头渲染的小 bug。

**标签**: `#developer-tools`, `#diagrams`, `#ai-agents`, `#visualization`, `#text-based`

---

<a id="item-7"></a>
## [Drawgent 让编码代理能够在实时 Excalidraw 画布上交互](https://tangled.org/yanndegat.tngl.sh/drawgent) ⭐️ 6.0/10

一篇新帖子介绍了 Drawgent，一个在实时 Excalidraw 画布上运行的编码代理，允许 AI 以视觉方式创建和修改图表。 该工具探索了视觉界面在 AI 代理中的可行性，并将其与基于文本的替代品（如 Mermaid）进行了对比。 用户讨论指出，虽然 Excalidraw 拥有官方 MCP 服务器，但模型处理复杂的 JSON 数据和边界框可能比较困难，因此基于文本或 HTML 的方法有时更有效。

hackernews · parasitid · 9月26日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=49857729)

**背景**: Excalidraw 是一款流行的在线白板应用，支持通过其 API 和模型上下文协议 (MCP) 进行编程控制。MCP 是一种标准，允许 AI 代理与外部工具和数据源交互，从而能够执行如画图等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/yctimlin/mcp_excalidraw">GitHub - yctimlin/mcp_excalidraw: MCP server and Claude Code ...</a></li>
<li><a href="https://deepwiki.com/excalidraw/excalidraw-mcp">excalidraw/excalidraw-mcp | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了不同的体验，指出有些人发现 Excalidraw 的 JSON 接口对代理来说具有挑战性，因此他们更倾向于使用 Mermaid 或基于 HTML 的方法。其他人则强调了视觉图表的认知益处，并分享了类似的白板代理开源项目。

**标签**: `#AI Agents`, `#Excalidraw`, `#MCP`, `#Visual Programming`, `#Developer Tools`

---

<a id="item-8"></a>
## [英特尔 PresentMon 2.6.0 降低 CPU 开销并添加游戏叠加层](https://www.techpowerup.com/353118/intel-presentmon-2-6-0-update-slashes-cpu-usage-adds-game-experience-overlay) ⭐️ 5.5/10

英特尔发布了 PresentMon 2.6.0，通过优化 ETW 刷新和后台任务时序，将该工具自身的 CPU 开销降低了最高 78%。该更新还引入了一个名为“游戏体验”的新叠加层预设，优先显示感知流畅度指标而非原始帧率数据。 通过大幅降低自身造成的性能损耗，PresentMon 2.6.0 确保了帧时间测量的准确性，因为监控工具本身对结果产生干扰的可能性更小。新的叠加层为关注视觉流畅度而非仅平均帧率的游戏玩家提供了更直观的性能视图。 CPU 开销的降低是通过使用对 Windows 事件跟踪（ETW）刷新较不激进的时序以及调整诊断日志进程实现的。此外，该更新支持按指标的多设备选择，允许来自多个 GPU 的遥测数据显示在同一个叠加层中，而不可用的指标现在会以变暗并附带说明的形式显示，而非直接消失。

rss · TechPowerUp News · 9月26日 15:29

**背景**: PresentMon 是由英特尔开发的一款免费开源工具，用于捕获详细的帧时间统计数据，包括在 DirectX、OpenGL 和 Vulkan 等图形 API 下的 CPU、GPU 和显示延迟。它依赖于 Windows 的“Windows 事件跟踪”（ETW）基础设施，以低开销记录内核级事件。监控工具的高 CPU 使用率可能会形成反馈回路，即测量性能的行为本身会削弱被测的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://presentmon.com/">PresentMon - Analyze GPU & CPU Performance</a></li>
<li><a href="https://github.com/gametechdev/presentmon">GitHub - GameTechDev/PresentMon: Capture and analyze the high-level performance characteristics of graphics applications on Windows. · GitHub</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing">About Event Tracing - Win32 apps | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Game Development`, `#Performance Monitoring`, `#PC Hardware`, `#Optimization`

---

<a id="item-9"></a>
## [Sandisk Optimus GX Pro 850P 2TB SSD review: A PS5 SSD you recognize at a price you don’t](https://www.tomshardware.com/pc-components/ssds/sandisk-optimus-gx-pro-850p-2tb-ssd-review) ⭐️ 5.5/10

The Sandisk Optimus GX Pro 850P is identified as a rebranded WD Black SN850P, offering mature performance suitable for PS5 upgrades at a premium price point.

rss · Tom's Hardware · 9月26日 13:00

**标签**: `#SSD`, `#Hardware Review`, `#PS5`, `#Storage`, `#Consumer Tech`

---

<a id="item-10"></a>
## [PNY 拒保因电源线导致熔毁的 RTX 5090](https://www.tomshardware.com/pc-components/gpus/pny-allegedly-refuses-to-cover-melted-rtx-5090-powered-by-native-power-supply-cable-company-closes-users-ticket-when-questioned-on-policy) ⭐️ 5.5/10

PNY 据称拒绝为一块因 12V-2x6 电源线熔毁而损坏的 RTX 5090 显卡提供保修。该厂商通过引用其官方保修政策中根本不存在的某些技术性理由，关闭了用户的售后工单。 该事件为 PC 组装用户敲响了关于新型 12V-2x6 电源接口可靠性的警钟。它凸显了高性能新一代显卡在物理安全方面的隐患以及厂商售后支持体系中存在的问题。 故障导致显卡的电源接口发生物理性熔化以及显卡整体报废。具体的抱怨在于，PNY 依靠其官方文件中未提及的保修政策漏洞来拒绝提供维修服务。

rss · Tom's Hardware · 9月26日 11:30

**背景**: 12V-2x6 接口旨在取代旧的显卡供电线，以适应 RTX 5090 等现代显卡的高功耗需求。虽然它通过修改引脚长度比之前的 12VHPWR 设计更具可靠性，但仍需正确安装以防止过热和熔化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/evolving-standards-12vhpwr-and-12v-2x6/">12VHPWR and 12V-2x6 Compared | CORSAIR</a></li>
<li><a href="https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/what-power-cable-does-the-nvidia-geforce-rtx-5090-use/">What power cable does the NVIDIA GeForce RTX 5090 use? | CORSAIR</a></li>

</ul>
</details>

**标签**: `#hardware`, `#gpu`, `#power-supply`, `#warranty`, `#pc-components`

---