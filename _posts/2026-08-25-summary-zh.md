---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 95 条内容中筛选出 20 条重要资讯。

---

1. [英特尔 Diamond Rapids Xeon 7：256 个 P 核、1.28 GB LLC、UCIe-S](#item-1) ⭐️ 8.5/10
2. [SK hynix 将混合键合推迟至 HBM5，775 微米堆叠厚度天花板逼近](#item-2) ⭐️ 8.5/10
3. [IBM 推出 2nm 11 核双指令集大型机处理器](#item-3) ⭐️ 8.5/10
4. [京都大学展示 600°C 碳化硅晶体管，采用标准离子注入工艺](#item-4) ⭐️ 8.5/10
5. [微软画图和照片应用秘密嵌入无法关闭的 GUID 水印](#item-5) ⭐️ 8.0/10
6. [AMD x86 市场份额创纪录达 30.7%，Intel 跌至 1995 年以来最低](#item-6) ⭐️ 7.5/10
7. [英特尔详解 Crescent Island 数据中心 GPU：32 个 Xe3P 核心、最高 480GB LPDDR5X 显存](#item-7) ⭐️ 7.5/10
8. [mVolt+ v0.36 无需硬件改装即可突破 RTX 50 系列功耗限制](#item-8) ⭐️ 7.5/10
9. [三星确认 HBM4E 内存速率达 16 Gbps 每引脚](#item-9) ⭐️ 7.5/10
10. [台湾起诉九人涉嫌走私英伟达 B300 GPU 至中国](#item-10) ⭐️ 7.5/10
11. [AMD 在 Hot Chips 2026 大会揭晓 MI400 GPU 架构](#item-11) ⭐️ 7.5/10
12. [Arm 在 Hot Chips 2026 发布首款完整数据中心 CPU——AGI](#item-12) ⭐️ 7.5/10
13. [富士通基于 Arm 架构的 Monaka 数据中心 CPU 亮相 Hot Chips 2026](#item-13) ⭐️ 7.5/10
14. [皮尤研究：ChatGPT 发布后逾三分之一英文网页带有 AI 痕迹](#item-14) ⭐️ 7.3/10
15. [整个旧金山市被重建为可交互的 3D 电子游戏](#item-15) ⭐️ 7.0/10
16. [RISC-V 十六年：从模块化 ISA 到 Hot Chips 2026 上的标准化平台](#item-16) ⭐️ 7.0/10
17. [Hot Chips 大会聚焦面向 AI 的演进型内存架构](#item-17) ⭐️ 7.0/10
18. [天工 Ultra 人形机器人百米赛跑超越最快人类](#item-18) ⭐️ 7.0/10
19. [Quintessent 开始提供单芯片 DWDM 梳状激光器样片](#item-19) ⭐️ 7.0/10
20. [LG 原生 1,000Hz 1080p 电竞显示器售价高达 1000 美元——25 英寸 UltraGear 25G590B 开启预售](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [英特尔 Diamond Rapids Xeon 7：256 个 P 核、1.28 GB LLC、UCIe-S](https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib) ⭐️ 8.5/10

在 Hot Chips 2026 大会上，英特尔公布了其下一代 Xeon 7「Diamond Rapids」服务器处理器，每个插槽最多配备 256 个「Panter Cove」P 核和 1.28 GB 末级缓存（LLC），采用英特尔 18A-P 工艺节点制造。该芯片以 UCIe-S 小芯片互连取代了英特尔传统的 EMIB，并新增 AVX 10.2 指令集与 PCI-Express Gen 6 I/O，面向企业级智能体（agentic AI）工作负载，计划于 2027 年正式发布。 Diamond Rapids 标志着英特尔多年来最激进的服务器 CPU 重新设计，直接挑战 AMD EPYC 和基于 ARM 的服务器芯片在多核数据中心市场的地位。256 核、1.28 GB LLC 与 PCI-Express Gen 6 的组合，使该产品定位于 AI 推理和智能体 AI 工作负载——在这些场景中，内存带宽和缓存容量是关键瓶颈。 该 MCM 封装包含 16 个核心 chiplet，组成 4 个基础 tile（每个 tile 64 核），通过 2 个 Fabric Hub Tile 和一个集中式服务器 I/O 晶圆（sIOD）互连，与 AMD 的 CCD/sIOD 分解设计理念非常接近。从英特尔专有的 EMIB 硅桥转向开放的 UCIe-S 标准，表明英特尔正与行业级 chiplet 互操作性对齐，而非继续维持封闭的互连技术。

rss · Tom's Hardware · 8月24日 21:07

**背景**: UCIe（Universal Chiplet Interconnect Express，通用小芯片互连快车）是一项开放的行业标准，最初于 2022 年 3 月发布，并于 2025 年 8 月更新到 3.0 版本，定义了标准化的裸片间（die-to-die）互连，允许不同厂商的 chiplet 在同一封装中混合使用。英特尔的 EMIB（Embedded Multi-die Interconnect Bridge，嵌入式多裸片互连桥）是一项专有的 2.5D 硅桥技术，于 2018 年首次出现，曾用于 Kaby Lake-G 和早期 Xeon tile 等产品。AVX 10.2 是英特尔高级矢量扩展指令集（AVX）的最新演进，新增了转换指令、饱和运算指令以及浮点比较指令，可加速 AI、科学计算和密码学工作负载。「P 核」（Performance core）指英特尔的性能核，针对单线程吞吐量优化，区别于更注重能效的 E 核（Efficient core）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UCIe">UCIe - Wikipedia</a></li>
<li><a href="https://semiwiki.com/semiconductor-manufacturers/intel/298674-intels-emib-packaging-technology-a-deep-dive/">Intel ’s EMIB Packaging Technology – A Deep Dive - SemiWiki</a></li>
<li><a href="https://hugeonotation.github.io/pblog/2024/11/03/avx10_2_new_instructions.html">AVX-10.2's New Instructions</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Xeon`, `#data-center`, `#HotChips2026`, `#server-CPUs`

---

<a id="item-2"></a>
## [SK hynix 将混合键合推迟至 HBM5，775 微米堆叠厚度天花板逼近](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling) ⭐️ 8.5/10

在 Hot Chips 2026 大会上，SK hynix 披露 HBM 立方体堆叠的总厚度已达到 775 微米的硬性上限——即 300mm 逻辑晶圆的标准厚度——这迫使公司将混合键合技术从 HBM4e 推迟到 HBM5，同时在 Nvidia Rubin 代际产品中继续采用 MR-MUF 封装工艺。 这是 AI 内存供应链的一个关键转折点：775 微米的上限直接限制了未来 HBM 堆叠的高度增长空间，意味着每一代产品必须在相同的垂直空间内塞入更大容量，而混合键合的推迟意味着热-机械瓶颈将在又一个产品周期内持续存在，影响每一家 AI 加速器供应商。 775 微米的限制并非随意设定，而是由 300mm 标准晶圆厚度决定——这定义了薄化晶圆在不发生破裂的情况下能承受的翘曲极限；MR-MUF（大规模回流模塑底填）通过焊料回流加上保护性模塑底填实现芯片互连并改善散热，而混合键合则通过金属与绝缘体直接键合实现更高的 I/O 密度和更低的热阻，但在量产中仍面临良率和吞吐量的挑战。

rss · Tom's Hardware · 8月24日 17:55

**背景**: 高带宽内存（HBM）是驱动现代 AI GPU 和加速器的堆叠式 DRAM，通过硅通孔（TSV）垂直堆叠多颗 DRAM 芯片，提供远超传统 GDDR 的带宽。MR-MUF 是 SK hynix 专有的大规模回流-模塑底填工艺，被广泛认为是 HBM 堆叠领域的业界最佳方案，因为它相比传统热压键合能显著改善散热和堆叠刚性。混合键合是下一代演进方向，通过铜-铜或金属-电介质直接键合（无需焊料凸点）实现更精细的间距互连和更低的热阻，但其所需的极端表面平整度和洁净室精度迄今限制了其在 HBM 大规模量产中的应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.skhynix.com/rulebreaker-revolutions-mr-muf-unlocks-hbm-heat-control/">Rulebreakers' Revolutions: MR - MUF Unlocks HBM Heat Control</a></li>
<li><a href="https://www.mdpi.com/2079-9292/14/13/2682">Thermal Issues Related to Hybrid Bonding of 3D-Stacked High ...</a></li>
<li><a href="https://chiplet-marketplace.com/library/wiki/mr-muf-mass-reflow-molded-underfill">MR - MUF ( Mass Reflow Molded Underfill ) - Chiplet Marketplace Wiki</a></li>

</ul>
</details>

**标签**: `#HBM`, `#SK-hynix`, `#hybrid-bonding`, `#semiconductors`, `#AI-infrastructure`

---

<a id="item-3"></a>
## [IBM 推出 2nm 11 核双指令集大型机处理器](https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores) ⭐️ 8.5/10

IBM 在 Hot Chips 2026 上公布了这款 11 核处理器，其核心可在同一核心中原生执行 z/Architecture 与 AArch64 指令，芯片采用 2nm 工艺，所有核心的基础频率为 5.7GHz。该处理器面向未来的 IBM Z 和 LinuxONE 系统，是 IBM 于 2026 年 4 月与 Arm 建立合作后推出的首个处理器里程碑。 该设计可让 Arm 原生 Linux 环境与 z/OS 及 IBM Z 上的 Linux 同时运行，从而把面向云原生和 AI 的软件生态带到擅长交易处理及数据密集型工作负载的平台。企业因此有机会在同一企业级平台上运行更多工作负载，同时沿用 IBM 所强调的硬件级故障检测与恢复、加密、安全密钥管理及 AI 加速能力。 该芯片的关键实现是让每个物理核心原生执行 z/Architecture 和 AArch64，而不是为两套指令集分别配置不同类型的核心。IBM 仍将这款处理器描述为正在开发中，并计划用于未来的 IBM Z 和 LinuxONE；公告未给出上市时间、实测性能、定价或软件迁移承诺。

rss · Tom's Hardware · 8月24日 17:42

**背景**: z/Architecture 是 IBM 大型机处理器采用的 64 位 CISC 指令集架构。AArch64 是 Arm 的 64 位指令集架构，可支持 Linux 以及广泛的云端、边缘和 AI 软件。IBM Z 平台主要承担交易处理和数据密集型工作负载，并可同时运行 z/OS 与 Linux；IBM 和 Arm 于 2026 年 4 月建立了此次合作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/ibm-z-and-linuxone-dual-isa-processor-and-ai-acceleration-at-hot-chips-2026/">IBM Z and LinuxONE Dual - ISA Processor and AI... - ServeTheHome</a></li>
<li><a href="https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores">IBM's first dual - ISA core natively executes ARM and z/ Architecture in...</a></li>
<li><a href="https://www.ibm.com/support/pages/sites/default/files/2021-05/SA22-7871-10.pdf">IBM z/Architecture Reference Summary</a></li>

</ul>
</details>

**标签**: `#IBM`, `#mainframe`, `#ARM`, `#z/Architecture`, `#Hot Chips 2026`

---

<a id="item-4"></a>
## [京都大学展示 600°C 碳化硅晶体管，采用标准离子注入工艺](https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation) ⭐️ 8.5/10

京都大学的研究人员制造出一款能在 600°C（873 K）下稳定工作的碳化硅（SiC）晶体管，采用标准离子注入工艺和底栅 JFET 设计，在 400°C 时阈值电压漂移控制在 0.1 V 以内。该方案解决了长期以来阻碍 SiC 晶体管采用传统半导体工艺制造的漏电和电压漂移问题。 这一突破使得航空航天、太空、油气井下等恶劣环境所需的高温电子器件，能够利用现有商业晶圆厂中已有的离子注入设备进行生产，而无需依赖特殊的专用工艺。SiC 高温晶体管实现与现有产线兼容，将大幅降低在硅基器件无法承受的极端环境中量产电子产品的门槛。 该器件是基于碳化硅的底栅结型场效应晶体管（JFET），利用 SiC 的宽禁带特性实现热稳定性，同时采用离子注入——一种低温且广泛使用的掺杂技术——来形成有源区。底栅架构专门用于抑制栅极漏电并稳定极高温下的阈值电压，这两种失效模式通常是采用传统方法制造的 SiC 晶体管的主要问题。

rss · Tom's Hardware · 8月24日 10:30

**背景**: 碳化硅是一种宽禁带半导体材料，这意味着激发电子进入导带所需的能量远高于硅，因而具备出色的耐高温、耐高压和高频特性。离子注入是一种标准的低温掺杂工艺，通过将加速离子注入半导体来改变其电学特性，几乎是所有现代 CMOS 晶圆厂的核心工艺。底栅晶体管将栅电极置于半导体沟道下方（而非上方），在该设计中这有助于控制漏电流和阈值电压稳定性。将这些要素结合，京都大学团队让 SiC 固有的耐高温能力与主流晶圆厂可执行的工艺流程得以兼容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation">Kyoto University builds transistor that survives... | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ion_implantation">Ion implantation - Wikipedia</a></li>
<li><a href="https://ece.engin.umich.edu/stories/u-m-awarded-up-to-7-5m-to-bring-heat-tolerant-semiconductors-from-lab-to-fab">U-M awarded up to $7.5M to bring heat-tolerant semiconductors from...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#silicon-carbide`, `#high-temperature-electronics`, `#research-breakthrough`, `#hardware`

---

<a id="item-5"></a>
## [微软画图和照片应用秘密嵌入无法关闭的 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

逆向工程发现，微软画图（MS Paint）和微软照片（Photos）会在图像中嵌入包含 GUID 的不可见且无法关闭的水印，即使是通过本地 AI 模型生成或编辑的图像也不例外。该隐形水印无法关闭，用户也不会收到任何相关通知。 这对数以亿计的 Windows 用户提出了严重的隐私和匿名性担忧，因为嵌入的水印有可能通过向微软发出版权传票来识别用户身份。它也打破了用户在使用本地 AI 模型时所期望的隐私保护——用户选择本地部署通常正是为了避免向外部服务器发送数据。 可见水印可以被用户手动关闭，但隐形水印在后台静默嵌入，用户完全无法察觉，也无法通过任何设置禁用。即使使用 Stable Diffusion 等本地 AI 模型生成图像时也会被嵌入水印，这暗示在表面上离线的处理过程中仍然存在遥测或网络请求。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: GUID（全局唯一标识符）是一个 128 位的数字，用于在计算机系统中唯一标识信息，在微软软件中被广泛用于标记数据。数字水印是一种隐写术技术，将隐藏数据嵌入到图像等数字媒体中，通常用于版权保护、身份验证或取证追踪。本地 AI 图像生成指的是直接在用户自己的硬件上运行 Stable Diffusion 等模型，无需将数据发送到云服务器——用户选择本地部署通常正是出于隐私考虑和规避内容审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>
<li><a href="https://techtactician.com/beginners-guide-to-local-ai-image-generation-software/">Beginner's Guide To Local AI Image Generation Software - How ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论主要集中在隐私和匿名性问题上。评论者强调，真正的危险不在于 AI 功能本身，而在于每张图像中嵌入的唯一标识符——这可以通过版权传票被滥用，从而实现用户去匿名化，与年龄验证系统的风险类似。一些用户对 MS Paint 已从简单绘图工具演变为复杂软件表示惊讶，另一些人则认为这是互联网匿名性被侵蚀和企业监控扩张的更广泛趋势的一部分。

**标签**: `#privacy`, `#security`, `#reverse-engineering`, `#microsoft`, `#watermarking`

---

<a id="item-6"></a>
## [AMD x86 市场份额创纪录达 30.7%，Intel 跌至 1995 年以来最低](https://www.techpowerup.com/351908/amd-gains-ground-as-intel-x86-market-share-goes-back-to-1995-levels) ⭐️ 7.5/10

根据 Mercury Research 的数据，Intel 的 x86 CPU 市场份额在 2026 年第二季度跌至 69.3%，这是自 1995 年以来首次跌破 70%，同比下滑 6.5 个百分点；与此同时 AMD 攀升至创纪录的 30.7%。如果将半定制、嵌入式和物联网产品计算在内，Intel 的份额进一步降至 65.9%，AMD 则达到 34.1%，后者得益于超出预期的主机 SoC 出货量。 这是三十年来 Intel 在 x86 生态中长期主导地位最显著的削弱，反映了 AMD Zen 架构在桌面、笔记本和服务器领域成功的累积效应。这一转变标志着 PC 和数据中心竞争格局的变化，将对全行业的定价、供货决策和平台投资产生影响。 按细分市场来看，AMD 的桌面 CPU 份额达到 34.9%（同比增长 2.7 个百分点），服务器份额达到 34.5%（同比增长 7.3 个百分点），笔记本份额跃升至 28.9%（同比增长 8.4 个百分点），后者是涨幅最大的领域。AMD 已推出基于 Zen 6 架构的第六代 EPYC "Venice" 服务器处理器，而 Intel 最近在 Hot Chips 大会上公布了即将发布的 Xeon 7 "Diamond Rapids" CPU 以及面向数据中心的 "Crescent Island" GPU。

rss · TechPowerUp News · 8月24日 23:50

**背景**: x86 是 Intel 于 1978 年以 8086 处理器为基础开发的 CISC 指令集架构，此后逐渐成为 PC 和服务器市场的主导 ISA。Intel 和 AMD 是仅有的两家主要 x86 CPU 供应商；在过去二十多年中，Intel 一直占据压倒性的份额领先优势，仅在 2000 年代初期以及 2017 年之后 AMD 曾两次短暂突破 25% 的份额。Mercury Research 是按细分市场追踪 x86 CPU 出货份额的领先分析机构，其季度报告被广泛视为行业标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/systems/2026/08/21/amd-grabs-more-cpu-share-while-pricier-pcs-punish-desktop-demand/5291053">AMD grabs more CPU share while pricier PCs punish desktop demand</a></li>
<li><a href="https://ms.codes/en-ca/blogs/computer-hardware/mercury-research-cpu-market-share">Mercury Research CPU Market Share</a></li>
<li><a href="https://en.wikipedia.org/wiki/X86">x86 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#CPU`, `#AMD`, `#Intel`, `#x86`, `#market-share`

---

<a id="item-7"></a>
## [英特尔详解 Crescent Island 数据中心 GPU：32 个 Xe3P 核心、最高 480GB LPDDR5X 显存](https://www.techpowerup.com/351901/intel-details-crescent-island-graphics-32-xe3p-cores-up-to-480-gb-lpddr5x-memory) ⭐️ 7.5/10

在 2026 年 Hot Chips 大会上，英特尔详细介绍了基于 Xe3P 架构的"Crescent Island"数据中心 GPU：配备 32 个 Xe3P 核心、256 个 XMX 引擎、最高 480GB LPDDR5X 显存（ODM 配置），采用 350W 风冷 PCIe 形态，专为 AI 推理工作负载设计。 该产品使英特尔在目前由 NVIDIA 主导的 AI 推理加速器市场中成为一个有力的竞争者，其大容量 LPDDR5X 显存仅需数张卡即可在本地运行前沿开源模型。彻底移除所有图形硬件的决策表明，英特尔正战略性地选择在 AI 基础设施领域开辟利基市场，而非在传统 GPU 市场正面竞争。 XMX 引擎从原来的 4 深度脉动阵列重新设计为 16 深度处理流水线，并新增对 FP4 数据格式的支持（同时支持 FP8）。每个 Xe3P 核心包含 8 个 Vector 引擎和 8 个 XMX 引擎（总计各 256 个），还配有 1MB 寄存器文件和 512KB L1 缓存，全芯片配备 32MB 统一 L2 缓存——且完全没有任何图形输出硬件，专门面向长上下文和 Agent 类 AI 推理任务。

rss · TechPowerUp News · 8月24日 19:49

**背景**: Intel Xe 架构是一系列 GPU 设计，涵盖从集成显卡到数据中心加速器，其中 Xe3P 是针对 AI/ML 工作负载优化的变体。XMX（Xe 矩阵扩展）引擎是英特尔版本的 NVIDIA Tensor Cores——专用脉动阵列硬件，用于执行神经网络推理的核心运算矩阵乘法。LPDDR5X 是 DDR5 的低功耗版本，最初面向移动设备设计；将其用于数据中心 GPU 较为少见，因为大多数 AI 加速器（NVIDIA H100、AMD MI300）均采用 HBM（高带宽内存），不过 LPDDR5X 可以以更低的成本提供更高的容量。Hot Chips 是半导体公司发布详细芯片架构的知名年度研讨会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/intel-details-xe3p-gpu-architecture-crescent-island-gets-up-to-480gb-memory-and-350w-pcie-variant">Intel details Xe3P GPU architecture, Crescent Island gets up to 480GB memory and 350W PCIe variant - VideoCardz.com</a></li>
<li><a href="https://www.intel.com/content/www/us/en/docs/oneapi/optimization-guide-gpu/2024-1/xmx.html">Boost Matrix Multiplication Performance with Intel® Xe Matrix Extensions</a></li>
<li><a href="https://hardwaretimes.com/lpddr-vs-ddr5-vs-gddr7-what-is-the-difference/">DDR4 vs DDR5 vs LPDDR4 vs LPDDR5 vs GDDR6 vs GDDR7: What is the Difference? | Hardware Times</a></li>

</ul>
</details>

**标签**: `#Intel`, `#GPU`, `#datacenter`, `#AI infrastructure`, `#hardware`

---

<a id="item-8"></a>
## [mVolt+ v0.36 无需硬件改装即可突破 RTX 50 系列功耗限制](https://www.techpowerup.com/351867/nvidia-power-limit-bypass-rtx-5090-oc-hits-700-w-rtx-5080-up-to-680-w-no-shunt-mod-needed) ⭐️ 7.5/10

据报道，mVolt+ v0.36 更新可在无需分流电阻改装或刷新 vBIOS 的情况下，通过软件方式突破 NVIDIA RTX 50 系列显卡的功耗限制。一位 Reddit 用户在 RTX 5090 上实现了 700 W 的功耗（高于默认 575 W TDP），核心频率达到 3,127 MHz，并在 3DMark Steel Nomad 中跑出 16,523 分；另一位用户则将华硕 ROG Astral RTX 5080 OC 推至 680 W（高于默认 400 W TDP）。 这标志着极限显卡超频方法论的重大转变——此前要达到如此功耗水平，通常需要进行侵入式的硬件改装（分流电阻改造）或刷新 vBIOS，二者都会使保修失效并带来永久性风险。如果该方法得到验证，这种纯软件途径有望让更多 RTX 50 系列用户体验极限超频，同时也为 NVIDIA 在功耗限制执行和驱动层面的保护机制提出了新问题。 mVolt+ v0.36 暴露了 Blackwell 架构隐藏的电压与功耗控制选项，包括 GPU 核心与显存的独立功耗通道限制，以及 Core、XBAR、SYS 和 Video 各域的电压调节功能——这些都是 MSI Afterburner 等常规超频工具所不具备的。报道中 RTX 5090 的 3,127 MHz 频率比参考设计的 2,407 MHz 加速频率高出约 720 MHz，而 RTX 5080 的 680 W 功耗甚至超过了通过 NVIDIA 官方工具可达到的 450 W 上限。

rss · TechPowerUp News · 8月24日 12:00

**背景**: GPU 的功耗限制由 vBIOS 和驱动固件强制执行，目的是让显卡工作在其标称热设计与电气设计参数之内。分流电阻改装（shunt mod）是一种硬件改造方式，通过更换或绕过 PCB 上的电流采样电阻（分流器），使 GPU 能够从监控电路读取范围之外汲取更多功率。刷入定制版 vBIOS 也能通过软件方式达到类似效果，但同样会绕过出厂安全限制。mVolt+ 是一款第三方工具，可在底层与 NVIDIA GPU 的电压调节硬件进行交互，其 v0.36 版本专门针对 RTX 50 系列所采用的新 Blackwell 架构，解锁了此前无法访问的控制选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vgtimes.com/tech-and-hardware/165162-mvolt-v0.36-lets-geforce-rtx-50-gpus-push-past-vbios-power-limits.html">mVolt+ v0.36 Lets GeForce RTX 50 GPUs Push Past VBIOS Power...</a></li>
<li><a href="https://www.pcworld.com/article/2854038/this-nvidia-rtx-laptop-mod-unlocks-amazing-performance-dont-do-it.html">This Nvidia RTX laptop mod unlocks amazing performance. | PCWorld</a></li>
<li><a href="https://www.overclock.net/threads/tutorial-power-target-limit-hardware-mod-shunt-mod-for-titan-x-and-many-other-nvidia-gpus.1608437/">overclock .net/threads/tutorial-power-target-limit- hardware - mod - shunt ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#GPU Overclocking`, `#mVolt+`, `#RTX 5090`, `#RTX 5080`

---

<a id="item-9"></a>
## [三星确认 HBM4E 内存速率达 16 Gbps 每引脚](https://www.techpowerup.com/351859/samsung-confirms-hbm4e-memory-running-at-16-gbps-per-pin) ⭐️ 7.5/10

三星在 Hot Chips 2026 会议上确认，公司正准备出货每引脚 16 Gbps 速率的 HBM4E 内存，较今年 5 月底开始出货的 14 Gbps 版本有所升级。在 2048 个引脚下，单颗 HBM4E 堆栈的最高带宽可达 4 TB/s，高于此前的 3.6 TB/s。 HBM 是下一代 AI 加速器和 GPU 的关键组件，内存带宽是训练大模型和运行推理负载的核心瓶颈。按每个加速器通常配备十余颗 HBM 堆栈计算，此次速率提升将显著增加 AI 芯片可获得的总带宽。 三星目前提供 12 层堆叠、容量 48 GB 的 HBM4E 配置，并计划根据客户需求推出 8 层 32 GB 和 16 层 64 GB 的版本。三星现有的 HBM4 出货速率为 11.7 Gbps，因此跃升至 16 Gbps 的 HBM4E 尤为引人注目。

rss · TechPowerUp News · 8月24日 05:30

**背景**: 高带宽内存（HBM）是一种堆叠式 DRAM，通过硅通孔（TSV）将多层存储裸片垂直互连，提供远超传统 GDDR 内存的带宽。HBM 对于 NVIDIA、AMD 及定制 ASIC 厂商的 AI 加速器至关重要，因为 AI 工作负载需要在计算单元与内存之间进行海量数据传输。该市场由三星、SK 海力士和美光三家主导，每一代（HBM2、HBM3、HBM3E、HBM4、HBM4E）都在每引脚速率、堆栈容量和能效方面持续提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://hotchips.org/">Hot Chips</a></li>
<li><a href="https://www.advisorpedia.com/active/the-memory-shortage-wall-street-isnt-seeing/">The Memory Shortage Wall Street Isn’t Seeing | Advisorpedia</a></li>

</ul>
</details>

**标签**: `#HBM4E`, `#Samsung`, `#high-bandwidth-memory`, `#AI-hardware`, `#semiconductors`

---

<a id="item-10"></a>
## [台湾起诉九人涉嫌走私英伟达 B300 GPU 至中国](https://www.tomshardware.com/tech-industry/artificial-intelligence/nine-indicted-by-taiwan-over-illegal-export-of-nvidia-b300-gpus-to-china-details-reveal-five-point-strategy-to-exploit-and-avoid-customs-controls) ⭐️ 7.5/10

台湾已对九名涉嫌非法走私英伟达 B300 AI 服务器至中国大陆的人员提起诉讼，据报道他们采用了五点策略来规避海关管控。 此案凸显了围绕 AI 芯片出口管制的执法力度不断升级，也展示了走私者为规避管制所采用的精密手段，反映出先进 AI 硬件对中国的地缘政治重要性。 英伟达 B300（Blackwell Ultra）是英伟达目前最强的单颗 GPU，配备 288GB HBM3e 显存、8TB/s 带宽和每芯片 15 petaFLOPS 的 FP4 密集算力，因此成为出口管制的重点目标。此次起诉与此前涉及英伟达高级经理与 Supermicro 的另一起走私案存在关联。

rss · Tom's Hardware · 8月24日 15:09

**背景**: 美国已对中国实施越来越严格的先进 AI 芯片出口管制，主要由工业与安全局（BIS）执行，旨在限制中国获取用于军事和 AI 应用的尖端半导体技术。英伟达 B300 属于 2026 年 1 月开始出货的 Blackwell Ultra 一代，是受这些管制约束的最新一代 AI 加速器。台湾作为 AI 服务器组装的主要枢纽和硬件运输的关键中转地，已成为打击走私行动的重要司法管辖区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spheron.network/blog/nvidia-b300-blackwell-ultra-guide/">NVIDIA B300 (Blackwell Ultra): 288GB Specs, Pricing & Benchmarks (2026) | Spheron Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/08/nvidia-senior-manager-linked-to-supermicro-scheme-smuggling-ai-servers-to-china/">Nvidia senior manager linked to Supermicro scheme smuggling AI servers to China - Ars Technica</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#export-controls`, `#B300`, `#AI-hardware`, `#Taiwan-China`

---

<a id="item-11"></a>
## [AMD 在 Hot Chips 2026 大会揭晓 MI400 GPU 架构](https://www.servethehome.com/amd-mi400-gpu-at-hot-chips-2026/) ⭐️ 7.5/10

AMD 在 Hot Chips 2026 大会上展示了其 MI400 GPU 架构，公布了这款专为 Helios 机架级系统打造的巨型 AI 加速器的设计细节。此次展示详细说明了该芯片如何与 EPYC Venice CPU 和 Pensando Vulcano AI NIC 协同工作，为 AMD 的全栈 AI 平台提供算力。 MI400 是 AMD 迄今为止在数据中心 AI 加速器领域挑战 NVIDIA 主导地位的最激进尝试，Helios 机架级平台旨在与 NVIDIA 的 GB200/NVLink 系统正面竞争。如果 MI400 这一代产品取得成功，将可能改变超大规模云厂商和企业在前沿 AI 训练与推理方面的经济模型。 MI400 采用 AMD CDNA 5 架构和台积电 2nm 工艺制造，据报道集成 3200 亿个晶体管，配备 432 GB HBM4 显存，单 GPU 可提供高达 40 PFLOPS 的 FP4 算力。Helios 机架每个整合 72 颗 MI400 GPU（MI455X 型号）搭配 EPYC Venice CPU，将整个机架作为单一协同加速器呈现。

rss · ServeTheHome · 8月25日 00:30

**背景**: Hot Chips 是自 1989 年以来在斯坦福大学举办的知名年度研讨会，是各大半导体公司发布高性能芯片深度架构细节的传统舞台。AMD 的 Instinct 产品线是其面向 AI 和 HPC 负载的数据中心 GPU 系列，直接对标 NVIDIA 的 H100/B100/B200 系列以及即将推出的 Rubin 产品。像 Helios 这样的机架级系统代表了从单个 GPU 向集成计算架构的转变，CPU、GPU 和高速网络经过共同设计，作为一个大型加速器协同工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/amd-helios-mi400-system-architecture-at-hot-chips-2026/">AMD Helios MI400 System Architecture at Hot Chips 2026</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi400.html">AMD Instinct™ MI400 Series GPUs</a></li>
<li><a href="https://hotchips.org/">Hot Chips</a></li>

</ul>
</details>

**标签**: `#AMD`, `#MI400`, `#GPU`, `#HotChips`, `#AI-Hardware`

---

<a id="item-12"></a>
## [Arm 在 Hot Chips 2026 发布首款完整数据中心 CPU——AGI](https://www.servethehome.com/arms-agi-data-center-cpu-at-hot-chips-2026/) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，Arm 发布了其首款完整商用 CPU 设计——AGI，基于 Neoverse V3 核心打造，面向下一代智能体 AI 服务器。这标志着 Arm 从纯粹的 IP 授权商转向提供完整芯片设计，进入数据中心市场。 这对 Arm 而言是一次重大的战略转变——从仅授权单个 CPU 核心 IP 转向交付完整的数据中心芯片设计，更直接地参与服务器 CPU 市场的竞争。明确聚焦智能体 AI 工作负载，使 Arm 能够抓住对自主 AI 系统快速增长的需求，这类系统需要大量通用计算来协调加速器并执行推理循环。 根据技术披露，AGI CPU 采用双 chiplet 设计，约包含 1000 亿个晶体管和 136 个 Neoverse V3 核心，每个核心是 10 宽乱序执行设计，具备第三代预取和分支预测功能，并配有紧邻核心的高速 L2 缓存。然而，AGI 基于现有的 Neoverse V3 IP 而非全新的微架构，其差异化主要体现在系统级集成、chiplet 封装和面向特定工作负载的调优上，而非核心层面的创新。

rss · ServeTheHome · 8月24日 19:00

**背景**: Arm Neoverse 是 Arm 专为数据中心、边缘计算和高性能计算设计的 64 位处理器核心系列，传统上授权给 AWS（Graviton）、Ampere 和 Microsoft（Cobalt）等合作伙伴。智能体 AI（Agentic AI）是指能够独立规划、使用工具并自适应完成任务的半自主或完全自主 AI 系统——与传统聊天机器人不同，它们会在环境中主动执行操作，通常每次任务会调用多次模型推理和工具交互。Hot Chips 是每年在斯坦福大学举办的享有盛誉的研讨会，领先的半导体公司会在会上详细披露其最新高性能处理器和加速器的技术细节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/arm-dissects-agi-cpu-tailor-made-for-ai-dual-chiplets-100b-transistors-136-neoverse-v3-cores/">Arm Dissects Its AGI CPU Which Is Tailor-Made For AI: Dual Chiplets...</a></li>
<li><a href="https://en.wikipedia.org/wiki/ARM_Neoverse">ARM Neoverse - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**标签**: `#Arm`, `#data-center`, `#CPU`, `#Hot Chips 2026`, `#agentic AI`

---

<a id="item-13"></a>
## [富士通基于 Arm 架构的 Monaka 数据中心 CPU 亮相 Hot Chips 2026](https://www.servethehome.com/fujitsus-arm-based-monaka-data-center-cpu-at-hot-chips-2026/) ⭐️ 7.5/10

富士通基于 Arm 架构的 Monaka 数据中心 CPU 在 Hot Chips 2026 大会上亮相。

rss · ServeTheHome · 8月24日 18:30

**标签**: `#ARM`, `#Fujitsu`, `#data-center`, `#Hot-Chips-2026`, `#CPU-architecture`

---

<a id="item-14"></a>
## [皮尤研究：ChatGPT 发布后逾三分之一英文网页带有 AI 痕迹](https://www.solidot.org/story?sid=85172) ⭐️ 7.3/10

皮尤研究中心的数据科学家使用 AI 检测工具分析了 50 万个过去五年的英文网页，发现 2022 年底 ChatGPT 发布之后创建的网页中，超过三分之一带有明显的 AI 创作痕迹。研究还识别出具体语言学标记：破折号使用频率翻倍、牛津逗号使用频率增加 63%，以及"delve""interplay""testament"等词汇使用频率翻倍以上。 这是首次大规模实证量化 AI 对开放网络影响的研究，对信息真实性、内容审核和在线信息源的信任度提出了紧迫的质疑。各顶级域名间分布不均——.com 网页的 AI 痕迹大约是 .edu 或 .gov 网页的十倍——表明商业内容被 AI 渗透的程度远高于教育或政府内容。 在 2026 年的样本中，10% 的 .com 域名显示出 AI 创作痕迹，相比之下 .org 为 4.6%，.edu 或 .gov 仅为 1%——尽管在 ChatGPT 刚发布时四种域名的 AI 模式出现频率大致相当。对比式修辞句型"it's not just X, it's Y"的使用频率几乎翻了三倍，进一步说明 LLM 倾向于使用公式化的结构化句式，而不仅仅是统计性的词汇选择。

rss · Solidot · 8月24日 07:06

**背景**: 皮尤研究中心是美国一家无党派智库，专门提供关于社会、政治和技术趋势的实证数据。AI 检测工具通过分析大语言模型输出特有的统计模式（如异常的词频分布和标点习惯）来识别文本。"delve""interplay""testament"等词因在 LLM 生成文本中出现频率远高于人类自然写作，已成为臭名昭著的"AI 标记词"。牛津逗号是列表中"and"或"or"之前可选的最后一个逗号（如"red, white, and blue"），而破折号是用于标示插入语或强调从句的长横线——这两种标点风格都被指出在 AI 写作中被不成比例地偏爱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/牛津逗號">牛 津 逗 号 - 维基百科，自由的百科全书</a></li>
<li><a href="https://wordvice.cn/blog/the-great-comma-debate/">英 语 标点符 号 - 牛 津 逗 号 ( oxford comma )... - Wordvice Blog</a></li>

</ul>
</details>

**标签**: `#AI content detection`, `#Pew Research`, `#Microsoft data loss`, `#non-profit organizations`, `#web trends`

---

<a id="item-15"></a>
## [整个旧金山市被重建为可交互的 3D 电子游戏](https://sf.thijs.gg/) ⭐️ 7.0/10

开发者 Thijs（cdngdev）在 sf.thijs.gg 上发布了整个旧金山市的交互式 3D 重建作品，该作品基于地图数据构建，允许用户像玩电子游戏一样在城市中驾驶和探索，并可拾取金币。该项目于 2025 年 12 月 9 日在 Twitter/X 上分享，迅速获得 326 个点赞和 115 条评论。 该项目展示了一条将真实世界地理空间数据（地图、高程、街景图像）转换为完全可探索的游戏引擎环境的创新流水线，暗示了公民自建开放世界游戏、城市数字孪生以及新型基于位置的交互体验的潜力。它也说明易用的工具和开放数据源能让独立开发者完成曾经只有大工作室才能做到的项目。 该重建作品似乎使用了 Apple Maps 数据并桥接到游戏引擎中，具备驾驶机制和可拾取的金币玩法。项目基于网页运行，部署在 sf.thijs.gg；用户指出，加入 DLSS 超采样、多人模式、街道名称标注以及地址传送等功能将显著提升体验。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**背景**: GIS (Geographic Information Systems) data, such as OpenStreetMap shapefiles, building footprints, digital elevation models (DEMs), and streetview imagery, can be converted into 3D environments using tools like BlenderGIS or GIS 2BLEND add-ons. These workflows typically extrude 2D building footprints into 3D meshes, apply terrain from elevation data, and texture surfaces from photographic sources. Bridging this GIS pipeline into real-time game engines like Unity or Unreal allows for interactive exploration of real-world locations, a technique increasingly used for urban planning visualization, digital twins, and game prototyping.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/domlysz/BlenderGIS">GitHub - domlysz/BlenderGIS: Blender addons to make the bridge...</a></li>
<li><a href="https://osmbuildings.org/">OSM Buildings 3 D city models and viewers</a></li>
<li><a href="https://superhivemarket.com/products/gis2blend/docs">GIS 2BLEND - Documentation - Superhive (formerly Blender Market)</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为热烈且技术性强。开发者们详细讨论了 GIS 到游戏引擎的流水线，其中 jvogt 描述了一种理想工作流，即结合高程、建筑、地图和街景数据，并利用图像到图像模型进行纹理增强。像 frankhorrigan 这样的前旧金山居民表示，重新走访熟悉的街区让他们产生了情感共鸣。用户提出了许多实用改进建议，包括 DLSS 超采样、多人模式支持、街道名称标注和地址传送功能，甚至有人请求改善日本城人行天桥下方的碰撞几何。

**标签**: `#3d-rendering`, `#game-engine`, `#open-world`, `#creative-coding`, `#gis-movie`

---

<a id="item-16"></a>
## [RISC-V 十六年：从模块化 ISA 到 Hot Chips 2026 上的标准化平台](https://semiwiki.com/ip/sifive/372639-risc-v-at-sixteen-from-modular-isa-to-standardized-platforms-at-hot-chips-2026/) ⭐️ 7.0/10

回顾 RISC-V 从伯克利研究项目发展成为全球标准化 ISA 的 16 年历程，并预览 Hot Chips 2026 上关于模块化与平台标准化的讨论。

rss · SemiWiki · 8月24日 19:00

**标签**: `#RISC-V`, `#ISA`, `#Hot Chips 2026`, `#SiFive`, `#hardware`

---

<a id="item-17"></a>
## [Hot Chips 大会聚焦面向 AI 的演进型内存架构](https://semiwiki.com/semiconductor-manufacturers/372632-hot-chips-evolving-memory-architectures-for-artificial-intelligence/) ⭐️ 7.0/10

SemiWiki 对 Hot Chips 大会演讲的报道探讨了新一代内存架构如何被设计来解决限制 AI 加速器扩展的内存带宽瓶颈。文章指出，现代 AI 性能越来越受内存而非算力限制，当处理器无法足够快地获取操作数时，参数、训练数据和算力三者协同增长的扩展定律便会失效。 随着 AI 模型规模持续扩展至数千亿乃至万亿参数，算力吞吐量与内存带宽之间的差距已成为性能和效率的主要瓶颈。内存架构的创新——例如 HBM 堆叠、片上 SRAM 以及新型互连结构——直接决定了 AI 硬件的扩展潜力，对芯片设计、超大规模数据中心运营商以及前沿模型训练的经济性都有深远影响。 文章公开可见的部分强调，当代加速器已受到内存限制，意味着原始 FLOPs 已不再是主要瓶颈。完整的技术细节——包括具体的公司发布、芯片堆叠方案和基准测试结果——位于付费墙/阅读全文链接之后，此处无法评估。

rss · SemiWiki · 8月24日 17:00

**背景**: Hot Chips 是一年一度在斯坦福大学举办、聚焦高性能微处理器及相关集成电路的顶级研讨会，自 1989 年延续至今。在现代 AI 工作负载中，GPU 和定制加速器（如 TPU）使用脉动阵列和大型片上内存等技术，来最小化 DRAM 与计算单元之间昂贵的数据搬运。高带宽内存（HBM）通过垂直堆叠 DRAM 芯片并采用宽接口，已成为业界应对内存带宽瓶颈的主流方案，并被 NVIDIA、AMD 等公司的 AI 加速器广泛采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hotchips.org/">Hot Chips</a></li>
<li><a href="https://medium.com/b8125-fall2025/the-memory-wall-ais-silent-bottleneck-and-the-path-to-unlocking-true-intelligence-525245193c16">The Memory Wall: AI ’s Silent Bottleneck and the Path to... | Medium</a></li>
<li><a href="https://blog.kistacklab.com/en/article/hbm-memory-explained/">HBM Explained: Why High Bandwidth Memory Became... | Kistack Blog</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#memory architecture`, `#Hot Chips`, `#semiconductors`, `#accelerators`

---

<a id="item-18"></a>
## [天工 Ultra 人形机器人百米赛跑超越最快人类](https://www.electronicsweekly.com/blogs/gadget-master/robot/picture-of-the-day-humanoid-4-0-human-2026-08/) ⭐️ 7.0/10

在北京国家体育场举办的世界人形机器人运动会上，天工 Ultra 人形机器人在百米短跑中超越了人类最快纪录。该报道将这一成绩定位为多项目人形机器人赛事中"人形机器人 3 比 0 战胜人类"的象征性里程碑。 这代表了机器人领域一个引人注目的象征性里程碑，表明人形机器人已不再是单纯的实验室原型，而是能够完成超越人类能力的运动表现。这标志着双足行走、平衡控制和爆发性速度方面的快速进步，对未来在物流、制造和服务领域的商业部署具有重要意义。 这篇文章本身内容非常简略，仅是一篇"每日图片"短文，没有提供性能参数、确切冲刺成绩，也没有任何对比指标（例如博尔特的 9.58 秒）。天工 Ultra 由北京人形机器人创新中心与优必选（UBTech）合作开发，此前曾以 2 小时 40 分钟完成全球首个人形机器人半程马拉松。

rss · Electronics Weekly · 8月24日 15:53

**背景**: 人形机器人是模仿人类外形和运动方式的双足机器，应用范围涵盖工业自动化到科学研究。世界人形机器人运动会是北京举办的多项目人形机器人竞赛，比赛项目包括短跑、足球和跳远等。天工 Ultra 是中国的人形机器人旗舰平台之一，由北京人形机器人创新中心与优必选机器人合作开发。该机器人首次引起公众关注是完成了半程马拉松，展示了长时间持续行走的能力——这与百米短跑所需的爆发性加速是完全不同的工程挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://humanoid.press/database/database-tiangong-ultra/">Tiangong Ultra | China’s Marathon-Running Humanoid Robot Champion</a></li>
<li><a href="https://www.aol.com/photos-beijings-world-humanoid-robot-124443007.html">Photos of Beijing 's World Humanoid Robot Games show how... - AOL</a></li>
<li><a href="https://www.roboatlas.ai/en-US/products/tiangong-ultra">X-Humanoid Tiangong Ultra Humanoid Robots Specs, Price & SDK ...</a></li>

</ul>
</details>

**标签**: `#humanoid-robots`, `#robotics`, `#Tiangong-Ultra`, `#Beijing-Robot-Games`, `#human-vs-machine`

---

<a id="item-19"></a>
## [Quintessent 开始提供单芯片 DWDM 梳状激光器样片](https://www.electronicsweekly.com/news/products/quintessent-begins-sampling-single-chip-dwdm-comb-laser-2026-08/) ⭐️ 7.0/10

Quintessent 在完成 4000 万美元 A 轮融资后，开始提供基于量子点的单芯片 DWDM 梳状激光器样片，用于光互连应用。

rss · Electronics Weekly · 8月24日 12:42

**标签**: `#optical-interconnects`, `#photonics`, `#semiconductors`, `#DWDM`, `#data-center-infrastructure`

---

<a id="item-20"></a>
## [LG 原生 1,000Hz 1080p 电竞显示器售价高达 1000 美元——25 英寸 UltraGear 25G590B 开启预售](https://www.tomshardware.com/monitors/gaming-monitors/lgs-native-1-000-hz-1080p-gaming-monitor-has-a-matching-usd1-000-price-tag-preorders-open-for-the-25-inch-ultragear-25g590b) ⭐️ 6.5/10

LG 开启 UltraGear 25G590B 预售，这是一款原生 1000Hz 1080p 电竞显示器，售价 1000 美元。

rss · Tom's Hardware · 8月24日 17:21

**标签**: `#gaming-monitors`, `#display-technology`, `#hardware`, `#lg-ultragear`, `#product-launch`

---