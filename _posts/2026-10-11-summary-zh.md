---
layout: default
title: "Horizon Summary: 2026-10-11 (ZH)"
date: 2026-10-11
lang: zh
---

> 从 38 条内容中筛选出 17 条重要资讯。

---

1. [DuckDB 2.0 在查询执行中实现重大性能提升](#item-1) ⭐️ 8.0/10
2. [参议院报告指控人工智能数据中心经济效益声明具有误导性](#item-2) ⭐️ 7.5/10
3. [乌克兰无人机袭击 Yandex 数据中心，多个模块离线](#item-3) ⭐️ 7.5/10
4. [灯泡计算机原型结合手势追踪与语音实现人机交互](#item-4) ⭐️ 7.0/10
5. [AI 时代下的 Unikernel 复兴提议](#item-5) ⭐️ 7.0/10
6. [超 NA  EUV 光刻预计 2036 年成为芯片制造下一前沿](#item-6) ⭐️ 7.0/10
7. [高通与 Arm 案件：陪审团仍在审议中](#item-7) ⭐️ 7.0/10
8. [PS5SX2 模拟器让越狱 PS5 能够直接加载 PS2 光盘](#item-8) ⭐️ 6.5/10
9. [AMD 上调合作伙伴 GDDR6 内存价格](#item-9) ⭐️ 6.5/10
10. [Super Micro smuggling co-conspirator pleads guilty to sending AI chips to China](#item-10) ⭐️ 6.5/10
11. [AnyPS5 项目达成关键 GPU 里程碑，助力实现 PS5 游戏在 PC 上原生运行](#item-11) ⭐️ 6.5/10
12. [毕业生用普通 PETG 材料成功试飞 3D 打印喷气遥控飞机](#item-12) ⭐️ 6.5/10
13. [全球 PC 出货量因 AI 导致内存涨价而骤跌逾 20%](#item-13) ⭐️ 6.3/10
14. [构建自定义决策模型与轻量级 AI 替代方案](#item-14) ⭐️ 6.0/10
15. [因发现 TAoCP 错误获得高德纳奖赏支票](#item-15) ⭐️ 6.0/10
16. [软银寻求中东投资者注资 AI 巨额基金](#item-16) ⭐️ 5.5/10
17. [SPECviewperf 15.0.1 Linux 版新增官方 Arm 支持](#item-17) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [DuckDB 2.0 在查询执行中实现重大性能提升](https://motherduck.com/blog/why-duckdb-20-is-faster/) ⭐️ 8.0/10

MotherDuck 发布了一份分析，表明 DuckDB 2.0 显著提升了性能，具体实现了递归公共表表达式（CTE）高达 90 倍的加速以及 S3 上异步 I/O 操作 2.4 倍的改进。 这些改进使 DuckDB 2.0 成为处理复杂数据负载更高效的分析型数据库引擎，影响了依赖该引擎进行可扩展且快速数据处理任务的开发者。 该版本引入了新的存储格式和增强的查询执行模型，其中 VARIANT 数据类型相较于标准 JSON 文本处理具有显著的性能提升。

hackernews · tosh · 10月10日 18:08 · [社区讨论](https://news.ycombinator.com/item?id=50035530)

**背景**: DuckDB 是一个开源嵌入式分析型数据库引擎，专为快速数据处理而设计，在概念上类似于 SQLite，但专用于分析任务。递归 CTE 是一种允许查询自我引用的 SQL 构造，对于在关系数据库中遍历层级数据结构至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://motherduck.com/blog/why-duckdb-20-is-faster/">Why DuckDB 2.0 is faster - MotherDuck</a></li>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights">A Preview of DuckDB v2.0</a></li>
<li><a href="https://sesamedisk.com/faster-database-queries-with-duckdb/">Why is DuckDB 2.0 Faster? - Sesame Disk</a></li>

</ul>
</details>

**社区讨论**: 社区讨论高度赞扬了新的 C++ 扩展 API，同时有用户指出 DuckDB 的任务型并行化和异步 I/O 方法相较于 Umbra 和 CedarDB 等现代数据库设计仍是一种追赶。另一位评论者则指出了 DuckDB 在基于 DuckPGQ 系统的图数据查询方面已有的强大扩展能力。

**标签**: `#duckdb`, `#databases`, `#performance`, `#sql`, `#query-optimization`

---

<a id="item-2"></a>
## [参议院报告指控人工智能数据中心经济效益声明具有误导性](https://www.tomshardware.com/tech-industry/data-centers/senate-investigation-says-that-some-ai-data-center-claims-are-misleading-senators-question-number-of-permanent-jobs-projects-bring-to-communities-but-companies-refuse-to-divulge-data) ⭐️ 7.5/10

美国参议院的一项调查得出结论，人工智能数据中心运营商在申请地方建筑许可时，关于其设施成本和经济效益的信息具有误导性。报告特别指出，这些公司拒绝披露能够准确评估其对当地社区影响的数据。 这种监管审查将迫使大型云服务商提高其环境影响的透明度，直接影响地方政府批准大规模人工智能基础设施项目的方式。这可能导致对新建数据中心发展实施更严格的城市规划要求和强制性的经济报告制度。 核心问题是，大型人工智能超算服务商提交的成本和效益数字未能反映出其对主办地社区的真实局部经济影响。这种差异引发了关于人工智能基础设施繁荣期透明度的严重质疑。

rss · Tom's Hardware · 10月10日 14:40

**背景**: “超算服务商”（Hyperscalers）是指为人工智能模型提供动力的大型云服务商，建设此类数据中心需要消耗大量的电力和土地。从历史上看，这些开发商在申请当地用地许可时经常提出乐观的经济预测，但其环境和社交成本往往被低估。

**标签**: `#AI Infrastructure`, `#Policy & Regulation`, `#Data Centers`, `#Economic Impact`, `#Transparency`

---

<a id="item-3"></a>
## [乌克兰无人机袭击 Yandex 数据中心，多个模块离线](https://www.tomshardware.com/tech-industry/data-centers/second-russian-data-center-targeted-by-ukrainian-drones-in-just-two-days-as-yandex-reels-from-another-service-outage-russian-state-media-admits-that-multiple-modules-completely-taken-out) ⭐️ 7.5/10

乌克兰无人机袭击了俄罗斯卡卢加的一个大型 Yandex 数据中心园区，导致该 140 万平方英尺设施内的多个模块完全离线。 此事件严重扰乱了俄罗斯的云计算基础设施，并凸显了重要科技设施在物理地缘政治冲突中的脆弱性。 此次袭击导致 Yandex 发生重大服务中断，俄罗斯官方媒体已承认该设施内的多个模块已完全停止服务。

rss · Tom's Hardware · 10月10日 10:30

**背景**: Yandex 是俄罗斯最大的科技公司之一，也是主要的互联网服务和云计算基础设施提供商。卡卢加园区是俄罗斯最大的数据中心之一，面积为 140 万平方英尺。此次袭击发生在两天前 Sasovo 的一座数据中心遭到乌克兰无人机袭击之后。

**标签**: `#data-center`, `#geopolitics`, `#infrastructure`, `#security`, `#cloud-outage`

---

<a id="item-4"></a>
## [灯泡计算机原型结合手势追踪与语音实现人机交互](https://lightbulbcomputer.com/) ⭐️ 7.0/10

一款名为“灯泡计算机”的研究原型发布，允许用户通过物理移动灯泡与计算机交互，并集成了手势追踪和语音识别功能。该系统运行在 Mac 上，使用苹果内置的视觉框架、一台 4K 激光投影机和网络摄像头。 该项目通过将物理物体与空间计算相结合，探索了人机交互的新范式，可能为环境计算和智能家居设计提供灵感。它通过将数字信息锚定在物理空间中，解决了传统基于屏幕的交互界面的局限性。 该原型依赖特定的技术栈，包括 Mac 电脑、自定义投影映射软件、消费级 4K 激光投影机和基础网络摄像头。创作者强调该项目主要是一个研究与设计原型，而非成熟的消费级产品，且存在语音响应循环中的延迟问题。

hackernews · oskarth · 10月10日 04:12 · [社区讨论](https://news.ycombinator.com/item?id=50029487)

**背景**: 人机交互（HCI）传统上依赖键盘、鼠标和触摸屏等物理界面。空间计算和环境接口代表了向理解用户物理环境的系统转变，利用传感器和人工智能将数字数据映射到现实世界物体上。手势追踪是指使用计算机视觉算法实时检测并跟踪手的位置和运动。

**社区讨论**: 社区反应不一，创作者强调了设备的技术限制和原型性质。用户表达了对系统持续监控特性的担忧，将其比作一个“永远在听”的精灵，而另一些人则赞扬该概念解决了 XR 头戴设备和 Humane Pin 中存在的问题。

**标签**: `#Human-Computer Interaction`, `#Hardware`, `#Voice Interface`, `#Prototype`, `#Apple`

---

<a id="item-5"></a>
## [AI 时代下的 Unikernel 复兴提议](https://ghuntley.com/unikernels/) ⭐️ 7.0/10

作者回顾了 Unikernel 历史上的技术挑战，并提议在 AI 时代复兴这一技术，该提议得到了社区关于硬件加速和专用云托管方案等讨论的支持。 随着传统隔离机制面对 AI 相关威胁时日益失效，Unikernel 提供了极小的攻击面，使其成为未来安全 AI 系统的关键架构组件。 值得关注的技术实现包括将 Zephyr 作为基于 RTOS 的 Unikernel 使用、利用 Zynq UltraScale+等 FPGA 进行硬件级隔离，以及使用 BareMetal 等微 VM 服务进行低资源部署。

hackernews · ghuntley · 10月10日 14:27 · [社区讨论](https://news.ycombinator.com/item?id=50033357)

**背景**: Unikernel 是将应用程序及其所有依赖项打包在单一轻量级虚拟机映像中的单地址空间机器。历史上，由于工具链缺乏和复杂性，它们逐渐被传统的虚拟机和容器所取代并变得不受欢迎。

**社区讨论**: 社区就推进 Unikernel 安全共享了多样且高质量的观点，包括采用 Zephyr 以实现嵌入式简化、开发 AI 编码的 FPGA（FOGAs）以对抗 LLM 的冗余，以及通过专用服务部署微 VM 来最小化 AI 架构的攻击面。

**标签**: `#Unikernels`, `#Systems`, `#Security`, `#AI`, `#Hardware`

---

<a id="item-6"></a>
## [超 NA  EUV 光刻预计 2036 年成为芯片制造下一前沿](https://semiwiki.com/lithography/374764-hyper-na-euv-the-next-frontier-in-chipmaking-could-arrive-in-2036/) ⭐️ 7.0/10

SemiWiki 讨论了超 NA EUV 光刻技术作为芯片制造的下一重大前沿领域，预计部署时间约为 2036 年。文章指出，这项技术代表了超越当前高 NA 系统的重大飞跃，并在此前硅谷举行的 SPIE 会议上受到重点关注。 转向超 NA EUV 对于通过实现 2nm 以下逻辑节点的分辨率来维持摩尔定律的缩放至关重要。这一演进将影响整个半导体供应链，从 ASML 的工具制造到晶圆厂的工艺开发，将决定下一代人工智能和高性能计算芯片的能力。 主要区别在于光学系统中数值孔径（NA）的增加，这使得光刻机能够收集更陡峭的光锥并聚焦于比标准或当前高 NA 系统更小的特征。具体挑战包括管理日益增加的光学成本和复杂性，以及解决由 3D 掩模效应引起的分辨率增强和对比度下降问题。

rss · SemiWiki · 10月10日 12:00

**背景**: EUV 光刻使用 13.5 nm 极紫外光在晶圆上打印图案，目前已成为先进节点的标准技术。高 NA EUV 是当前的下一代技术步骤，主要晶圆厂已将其部署用于领先边缘的逻辑芯片。超 NA EUV 提议将数值孔径进一步提高至当前高 NA 工具的极限之外，以将分辨率进一步推向 2nm 以下的时代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chipdocket.com/articles/what-is-high-na-euv-lithography-explainer-2026-06-22">High-NA EUV Lithography Explained | ChipDocket</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#lithography`, `#EUV`, `#hardware`, `#manufacturing`

---

<a id="item-7"></a>
## [高通与 Arm 案件：陪审团仍在审议中](https://www.electronicsweekly.com/news/business/jury-still-out-in-qualcomm-vs-arm-case-2026-10/) ⭐️ 7.0/10

高通与 Arm 法律案中的陪审团在审议四小时后未能得出裁决，并返回法庭。该陪审团已排定计划于下周二重新集合，继续对该案件进行审议。 这场备受瞩目的半导体行业知识产权诉讼是一件值得关注的重大事件，尽管此次更新主要是程序性进展。该案的最终裁决将对 Arm 的授权模式以及更广泛的芯片生态系统产生重要影响。 这一程序性延迟意味着具体的裁决及其法律后果仍未可知。该案件代表了半导体行业主要参与者之间的一场高风险法律纠纷。

rss · Electronics Weekly · 10月10日 07:20

**背景**: 高通和 Arm 是半导体行业的重要参与者，其中 Arm 通常提供 CPU 架构的知识产权授权。这一持续进行的争议涉及 Arm 的授权协议以及高通的创新权利（包括其对 Nuvia 的收购）。以往的网页搜索结果表明，这是更广泛、高风险的知识产权法律战的一部分，其历史曾出现过多次不同的司法裁决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://futurumgroup.com/insights/litigation-sitrep-ongoing-dispute-between-qualcomm-and-arm/">Litigation SITREP: Ongoing Dispute Between Qualcomm and Arm ...</a></li>
<li><a href="https://www.qualcomm.com/news/releases/2025/09/qualcomm-achieves-complete-victory-over-arm-in-litigation-challe">Qualcomm Achieves Complete Victory Over Arm in Litigation ...</a></li>

</ul>
</details>

**标签**: `#IP Litigation`, `#Semiconductors`, `#Qualcomm`, `#Arm`, `#Legal`

---

<a id="item-8"></a>
## [PS5SX2 模拟器让越狱 PS5 能够直接加载 PS2 光盘](https://www.techpowerup.com/353588/ps2-discs-now-load-on-jailbroken-ps5-consoles-through-ps5sx2-emulator) ⭐️ 6.5/10

开发者 Sword 为越狱 PS5 上的 PS5SX2 模拟器发布了测试版更新，该功能允许将实体 PS2 光盘复制到主机存储中并在硬件上直接运行。

rss · TechPowerUp News · 10月10日 23:43

**标签**: `#Emulation`, `#Jailbreak`, `#PS5`, `#PS2`, `#Homebrew`

---

<a id="item-9"></a>
## [AMD 上调合作伙伴 GDDR6 内存价格](https://www.techpowerup.com/353584/amd-reportedly-raises-gddr6-prices-for-board-partners) ⭐️ 6.5/10

据传，AMD 自 2026 年 10 月 1 日起提高了供应给合作伙伴的 GDDR6 内存成本。此次涨价直接导致了近期中国市场 Radeon 显卡零售价格的上涨。 这一发展反映了硬件组件成本上升的 broader 趋势，因为内存涨价会直接导致消费者购买的显卡变得更加昂贵。由于这与英伟达相对稳定的 GDDR7 定价形成鲜明对比，影响了 GPU 制造商之间的竞争态势，因此具有重要意义。 GDDR6 涨价的时间与中国市场特定型号（如 RX 9070 和 RX 9060 XT 8 GB）的价格上调相吻合。值得注意的是，AMD 是 GDDR6 的主要供应商，而英伟达在年初进行涨价后，目前保持其 GDDR7 价格稳定。

rss · TechPowerUp News · 10月10日 17:54

**背景**: AMD 将其 GPU 芯片连同内存一起销售给独立显卡（AIB）合作伙伴，这意味着组件成本会直接影响显卡的最终零售价格。相比之下，据报道 RX 9070 XT 并未受到中国近期涨价的影响。在 2026 年，AMD 已实施多次价格上调，其中包括因台积电晶圆成本上升而导致的涨价。

**标签**: `#AMD`, `#NVIDIA`, `#Hardware Pricing`, `#GDDR6`, `#GPU Market`

---

<a id="item-10"></a>
## [Super Micro smuggling co-conspirator pleads guilty to sending AI chips to China](https://www.tomshardware.com/tech-industry/artificial-intelligence/super-micro-smuggling-co-conspirator-pleads-guilty-to-sending-ai-chips-to-china-broker-admits-breaking-export-control-rules-as-company-co-founder-denies-charges) ⭐️ 6.5/10

A co-conspirator in the Super Micro server smuggling case has pleaded guilty to sending advanced Nvidia AI chips to China in violation of export control rules.

rss · Tom's Hardware · 10月10日 15:35

**标签**: `#AI Hardware`, `#Export Controls`, `#Legal`, `#Super Micro`, `#Nvidia`

---

<a id="item-11"></a>
## [AnyPS5 项目达成关键 GPU 里程碑，助力实现 PS5 游戏在 PC 上原生运行](https://www.tomshardware.com/video-games/playstation/anyps5-reaches-critical-gpu-milestone-with-100-percent-shader-instruction-coverage-ps5-games-running-natively-on-pc-still-far-off) ⭐️ 6.5/10

开源 AnyPS5 项目已实现 100% GPU 着色器指令覆盖，标志着其在实现 PS5 游戏在 PC 上原生运行的目标上取得了关键进展。

rss · Tom's Hardware · 10月10日 11:30

**标签**: `#Emulation`, `#Open-Source`, `#GPU`, `#PlayStation`, `#Hardware`

---

<a id="item-12"></a>
## [毕业生用普通 PETG 材料成功试飞 3D 打印喷气遥控飞机](https://www.tomshardware.com/3d-printing/worlds-first-3d-printed-remote-control-aircraft-with-a-jet-turbine-takes-flight-aims-for-mach-0-8-to-beat-world-record-for-fastest-model-aircraft-mostly-printed-using-standard-petg-materials) ⭐️ 6.5/10

一支毕业生团队成功试飞了一架由微型喷气涡轮引擎驱动的 3D 打印遥控飞机，其目标是突破模型飞机的最高速度世界纪录，目标为马赫 0.8。这架飞机主要由标准的 PETG 材料打印而成，鉴于该材料的典型耐温限制，这是一项显著的工程挑战。 这一成就表明，3D 打印技术能够利用相对廉价且标准的线材材料，制造出适用于高性能喷气式模型飞机的功能性部件。它填补了普通消费级 3D 打印技术与高级小型航空工程之间的空白。 0.8 马赫的目标速度使这次尝试成为喷气式遥控飞机吉尼斯世界纪录的高风险挑战。标准 PETG 通常在 70 至 100°C 时保持稳定，团队的暗示着他们巧妙利用工程设计或结构设计来管理飞行中喷气涡轮机产生的热量。

rss · Tom's Hardware · 10月10日 10:00

**背景**: 大多数模型飞机依赖电动机或螺旋桨引擎，而喷气涡轮机提供持续推力，但排气温度极高。标准 PETG 是一种常用于 FDM 3D 打印的热塑性线材，以其耐用性和易挤出性著称，但其热变形温度通常限制在 70-100°C 左右，使其难以直接接触高温喷气部件。

**标签**: `#3D-Printing`, `#Aviation`, `#Materials-Science`, `#Engineering`, `#World-Record`

---

<a id="item-13"></a>
## [全球 PC 出货量因 AI 导致内存涨价而骤跌逾 20%](https://www.solidot.org/story?sid=85572) ⭐️ 6.3/10

2026 年第三季度，受 AI 需求导致内存及 SSD 价格暴涨四倍的推动，全球 PC 出货量同比下滑 20-21%。内存成本占 PC BOM（物料清单）的比例升至 40%，促使市场重新回归 DDR4 硬件。 这一中断对 PC 制造商和消费者产生了巨大影响，表明 AI 硬件热潮正在传统 PC 领域造成严重的供应链约束。这标志着 AI 数据中心需求开始直接决定消费电子产品的价格和硬件配置。 目前一套 32GB 的芝奇（Corsair）DDR5 内存价格为 620 美元，而同规格 DDR4 仅 260 美元，促使技嘉等厂商发布支持 DDR4 的 Intel LGA 1700 和 AMD AM4 主板。分析师预计 2026 年第四季度出货量将再降 24%，2027 年将下滑 7%。

rss · Solidot · 10月10日 07:53

**背景**: “AI 热潮”导致数据中心客户积极采购高带宽内存芯片，耗尽了制造商面向消费级组件的产能。DRAM（动态随机存取存储器）价格对这些转变非常敏感，在新一代 DDR5 价格令人望而却步时，市场通常会回归上一代 DDR4 以保持竞争力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/09/tesla-renames-full-self-driving-to-tesla-assisted-driving-in-europe/">Tesla renames 'Full Self-Driving' to 'Tesla Assisted Driving ...</a></li>
<li><a href="https://hwbusters.com/news/gigabyte-builds-new-am4-motherboards-in-2026-b550-x-gets-wi-fi-7-and-a-60a-drmos-vrm/">Gigabyte Builds New AM4 Motherboards in 2026 — B550 X Gets Wi ...</a></li>
<li><a href="https://www.playground.ru/misc/news/gigabyte_podtverdila_intel_vypustit_novye_protsessory_lga1700_v_nachale_2027_goda_s_podderzhkoj_pamyati_ddr4_i_ddr5-1880402">GIGABYTE подтвердила: Intel выпустит новые процессоры...</a></li>

</ul>
</details>

**标签**: `#PC Market`, `#Memory Prices`, `#AI Hardware`, `#Supply Chain`, `#DDR4/DDR5`

---

<a id="item-14"></a>
## [构建自定义决策模型与轻量级 AI 替代方案](https://nishtahir.com/build-your-own-decision-model/) ⭐️ 6.0/10

该文章介绍了一种使用轻量级技术构建自定义决策模型的指南。社区讨论中介绍了可在 CPU 上运行分类的自制工具 Jeffy，并指出 Jev 是最近出现的商用 System 1 决策模型案例。 这表明了向极简主义 AI 工具发展的趋势，使开发者能够在资源受限的环境中部署智能决策能力，而无需依赖庞大的框架。它为特定的分类任务提供了大语言模型之外的选择。 Jev 是一个类型化 AI 模型，通过为预定义问题返回概率来驱动业务规则，而 Jeffy 是一个完全在 CPU 上运行的轻量级工具。一名社区用户还分享了一个使用 SQLite-vec 数据库和 Qwen 嵌入模型生成特定内容的自定义应用程序。

hackernews · softwaredoug · 10月10日 22:50 · [社区讨论](https://news.ycombinator.com/item?id=50037949)

**背景**: 在软件工程领域，决策模型或分类器是分析数据以进行自动化选择的系统。'System 1' 模型是指受双重过程理论启发的快速直觉决策，而传统框架通常需要大量的计算资源。轻量级或极简主义 AI 工具旨在以较少的依赖项和较低的硬件要求运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aijev.org/">Jev: System One Decision Model Explained | AIJev</a></li>
<li><a href="https://aiindigo.com/blog/beyond-the-framework-lightweight-binaries-and-the-rise-of-minimalist-ai-tools">Beyond the Framework: Lightweight Binaries and the Rise of ...</a></li>

</ul>
</details>

**社区讨论**: 对于构建轻量级 AI 工具的可访问性，整体情绪是积极的，用户分享了各种 DIY 实现方案及对比。然而，有人对 Jev 最近融资估值是否因其算法优势而合理表示怀疑，并提出了关于事后调整模型温度的统计有效性的小担忧。

**标签**: `#machine-learning`, `#algorithm-design`, `#lightweight-ai`, `#programming`

---

<a id="item-15"></a>
## [因发现 TAoCP 错误获得高德纳奖赏支票](https://www.thomas-huehn.com/knuth-reward-check/) ⭐️ 6.0/10

一位作者因在《计算机程序设计艺术》中识别出一个逻辑错误而获得 Donald Knuth 的奖赏支票，该错误将“无穷多个”替换为“巨量”的字母表数量。这篇文章记录了收到支票的个人经历，并解释了数学修正的具体细节。 这个故事凸显了 Knuth 漏洞赏金计划的持久影响力，该计划鼓励对最具影响力的计算机科学文本进行严格的同行评审。它成为算法研究者的文化标志，并强调了在数学文献中细致审查的价值。 该具体错误涉及声称可以用有限参数生成无穷多个字母表，后被更正为“巨量数字”。作者指出，该错误出现在书的第一句话中这一事实颇具讽刺意味。

hackernews · Curiositry · 10月10日 15:47 · [社区讨论](https://news.ycombinator.com/item?id=50034081)

**背景**: Donald Knuth 是一位著名的计算机科学家和图灵奖得主，他于 1968 年建立了奖励系统，以表彰那些在其出版物（最初是《计算机程序设计艺术》）中发现错误的人。最初的奖励是每处错误 2.56 美分，后来变为 2.56 美元，目前已演变为数字或证书形式的奖励。《计算机程序设计艺术》被认为是一部关于算法的开创性多卷本专著，是计算机科学课程体系的基石。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knuth_reward_check">Knuth reward check - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming">The Art of Computer Programming - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了对各自获得奖赏支票的自豪与遗憾情绪，其中一位用户幽默地哀叹自己遗失了支票，另一位用户则提到了具体的过往收款记录。讨论还包括对“无穷多个”错误的详细验证，以及关于 Knuth 亲自发邮件给读者讨论其已发表文章的说明。

**标签**: `#algorithms`, `#knuth`, `#taocp`, `#academic`, `#anecdote`

---

<a id="item-16"></a>
## [软银寻求中东投资者注资 AI 巨额基金](https://www.tomshardware.com/tech-industry/artificial-intelligence/softbank-seeks-usd100-billion-for-ai-refined-projects-from-middle-eastern-investors-fund-would-be-used-to-acquire-companies-and-improve-their-operations-using-artificial-intelligence-and-robotics) ⭐️ 5.5/10

软银正在积极寻求来自中东投资者的 1000 亿美元投资，以建立一个专注于人工智能项目的巨额基金。该资金将用于收购目前未使用 AI 或机器人技术的公司，目标是改造其运营以提升估值。 这项巨额投资举措标志着传统企业如何通过整合先进的 AI 和机器人技术来优化运营的重大转变，是全球 AI 商业化的重要催化剂。通过改造非 AI 公司，软银旨在释放各个经济部门的巨大价值。 该战略涉及收购尚未采用人工智能或机器人技术的业务，然后应用这些新技术以提高运营效率。1000 亿美元的目标明确将资金划归给由这些先进自动化和机器学习工具细化的项目。

rss · Tom's Hardware · 10月10日 15:40

**背景**: 软银是一家日本大型综合企业集团，作为全球科技行业最大的投资者之一而闻名，最著名的是其投资 Uber 的案例。目前的战略不同于从零开始建立科技公司，而是专注于通过向现有业务注入 AI 能力来实现“收购与改进”。这一方法是针对数字经济中保持竞争力所需的企业级 AI 集成日益增长的需求而作出的回应。

**标签**: `#Artificial Intelligence`, `#Robotics`, `#Venture Capital`, `#SoftBank`, `#Industry`

---

<a id="item-17"></a>
## [SPECviewperf 15.0.1 Linux 版新增官方 Arm 支持](https://www.servethehome.com/specviewperf-15-0-1-linux-edition-released-linuxs-key-graphics-benchmark-adds-arm-support/) ⭐️ 5.5/10

SPEC 发布了 SPECviewperf Linux 版 15.0.1，引入了官方 Arm 架构支持并更新了基准测试套件。该版本还新增了 Blender 3.6 LTS 工作负载。 此更新支持 ARM64 Linux 工作站的专业图形标准化基准测试，迎合了日益增长的 Arm 架构服务器和工作站硬件市场。它有助于缩小非 x86 环境硬件认证方面的差距。 该基准测试衡量基于 OpenGL、DirectX 和 Vulkan API 的 3D 图形性能。厂商许可费用定为 2,500 美元，以降低硬件认证成本。

rss · ServeTheHome · 10月10日 21:00

**背景**: SPECviewperf 是衡量专业应用程序图形性能的全球标准。尽管该套件已在 x86 架构上广泛使用，但 Arm 系统此前缺乏一种官方且标准化的方法来在此基准测试中验证图形性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gwpg.spec.org/benchmarks/benchmark/specviewperf-15_0_1/">SPECviewperf 15.0.1 - SPEC GWPG</a></li>
<li><a href="https://briefglance.com/articles/bridging-the-gap-linux-and-arm64-secure-a-seat-at-the-graphics-table">Bridging the Gap: Linux and ARM64 Secure a Seat at the ...</a></li>

</ul>
</details>

**标签**: `#Benchmarking`, `#Arm`, `#Linux`, `#Graphics`, `#SPECviewperf`

---