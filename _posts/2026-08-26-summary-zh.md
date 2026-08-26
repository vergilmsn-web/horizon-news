---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> 从 122 条内容中筛选出 20 条重要资讯。

---

1. [d-Matrix Raptor：首款 3D 堆叠 DRAM AI 加速器实现 100 TB/s 带宽](#item-1) ⭐️ 8.5/10
2. [OpenAI 的 700 瓦 Jalapeño ASIC 超越 1400 瓦英伟达旗舰 GPU——声称每瓦吞吐量提升高达 1.9 倍、延迟降低 3.6 倍，与博通共同开发](#item-2) ⭐️ 8.5/10
3. [Intel 在 Hot Chips 2026 详解 Crescent Island AI 加速器](#item-3) ⭐️ 8.5/10
4. [内存价格飙升；2027 年 DRAM 与 NAND 将占 CSP 资本支出的 68%](#item-4) ⭐️ 7.5/10
5. [（新闻稿）苹果推出搭载 M5 Max 和 M5 Ultra 的新款 Mac Studio](#item-5) ⭐️ 7.5/10
6. [富士通 Monaka CPU：144 核 Arm 服务器芯片，采用 chiplet 缓存与双 256-bit SVE2](#item-6) ⭐️ 7.5/10
7. [OXMIQ 在 Hot Chips 2026 上阐述高带宽闪存的有限应用场景](#item-7) ⭐️ 7.5/10
8. [Arm 在 Hot Chips 展示 AGI 服务器 CPU：136 核、UCIe Chiplet 互联](#item-8) ⭐️ 7.5/10
9. [EPA 拟取消数据中心空气污染许可证的公众意见征询要求](#item-9) ⭐️ 7.5/10
10. [三星在 Hot Chips 2026 发布内置逻辑单元的 LPDDR5X-PIM](#item-10) ⭐️ 7.5/10
11. [英特尔 Wildcat Lake：采用 UCIe 芯粒互连的 18A 入门级芯片](#item-11) ⭐️ 7.5/10
12. [谷歌在 Hot Chips 2026 大会发布第八代 TPU 芯片家族](#item-12) ⭐️ 7.5/10
13. [微软将在 Hot Chips 2026 揭秘 Maia 200 AI 加速器](#item-13) ⭐️ 7.5/10
14. [Cerebras 在 2026 年 Hot Chips 大会上探讨将 WSE 扩展至机架规模](#item-14) ⭐️ 7.5/10
15. [NVIDIA 将 Groq 3 LPU 集成至 Vera Rubin 实现异构 AI 计算](#item-15) ⭐️ 7.5/10
16. [全球海洋表面温度受气候变化影响创历史新高](#item-16) ⭐️ 7.3/10
17. [AWS 收购 DuckDB](#item-17) ⭐️ 7.0/10
18. [Qwen3.8-Flash-Next：1760 亿参数 MoE，Qwen4 架构预览](#item-18) ⭐️ 7.0/10
19. [以色列设立并资助虚假美国智库，试图操纵 AI 进行宣传](#item-19) ⭐️ 7.0/10
20. [XCorp 向 XCancel 和 Nitter 发出停止侵权通知函](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [d-Matrix Raptor：首款 3D 堆叠 DRAM AI 加速器实现 100 TB/s 带宽](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card) ⭐️ 8.5/10

在 2026 年 Hot Chips 大会上，d-Matrix 发布了 Raptor，这是首款面向生成式推理的 3D DRAM AI 加速器。它采用 36 微米间距的面对面（face-to-face）键合技术，将 TSMC 4nm 计算芯片直接堆叠在定制 DRAM 芯片之上，单卡实现 100 TB/s 的内存带宽。 该架构的带宽比当前基于 HBM 的加速器（如 H100 约 3.35 TB/s、B200 约 8 TB/s）高出一个数量级，直接突破了限制大语言模型推理的内存带宽瓶颈。由于省去了 HBM 和硅中介层（interposer），d-Matrix 声称其每比特能耗仅为 HBM3 的六分之一，有望重塑大规模生成式 AI 服务的成本效率指标。 Raptor 采用 36 微米间距的面对面微凸点（microbump）键合，虽然间距比最前沿的混合键合（sub-10 µm）更宽，但 d-Matrix 称该工艺已成熟且良率高。计算芯片直接位于 DRAM 芯片之上，省去了传统设计中必需的硅中介层、硅通孔（TSV）和 HBM 堆叠步骤。

rss · Tom's Hardware · 8月26日 12:00

**背景**: 现代 AI 加速器通常依赖高带宽存储器（HBM），通过硅中介层和硅通孔（TSV）将垂直堆叠的 DRAM 芯片与逻辑芯片相连。3D 面对面堆叠是一种替代性集成方案，将两块芯片的有源面（active surface）相对键合，从而实现更密集、延迟更低、功耗更低的互连。生成式 AI 推理（即运行大语言模型等模型生成文本）具有独特的内存访问模式，高度依赖带宽，因为模型权重必须在每个 token 生成时从内存中流式读取。Hot Chips 是一年一度的顶级半导体会议，各公司在此向技术社区展示前沿芯片架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/">d-Matrix Raptor 3D-DRAM Accelerator for Generative Inference at Hot Chips 2026 - ServeTheHome</a></li>
<li><a href="https://www.techtimes.com/articles/325300/20260824/d-matrix-raptor-delivers-100-tb-s-stacked-dram-fraction-hbm-energy-cost.htm">d-Matrix Raptor Delivers 100 TB/s From Stacked DRAM at Fraction of HBM Energy Cost</a></li>

</ul>
</details>

**标签**: `#AI accelerators`, `#3D stacking`, `#DRAM`, `#semiconductors`, `#Hot Chips 2026`

---

<a id="item-2"></a>
## [OpenAI 的 700 瓦 Jalapeño ASIC 超越 1400 瓦英伟达旗舰 GPU——声称每瓦吞吐量提升高达 1.9 倍、延迟降低 3.6 倍，与博通共同开发](https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks) ⭐️ 8.5/10

OpenAI 首次公布了其 Jalapeño ASIC 的基准测试数据，声称相比英伟达 GB300，每瓦吞吐量提升 1.9 倍、延迟降低 3.6 倍，该芯片与博通共同开发。

rss · Tom's Hardware · 8月25日 18:05

**标签**: `#AI hardware`, `#ASIC`, `#OpenAI`, `#Nvidia`, `#semiconductors`

---

<a id="item-3"></a>
## [Intel 在 Hot Chips 2026 详解 Crescent Island AI 加速器](https://www.tomshardware.com/pc-components/gpus/hot-chips-2026-intel-dives-deep-on-crescent-island-ai-accelerator-larger-caches-and-deeper-xmx-engines-target-maximum-ai-flops-per-watt) ⭐️ 8.5/10

在 Hot Chips 2026 大会上，Intel 公布了其 Crescent Island AI 加速器的详细架构，该加速器基于 Xe3P 架构打造，拥有最多 32 个 Xe 核心、更深的 XMX 矩阵引擎、更大的缓存，支持 HBM4 内存，并采用液冷散热，面向数据中心推理工作负载，追求每瓦最高 AI FLOPS 性能。 Crescent Island 标志着 Intel 重新进入由 NVIDIA 和 AMD 主导的竞争激烈的 AI 加速器市场。通过移除图形专用硬件（3D 和光线追踪）并将芯片面积专用于 AI 计算，Intel 释放出一个明确的信号：采取聚焦且效率优先的策略，主攻快速增长的推理市场，尤其是智能体 AI（agentic AI）工作负载。 Crescent Island 的 32 个 Xe 核心各包含 8 个 Vector Engines 和 8 个 XMX Engines，整个 GPU 总计各 256 个；该设计移除了 3D 和光线追踪单元，以释放芯片面积用于 AI 计算。Intel 还公布了 350W 的 PCIe 版本和支持最高 480GB 内存的配置，而 XMX 引擎在二维脉动阵列上执行 DPAS 指令以加速矩阵乘法运算。

rss · Tom's Hardware · 8月25日 15:12

**背景**: Hot Chips 是每年举办的知名半导体会议，各公司会在会上展示即将推出的芯片的深度架构细节。XMX（Xe Matrix Extensions）是 Intel 专用的 AI 矩阵乘法引擎，类似于 NVIDIA Tensor Core，在二维脉动阵列上执行 DPAS 指令，相比传统 GPU 通路可提供高达 16 倍的 AI 推理算力。HBM4（第四代高带宽内存）是下一代 3D 堆叠 DRAM，可提供显著更高的带宽，对于驱动大型 AI 模型至关重要。Xe3P 是 Intel 第三代 Xe 架构，通过移除仅用于图形的模块，Intel 打造了一个纯粹面向数据中心的变体，专门优化每瓦 AI 吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/intel-details-xe3p-gpu-architecture-crescent-island-gets-up-to-480gb-memory-and-350w-pcie-variant">Intel details Xe3P GPU architecture, Crescent Island gets up to 480GB memory and 350W PCIe variant - VideoCardz.com</a></li>
<li><a href="https://wccftech.com/intel-crescent-island-gpus-32-xe3p-cores-for-agentic-ai-low-cost-lpddr5x-up-to-480-gb/">Intel Crescent Island GPUs Pack Up To 32 Xe3P Cores, Optimized For Agentic AI With Low-Cost LPDDR5X That Reaches Up To 480 GB Capacity</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000091112/graphics.html">What is Xe Matrix eXtensions (XMX)? - Intel</a></li>

</ul>
</details>

**标签**: `#Intel`, `#AI accelerator`, `#Hot Chips 2026`, `#GPU`, `#data center`, `#HBM4`

---

<a id="item-4"></a>
## [内存价格飙升；2027 年 DRAM 与 NAND 将占 CSP 资本支出的 68%](https://www.techpowerup.com/351976/memory-prices-soar-dram-and-nand-flash-to-account-for-68-of-major-csp-capex-in-2027) ⭐️ 7.5/10

TrendForce 预测，主要云服务提供商（CSP）的总资本支出将在 2026 年同比增长 98%，并在 2027 年再增长 50%，主要受内存价格飙升和 AI 基础设施需求推动。DRAM 与 NAND Flash 合计将占 2026 年 CSP 资本支出的 47%，到 2027 年升至 68%。 这标志着云基础设施经济结构的根本性重塑，内存（而非计算芯片）正成为超大规模云厂商的主导支出项。内存价格的剧烈上涨将影响 AI 部署成本、云服务提供商的利润空间以及整个硬件供应链，可能挤压 GPU 和网络设备的预算。 服务器 DRAM 合约价格在 2025 年下半年已上涨 64%，预计 2026 年再飙升约 270%；企业级 SSD 价格在 2025 年下半年上涨约 35%，预计 2026 年累计涨幅达 235%。这些数字反映的是大批量采购的合约价格，而非现货市场价格。

rss · TechPowerUp News · 8月26日 09:21

**背景**: DRAM（动态随机存取内存）是 CPU 和 GPU 用于快速数据访问的易失性主内存，而 NAND Flash 是 SSD 和存储卡背后的非易失性存储技术。企业级 SSD 是为数据中心工作负载设计的高耐用性、高性能驱动器，在可靠性和耐用性方面与消费级 SSD 有所不同。云服务提供商（CSP），如 AWS、Microsoft Azure 和 Google Cloud 运营着大规模数据中心，是服务器内存的最大采购方。HBM（高带宽内存）是 DRAM 的一种专用形式，对 AI 加速 GPU 尤为关键，这有助于解释为何随着 AI 训练和推理工作负载的扩展，内存需求会如此急剧上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flash_memory">Flash memory - Wikipedia</a></li>
<li><a href="https://www.crucial.com/articles/for-businesses/consumer-ssds-vs-enterprise-ssds">Consumer vs. Enterprise SSDs: What’s the Difference</a></li>
<li><a href="https://medium.com/@junyoungshin0122/the-evolution-toward-high-bandwidth-memory-hbm-601d38ce2917">Why Memory Matters: The Role of DRAM, NAND Flash, and HBM in Modern Computing | by June_0 | Medium</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#NAND Flash`, `#Cloud Infrastructure`, `#AI Hardware`, `#Memory Market`

---

<a id="item-5"></a>
## [（新闻稿）苹果推出搭载 M5 Max 和 M5 Ultra 的新款 Mac Studio](https://www.techpowerup.com/351920/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra) ⭐️ 7.5/10

苹果发布搭载 M5 Max 和 M5 Ultra 芯片的新款 Mac Studio，配备高达 512 GB 统一内存，并号称 AI 性能提升 4.3 倍，可在本地设备上运行大型语言模型。

rss · TechPowerUp News · 8月25日 13:51

**标签**: `#apple`, `#hardware`, `#M5 Ultra`, `#on-device AI`, `#local LLM inference`

---

<a id="item-6"></a>
## [富士通 Monaka CPU：144 核 Arm 服务器芯片，采用 chiplet 缓存与双 256-bit SVE2](https://www.tomshardware.com/pc-components/cpus/fujitsus-monaka-cpu-stacks-its-entire-cache-on-a-separate-5nm-die-and-narrows-to-256-bit-sve2) ⭐️ 7.5/10

在 2026 年 8 月 24 日的 Hot Chips 大会上，富士通公布了其 144 核 Monaka Arm 服务器 CPU 的详细规格，确认采用双 256-bit SVE2 矢量单元（相比前代 A64FX 的 512-bit SVE 有所收窄），并将全部缓存放在独立的 5nm 芯片上以 chiplet 形式封装，350W 和 500W 型号计划于 2027 年推出。 Monaka 是富士通首款采用 chiplet 设计的产品，标志着其从 A64FX（曾驱动富岳超算）开创的超宽矢量架构转向新方向。256-bit SVE2 的收窄反映了 Arm 生态正从纯 HPC 向 AI 和云计算等更广泛工作负载拓展的趋势。 独立的 5nm 缓存芯片使富士通能够独立优化计算芯片和缓存芯片，有望提升良率与设计灵活性。从 512-bit SVE 缩减到双 256-bit SVE2，使每核峰值矢量性能减半，但换来了更好的能效和更广泛的应用兼容性。

rss · Tom's Hardware · 8月26日 13:30

**背景**: 富士通的 A64FX 是首款实现 Arm 可扩展矢量扩展（SVE）的处理器，曾驱动日本富岳超算，在 2020 至 2022 年间登顶 TOP500。SVE2 是其继任扩展，新增了机器学习和 DSP 等更广泛的数据处理指令。Chiplet 设计是现代 CPU 越来越常见的方法，将多个小芯片集成在一个封装内，以提高制造良率、降低成本并允许混用不同工艺节点——Monaka 在计算芯片之外使用 5nm 缓存芯片正是这种取舍的典型案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fujitsu_A64FX">Fujitsu A64FX - Wikipedia</a></li>
<li><a href="https://chipsandcheese.com/p/hot-chips-2026-fujitsus-monaka-cpu">Hot Chips 2026: Fujitsu’s Monaka CPU - by Chester Lam</a></li>
<li><a href="https://anysilicon.com/the-ultimate-guide-to-chiplets/">The Ultimate Guide to Chiplets - AnySilicon</a></li>

</ul>
</details>

**标签**: `#fujitsu`, `#monaka`, `#hot-chips-2026`, `#arm`, `#server-cpu`, `#chiplet-design`, `#sve2`

---

<a id="item-7"></a>
## [OXMIQ 在 Hot Chips 2026 上阐述高带宽闪存的有限应用场景](https://www.tomshardware.com/pc-components/ssds/hot-chips-2026-high-bandwidth-flash-promises-massive-bandwidth-and-capacity-but-its-usability-is-extremely-limited-new-memory-format-strikes-a-balance-between-hbm-and-nand-flash) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，OXMIQ 展示了高带宽闪存（HBF）的应用场景分析。HBF 是一种介于 HBM 和 NAND 闪存之间的新型内存格式，但此次展示显著收窄了 HBF 真正具有实用价值的应用范围。 HBF 代表了内存层次结构中一个潜在的新层级，可能改变 AI 加速器和高性能计算系统的设计方式，尤其是在内存带宽成为关键瓶颈的 AI 推理工作负载中。然而，OXMIQ 对有限应用场景的坦诚评估凸显了将基于 NAND 的存储级内存集成到传统上针对类 DRAM 性能优化的系统中所面临的实际挑战。 HBF 基于 TSV 堆叠的 NAND（最高 16 层堆叠）并通过 UCIe 互连，提供高达 3 TB/s 的带宽和每模块 512 GB 的容量——在容量上远超 HBM，但性能较低且具有非易失性。OXMIQ 的展示重点在于识别 HBF 独特的带宽/容量权衡优于 HBM 或传统 SSD 的窄交集工作负载。

rss · Tom's Hardware · 8月26日 13:00

**背景**: 现代计算中的内存层次结构从快速、昂贵、易失的 DRAM（包括用于 GPU 和 AI 加速器的 HBM——高带宽内存）一直延伸到较慢、便宜、非易失的 NAND 闪存存储（用于 SSD）。HBM 通过使用硅通孔（TSV）堆叠 DRAM 裸片来提供非常高的带宽，但其容量有限且成本较高；NAND 闪存则可以低成本提供海量容量，但带宽要低得多。由 Sandisk 和 SK hynix 联合开发并于 2026 年 8 月正式发布的高带宽闪存（HBF）试图通过将 HBM 风格的 TSV 堆叠技术应用于 NAND 裸片来弥合这一差距。OXMIQ 是一家通过其 OxCore 平台构建可授权 AI 计算架构的初创公司，于 2026 年 7 月完成了 3500 万美元的 A 轮融资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie">New HBF spec outlines tech that can give GPUs terabytes of ...</a></li>
<li><a href="https://www.businesswire.com/news/home/20260701241910/en/OXMIQ-Raises-$35-Million-to-Scale-OxCore-Architecture">OXMIQ Raises $35 Million to Scale OxCore™ Architecture</a></li>

</ul>
</details>

**标签**: `#memory-systems`, `#hardware-architecture`, `#HotChips`, `#HBM`, `#NAND-flash`

---

<a id="item-8"></a>
## [Arm 在 Hot Chips 展示 AGI 服务器 CPU：136 核、UCIe Chiplet 互联](https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-arm-details-agi-server-cpu-with-two-70-core-n3p-chiplets-touts-2-tb-s-ucie-fabric-link-and-12-channel-memory-controller) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，Arm 披露了其 AGI 服务器 CPU 的更多细节：该处理器集成两个采用台积电 N3P 工艺制造的 70 核 chiplet，总计最高 136 核，通过 2 TB/s 的 UCIe 互连总线连接，并配备 12 通道内存控制器。不过，Arm 并未公布任何性能基准测试数据。 这一发布标志着 Arm 正式进军长期由 Intel 和 AMD 等 x86 厂商主导的 AI/数据中心服务器 CPU 市场，并利用基于 chiplet 的可扩展性和开放式互连标准。大量核心数、海量内存带宽和高带宽 die-to-die 互连的组合，是专门为 AI 训练和推理工作负载而设计的。 该设计依赖 UCIe——一种用于 die-to-die 通信的开放式行业标准，允许来自不同厂商的 chiplet 在同一封装内互操作。台积电 N3P 是其 3nm 级 FinFET 工艺的性能增强版本，已于 2024 年末进入大规模量产，在功耗、性能和面积方面均优于基础 N3 节点。

rss · Tom's Hardware · 8月26日 11:00

**背景**: 基于 chiplet 的架构将处理器拆分为多个较小的 die，并集成在同一个封装内，而不是将所有功能都构建在单个大型单片 die 上，从而提高了良率、降低了成本，并实现了更灵活的扩展。UCIe（Universal Chiplet Interconnect Express，通用小芯片互联标准）是定义这些 chiplet 在封装内如何相互通信的开放标准，目前已是 3.0 版本。Arm 的 AGI（这是一个品牌名称，并非指通用人工智能）是面向超大规模和 AI 工作负载的服务器级 CPU 产品系列，旨在与 AMD 的 EPYC 和 Intel 的 Xeon 等产品竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.uciexpress.org/specifications">Specifications | UCIe Consortium</a></li>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_3nm">3nm Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://anysilicon.com/the-ultimate-guide-to-chiplets/">The Ultimate Guide to Chiplets - AnySilicon</a></li>

</ul>
</details>

**标签**: `#Arm`, `#server CPU`, `#chiplets`, `#UCIe`, `#AI hardware`, `#Hot Chips`

---

<a id="item-9"></a>
## [EPA 拟取消数据中心空气污染许可证的公众意见征询要求](https://www.tomshardware.com/tech-industry/data-centers/u-s-govt-moves-to-suppress-pushback-on-data-centers-by-removing-requirements-for-public-input-on-pollution-epa-change-would-allow-air-pollution-permits-without-publicizing-them) ⭐️ 7.5/10

美国环保署拟修改法规，取消各州在签发空气污染许可证时必须征询公众意见的要求，这一变化尤其会影响 AI 数据中心及其他大型工业设施的许可审批流程。 这一监管变化可能通过简化许可流程来加速 AI 数据中心的建设，但同时也会削弱社区对这些高能耗设施环境影响的监督能力。随着谷歌和微软等科技巨头的 AI 相关排放持续飙升，降低空气质量许可的透明度引发了人们对 AI 扩张与环境保护之间问责机制的担忧。 此次拟议修改针对的是《清洁空气法》第五章（Title V）运营许可证，该许可证适用于大型工业设施，并提供了一套统一的空气质量法规。值得注意的是，这一监管变化出台之际，数据中心的能源和水资源消耗正因 AI 工作负载而快速增长，而直触芯片冷却和浸没式冷却等新技术正作为降低资源使用的方式出现。

rss · Tom's Hardware · 8月26日 10:00

**背景**: 《清洁空气法》第五章（Title V）建立了一套针对大型空气污染工业源的联邦运营许可制度，将所有适用的空气质量要求整合到一份单一文件中，并要求在签发或修改许可证时进行公示和征求公众意见。AI 数据中心由于训练和推理工作负载需要大量能源用于供电和冷却，属于这些空气质量法规的监管范围，因为其备用发电机和其他现场电力基础设施会产生排放。大型科技公司已报告称，数据中心因 AI 需求而增长的能源消耗直接导致了排放上升，使这些设施的环境许可审批过程成为公众日益关注的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.epa.gov/title-v-operating-permits/basic-information-about-operating-permits">Basic Information about Operating Permits - US EPA</a></li>
<li><a href="https://www.npr.org/2024/07/12/g-s1-9545/ai-brings-soaring-emissions-for-google-and-microsoft-a-major-contributor-to-climate-change">Google and Microsoft report growing emissions as they... : NPR</a></li>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#EPA regulation`, `#environmental policy`, `#government policy`

---

<a id="item-10"></a>
## [三星在 Hot Chips 2026 发布内置逻辑单元的 LPDDR5X-PIM](https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth) ⭐️ 7.5/10

三星在 Hot Chips 2026 大会上发布了业界首款 LPDDR5X-PIM，将处理逻辑直接集成到低功耗内存中，以加速 AI 推理负载。公司声称这款新内存在 AI 推理性能上比标准 LPDDR5X 快 3.01 倍，带宽高达 8 倍。 这标志着三星将存内计算（PIM）技术从高带宽内存（HBM）扩展到广泛用于移动和边缘设备的 LPDDR5X 标准。通过直接解决内存带宽瓶颈，该技术有望让智能手机、笔记本电脑和边缘硬件在不依赖云端连接的情况下，实现更强大的端侧 AI 推理。 LPDDR5X 是智能手机、平板和笔记本电脑常用的低功耗 DRAM 标准，因此 PIM 在这一层级的应用对功耗敏感的 AI 工作负载尤为相关。三星此前已为数据中心应用出货过 HBM-PIM，因此此次发布代表该架构向移动和边缘平台的迁移，但实际的生态系统支持（编译器、运行时、操作系统集成）仍有待观察。

rss · Tom's Hardware · 8月25日 18:31

**背景**: 存内计算（PIM）是一种将计算单元放置在内存阵列附近或内部以降低数据在内存与处理器之间搬运的能耗和延迟的架构方法，这一问题被称为"内存墙"。三星此前已在服务器的 HBM 堆栈中商用化 PIM 技术。LPDDR5X 是低功耗 DDR 内存的最新一代，通常用于电池供电的设备，对能效要求极为严格。将 PIM 引入 LPDDR5X 瞄准的是在手机和边缘设备上本地运行 AI 模型日益增长的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth">Hot Chips 2026: Samsung makes LPDDR 5 X smart... | Tom's Hardware</a></li>
<li><a href="https://www.servethehome.com/samsung-lpddr5x-pim-at-hot-chips-2026/">Samsung LPDDR 5 X- PIM at Hot Chips 2026 - ServeTheHome</a></li>
<li><a href="https://en.wikipedia.org/wiki/LPDDR">LPDDR - Wikipedia</a></li>

</ul>
</details>

**标签**: `#memory-architecture`, `#processing-in-memory`, `#samsung`, `#AI-inference`, `#hardware`

---

<a id="item-11"></a>
## [英特尔 Wildcat Lake：采用 UCIe 芯粒互连的 18A 入门级芯片](https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-intel-details-cutting-edge-tech-in-entry-level-wildcat-lake-value-focused-18a-chips-necessitated-ucie-integration) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，英特尔详细介绍了其 Wildcat Lake（品牌名为 Intel Core Series 3）入门级笔记本 SoC，该芯片源自基于 Panther Lake 的 Core Ultra Series 3 架构，并采用英特尔最先进的 18A 工艺节点结合 UCIe 芯粒互连技术，目标瞄准预算级笔记本市场。 这一举措意义重大，因为它表明英特尔正致力于将其最先进的封装和工艺技术扩展到预算级产品线，而在这一细分市场中，成本限制通常迫使厂商在最先进特性上做出妥协。在入门级芯片中使用 UCIe 标志着基于芯粒的设计正在变得主流化，不再仅限于高端产品，这可能重塑与 AMD 和 高通在价值型笔记本市场的竞争格局。 Wildcat Lake 的设计目标是优先广泛部署当前一代的 CPU、显卡、AI、内存、安全和连接功能，而非追求最高的功能密度。鉴于 18A 是英特尔旨在从台积电手中夺回制造领先地位的成败关键代工技术，将 UCIe 这一标准化芯粒互连集成到预算级芯片中尤为引人注目。

rss · Tom's Hardware · 8月25日 15:45

**背景**: UCIe（通用芯粒互连 express）是一项开放的行业标准，使来自不同厂商的芯粒能够在同一封装内无缝通信，从而促进模块化芯片设计。英特尔的 18A 工艺节点是该公司最先进的制造技术，采用了 RibbonFET 环栅晶体管和 PowerVia 背面供电技术，被广泛视为英特尔夺回与台积电代工竞争力的关键赌注。基于芯粒的架构将单片芯片拆分为更小的专用裸片，这些裸片可以混合搭配，从而提高良率和灵活性并降低成本——这种设计理念正在整个半导体行业中普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.uciexpress.org/">Home | UCIe Consortium</a></li>
<li><a href="https://abhs.in/blog/intel-18a-foundry-tsmc-rival-us-chip-independence-2026">Intel 18 A : The Make-or-Break Foundry Bet That Could End...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#UCIe`, `#18A process node`, `#chiplets`, `#Hot Chips 2026`

---

<a id="item-12"></a>
## [谷歌在 Hot Chips 2026 大会发布第八代 TPU 芯片家族](https://www.servethehome.com/googles-tpuv8s-for-training-and-inference-at-hot-chips-2026/) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，谷歌公布了其第八代 TPU 芯片家族，其中包括面向训练负载的 TPU 8t 和面向推理负载的 TPU 8i，进一步推进了谷歌的自研 AI 芯片路线图。 谷歌是为数不多仍坚持自研训练芯片的超大规模云服务商之一，因此每一代 TPU 的发布都会对竞争激烈的 AI 硬件市场格局以及谷歌云提供差异化 AI 基础设施的能力产生重要影响。 谷歌在新一代产品中将训练（TPU 8t）和推理（TPU 8i）拆分为独立型号，体现了面向特定工作负载定制加速器的趋势，不过 ServeTheHome 这篇文章仅为预告性质，并未披露制程工艺、HBM 容量或互联带宽等详细规格。

rss · ServeTheHome · 8月26日 00:15

**背景**: TPU（Tensor Processing Unit，張量处理单元）是谷歌自研的 ASIC 芯片，专门优化用于深度学习（如 CNN 和大语言模型）中占主导地位的大规模矩阵乘法运算。Hot Chips 是一年一度的芯片设计研讨会，2026 年于斯坦福大学举办（8 月 23 日至 25 日），芯片设计者在此向技术受众展示架构细节。像谷歌、AWS 和微软 Azure 这样的超大规模云服务商运营着全球规模的数据中心，并且越来越多地自研加速器以减少对英伟达等第三方 GPU 的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hotchips.org/">Hot Chips</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Google TPU`, `#AI hardware`, `#Hot Chips 2026`, `#machine learning`, `#data center accelerators`

---

<a id="item-13"></a>
## [微软将在 Hot Chips 2026 揭秘 Maia 200 AI 加速器](https://www.servethehome.com/microsofts-maia-200-accelerator-at-hot-chips-2026/) ⭐️ 7.5/10

微软将在 Hot Chips 2026 大会上深入披露其第二代 Maia 200 AI 推理加速器的架构细节，这是该芯片于 2026 年 1 月发布并部署于 Azure 之后的进一步技术公开。 此次演讲表明微软致力于通过自研 AI 芯片来降低对 NVIDIA 的依赖，而 Hot Chips 是深度微架构细节披露的首选平台，将让竞争对手和客户更清晰地了解微软的硬件路线图。 Maia 200 采用台积电 3nm 工艺制造，配备原生 FP8/FP4 Tensor Core、216GB HBM3e 显存（带宽达 7 TB/s）、272MB 片上 SRAM，FP4 算力约 10 PFLOPS，功耗 750W；微软声称其总拥有成本（TCO）比其机队中其他加速器降低 30%，能耗降低 15%。

rss · ServeTheHome · 8月25日 22:45

**背景**: Maia 200 是微软首款专为推理（即 AI 模型的生产部署阶段）而非训练设计的自研 AI 加速器，是初代 Maia 100 的继任者，体现了微软在 AI 基础设施领域的垂直整合战略。Hot Chips 是每年举办的专注于高性能芯片架构的研讨会，传统上各公司会在此披露包括流水线设计、存储层次结构和互连在内的深度微架构信息。该会议深受硬件工程师、研究人员和行业分析师的欢迎，他们寻求超越市场宣传的深度技术洞察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/">Maia 200: The AI accelerator built for inference - The ...</a></li>
<li><a href="https://www.hotchips.org/">Hot Chips</a></li>
<li><a href="https://aimagazine.com/news/microsoft-unveils-maia-200-ai-accelerator">Microsoft: How Maia 200 Accelerator Addresses AI Bottlenecks</a></li>

</ul>
</details>

**标签**: `#AI-hardware`, `#Microsoft`, `#Hot-Chips`, `#AI-accelerators`, `#custom-silicon`

---

<a id="item-14"></a>
## [Cerebras 在 2026 年 Hot Chips 大会上探讨将 WSE 扩展至机架规模](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/) ⭐️ 7.5/10

Cerebras 在 2026 年 Hot Chips 大会上宣布，其下一代晶圆级引擎（WSE）将通过全新的 Nexus 架构实现机架级部署，标志着 AI 加速器规模化部署迈出了重要一步。

rss · ServeTheHome · 8月25日 22:15

**标签**: `#Cerebras`, `#AI hardware`, `#wafer-scale`, `#Hot Chips 2026`, `#rack-scale architecture`

---

<a id="item-15"></a>
## [NVIDIA 将 Groq 3 LPU 集成至 Vera Rubin 实现异构 AI 计算](https://www.servethehome.com/nvidias-groq-3-lpu-accelerators-for-heterogeneous-ai-compute-at-hot-chips-2026/) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，NVIDIA 详细介绍了如何将 Groq 3 LPU 集成到 Vera Rubin 集群中，作为异构计算架构的一部分，专门针对 LLM 推理解码阶段的低延迟需求。该 LPX 系统基于 256 颗互联的 LPU 构建，并与 Vera Rubin NVL72 平台协同设计，被定位为面向智能体 AI 工作负载的机架级推理加速器。 这一声明标志着 NVIDIA 向异构 AI 计算的战略转变，承认 GPU 单独使用无法最优地服务于推理的每个阶段，并且像 LPU 这样的专用加速器是逐 token 解码阶段所必需的。这验证了将 prefill 和 decode 工作负载拆分到不同硅芯片上的行业趋势，可能会重塑超大规模云服务商和企业设计 AI 基础设施的方式。 NVIDIA 声称 Groq 3 LPX 可实现每兆瓦推理吞吐量高达 35 倍的提升，并为万亿参数模型带来 10 倍的收入增长机会。LPU 与 GPU 的不同之处在于将模型权重存储在片上 SRAM 中，并采用确定性执行调度，从而消除 GPU 在 token 生成过程中遇到的内存等待停顿。256 颗 LPU 组成的 LPX 机架与 Vera Rubin GPU 并行工作，而非取代它们。

rss · ServeTheHome · 8月25日 21:45

**背景**: LLM 推理分为两个不同的阶段：prefill 阶段处理整个输入提示以构建 KV 缓存，属于计算密集型；decode 阶段则逐个生成输出 token，受内存带宽限制。LPU（语言处理单元）是 Groq 设计的推理专用芯片，将模型权重存储在片上 SRAM 中，并采用确定性调度避免内存延迟停顿，因此特别适合 decode 工作负载。LPU 推理引擎通常与基于 GPU 的训练和 prefill 系统并行使用，而非替代它们，这也是结合两种加速器的异构架构日益受到关注的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/nvidias-groq-3-lpu-accelerators-for-heterogeneous-ai-compute-at-hot-chips-2026/">NVIDIA’s Groq 3 LPU Accelerators for Heterogeneous AI Compute ...</a></li>
<li><a href="https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform">Inside NVIDIA Groq 3 LPX: The Low-Latency Inference ...</a></li>
<li><a href="https://groq.com/blog/the-groq-lpu-explained">What is a Language Processing Unit? | Groq is the premier ...</a></li>
<li><a href="https://redis.io/blog/prefill-vs-decode/">Prefill vs Decode : LLM Inference Phases Explained</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Groq`, `#LPU`, `#Hot Chips 2026`, `#AI inference`, `#heterogeneous compute`, `#Vera Rubin`

---

<a id="item-16"></a>
## [全球海洋表面温度受气候变化影响创历史新高](https://www.solidot.org/story?sid=85198) ⭐️ 7.3/10

根据欧洲哥白尼气候变化服务中心的数据，除极地外全球海洋表面平均温度在周六达到了 21.1°C，略高于 2024 年 3 月创下的 21.09°C 的纪录。科学家警告，当前的厄尔尼诺现象尚未达到峰值，可能成为数个世纪以来最强的一次。 海洋温度破纪录会带来广泛影响，包括加剧极端天气、加速海平面上升以及损害海洋生态系统。由于海洋吸收了大气中绝大部分多余热量，这些温度纪录是衡量全球气候变化速度和严重程度的关键指标。 该温度数据基于海面以下 10 米的海水温度测量，综合利用了浮标、船舶和卫星的数据。全球海水平均温度的年度峰值通常出现在 3 月或 4 月，对应南半球夏季结束，因为南半球的海洋面积远大于北半球。

rss · Solidot · 8月26日 07:45

**背景**: 厄尔尼诺是一种气候现象，其特征是赤道中东太平洋海面温度异常升高，由信风减弱驱动。它通常每 2 到 7 年发生一次，会扰乱全球气候模式，往往导致全球气温飙升。哥白尼气候变化服务中心是欧盟的地球观测项目，利用卫星观测和全球现场测量数据提供权威的气候信息。

**标签**: `#AI-hardware`, `#OpenAI`, `#Nvidia`, `#climate-science`, `#China-AI`

---

<a id="item-17"></a>
## [AWS 收购 DuckDB](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 7.0/10

AWS 收购了 DuckDB 背后的商业实体 DuckLabs，但开源的 DuckDB 项目仍由非营利组织 DuckDB 基金会管控。

hackernews · onderkalaci · 8月26日 12:59 · [社区讨论](https://news.ycombinator.com/item?id=49448321)

**标签**: `#aws`, `#duckdb`, `#acquisition`, `#open-source`, `#databases`

---

<a id="item-18"></a>
## [Qwen3.8-Flash-Next：1760 亿参数 MoE，Qwen4 架构预览](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 7.0/10

通义千问发布了 Qwen3.8-Flash-Next，作为 Qwen4 架构的实验性预览版本：这是一款多模态超稀疏 MoE 模型，总参数量达 1760 亿（含 510 亿 N-gram 嵌入表），但每个 token 仅激活 60 亿参数；据官方称其性能超越了此前的 27B 模型，而量化后约 73GB 即可装入 128GB 硬件。 此次发布表明，将超稀疏 MoE 与 GDN + QSA 混合注意力设计相结合，可以用小型模型的算力成本获得千亿级模型的品质，有望重塑自托管 AI 的经济性，让高端推理能够在 Mac Studio 和 AMD Strix Halo 等消费级硬件上普及。 该模型以 FP8 精度发布，开箱即支持 vLLM 和 SGLang，并已集成到 Unsloth Desktop 中。其 60 亿的激活参数量绕过了内存带宽瓶颈——这正是同等消费级 GPU 拖累稠密 27B 级模型的核心原因，从而即使在单台 128GB 主机上，也能以 Q3/Q4 量化进行较长上下文推理。

hackernews · tosh · 8月26日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=49448210)

**背景**: 混合专家（MoE）模型将权重划分为多个「专家」子网络，由可学习的路由器在每个 token 上仅激活其中一小部分专家子网络，从而大幅降低计算量，同时显存占用仍与总参数成正比；此前的稀疏 MoE 设计如 Mixtral 8x7B 已证明此模式能击败更大的稠密模型。本次发布的架构还以门控 DeltaNet（GDN）与 QSA 的混合注意力机制替代纯 softmax 注意力，进一步削减长上下文场景下的显存与算力开销。Qwen 将 Qwen3.8-Flash-Next 定位为支撑下一代 Qwen4 模型族的实验性基石。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next-FP8">Qwen/ Qwen 3 .8- Flash -Next-FP8 · Hugging Face</a></li>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 .8- Flash -Next | vLLM Recipes</a></li>
<li><a href="https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next">Qwen 3 .8- Flash -Next - SGLang Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，尤其兴奋地关注在 Strix Halo 和 128GB Mac 上的自托管部署，因为 ~73GB 的量化体积对此类硬件完全可行。用户关心它能否匹配更大尺寸 Qwen3.8 变体的推理深度，也有人询问它是否继承了 Qwen3.8-27B 和 GLM 5.2 上已观察到的高冗长度和累计输入 token 成本问题。整体情绪乐观但仍保持谨慎，期待在生产负载上的实测基准验证。

**标签**: `#qwen`, `#llm`, `#model-release`, `#cost-efficiency`, `#self-hosting`

---

<a id="item-19"></a>
## [以色列设立并资助虚假美国智库，试图操纵 AI 进行宣传](https://www.theguardian.com/world/2026/aug/26/fake-thinktank-israel-ai-propaganda) ⭐️ 7.0/10

OpenAI 的反滥用工作披露，一个由以色列资助的虚假美国智库被用于试图影响 AI 系统，以达到宣传目的。

hackernews · n1b0m · 8月26日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=49447600)

**标签**: `#AI safety`, `#disinformation`, `#state-sponsored-actors`, `#propaganda`, `#AI ethics`

---

<a id="item-20"></a>
## [XCorp 向 XCancel 和 Nitter 发出停止侵权通知函](https://news.ycombinator.com/item?id=49446210) ⭐️ 7.0/10

X 公司已向 Nitter 和 XCancel 发出停止侵权通知函，导致这两个支持免登录、保护隐私访问 Twitter/X 内容的替代前端被关闭。

hackernews · mobilio · 8月26日 09:34

**标签**: `#twitter`, `#nitter`, `#open-web`, `#platform-policy`, `#decentralization`

---