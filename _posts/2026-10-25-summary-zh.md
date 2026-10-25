---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> 从 41 条内容中筛选出 15 条重要资讯。

---

1. [泄露数据显示 Zen 6 单核性能比 Zen 5 提升 16.5%](#item-1) ⭐️ 8.5/10
2. [研究人员发现三星电视使用 AI 进行音频和截图追踪](#item-2) ⭐️ 8.5/10
3. [Cerebras Deploys Trillion-Parameter AI Models](#item-3) ⭐️ 8.0/10
4. [New Linux Tool Brings Resizable BAR to Intel Arc GPUs on Old Motherboards](#item-4) ⭐️ 7.5/10
5. [越狱 PS5 现可通过自制工具运行 Windows 版 Steam 游戏](#item-5) ⭐️ 7.5/10
6. [英伟达探索将德国退役核电站改造为 AI 数据中心](#item-6) ⭐️ 7.5/10
7. [Dan Luu 论证在 AI 时代软件工程应更具雄心](#item-7) ⭐️ 7.0/10
8. [LattePanda 发布 Sigma 2 嵌入式 AI 单板服务器](#item-8) ⭐️ 6.5/10
9. [人工智能导致企业财务表现分化和成本上升](#item-9) ⭐️ 6.5/10
10. [Ukrainian drone attacks hammer Russia's finance ministry data center, damaged facility reportedly holds tax databases](#item-10) ⭐️ 6.5/10
11. [fheroes2: A recreation of Heroes of Might and Magic II game engine](#item-11) ⭐️ 6.0/10
12. [三星电视运行 TensorFlow Lite 模型用于设备内跟踪](#item-12) ⭐️ 6.0/10
13. [Hacker News 热议 Goose 实验性基于栈的编程语言](#item-13) ⭐️ 6.0/10
14. [编写极小程序和语言的实用性与创造力](#item-14) ⭐️ 6.0/10
15. [SemiWiki 首席执行官访谈：Cornelis 的 Lisa Spelman 谈 AI/HPC 网络](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [泄露数据显示 Zen 6 单核性能比 Zen 5 提升 16.5%](https://www.techpowerup.com/354103/amd-epyc-9996-geekbench-listing-offers-first-look-at-zen-6-single-core-gains) ⭐️ 8.5/10

AMD EPYC 9996 的 Geekbench 测试结果显示，Zen 6 架构在同等频率下的单核性能比 Zen 5 提升了约 16.5%。该性能提升在全部 15 个单核子测试中均有所体现，其中文件压缩测试提升 8.2%，HTML5 浏览器测试提升高达 25.7%。 该早期数据为系统工程师提供了新 Zen 6 架构的明确基准，证实了密集 Zen 6c 核心变体在每时钟周期效率方面的显著改善。随着 AMD 旨在通过其旗舰“Venice”芯片主导数据中心市场，这些性能提升凸显了其与 Intel 和 Nvidia 等竞争对手之间不断演变的市场格局。 该对比使用了锁定在 4.1 GHz 的 Ryzen 7 9700X 以匹配 EPYC 9996 的最大加速频率，但两者运行在不同的平台和操作系统上。由于 EPYC 9996 使用的是密集型 Zen 6c 核心而非台式机芯片中的完整 Zen 6 核心，其性能表现能否完全平移到未来的桌面硬件上仍不确定。

rss · TechPowerUp News · 10月24日 18:42

**背景**: AMD 的 Zen 6 架构驱动了新的 EPYC“Venice”系列，该系列最近采用台积电 2 nm 工艺制造。EPYC 9996 是一款旗舰级 256 核处理器，支持高达 1,024 MB 的 L3 缓存和高带宽内存，专为高带宽 AI 和数据中心工作负载设计。在消费级市场，下一代台式机 CPU 代号为“Olympic Ridge”，预计将保留 AM5 接口兼容性，但据报道已延期至 2027 年推出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds">AMD ’s 256 - core Epyc 9996 ‘ Venice ’ claims up to... | Tom's Hardware</a></li>
<li><a href="https://www.igorslab.de/en/amd-epyc-9996-venice-256-zen-6-cores-pressure-xeon-vera/">AMD EPYC 9996 Venice : 256 Zen 6 cores for AI racks</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Zen 6`, `#EPYC`, `#CPU Performance`, `#Hardware`

---

<a id="item-2"></a>
## [研究人员发现三星电视使用 AI 进行音频和截图追踪](https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting) ⭐️ 8.5/10

一名安全研究人员对三星电视进行了逆向工程，发现其运行一个本地 AI 模型，能够捕获音频和屏幕截图。 这一发现突显了智能家居设备中严重的隐私漏洞，揭示了未经披露的数据收集所带来的针对性广告风险。 收集的数据包括音频录制和屏幕截图，这些内容专门用于广告定向，而非一般的系统诊断。

rss · Tom's Hardware · 10月25日 10:00

**背景**: 智能家居设备通常使用“常开”AI 功能，能够本地处理用户行为以优化体验或服务。逆向工程是安全专家分析设备软件以发现隐藏或未记录功能的常用技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://readmedium.com/detecting-device-colocation-in-smart-homes-through-advanced-reverse-engineering-techniques-5d096bdc2d38">Detecting Device Colocation in Smart Homes Through Advanced...</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#IoT Security`, `#AI Privacy`, `#Samsung`, `#Reverse Engineering`

---

<a id="item-3"></a>
## [Cerebras Deploys Trillion-Parameter AI Models](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) ⭐️ 8.0/10

Cerebras announces the deployment of trillion-parameter frontier models, sparking debate in the community about the practical utility and currency of the available model options.

hackernews · gmays · 10月25日 01:33 · [社区讨论](https://news.ycombinator.com/item?id=50227356)

**标签**: `#AI Hardware`, `#Cerebras`, `#LLM Deployment`, `#Frontier Models`

---

<a id="item-4"></a>
## [New Linux Tool Brings Resizable BAR to Intel Arc GPUs on Old Motherboards](https://www.techpowerup.com/354116/new-linux-tool-brings-resizable-bar-to-intel-arc-gpus-on-old-motherboards) ⭐️ 7.5/10

A new Linux tool called 'arc-rebar' enables Resizable BAR on older motherboards that lack BIOS support, significantly improving Intel Arc GPU performance without hardware modifications.

rss · TechPowerUp News · 10月25日 16:40

**标签**: `#Intel Arc`, `#Linux`, `#Hardware`, `#GPU Optimization`, `#Resizable BAR`

---

<a id="item-5"></a>
## [越狱 PS5 现可通过自制工具运行 Windows 版 Steam 游戏](https://www.techpowerup.com/354104/jailbroken-ps5-consoles-can-now-run-windows-steam-games-locally) ⭐️ 7.5/10

自制作家 leolobato 发布了 Playden for PS5，这是一款实验性启动器，允许越狱 PS5 主机下载并在本地运行 Windows 版 Steam 游戏。它依赖于 prospero-win（Wine 的 PS5 移植版）以及 DXVK 来处理 Direct3D 图形渲染。 由于它展示了在不切换操作系统或不使用外部 PC 的情况下，在主机上直接运行原生 Windows 可执行文件的复杂方法，因此该工具对系统研究和软件移植具有重要意义。它通过引入庞大的 Windows/Steam 游戏库，极大地扩展了越狱 PS5 生态系统的功能。 Playden 作为标准的 PS5 应用运行，而非独立操作系统，最近的新版本增加了 120 Hz 输出和 4K 分辨率选项。目前它仍属于 Alpha 测试工具，对《半衰期 2》和《新维加斯》等较老或独立游戏支持较好，而许多现代游戏仍会崩溃或无法启动。

rss · TechPowerUp News · 10月24日 19:18

**背景**: “越狱”是指利用安全漏洞运行未经授权的自制作（homebrew）软件，以绕过制造商的限制。Wine 是一个开源的兼容层，通过翻译 Windows API 调用为本地系统调用的方式，允许 Windows 应用程序在非 Windows 系统上运行；而 DXVK 则是一个将 Direct3D 调用转换为 Vulkan API 的翻译层，以改善图形性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK - Wikipedia</a></li>
<li><a href="https://github.com/leolobato/playden-ps5">GitHub - leolobato/ playden - ps 5 : Play your Steam library's Windows...</a></li>
<li><a href="https://www.youtube.com/watch?v=CVJByJ6u6hU">Prospero - Win : Windows Compatibility on PS 5 Without Linux - YouTube</a></li>

</ul>
</details>

**标签**: `#PS5`, `#Jailbreaking`, `#Wine`, `#Emulation`, `#Gaming Tech`

---

<a id="item-6"></a>
## [英伟达探索将德国退役核电站改造为 AI 数据中心](https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch) ⭐️ 7.5/10

英伟达和普鲁士电力公司（PreussenElektra）正在评估将德国已退役的核电站场地改造为大规模 AI 数据中心的可行性。该计划旨在利用现有基础设施，以大幅缩短部署时间。 此次合作解决了 AI 行业的一个关键瓶颈：现代数据中心巨大的电力需求。改造已接入电网的现有场地，有望大幅降低扩展全球计算资源的资金成本和所需时间。 该项目侧重于利用已退役核电站场地现有的电网连接、已分配土地及工业基础设施。虽然这可能更高效，但可行性研究必须解决与旧核设施相关的特定电力输出限制和安全法规问题。

rss · Tom's Hardware · 10月25日 10:30

**背景**: 随着 AI 模型规模扩大，对高密度算力的需求已超过了传统开发商获取充足电力并快速建设新基础设施的能力。核电站提供高密度电力和稳定的基荷容量，尽管已退役，其场地对于高功率 AI 工作负载仍极具吸引力。

**标签**: `#AI Infrastructure`, `#Data Centers`, `#Nuclear Energy`, `#Nvidia`, `#Sustainability`

---

<a id="item-7"></a>
## [Dan Luu 论证在 AI 时代软件工程应更具雄心](https://danluu.com/ambitious/) ⭐️ 7.0/10

Dan Luu 发表了一篇文章，论证软件工程师不应满足于平庸，而应追求更具雄心的成果。这一观点引发了社区关于 AI 生产力提升是否能证明新工程范式的合理性的讨论。 这场辩论凸显了软件行业从维护遗留系统到积极利用 AI 解决复杂问题的转变，这些问题以前仅靠人类团队是无法解决的。它为开发者提供了一个框架，以评估当前 AI 局限性产生的长期影响。 讨论中的批评者指出，AI 的加速效果尚未达到 10 万倍，而消除代码编写瓶颈往往会带来团队内部的“协作损耗”和意识形态摩擦。此外，消费级硬件中质量低下的嵌入式软件等现实案例表明，AI 的集成尚未消除低质量开发。

hackernews · ltratt · 10月24日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50225695)

**背景**: 雄心勃勃的软件工程指的是优先追求长期架构优雅、新颖算法或定制基础设施，而非快速且常规的修复的哲学。Dan Luu 是一位知名的软件工程师，他写作关于性能、系统和编程未来的文章。在人工智能背景下，“氛围编程”是指基于直觉提示而非深入技术知识来编写软件，一些人认为这会导致代码质量下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2025/03/is-vibe-coding-with-ai-gnarly-or-reckless-maybe-some-of-both/">Will the future of software development run on vibes? - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 社区情绪不一，部分人支持需要建立新流程以应对 AI 开发带来的协作损耗。其他人则提出技术怀疑论，质疑大语言模型被夸大的加速效果，并提供了实际见解，指出 AI 尚未解决嵌入式或消费级硬件软件中的根本问题。

**标签**: `#software-engineering`, `#AI`, `#future-of-technology`, `#productivity`, `#code-quality`

---

<a id="item-8"></a>
## [LattePanda 发布 Sigma 2 嵌入式 AI 单板服务器](https://www.techpowerup.com/353798/lattepanda-launches-lattepanda-sigma-2-the-embeddable-ai-single-board-server) ⭐️ 6.5/10

LattePanda 团队推出了 LattePanda Sigma 2，这是一款基于英特尔酷睿 Ultra X7 358H 处理器和英特尔 Arc B390 图形核心的可嵌入 x86 单板服务器。
该主板专为直接集成到智能系统中而设计，可提供 180 TOPS 的 AI 算力。 该硬件通过紧凑形态提供高规格计算能力，显著填补了低功耗边缘设备与高性能工作站之间的空白。
它使得强大的本地 AI 无需外部组件即可直接集成到自主机器人和私有 AI 设备等产品中。 该设备支持最高 64 GB 内存和高速网络，在 INT8 精度下可提供高达 180 TOPS 的总 AI 性能。
它具备灵活的扩展性和实时硬件控制功能，专门针对自主机器人和专业仪器等应用。

rss · TechPowerUp News · 10月25日 15:40

**背景**: LattePanda 是一个以单板计算机和嵌入式系统闻名的品牌，常用于 DIY 和专业工程项目中。
英特尔酷睿 Ultra X7 358H 是一款高性能处理器，内含新的英特尔 Arc B390 集成显卡，为本地 AI 和图形工作负载带来显著的性能提升。
TOPS（每秒万亿次操作）是衡量 AI 性能的常用指标，INT8 指的是用于高效推理的特定 8 位整数精度。

**标签**: `#Hardware`, `#AI Hardware`, `#Local AI`, `#Embedded Systems`, `#LattePanda`

---

<a id="item-9"></a>
## [人工智能导致企业财务表现分化和成本上升](https://www.tomshardware.com/tech-industry/artificial-intelligence/big-tech-is-cashing-in-on-ai-while-the-rest-of-corporate-america-sees-no-financial-returns-report-outlines-how-rising-token-costs-threaten-to-squeeze-corporate-profit-margins) ⭐️ 6.5/10

最新报告指出，尽管大型科技公司（特别是“七巨头”）正从人工智能中获得显著的收入增长，但更广泛的行业尚未看到类似的财务回报。这种差异凸显了美国最大科技公司与标准普尔 500 指数其余成分股之间的日益扩大的鸿沟。 这种显著的分化凸显了日益扩大的财务表现鸿沟，对人工智能行业的可持续性构成挑战。非科技企业在 token 使用方面不断上升的成本威胁到其利润空间，进而影响更广泛的行业生态系统。 “七巨头”的人均收入增长已超越标准普尔 493 指数的表现，突显了生产力和回报率的日益差异。该报告强调了与人工智能采用相关的不断上升的 token 成本正如何威胁非科技行业的利润空间。

rss · Tom's Hardware · 10月25日 15:25

**背景**: “七巨头”指的是七家表现卓越且具有影响力的科技公司，它们构成了标准普尔 500 指数的很大一部分，往往主导着市场收益。标准普尔 493 指数代表该指数中剩余的 493 家成分股，作为更广泛市场的基准。“Token 成本”是指与处理 AI 数据单位相关的财务支出，正在成为采用此类技术的公司的主要运营成本驱动因素之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/magnificent-seven-stocks-8402262">investopedia.com/ magnificent - seven - stocks -8402262</a></li>
<li><a href="https://stansberryresearch.com/stansberry-digest/investors-are-rotating-into-the-sp-493">Investors Are Rotating Into the ' S & P 493 ' | Stansberry Research</a></li>

</ul>
</details>

**标签**: `#AI Economics`, `#Big Tech`, `#Corporate Finance`, `#Token Costs`, `#Industry Analysis`

---

<a id="item-10"></a>
## [Ukrainian drone attacks hammer Russia's finance ministry data center, damaged facility reportedly holds tax databases](https://www.tomshardware.com/tech-industry/data-centers/ukrainian-drone-attacks-hammer-russias-finance-ministry-data-center-damaged-facility-reportedly-holds-tax-databases-facility-also-holds-other-important-state-registry-data) ⭐️ 6.5/10

Ukrainian drone strikes reportedly damaged a Russian finance ministry data center housing tax databases and other critical state registry information.

rss · Tom's Hardware · 10月25日 14:05

**标签**: `#Data Centers`, `#Security`, `#Geopolitics`, `#Infrastructure`, `#War`

---

<a id="item-11"></a>
## [fheroes2: A recreation of Heroes of Might and Magic II game engine](https://github.com/ihhub/fheroes2) ⭐️ 6.0/10

A Hacker News discussion about an open-source recreation of the Heroes of Might and Magic II game engine, highlighting community preservation efforts and experimental AI gameplay.

hackernews · tosh · 10月25日 11:09 · [社区讨论](https://news.ycombinator.com/item?id=50230384)

**标签**: `#open-source`, `#game-engine`, `#retro-gaming`, `#llm-experiment`, `#c++`

---

<a id="item-12"></a>
## [三星电视运行 TensorFlow Lite 模型用于设备内跟踪](https://twitter.com/mike64_t/status/2114150399406202896) ⭐️ 6.0/10

有发现显示，三星在其智能电视上运行 TensorFlow Lite 模型，以处理 960x540 分辨率的视频帧用于跟踪目的。这表明该公司在消费级硬件上进行设备端 AI 推理，以监测用户活动。 在主要消费电子设备中发现设备端跟踪功能引发了重大的隐私担忧，并凸显了针对大型科技公司全面监控行为的监管空白。这表明“智能”硬件可能比消费者意识到的更具侵入性。 具体的技术细节涉及使用 TensorFlow Lite 模型在低分辨率的 960x540 图像上运行，这很可能意味着采用了适合处理功率有限的嵌入式系统的轻量级推理引擎。这种方法允许在不向云端发送原始视频数据的情况下进行持续跟踪，但它仍在本地处理视觉数据。

hackernews · mashally · 10月25日 10:42 · [社区讨论](https://news.ycombinator.com/item?id=50230181)

**背景**: TensorFlow Lite 是一个用于在移动和嵌入式设备上运行机器学习模型的轻量级跨平台解决方案。与将数据上传到服务器的基于云的 AI 不同，设备端推理在本地处理数据，这可能引发关于设备内部正在分析哪些数据的不同隐私问题。

**社区讨论**: 社区讨论意见不一，但普遍对大型科技公司的隐私记录持批评态度，有人认为技术专长较少的非科技巨头保护数据的能力可能不如谷歌或 Meta 等大公司。一些人还对大型科技公司的大规模监控缺乏监管感到沮丧，并指出与之相比，琐碎的法律却层出不穷。此外，一些用户推测手机可能比电视受到更具侵入性的跟踪。

**标签**: `#Privacy`, `#EmbeddedAI`, `#Samsung`, `#Security`, `#Regulation`

---

<a id="item-13"></a>
## [Hacker News 热议 Goose 实验性基于栈的编程语言](https://aardappel.github.io/goose/) ⭐️ 6.0/10

实验性编程语言 Goose 的创造者 Aardappel 在 Hacker News 上参与讨论，社区分析了其用类栈结构替代传统堆内存分配的新型内存管理方法。 该讨论凸显了系统编程中可能发生的范式转变，通过消除垃圾回收并提供确定性的内存布局，尽管目前仍处于早期阶段，在通用用途上存在实际限制。 批评者指出，在 Goose 的静态内存模型中，表示动态数据结构（如具有可变长度字符串的哈希表）仍有挑战性，作者澄清该语言针对的是可增长区域被静态指定的受限使用场景。

hackernews · bobbydigitales · 10月24日 19:06 · [社区讨论](https://news.ycombinator.com/item?id=50224100)

**背景**: 大多数现代编程语言使用堆来管理内存，允许动态分配，但通常需要垃圾回收来防止内存泄漏。基于栈的内存管理更快且更可预测，但通常要求数据结构具有固定大小或严格定义的生命周期。Goose 探索了一种混合方法，开发者手动定义类栈段来存储需要增长的数据，从而避免全局堆分配的开销。

**社区讨论**: 社区成员对该语言直观的内存管理方法表示好奇，同时对其难以轻松处理任意动态数据结构表示担忧。作者参与讨论以解答疑问，但一些用户指出了初始教程中关于字符串分配的事实错误。

**标签**: `#programming_languages`, `#memory_management`, `#systems_programming`, `#compiler_design`, `#hacker_news`

---

<a id="item-14"></a>
## [编写极小程序和语言的实用性与创造力](https://ratfactor.com/cards/pl-small) ⭐️ 6.0/10

文章通过展示为 uxn 虚拟机编写的极小程序示例，探讨了在严格约束下计算的实用性。它还包含关于脚本语言是否应直接编译为机器代码而非使用字节码和解释器的技术争论。 通过展示严苛的限制如何激发创造力并产生惊人的功能工具，该讨论为系统编程和语言设计提供了实用见解。它鼓励开发者重新思考传统的语言实现选择，以提高效率和简化设计。 具体示例包括在 uxn 虚拟机中实现 39 字节的十六进制解码器和 1024 字节的 BLAKE2s 哈希实现。一位评论者认为，直接将机器代码用作“字节码”比设计字节码并编写解释器更简单，并指出为 x86_64 和 ARM64 生成机器代码很直接。

hackernews · andsoitis · 10月24日 21:44 · [社区讨论](https://news.ycombinator.com/item?id=50225674)

**背景**: uxn 虚拟机是一个高度受约束的基于栈的系统，拥有极简的指令集，旨在通过迫使开发者在严格的字节限制内工作来让编程变得有趣。关于字节码与机器代码的争论触及了语言设计的核心权衡：字节码提供可移植性和安全沙箱，而机器代码提供最大的执行速度和简洁性，但以可移植性为代价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/DeltaF1/uxn-impl-guide">GitHub - DeltaF1/ uxn -impl-guide: Notes on how to implement the...</a></li>
<li><a href="https://digitalcommons.ncf.edu/cgi/viewcontent.cgi?article=7765&context=theses_etds">Implementing a tiny virtual machine , assembler, and compiler</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了在 uxn 编程中的具体成就，例如仅用几 KB 就实现了 JSON 转换器和一个完整的卡牌游戏。其他人则探讨了严苛限制带来的心理吸引力，并提出了绕过字节码解释的替代语言架构。

**标签**: `#systems`, `#programming-languages`, `#code-golf`, `#architecture`, `#constrained-computing`

---

<a id="item-15"></a>
## [SemiWiki 首席执行官访谈：Cornelis 的 Lisa Spelman 谈 AI/HPC 网络](https://semiwiki.com/ceo-interviews/374432-ceo-interview-with-lisa-spelman-of-cornelis/) ⭐️ 6.0/10

SemiWiki 发布了对 Cornelis 首席执行官 Lisa Spelman 的访谈，重点介绍了该公司在 AI 和 HPC 基础设施高性能网络方面的战略。 该访谈为业内人士提供了了解 Cornelis 如何应对现代 AI 和 HPC 系统关键网络挑战的见解。 Lisa Spelman 拥有超过 20 年的 AI、云计算和数据中心运营经验，领导着 Cornelis 的产品战略和市场推广工作。

rss · SemiWiki · 10月25日 13:00

**背景**: 高性能计算（HPC）指的是使用集群系统以高速处理海量数据集和复杂问题。现代 AI 基础设施严重依赖先进的网络技术以实现处理节点之间的高效通信，使 Cornelis 等供应商对生态系统至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/hpc">What is high-performance computing ( HPC )? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/High-performance_computing">High-performance computing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Networking`, `#AI Infrastructure`, `#HPC`, `#Industry Interview`, `#Data Center`

---