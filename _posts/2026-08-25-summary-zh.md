---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 92 条内容中筛选出 20 条重要资讯。

---

1. [IBM 发布首款原生同时执行 ARM 和 z/Architecture 的双 ISA 核心，2nm 工艺下主频达 5.7 GHz](#item-1) ⭐️ 9.5/10
2. [法医团队称，由英伟达 Jetson Orin 引导的俄罗斯人工智能无人机在乌克兰造成三名平民死亡——这是首例有记录在案的俄罗斯无人机使用完全自主目标锁定导致平民死亡的案件](#item-2) ⭐️ 8.5/10
3. [美光警告：HBM 每代硅晶圆成本差距持续扩大](#item-3) ⭐️ 8.5/10
4. [英伟达在 Hot Chips 2026 详解 88 核 Vera CPU 与空间多线程技术](#item-4) ⭐️ 8.5/10
5. [AliExpress 据称通过隐藏的 Web Audio API 代码对电脑进行指纹识别](#item-5) ⭐️ 8.5/10
6. [英特尔发布 Diamond Rapids Xeon 7：256 个 P 核、1.28 GB LLC、18A-P 工艺、UCIe-S 互联](#item-6) ⭐️ 8.5/10
7. [SK 海力士：HBM 遭遇 775 微米厚度上限，混合键合推迟至 HBM5](#item-7) ⭐️ 8.5/10
8. [微软画图和照片应用静默嵌入无法移除的 GUID 水印到本地图片](#item-8) ⭐️ 8.0/10
9. [Hot Chips：面向人工智能的演进型内存架构](#item-9) ⭐️ 8.0/10
10. [英伟达与 SpaceXAI 将地面数据中心基础设施改造应用于太空](#item-10) ⭐️ 8.0/10
11. [IBM 与 Arm 联合开发双架构处理器，瞄准主机平台](#item-11) ⭐️ 8.0/10
12. [SK 海力士下一代 HBM 内存将采用英特尔 EMIB-T 封装技术](#item-12) ⭐️ 7.5/10
13. [AMD 创下 30.7% x86 市场份额新高，英特尔跌至 31 年低点](#item-13) ⭐️ 7.5/10
14. [英特尔详解 Crescent Island GPU：32 个 Xe3P 核心，最高 480GB LPDDR5X](#item-14) ⭐️ 7.5/10
15. [英特尔在 HOT CHIPS 大会详解 Xeon 7'Diamond Rapids'封装设计](#item-15) ⭐️ 7.5/10
16. [IBM 发布业界首款同时支持 IBM Z 与 Arm 的双架构大型机处理器](#item-16) ⭐️ 7.5/10
17. [苹果发布 M6 与 M5 Ultra 芯片，搭载于新款 Mac Mini 与 Mac Studio](#item-17) ⭐️ 7.5/10
18. [中国放缓对台关键材料出口，威胁芯片、光学与机器人供应链](#item-18) ⭐️ 7.5/10
19. [美国上诉法院驳回 Xinuos 上诉，结束长达数十年的 Linux 所有权之争](#item-19) ⭐️ 7.5/10
20. [台湾起诉九人涉嫌非法向中国出口英伟达 B300 GPU——细节揭露其利用和逃避海关管制的五点策略](#item-20) ⭐️ 7.5/10

---

<a id="item-1"></a>
## [IBM 发布首款原生同时执行 ARM 和 z/Architecture 的双 ISA 核心，2nm 工艺下主频达 5.7 GHz](https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores) ⭐️ 9.5/10

IBM 在 Hot Chips 2026 大会上展示了其首款双 ISA CPU 核心，可在同一核心内原生执行 ARM（AArch64）和 z/Architecture 指令。该处理器采用 2nm 工艺节点，集成了 11 个 IBM Z 核心，主频高达 5.7 GHz，标志着 IBM 大型机和 LinuxONE 系统软件支持范围的一次重大扩展。 这款双 ISA 设计将 IBM 拥有数十年历史的大型机生态与更广泛的 ARM 软件生态连接起来，使企业能够在同一颗芯片上同时运行主流 AI 和云原生工作负载以及传统 z/Architecture 应用。这标志着 IBM 在战略上转向使大型机成为现代 AI 和容器化工作负载的可行平台，有望重塑混合云和企业计算战略。 每个核心配备 36 MB 私有 L2 缓存以及虚拟 L3 和 L4 缓存，其容量超过了上一代 Telum II（虚拟 L3 为 432 MB，虚拟 L4 为 3.5 GB）。全部 11 个核心在 2nm 工艺下统一运行在 5.7 GHz 的高基础频率上，对于集成度如此之高的大型机级芯片而言，这一频率令人印象深刻。

rss · Tom's Hardware · 8月24日 17:42

**背景**: z/Architecture 是 IBM 自 2000 年底推出 z900 系统以来在大型机中使用的 64 位复杂指令集（CISC）架构，其技术渊源可追溯到 1964 年的 IBM System/360。ARM（AArch64）是目前在移动、云端以及越来越多服务器和 AI 工作负载中占主导地位的 RISC 架构。历史上，大型机软件一直是一个相对封闭的生态，因此增加对 ARM 指令的原生执行能力使 IBM Z 客户能够直接利用庞大的 ARM/Linux 软件生态——包括各种 AI 框架——而无需通过速度过慢、无法满足生产需求的模拟方式运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/ibms-first-dual-isa-core-natively-executes-arm-and-z-architecture-in-the-same-core-all-cores-run-at-5-7-ghz-base-frequency-next-gen-mainframe-ai-processor-is-built-on-2nm-node-with-11-cores">IBM's first dual - ISA core natively executes ARM and z/ Architecture in...</a></li>
<li><a href="https://www.servethehome.com/ibm-z-and-linuxone-dual-isa-processor-and-ai-acceleration-at-hot-chips-2026/">IBM Z and LinuxONE Dual - ISA Processor and AI... - ServeTheHome</a></li>
<li><a href="https://en.wikipedia.org/wiki/Z/Architecture">z / Architecture - Wikipedia</a></li>

</ul>
</details>

**标签**: `#IBM`, `#dual-ISA`, `#ARM`, `#mainframe`, `#2nm`, `#Hot Chips`, `#AI processor`, `#z/Architecture`

---

<a id="item-2"></a>
## [法医团队称，由英伟达 Jetson Orin 引导的俄罗斯人工智能无人机在乌克兰造成三名平民死亡——这是首例有记录在案的俄罗斯无人机使用完全自主目标锁定导致平民死亡的案件](https://www.tomshardware.com/tech-industry/drones/nvidia-jetson-orin-guided-the-russian-ai-drone-that-killed-three-civilians-in-ukraine-forensic-teams-say) ⭐️ 8.5/10

一架搭载英伟达 Jetson Orin AI 模块的俄罗斯 Molniya 无人机在乌克兰自主锁定目标并造成三名平民死亡，这是首例有记录的由完全自主无人机目标锁定导致平民死亡的案件。

rss · Tom's Hardware · 8月25日 12:40

**标签**: `#AI ethics`, `#autonomous weapons`, `#Nvidia Jetson`, `#drones`, `#military AI`

---

<a id="item-3"></a>
## [美光警告：HBM 每代硅晶圆成本差距持续扩大](https://www.tomshardware.com/tech-industry/semiconductors/micron-says-the-silicon-gap-between-hbm-and-ddr5-is-widening-with-every-generation) ⭐️ 8.5/10

在 Hot Chips 2026 大会上，美光研究员 Raghu Sreeramaneni 警告称，HBM 相对于 DDR5 的硅晶圆成本差距每一代都在扩大，HBM 每比特所消耗的硅面积约为 DDR5 的三倍。 这一不断扩大的效率差距意味着 AI 基础设施成本将持续攀升，因为 HBM 是为 NVIDIA Blackwell 等 GPU 及 AMD 等厂商加速器供给数据的关键。这表明内存墙——即计算与内存性能之间日益扩大的不匹配——非但没有解决反而在恶化，对 AI 扩展的经济性具有深远影响。 这一差距源于结构本身：HBM 通过 DRAM 芯片的 3D 堆叠和宽 I/O 接口获得带宽优势，这两种方式每比特所消耗的硅面积都远大于平面型的 DDR5。美光将这一趋势描述为持续恶化而非固定成本，意味着 HBM4 及未来世代的硅效率将比当前的 HBM3E 更低。

rss · Tom's Hardware · 8月25日 12:19

**背景**: 高带宽内存（HBM）是一种 3D 堆叠的 DRAM 技术，最初由三星、AMD 和 SK 海力士共同开发，通过将多个存储芯片垂直堆叠并通过宽接口经由硅中介层互联，实现远超标准 DDR5 的带宽。它是 AI 加速器的首选内存，因为向 GPU 张量核心供给海量数据需要极高的带宽。"内存墙"是计算机体系结构中的一个长期概念，描述的是处理器算力与内存访问速度之间不断扩大的差距；在 AI 时代，随着模型规模和上下文窗口急剧膨胀，这堵墙已成为核心瓶颈。Hot Chips 是每年在斯坦福大学举办的顶级研讨会，展示业界领军企业的前沿处理器和芯片设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.hotchips.org/about/">About - Hot Chips</a></li>
<li><a href="https://medium.com/@patan4ik/the-memory-wall-never-went-away-ai-just-made-it-impossible-to-ignore-2bfe3092f501">The Memory Wall Never Went Away. AI Just Made It... | Medium</a></li>

</ul>
</details>

**标签**: `#HBM`, `#memory-wall`, `#semiconductors`, `#AI-infrastructure`, `#Micron`

---

<a id="item-4"></a>
## [英伟达在 Hot Chips 2026 详解 88 核 Vera CPU 与空间多线程技术](https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-nvidia-breaks-down-88-core-vera-cpu-spatial-multithreading-benchmarked-1-2-tb-s-socamm2-memory-agentic-workloads-detailed-and-more) ⭐️ 8.5/10

英伟达在 Hot Chips 2026 大会上详细介绍了其 88 核 Vera CPU，展示了通过分区核心资源实现空间多线程技术、从 88 个核心创建 176 个线程，并搭配带宽达 1.2 TB/s 的 SOCAMM2 LPDDR5X 内存子系统，专为智能体（agentic）AI 数据中心工作负载而设计。 Vera CPU 标志着英伟达从 GPU 扩展到专为 AI 基础设施定制的硅芯片领域，直接挑战英特尔和 AMD 等传统 CPU 厂商在面向智能体 AI 优化的数据中心市场中的地位，在这类场景中海量内存带宽和可预测的多线程吞吐量至关重要。 空间多线程技术与传统的时间分片 SMT 不同，它通过将核心资源在多个线程间进行物理分区，以在大规模场景下实现更可预测的吞吐量；而 SOCAMM2 LPDDR5X 内存在大约传统 CPU 内存系统一半的功耗下提供约两倍的带宽。

rss · Tom's Hardware · 8月25日 11:53

**背景**: Hot Chips 是一年一度的知名半导体会议，各公司会在会上展示即将推出的处理器和加速器的深度技术细节。智能体 AI（agentic AI）指的是能够自主规划、调用工具并执行多步骤任务的 AI 系统，而不仅仅是对单一提示做出响应，这对 CPU 的响应速度和内存带宽提出了新的要求。SOCAMM2 是 JEDEC 标准化的新型紧凑型 LPDDR5X 服务器内存模块形态，相比传统 DDR RDIMM 提供更高密度和显著更低的功耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-cpu/">Next Gen Data Center CPU | NVIDIA Vera CPU</a></li>
<li><a href="https://www.thinkers360.com/tl/blog/members/the-architect-of-agency-nvidias-vera-cpu-and-the-dawn-of-the-ai-super-factory">The Architect of Agency: NVIDIA’s Vera CPU and the Dawn of the AI Super-Factory</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#vera-cpu`, `#hot-chips`, `#data-center`, `#spatial-multithreading`, `#ai-infrastructure`

---

<a id="item-5"></a>
## [AliExpress 据称通过隐藏的 Web Audio API 代码对电脑进行指纹识别](https://www.tomshardware.com/tech-industry/cyber-security/aliexpress-allegedly-uses-your-browsers-audio-system-to-fingerprint-your-pc-hidden-code-runs-even-when-no-sound-is-playing) ⭐️ 8.5/10

一位开发者在调查蓝牙耳机问题时发现，AliExpress 运行隐藏的 Web Audio API 处理代码，即使没有播放任何音频，也会对浏览器进行指纹识别并收集详细的设备信息。 这一发现揭示了全球主要电商平台上一种隐蔽且具有侵入性的追踪行为，引发了人们对网络隐私、浏览器安全策略以及用户对设备级信号如何在无用户同意或无声音反馈的情况下被利用的严重担忧。 该技术利用 Web Audio API 在软件中生成声音，读取浏览器处理该声音后产生的数值，并将其哈希为唯一签名——所有操作都在后台静默执行，没有任何可听输出，使用户难以察觉。

rss · Tom's Hardware · 8月25日 09:44

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mangoproxy.com/blog/audio-fingerprinting-explained/">Audio Fingerprinting Explained: How Websites Use... - MangoProxy</a></li>
<li><a href="https://www.capsolver.com/glossary/audiocontext-fingerprinting">Audiocontext Fingerprinting</a></li>
<li><a href="https://ppc.land/audio-fingerprinting/">Explaining audio fingerprinting</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#fingerprinting`, `#web-security`, `#aliexpress`

---

<a id="item-6"></a>
## [英特尔发布 Diamond Rapids Xeon 7：256 个 P 核、1.28 GB LLC、18A-P 工艺、UCIe-S 互联](https://www.tomshardware.com/pc-components/cpus/intel-xeon-7-diamond-rapids-comes-with-up-to-256-p-cores-1-28-gb-of-last-level-cache-next-gen-18a-p-cpu-also-brings-avx-10-2-and-uses-ucie-s-instead-of-emib) ⭐️ 8.5/10

在 Hot Chips 2026 大会上，英特尔公布了其下一代 Diamond Rapids Xeon 7 服务器 CPU，最高配备 256 个 P 核、1.28 GB 末级缓存，支持 AVX 10.2 指令集，并将芯片间互联从 EMIB 转向行业标准的 UCIe-S。该芯片采用英特尔的 18A-P 工艺节点制造。 这一发布标志着英特尔对 AMD EPYC 最为强势的数据中心反击，可能重塑高端服务器 CPU 市场格局，尤其对受益于大量核心数和超大缓存的 HPC 与 AI 工作负载而言。从自有的 EMIB 转向开放标准 UCIe-S，是英特尔旗舰至强产品线在架构和生态系统上的重要转变。 Diamond Rapids 采用英特尔 18A 工艺的性能优化版本 18A-P，在 RibbonFET 环栅晶体管和 PowerVia 背面供电的基础上增加了性能优化的设计规则。将 EMIB 替换为 UCIe-S，使英特尔的旗舰服务器产品线与更广泛的 Chiplet 生态系统接轨，有望改善多供应商 Chiplet 采购以及 HBM 级别内存的集成。

rss · Tom's Hardware · 8月24日 21:07

**背景**: EMIB（Embedded Multi-die Interconnect Bridge，嵌入式多芯片互连桥接）是英特尔自有的 2.5D 封装技术，通过嵌入基板中的小型硅桥连接 Chiplet，曾用于 Sapphire Rapids 等前代至强处理器。UCIe（Universal Chiplet Interconnect Express，通用 Chiplet 互连标准）是英特尔于 2022 年共同创建的开放式芯片间互连行业标准，可实现不同厂商 Chiplet 之间的互操作。AVX 10.2 是英特尔的向量指令集架构，将大部分 AVX-512 扩展统一为一个规范，可通过 oneDNN 等库服务于 HPC、AI 推理和深度学习工作负载。18A 是英特尔首个在量产中同时采用 RibbonFET（环栅晶体管）和 PowerVia（背面供电）技术的工艺节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-03/foundry-18a-platform-brief.pdf">1 White Paper Industry / Solution Focus Area Contents Intel 18A 1 Intel 18A‑P 3</a></li>
<li><a href="https://www.verilogpro.com/how-chiplets-assemble-into-the-most-advanced-socs/">How Chiplets Assemble Into the Most Advanced SoCs - Verilog Pro</a></li>
<li><a href="https://www.phoronix.com/news/oneDNN-3.13">UXL's oneDNN 3.13 Preps For Intel Nova Lake With AVX 10 . 2 , More...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Xeon`, `#Diamond Rapids`, `#Hot Chips 2026`, `#data center CPUs`, `#18A-P`, `#chiplet`

---

<a id="item-7"></a>
## [SK 海力士：HBM 遭遇 775 微米厚度上限，混合键合推迟至 HBM5](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-says-hybrid-bonding-wont-be-ready-for-hbm4e-as-ai-memory-runs-into-a-775-micron-ceiling) ⭐️ 8.5/10

在 Hot Chips 2026 大会上，SK 海力士披露 HBM 堆叠芯片已经触及 775 微米的厚度上限（相当于 300 毫米逻辑晶圆的标准厚度），混合键合技术无法在 HBM4e 上就绪，将推迟到 HBM5 实现。同时，SK 海力士将继续在其面向 Nvidia Rubin 平台的产品中使用 MR-MUF（大规模回流模塑底部填充）封装技术。 这一路线图调整重塑了整个 AI 内存生态的封装节奏，因为 SK 海力士是 Nvidia 及其他 AI 加速器厂商高端 HBM 的主要供应商。775 微米的厚度上限表明，基于传统凸点互连的渐进式堆叠方式已接近极限，这迫使业界加速向混合键合等更具颠覆性的互连技术转型，以维持 AI 算力所需的内存带宽增长。 混合键合通过在堆叠芯片之间直接建立铜-铜与介质-介质的连接，省去了凸点结构，从而可实现更细的间距、更低的功耗和更薄的堆叠高度，但其良率与产能尚未成熟到能支持 HBM4e。相比之下，MR-MUF 采用大规模回流焊配合模塑底部填充工艺，是 SK 海力士自 HBM3 以来的主力封装技术，在散热和产能方面具有优势，并将延续至 Rubin 一代。

rss · Tom's Hardware · 8月24日 17:55

**背景**: 高带宽内存（HBM）是一种三维堆叠的 DRAM 形式，通过硅通孔（TSV）将多层 DRAM 芯片垂直互连，提供远超传统 GDDR 的内存带宽，是当前 AI GPU 的事实标准内存。SK 海力士、三星和美光是 HBM 的三大主要供应商，SK 海力士凭借其独有的 MR-MUF 堆叠工艺长期保持领先，并因此在 Nvidia 的 HBM3 及 HBM3E 供货中占据绝大部分份额。混合键合被普遍视为下一代封装拐点——其影响力可与 EUV 光刻技术相媲美——因为它消除了凸点间距对堆叠密度的限制，能实现更高、更致密的堆叠结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/hybrid-bonding-process-flow-advanced">Hybrid Bonding Process Flow - Advanced Packaging Part 5</a></li>
<li><a href="https://www.eetimes.com/sk-hynixs-mr-muf-innovations-tackle-heat-generation-to-secure-hbm-leadership/">MR - MUF Innovations Tackle Heat Generation - EE Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#HBM`, `#semiconductors`, `#AI-hardware`, `#SK-hynix`, `#advanced-packaging`

---

<a id="item-8"></a>
## [微软画图和照片应用静默嵌入无法移除的 GUID 水印到本地图片](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

安全研究员 Xu Sheng 发现，微软画图（MS Paint）和微软照片（Microsoft Photos）会自动向本地处理的图片中嵌入基于 GUID 的不可见水印，包括使用本地 AI 模型（如背景移除）生成或修改的图片。该不可见水印在后台静默嵌入，用户无任何提示，且无法通过任何设置关闭。 这一发现引发了严重的隐私担忧，因为嵌入的 GUID 可以通过版权传票等法律手段追溯到用户的微软账户，从而实现对任何图片创作者的去匿名化。这代表了微软在未经用户知情同意的情况下，静默向用户本地生成的内容中嵌入身份元数据的模式，对活动人士、记者、表情包创作者以及任何重视匿名性的用户都有重大影响。 该不可见水印使用隐写术（steganographic）技术将唯一的 GUID 直接嵌入图片像素数据中，肉眼不可察觉但可被机器读取。虽然可见的 AI 生成水印可以在设置中关闭，但不可见的 GUID 水印没有任何关闭选项，且即使 AI 功能完全在本地硬件（而非云端服务）上运行时，该行为仍然生效。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: 隐写术（Steganography）是在非秘密载体中隐藏信息的做法，例如将数据嵌入图片像素中，使人类观察者看到的图片表面毫无变化。数字水印是一种相关技术，将识别信息嵌入媒体文件中，常被版权方用于追踪所有权，或被 AI 公司用于标记 AI 生成内容。GUID（全局唯一标识符）是一个 128 位数字，用于唯一标识对象或实体，在本场景中它似乎用于将每张带水印的图片链接到特定的微软用户账户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Steganography">Steganography - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪强烈负面，用户称这是巨大的隐私越权行为，并批评微软以敌对方式对待付费客户。多位评论者指出，AI 角度只是幌子，核心问题是微软秘密向所有用户图片中嵌入唯一标识符，这使得通过版权传票实现去匿名化成为可能。一位用户提到此前微软曾错误地为所有 Azure DevOps 提交添加 Copilot 水印（无论是否实际涉及 LLM），表明微软存在粗暴、过度干预的实施模式。

**标签**: `#privacy`, `#microsoft`, `#watermarking`, `#steganography`, `#security`

---

<a id="item-9"></a>
## [Hot Chips：面向人工智能的演进型内存架构](https://semiwiki.com/semiconductor-manufacturers/372632-hot-chips-evolving-memory-architectures-for-artificial-intelligence/) ⭐️ 8.0/10

Hot Chips 会议报道，讨论了演进型内存架构对于解决现代 AI 加速器中内存带宽瓶颈的必要性。

rss · SemiWiki · 8月24日 17:00

**标签**: `#AI hardware`, `#memory architecture`, `#Hot Chips`, `#AI accelerators`, `#semiconductors`

---

<a id="item-10"></a>
## [英伟达与 SpaceXAI 将地面数据中心基础设施改造应用于太空](https://www.electronicsweekly.com/news/business/nvidia-and-spacexai-adapting-terrestrial-datacentre-infrastructure-for-space-2026-08/) ⭐️ 8.0/10

SpaceXAI 计划中的 Starmind 数据中心卫星将采用英伟达的 Vera Rubin NVL72 机架级系统，标志着向天基人工智能计算基础设施迈出了实质性的一步。

rss · Electronics Weekly · 8月25日 05:15

**标签**: `#space-computing`, `#nvidia`, `#datacenter`, `#ai-infrastructure`, `#spacex`

---

<a id="item-11"></a>
## [IBM 与 Arm 联合开发双架构处理器，瞄准主机平台](https://www.electronicsweekly.com/news/business/ibm-and-arm-designing-dual-architecture-processor-2026-08/) ⭐️ 8.0/10

IBM 与 Arm 正在联合设计一款双架构处理器，其中每个核心都能同时原生执行 IBM Z（或 LinuxONE）和 Arm 指令集，而非将 Arm 作为芯片上的独立子系统。该芯片采用 2nm 工艺制造，预计 2028 年前后推出。 这代表了企业计算领域的一项重要架构进步，因为它使单一芯片能够无缝运行传统主机工作负载和现代基于 Arm 的 Linux 应用程序，无需独立处理域的额外开销。这表明 IBM 正致力于将其主机平台现代化，以适应混合云和 AI 驱动的工作负载，同时保留企业客户所依赖的向后兼容性。 该处理器采用 2nm 工艺节点制造，其裸片设计允许单个核心在同一核心内部原生解码并执行 Arm 和 IBM Z 指令，而非采用异构多芯片或协处理器方案。IBM 尚未为该处理器命名，也未公布将搭载该处理器的具体系统型号。

rss · Electronics Weekly · 8月25日 05:14

**背景**: IBM Z 是 IBM 当前的主机服务器产品线，以极高的可靠性、安全性和跨越数十年的向后兼容性著称。LinuxONE 是 IBM 的纯 Linux 主机服务器系列，经过认证可运行 Red Hat Enterprise Linux、SUSE Linux Enterprise Server 和 Ubuntu 等发行版。最新一代（包括 z16 和 LinuxONE 5）采用 IBM 的 Telum 和 Telum II 处理器，具备芯片级集成 AI 推理引擎。历史上，IBM 在添加辅助处理能力时，通常以独立子系统或协处理器的形式实现；而这次的新设计则直接在核心层面统一了两种指令集架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/news/ibm-mainframe-chip-to-run-arm-and-z-workloads-on-the-same-cores/">IBM mainframe chip to run Arm and Z workloads on the same cores</a></li>
<li><a href="https://www.storagereview.com/news/ibms-2nm-dual-architecture-mainframe-processor-runs-arm-and-ibm-z-instructions-in-the-same-cores">IBM ’s 2nm Dual - Architecture Mainframe Processor Runs Arm and...</a></li>
<li><a href="https://www.techspot.com/news/113600-ibm-building-dual-architecture-mainframe-chip-run-arm.html">IBM is building a dual - architecture mainframe chip that will run Arm ...</a></li>

</ul>
</details>

**标签**: `#IBM`, `#Arm`, `#mainframe`, `#processor-architecture`, `#enterprise-computing`

---

<a id="item-12"></a>
## [SK 海力士下一代 HBM 内存将采用英特尔 EMIB-T 封装技术](https://www.techpowerup.com/351913/sk-hynix-next-gen-hbm-memory-to-use-intel-emib-t-packaging) ⭐️ 7.5/10

在 Hot Chips 2026 大会上，SK 海力士透露正在与英特尔代工合作，将其下一代 HBM 内存集成采用英特尔的 EMIB 先进封装，特别是带有 TSV 的 EMIB-T 变体，同时也在与台积电就 CoWoS-L、CoWoS-S 和 CoWoS-R 展开合作。HBM4 的引脚数正从约 1,024 个扩展到 2,048 个，TSV 数量不断增加，需要采用 2.5D 封装、混合键合和 3D DRAM 集成技术。 这一合作验证了英特尔的 EMIB-T 先进封装技术获得了领先内存厂商的认可，并反映了业界在 HBM 集成方面努力寻求台积电 CoWoS 之外替代方案的潮流。由于 HBM 是 AI 芯片供应的关键瓶颈，多元化的封装路径降低了对单一供应商的依赖，可能重塑先进封装领域的竞争格局。 EMIB-T 在英特尔的硅桥接上增加了硅通孔（TSV），可实现跨堆叠芯片的垂直供电——直接支持 SK 海力士在封装层级实现 3D 内存模块垂直供电的概念。EMIB 系列还包括 EMIB-M（在桥接中集成 MIM 电容）以及基础版 EMIB，后者可在不使用完整硅中介层的情况下连接小芯片，在某些应用场景中比 CoWoS 更具成本效益。

rss · TechPowerUp News · 8月25日 08:23

**背景**: HBM（高带宽内存）是一种堆叠式 DRAM，可提供极高的数据吞吐量，对于 NVIDIA H100 和 B200 等 AI 加速器至关重要。CoWoS（芯片上晶圆上基板，Chip-on-Wafer-on-Substrate）是台积电占主导地位的 2.5D 先进封装技术，通过硅中介层将 HBM 堆栈与逻辑芯片相连，一直是 AI 芯片生产的主要瓶颈。英特尔的 EMIB（嵌入式多芯片互连桥接）是一种替代的 2.5D 方案，在封装基板中嵌入小型硅桥接来连接小芯片，无需使用大型中介层。混合键合是一项新兴的互连技术，可实现无需微凸点的直接铜对铜连接，随着 HBM 引脚数向 2,048 甚至更多扩展，这一技术变得至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/foundry/packaging.html">Advanced Packaging Innovations | Chip Packages - Intel</a></li>
<li><a href="https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-07/emib-product-brief.pdf">Intel Foundry EMIB Technology Brief</a></li>
<li><a href="https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm">CoWoS ® - Taiwan Semiconductor Manufacturing Company Limited</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#HBM`, `#Intel`, `#advanced-packaging`, `#AI-hardware`

---

<a id="item-13"></a>
## [AMD 创下 30.7% x86 市场份额新高，英特尔跌至 31 年低点](https://www.techpowerup.com/351908/amd-gains-ground-as-intel-x86-market-share-goes-back-to-1995-levels) ⭐️ 7.5/10

根据 Mercury Research 的数据，2026 年第二季度英特尔的 x86 CPU 市场份额跌至 69.3%，为 1995 年以来首次跌破 70%；与此同时 AMD 攀升至创纪录的 30.7%，同比增长 6.5 个百分点。这一变化覆盖所有细分市场，AMD 的笔记本份额增长 8.4 个百分点至 28.9%，桌面端达到 34.9%，服务器端达到 34.5%。 这标志着延续三十年的 x86 双寡头格局发生了历史性的再平衡，表明 AMD 的 Zen 架构和 EPYC 服务器战略正在转化为持续的市场份额增长，而非暂时性的飙升。同时也给英特尔带来竞争压力，因为英特尔正准备推出下一代 Xeon 7 "Diamond Rapids"和"Crescent Island"加速器，以捍卫其在数据中心的地位。 若纳入半定制、嵌入式和物联网产品，AMD 的份额将升至 34.1%，英特尔为 65.9%，这得益于游戏主机 SoC 的出货（英特尔在该领域不直接竞争，仅推出了面向掌机的 Arc G3 CPU，自 2026 年 6 月起陆续上市）。AMD 已交付基于 Zen 6 微架构的第六代 EPYC "Venice"服务器处理器，而英特尔的反击则集中在 Xeon 7 "Diamond Rapids"以及配备最多 32 个 Xe3P 核心和 480 GB LPDDR5X 内存的"Crescent Island" GPU 上。

rss · TechPowerUp News · 8月24日 23:50

**背景**: Mercury Research 是追踪桌面、移动和服务器渠道 x86 CPU 出货量的主要第三方分析机构，其季度数据是衡量 AMD 与英特尔竞争态势的行业基准。"x86"指令集为两家公司共同采用，自 1990 年代以来一直主导 PC 和服务器市场，因此英特尔跌破 70%的份额是一个具有象征意义的里程碑。AMD 近年来的复兴通常归功于 2017 年推出的 Zen 架构以及后续的 Zen 4、Zen 5 等版本，它们缩小了与英特尔在性能和能效方面的长期差距，同时 EPYC 激进的定价策略也削弱了 Xeon 在数据中心的统治地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/systems/2026/08/21/amd-grabs-more-cpu-share-while-pricier-pcs-punish-desktop-demand/5291053">AMD grabs more CPU share while pricier PCs punish desktop demand</a></li>
<li><a href="https://www.tomshardware.com/news/amd-and-intel-cpu-market-share-report-recovery-looms-on-the-horizon">AMD and Intel CPU Market Share Report: Recovery... | Tom's Hardware</a></li>
<li><a href="https://ms.codes/en-ca/blogs/computer-hardware/mercury-research-cpu-market-share">Mercury Research CPU Market Share</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Intel`, `#CPU market share`, `#x86`, `#semiconductor industry`

---

<a id="item-14"></a>
## [英特尔详解 Crescent Island GPU：32 个 Xe3P 核心，最高 480GB LPDDR5X](https://www.techpowerup.com/351901/intel-details-crescent-island-graphics-32-xe3p-cores-up-to-480-gb-lpddr5x-memory) ⭐️ 7.5/10

在 2026 年 Hot Chips 大会上，英特尔披露了其基于 Xe3P 架构的数据中心 GPU“Crescent Island”的详细规格，包含 32 个 Xe3P 核心、256 个重新设计的 XMX 引擎、32MB 统一 L2 缓存，以及在 350W 风冷 PCIe 卡上最高 480GB 的 LPDDR5X 内存。XMX 引擎从标准 Xe3 的 4 深度脉动阵列重新设计为 Xe3P 上的 16 深度脉动阵列，并新增了 FP4 数据格式支持，与 FP8 并存。 Crescent Island 凭借最高 480GB 的大容量内存，使其能够在本地运行前沿开源模型而无需昂贵的 HBM，这让英特尔在数据中心 AI 加速器市场中成为对抗 NVIDIA 和 AMD 的更具可信度的竞争者。其纯 AI 推理定位（无图形输出）和低成本 LPDDR5X 设计，表明英特尔的战略是瞄准成本高效、长上下文和智能体（agentic）AI 工作负载，而非在高端训练市场正面对决。 该卡使用 LPDDR5X 内存（英特尔品牌型号为 160GB，通过 ODM 可达 480GB）而非 HBM，将功耗保持在 350W 的同时降低成本。每个 Xe3P 核心包含 8 个 XMX 引擎（共计 256 个）、1MB 寄存器文件和 512KB L1 缓存，共享 32MB L2 缓存；芯片不含图形输出路径，使其成为专用于长上下文和智能体任务的推理加速器。

rss · TechPowerUp News · 8月24日 19:49

**背景**: 英特尔的 Xe 架构是该公司用于消费级 Arc 显卡和数据中心产品的 GPU IP。Xe3P 是第三代 Xe3 架构的变体，其中 Xe3 用于 PC 端的 Panther Lake（Core Ultra 300 系列），而 Xe3P 则面向数据中心 AI 加速器。XMX（Xe Matrix Extensions）引擎是英特尔对标 NVIDIA Tensor Core 的方案，通过 DPAS（点积累脉动）指令在脉动阵列上执行矩阵乘法——脉动阵列是一种针对神经网络推理中常见的重复并行算术操作而优化的硬件结构。从 4 深度到 16 深度脉动阵列的转变意味着每个周期可实现更高的数据复用，从而提升矩阵工作负载的吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/intel-details-xe3p-gpu-architecture-crescent-island-gets-up-to-480gb-memory-and-350w-pcie-variant">Intel details Xe3P GPU architecture, Crescent Island gets up ...</a></li>
<li><a href="https://wccftech.com/intel-crescent-island-gpus-32-xe3p-cores-for-agentic-ai-low-cost-lpddr5x-up-to-480-gb/">Intel Crescent Island GPUs Pack Up To 32 Xe 3 P Cores, Optimized For...</a></li>
<li><a href="https://www.servethehome.com/intel-crescent-island-160gb-to-480gb-lpddr5x-ai-gpu-at-hot-chips-2026/">Intel Crescent Island 160GB to 480GB LPDDR5X AI... - ServeTheHome</a></li>

</ul>
</details>

**标签**: `#intel`, `#gpu`, `#data-center`, `#ai-hardware`, `#xe3p-architecture`

---

<a id="item-15"></a>
## [英特尔在 HOT CHIPS 大会详解 Xeon 7'Diamond Rapids'封装设计](https://www.techpowerup.com/351893/intel-details-xeon-7-diamond-rapids-package-design-at-hot-chips) ⭐️ 7.5/10

英特尔在 HOT CHIPS 大会上详细介绍了其下一代 Xeon 7'Diamond Rapids'服务器处理器，公布了基于小芯片（chiplet）的设计方案：每插槽最多 256 个'Panther Cove' P 核、最高 1.28 GB 末级缓存、PCIe Gen 6 I/O，并采用 Intel 18A-P 制程节点制造。整个 MCM 由两个 Fabric Hub Tile、四个 Base Tile 和 16 个核心小芯片（各含 16 个核心）组成。 Diamond Rapids 代表了英特尔在高核心数服务器市场最激进的布局，也是其最明确地效仿 AMD 小芯片分解架构的举措，直接瞄准需要海量串行计算能力的企业级智能体（agentic）AI 工作负载。选择自家 18A-P 制程也预示着英特尔代工战略能否为其旗舰数据中心产品提供具备竞争力的制程技术。 1.28 GB 的末级缓存容量相当可观，体现了英特尔一贯坚持的大容量缓存策略，以满足数据密集型 AI 推理和智能体工作负载的供数需求。尽管核心数量追平了 AMD 顶级 EPYC 产品，但 Diamond Rapids 的竞争力将取决于每核 IPC、内存带宽、平台成熟度，以及英特尔能否真正实现 18A-P 硅片的规模化量产。

rss · TechPowerUp News · 8月24日 15:55

**背景**: 基于小芯片的设计已成为现代服务器 CPU 的主流方案：制造商不再构建单一的单片芯片，而是将处理器拆分为较小的计算芯片和一个独立的 I/O 芯片，从而提升良率并实现每插槽更多核心。AMD 率先在其基于 Zen 架构的 EPYC 处理器上采用 CCD 加中心化 I/O 芯片的方式。英特尔历来更倾向于单片设计，但如今在 Diamond Rapids 上也转向了类似的分解式架构。Intel 18A 是英特尔的领先制程节点，集成 RibbonFET 全环栅晶体管和 PowerVia 背面供电技术，'-P'版本则面向追求性能的大型服务器芯片。智能体 AI（agentic AI）指的是能够自主规划和执行多步骤任务的 AI 系统，对 CPU 提出了大规模并发串行处理能力的要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/351893/intel-details-xeon-7-diamond-rapids-package-design-at-hot-chips">Intel Details Xeon 7 "Diamond Rapids" Package Design at HOT CHIPS</a></li>
<li><a href="https://wccftech.com/intel-diamond-rapids-xeon-7-cpus-256-p-cores-1-28-gb-of-cache-12800-mtps-memory/">Intel Diamond Rapids "Xeon 7" CPUs Feature 256 P -Cores, The Same...</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-enterprise">What is an agentic enterprise? - IBM</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Xeon`, `#server processors`, `#chip architecture`, `#HOT CHIPS`

---

<a id="item-16"></a>
## [IBM 发布业界首款同时支持 IBM Z 与 Arm 的双架构大型机处理器](https://www.techpowerup.com/351885/ibm-unveils-next-generation-dual-architecture-processor-for-ibm-z-and-linuxone) ⭐️ 7.5/10

在 Hot Chips 大会上，IBM 发布了业界首款双架构大型机处理器，旨在让未来的 IBM Z 和 LinuxONE 系统能够同时运行 IBM Z 和 Arm 两个计算平台上的操作系统和应用程序。这是 IBM 与 Arm 于 2026 年 4 月建立合作以来的首个重大里程碑。 这一突破将 IBM 的企业级大型机生态系统（承载全球 68%的交易）与拥有 2200 万开发者的 Arm 软件生态连接起来，使企业能够在同一硬件上同时运行云原生和 AI 工作负载以及关键事务处理负载。它实际上向更广泛的 Arm 开发者社区开放了大型机市场，同时让 Arm 工作负载能够利用 IBM 的企业级安全性和可靠性。 该处理器采用 2nm 工艺节点制造，支持 z/OS、Linux on IBM Z 和 Arm 原生 Linux 环境的并行执行。在该平台上运行的 Arm 工作负载将获得 IBM 的硬件级故障检测与恢复、高级加密、安全密钥管理以及片上 AI 加速等能力。

rss · TechPowerUp News · 8月24日 14:26

**背景**: IBM Z 大型机是关键任务企业计算的支柱，承载全球 68%的交易，以无与伦比的可靠性、安全性和垂直整合而著称。LinuxONE 是 IBM 的企业服务器产品线，将相同的 Z 硬件架构引入纯 Linux 环境，面向那些希望获得大型机级可靠性但又不想使用专有 z/OS 的机构。而 Arm 已成为全球应用最广泛的处理器架构，从移动设备到云服务器无所不在，拥有超过 2200 万开发者的庞大生态支持。迄今为止，Arm 和 IBM Z 基本处于各自独立的世界；这款双架构处理器是 IBM 首次尝试将二者统一在同一颗芯片上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IBM_Z">IBM Z - Wikipedia</a></li>
<li><a href="https://www.ibm.com/products/linuxone-4">IBM LinuxONE 4</a></li>
<li><a href="https://interestingengineering.com/innovation/ibm-2nm-dual-architecture-arm-mainframe-processor">IBM unveils 2nm processor built for dual - architecture computing</a></li>

</ul>
</details>

**标签**: `#IBM`, `#Arm`, `#mainframe`, `#enterprise-computing`, `#hardware`

---

<a id="item-17"></a>
## [苹果发布 M6 与 M5 Ultra 芯片，搭载于新款 Mac Mini 与 Mac Studio](https://www.tomshardware.com/pc-components/cpus/apple-launches-new-m6-and-m5-ultra-apple-silicon-chips-debuting-in-new-mac-mini-and-mac-studio) ⭐️ 7.5/10

苹果于 2026 年 8 月 25 日发布了两款新 Apple Silicon 芯片：M6（苹果首款 2 纳米制程芯片）以及 M5 Ultra（苹果迄今最强大的芯片，也是首款采用四芯片模块架构的产品）。M6 首发搭载于新款 Mac Mini，M5 Ultra 则搭载于全新 Mac Studio。 M6 标志着苹果迈入 2 纳米工艺时代，这是芯片设计领域的重要里程碑，有望带来更高的每瓦性能与更强的端侧 AI 算力。同时，M5 Ultra 的四芯片模块架构表明苹果正持续向工作站级性能市场渗透，进一步加剧与 Intel、AMD 高端 x86 平台的竞争。 M6 配备 12 核 CPU、12 核 GPU 以及双 16 核 Neural Engine。M5 Ultra 则采用 UltraFusion 高速互联技术，将两颗双芯片模块的 M5 Max 连接在一起，构成苹果首款四芯片模块架构。

rss · Tom's Hardware · 8月25日 13:26

**背景**: Apple Silicon 是苹果自 2020 年推出 M1 以来基于 ARM 架构自研的处理器系列，已逐步取代 Mac 中的 Intel 芯片。苹果的「Ultra」级别芯片历来通过 UltraFusion 高速互联将两颗「Max」芯片模块合二为一，实现性能翻倍。从 3 纳米向 2 纳米制程的跨越意味着晶体管密度的显著提升，从而在相同功耗下实现更多核心、更高能效以及更强的 AI 与 Neural Engine 性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M 6 and M5 Ultra for a big leap in performance and...</a></li>
<li><a href="https://www.wired.com/story/apple-announces-m6-and-m5-ultra-mac-mini-mac-studio/">Apple Mac Mini M6 and Mac Studio M 5 Ultra : Specs , Price... | WIRED</a></li>
<li><a href="https://9to5mac.com/2026/08/25/apple-launches-next-gen-apple-silicon-chips-m6-and-m5-ultra/">Apple launches next-gen Apple Silicon chips : M 6 and... - 9to5Mac</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Apple Silicon`, `#M6`, `#Mac Mini`, `#Mac Studio`

---

<a id="item-18"></a>
## [中国放缓对台关键材料出口，威胁芯片、光学与机器人供应链](https://www.tomshardware.com/tech-industry/china-strategically-slows-exports-of-critical-materials-used-in-semiconductor-fabrication-to-taiwan-germanium-and-quartz-exports-to-the-region-also-threaten-optical-and-robotics-supply-chain) ⭐️ 7.5/10

中国已战略性放缓对台湾地区的锗、石英基材料及稀土磁体出口，此举可能扰乱台湾的半导体制造、光学连接及机器人产业。 台湾拥有全球最先进的半导体代工厂，任何关键输入材料的供应中断都可能波及全球电子、光子及自动化产业，并进一步升级北京与台北之间围绕科技领域的贸易紧张局势。 锗是高速晶体管、光纤及红外系统的关键材料；熔融石英坩埚用于生长硅单晶以制造晶圆；稀土磁体则为工业机器人提供所需的扭矩密度和精度。

rss · Tom's Hardware · 8月25日 13:00

**背景**: 锗是一种金属元素，广泛用于先进半导体、光纤网络及军用红外光学器件，全球年产量仅约 130 吨。熔融石英坩埚是直拉法（Czochralski 法）生长硅单晶时进行超洁净熔炼的黄金标准容器，几乎所有硅晶圆的制备都依赖于此。稀土磁体（尤其是钕铁硼磁体）在高性能电机和人形机器人执行器中不可替代，使其成为先进自动化领域的战略瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rare-earth-mining.com/top-10-germanium-uses/">Top 10 Germanium Uses : Semiconductors to Defence 2026</a></li>
<li><a href="https://www.momentivetech.com/products/crucibles/quartz-glass-crucibles">Quartz Crucibles – Momentive Technologies</a></li>
<li><a href="https://rareearthexchanges.com/industrial-robotics-2/">How Rare Earth Elements Power Industrial Robotics</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply-chain`, `#geopolitics`, `#china-taiwan`, `#trade-policy`

---

<a id="item-19"></a>
## [美国上诉法院驳回 Xinuos 上诉，结束长达数十年的 Linux 所有权之争](https://www.tomshardware.com/software/linux/decades-long-linux-ownership-dispute-effectively-dead-after-xinuos-appeal-rejected-us-court-of-appeals-halts-the-legal-wrangling-over-ibms-and-red-hats-use-of-project-monterey-unix-code) ⭐️ 7.5/10

美国第二巡回上诉法院驳回了 Xinuos 的上诉，基本结束了这场长达数十年的关于 Linux 所有权的法律纠纷。法院驳回了 Xinuos 关于 IBM 和 Red Hat 不当将联合开发的 Project Monterey UNIX 代码贡献给 Linux 的指控。 这一裁决为开源生态系统提供了期待已久的法律澄清，确认了 IBM 和 Red Hat 对 Linux 贡献的合法性，并消除了笼罩在 Linux 开发之上的长期法律阴影。它强化了这样一个原则：在适当协议下向开源项目所做的贡献，不会将底层知识产权的所有权转移给前商业合作伙伴。 上诉法院认同 Xinuos 试图将此案定性为许可纠纷，但实际核心问题是所有权主张，法院认定这些主张毫无根据。Xinuos 表示打算向上诉法院全体法官申请复审，此种申请极为罕见且很少获得批准。

rss · Tom's Hardware · 8月25日 10:00

**背景**: Project Monterey 项目是 1990 年代末由 SCO、IBM、Sequent 和 Intel 共同发起的合资项目，旨在打造跨不同架构的统一 UNIX 产品线。IBM 于 1999 年以 8.1 亿美元收购了 Sequent，此交易也加强了 IBM 在 Project Monterey 中的地位。最初的诉讼可追溯到 2000 年代初，当时围绕 UNIX 知识产权以及这些联合开发项目的代码是否不当流入 Linux 内核展开了更广泛的诉讼。从老 SCO Group 收购资产的 Xinuos 多年来一直在追诉这些主张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/tech/tech-industry/ibm-buys-sequent-for-810-million/">IBM buys Sequent for $810 million - CNET</a></li>
<li><a href="https://www.theregister.com/software/2026/08/24/ancient-who-owns-linux-case-now-has-one-foot-very-deep-in-the-grave/5291513">Ancient 'Who owns Linux?' case now has one foot very deep in ...</a></li>
<li><a href="https://landley.net/history/mirror/unix/unix-history.html">UNIX Chronology</a></li>

</ul>
</details>

**标签**: `#linux`, `#open-source`, `#legal`, `#ibm`, `#red-hat`

---

<a id="item-20"></a>
## [台湾起诉九人涉嫌非法向中国出口英伟达 B300 GPU——细节揭露其利用和逃避海关管制的五点策略](https://www.tomshardware.com/tech-industry/artificial-intelligence/nine-indicted-by-taiwan-over-illegal-export-of-nvidia-b300-gpus-to-china-details-reveal-five-point-strategy-to-exploit-and-avoid-customs-controls) ⭐️ 7.5/10

台湾起诉九人，指控他们通过五点计划向中国走私英伟达 B300 GPU 服务器以逃避海关管制。

rss · Tom's Hardware · 8月24日 15:09

**标签**: `#nvidia`, `#export-controls`, `#ai-hardware`, `#geopolitics`, `#semiconductors`

---