---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> 从 64 条内容中筛选出 19 条重要资讯。

---

1. [英伟达向联发科投资 35 亿美元，拓展 NVLink Fusion 生态系统](#item-1) ⭐️ 8.5/10
2. [MacBook Neo 的 8GB 内存导致 SSD 写入次数消耗惊人](#item-2) ⭐️ 7.5/10
3. [SK 海力士考虑采用英特尔代工生产 HBM4E 基础裸片](#item-3) ⭐️ 7.5/10
4. [SK 海力士 CEO 警告存储芯片短缺将持续至 2030 年](#item-4) ⭐️ 7.5/10
5. [无电机固态冷却器利用废热实现制冷](#item-5) ⭐️ 7.5/10
6. [长鑫存储率先量产 LPDDR6，超越西方竞争对手](#item-6) ⭐️ 7.5/10
7. [NVIDIA Jetson Orin Nano 2：入门级边缘 AI 板性能翻倍](#item-7) ⭐️ 7.5/10
8. [长鑫存储启动 HBM3E 风险量产，仍落后韩国厂商两代](#item-8) ⭐️ 6.5/10
9. [AMD 在 Linux 7.3 中开启 Zen 6 桌面处理器支持](#item-9) ⭐️ 6.5/10
10. [英伟达和英特尔关键供应商遭搜查，涉嫌产地欺诈——欣兴电子面临 PCB 产地洗白调查，或遭 40%美国关税处罚](#item-10) ⭐️ 6.5/10
11. [苹果低估了 AI 驱动的 Mac Mini 和 Mac Studio 需求](#item-11) ⭐️ 6.0/10
12. [军人服务社冷柜疑似遭入侵引发工控安全讨论](#item-12) ⭐️ 6.0/10
13. [经济高效地利用智能体自动化。验证领域的创新](#item-13) ⭐️ 6.0/10
14. [Signaloid 创始人从剑桥离职，全职领导不确定性感知计算创业公司](#item-14) ⭐️ 6.0/10
15. [先进冷却技术应对汽车散热挑战](#item-15) ⭐️ 6.0/10
16. [中国最大 DRAM 厂商长鑫存储因五角大楼军事黑名单起诉美国国防部](#item-16) ⭐️ 5.5/10
17. [泄露版 DLSS 5 通过 FP16 模组在 RTX 20 系图灵显卡上测试](#item-17) ⭐️ 5.5/10
18. [战马开发者为 DLSS 5 辩护，称其并非 AI 垃圾滤镜](#item-18) ⭐️ 5.5/10
19. [NVIDIA 在 616.56 驱动中封锁 mVolt+ 功耗限制超频功能](#item-19) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [英伟达向联发科投资 35 亿美元，拓展 NVLink Fusion 生态系统](https://www.techpowerup.com/352174/nvidia-invests-usd-3-5-billion-in-mediatek-partners-on-nvlink-fusion) ⭐️ 8.5/10

英伟达宣布向联发科投资 35 亿美元，并通过 NVLink Fusion 生态系统扩大合作，使第三方处理器和加速器（包括谷歌的 XPU）能够接入英伟达的数据中心架构。联发科将向其 ASIC 客户提供 NVLink Fusion、NVLink-C2C 以及英伟达新推出的 NVHBM 内存技术。 这笔交易使英伟达成为异构 AI 数据中心的核心互联架构提供商，让谷歌等公司的定制 ASIC 能够与英伟达的网络堆栈原生互操作，而不再彼此孤立。它也标志着英伟达从销售独立 GPU 转向成为整个 AI 基础设施堆栈的基础层，提升了竞争对手互联标准的竞争壁垒。 NVLink Fusion 同时支持光子互联和经典铜互联，而 NVLink-C2C 提供相邻 XPU 之间的高带宽芯片互联，并将用于英伟达即将推出的"Rosa" CPU。英伟达的 NVHBM 将内存控制器直接集成到 3D HBM 堆栈中，据称相比 HBM4E 带宽提升高达 30%，HBM 功耗降低 15%，处理器可用计算芯片面积增加高达 25%。

rss · TechPowerUp News · 8月31日 13:55

**背景**: NVLink 是英伟达专有的高速互联技术，用于连接数据中心系统内的 GPU 和其他加速器；NVLink Fusion 通过将该 IP 和 chiplet 框架授权给第三方芯片制造商，让定制 ASIC（其中最著名的是谷歌的 XPU/TPU 和 AWS Trainium）能够与英伟达的网络堆栈进行原生通信。XPU 是业界对非 GPU AI 加速器的统称，通常是超大规模云厂商自研的 ASIC 芯片，目的是减少对商用 GPU 的依赖。Chiplet 架构是一种将多个较小芯片裸片集成在单一封装内的半导体设计方法，相比单片设计能够提供更好的良率、设计灵活性和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techinasia.com/news/nvidia-unveils-ai-chip-communication-tech-nvlink-fusion">Tech in Asia - Connecting Asia's startup ecosystem</a></li>
<li><a href="https://hothardware.com/news/nvidia-unveils-nvhbm-memory-nvlink-fusion">NVIDIA Unveils NVHBM Memory To Turbocharge AI Chip Speeds By...</a></li>
<li><a href="https://www.linkedin.com/pulse/interconnect-computer-why-nvidias-nvlink-fusion-most-trojan-kannan-yoiec">The Interconnect Is the Computer: Why Nvidia ’s NVLink Fusion is the...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#MediaTek`, `#NVLink-Fusion`, `#AI-infrastructure`, `#chiplets`, `#data-center`

---

<a id="item-2"></a>
## [MacBook Neo 的 8GB 内存导致 SSD 写入次数消耗惊人](https://www.techpowerup.com/352178/macbook-neo-burns-through-ssd-cycles-at-an-alarming-rate) ⭐️ 7.5/10

YouTube 频道 UFD Tech 的 SSD 耐久度测试显示，搭载仅 8GB 内存的苹果平价 MacBook Neo 由于大量写入 SSD 交换文件，闪存写入次数消耗速度惊人。在仅三小时的使用 Chrome、WhatsApp 和 Discord 进行日常网页浏览的过程中，该笔记本向 SSD 交换文件写入了近 900GB 数据。 这一发现引发了对 MacBook Neo 长期可靠性的严重担忧——由于内存不足导致的大量交换文件写入可能大幅缩短设备的使用寿命，令那些将其作为平价日常笔记本购买的用户措手不及。这也突显了一个更广泛的行业问题：随着现代操作系统和应用程序对内存的需求日益增长，低于 16GB 的内存配置可能因加速闪存磨损而带来隐性成本。 UFD Tech 的写入测试估算 256GB 版本的额定耐久度约为 414 TBW（每写入 20TB 损耗约 5% 寿命），而 512GB 版本表现更好，约为 1521 TBW。按照观测到的轻度浏览三小时即写入 900GB 交换文件的速度，重度用户可能在数年的正常使用内即超过较低端 SSD 的耐久度额定值。

rss · TechPowerUp News · 8月31日 15:43

**背景**: SSD 依赖 NAND 闪存单元，每个单元只能承受有限次数的编程和擦除循环，之后便会降级，该指标通常以 TBW（写入总字节数）来衡量。当系统物理内存耗尽时，操作系统会将不活跃的内存页面转移到 SSD 上的交换文件，将存储驱动器当作溢出内存使用。这意味着如果机器内存不足以应对其工作负载，将产生异常大量的 SSD 写入流量，加速闪存磨损，并可能使硬盘的实际寿命远低于其额定耐久度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.computerworld.com/article/1408926/more-memory-means-a-longer-ssd-lifespan.html">More memory means a longer SSD lifespan – Computerworld</a></li>
<li><a href="https://disk-scout.com/guides/ssd-endurance-tbw-explained">SSD Endurance Explained — TBW, DWPD & How Long SSDs Really Last (2026)</a></li>
<li><a href="https://www.techtarget.com/it-infrastructure/podcast/How-NAND-flash-degrades-and-what-vendors-do-to-increase-SSD-endurance">How NAND flash degrades and what vendors do to increase SSD ...</a></li>

</ul>
</details>

**标签**: `#MacBook Neo`, `#Apple`, `#SSD longevity`, `#hardware review`, `#RAM limitations`

---

<a id="item-3"></a>
## [SK 海力士考虑采用英特尔代工生产 HBM4E 基础裸片](https://www.techpowerup.com/352169/sk-hynix-eyes-intel-foundry-for-hbm4e-base-die-manufacturing) ⭐️ 7.5/10

据《韩国先驱报》报道，SK 海力士据传正在考虑将英特尔代工与台积电并列为下一代 HBM4E 存储器的定制逻辑基础裸片的代工来源，这可能为英特尔代工带来一个重要的客户胜利。此前，SK 海力士在先进 HBM 基础裸片制造方面一直完全依赖台积电。 这标志着对英特尔代工先进制程能力的显著认可，也预示着 HBM 供应链——这一对 AI 加速器至关重要的环节——可能出现格局变化。SK 海力士采用英特尔作为双源供应商将获得更强的供应弹性和议价能力，同时也表明英特尔代工正成为台积电在先进封装生态中的可信替代选择。 HBM4E 基础裸片将内存控制器和 PHY 等定制逻辑直接集成到堆栈中，从而释放计算小芯片上的面积并降低延迟。目前 SK 海力士的 HBM4 基础裸片采用台积电 12nm 工艺，但 HBM4E 需要更先进的制程，因为 SK 海力士自有的 10nm 级工艺已无法满足客户需求。目前尚未披露将使用的英特尔具体制程节点，且基础裸片的成本已是 DRAM 核心裸片的 3 到 4 倍，若升级至 5nm，这一成本差距将进一步扩大。

rss · TechPowerUp News · 8月31日 13:16

**背景**: 高带宽存储器（HBM）是一种堆叠式 DRAM 技术，主要用于 AI 加速器和高性能 GPU，多个 DRAM 裸片通过硅通孔（TSV）垂直互连，放置在一颗逻辑基础裸片之上。基础裸片传统上负责缓冲电路和测试逻辑，但 HBM4 和 HBM4E 等新一代产品允许客户将内存控制器和 PHY 接口等定制逻辑直接集成到其中，从而减小主计算小芯片的占用面积和延迟。英特尔代工（Intel Foundry）原名英特尔代工服务（IFS），开放了英特尔晶圆厂对外承接客户订单，旨在实现收入多元化并提高晶圆厂利用率，定位为台积电在先进制程和封装领域的替代选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/352169/sk-hynix-eyes-intel-foundry-for-hbm4e-base-die-manufacturing">SK hynix Eyes Intel Foundry for HBM 4 E Base Die ... | TechPowerUp</a></li>
<li><a href="https://wccftech.com/with-the-hbm-base-die-costing-3-4x-as-much-as-the-core-die-nvidias-nvhbm-is-a-master-stroke-for-capturing-most-of-the-hbm-value-while-relegating-the-big-three-to-the-commodity-status/">With The HBM Base Die Costing 3-4x As Much As The Core Die ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#HBM4E`, `#Intel Foundry`, `#SK hynix`, `#semiconductors`, `#AI hardware`

---

<a id="item-4"></a>
## [SK 海力士 CEO 警告存储芯片短缺将持续至 2030 年](https://www.techpowerup.com/352156/sk-hynix-ceo-says-memory-shortage-will-last-through-2030) ⭐️ 7.5/10

SK 海力士 CEO 郭鲁正（Kwak Noh-Jung）表示，当前存储芯片短缺将持续到 2030 年底，目前没有明显的放缓迹象，这比此前公司预测的 2028 年供应紧张又延长了两年。他指出，由于 AI 驱动需求使存储产品不再纯粹是大宗商品，任何最终的缓解都可能是渐进的，而非以往存储周期中出现过的价格骤跌。 作为全球三大存储芯片制造商之一，SK 海力士的这一预测表明 DRAM 和 HBM 的供应紧张将持续，直接影响 AI 基础设施成本、云服务商的资本开支以及消费电子产品的定价。将存储芯片重新定义为战略性定制产品而非大宗商品，对超大规模云服务商、GPU 制造商以及下游 OEM 厂商的供应链和定价规划具有重大影响。 郭鲁正是在 SK 海力士位于印第安纳州的新封装工厂奠基仪式上做出上述表态的，该工厂目标在 2029 年第二季度实现量产。他将这一结构性变化归因于客户转向为 AI 工作负载定制的 DRAM 和 HBM 配置，这使得制造商的需求预测更加准确，也减少了此前因突然供过于求而导致价格暴跌的风险。

rss · TechPowerUp News · 8月30日 19:45

**背景**: 高带宽内存（HBM）是一种 3D 堆叠的 DRAM，通过硅通孔（TSV）技术垂直连接多颗内存芯片，提供远高于传统 DRAM 的带宽，这对 GPU 等 AI 加速器至关重要。历史上，存储市场具有高度周期性，短缺期之后往往伴随因产能过剩导致的价格暴跌。SK 海力士与三星、美光共同主导全球 DRAM 和 HBM 市场，是英伟达等 AI 芯片领军企业的关键供应商。晶圆厂（fab，用于在晶圆上制造芯片）与封装厂（对成品芯片进行组装、堆叠和测试）之间的区别也很重要：SK 海力士的印第安纳工厂是一座封装厂，对 HBM 组装尤为关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://blog.kistacklab.com/en/article/hbm-memory-explained/">HBM Explained : Why High Bandwidth Memory ... | Kistack Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_fabrication_plant">Semiconductor fabrication plant - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory`, `#AI-infrastructure`, `#supply-chain`, `#DRAM`

---

<a id="item-5"></a>
## [无电机固态冷却器利用废热实现制冷](https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration) ⭐️ 7.5/10

德国和日本的研究人员展示了一种利用形状记忆合金（SMA）薄膜将废热直接转化为制冷能力的固态弹热冷却器，无需任何电机或压缩机。该装置利用来自处理器等热源的热量驱动 SMA 致动器，在定制的 SMA 薄膜中产生制冷效果。 数据中心消耗大量能源，其中大部分以热量的形式浪费，而这些废热本身又需要额外能量来排出。一个无电机的固态系统能够将废热转化为主动制冷，从而形成自维持的热循环，可以大幅提升能源效率，并减少对蒸气压缩制冷及其相关温室气体制冷剂的依赖。 该冷却器依赖于弹热效应——即形状记忆合金在应力诱发马氏体相变过程中吸收或释放的潜热。SMA 薄膜具有较大的表面积与体积比，能够通过固-固接触实现高效传热，但存在一个已知的权衡：具有较大等温熵变的材料通常只能在较窄的温度窗口内工作，从而限制了其整体制冷性能。

rss · Tom's Hardware · 8月31日 15:40

**背景**: 传统制冷依赖于蒸气压缩技术，使用压缩机和制冷剂，会加剧全球变暖。弹热制冷是一种新兴的固态替代方案，利用形状记忆合金的相变——当施加或移除机械应力时，材料吸收或释放热量，产生类似于冰箱的制冷效果，但无需有害气体或运动的压缩机。形状记忆合金薄膜在此应用中尤其具有吸引力，因为其高表面积可实现快速热交换，非常适合微尺度和芯片级的热管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elastocaloric_materials">Elastocaloric materials - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s40830-024-00484-y">SMA Film-Based Elastocaloric Cooling Devices | Shape Memory ...</a></li>
<li><a href="https://www.nature.com/articles/s41560-026-02122-6.pdf">Heat-driven elastocaloric cooling with shape memory films</a></li>

</ul>
</details>

**标签**: `#thermal-management`, `#data-centers`, `#shape-memory-alloys`, `#solid-state-cooling`, `#energy-efficiency`

---

<a id="item-6"></a>
## [长鑫存储率先量产 LPDDR6，超越西方竞争对手](https://www.tomshardware.com/pc-components/dram/chinas-cxmt-beats-western-chipmakers-to-announcement-of-lpddr6-mass-production-xiaomi-smartphones-to-debut-industrys-first-lpddr6-chips) ⭐️ 7.5/10

中国长鑫存储（CXMT）宣布成为首家量产 LPDDR6 内存的芯片厂商，小米智能手机将率先搭载这一新标准内存芯片。 这一突破挑战了三星、SK 海力士和美光在 DRAM 市场的传统主导地位，具有重大的地缘政治意义，标志着中国在先进存储技术领域加速推进自主可控。 LPDDR6 标准（JESD209-6）于 2025 年 7 月 9 日由 JEDEC 正式发布，设备密度范围为 4 Gb 至 64 Gb，具备片上 ECC、命令/地址奇偶校验和内存内建自测试（MBIST）等特性。成立于 2016 年、总部位于合肥的长鑫存储是中国唯一实现量产的本土 DRAM 厂商，目前正计划进行 IPO。

rss · Tom's Hardware · 8月31日 10:30

**背景**: LPDDR（低功耗双倍数据率）是一种专为智能手机等移动和低功耗应用设计的 DRAM 内存类型，每一代新标准都在带宽和能效方面有所提升。长鑫存储（CXMT）是中国的一家 DRAM 制造商，自 2016 年成立以来产能迅速扩张。全球 DRAM 市场历来由三星、SK 海力士和美光三大厂商主导，共同控制着全球绝大部分的供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LPDDR">LPDDR - Wikipedia</a></li>
<li><a href="https://www.jedec.org/news/pressreleases/jedec®-releases-new-lpddr6-standard-enhance-mobile-and-ai-memory-performance">JEDEC® Releases New LPDDR6 Standard to Enhance Mobile and AI Memory Performance | JEDEC</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LPDDR6`, `#semiconductors`, `#CXMT`, `#DRAM`, `#China-tech`

---

<a id="item-7"></a>
## [NVIDIA Jetson Orin Nano 2：入门级边缘 AI 板性能翻倍](https://www.servethehome.com/nvidia-announces-jetson-orin-nano-2-entry-level-edge-board-gets-new-ampere-silicon/) ⭐️ 7.5/10

NVIDIA 发布了 Jetson Orin Nano 2，这是一款全新的入门级边缘 AI 机器人计算机，搭载的是全新设计的 Orin SoC，而非简单升级。在相同外形尺寸下，其推理性能达到前代产品的 2 倍，并在同等性能下功耗降低 40%。 这款开发板将前沿级生成式 AI 能力带入入门级开发者群体，可用于构建机器人、巡检与配送无人机以及视觉 AI 系统。性能翻倍同时功耗降低，直击边缘部署的核心权衡问题，有望加速物理 AI 在机器人和物联网领域的普及。 新的 Orin SoC 采用 NVIDIA 的 Ampere GPU 架构，但模组和开发者套件预计要到 2027 年上半年才会上市——从发布到出货至少有四个月的间隔。定价尚未公布，在此期间现有的 249 美元 Jetson Orin Nano Super 仍将是实际的入门级产品。

rss · ServeTheHome · 8月30日 22:00

**背景**: 边缘 AI 是指直接在本地设备上运行机器学习推理，而非将数据发送到集中式云服务器，从而实现更快响应、更低延迟和更少带宽消耗。NVIDIA 的 Jetson 产品线是专为这一用途设计的紧凑型计算板，广泛应用于机器人、无人机、智能摄像头和嵌入式 AI 场景。Orin SoC 系列基于 NVIDIA 的 Ampere GPU 架构，并集成 Arm CPU 内核，为自主机器提供 AI 算力与能效之间的平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai">NVIDIA Announces Jetson Orin Nano 2 Robotics Computer to ...</a></li>
<li><a href="https://www.unite.ai/nvidia-unveils-jetson-orin-nano-2-to-redefine-entry-level-edge-ai/">NVIDIA Unveils Jetson Orin Nano 2 to Redefine Entry-Level ...</a></li>
<li><a href="https://www.ibm.com/think/topics/edge-ai">What is edge AI? - IBM</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#edge-ai`, `#jetson`, `#embedded-systems`, `#hardware`

---

<a id="item-8"></a>
## [长鑫存储启动 HBM3E 风险量产，仍落后韩国厂商两代](https://www.techpowerup.com/352175/cxmt-starts-risk-production-of-hbm3e-memory) ⭐️ 6.5/10

据报道，中国内存制造商长鑫存储（CXMT）已开始 HBM3E 内存的风险量产，标志着中国国产内存行业迈出了重要里程碑，但目前的产量仍然非常低。 这一进展对中国的半导体自主化战略具有重要意义，尤其是对于高度依赖高带宽内存的 AI 基础设施而言。但长鑫存储仍落后三星和 SK 海力士大约两代，后者已开始向 HBM4E 生产过渡。 长鑫存储的目标是在年底前达到每月约 35 万片 DRAM 晶圆的产能，鉴于其历史推进速度，HBM3E 的大规模量产可能仅在数周后就会启动。JEDEC HBM3E 规范要求 1024 位接口、每引脚 9.2 至 12.4 Gbps 的速度，以及单堆栈约 1.2 TB/s 的带宽，容量为 24 GB（8 层堆叠）或 36 GB（12 层堆叠）。

rss · TechPowerUp News · 8月31日 14:30

**背景**: HBM（高带宽内存）是一种对 AI 加速器和高性能 GPU 至关重要的 3D 堆叠 DRAM 技术，通过宽接口和垂直堆叠实现远超传统 DRAM 的带宽。风险量产是半导体制造中的一个关键低产量阶段，即用单一芯片设计流片整片晶圆，以验证性能并优化良率，然后才进入大规模量产。JEDEC HBM3E 标准（JESD238）规定了跨 16 个通道的 1024 位接口，每引脚速度通常在 9.2 至 9.8 Gbps 之间。其继任者 HBM4 计划于 2026 年投产，接口宽度翻倍至 2048 位，单堆栈带宽可超过 1.6 TB/s，HBM4E 则会进一步提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Risk_production_semiconductors">Risk production (semiconductors) — Grokipedia</a></li>
<li><a href="https://blogs.sw.siemens.com/semiconductor-packaging/2026/04/24/hbm3e-hbm4-ic-design-guide/">HBM3e and HBM4: IC design guide for next-generation high bandwidth memory</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#HBM`, `#memory`, `#CXMT`, `#China-tech`

---

<a id="item-9"></a>
## [AMD 在 Linux 7.3 中开启 Zen 6 桌面处理器支持](https://www.techpowerup.com/352155/amd-starts-zen-6-desktop-enablement-in-linux-7-3) ⭐️ 6.5/10

AMD 已在 Linux 7.3 内核中开始为其即将推出的 Zen 6 桌面处理器（代号 "Olympic Ridge"）添加支持。更新包括为 Zen 6 Family 1Ah Model 80H 处理器添加 HSMP 协议第 7 版支持，以及 AMD PMF 平台驱动的新功能，其中包含一个新的用于设备指标查询的 ioctl 接口。 这次内核支持工作是 Zen 6 桌面处理器接近发布的重要里程碑，对 Linux 用户和开源生态系统有直接影响。每个 CCD 的核心数提升至最多 12 颗（此前最多 8 颗），以及转向台积电 N2 2nm 工艺，代表了重要的架构进步，将影响整个桌面 CPU 市场以及 AMD 对英特尔（Intel）的竞争地位。 Zen 6 架构将每个 CCD 的核心数提升至最多 12 颗（前代最多 8 颗），双 CCD 配置提供 12、16、20 核以及旗舰 24 核型号。转向台积电 N2 2nm 制造工艺可提供更高的晶体管密度，从而在每个 CCD 上容纳更多核心。

rss · TechPowerUp News · 8月31日 11:58

**背景**: AMD 的 Zen 微架构是其 Ryzen 处理器的基础，每一代通常都会带来性能和能效的提升。CCD（Core Complex Die，核心复合芯片）是 AMD 多芯片 CPU 设计中的一个小芯片模块，AMD 可以将多个 CCD 与一个 I/O 芯片组合以扩展核心数量。HSMP（Host System Management Port，主机系统管理端口）是一个允许操作系统级软件通过邮箱寄存器与系统管理固件通信的接口，可用于系统参数的监控和控制。AMD PMF（Platform Management Framework，平台管理框架）是一个 Linux 驱动，旨在通过适应用户行为和环境，使 AMD 电脑更智能、更安静、更节能，从而提升用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.kernel.org/arch/x86/amd_hsmp.html">20. AMD HSMP interface — The Linux Kernel documentation</a></li>
<li><a href="https://qsantos.fr/2024/10/03/amd-cpus-ccds-and-ccxs/">AMD CPUs, CCDs and CCXs - Quentin Santos</a></li>
<li><a href="https://www.guru3d.com/story/amd-zen-6-medusa-ridge-processor-leak-reveals-12core-ccd-architecture/">AMD Zen 6 Medusa Ridge Processor Leak Reveals 12- Core CCD ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Zen 6`, `#Linux kernel`, `#CPU architecture`, `#hardware`

---

<a id="item-10"></a>
## [英伟达和英特尔关键供应商遭搜查，涉嫌产地欺诈——欣兴电子面临 PCB 产地洗白调查，或遭 40%美国关税处罚](https://www.tomshardware.com/tech-industry/big-tech/key-nvidia-and-intel-supplier-raided-over-alleged-china-origin-fraud-unimicron-faces-probe-over-pcb-origin-washing-risk-of-40-percent-u-s-tariff-penalty) ⭐️ 6.5/10

台湾检方正在调查欣兴电子（Unimicron），该公司是英伟达、英特尔、谷歌和亚马逊的主要 PCB 及基板供应商，涉嫌将中国制造的 PCB 重新标注为台湾制造以规避美国关税，可能面临 40%的关税处罚。

rss · Tom's Hardware · 8月31日 11:55

**标签**: `#supply-chain`, `#semiconductors`, `#trade-policy`, `#nvidia`, `#intel`

---

<a id="item-11"></a>
## [苹果低估了 AI 驱动的 Mac Mini 和 Mac Studio 需求](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/) ⭐️ 6.0/10

一份报道指出，苹果因本地 AI 工作负载带来的需求激增而措手不及，Mac Mini、Mac Studio 等 Mac 机型销量超出预期，暴露出苹果据称缺乏专门面向企业客户的工程团队以及明确的企业 AI 战略。 这一事件意义重大，因为它暴露出全球最大的硬件公司之一在本地与边缘 AI 部署正在重塑开发者与企业硬件采购决策的当下所存在的战略盲区。这一缺口可能将聚焦 AI 的买家推向 NVIDIA、基于 AMD 的工作站，或联想、惠普等专业 AI 工作站等竞争对手。 据报道，苹果既没有专门面向企业客户的工程团队，也没有负责企业 AI 业务的开发者关系人员，因此未能预判或抓住专业人士在 Apple Silicon 上搭建本地大语言模型与推理环境的浪潮。社区反馈还显示，入门级的 Mac Neo 已售罄至 9 月下旬，表明需求远超高端型号。

hackernews · thm · 8月31日 12:41 · [社区讨论](https://news.ycombinator.com/item?id=49508982)

**背景**: Local AI refers to running AI models directly on a user's own hardware rather than relying on cloud-based services, and it has gained traction due to privacy concerns, lower latency, and the availability of capable consumer GPUs. Edge AI is a related concept that deploys AI algorithms on local edge devices rather than centralized data centers, enabling real-time processing without constant cloud connectivity. Apple's M-series chips, with unified memory architecture, have become popular for local AI inference because they can allocate large amounts of memory to AI workloads, which is a key advantage when running large language models on-device.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.local-llm.net/learn/what-is-local-ai/">What Is Local AI? The Complete Guide to Running AI on Your Own Hardware | local-llm.net</a></li>
<li><a href="https://www.ibm.com/think/topics/edge-ai">What is edge AI? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Edge_computing">Edge computing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论观点不一，但总体具有建设性。一位用户质疑本地 AI 方案能否真正与廉价的云端订阅服务抗衡，并表示即便使用 16GB 显存的 GPU 也难以获得理想体验。也有评论指出苹果这样规模的公司竟然缺乏企业战略实属讽刺，并对 Mac Mini 库存被 AI 买家抢购而非家庭影音爱好者购得表示不满。还有人希望在新任领导层带领下，苹果能重视系统稳定性并修复长期存在的 Bug。

**标签**: `#Apple`, `#Local AI`, `#Mac Mini`, `#Hardware Demand`, `#Edge Computing`

---

<a id="item-12"></a>
## [军人服务社冷柜疑似遭入侵引发工控安全讨论](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) ⭐️ 6.0/10

一篇推测性的 Substack 博文声称军方服务社的冷柜可能被入侵，此事在 Hacker News 上引发了讨论，相关专家对工业控制系统漏洞发表了见解。具有军方 IT 经验的评论者与描述真实遭遇未受保护且使用默认凭据的西门子 PLC 的工程师一同参与了讨论。 此次讨论揭示了关键和军事基础设施中 ICS 安全的真实且持续的担忧，使用默认凭据且通信未加密的遗留 PLC 仍然很常见。它还凸显了关岛和夏威夷等偏远海外基地如何成为国家级行为者寻求对当地经济产生连锁影响的高价值目标。 讨论中的工程师报告称，西门子 S7-1500 PLC 经常使用默认的 admin/admin 凭据部署，承包商通常缺乏在这些设备上启用 TLS 的专业知识。评论者还指出，国防服务社（DECA）似乎集中管理各基地的制冷设备，并且在没有基线故障率数据的情况下，每天少量故障可能是正常维护而非恶意活动。

hackernews · jcurbo · 8月31日 11:45 · [社区讨论](https://news.ycombinator.com/item?id=49508506)

**背景**: 可编程逻辑控制器（PLC）是一种用于自动化和监控工厂、基础设施和军事系统中物理过程的专用工业计算机，通常通过 SCADA 或 HMI 平台进行通信。基于这些 PLC 构建的工业控制系统（ICS）经常因遗留硬件、默认凭据、网络隔离不足以及在不中断运营的情况下难以应用补丁而存在漏洞。美国网络安全和基础设施安全局（CISA）定期发布 ICS 公告，列出此类漏洞，强调关键基础设施面临的持续风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/topics/industrial-control-systems">Industrial Control Systems | Cybersecurity and Infrastructure ... ICS Advisories - CISA Guide to Industrial Control Systems (ICS) Security | NIST Industrial Control System Cybersecurity: A Practical Guide The 2026 Cybersecurity Guide to Industrial Control Systems Top 10 most common vulnerabilities in Industrial Control ...</a></li>
<li><a href="https://cybersecmagazine.com/industrial-control-systems-vulnerabilities-and-best-practices/">Industrial Control Systems: Vulnerabilities and Best ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Programmable_logic_controller">Programmable logic controller - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 具有军方 IT 背景的 Hacker News 评论者总体上倾向于认为是配置错误而非蓄意入侵，同时对时机和偏远海外基地的定向价值表示担忧。工程师们通过分享西门子 PLC 仍使用默认 admin/admin 凭据运行以及承包商无法配置 TLS 的第一手经验，证实了文章的关注。怀疑论者则敦促保持谨慎，指出在不知道冷柜总数的情况下，每天少量故障很容易通过常规维护来解释。

**标签**: `#cybersecurity`, `#industrial-control-systems`, `#military`, `#critical-infrastructure`, `#plc-security`

---

<a id="item-13"></a>
## [经济高效地利用智能体自动化。验证领域的创新](https://semiwiki.com/artificial-intelligence/372524-exploiting-agentic-automation-cost-effectively-innovation-in-verification/) ⭐️ 6.0/10

围绕在经济高效的前提下,如何利用前沿模型及本地开源权重 AI 模型实现半导体验证工作流中的智能体自动化,展开的行业讨论。

rss · SemiWiki · 8月31日 13:00

**标签**: `#agentic-ai`, `#semiconductor-verification`, `#eda`, `#ai-cost-optimization`, `#open-weight-models`

---

<a id="item-14"></a>
## [Signaloid 创始人从剑桥离职，全职领导不确定性感知计算创业公司](https://semiwiki.com/ceo-interviews/372496-ceo-interview-with-phillip-stanley-marbell-of-signaloid/) ⭐️ 6.0/10

SemiWiki 发布了对 Signaloid 创始人 Phillip Stanley-Marbell 的 CEO 专访，他于 2025 年 9 月从剑桥大学物理计算讲席教授的全职职位离职，转为全职领导该公司。专访内容涵盖他从学术界到工业界的转型经历，以及 Signaloid 在不确定性感知计算平台方面的方法。 Stanley-Marbell 从剑桥的知名教授职位转向半导体创业公司，反映了概率计算和不确定性感知计算范式的商业势头日益增强。由于量化金融、物理仿真和机器学习中的工作负载本质上是概率性的，能够原生处理不确定性的架构可能会颠覆传统的 CPU/GPU 设计假设。 Signaloid 销售其计算平台，声称在量化金融、物理仿真和概率机器学习等概率工作负载上，相比现有高端处理器每核心可实现高达 1000 倍的加速。公司的知识产权源于 Stanley-Marbell 在剑桥领导的物理计算实验室的学术研究成果。

rss · SemiWiki · 8月30日 21:00

**背景**: 不确定性感知计算是一种旨在通过硬件原生表示和传播概率分布的范式，而不是将不确定性作为事后在软件中处理的问题。这与传统确定性计算（计算机处理精确数值）以及近似计算（牺牲精度换取效率但不明確追踪不确定性）形成对比。随着概率机器学习、贝叶斯推理以及在量化金融和科学计算中使用的蒙特卡洛模拟的发展，这种方法越来越受关注。Signaloid 将自己定位为专为这些概率工作负载构建的平台提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://signaloid.com/">Signaloid: The Future of Computing for Probabilistic Workloads</a></li>
<li><a href="https://signaloid.com/technology">Signaloid: Technology</a></li>
<li><a href="https://www.computer.org/csdl/magazine/co/2025/04/10938012/25mYGwzXBYc">Uncertainty in Machine Learning and Future Computers</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#uncertainty-computing`, `#signaloid`, `#startup-interview`, `#approximate-computing`

---

<a id="item-15"></a>
## [先进冷却技术应对汽车散热挑战](https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/) ⭐️ 6.0/10

简要新闻预告，介绍用于应对电驱动系统、人工智能处理器及自动驾驶汽车系统中日益增长的散热通量的新兴冷却技术。

rss · EE Times · 8月31日 07:46

**标签**: `#automotive`, `#thermal-management`, `#EV`, `#AI-hardware`, `#cooling-technology`

---

<a id="item-16"></a>
## [中国最大 DRAM 厂商长鑫存储因五角大楼军事黑名单起诉美国国防部](https://www.techpowerup.com/352190/chinas-top-dram-maker-cxmt-takes-pentagon-to-court-over-military-blacklist) ⭐️ 5.5/10

中国最大的 DRAM 制造商长鑫存储（CXMT）正在起诉美国国防部，指控其根据《1260H 条款》将其列入军事黑名单的做法不当，并辩称其遵循 JEDEC 商用标准的事实证明该公司与军方并无关联。

rss · TechPowerUp News · 8月31日 18:49

**标签**: `#semiconductors`, `#DRAM`, `#US-China tech relations`, `#geopolitics`, `#CXMT`

---

<a id="item-17"></a>
## [泄露版 DLSS 5 通过 FP16 模组在 RTX 20 系图灵显卡上测试](https://www.techpowerup.com/352181/leaked-dlss-5-is-being-tested-on-rtx-20-series-turing-gpus-now-runs-on-emulators-and-old-directx-titles) ⭐️ 5.5/10

modder 们已经使用 FP16 实现成功将泄露的 DLSS 5（DLSS-NR）DLL 移植到 NVIDIA 的 RTX 20 系图灵显卡上，开发者 ShortFuse 还发布了适用于老款 RTX 硬件的新版本。社区也已确认 DLSS 5 可在 PCSX2 模拟器（《Manhunt》）以及老旧的 DirectX 9/11 游戏中运行，远超 NVIDIA 官方支持的 API 范围，但不同游戏之间的兼容性仍不稳定。 这表明 NVIDIA 的下一代神经渲染技术在技术上可以在比其目标 Blackwell 架构早三代的硬件上运行，有可能延长老款 RTX 显卡的使用寿命。同时也凸显出 modder 社区在 NVIDIA 正式发布之前拆解和部署泄露版 DLSS 5 技术的惊人速度。 从 FP8 切换到 FP16 精度是关键：FP8 在 Ampere 显卡上导致性能崩溃，因为图灵和 Ampere 都不像 Blackwell 那样原生加速 FP8。测试结果非常不稳定——《Red Dead Redemption》可以运行，但《Red Dead Redemption 2》失败，《霍格沃茨之遗》卡在待机状态，《GTA 5》在大约十秒后丢失显示信号。

rss · TechPowerUp News · 8月31日 16:00

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.itechpost.com/articles/237175/20260830/nvidia-dlss-5-leaked-modders-bring-its-neural-rendering-ai-graphics-games.htm">NVIDIA DLSS 5 Leaked as Modders Bring Its Neural Rendering ...</a></li>

</ul>
</details>

**社区讨论**: RenoDX Discord 和 X（原 Twitter）上的社区成员一直在各种硬件配置上积极测试 DLSS 5，用户 @DystopianSuns 主导了 FP16 实现的开发工作。社区对于在老显卡和模拟器上运行该技术热情高涨，但测试者承认目前的体验仍然不稳定，离可用还差得很远。

**标签**: `#DLSS`, `#NVIDIA`, `#GPU`, `#graphics-technology`, `#modding`

---

<a id="item-18"></a>
## [战马开发者为 DLSS 5 辩护，称其并非 AI 垃圾滤镜](https://www.techpowerup.com/352160/warhorse-developer-defends-dlss-5-says-its-not-an-ai-slop-filter) ⭐️ 5.5/10

《天国：拯救 2》总监丹尼尔·瓦夫拉为 DLSS 5 辩护，称其是一项正当的照明改进技术，能够解决长期存在的阴影渲染问题，尽管会使帧率减半。

rss · TechPowerUp News · 8月31日 00:36

**标签**: `#DLSS`, `#NVIDIA`, `#gaming`, `#graphics-technology`, `#ray-tracing`

---

<a id="item-19"></a>
## [NVIDIA 在 616.56 驱动中封锁 mVolt+ 功耗限制超频功能](https://www.techpowerup.com/352157/nvidia-shuts-down-rtx-5000-power-limit-control-oc-in-latest-driver-update) ⭐️ 5.5/10

NVIDIA 最新驱动版本 616.56 破坏了 mVolt+ 超频工具绕过 RTX 5000 系列显卡默认功耗限制的能力，用户尝试提升功耗时会出现黑屏崩溃。值得注意的是，Hydra 2.3 测试版在新驱动下仍可正常工作，这表明冲突可能是非有意为之。 此举影响了那些无需硬件改装便能从 RTX 5090（最高 700W）和 RTX 5080（最高 680W）显卡中榨取额外性能的发烧友。这也引发了人们对于 NVIDIA 对绕过软件功耗限制工具立场的质疑，这些工具介于用户自由与保修/责任问题之间的灰色地带。 mVolt+ v0.36 暴露了隐藏的 Blackwell GPU 寄存器，允许分别控制 GPU 核心和显存的功耗通道限制，并可对 Core、XBAR、SYS 和 Video 等域进行电压调节。MSI Afterburner 等常规工具仍受限于 VBIOS 定义的功耗上限，要超过这些上限通常需要硬件分流电阻改装（shunt mod），而 mVolt+ 纯粹通过软件实现了同样的效果。

rss · TechPowerUp News · 8月30日 21:16

**背景**: GPU 超频通常需要借助软件工具来调整核心频率、显存频率和功耗限制等参数。NVIDIA 通过显卡上的 VBIOS（视频 BIOS）固件强制执行功耗上限，MSI Afterburner 等标准工具在不进行硬件改装的情况下无法突破该限制。分流电阻改装（shunt mod）是一种物理硬件改装，通过更换电阻使 GPU 读取到比实际更低的功耗值，从而间接抬高软件功耗上限。而 mVolt+ 这类工具则发现了未公开的 Blackwell GPU 硬件寄存器，能够完全通过软件绕过 VBIOS 功耗限制，让用户在无需改装硬件、不会影响保修的情况下获得更大的控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpu-drivers/nvidias-latest-driver-update-breaks-mvolt-overclocking-functionality-nifty-open-source-app-allowed-users-to-increase-the-power-limit-to-700w-on-their-rtx-50-series-gpus-without-hardware-mods">Nvidia's latest driver update breaks mVolt+ overclocking functionality...</a></li>
<li><a href="https://www.techpowerup.com/351867/nvidia-power-limit-bypass-rtx-5090-oc-hits-700-w-rtx-5080-up-to-680-w-no-shunt-mod-needed">NVIDIA Power Limit Bypass: RTX 5090 OC Hits 700 W, RTX 5080 ...</a></li>
<li><a href="https://windowsforum.com/windows-news.4/mvolt-0-36-unlocks-700w-rtx-5090-and-680w-rtx-5080.443441/">mVolt+ 0.36 Unlocks 700W RTX 5090 and 680W RTX 5080</a></li>

</ul>
</details>

**社区讨论**: Overclock.net 论坛和 X/Twitter（通过 Uniko's Hardware）的讨论显示，mVolt+ 在新驱动下尝试使用时会导致立即黑屏，但多位用户指出 Hydra 2.3 测试版仍可正常工作，这引发了人们猜测这可能只是兼容性问题而非刻意封杀。社区对于 NVIDIA 是否有意针对 mVolt+，抑或仅是未经测试的兼容问题并将在后续驱动中得到修复，仍然意见不一。

**标签**: `#nvidia`, `#gpu`, `#overclocking`, `#driver-update`, `#hardware`

---