---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 96 条内容中筛选出 20 条重要资讯。

---

1. [AMD 揭晓 Zen 6 和 Zen 6c 处理器架构细节](#item-1) ⭐️ 9.3/10
2. [IBM 发布 Nighthawk r3 处理器及 1000 量子比特路线图](#item-2) ⭐️ 8.5/10
3. [沉痛悼念：Python 核心开发者、《Python 之禅》作者 Tim Peters 离世](#item-3) ⭐️ 8.0/10
4. [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](#item-4) ⭐️ 8.0/10
5. [Using voltage glitching to unleash the A100 in my mining card](#item-5) ⭐️ 8.0/10
6. [NVHBM: Can Custom HBM Change Who Builds the Memory Stack?](#item-6) ⭐️ 8.0/10
7. [STMicros’ Maria Heriz on Moving All Its MCUs to One STM32 Platform](#item-7) ⭐️ 8.0/10
8. [Credo 在 OCP 2026 发布 1.6T ZeroFlap ALC 提升 AI 互连可靠性](#item-8) ⭐️ 8.0/10
9. [谷歌云整合 TPU 8i Max 与 Arm Neoverse Axion 处理器](#item-9) ⭐️ 8.0/10
10. [Imec 在 NanoIC 中试线建立硅中介层流程](#item-10) ⭐️ 8.0/10
11. [Linux 内存管理审核员因泛滥的 AI 垃圾补丁辞职](#item-11) ⭐️ 7.5/10
12. [AMD MEXT 技术使用一半内存即可实现 95%服务器性能](#item-12) ⭐️ 7.5/10
13. [马斯克的 xAI 拟在德州建造 240 亿美元燃气 AI 数据中心面临审批](#item-13) ⭐️ 7.5/10
14. [Ukrainian drone operations squeezed by fiber optic cable shortage triggered by AI data center buildouts](#item-14) ⭐️ 7.5/10
15. [AWS Finally Built Its Own AWS Emulator](#item-15) ⭐️ 7.0/10
16. [Can a Linear Program Do Weight-Space Programming?](#item-16) ⭐️ 7.0/10
17. [Pharo in the Browser with WebAssembly](#item-17) ⭐️ 7.0/10
18. [SemiWiki 解析硅衬底与 SOI 在晶体管中的关键作用](#item-18) ⭐️ 7.0/10
19. [Mobilint 与 Chips&Media 量产面向人形机器人的边缘 AI 芯片](#item-19) ⭐️ 7.0/10
20. [挪威部署 3500 台 AI 激光无人机保护三文鱼](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [AMD 揭晓 Zen 6 和 Zen 6c 处理器架构细节](https://www.solidot.org/story?sid=85852) ⭐️ 9.3/10

AMD 披露了 Zen 6 和 Zen 6c 处理器的微架构，展示了 3-3.5 纳秒的分支预测错误惩罚、双解码集群以及服务器工作负载 27% 的总体每时钟周期指令数提升。新设计在高频优化的 Zen 6 核心和具备更宽乱序执行窗口的高密度 Zen 6c 核心之间引入了显著的架构差异。 这次重大架构转变对 AMD 的核心设计进行了显著重构，类似于从 Zen 1 到 Zen 2 的跨越，为下一代 CPU 设定了新的性能基准。它通过提供大幅更高的每时钟周期指令数和扩展的缓存结构，对高性能计算、云服务以及消费级桌面设备产生了深远影响。 Zen 6 配备了采用 12 核 CCD 和 48MB 三级缓存的设计，而高密度的 Zen 6c 则使用 32 核 CCD 和 128MB 三级缓存。为了节省芯片面积，整数乘法单元从 3 个减少到了 2 个，但更宽的乱序执行窗口使 64 位加法吞吐量提升至每周期 5.96 次。

rss · Solidot · 11月11日 06:25

**背景**: AMD 使用核心复合体芯片 (CCD) 来封装其 CPU 核心，这些核心通过高速链路连接到中央输入/输出 (I/O) 芯片。此前的 Zen 5 提供的经典核心和高密度核心在架构上几乎完全相同，仅在缓存和核心数量上有所区别。新一代基于 TAGE 的分支预测器和更大的乱序执行窗口代表了复杂整数和浮点指令处理方式的基本转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive - TechPowerUp</a></li>
<li><a href="https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast">AMD’s Zen 6 Family: Feeding the Beast - by George Cozma</a></li>
<li><a href="https://wccftech.com/amd-zen-6-architecture-ipc-cores-memory-performance-epyc-venice/">AMD Zen 6 Architecture Brings A Phenomenal 27% IPC Increase...</a></li>

</ul>
</details>

**标签**: `#CPU Architecture`, `#AMD Zen 6`, `#Microarchitecture`, `#Branch Prediction`, `#Computer Hardware`

---

<a id="item-2"></a>
## [IBM 发布 Nighthawk r3 处理器及 1000 量子比特路线图](https://www.techpowerup.com/354696/ibm-announces-quantum-nighthawk-r3-processor-plans-to-scale-beyond-1-000-qubits-in-2027) ⭐️ 8.5/10

IBM 发布了其新一代 Quantum Nighthawk r3 处理器，该处理器旨在跨 520 个量子比特执行 10,000 次量子操作。此外，公司计划在 2027 年前将两个此类单元连接成一个拥有 1,040 个量子比特的单一系统。 这一里程碑使 IBM 的量子架构朝着实现行业相关问题求解所需的复杂度阈值迈进，同时保持了具有竞争力的执行速度。扩展到 1000 个量子比特以上，对于支持需要数百万至数十亿个样本的应用而言是关键一步。 Nighthawk r3 的设计优先考虑运行 10,000 次操作深层量子电路的能力，以确保计算在合理的时间框架内以合理成本完成。它在增加量子比特数量和电路深度的同时，保持了当前 Nighthawk 系统的高速性能特征。

rss · TechPowerUp News · 11月11日 16:18

**背景**: 量子计算机通过对量子电路结果的采样进行运算，每次运行仅返回一个结果，需要数百万次试验进行统计汇总。与一些离子阱竞争对手不同，IBM 依赖超导量子比特，这提供了更高的执行速度，从而支持更快的样本生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thequantuminsider.com/2026/11/11/ibm-nighthawk-r3-processor-520-programmable-qubits/">IBM Plans 1,040-Qubit Quantum System with Next-Generation ...</a></li>
<li><a href="https://www.fool.com/investing/2026/10/26/ibm-continues-to-plug-along-its-quantum-computing/">IBM Continues to Plug Along, but Its Quantum ... | The Motley Fool</a></li>
<li><a href="https://www.ibm.com/think/news/ibm-goes-big-keep-quantum-computers-cold">IBM goes big to keep quantum computers cold | IBM</a></li>

</ul>
</details>

**标签**: `#quantum-computing`, `#ibm`, `#hardware`, `#scalability`

---

<a id="item-3"></a>
## [沉痛悼念：Python 核心开发者、《Python 之禅》作者 Tim Peters 离世](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028) ⭐️ 8.0/10

CPython 核心开发者、《Python 之禅》作者 Tim Peters 已经去世。Python 社区正汇聚在一起进行悼念，纪念他在技术和社区方面的巨大贡献。 他的离世对编程生态系统而言是一个巨大的损失，特别是他不仅帮助塑造了 Python 的核心设计哲学，还发明了被许多现代语言使用的 Timsort 算法。他是一位传奇人物，其指导和代码对历代开发者产生了深远影响。 除了《Python 之禅》（PEP 20）和 Timsort 排序算法外，他还参与开发了成功的 SpamBayes 程序，并合著了《Python Cookbook》。自 2000 年代初起，他便一直担任 CPython 的核心开发者。

hackernews · ayhanfuat · 11月11日 07:03 · [社区讨论](https://news.ycombinator.com/item?id=50450488)

**背景**: Tim Peters 是 Python 生态系统中极具影响力的软件工程师，曾长期担任 CPython 核心开发者。他最著名的贡献是 1999 年写下的《Python 之禅》，这是一组指导 Python 设计的箴言，在 Python 解释器中输入“import this”即可查看。在计算机科学中，Timsort 是他发明的高效混合排序算法，至今仍是 Python 和 Java 等语言的标准排序实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)">Tim Peters (software engineer) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zen_of_Python">Zen of Python - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了深刻的个人感悟，回忆了他在代码和讨论中慷慨指导的态度，这极大地拓宽了他们的认知。许多人发布了具体的技术致敬，例如运行“import this”来显示他的诗歌，并强调了他在 SpamBayes 以及通过《Python Cookbook》对社区产生的教育影响力。

**标签**: `#Python`, `#Community`, `#Milestone`, `#Obituary`, `#CPython`

---

<a id="item-4"></a>
## [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](https://pietromiotti.com/latest/maya-site/?maya) ⭐️ 8.0/10

Google deployed 48 AI agents to analyze NASA LIDAR data, identifying an unmapped Maya pyramid within 72 hours, sparking debate on the scalability of AI-driven archaeological discoveries.

hackernews · eyvindn · 11月11日 12:05 · [社区讨论](https://news.ycombinator.com/item?id=50452455)

**标签**: `#AI`, `#Archaeology`, `#LIDAR`, `#Computer Vision`, `#Google`

---

<a id="item-5"></a>
## [Using voltage glitching to unleash the A100 in my mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) ⭐️ 8.0/10

A detailed post explains using voltage glitching to unlock the full 80GB of HBM memory on NVIDIA A100-based mining cards, with community discussion exploring risks, alternatives, and the economics behind the hardware binning.

hackernews · lae · 11月11日 10:48 · [社区讨论](https://news.ycombinator.com/item?id=50451903)

**标签**: `#hardware-hacking`, `#nvidia`, `#reverse-engineering`, `#gpu`, `#hbm`

---

<a id="item-6"></a>
## [NVHBM: Can Custom HBM Change Who Builds the Memory Stack?](https://semiwiki.com/semiconductor-manufacturers/376093-nvhbm-can-custom-hbm-change-who-builds-the-memory-stack/) ⭐️ 8.0/10

NVIDIA's NVHBM initiative may reshape the semiconductor industry by altering how high-bandwidth memory is designed, manufactured, and qualified among key suppliers.

rss · SemiWiki · 11月11日 16:00

**标签**: `#NVIDIA`, `#HBM`, `#Semiconductor Supply Chain`, `#Memory`, `#SK Hynix`

---

<a id="item-7"></a>
## [STMicros’ Maria Heriz on Moving All Its MCUs to One STM32 Platform](https://www.eetimes.com/stmicros-maria-heriz-on-moving-all-its-mcus-to-one-stm32-platform/) ⭐️ 8.0/10

STMicroelectronics executive Maria Heriz discusses the strategic decision to unify all company MCUs under the STM32 platform, while also addressing preparation for EU cyber regulations and the integration of RISC-V, AI agents, and robotics technologies.

rss · EE Times · 11月11日 18:28

**标签**: `#STMicroelectronics`, `#STM32`, `#Microcontrollers`, `#Embedded Systems`, `#RISC-V`

---

<a id="item-8"></a>
## [Credo 在 OCP 2026 发布 1.6T ZeroFlap ALC 提升 AI 互连可靠性](https://www.eetimes.com/credo-at-ocp-2026-micro-emitter-optics-and-ai-interconnect-reliability/) ⭐️ 8.0/10

Credo 的 Don Barnetson 在 OCP 2026 上展示了 1.6T ZeroFlap 有源光缆（ALC），该技术采用微发射器光学技术为 AI 集群提供 1.6Tb/s 的连接能力。此技术在重量的 1/10 的光缆中提供类似铜缆的可靠性，传输距离可达 50 米，支持行级扩展网络。 该互连技术对于扩展现代 AI 数据中心至关重要，因为它缓解了传统可插拔光学器件在高速网络中带来的延迟和可靠性风险。通过在 50 米传输距离下提供稳健且高性价比的连接，Credo 正在帮助 AI 系统架构师构建更高效、稳定的集群基础设施。 1.6T ZeroFlap 收发器在标准 OSFP 可插拔封装中集成了 Credo 的 Kfir200 SiPho PIC 和 PILOT 诊断功能。该架构通过众多小型、低功耗通道分发数据，具备冗余设计，在扩展场景中可提供比传统铜缆背板高出 10 倍的带宽。

rss · EE Times · 11月11日 18:01

**背景**: 随着计算节点之间对高速、低延迟通信的需求增长，光互连正成为现代 AI 数据中心的关键瓶颈。开放计算项目（OCP）是专注于设计和构建开放、可扩展基础设施的行业标准，Credo 在此标准框架下展示了其 1.6T ZeroFlap ALC 技术，以解决这些特定的硬件集成需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://credosemi.com/blogs/zeroflap-optics-expands-to-1-6t-why-combining-our-best-optical-technologies-changes-the-reliability-equation-for-ai/">ZeroFlap Optics Expands to 1.6T: Why Combining Our Best ...</a></li>
<li><a href="https://www.ico-optics.org/credos-zeroflap-alc-redefines-ai-data-center-reliability/">Credo’s ZeroFlap ALC Redefines AI Data Center Reliability</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#High-Speed Interconnects`, `#Optical Computing`, `#Hardware`, `#Data Centers`

---

<a id="item-9"></a>
## [谷歌云整合 TPU 8i Max 与 Arm Neoverse Axion 处理器](https://www.electronicsweekly.com/news/business/goggle-pairs-tpu-with-arm-2026-11/) ⭐️ 8.0/10

谷歌云正在将其 TPU 8i Max 系统与基于 Arm 的 Axion 处理器配对。这些处理器是专为数据中心设计的定制 Arm Neoverse CPU。 这种战略性硬件整合标志着向以 Arm 为核心的云计算数据中心基础设施的重大架构转变。它加强了谷歌在 AI 工作负载中定制芯片的承诺，并提升了云基础设施的性能。 该整合采用了基于 Arm Neoverse 的定制 CPU Axion，使其与 TPU 8i Max 系统协同工作。这种特定的配对是谷歌扩大其云服务中 Axion 使用范围的努力的一部分。

rss · Electronics Weekly · 11月11日 06:32

**背景**: TPU（张量处理器）是谷歌专为机器学习计算设计的定制芯片，而 Axion 是基于 Arm Neoverse 架构的 CPU。在云计算中，将类似 TPU 的专用加速器芯片与高效通用 CPU 结合，可以构建一个平衡的基础架构，以运行复杂的 AI 任务。

**标签**: `#Hardware`, `#AI Infrastructure`, `#Cloud Computing`, `#Google`, `#Arm`

---

<a id="item-10"></a>
## [Imec 在 NanoIC 中试线建立硅中介层流程](https://www.electronicsweekly.com/news/business/imec-delivers-baseline-flows-for-nanoic-interposed-2026-11/) ⭐️ 8.0/10

Imec 已成功在其 NanoIC 中试线中建立了硅中介层的基线制造流程。这为先进封装中用于芯粒集成的关键提供了早期的技术视角。 这一里程碑对半导体行业意义重大，因为它推进了先进封装技术的发展，这对于提高芯粒的可扩展性和集成至关重要。它为硬件和系统工程专业人员提供了早期技术洞察。 交付基线流程是开发中介层平台的一个渐进步骤，而非成品或大规模生产。NanoIC 中试线专为开发 2nm 以下系统级芯片而设计，并得到欧盟芯片法案的支持。

rss · Electronics Weekly · 11月11日 06:10

**背景**: 硅中介层是先进封装中用于在处理器、加速器芯粒和高带宽内存之间提供高密度连接的电气接口。它采用硅而非传统层压板，以支持更细的引脚 I/O 密度和硅通孔（TSV）形成。由比利时 imec 托管的 NanoIC 中试线是一个重要的研发基础设施，得到弗拉芒政府的支持，并获得欧盟芯片联合行动的资金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Interposer">Interposer - Wikipedia</a></li>
<li><a href="https://www.manufacturingmag.com/article/silicon-interposers-and-the-gap-in-us-advanced-packaging">What Is a Silicon Interposer? CoWoS and the US Supply Chain</a></li>
<li><a href="https://www.imec-int.com/en/what-we-offer/nanoic-pilot-line-accelerating-beyond-2nm-innovation-across-europe">NanoIC pilot line | imec</a></li>

</ul>
</details>

**标签**: `#Silicon Interposers`, `#Advanced Packaging`, `#Imec`, `#Chiplets`, `#Semiconductors`

---

<a id="item-11"></a>
## [Linux 内存管理审核员因泛滥的 AI 垃圾补丁辞职](https://www.tomshardware.com/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back) ⭐️ 7.5/10

一位资深 Linux 内核审核员已正式辞去其内存管理职责。这一决定是由于低质量的 AI 生成补丁涌入速度不可持续，且团队人手严重不足。 这标志着 AI 生成代码的规模已超出开源维护的能力极限，成为关键的临界点。它为更广泛的软件行业提供了关于 AI 编程趋势可持续性的警示。 核心问题不在于单个漏洞，而在于低质量提交与可用审核人手之间的压倒性比例。这种规模的“AI 垃圾代码”使得内存管理等关键内核基础设施当前的维护模式在结构上已不可持续。

rss · Tom's Hardware · 11月11日 12:30

**背景**: Linux 内核是一个庞大的协作项目，社区提交的代码补丁必须由专门的维护者进行人工审查后才能被合并。内存管理是内核中最复杂的子系统之一，需要严格的审查标准以防止系统崩溃。随着 AI 编程工具变得更加普及，自动化和半自动化代码提交的激增，往往缺乏内核开发者的上下文理解能力。

**标签**: `#Linux`, `#AI Coding`, `#Open Source`, `#Kernel Development`

---

<a id="item-12"></a>
## [AMD MEXT 技术使用一半内存即可实现 95%服务器性能](https://www.tomshardware.com/pc-components/cpus/amd-shares-how-it-can-retain-95-percent-of-server-performance-with-just-half-the-dram-sidestepping-memory-shortages-with-mext-tech-powers-over-100-servers-already-running-with-plans-to-expand-to-2-000-servers-in-2027) ⭐️ 7.5/10

AMD 正在其内部 IT 基础设施中部署其收购的 MEXT 技术，声称服务器在特定工作负载下可使用 50% 的 DRAM 容量并保留 95% 的性能。该公司目前已有 145 台服务器运行 MEXT，并计划在 2027 年将该部署扩展至 2,000 台。 该创新为面临严重 DRAM 供应短缺和价格飙升的数据中心运营商提供了一种具有成本效益的变通方案，可大幅降低 AI 和通用计算系统的硬件成本。它展示了从单纯依赖芯片制造进步向采用 AI 驱动的软件内存优化技术以解决基础设施瓶颈的转变。 MEXT 使用 AI 预测内存需求，将冷页卸载到闪存存储，并主动将即将使用的页面前移回 DRAM。在极端情况下，该技术可将物理 DRAM 需求减少多达 75%，从而以更低的成本有效增加可用内存容量，而非添加物理芯片。

rss · Tom's Hardware · 11月11日 12:00

**背景**: MEXT 是 AMD 收购的 AI 驱动内存优化技术，旨在无需更改硬件即可解决数据中心瓶颈。DRAM 目前占服务器总成本的比例高达 75%，使得供应链短缺成为扩展云基础设施的关键问题。通过使用预测软件管理内存分层，企业可以使用比 DRAM 更便宜且更充裕的闪存作为下层存储，从而以接近满性能的方式运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/amd-mext-memory-solution-flash-repaces-dram-same-performance/">AMD Unveils MEXT Memory Solution: Leverages Flash ... - Wccftech</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/11/news-amd-taps-flash-based-mext-amid-memory-crunch-aims-to-cut-dram-needs-by-up-to-75/">[News] AMD Taps Flash-Based MEXT amid Memory Crunch, Aims to ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#MEXT`, `#DRAM`, `#Server Performance`, `#Memory Optimization`

---

<a id="item-13"></a>
## [马斯克的 xAI 拟在德州建造 240 亿美元燃气 AI 数据中心面临审批](https://www.tomshardware.com/tech-industry/data-centers/elon-musk-wants-to-build-a-new-gas-powered-data-center-in-starbase-texas-usd24-billion-site-goes-up-for-approval-in-december-but-could-face-headwinds-from-new-governor) ⭐️ 7.5/10

埃隆·马斯克正在申请批准在得克萨斯州星际基地建造一座耗资 240 亿美元的燃气 AI 数据中心。该项目可能面临当地官员的阻力以及新的州级监管挑战，是 xAI 扩展计算基础设施的关键一步。 该项目凸显了大规模 AI 模型训练对电力的巨大需求，以及数据中心在过渡期对天然气的依赖。得克萨斯州的不确定性监管可能会为未来的 AI 基础设施审批树立先例。 xAI 已利用五台 380 兆瓦的天然气涡轮机确保了为其超级计算机提供电力。星际基地是得克萨斯州的一个 C 类城市，这种身份限制了其征收某些税种和监管复杂项目的权限。

rss · Tom's Hardware · 11月11日 11:30

**背景**: 星际基地是位于得克萨斯州南部、以 SpaceX 星舰发射场为中心的快速增长社区。随着 AI 计算负载的增长，由于电网瓶颈，数据中心越来越多地转向天然气涡轮机以获取快速且大容量的电力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c39j8rj4nmmo">Elon Musk's Starbase in Texas will officially become a city</a></li>
<li><a href="https://www.techtimes.com/articles/313840/20260107/elon-musks-xai-secures-massive-power-infrastructure-five-380-mw-natural-gas-turbines.htm">Elon Musk's xAI Secures Massive Power Infrastructure with Five 380...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Data Centers`, `#Energy`, `#Elon Musk`, `#Hardware`

---

<a id="item-14"></a>
## [Ukrainian drone operations squeezed by fiber optic cable shortage triggered by AI data center buildouts](https://www.tomshardware.com/tech-industry/drones/data-center-demand-for-fiber-optics-squeezes-ukrainian-drone-operations-supply-crunch-has-incurred-6x-10x-cost-increase-for-critical-cabling) ⭐️ 7.5/10

Ukrainian drone manufacturers are facing significant supply chain disruptions and cost increases for jam-proof drones due to a global fiber optic cable shortage driven by AI data center expansion.

rss · Tom's Hardware · 11月11日 11:00

**标签**: `#Supply Chain`, `#AI Infrastructure`, `#Defense Technology`, `#Fiber Optics`, `#Geopolitics`

---

<a id="item-15"></a>
## [AWS Finally Built Its Own AWS Emulator](https://github.com/aws/aws-emulator) ⭐️ 7.0/10

AWS has released its own open-source AWS emulator, prompting discussion about its utility compared to existing tools like Moto and LocalStack for testing and development.

hackernews · super_linear · 11月11日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50456631)

**标签**: `#cloud-computing`, `#aws`, `#devops`, `#testing`, `#infrastructure-as-code`

---

<a id="item-16"></a>
## [Can a Linear Program Do Weight-Space Programming?](https://nathan.rs/posts/weight-space-lp/) ⭐️ 7.0/10

An analysis proposing that Linear Programming can be used to edit neural network weights by defining linear constraints in weight-space, offering a structured alternative to gradient-based optimization for specific model modification tasks.

hackernews · emschwartz · 11月11日 12:30 · [社区讨论](https://news.ycombinator.com/item?id=50452655)

**标签**: `#Linear Programming`, `#Neural Networks`, `#Model Editing`, `#Optimization`, `#AI Research`

---

<a id="item-17"></a>
## [Pharo in the Browser with WebAssembly](https://massimo-nocentini.github.io/pharo-vm/world.html) ⭐️ 7.0/10

A demonstration of the Pharo Smalltalk virtual machine running in a web browser using WebAssembly, allowing users to interact with a live coding environment directly online.

hackernews · xkriva11 · 11月11日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=50453763)

**标签**: `#WebAssembly`, `#Smalltalk`, `#Pharo`, `#Interpreter`, `#Browser`

---

<a id="item-18"></a>
## [SemiWiki 解析硅衬底与 SOI 在晶体管中的关键作用](https://semiwiki.com/semiconductor-manufacturers/soitec/376187-semiconductors-and-soi-from-bulk-wafers-to-engineered-substrates/) ⭐️ 7.0/10

SemiWiki 上的一篇深度文章解释了硅衬底的特性（如 1.12 eV 带隙和高质量的本征 SiO2 氧化物）如何决定现代晶体管的性能。文章概述了从标准体晶圆到工程化绝缘体上硅 (SOI) 衬底的转变过程。 这一教育资源帮助行业专业人士和学生理解驱动芯片设计演进的材料科学限制。它阐明了为什么衬底工程对于减少先进半导体节点中的漏电并提高功耗效率至关重要。 文章强调，尽管有源晶体管位于晶体顶部的几百纳米内，但晶圆的其余部分可能成为机械负担。它特别指出硅的中等带隙（1.12 eV）和优异的本征氧化物质量是其在行业中占据主导地位的主要原因。

rss · SemiWiki · 11月11日 18:00

**背景**: 在标准的半导体制造中，体硅晶圆被用作构建芯片的基础材料。随着晶体管尺寸缩小，底层体硅带来的电气干扰成为主要障碍，从而推动了绝缘体上硅（SOI）技术的发展。SOI 晶圆在有源硅层和衬底之间使用绝缘层（通常是二氧化硅），从而显著减少了寄生效应和功耗。

**标签**: `#Semiconductors`, `#SOI`, `#Material Science`, `#Transistors`, `#Wafer Technology`

---

<a id="item-19"></a>
## [Mobilint 与 Chips&Media 量产面向人形机器人的边缘 AI 芯片](https://semiwiki.com/ip/chipsmedia/375958-why-video-processing-matters-for-the-next-generation-of-robots/) ⭐️ 7.0/10

韩国公司 Mobilint 和 Chips&Media 于 11 月 4 日宣布，已开始量产集成了 Chips&Media 视频编解码技术的新一代边缘 AI 芯片。这些芯片专为处理多摄像头人形机器人产生高带宽视频流而设计。 由于人形机器人依赖多个摄像头来导航复杂环境，高效的本地视频处理对于管理带宽和延迟至关重要。将专用编解码 IP 集成到边缘 AI 芯片中，解决了将机器人应用扩展至商业化生产过程中的关键瓶颈。 Mobilint 与 Chips&Media 的合作重点是将视频编解码 IP 直接集成到边缘 AI 芯片中，以便在本地处理数据而非将其卸载。具体的目标应用是多摄像头人形机器人，其产生的视频数据量超出了传统系统的处理能力。

rss · SemiWiki · 11月11日 14:00

**背景**: 边缘 AI 指的是在本地硬件设备上而非云端运行人工智能模型，从而减少延迟和带宽使用。在机器人领域，特别是人形机器人中，来自多个摄像头的视觉感知会产生大量数据，需要视频编解码器等专用硬件来高效压缩和处理这些信息。

**标签**: `#robotics`, `#edge-ai`, `#video-processing`, `#hardware`, `#chips`

---

<a id="item-20"></a>
## [挪威部署 3500 台 AI 激光无人机保护三文鱼](https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths) ⭐️ 6.5/10

Stingray Marine Solutions 已将挪威三文鱼农场中的水下 AI 激光无人机部署规模扩大至 3500 台，现已保护 1.12 亿尾鱼类。这些自主潜航器 24/7 全天候运行，无需使用有害化学药浴即可消除海水虱。 这种无化学物质的方法显著降低了水产养殖行业传统被动治疗带来的环境风险和鱼类死亡率。它标志着向可持续的自动化害虫控制迈出了重要一步，最大限度地减少了对生态系统的影响。 这些无人机利用立体相机和蓝光照明确分寄生虫和鱼皮，发射精确的激光脉冲使虱子凝固，同时宿主不受伤害。每个单元最多可发射 5 次激光脉冲，以有效去除单个寄生虫。

rss · Tom's Hardware · 11月11日 10:00

**背景**: 海水虱是一种以养殖三文鱼为食的寄生虫，会削弱鱼类并引发对化学药浴或机械去除等应激性治疗的需求。光学除虱是一种新兴技术，使用机器视觉和定向激光来杀死自由游动鱼类身上的寄生虫，为传统方法提供了一种持续且侵入性更小的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thefishsite.com/articles/interest-grows-in-new-salmon-licezapping-laser">Interest Grows in New Salmon Lice -Zapping Laser | The Fish Site</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0044848625007963">Control of salmon lice through optical delousing in ...</a></li>

</ul>
</details>

**标签**: `#Autonomous Systems`, `#AI Application`, `#Robotics`, `#Agricultural Technology`, `#Sustainability`

---