---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> 从 114 条内容中筛选出 20 条重要资讯。

---

1. [JEDEC 发布 SPHBM4 标准，在有机基板上实现 HBM4 级带宽](#item-1) ⭐️ 8.5/10
2. [TrendForce：2026 下半年 SLC NAND 价格将暴涨 120–170%](#item-2) ⭐️ 8.0/10
3. [南亚科技投资 150 亿美元建设月产能 4.5 万片晶圆厂](#item-3) ⭐️ 8.0/10
4. [长鑫存储 DRAM 晶圆产能将于 2026 年底接近美光水平](#item-4) ⭐️ 7.5/10
5. [Intel 18A 硅片通过航天级认证，Starfire SoC 问世](#item-5) ⭐️ 7.5/10
6. [美光投资 5 亿美元支持环球晶圆德州晶圆厂，推进 2500 亿美元美国计划](#item-6) ⭐️ 7.5/10
7. [Meta 将 Hyperion AI 超算集群扩至 5GW，路易斯安那州投资超 500 亿美元](#item-7) ⭐️ 7.5/10
8. [逐际动力完成近 2 亿美元 Pre-IPO 轮融资，估值达 150 亿元](#item-8) ⭐️ 7.3/10
9. [「爱诗科技」完成 29.8 亿元 C 轮融资](#item-9) ⭐️ 7.3/10
10. [苹果 SpeechAnalyzer API 基准测试：比 Whisper 更快，精度略低](#item-10) ⭐️ 7.0/10
11. [Linux SMP 移植到 Sega 32X，仅使用软件实现同步](#item-11) ⭐️ 7.0/10
12. [英特尔向莱克斯利普投资 57 亿美元](#item-12) ⭐️ 7.0/10
13. [中国电网级电池储能装机容量激增至 140 吉瓦](#item-13) ⭐️ 7.0/10
14. [特斯拉 A15 芯片将在三星和台积电双源代工，采用 2nm 工艺](#item-14) ⭐️ 7.0/10
15. [台积电 6 月营收创纪录达 137.5 亿美元，N2 2 纳米进入量产](#item-15) ⭐️ 6.5/10
16. [AMD FSR 多帧生成技术开发中，最高支持 8x 模式](#item-16) ⭐️ 6.5/10
17. [特斯拉 AI5 芯片在三星代工完成 2nm 级流片](#item-17) ⭐️ 6.5/10
18. [苹果 M7 Ultra 据传配备 1.5TB 内存和 Blackwell 级 AI 性能](#item-18) ⭐️ 6.5/10
19. [ASRock Rack 基于 NVIDIA Thor 工业 SoC 打造边缘服务器](#item-19) ⭐️ 6.5/10
20. [字节探索自动驾驶，Seed 世界模型团队负责｜36 氪独家](#item-20) ⭐️ 6.3/10

---

<a id="item-1"></a>
## [JEDEC 发布 SPHBM4 标准，在有机基板上实现 HBM4 级带宽](https://www.techpowerup.com/350725/jedec-sphbm4-standard-enables-hbm4-class-bandwidth-on-organic-substrates) ⭐️ 8.5/10

JEDEC 发布了 JESD330-4 标准封装高带宽内存（SPHBM4）标准，该标准使用与 HBM4 相同的 DRAM 芯片，但引入了新的接口基底芯片，使其能够安装于标准有机基板而非硅基板。通过 4:1 信号序列化技术，SPHBM4 将数据信号数量从 HBM4 的 2048 个减少到仅 512 个，同时保持等效的聚合带宽。 该标准通过消除对昂贵硅中介层和先进封装技术的需求，可能显著降低 AI 加速器部署 HBM4 级内存的成本和复杂度。它使更广泛的应用和厂商能够获得 HBM4 级别的性能，特别是那些不具备或不愿承担尖端 2.5D/3D 封装技术成本的厂商。 4:1 序列化技术在更高频率下运行，以补偿引脚数量的减少，从而实现与 HBM4 相同的聚合吞吐量。放宽的凸点间距要求是有机基板集成的关键，因为有机基板无法实现传统 HBM4 的 2048 信号接口所需的精细间距。

rss · TechPowerUp News · 7月13日 15:34

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，最初由三星、AMD 和 SK 海力士开发，广泛用于需要海量内存带宽的 AI 加速器和 GPU。传统 HBM 集成需要使用硅中介层（一种用于在 GPU/AI 芯片和 HBM 堆栈之间路由信号的薄硅层）的先进封装技术，这种封装昂贵且制造复杂。有机基板（传统芯片封装中使用的类 PCB 材料）成本远低得多，但无法支持 HBM 宽接口所需的超精细凸点间距。JEDEC 是微电子行业的主要标准机构，其 HBM 标准（JESD235 系列）自 2015 年以来定义了一代又一代的内存规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates">JEDEC releases new SPHBM 4 standard to slash AI... | Tom's Hardware</a></li>
<li><a href="https://www.electronicdesign.com/technologies/embedded/article/55358355/eliyan-hbm4-vs-sphbm4-breaking-the-ai-memory-wall-with-next-gen-high-bandwidth-memory">HBM 4 vs. SPHBM4: Breaking the AI Memory Wall... | Electronic Design</a></li>
<li><a href="https://www.jedec.org/news/pressreleases/new-jedec®-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates">New JEDEC ® SPHBM 4 Standard Enables HBM4-Class... | JEDEC</a></li>

</ul>
</details>

**标签**: `#HBM4`, `#JEDEC`, `#memory-standards`, `#AI-hardware`, `#semiconductor-packaging`

---

<a id="item-2"></a>
## [TrendForce：2026 下半年 SLC NAND 价格将暴涨 120–170%](https://www.dramexchange.com/WeeklyResearch/Post/2/12765.html) ⭐️ 8.0/10

TrendForce 预测，2026 年下半年 SLC NAND 闪存价格将上涨 120%–170%，主要原因是小众市场需求持续旺盛，以及成熟制程 NAND 产能正加速向更高附加值的 MLC 产品转移。 如此幅度的价格上涨将对依赖 SLC NAND（因其卓越耐久性和可靠性）的嵌入式系统、工业自动化、汽车电子及物联网设备制造商产生重大影响。SLC 供应趋紧可能打乱长生命周期产品的设计，迫使企业进行昂贵的重新设计或元件替换。 SLC（单层单元）每个单元存储 1 比特，拥有 5 万至 10 万次擦写周期，错误率较低仅需 1 位 ECC 纠错；MLC 则将存储密度翻倍，但错误率显著升高，需要 4 位 ECC 纠错。各厂商正将老旧平面 NAND 晶圆厂产能转向 3D NAND 及更高密度的 MLC/TLC/QLC 产品，从结构上削减了 SLC 的供应，而非新增产能。

rss · DRAMeXchange (TrendForce) · 7月13日 15:16

**背景**: NAND 闪存分为多种单元类型：SLC（每单元 1 比特）、MLC（每单元 2 比特）、TLC（每单元 3 比特）和 QLC（每单元 4 比特）。比特密度越高，每 GB 成本越低，但耐久性和可靠性也随之下降，因此尽管 SLC 价格更高，仍是工业、汽车、航空航天及关键任务应用的首选。NAND 行业正经历结构性产能重构，比特增长通过技术节点升级实现而非新建晶圆厂，行业分析师指出新增产能最早要到 2027 年底才能缓解供应压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.delkin.com/blog/slc-nand-vs-mlc-nand/">SLC NAND vs . MLC NAND | Delkin Devices</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multi-level_cell">Multi - level cell - Wikipedia</a></li>
<li><a href="https://www.isaiahresearch.com/Insight/Detail/105">NAND Flash Supply Forecast 2022-2027: Structural Shift & AI Impact</a></li>

</ul>
</details>

**标签**: `#NAND-flash`, `#memory-pricing`, `#semiconductor-industry`, `#market-forecast`, `#TrendForce`

---

<a id="item-3"></a>
## [南亚科技投资 150 亿美元建设月产能 4.5 万片晶圆厂](https://www.electronicsweekly.com/news/business/899817-2026-07/) ⭐️ 8.0/10

台湾 DRAM 厂商南亚科技宣布投资 150 亿美元建设一座月产能达 4.5 万片晶圆的工厂，明年的资本支出将翻两番，达到 62 亿美元。

rss · Electronics Weekly · 7月13日 05:25

**标签**: `#semiconductors`, `#DRAM`, `#manufacturing`, `#Nanya`, `#capex`

---

<a id="item-4"></a>
## [长鑫存储 DRAM 晶圆产能将于 2026 年底接近美光水平](https://www.techpowerup.com/350726/chinese-cxmt-to-match-microns-dram-manufacturing-capacity-this-year) ⭐️ 7.5/10

根据 Citrini Research 的分析，中国的 CXMT 预计到 2026 年底将实现每月约 35 万片 DRAM 晶圆的产量，接近美光估计的每月 37.5 万片。CXMT 通过将洁净室建设周期压缩至约 12 个月来实现这一扩张，而行业通常需要 21 到 24 个月。 CXMT 接近与 DRAM 三巨头之一的美光平起平坐，标志着全球内存市场的重大转变，在 AI 驱动需求加剧供应链紧张的情况下，可能进一步加剧价格竞争。这也凸显了中国半导体企业在被美国制裁限制获取先进 EUV 光刻设备的情况下，依然在快速扩张产能。 CXMT 被列入美国实体清单，无法采购先进的 EUV 光刻机，因此依赖较旧的 DUV 光刻设备并结合多重图形技术来弥补 EUV 的缺失。其 12 个月的洁净室建设周期约为行业标准 21 到 24 个月的一半，是一项突出的运营成就。

rss · TechPowerUp News · 7月13日 16:00

**背景**: CXMT（长鑫存储，ChangXin Memory Technologies）是中国最大的本土 DRAM 制造商，总部位于安徽合肥，成立目的是满足中国国内的内存需求。全球 DRAM 市场由三星、SK 海力士和美光三巨头主导，因此 CXMT 的快速崛起代表着潜在第四大主要供应商的出现。洁净室是硅晶圆制造所需的超洁净受控环境，而 EUV（极紫外）光刻是当前最先进的芯片曝光技术，DUV（深紫外）作为较旧的代次，可通过多重图形技术在更高成本和复杂度下部分替代 EUV。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.techpowerup.com/350726/chinese-cxmt-to-match-microns-dram-manufacturing-capacity-this-year">Chinese CXMT to Match Micron's DRAM Manufacturing Capacity This...</a></li>
<li><a href="https://www.scmp.com/business/china-business/article/3354223/why-chinese-dram-maker-cxmts-ipo-attracting-so-much-attention">Why is Chinese DRAM maker CXMT ’s IPO attracting so much attention?</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#memory-manufacturing`, `#CXMT`, `#semiconductor-industry`

---

<a id="item-5"></a>
## [Intel 18A 硅片通过航天级认证，Starfire SoC 问世](https://www.techpowerup.com/350713/intel-18a-silicon-goes-to-space-with-starfire-processors) ⭐️ 7.5/10

Intel 18A 工艺节点已正式获得航天级认证，全新 Starfire SoC 系列专为轨道计算设计。该系列包含两个 SKU——低功耗版（10W TDP，P 核 1.0 GHz）和性能版（35W TDP，P 核 3.1 GHz），均配备 4 个 P 核、4 个 LPE 核、基于 Intel 3 工艺的 GPU 芯片（含 4 个 Xe 核、64 个 EU）以及算力高达 75 TOPS 的 NPU。样品预计于本季度（Q3）推出。 这一里程碑验证了 Intel 先进 18A 工艺在极端环境应用中的可行性，为美国政府提供了国产的、具备抗辐射加固能力的先进制程航天处理器。它也标志着 Intel 代工业务在航空航天和国防市场不断扩展，而该领域对国产供应链安全的要求极为严格，具有重要的战略意义。 该 SoC 可在 -55°C 至 125°C 的结温范围内工作，并获得 TID（总剂量效应）、SEL（单粒子锁定）和 SEE（单粒子效应）抗辐射加固认证。其 chiplet 设计将 18A 计算芯片与 Intel 3 GPU 芯片相结合，并集成 NPU，可提供 45 TOPS（低功耗版）和 75 TOPS（性能版）的 INT8 算力，适合在轨 AI 推理负载。

rss · TechPowerUp News · 7月13日 11:38

**背景**: Intel 18A（1.8 埃米）是先进的半导体工艺节点，结合了 RibbonFET 环栅晶体管和 PowerVia 背面供电（BSPDN）技术，是首个实现量产的背面供电网络。LPE 核（低功耗高效核）是 Intel 首次在 Meteor Lake 中引入的超低功耗核心，位于独立的 SoC 芯片上，可高效处理轻负载任务。航天级芯片必须能够承受极端温度、真空环境和电离辐射，需要通过 TID（总剂量效应）、SEL（单粒子锁定）和 SEE（单粒子效应）等严格的抗辐射加固认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-06/foundry-18a-technology-brief.pdf">Intel Foundry Technology Brief: Intel 18A Process Node Family</a></li>
<li><a href="https://www.intel.com/content/www/us/en/support/articles/000099551/processors/intel-core-ultra-processors.html">Why Are the Efficient Cores Called Low Power Efficient Cores in Lunar Lake?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meteor_Lake">Meteor Lake - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Intel`, `#semiconductor`, `#space-computing`, `#Intel-18A`, `#SoC`

---

<a id="item-6"></a>
## [美光投资 5 亿美元支持环球晶圆德州晶圆厂，推进 2500 亿美元美国计划](https://www.tomshardware.com/tech-industry/semiconductors/micron-commits-500-million-to-globalwafers-texas-wafer-plant-as-it-raises-us-spending-to-250-billion) ⭐️ 7.5/10

美光承诺向环球晶圆位于德州的新建硅晶圆制造工厂投资 5 亿美元，这是其总额达 2500 亿美元的在美投资计划的一部分，目标是在 2030 年代中期实现 40%的 DRAM 在美国本土生产。 这项投资通过减少对海外晶圆生产（尤其是东亚地区）的依赖，强化了美国半导体供应链，并在地缘政治紧张局势持续的背景下支持了半导体制造业回流美国的努力。在 AI 和数据中心需求推动存储芯片需求激增的背景下，此举标志着美光对本土芯片制造的长期承诺。 环球晶圆的德州工厂被描述为该公司最新、最大且最先进的硅晶圆制造厂，主要生产 300mm 抛光片和外延片。2500 亿美元的投资承诺持续至 2035 年，是单一公司在美国做出的最大规模半导体资本支出承诺之一。

rss · Tom's Hardware · 7月13日 17:09

**背景**: 硅晶圆是薄片状的晶体硅，是制造集成电路和其他半导体器件的基础基底材料。DRAM（动态随机存取存储器）是一种易失性存储器，使用一个晶体管和一个电容器来存储每一位数据，是计算机、服务器和移动设备中最常用的内存类型。环球晶圆总部位于台湾，截至 2022 年是全球第三大硅晶圆供应商。美国推动半导体制造业回流的努力由《CHIPS 法案》和近年来全球供应链中断所暴露的脆弱性所加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GlobalWafers">GlobalWafers - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Random-access_memory">Random - access memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wafer_(electronics)">Wafer (electronics) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply-chain`, `#DRAM`, `#manufacturing`, `#investment`

---

<a id="item-7"></a>
## [Meta 将 Hyperion AI 超算集群扩至 5GW，路易斯安那州投资超 500 亿美元](https://www.tomshardware.com/tech-industry/data-centers/meta-expands-colossal-hyperion-ai-supercluster-plans-to-5gw-pushes-louisiana-investment-past-usd50-billion-as-ai-race-accelerates-says-it-plans-to-invest-over-usd1-billion-in-local-infrastructure-improvements) ⭐️ 7.5/10

Meta 正在将其位于路易斯安那州里奇兰教区的 Hyperion AI 超算集群园区从 2GW 扩展至 5GW，总投资额超过 500 亿美元，并承诺投入逾 10 亿美元用于当地基础设施建设。该项目于 2024 年 12 月首次公布时为 100 亿美元，将为 Meta 超级智能实验室提供算力支撑。 此次扩建使 Hyperion 跻身全球最大 AI 基础设施项目之列，标志着 Meta 在超大规模云厂商竞争加剧之际，积极抢占行业领先算力的决心。5GW 的规模远超普通数据中心，反映了训练前沿 AI 模型所需资本的不断攀升。 Hyperion 园区由 PIMCO 和 Blue Owl Capital 提供融资支持，CEO 马克·扎克伯格表示该设施将提供业界最高的单研究人员算力。与传统数据中心不同，超算集群密集部署了针对 AI 工作负载优化的 GPU 和专用硬件，而 GW 级规模代表了新的基础设施标准——预计 2026 年仅有少数几家超大规模云厂商的不同设施将达到这一量级。

rss · Tom's Hardware · 7月13日 13:25

**背景**: AI 超算集群是由数万台 GPU 通过高带宽网络互联组成的超大规模计算设施，专门用于训练大型 AI 模型。GW（吉瓦）级别的电力指标至关重要，因为每 GW 约等于一座大型核反应堆的发电量，足以为数十万户家庭供电，体现了前沿 AI 训练的惊人能耗。根据 Epoch AI 的研究，预计 2026 年将有至少五座 1GW 及以上的数据中心上线，由 xAI、微软和 Meta 等不同超大规模云厂商运营，标志着数据中心规模进入新时代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/data-centers/meta-expands-colossal-hyperion-ai-supercluster-plans-to-5gw-pushes-louisiana-investment-past-usd50-billion-as-ai-race-accelerates-says-it-plans-to-invest-over-usd1-billion-in-local-infrastructure-improvements">Meta expands colossal Hyperion AI supercluster plans to 5GW, pushes Louisiana investment past $50 billion as AI race accelerates — says it plans to invest over $1 billion in local infrastructure improvements | Tom's Hardware</a></li>
<li><a href="https://qz.com/what-are-ai-superclusters">Big Tech bets on AI superclusters. What are they? - Quartz</a></li>
<li><a href="https://qz.com/ai-data-centers-gigawatt-power-grid-strain-051126">AI data centers pass 1 gigawatt and strain the U.S. power grid</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Meta`, `#data centers`, `#supercomputing`, `#AI race`

---

<a id="item-8"></a>
## [逐际动力完成近 2 亿美元 Pre-IPO 轮融资，估值达 150 亿元](https://36kr.com/p/3893976502287618?f=rss) ⭐️ 7.3/10

中国人形机器人公司逐际动力（LimX Dynamics）宣布完成近 2 亿美元的 Pre-IPO 轮融资，投后估值约 150 亿元人民币，过去半年累计融资额已达 4 亿美元。公司已于 2026 年 3 月完成股改，并在此前开启了 IPO 进程。 这是中国人形机器人/具身智能领域规模最大的 Pre-IPO 融资之一，显示出市场对赛道的高度认可，也预示着 IPO 前的竞争日趋激烈。本轮资金将加速逐际动力数千台全自主人形机器人的规模化部署，深化其 System 0/1/2 三层 AI 架构，并推动其在中东、欧洲及亚洲的全球化布局。 逐际动力的三层 AI 架构包括 System 0（全身运动基础模型）、System 1（人形机器人 VLA/WAM 能力）和 System 2（COSA——由大语言模型和世界模型驱动的具身智能体操作系统）。其产品包括 5 月发布的 LimX Luna（全尺寸 160cm，27 个自由度）以及模块化多形态机器人 TRON 2，累计获得数千台订单，其中过半来自海外客户。

rss · 36氪 · 7月14日 00:46

**背景**: 人形机器人与具身智能——即将 AI 模型集成到能在真实世界中感知和行动的物理机器人中——已成为全球最热门的融资赛道之一。视觉-语言-动作（VLA）模型将大型视觉语言模型扩展为从视觉观察和语言指令生成机器人动作，而世界动作模型（WAM）则增加了对物理动力学的预测能力。逐际动力于 2026 年 1 月发布的 COSA（具身智能体认知操作系统）被定位为全球首个面向人形机器人的智能体操作系统，支持自主感知、推理与行动。公司还开源了 FluxVLA Engine，覆盖数据处理、仿真训练、真机迭代和硬件部署的完整工具链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.therobotreport.com/limx-dynamics-demonstrates-latest-humanoid-robot-motions/">LimX Dynamics demonstrates latest humanoid ... - The Robot Report</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/CHINA-LIMX-UNVEILS-ROBOT-OPERATING-SYSTEM">LimX unveils operating system for humanoid robots to navigate alone</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision-language-action_model">Vision-language-action model</a></li>

</ul>
</details>

**标签**: `#humanoid-robotics`, `#embodied-ai`, `#funding`, `#limx-dynamics`, `#china-tech`

---

<a id="item-9"></a>
## [「爱诗科技」完成 29.8 亿元 C 轮融资](https://36kr.com/newsflashes/3894795352669446?f=rss) ⭐️ 7.3/10

PixVerse（爱诗科技）完成 29.8 亿元 C 轮融资，由阿里巴巴领投，资金将用于推进视频生成基础模型和实时世界模型的研发。

rss · 36氪 · 7月14日 01:10

**标签**: `#funding`, `#video-generation`, `#world-models`, `#AI-investment`, `#China-AI`

---

<a id="item-10"></a>
## [苹果 SpeechAnalyzer API 基准测试：比 Whisper 更快，精度略低](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 7.0/10

对苹果新推出的 SpeechAnalyzer API（随 iOS 26 引入）的技术基准测试显示，它比 OpenAI 的 Whisper 快得多，并支持流式转录，但精度略低。该测试将苹果的设备端语音转文字方案与 Whisper 及其前代 SFSpeechRecognizer 进行了对比。 由于 SpeechAnalyzer 免费且内置于苹果操作系统中并支持流式转录，它对那些仅仅包装 Whisper 提供转录服务的付费第三方应用构成了直接威胁。这一进展标志着苹果正在推动端侧 AI 的发展，缩小了专有方案与开源语音识别在日常使用场景中的差距。 SpeechAnalyzer 取代了 iOS 10 引入的 SFSpeechRecognizer，提供实时流式转录——用户边说话文字边出现，这是相比 Whisper 批量处理方式的重大用户体验升级。然而，该基准测试仅与 Whisper 进行了比较，未与当前最先进的模型（如英伟达的 Nemotron/Parakeet 或 Mistral 的 Voxtral）对比。

hackernews · get-inscribe · 7月13日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**背景**: 自动语音识别（ASR）是将口语转换为书面文本的技术，广泛应用于转录、字幕生成和语音助手等领域。OpenAI 于 2022 年发布的 Whisper 是一款流行的开源 ASR 模型，使用 68 万小时多语言数据训练而成，并催生了大量付费封装应用。苹果在 WWDC 2025 上宣布的新 SpeechAnalyzer API 是其旧版 SFSpeechRecognizer 框架的替代品，将现代 AI 驱动的转录功能原生集成到 iOS 和 macOS 设备中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer-mdn.apple.com/videos/play/wwdc2025/277/">Bring advanced speech -to-text to your app with... - Apple Developer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)">Whisper ( speech recognition system) - Wikipedia</a></li>
<li><a href="https://huggingface.co/spaces/hf-audio/open_asr_leaderboard">Open ASR Leaderboard - a Hugging Face Space by hf-audio</a></li>

</ul>
</details>

**社区讨论**: 社区普遍认为 Whisper 已不再是最佳基准测试对象，指出英伟达的 Nemotron 和 Parakeet、Mistral 的 Voxtral 以及 Cohere Transcribe 是目前更先进的 SOTA 选择。评论者强调流式支持是相比批量处理竞品的突出用户体验优势，不过也有人指出，对于像数学讲座字幕这类离线场景，Whisper 的精度仍然更优。多位用户提到 macOS 上现有的 Willow 等应用已经能提供近乎完美的实时转录，表明语音转文字正趋于成为一个被解决的问题，这可能会挤压付费 Whisper 封装应用的生存空间。

**标签**: `#speech-recognition`, `#apple`, `#whisper`, `#asr`, `#benchmarking`

---

<a id="item-11"></a>
## [Linux SMP 移植到 Sega 32X，仅使用软件实现同步](https://cakehonolulu.github.io/linux-on-32x/) ⭐️ 7.0/10

开发者 cakehonolulu 成功将支持 SMP 的 Linux 移植到 Sega 32X 扩展设备的双 Hitachi SH-2 处理器上。由于硬件缺乏任何同步原语，移植中采用了 Peterson 算法来实现互斥。该项目是作者此前为 Atari Jaguar 移植 Linux 工作的延续。 这一成果表明，通过巧妙的软件工程，即使在资源极为有限的复古硬件上也可以实现完整的对称多处理，为研究内核内部机制、并发算法以及硬件辅助同步的极限提供了一个教育窗口。它也拓展了复古计算和爱好者操作系统社区对 1990 年代消费级设备可行性的认知。 32X 中的 SH-2 CPU 不具备任何硬件原子的比较并交换（CAS）或测试并置位（test-and-set）操作，因此互斥完全通过 Peterson 算法实现——该算法仅依赖共享内存的读写操作，最初由 Gary L. Peterson 于 1981 年提出。有社区评论者提到了 Lamport 提出的相关快速互斥算法作为替代方案，另一位则提出了一个待解答的问题：SH-2 是否真的能写入卡带区域，这意味着目前的构建可能仅在模拟器中测试，而尚未在真实 32X 硬件上运行。

hackernews · cakehonolulu · 7月13日 18:18 · [社区讨论](https://news.ycombinator.com/item?id=48896600)

**背景**: Sega 32X 代号为"Project Mars"，是 1994 年为 Sega Genesis/Mega Drive 设计的扩展设备，旨在 Saturn 发布前将主机过渡到 32 位时代；它在 Genesis 原有的 Motorola 68000 之外，集成了两颗运行于 23 MHz 的 Hitachi SH-2 处理器。SH-2 是 Hitachi SuperH 家族的 32 位 RISC 内核，以紧凑的 16 位指令和分支延迟槽等典型 RISC 特性著称。Linux 中的 SMP（对称多处理）通常依赖比较并交换等硬件原子指令；Peterson 算法是一种经典的纯软件互斥技术，不需要此类硬件支持，因此非常适合移植到缺乏或不包含这些原语的老旧芯片上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/32X">32X - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Peterson's_algorithm">Peterson ' s algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SuperH">SuperH - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者们围绕具体技术细节展开了深入讨论：mikepavone 对该移植是在真实硬件上验证还是仅在模拟器中测试提出了疑问，并指出 SH-2 无法写入卡带区域这一已知限制。ajb 提到了 Lamport 的快速互斥算法作为一种相关同步方案；Dwedit 则提供了有价值的背景，将 SuperH 指令集与 ARM Thumb 进行了比较（提到 Hitachi 之间的专利交叉授权以及 SuperH 的分支延迟槽特性）。jonhohle 对尚未开发的潜力表示兴奋，询问了 I/O 选项，例如使用串口作为终端访问，并指出 Sega CD 扩展设备可以提供更多 RAM 和一颗速度更快的辅助 68000。

**标签**: `#linux-kernel`, `#embedded-systems`, `#retro-computing`, `#synchronization`, `#kernel-hacking`

---

<a id="item-12"></a>
## [英特尔向莱克斯利普投资 57 亿美元](https://www.electronicsweekly.com/news/business/intel-puts-5-7bn-into-leixlip-2026-07/) ⭐️ 7.0/10

英特尔宣布将投资 57 亿美元，用于改造其位于爱尔兰莱克斯利普的 Fab 34 工厂，以采用 Intel 3 工艺并扩大制造产能。

rss · Electronics Weekly · 7月13日 15:32

**标签**: `#semiconductors`, `#Intel`, `#manufacturing`, `#Intel 3 process`, `#fab investment`

---

<a id="item-13"></a>
## [中国电网级电池储能装机容量激增至 140 吉瓦](https://www.electronicsweekly.com/blogs/mannerisms/manuf/chinas-massive-battery-build-capacity-2026-07/) ⭐️ 7.0/10

中国的电网级电池储能装机容量从 2020 年仅有 2.4 吉瓦激增至 2025 年的超过 140 吉瓦，远远超过同期仅达到约 57 吉瓦的美国。 五年内约 58 倍的扩张凸显了中国在储能基础设施领域的领先优势，这对整合可再生能源、稳定电网以及支撑更广泛的清洁能源转型至关重要——也让中国在全球能源技术竞赛中占据战略优势。 中国超过 140 吉瓦的装机容量约为美国 57 吉瓦的 2.5 倍，不过这条新闻摘要缺乏关于电池化学体系、项目时间线，以及锂离子电池与替代技术之间部署分布的进一步技术细节。

rss · Electronics Weekly · 7月13日 13:01

**背景**: 电网级电池储能系统（BESS）是部署在电网上的大规模电池组，用于储存电能，帮助平衡供需，整合太阳能、风能等间歇性可再生能源，并提供电网稳定性服务。随着电池成本下降和可再生能源渗透率上升，储能的性价比和全球部署规模不断提升。以吉瓦（GW）计量的装机容量指的是储能系统可输出的峰值功率，与以吉瓦时（GWh）计量的总储能容量有所不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Battery_energy_storage_system">Battery energy storage system - Wikipedia</a></li>
<li><a href="https://innovationatwork.ieee.org/battery-energy-storage-systems-the-backbone-of-a-reliable-grid/">Battery Energy Storage Systems: The Backbone of a Reliable Grid</a></li>
<li><a href="https://www.powermag.com/group-forecasts-massive-increase-in-energy-storage-by-2030/">Group Forecasts Massive Increase in Energy Storage by 2030</a></li>

</ul>
</details>

**标签**: `#battery-storage`, `#energy-infrastructure`, `#china-manufacturing`, `#grid-energy`, `#clean-energy`

---

<a id="item-14"></a>
## [特斯拉 A15 芯片将在三星和台积电双源代工，采用 2nm 工艺](https://www.electronicsweekly.com/news/business/tesla-a15-chip-to-be-fabbed-at-samsung-and-tsmv-2026-07/) ⭐️ 7.0/10

特斯拉的下一代 A15 AI 芯片将在台积电位于台湾的 2nm 工艺产线和三星位于德克萨斯州泰勒市的 2nm 工艺产线上同步代工，台积电的亚利桑那工厂有可能被加入作为第三个生产基地。 在最先进的 2nm 节点上采取双源代工策略，表明特斯拉对其 AI 和自动驾驶领域自研芯片的战略加码，同时也通过跨地理区域和跨代工厂的方式分散供应链风险。 台积电的 N2 工艺已于 2025 年第四季度开始量产，采用第一代 nanosheet（GAA，环绕栅极）晶体管技术，在性能和功耗方面均有显著提升。三星的泰勒（德克萨斯州）工厂是其在美国布局的重要先进制造基地。特斯拉此前公布的 AI5 芯片号称比 HW4 芯片性能提升约 40 倍，原始算力提升 8 倍，内存提升 9 倍。

rss · Electronics Weekly · 7月13日 11:57

**背景**: 2nm 工艺节点是当前半导体制造的最前沿，取代了 3nm 节点。该节点的命名已不再对应实际的物理特征尺寸，而是代表着晶体管密度、性能和能效的代际提升。台积电和三星等头部代工厂在这一节点均采用 GAA（Gate-All-Around，环绕栅极）nanosheet 晶体管技术。特斯拉一直在开发自研 AI 推理芯片以驱动其全自动驾驶（FSD）硬件，HW4 为当前一代，AI5/A15 则代表其硅芯片路线图的下一代产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://wccftech.com/samsung-2nm-node-lands-tesla-ai5-chip-at-its-texas-taylor-fab-silencing-yield-doubters/">Samsung's 2nm Node Lands Tesla 's AI 5 Chip at Its Texas Taylor Fab...</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#semiconductors`, `#TSMC`, `#Samsung`, `#AI chips`

---

<a id="item-15"></a>
## [台积电 6 月营收创纪录达 137.5 亿美元，N2 2 纳米进入量产](https://www.techpowerup.com/350730/tsmc-achieves-record-usd-13-75-billion-revenue-in-june-2026) ⭐️ 6.5/10

台积电 2026 年 6 月单月营收达到约 137.5 亿美元（新台币 4,426.8 亿元），创历史新高，同比增长 67.9%，环比增长 6.2%。公司同时于 6 月启动了 N2（2 纳米）制程的大规模量产，AMD 的 EPYC「Venice」确认成为早期采用者，紧随其后的还有苹果即将推出的 A20 和 M6 SoC。 这一里程碑事件确认了 AI 驱动的需求持续推动半导体行业增长，也标志着全球领先代工厂的 2 纳米制程已进入商业化阶段。AMD 取代苹果成为台积电新制程的首批主要采用者，这是台积电客户层级的一次重要变化，可能会重塑服务器 CPU 和 AI 加速器领域的竞争格局。 N2 制程是台积电首次采用 GAAFET（全栅场效应晶体管/纳米片）晶体管架构，取代自 16 纳米以来一直使用的 FinFET 设计。AMD 的 EPYC Venice 将 N2 计算芯片与 CoWoS（Chip-on-Wafer-on-Substrate）先进封装技术相结合——这也是 NVIDIA H100/B200 和 AMD MI300/MI400 AI 加速器所使用的 2.5D 封装技术。2026 年上半年累计营收达 746.6 亿美元，同比增长 35.6%；2026 年第二季度营收同比增长 36%，达到 396 亿美元。

rss · TechPowerUp News · 7月13日 17:30

**背景**: 台积电是全球最大的合同半导体制造商（晶圆代工厂），为苹果、AMD 和 NVIDIA 等公司生产芯片设计，而非销售自有品牌产品。「2 纳米」（N2）等制程节点指的是制造技术的最小特征尺寸——更小的节点通常意味着更多的晶体管、更好的性能和更低的功耗。进入 2 纳米制程标志着一项根本性的架构变革：台积电的 N2 是其首个采用 GAA（全栅环绕）纳米片晶体管的制程节点，相比从 16 纳米到 3 纳米一直使用的 FinFET 晶体管，GAA 对沟道的静电控制能力更优。CoWoS 是台积电的先进 2.5D 封装技术，可将多个小芯片（chiplet）集成在硅中介层上，对于高带宽 AI 加速器至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/tsmc-n2-process-technology-wiki/">TSMC N2 Process Technology Wiki - SemiWiki</a></li>
<li><a href="https://semiconductorx.com/packaging-cowos.html">CoWoS Advanced Packaging: Chip-on-Wafer-on-Substrate, TSMC 2 ...</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#semiconductors`, `#AI infrastructure`, `#2nm`, `#financials`

---

<a id="item-16"></a>
## [AMD FSR 多帧生成技术开发中，最高支持 8x 模式](https://www.techpowerup.com/350704/amd-fsr-multi-frame-generation-with-up-to-8x-mode-in-development) ⭐️ 6.5/10

第三方工具 RadeonTuner 在最新的 Radeon 驱动程序中发现了 AMD 即将推出的多帧生成（MFG）技术的占位符支持，选项从 1x 到 8x 帧生成模式不等。在 RX 9060 XT 上的早期测试证实该功能目前无法使用，因为 AMD 尚未发布驱动其运行所需的底层模型。 这是 AMD 对 NVIDIA DLSS 4 多帧生成功能的直接回应，如果成功推出，可能会显著缩小 Radeon 与 GeForce GPU 在超采样和帧生成方面的差距。最高 8x 帧生成可以带来巨大的感知帧率提升，但在极端设置下会引发关于延迟和图像质量的疑问。 AMD 经常在新功能正式发布之前很早就植入占位符代码，目前在《Forza Horizon 6》、《Resident Evil 9》和《Death Stranding 2》等游戏中启用 MFG 的尝试均完全失败。RadeonTuner 开发者表示，该功能距离可用版本可能还需数月时间，而且尚不清楚 8x 模式是否会以其当前的占位符形式最终发布。

rss · TechPowerUp News · 7月13日 06:00

**背景**: FSR（FidelityFX Super Resolution）是 AMD 的空间和时间超采样套件，与 NVIDIA 的 DLSS 竞争；两者都可以在原生渲染的帧之间生成额外帧，以提升感知流畅度。NVIDIA 的 DLSS 4 引入了多帧生成（Multi Frame Generation），可在每个渲染帧的基础上合成最多三帧额外画面（总计 4x）。帧生成通过在帧之间插值运动矢量来工作，但生成的帧会增加延迟并可能引入伪影，这就是为什么 8x 这类激进模式在技术上极具挑战性且备受争议。RadeonTuner 是一个轻量级开源工具，可以访问通常只有通过 AMD 完整的 Adrenalin 软件套件才能看到的隐藏或高级 Radeon 驱动程序设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/350704/amd-fsr-multi-frame-generation-with-up-to-8x-mode-in-development">AMD FSR Multi-Frame Generation With Up to 8x Mode in ...</a></li>
<li><a href="https://wccftech.com/amd-radeon-drivers-hid-multi-frame-generation-mfg-8x-ray-regeneration-neural-radiance-overrides-hinting-at-a-bigger-fsr-push/">AMD Radeon Drivers Silently Add Multi Frame Generation “MFG ...</a></li>
<li><a href="https://github.com/dumbie/RadeonTuner">GitHub - dumbie/RadeonTuner: RadeonTuner is an easy to use ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#FSR`, `#GPU`, `#frame-generation`, `#Radeon`

---

<a id="item-17"></a>
## [特斯拉 AI5 芯片在三星代工完成 2nm 级流片](https://www.tomshardware.com/tech-industry/artificial-intelligence/teslas-ai5-with-2nm-class-node-tapes-out-at-samsung-foundry-production-starts-soon-months-after-tsmc-tape-out) ⭐️ 6.5/10

特斯拉的下一代 AI5 处理器已在三星代工（Samsung Foundry）完成 2nm 级工艺节点的流片，距其在台积电完成流片已有数月。三星预计将很快启动量产，成为该芯片的第二家代工合作伙伴。 这一双代工厂策略表明特斯拉正努力在全球两家最先进的代工厂之间分散其最关键 AI 芯片的供应链。通过在台积电和三星同时完成同一芯片设计的认证，特斯拉降低了供应风险，并在 2nm 级产能需求极其旺盛的背景下获得了定价与产能谈判的筹码。 两家代工厂均采用 2nm 级工艺节点——台积电的 N2 技术已于 2025 年第四季度进入量产，而三星的第二代 2nm（SF2P）工艺将于 2026 年逐步量产。AI5 预计将驱动特斯拉的完全自动驾驶（FSD）及其他 AI 工作负载，因此制造产能与该公司的自动驾驶路线图直接挂钩。

rss · Tom's Hardware · 7月13日 17:59

**背景**: “流片”（Tape-out）是芯片设计最终完成并交付晶圆厂进行物理制造的关键里程碑；此后任何改动都将变得极其昂贵和耗时。2nm 级工艺节点是指当前最先进的半导体制造工艺世代，采用全环绕栅极（GAA）纳米片晶体管来提升性能和能效。台积电与三星代工是全球两家领先的代工芯片制造商，特斯拉选择在两家厂商同时完成 AI5 的认证，反映了行业更广泛的双源采购趋势，以对冲地缘政治和供应风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://blog.carnex.ca/tesla-nears-final-design-of-its-ai5-chip-what-it-means-for-the-future-of-fsd-and-used-tesla-owners-in-canada/">Tesla Nears Final Design of Its AI5 Chip — What It Means for the...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#tesla`, `#samsung-foundry`, `#tsmc`, `#chip-manufacturing`

---

<a id="item-18"></a>
## [苹果 M7 Ultra 据传配备 1.5TB 内存和 Blackwell 级 AI 性能](https://www.tomshardware.com/tech-industry/semiconductors/apples-rumored-m7-ultra-targets-1-5tb-of-memory-and-blackwell-class-ai) ⭐️ 6.5/10

据 Bloomberg 记者 Mark Gurman 透露，苹果计划于 2028 年推出的 M7 Ultra 芯片正在设计支持高达 1.5TB 的统一内存，并提供可与英伟达 Blackwell 加速器竞争的 AI 性能。该芯片面向 Mac Studio，其发布取决于全球内存供应状况的缓解。 如果得以实现，M7 Ultra 将使苹果目前的最大统一内存容量（M3 Ultra 的 512GB）增加三倍，并使 Apple Silicon 成为在当前由英伟达数据中心 GPU 主导的高端 AI 工作负载领域的有力竞争者。这表明苹果有意在本地 AI 开发和推理市场占据一席之地，而大容量内存正是运行大型语言模型的主要瓶颈。 据报道，苹果已完全取消 M6 Pro 和 M6 Max 版本，直接跳到 M7 系列，基础版 M7 预计于 2027 年初发布，采用 Intel 的 18A-P 工艺节点——这是苹果首款由 Intel 代工的芯片设计。1.5TB 代表的是芯片的最大能力上限，而非已确认的零售配置，如果持续的内存短缺无法缓解，2028 年的时间表可能推迟。

rss · Tom's Hardware · 7月13日 12:02

**背景**: Apple Silicon 是苹果定制的 ARM 架构处理器系列，应用于 Mac 电脑产品线，采用统一内存架构（UMA），使 CPU、GPU 和神经网络引擎可以共享同一内存池以实现更快的数据访问。M 系列采用分级命名方案——基础版、Pro、Max 和 Ultra，其中 Ultra 是最高端配置，通常用于 Mac Studio 和 Mac Pro 工作站。英伟达的 Blackwell 架构是该公司最新的数据中心 GPU 平台，专为生成式 AI 训练和推理设计，目前是高端 AI 加速的性能标杆，而 M7 Ultra 据称正是要对标这一水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/07/12/m7-ultra-mac-studio-to-support-up-to-1-5-tb-unified-memory/">M7 Ultra to potentially feature up to 1.5TB of RAM, finally ...</a></li>
<li><a href="https://zeerawireless.com/blogs/news/mac-studio-m7-ultra-2028-release-specs-1-5tb-memory">Mac Studio M7 Ultra Rumors: 1.5TB Memory, 2028 Release and Specs</a></li>
<li><a href="https://www.nvidia.com/en-sg/data-center/technologies/blackwell-architecture/">NVIDIA Blackwell : GPU Architecture for Generative AI & HPC | NVIDIA</a></li>

</ul>
</details>

**标签**: `#Apple Silicon`, `#M7 Ultra`, `#AI Hardware`, `#Nvidia Blackwell`, `#Semiconductors`

---

<a id="item-19"></a>
## [ASRock Rack 基于 NVIDIA Thor 工业 SoC 打造边缘服务器](https://www.servethehome.com/asrock-rack-built-an-edge-server-based-on-nvidias-thor-industrial-soc/) ⭐️ 6.5/10

ASRock Rack 推出了一款基于 NVIDIA Blackwell 时代 Thor 工业 SoC 的 2U 边缘服务器 2UXGI-THOR，该芯片最初是为汽车应用设计的。该系统面向工业和医疗市场领域，而非 NVIDIA 通常使用 Thor 所针对的机器人或自动驾驶场景。 这款产品标志着 NVIDIA 的嵌入式/汽车级芯片与传统服务器形态之间的交叉融合，有望将 Thor 的目标市场从汽车 OEM 拓展到更广泛的领域。工业和医疗领域的边缘部署通常需要紧凑、坚固且具备高 AI 算力的计算设备，而 Thor 提供的 2070 FP4 TFLOPS 算力可能正好满足这一独特需求。 该系统采用 2U 机架式形态，表明它面向本地部署或加固型环境，而非车载集成。Thor 属于 NVIDIA Blackwell 架构世代，与 RTX 50 系列 GPU 和 GB200 数据中心芯片同属一个家族，因此尽管定位为工业级产品，仍具备现代化的 AI 推理能力。

rss · ServeTheHome · 7月13日 20:00

**背景**: NVIDIA Thor SoC 是该公司嵌入式系统产品线的一部分，Jetson Thor AGX 开发者套件可提供 2070 FP4 TFLOPS 的算力，面向人形机器人和物理 AI 等机器人应用。边缘计算是指在数据产生源附近而非集中式云数据中心进行数据处理，能够降低延迟并减少带宽需求——这些特性在工业自动化和医疗影像领域尤为重要。Blackwell 架构由 NVIDIA 于 2024 年发布，并在 2025 年 GTC 大会上扩展出 Blackwell Ultra，支撑着消费级、数据中心乃至现在嵌入式领域的新一代 GPU 和加速器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/downloads/assets/embedded/secure/jetson/thor/docs/thor-soc-trm_dp-11881-002.pdf">NVIDIA Thor Series System-on-Chip</a></li>
<li><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/">Jetson Thor | Advanced AI for Physical Robotics | NVIDIA</a></li>
<li><a href="https://contabo.com/blog/edge-computing-explained/">Edge Computing Explained : What It Is and Why It... | Contabo Blog</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#ASRock Rack`, `#edge computing`, `#Thor SoC`, `#hardware`

---

<a id="item-20"></a>
## [字节探索自动驾驶，Seed 世界模型团队负责｜36 氪独家](https://36kr.com/p/3893815451417347?f=rss) ⭐️ 6.3/10

据报道，字节跳动正通过其 Seed 团队的世界模型小组探索自动驾驶，有望将世界模型技术应用于无人物流领域，尽管该公司此前否认有智能驾驶业务计划。

rss · 36氪 · 7月13日 08:34

**标签**: `#ByteDance`, `#autonomous-driving`, `#world-models`, `#physical-AI`, `#industry-news`

---