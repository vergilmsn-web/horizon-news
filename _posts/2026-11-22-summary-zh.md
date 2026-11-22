---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 46 条内容中筛选出 13 条重要资讯。

---

1. [Claude AI 协助在 Lean 中形式化验证黎曼猜想](#item-1) ⭐️ 9.0/10
2. [美国政府提议禁止或重税海外数据中心建设](#item-2) ⭐️ 8.5/10
3. [群晖预览搭载内置 NPU 和 64GB 内存的企业级 SSD](#item-3) ⭐️ 7.5/10
4. [USB 集线器延迟导致 2.5Gbps 以太网速度下降 75%](#item-4) ⭐️ 7.0/10
5. [PostgreSQL Extensions in Go](#item-5) ⭐️ 7.0/10
6. [Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk](#item-6) ⭐️ 6.5/10
7. [Defense firm’s EMP ‘Dragon’ weapon fries 51 jam-proof drones simultaneously](#item-7) ⭐️ 6.5/10
8. [Homelabber’s second-gen Optane build uses two RTX 3090s to run 2.8-trillion-parameter Kimi AI model at 3.11 tokens per second](#item-8) ⭐️ 6.5/10
9. [英特尔 Nova Lake-H 规格表揭示 4.8 GHz 睿频与 25 W 热设计功耗](#item-9) ⭐️ 5.5/10
10. [摩尔线程预告“庐山”GPU，将打破消费级显存纪录](#item-10) ⭐️ 5.5/10
11. [银欣 HELA 1350Rz 配备三根 EPS 线缆支持高功耗 CPU](#item-11) ⭐️ 5.5/10
12. [Tom's Hardware 回顾 SC26 高性能计算硬件发布](#item-12) ⭐️ 5.5/10
13. [研究人员在 35 年前超级任天堂游戏机上利用 Super FX 2 芯片运行 220 万参数大语言模型](#item-13) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Claude AI 协助在 Lean 中形式化验证黎曼猜想](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

研究人员使用 Claude AI 协助在 Lean 定理证明器中形式化和验证黎曼猜想的证明，包括验证黎曼 zeta 函数的所有非平凡零点的实部均为 1/2。 这一里程碑展示了自动定理证明的范式转变，表明 AI 可以协助形式化复杂的数学结果和现代数学基础。它还引发了关于 AI 生成证明的可靠性以及独立一致性检查器作用的重要问题。 Claude 对现代数学很大一部分的形式化不仅是针对特定假设，也是对数学基础的重大成就。该过程需要人类专家参与，以确保 AI 没有利用证明检查器中的漏洞。

hackernews · g-b-r · 11月21日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**背景**: 黎曼猜想是数学中最著名的未解决问题之一，涉及素数的分布。形式化验证使用 Lean 等计算机系统来机械地检查数学证明的正确性。Lean 定理证明器是一个用于以绝对精度表达和验证数学陈述的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kingy.ai/blog/levent-alpoge-claude-riemann-hypothesis-proof/">Riemann hypothesis proof verified in Lean</a></li>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>
<li><a href="https://lean-lang.org/learn/">Learn — Lean Lang</a></li>

</ul>
</details>

**社区讨论**: 社区就 AI 辅助证明的可靠性展开了辩论，指出虽然 con-leche 和 con-ron 等独立检查器有自身的一致性证明，但理论上 AI 可能会利用漏洞。人类专家的参与也获得了认可，该结果被视为形式化数学基础的一大进步。

**标签**: `#AI`, `#Formal Verification`, `#Lean`, `#Riemann Hypothesis`, `#Mathematics`

---

<a id="item-2"></a>
## [美国政府提议禁止或重税海外数据中心建设](https://www.tomshardware.com/tech-industry/data-centers/trump-wants-to-ban-us-companies-from-building-overseas-data-centers-as-bans-slow-development-also-considers-putting-a-tremendous-tax-in-lieu-of-prohibition) ⭐️ 8.5/10

美国政府已宣布一项提案，限制美国公司在境外建设数据中心。该计划涉及要么完全禁止海外建设，要么对此类国际扩张活动征收高额税收。 这一政策转变将通过迫使人工智能和科技公司将其物理资产本地化到美国境内，从根本上改变全球云基础设施战略。这种强制性要求可能会大幅增加运营成本，并重塑全球数据主权和数字基础设施发展的竞争格局。 该提案明确将行业开发放缓与新限制措施联系起来，将其框架定为维持国内技术领导地位的必要手段。虽然提到了禁令，但政府也在考虑以“巨额税收”作为直接禁止的可行替代方案。

rss · Tom's Hardware · 11月21日 16:29

**背景**: 数据主权是指在一个国家境内产生的数据必须受该国法律和监管框架管辖的原则。历史上，美国一直 favor 市场驱动的数据中心增长方式，允许全球玩家在最有效的地方建设基础设施。这项拟议政策代表了与传统市场驱动模式的显著偏离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>
<li><a href="https://michaelbommarito.com/wiki/datacenters/policy/international/">international datacenter policy comparison | mike bommarito</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Geopolitics`, `#Data Centers`, `#Policy`, `#Tech Industry`

---

<a id="item-3"></a>
## [群晖预览搭载内置 NPU 和 64GB 内存的企业级 SSD](https://www.techpowerup.com/355089/phison-previews-an-ssd-that-runs-ai-frameworks-on-its-own-npu) ⭐️ 7.5/10

群晖在 2026 年高性能计算大会（SC26）上预览了一款计算存储企业级 SSD，该设备集成了片上 NPU 和运行速度达 130 GB/s 的 64GB 内存。这款固态硬盘支持直接在设备上运行 PyTorch、vLLM、OpenVINO 和 llama.cpp 等 AI 框架。 这一进展大幅降低了数据密集型 AI 工作负载的数据传输开销，通过存储设备本地处理数据，可将主机数据传输量减少 10 至 100 倍。它代表了系统架构的重大转变，使得 AI 推理可以从主 CPU/GPU 卸载到存储层。 该 NPU 的性能以 DMIPS 而非标准的 TOPS 指标来衡量，这在 AI 加速器中较为罕见。由于仍处于概念验证预览阶段，关于该 NPU 固态硬盘的控制器类型、接口、形态因子和内存类型等详细规格目前尚不明确。

rss · TechPowerUp News · 11月22日 01:23

**背景**: 计算存储（CS）是指在存储设备中集成处理能力，以对在设备上存储的数据执行计算，从而减少对主 CPU 的数据传输需求。NPU（神经网络处理单元）是专为加速机器学习和 AI 工作负载而设计的专用硬件。TOPS（每秒万亿次操作）是衡量 AI 硬件峰值性能的常见指标，而 DMIPS（每秒百万条指令）则是一种较旧的指标，通常用于通用 CPU 性能评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.guru3d.com/story/phison-previews-a-computational-ssd-with-an-npu-and-64gb-of-memory/">Phison Previews a Computational SSD With an NPU and 64GB of ...</a></li>
<li><a href="https://www.techspot.com/news/114653-phison-shows-ssd-design-npu-64gb-memory-runs.html">Phison shows an SSD design with an NPU and 64GB of memory ...</a></li>
<li><a href="https://www.tomshardware.com/pc-components/ssds/phison-details-ssd-with-a-built-in-npu-and-64gb-of-memory-that-supports-pytorch-and-llama-cpp-running-on-the-drive-second-design-merges-fast-pslc-cache-and-qlc-capacity-behind-one-controller">Phison details SSD with a built-in NPU and 64GB of memory ...</a></li>

</ul>
</details>

**标签**: `#Storage`, `#AI Hardware`, `#Computational Storage`, `#SSD`, `#Edge AI`

---

<a id="item-4"></a>
## [USB 集线器延迟导致 2.5Gbps 以太网速度下降 75%](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

有用户演示了通过 USB 集线器连接 USB 显示器会导致 2.5Gbps 以太网下载速度下降 75%，原因是网络协议栈延迟增加。这种延迟导致操作系统无法足够快地确认接收到的数据包，从而引起网卡接收缓冲区溢出并丢弃数据。 对于使用高带宽住宅网络（1Gbps+）并依赖 USB 外设的用户而言，此问题意义重大，因为它凸显了物理 USB 拓扑结构而非仅仅带宽限制可能会严重降低现代有线网络性能。这为网络工程师和技术爱好者提供了反直觉的特定故障排查视角。 通过使用一个需要较少数据包确认的网络适配器解决了性能问题。这证实了根本原因是集线器引起的延迟与特定 TCP/IP 协议栈确认时序之间的相互作用，而不是 USB 线缆的原始数据速率限制。

hackernews · soheilpro · 11月21日 10:36 · [社区讨论](https://news.ycombinator.com/item?id=50587875)

**背景**: 以太网连接依赖于确认系统，接收主机需确认数据包的到达。在高速网络中，如果主机过忙或受 USB 集线器等硬件的延迟影响，将无法及时发送确认信息，导致发送方暂停，且接收方内部缓冲区填满，从而引发数据包丢失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kb.plugable.com/wired-network-adapters/maximizing-25gb-ethernet-performance">Maximizing 2.5Gbps Ethernet Performance - Plugable Knowledge Base</a></li>
<li><a href="https://www.xda-developers.com/usb-ethernet-adapters-are-bottlenecking-your-nas/">USB Ethernet adapters are bottlenecking your NAS - XDA Developers</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000005811/ethernet-products.html">Tuning Throughput Performance for Intel® Ethernet Adapters</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出，瓶颈实际上在于网络适配器而非显示器本身，也有人分享了与 SFP+ 模块等其他硬件相关的类似荒谬延迟问题。部分用户还讨论了千兆以上住宅网速在日常实际任务中的实用性。

**标签**: `#networking`, `#hardware`, `#troubleshooting`, `#usb`, `#performance`

---

<a id="item-5"></a>
## [PostgreSQL Extensions in Go](https://jespino.github.io/gopgext/) ⭐️ 7.0/10

A tool by Valentin Viallet allows developers to write PostgreSQL extensions using the Go programming language, sparking discussion on the suitability of Go for data-layer components.

hackernews · valyala · 11月21日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50591260)

**标签**: `#Go`, `#PostgreSQL`, `#Database Extensions`, `#CGO`, `#Systems Programming`

---

<a id="item-6"></a>
## [Rapidus reportedly struggles to produce working SRAM on its 2nm node, putting 2027 mass production at risk](https://www.tomshardware.com/tech-industry/semiconductors/rapidus-reportedly-struggles-to-produce-working-sram-on-its-2nm-node-putting-2027-mass-production-at-risk-company-faces-significant-challenges-using-euv-to-develop-gaa-transistors) ⭐️ 6.5/10

Rapidus faces significant challenges in producing working SRAM on its 2nm GAA node, jeopardizing its 2027 mass production target.

rss · Tom's Hardware · 11月21日 15:30

**标签**: `#Semiconductors`, `#Rapidus`, `#2nm`, `#GAA Transistors`, `#Supply Chain`

---

<a id="item-7"></a>
## [Defense firm’s EMP ‘Dragon’ weapon fries 51 jam-proof drones simultaneously](https://www.tomshardware.com/tech-industry/drones/defense-firms-emp-dragon-weapon-fries-51-jam-proof-drones-simultaneously-high-power-electromagnetic-system-relies-on-120-year-old-vacuum-tube-tech-to-defeat-fiber-optic-uavs) ⭐️ 6.5/10

Aselsan's 'Dragon' weapon system utilizes high-power electromagnetic energy to simultaneously disable 51 fiber-optic, jam-proof drones.

rss · Tom's Hardware · 11月21日 13:54

**标签**: `#Defense Technology`, `#Counter-Drone`, `#Electromagnetic Pulse`, `#Hardware`, `#Military`

---

<a id="item-8"></a>
## [Homelabber’s second-gen Optane build uses two RTX 3090s to run 2.8-trillion-parameter Kimi AI model at 3.11 tokens per second](https://www.tomshardware.com/tech-industry/artificial-intelligence/homelabbers-second-gen-optane-build-runs-2-8-trillion-parameter-kimi-k3-at-3-11-tokens-per-second-after-adding-two-rtx-3090s-moving-nearly-half-the-model-into-a-ram-drive-boosted-performance-by-41-percent) ⭐️ 6.5/10

A homelabber utilized a second-gen Optane PMem server and two RTX 3090s to run the 2.8-trillion-parameter Kimi K3 model, achieving 3.11 tokens per second by offloading nearly half the model to a RAM drive.

rss · Tom's Hardware · 11月21日 12:00

**标签**: `#homelab`, `#optane`, `#LLM-inference`, `#rtx-3090`, `#kimi`

---

<a id="item-9"></a>
## [英特尔 Nova Lake-H 规格表揭示 4.8 GHz 睿频与 25 W 热设计功耗](https://www.techpowerup.com/355088/intel-nova-lake-h-spec-sheet-shows-up-with-a-4-8-ghz-boost-and-25-w-tdp) ⭐️ 5.5/10

研华科技（Advantech）的初步数据表揭示，英特尔 Core Ultra Series 4 “Nova Lake-H” 移动 CPU 将采用 16 核心设计，具备 4.8 GHz 睿频和 25 W TDP。该芯片专为移动设备设计，例如用于自主移动机器人的 4 英寸 ASR-A505 单板计算机。 该规格表确认了英特尔即将推出的移动处理器及其目标用例，表明其致力于面向机器人等专门应用的高性能、低功耗计算。它为硬件爱好者和系统设计人员提供了有关下一代 Core Ultra 移动系列处理器性能和功耗限制的早期洞察。 研华科技的数据表列出了“8P+4E+4LE”的核心配置，这很可能是一个笔误，与先前泄露的 4P+8E+4LE 配置相矛盾。根据该文档的框图，TDP 可能被配置为 15 W 到 25 W 之间。

rss · TechPowerUp News · 11月21日 23:58

**背景**: 英特尔的 “Nova Lake” 是其下一代 Core Ultra 处理器系列，预计于 2026 年发布。混合架构使用两种核心：用于繁重任务的高性能 “P 核” 和用于后台任务的能效 “E 核”，这种设计旨在提高笔记本电脑的电池续航。TDP 或热设计功耗是组件预计生成的最大热量，它决定了系统维持稳定性能所需的散热能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/intel-core-ultra-4-series-16-core-nova-lake-mobile-processor-specifications-leaked/">Intel’s 16-Core Nova Lake-H Leaked Spec Sheet Lists 4.8 GHz ...</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000055611/processors.html">Thermal Design Power (TDP) in Intel® Processors</a></li>

</ul>
</details>

**标签**: `#Intel`, `#CPU`, `#Hardware`, `#Mobile`, `#Leak`

---

<a id="item-10"></a>
## [摩尔线程预告“庐山”GPU，将打破消费级显存纪录](https://www.techpowerup.com/355084/moore-threads-claims-its-next-gpu-will-break-the-consumer-vram-record) ⭐️ 5.5/10

摩尔线程声称其下一代桌面 GPU（代号“庐山”）将拥有消费级显卡中最大的显存容量，这一预告是在 2026 年 12 月的开发者大会前夕发布的。 这一战略举措使摩尔线程能够与英伟达等全球巨头在消费级市场和本地大语言模型（LLM）领域展开更激烈的竞争。 基于公司此前的承诺，外界推测该显卡可能配备高达 64 GB 的显存，这将远超 GeForce RTX 5090 上的 32 GB。

rss · TechPowerUp News · 11月21日 20:56

**背景**: 摩尔线程是中国主要的 GPU 制造商，其 MTT S80 显卡配备了 16 GB 显存。“庐山”架构首次亮相于首届 MUSA 开发者大会，旨在与高端西方 GPU 抗衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/gpu-specs/mtt-s80.c4259">Moore Threads MTT S 80 Specs | TechPowerUp GPU Database</a></li>
<li><a href="https://hyperpc.ae/company/news/moore-threads-introduced-lushan-chip">Moore Threads Reveals Huagang Architecture & Lushan GPU ...</a></li>

</ul>
</details>

**标签**: `#GPU`, `#Moore Threads`, `#VRAM`, `#Hardware`, `#Computer Architecture`

---

<a id="item-11"></a>
## [银欣 HELA 1350Rz 配备三根 EPS 线缆支持高功耗 CPU](https://www.techpowerup.com/355083/silverstone-equips-hela-1350rz-with-three-eps-cables-citing-nova-lake-s-high-power-demands) ⭐️ 5.5/10

银欣推出了 HELA 1350Rz，这是一款 1350W 的 ATX 3.1 电源，配备了三根 4+4-pin EPS 线缆，而非常见的两根，以适应英特尔即将推出的 Nova Lake-S CPU。公司明确指出，这是为了满足新平台的高功耗需求而增加的线缆。 这一硬件更新表明英特尔新一代桌面 CPU 的功耗可能会显著增加，这对于发烧友和系统搭建者确保电源供电稳定性具有重要意义。它为准备基于新的 Z990 主板平台构建系统的用户提供了前瞻性的规格参考。 泄露信息表明，52 核心的旗舰版 Nova Lake-S 变体的 PL2 功耗限制可能高达 474W，而 Z990 主板支持三个 8-pin EPS 接口。有爆料人指出，第三个接口是一个“锦上添花”的配置，有助于超频，但并非发挥最大性能所必需。

rss · TechPowerUp News · 11月21日 20:27

**背景**: EPS（增强型电源）线缆用于从电源向 CPU 插座供电；4+4 针设计用于高功耗连接。12V-2x6 连接器是 ATX 3.1 的高功耗显卡标准，替代了旧版标准。PL2 指的是 CPU 在密集工作负载下可以短暂超过的峰值功率限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/news/16-pin-power-connector-gets-a-much-needed-revision-meet-the-new-12v-2x6-connector">16-Pin Power Connector Gets A Much-Needed... | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Power_supply_unit_(computer)">Power supply unit (computer) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Hardware`, `#PSU`, `#Intel`, `#SilverStone`, `#Nova Lake`

---

<a id="item-12"></a>
## [Tom's Hardware 回顾 SC26 高性能计算硬件发布](https://www.tomshardware.com/tech-industry/supercomputers/this-week-on-toms-hardware-premium-21-november-2026-amd-nvidia-and-more-show-off-the-future-of-high-performance-computing-at-sc26) ⭐️ 5.5/10

Tom's Hardware 于 2026 年 11 月 21 日发布了一期高级每周通讯，总结了 AMD、Nvidia 和 Intel 在超级计算 2026（SC26）会议上发布的硬件。该摘要涵盖了高性能计算（HPC）领域的新设备和相关发展。 SC26 是展示新一代超级计算机和 AI 基础设施的顶级场所，因此来自主要科技媒体的综合摘要对于快速了解行业的技术发展方向非常有帮助。该总结有助于读者理解主要硬件厂商在数据中心领域的竞争格局。 SC26 大会于 2026 年 11 月 15 日至 20 日在芝加哥的 McCormick Place 举行，展会开放时间为 11 月 17 日至 19 日。Tom's Hardware 指出，该通讯是对该活动报道内容的详尽清单。

rss · Tom's Hardware · 11月21日 16:00

**背景**: 超级计算（SC）大会是高性能计算行业的一项重要年度活动，研究人员和从业人员在此讨论硬件、网络和存储方面的最新进展。AMD 和 Nvidia 等厂商通常会在此类活动上发布新的数据中心 GPU 和 CPU，以争夺在 AI 和科学计算领域的市场份额。

**标签**: `#HPC`, `#SC26`, `#GPU`, `#AMD`, `#Nvidia`

---

<a id="item-13"></a>
## [研究人员在 35 年前超级任天堂游戏机上利用 Super FX 2 芯片运行 220 万参数大语言模型](https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies) ⭐️ 5.5/10

爱好者们成功在 35 年前的任天堂超级任天堂(SNES)游戏机上运行了 220 万参数聊天机器人模型的客户端。该系统利用 Super FX 2 芯片进行加速，该芯片提供了 21 MHz 的 RISC 处理能力来执行推理任务。 该项目通过在最古老的硬件上执行 AI 工作负载，展示了模型压缩和嵌入式推理的极限。它作为一个有趣的原型验证，证明了轻量级模型在资源极度受限的嵌入式系统上的高效性。 该实现依赖一个主要用于图形渲染的 16 位 RISC 处理器来处理量化大语言模型的数学运算。220 万参数的大小表明使用了极端的量化和压缩技术，以便将该模型适配到主机有限的内存架构中。

rss · Tom's Hardware · 11月21日 15:02

**背景**: Super FX 是一款用于超级任天堂(SNES)的定制 RISC 处理器，主要作为图形协处理器来渲染 3D 多边形。大语言模型通常是重型软件，需要现代硬件支持；但量化等技术通过降低模型权重的精度，使得较小版本的模型能够在资源受限的嵌入式设备上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Super_FX">Super FX - Wikipedia</a></li>
<li><a href="https://superfxchip.berrry.app/">Super FX - Revolutionary 16-bit Graphics Coprocessor</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/35-year-old-snes-runs-chatgpt-accelerated-with-a-super-fx-2-chip-21-mhz-of-risc-muscle-speeds-2-2m-parameter-chatbot-replies">35-year-old SNES runs ChatGPT, accelerated with a Super FX 2 chip</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Embedded Systems`, `#Retro Computing`, `#Model Compression`, `#Inference`

---