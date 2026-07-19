---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 51 条内容中筛选出 13 条重要资讯。

---

1. [黑客用巧妙哈希技术将 53.7 万域名装入 5 美元 ESP32 广告拦截器](#item-1) ⭐️ 7.5/10
2. [世界人工智能合作组织未来将重点开展三方面工作](#item-2) ⭐️ 7.3/10
3. [阿里千问 3.8 大模型即将发布并开源](#item-3) ⭐️ 7.3/10
4. [Kimi K3 时刻](#item-4) ⭐️ 7.0/10
5. [Zilog Z80 问世 50 周年，开源替代芯片即将流片为 DIP40 封装](#item-5) ⭐️ 6.5/10
6. [内存芯片大佬承认内存价格“异常高昂”——SK 集团董事长考虑在美国建设半导体工厂以扩大供应，平息“芯片通胀”](#item-6) ⭐️ 6.5/10
7. [Computex 2026 展示 DDR5-8000 RDIMM 与 DDR5-12800 MRDIMM Gen2](#item-7) ⭐️ 6.5/10
8. [商汤科技旗舰级 SenseNova U1 Pro 正式发布](#item-8) ⭐️ 6.3/10
9. [销售 2,500 台 MIDI 录音设备的经验：硬件开发其实没那么难](#item-9) ⭐️ 6.0/10
10. [Transcribe.cpp：开源 C++ 语音转文字库引发 Hacker News 关注](#item-10) ⭐️ 6.0/10
11. [据报道 Valve 每周售出 1.2 万至 1.5 万台 Steam Machine](#item-11) ⭐️ 5.5/10
12. [“幻影旋转”无人机旋转速度极快，几乎隐形——这款飞行装置为现实世界增添了运动模糊效果](#item-12) ⭐️ 5.5/10
13. [俄罗斯无人机加装磁罗盘作为备用导航](#item-13) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [黑客用巧妙哈希技术将 53.7 万域名装入 5 美元 ESP32 广告拦截器](https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds) ⭐️ 7.5/10

一位黑客展示了在一款仅售 5 美元的 ESP32 dongle 上实现的基于 DNS 的广告拦截方案，通过巧妙的哈希技术将 53.7 万个被拦截域名装入仅 4MB 的闪存中，仅占用约 50KB 的 RAM，域名查询响应时间约为 10 毫秒。 这证明了资源极度受限的硬件也能以远低于 Pi-hole 等商业方案的功耗与成本实现全网络广告拦截，让注重隐私的网络管理对具备基础电子技能的爱好者来说变得触手可及。 该实现几乎可以确定依赖于 Bloom 过滤器——一种以可调的误报率换取显著内存节省的概率型数据结构；ESP32 通常配备 520KB SRAM 和 4MB 闪存，因此仅占用 50KB 为 Wi-Fi、TCP/IP 以及 DNS 协议处理留出了充足的运行余量。

rss · Tom's Hardware · 7月19日 10:00

**背景**: ESP32 是乐鑫科技推出的低成本、低功耗微控制器，广泛应用于物联网项目中。基于 DNS 的广告拦截通过劫持域名解析请求并拒绝解析黑名单上的域名来工作，这与 Pi-hole 和 AdGuard Home 的原理相同。Bloom 过滤器是一种节省空间的概率型数据结构，由 Burton Howard Bloom 于 1970 年提出，可以用极小的内存占用检测集合成员关系，但允许少量误报——即偶尔可能误拦合法域名，但绝不会漏放被拦截的域名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bloom_filter">Bloom filter - Wikipedia</a></li>
<li><a href="https://dev.to/ashokan/bloom-filters-a-deep-dive-into-probabilistic-data-structures-5gii">Bloom Filters: A Deep Dive into Probabilistic Data Structures - DEV Community</a></li>

</ul>
</details>

**标签**: `#embedded-systems`, `#ESP32`, `#ad-blocking`, `#DNS`, `#IoT`

---

<a id="item-2"></a>
## [世界人工智能合作组织未来将重点开展三方面工作](https://36kr.com/newsflashes/3902324507281026?f=rss) ⭐️ 7.3/10

29 个国家在上海签署协议，成立世界人工智能合作组织，中方宣布将重点开展国际人工智能能力建设、资源协作和全球人工智能治理三方面工作。

rss · 36氪 · 7月19日 08:58

**标签**: `#AI governance`, `#international cooperation`, `#China AI policy`, `#global AI regulation`, `#geopolitics`

---

<a id="item-3"></a>
## [阿里千问 3.8 大模型即将发布并开源](https://36kr.com/newsflashes/3902296634050437?f=rss) ⭐️ 7.3/10

7 月 19 日，阿里宣布其最新一代大模型千问 3.8 即将发布并开源。目前，Qwen3.8-Max 预览版已率先上线阿里云 Token Plan、Qoder 及 QoderWork 平台，供用户提前体验。 千问系列一直是全球最具影响力的开源模型家族之一，此次 2.4T 参数的新模型开源将加剧与月之暗面 Kimi K3 等开放权重大模型的竞争。开源如此规模的模型对研究者、开发者和寻求替代闭源模型的企业都具有重要价值。 根据社区讨论，千问 3.8 据传参数量约为 2.4 万亿，属于目前最大的开放权重大模型之一。预览版已可通过 Qwen Chat 免费体验，也可通过阿里云 Token Plan 订阅使用，正式开源版本预计近期发布。

rss · 36氪 · 7月19日 08:43

**背景**: 阿里千问（Tongyi Qianwen）模型系列已成为领先的开源大模型阵容，Qwen2.5 和 Qwen3 等早期版本已被广泛用于研究和生产环境。阿里云 Token Plan 是一项基于订阅的大模型服务套餐，为 Claude Code、Cursor、Cline 等 AI 编程工具提供打包的模型调用额度。Qoder 和 QoderWork 是阿里旗下的 AI 开发工具，QoderWork 是由 Qoder 团队推出的桌面级 AI 智能体助手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aliyunbaike.com/bailian/10051/">阿 里 云 百炼 Token Plan 支持哪些 AI 大 模 型 ？这张表一目了然！</a></li>
<li><a href="https://qoder.com/qoderwork">QoderWork | A desktop agentic assistant for everyone</a></li>
<li><a href="https://qoder.com.cn/">研 发 编程助手 | Qoder CN</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极热情，用户欢迎此次开源发布，并希望能有适合本地部署的较小参数版本（如 35B MoE 或 27B 稠密模型）。多位评论者认为该发布是对月之暗面 Kimi K3（2.8T 参数）的竞争性回应，同时提及 DeepSeek 4 也将很快发布。总体而言，讨论反映出开源大模型的势头持续增强，用户既需要前沿规模的模型，也需要可在本地运行的版本。

**标签**: `#AI`, `#LLM`, `#Open Source`, `#Alibaba`, `#Qwen`

---

<a id="item-4"></a>
## [Kimi K3 时刻](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 7.0/10

分析 Kimi K3 模型如何标志着一个潜在的转折点——中国开源权重模型有望达到前沿水平，从而打破西方 AI 实验室主导的竞争格局。

hackernews · sbochins · 7月18日 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48960218)

**标签**: `#AI`, `#Kimi K3`, `#open-weight models`, `#distillation`, `#AI competition`

---

<a id="item-5"></a>
## [Zilog Z80 问世 50 周年，开源替代芯片即将流片为 DIP40 封装](https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon) ⭐️ 6.5/10

Zilog Z80 是最具标志性的 8 位 CPU 之一，于 1976 年 7 月推出，并于 2024 年正式停产，如今迎来了它的 50 周年纪念。与此同时，一款针对经典 DIP40 封装的开源即插即用替代芯片正在准备进入流片生产阶段。 这一里程碑既彰显了 Z80 在复古计算历史中经久不衰的影响力，也反映了通过开源硅设计来保护经典 CPU 架构的日益壮大的运动。爱好者、教育工作者以及嵌入式系统开发者都将受益于这种引脚兼容的现代开源实现的持续供应。 原始的 Z80 在 4μm 制程节点上集成了 8,500 个晶体管，典型运行频率为 2.5 MHz。DIP40（40 引脚双列直插封装）是一种通孔式集成电路封装，曾是复杂逻辑和存储芯片的行业标准，在表面贴装技术成为主流之前，提供了坚固且易于维护的解决方案。

rss · Tom's Hardware · 7月19日 14:12

**背景**: Zilog Z80 由 Federico Faggin 设计，曾是 1980 年代中期以前最受欢迎的家庭电脑 CPU 之一，通常运行 CP/M 操作系统。它驱动了 Heathkit H89、Osborne 1、Kaypro 系列、TRS-80 以及部分 Timex/Sinclair 电脑等知名机型。原始 Z80 所使用的 4μm 制程节点比现代半导体制造落后了数代——当今最先进的制程以个位数纳米计，这意味着这款开源替代芯片很可能采用远比原版先进的制造工艺，同时保持与传统系统的电气和物理兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dual_in-line_package">Dual in-line package - Wikipedia</a></li>
<li><a href="https://hackaday.com/2018/06/19/federico-faggin-the-real-silicon-man/">Federico Faggin: The Real Silicon Man | Hackaday</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_semiconductor_scale_examples">List of semiconductor scale examples - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Z80`, `#retro-computing`, `#open-source-hardware`, `#CPU-architecture`, `#embedded-systems`

---

<a id="item-6"></a>
## [内存芯片大佬承认内存价格“异常高昂”——SK 集团董事长考虑在美国建设半导体工厂以扩大供应，平息“芯片通胀”](https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation) ⭐️ 6.5/10

SK 集团董事长承认内存芯片价格“异常高昂”，并考虑在美国建设半导体工厂以扩大供应，应对“芯片通胀”担忧及潜在新市场进入者的冲击。

rss · Tom's Hardware · 7月19日 13:55

**标签**: `#semiconductors`, `#memory`, `#SK-Hynix`, `#supply-chain`, `#hardware-pricing`

---

<a id="item-7"></a>
## [Computex 2026 展示 DDR5-8000 RDIMM 与 DDR5-12800 MRDIMM Gen2](https://www.servethehome.com/next-gen-server-memory-on-display-ddr5-8000-rdimms-and-mrdimm-gen2-hits-ddr5-12800/) ⭐️ 6.5/10

在 2026 年的 Computex 展会上，Micron 展示了 DDR5-8000 RDIMM，而 Samsung 则展示了速率高达 12,800 MT/s 的第二代 MRDIMM，标志着服务器内存速度的又一次飞跃。 更快的服务器内存对于 AI/ML 工作负载和数据中心应用至关重要，因为内存带宽瓶颈可能限制性能，这些速率的提升在应对这一挑战方面迈出了重要一步。 MRDIMM Gen2 采用多路复用技术，使 DRAM 芯片以其原生数据速率运行，同时将内存通道频率有效地翻倍。JEDEC 的 MRDIMM Gen 2 标准即将完成，并将引入新型多路复用秩寄存器时钟驱动器（MRRCD），以改善信号完整性和时序控制。

rss · ServeTheHome · 7月18日 17:00

**背景**: RDIMM（寄存式内存模组）是服务器内存的标准类型，配备寄存器缓冲芯片以提升信号稳定性和可靠性。MRDIMM（多路复用秩内存模组）是一种较新的类型，通过在主机内存通道与 DRAM 芯片之间进行多路复用，在让底层 DRAM 以原生速率运行的同时，实现了比传统 RDIMM 高得多的有效数据传输率。这两类内存模组都面向 AI、HPC 和数据中心等内存带宽成为关键性能瓶颈的工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tweaktown.com/news/111452/jedec-pushes-ddr5-server-memory-to-12800-mt-s-with-new-mrdimm-gen2-standard-for-ai-and-data-center-workloads/index.html">JEDEC pushes DDR5 server memory to 12,800 MT/s with new...</a></li>
<li><a href="https://www.industrysourcing.com/article/476129">JEDEC pushes DDR5 memory performance to new heights with...</a></li>
<li><a href="https://arxiv.org/html/2605.02371">Performance and Energy Benefits of MRDIMMs</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#server memory`, `#MRDIMM`, `#RDIMM`, `#Computex 2026`

---

<a id="item-8"></a>
## [商汤科技旗舰级 SenseNova U1 Pro 正式发布](https://36kr.com/newsflashes/3902187700766593?f=rss) ⭐️ 6.3/10

商汤科技正式发布其旗舰级多模态大模型 SenseNova U1 Pro，该模型具备统一的理解、生成和动作能力，并支持交付级图像创作。

rss · 36氪 · 7月19日 06:30

**标签**: `#multimodal-ai`, `#sense-time`, `#large-language-models`, `#chinese-ai`, `#product-launch`

---

<a id="item-9"></a>
## [销售 2,500 台 MIDI 录音设备的经验：硬件开发其实没那么难](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard) ⭐️ 6.0/10

一位硬件创业者分享了销售 2,500 台 MIDI 录音设备的经验，认为硬件开发的门槛并没有人们想象中那么高。

hackernews · chipweinberger · 7月19日 10:34 · [社区讨论](https://news.ycombinator.com/item?id=48966713)

**标签**: `#hardware`, `#entrepreneurship`, `#manufacturing`, `#product-development`, `#midi`

---

<a id="item-10"></a>
## [Transcribe.cpp：开源 C++ 语音转文字库引发 Hacker News 关注](https://workshop.cjpais.com/projects/transcribe-cpp) ⭐️ 6.0/10

Transcribe.cpp 是通过 Mozilla.ai 驻场开发者计划开发的开源 C/C++ 语音转文字推理库，在 Hacker News 上获得 611 个点赞和 130 条评论，引起了广泛关注。该工具提供可移植的 GPU 加速支持，兼容多种 STT 模型，旨在让开发者更轻松地在应用中集成快速、本地化的转录功能。 这次发布的意义在于，本地化的开源 STT 基础设施减少了对云端 API 的依赖，让开发者能够更精细地控制模型选择和部署。社区讨论揭示了专有解决方案未能解决的一些空白，包括濒危语言的音标转写以及无缝的连续听写工作流。 该库使用 GGUF 格式的模型，并附带 transcribe-quantize 工具用于生成更小的模型变体。它支持多种 STT 模型架构，并提供跨平台可移植性，适合嵌入到桌面应用中，例如 macOS 虚拟摄像头应用 Emyn。

hackernews · sebjones · 7月19日 00:38 · [社区讨论](https://news.ycombinator.com/item?id=48963879)

**背景**: 语音转文字（STT）技术将口语转换为书面文本，常用于转录、语音助手和无障碍辅助等场景。大多数 STT 系统依赖大型神经网络模型，传统上需要云端处理，但近期的进展使得在消费级硬件上进行本地推理成为可能。ggml 生态系统（包括 llama.cpp 等项目）在实现跨平台高效的设备端 AI 推理方面发挥了重要作用。Mozilla.ai 的驻场开发者计划致力于支持从事开源 AI 工具开发的独立开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/handy-computer/transcribe.cpp/">GitHub - handy-computer/ transcribe . cpp : ggml speech - to - text ...</a></li>
<li><a href="https://blog.mozilla.ai/announcing-transcribe-cpp/">Announcing transcribe . cpp</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论浮现出几个实质性主题：rmunn 指出了缺少用于记录少于一万人的少数族裔语言的国际音标（IPA）音素转写功能；abdullahkhalids 强调了缺少能够实时在文档光标处输入文字的连续听写工作流；ghm2199 表达了对开源 STT 项目可持续性和资金支持的担忧；terhechte 则称赞了该库在其 macOS 虚拟摄像头应用 Emyn 中的便捷集成。

**标签**: `#speech-to-text`, `#transcription`, `#cpp`, `#open-source`, `#linguistics`

---

<a id="item-11"></a>
## [据报道 Valve 每周售出 1.2 万至 1.5 万台 Steam Machine](https://www.techpowerup.com/350872/valve-reportedly-sells-12-15k-steam-machine-units-per-week) ⭐️ 5.5/10

据报道，Valve 每周售出 12,000 至 15,000 台 Steam Machine，该数据基于 Steam 全球热销榜所估算的收入得出。

rss · TechPowerUp News · 7月18日 21:38

**标签**: `#Steam Machine`, `#Valve`, `#gaming hardware`, `#PC gaming`, `#sales data`

---

<a id="item-12"></a>
## [“幻影旋转”无人机旋转速度极快，几乎隐形——这款飞行装置为现实世界增添了运动模糊效果](https://www.tomshardware.com/tech-industry/drones/phantom-twist-drone-spins-so-fast-that-it-is-nearly-invisible-flying-device-adds-motion-blur-to-the-real-world) ⭐️ 5.5/10

美国西北大学的研究人员制造了一架旋转速度极快的无人机，由于运动模糊效应使其看起来几乎不可见，从而实现了一种初级的视觉隐身效果。

rss · Tom's Hardware · 7月19日 13:27

**标签**: `#drones`, `#robotics`, `#motion-blur`, `#cloaking`, `#research`

---

<a id="item-13"></a>
## [俄罗斯无人机加装磁罗盘作为备用导航](https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost) ⭐️ 5.5/10

俄罗斯无人机操作员被发现将廉价的磁罗盘用螺丝固定在无人机上，作为临时性的备用导航辅助设备。当卫星通信中断时，无人机的机载摄像头可以偶尔向下倾斜以目视确认方位，使操作员在无 GPS 的情况下仍能保持方向感知。 这种粗糙的应急方案凸显了现代战场上电子战和 GPS 干扰如何迫使军方开发低成本、冗余的导航方法。同时也展示了商业级 GPS 拒止方案（使用基于 AI 的视觉惯性里程计）与冲突地区可快速部署方案之间的巨大差距。 该罗盘是一个廉价的市售元件，通过螺丝物理固定在机体上，而非集成到飞控系统中，这意味着其读数必须通过摄像头向下拍摄的画面进行人工交叉核对。这种方法的精度远不如正规的传感器融合或视觉惯性里程计系统，而且无人机自身电机和电子设备产生的磁场干扰会显著降低读数准确性。

rss · Tom's Hardware · 7月19日 12:05

**背景**: 现代军用无人机通常依赖 GPS 或 GLONASS 卫星导航来实现航点跟踪和目标定位，但在俄乌冲突中双方都广泛部署了 GPS 干扰和欺骗系统。因此，GPS 拒止环境下的导航是一项关键能力，而视觉惯性里程计（VIO）模块和基于 AI 的地形匹配等商业解决方案也越来越普及。磁罗盘方案则是一种更为粗糙的替代方案，以精度换取简单性和低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spleenlab.ai/solutions-for-gps-denied-navigation">GPS - Denied Navigation Solutions for Drones | Spleenlab</a></li>
<li><a href="https://oksi.ai/omninav-gps-denied-navigation/">OMNInav: A Breakthrough in GPS - Denied Navigation for UAS - OKSI</a></li>
<li><a href="https://pilotinstitute.com/heavy-interference-drones/">Flying Your Drone in Urban Areas with Heavy Signal Interference</a></li>

</ul>
</details>

**标签**: `#drones`, `#navigation`, `#military-tech`, `#GPS-denied`, `#hardware-quirks`

---