---
layout: default
title: "Horizon Summary: 2026-08-09 (ZH)"
date: 2026-08-09
lang: zh
---

> 从 29 条内容中筛选出 14 条重要资讯。

---

1. [FCC moves to ban LiDAR-equipped foreign drones from US — classifies the technology as "military-grade" in a proposal that could also hit thermal models and the swarms used in drone light shows](#item-1) ⭐️ 7.5/10
2. [亚马逊在德州新建 7.65GW AI 数据中心发电厂或成美国最大 CO₂污染源——定制 35 台涡轮天然气电厂获批每年排放 3300 万吨温室气体](#item-2) ⭐️ 7.5/10
3. [Phantom Drive：开源 U 盘在诱饵驱动器后隐藏加密分区](#item-3) ⭐️ 7.5/10
4. [Shopify 将 Redis 替换为 MySQL 用于库存预占——并成功实现了规模化](#item-4) ⭐️ 7.0/10
5. [亚马逊利用 45 年前法规绕过吉尔罗伊社区投票建 AI 数据中心](#item-5) ⭐️ 6.5/10
6. [台达 GoCool-150 150kW 液冷-风冷 CDU 瞄准 NVIDIA VR NVL72](#item-6) ⭐️ 6.5/10
7. [英国研究：电动滑板车比摩托车更危险；DeepMind AI 提前预测飓风梅丽莎](#item-7) ⭐️ 6.3/10
8. [Nvidia RTX Spark 跑分泄露：20 核与 18 核双版本曝光](#item-8) ⭐️ 5.5/10
9. [堪萨斯小镇因 AI 数据中心收到死亡威胁取消公开评论改为线上会议](#item-9) ⭐️ 5.5/10
10. [Intel Core Ultra 7 270K Plus 对决 AMD Ryzen 7 7700X3D](#item-10) ⭐️ 5.5/10
11. [顶尖程序员创造可自我复制的 Piet Quine GIF](#item-11) ⭐️ 5.5/10
12. [美光对 Crucial 内存保修仅按原价赔偿，遭批评后修正方案](#item-12) ⭐️ 5.5/10
13. [Intel 8080 原始预生产红宝石膜所有者寻求修复者](#item-13) ⭐️ 5.5/10
14. [RTX 5090 在台湾以捆绑 8 块主板的奇葩套装出售](#item-14) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [FCC moves to ban LiDAR-equipped foreign drones from US — classifies the technology as "military-grade" in a proposal that could also hit thermal models and the swarms used in drone light shows](https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows) ⭐️ 7.5/10

The FCC is proposing a retroactive sales ban on foreign-made drones with LiDAR and other 'military-grade' features, potentially removing popular DJI models from US stores.

rss · Tom's Hardware · 8月9日 13:00

**标签**: `#drones`, `#FCC`, `#regulation`, `#DJI`, `#LiDAR`

---

<a id="item-2"></a>
## [亚马逊在德州新建 7.65GW AI 数据中心发电厂或成美国最大 CO₂污染源——定制 35 台涡轮天然气电厂获批每年排放 3300 万吨温室气体](https://www.tomshardware.com/tech-industry/data-centers/amazons-new-7-65gw-texas-ai-data-center-power-plant-could-become-the-largest-source-of-co2-pollution-in-the-us-custom-35-turbine-gas-plant-authorized-to-emit-33-million-tons-of-annual-greenhouse-gases) ⭐️ 7.5/10

亚马逊正在德克萨斯州为 AI 数据中心建设一座 7.65GW 的天然气发电厂，获批每年排放 3300 万吨二氧化碳，可能成为美国最大的单一二氧化碳排放源。

rss · Tom's Hardware · 8月9日 12:40

**标签**: `#AI infrastructure`, `#data centers`, `#environmental impact`, `#energy policy`, `#Amazon`

---

<a id="item-3"></a>
## [Phantom Drive：开源 U 盘在诱饵驱动器后隐藏加密分区](https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data) ⭐️ 7.5/10

一个名为"Phantom Drive"的新开源项目打造了一种 U 盘，外观是普通的 8GB 设备，但隐藏了一个加密分区，只有创建包含密码的文本文件才能解锁。自定义固件在写入操作过程中拦截密码，并在微控制器的 SRAM 中直接处理，密码本身永远不会被写入闪存。 密码永远不会写入闪存——自定义固件仅在哈希运算期间拦截并将其复制到微控制器的 SRAM 中，而 SRAM 是易失性的，断电后凭据即消失。由于隐藏分区及其认证数据存在于可见的 8GB 存储区域之外，对诱饵驱动器的取证分析无法发现隐藏秘密卷的存在。

rss · Tom's Hardware · 8月9日 12:00

**背景**: 加密中的合理推诿（plausible deniability）是指由于无法证明加密隐藏数据的存在，用户可以否认其存在——通常通过将一个加密卷嵌套在另一个卷内来实现，披露外部密码只会暴露无害内容。VeraCrypt 等软件工具通过在文件系统层面将内部卷隐藏在外部卷内来实现这一点。"Phantom Drive"将同样的理念下沉到硬件/固件层面，使用自定义 U 盘控制器固件，使隐藏分区不仅在文件系统层不可见，而且在原始存储布局中也不可见，密码本身也从不持久化到非易失性闪存中。SRAM（静态随机存取存储器）是微控制器内部的易失性存储器，断电后内容即丢失，因此非常适合用于临时的密码处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.comparitech.com/blog/information-security/plausible-deniability-encryption/">What is plausible deniability (in encryption ) and does it work?</a></li>
<li><a href="https://stealthcloud.ai/cryptography/plausible-deniability-encryption/">Plausible Deniability in Encryption : VeraCrypt and Hidden</a></li>
<li><a href="https://en.wikipedia.org/wiki/Firmware">Firmware - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#open-source`, `#encryption`, `#hardware`, `#privacy`

---

<a id="item-4"></a>
## [Shopify 将 Redis 替换为 MySQL 用于库存预占——并成功实现了规模化](https://shopify.engineering/scaling-inventory-reservations) ⭐️ 7.0/10

Shopify 详细介绍了他们如何在大规模场景下将库存预占从 Redis 替换为 MySQL，使用每个商品/位置的有界行池而非数量列来实现扩展。

hackernews · adletbalzhanov · 8月8日 22:32 · [社区讨论](https://news.ycombinator.com/item?id=49226536)

**标签**: `#shopify`, `#mysql`, `#redis`, `#scalability`, `#distributed-systems`

---

<a id="item-5"></a>
## [亚马逊利用 45 年前法规绕过吉尔罗伊社区投票建 AI 数据中心](https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window) ⭐️ 6.5/10

亚马逊在加利福尼亚州吉尔罗伊利用 45 年前的分区法规，秘密绕过了社区投票和公众意见征询期，开始建设一座大型 AI 数据中心。该项目的谈判始于 2020 年，公众意见征询期开放至 2024 年，但居民在建设动工时才发现，完全失去了直接参与的机会。 此次事件凸显了 AI 基础设施快速扩张所需的必要性与地方民主程序之间的重大矛盾。它引发了关于科技巨头在居民社区建设关键 AI 基础设施时问责制和透明度的更广泛问题，并可能为其他地方的类似项目开创先例。 据报道，该项目价值约 20 亿美元，建设在远早于 AI 时代设计的分区规则下推进。这些历史遗留法规使亚马逊得以避开通常适用于市内同规模开发项目的公开听证程序。

rss · Tom's Hardware · 8月8日 13:51

**背景**: AI 数据中心与传统数据中心有显著不同——它们需要更强的计算能力、更高的带宽、更低的网络延迟以及大幅增加的电力来支持 GPU 密集型工作负载。随着 AI 驱动服务的需求不断增长，大型科技公司已在美国各地积极争取土地和许可，目标常包括农村或郊区社区。加州立法者（包括州参议员 Steve Padilla）已提出多项法案，旨在监管数据中心的建设，因为公众对环境、健康和经济影响的担忧日益加剧。吉尔罗伊案件正体现了在 AI 热潮之前起草的分区条例如何被利用，来批准现代基础设施项目而无需充分的公众监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window">Amazon secretly circumvents community vote for massive AI ...</a></li>
<li><a href="https://www.gadgetreview.com/no-votes-no-hearings-how-amazon-built-a-2-billion-data-center-that-no-one-noticed">No Votes, No Hearings: How Amazon Built a $2 Billion Data ...</a></li>
<li><a href="https://calmatters.org/environment/2026/06/imperial-county-data-center/">Imperial County approved a massive data center. Then it ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#corporate accountability`, `#community impact`, `#Amazon`

---

<a id="item-6"></a>
## [台达 GoCool-150 150kW 液冷-风冷 CDU 瞄准 NVIDIA VR NVL72](https://www.servethehome.com/deltas-gocool-150-goes-big-to-enable-150kw-liquid-to-air-cooling-for-asrock-racks-vr-nvl72/) ⭐️ 6.5/10

台达推出了 GoCool-150，这是一款 150kW 的液冷转风冷冷媒分配单元（CDU），专门用于为 ASRock Rack 的 NVIDIA VR NVL72 及其他高密度 AI 机柜散热。该设备作为大型热交换器，可应对下一代机柜级 AI 系统所产生的极端热负载。 随着 AI 加速器将单机柜功率密度推高至 100kW 以上，传统风冷已无法胜任，大容量 CDU 已成为关键基础设施。台达这款 150kW 液冷转风冷 CDU 使数据中心即使没有机房水路接口也能部署液冷机柜，扩展了 NVIDIA Vera Rubin 平台的实际部署场景。 GoCool-150 采用液冷转风冷架构，即热量排向环境空气而非机房水回路，这简化了在现有数据中心中的改造部署。凭借 150kW 的散热能力，单台设备即可处理整个 NVL72 级机柜的热输出，该机柜集成 72 颗 Rubin GPU 和 36 颗 Vera CPU。

rss · ServeTheHome · 8月8日 15:05

**背景**: 冷媒分配单元（CDU）负责在数据中心内调节、循环并分配液冷工质，连接机房级与机柜级冷却回路。NVIDIA 的 VR NVL72 是一个机柜级 AI 超级计算系统，集成了 72 颗 Rubin GPU 和 36 颗 Vera CPU，采用 NVLink 6 互联，并使用全液冷、无线缆的托盘设计。随着每机柜 GPU 功耗从早期几代的约 10kW 增长到今天远超 100kW，液冷已从 HPC 领域的小众技术转变为主流 AI 基础设施的必备方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nautilusdt.com/blog/what-is-a-coolant-distribution-unit-cdu/">What Is a Coolant Distribution Unit ( CDU )? - Nautilus Data ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72</a></li>
<li><a href="https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack">NVIDIA Launches Vera Rubin Architecture at CES 2026: The VR NVL72 Rack - StorageReview.com</a></li>

</ul>
</details>

**标签**: `#liquid-cooling`, `#AI-infrastructure`, `#data-center`, `#NVIDIA-NVL72`, `#CDU`

---

<a id="item-7"></a>
## [英国研究：电动滑板车比摩托车更危险；DeepMind AI 提前预测飓风梅丽莎](https://www.solidot.org/story?sid=85039) ⭐️ 6.3/10

对英格兰和威尔士 2020–2022 年创伤数据的分析发现，成年电动滑板车骑行者遭受创伤性脑损伤的风险比摩托车骑行者高 3.5 倍，但仅 5.9%佩戴了头盔。同时，Google DeepMind 的 WeatherNext AI 模型以 80%的置信度提前五天预测飓风梅丽莎将以五级强度登陆牙买加，发表于《自然》的论文证明其比传统模型多提供一天的预警时间。 这些发现凸显了电动滑板车法规和头盔佩戴的紧迫公共安全问题，而 WeatherNext 的突破展示了机器学习如何改变拯救生命的灾害准备工作。该 AI 模型多出的一天预警时间，对于飓风路径上的社区而言可能是生与死的区别。 创伤数据集涵盖英格兰和威尔士 18 个城市的 15,247 名患者，包括 580 名电动滑板车骑行者、7,027 名摩托车骑行者和 7,640 名自行车骑行者；女性骑行者遭受严重伤害的可能性是男性的 2.1 倍，可能是因为大多数电动滑板车的设计针对男性体型。WeatherNext 由 Google DeepMind 和 Google Research 联合开发，通过在广泛的天气数据上训练来专门预测热带气旋，尽管气旋样本有限，并将开源发布。

rss · Solidot · 8月8日 13:52

**背景**: 电动滑板车作为便捷的微型交通工具已在全球城市迅速普及，但随着法规难以跟上其普及速度，其安全性一直备受争议。飓风梅丽莎于 2025 年 10 月袭击牙买加，造成灾难性洪水和山体滑坡。传统天气预报依赖基于物理学的数值模型，需要巨大的计算资源，而 WeatherNext 等 AI 方法直接从历史天气数据中学习模式，以更快、更便宜且有时更准确的方式生成预报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/">AI model achieves breakthrough in forecasting cyclones</a></li>
<li><a href="https://www.techtimes.com/articles/323617/20260808/weathernext-publishes-proof-cyclone-ai-gave-nhc-extra-day-warning-hurricane-melissa.htm">WeatherNext Publishes Proof: Cyclone AI Gave NHC Extra Day of...</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/weathernext-2/">WeatherNext 2: Google DeepMind’s most advanced forecasting model</a></li>

</ul>
</details>

**标签**: `#public-safety`, `#e-scooter`, `#Google-DeepMind`, `#AI-weather-forecasting`, `#hurricane-prediction`

---

<a id="item-8"></a>
## [Nvidia RTX Spark 跑分泄露：20 核与 18 核双版本曝光](https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests) ⭐️ 5.5/10

Nvidia RTX Spark 的两个版本已现身 Geekbench：完整 20 核型号单核得分 2,570、多核得分 23,126；精简版 18 核型号单核得分 2,541、多核得分 21,776。两者在单核和多核测试中均优于大多数 x86 移动处理器。 这些泄露信息表明 Nvidia 正在为紧凑型 AI 工作站和轻薄笔记本准备旗舰版与低配版两款 RTX Spark，为 Windows-on-Arm 生态系统注入了一位强有力的性能竞争者。出色的多核跑分说明 Grace Arm CPU 在通用负载下已经足够成熟，能够挑战传统 x86 移动处理器，而不仅仅局限于 AI 加速场景。 20 核版本与此前公布的 GB10 Grace Blackwell 超级芯片配置一致，该芯片将 Arm 架构 Grace CPU 与 Blackwell GPU 整合，并配备最高 128GB 一致性统一 LPDDR5x 内存，用于 DGX Spark。18 核精简版此前未曾公布，可能面向更低价位市场，同时保留绝大部分多核性能（仅比完整版低约 6%）。

rss · Tom's Hardware · 8月9日 13:20

**背景**: RTX Spark 是 Nvidia GB10 Grace Blackwell 超级芯片的消费级品牌名称，该芯片在一块封装上通过 NVLink-C2C 互联整合了基于 Arm 架构的 Nvidia Grace CPU 与 Blackwell 架构 GPU。它定位为个人 AI 超级计算机，本地可运行最高 2000 亿参数的大语言模型，提供高达 1 PFLOP 的 FP4 AI 算力。该芯片是 DGX Spark 桌面设备的基础，并预计将扩展到运行 Windows on Arm 的轻薄笔记本和小型 PC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/products/rtx-spark/">Slim Laptops & Small Desktops | NVIDIA RTX Spark</a></li>
<li><a href="https://dam-cdn.nvd.orangelogic.com/AssetLink/3lhuar5pc56pn7se4c7ahsskw20xw8h5.pdf">NVIDIA DGX Spark | NVIDIA</a></li>
<li><a href="https://www.linkedin.com/pulse/nvidia-rtx-spark-could-big-push-windows-arm-has-been-david-altavilla-mo37f">NVIDIA RTX Spark Could Be The Big Push Windows On Arm Has...</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#rtx-spark`, `#geekbench`, `#hardware-benchmarks`, `#gb10`

---

<a id="item-9"></a>
## [堪萨斯小镇因 AI 数据中心收到死亡威胁取消公开评论改为线上会议](https://www.tomshardware.com/tech-industry/data-centers/kansas-town-silences-public-comment-on-gigawatt-ai-data-center-after-receiving-death-threats-moves-to-virtual-meetings-shift-follows-physics-teachers-arrest-for-clapping-at-data-center-hearing) ⭐️ 5.5/10

堪萨斯州恩波里亚市因一座拟建的吉瓦级 AI 数据中心引发的争议收到针对市领导人的死亡威胁，随后取消了市议会会议的公开评论环节，全面改为线上举行。此前，一名物理教师因在数据中心听证会上鼓掌而被逮捕，进一步激化了矛盾。 此事件表明，美国小型社区正因 AI 基础设施热潮而爆发激烈的地方反对情绪，其激烈程度足以压制正常的民主参与。随着超大规模 AI 园区日益需要吉瓦级电力容量——相当于一座小城市的用电需求——科技驱动的能源需求与当地居民之间的冲突可能会变得更加普遍。 吉瓦级数据中心的单机架功耗约为传统设施的 10 倍，电力消耗堪比一座小型城市。取消线下公开评论不仅影响了反对数据中心的居民，也波及了希望提出其他议题的普通市民，引发了对会议程序的额外质疑。

rss · Tom's Hardware · 8月9日 12:20

**背景**: 随着大语言模型及其他生成式 AI 工作负载的训练和推理需求激增，AI 数据中心已从几十兆瓦级别迅速扩展到吉瓦级园区。Meta 等公司已宣布投资数十亿美元建设 1 GW 的设施，这些项目的占地和能耗远远超过传统云数据中心。恩波里亚这样的小城市之所以被选中，是因为当地拥有可用的土地和电网资源，但工业级基础设施的突然入驻往往与当地居民的预期产生冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techplustrends.com/power-requirements-ai-data-centers/">Power Requirements for AI Data Centers (2026): Complete Guide</a></li>
<li><a href="https://www.novaedgedigitallabs.in/Blog/meta-10-billion-ai-data-center-indiana-2026">Meta's $10B AI Data Center : 1 Gigawatt Power (2026) | NovaEdge...</a></li>
<li><a href="https://inforcapital.com/news/africa-needs-grid-scale-energy-to-power-ai-data-centres/">Africa's AI Data Centers Need Gigawatt Power Overhaul</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#community impact`, `#civic engagement`, `#tech policy`

---

<a id="item-10"></a>
## [Intel Core Ultra 7 270K Plus 对决 AMD Ryzen 7 7700X3D](https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-7-270k-plus-vs-amd-ryzen-7-7700x3d-faceoff) ⭐️ 5.5/10

Tom's Hardware 发布了一篇对决评测，将 Intel Core Ultra 7 270K Plus 与 AMD Ryzen 7 7700X3D 进行对比，从游戏性能、生产力、功耗和性价比等维度对两款处理器进行了全面评估。 此次对比面向中高端 CPU 市场的消费者，这一领域历来由 AMD 的 3D V-Cache 技术在游戏基准测试中占据主导，而 Intel 最新的 Core Ultra 架构正试图夺回失地。 AMD Ryzen 7 7700X3D 利用堆叠式 3D V-Cache 技术大幅扩展 L3 缓存容量以提升游戏性能，而 Intel Core Ultra 7 270K Plus 则代表了 Intel 较新的基于 chiplet 的桌面架构，具有改进的效率与特性目标。

rss · Tom's Hardware · 8月9日 12:05

**背景**: AMD 的 3D V-Cache 是一项封装技术，它在 CPU 芯片上方堆叠额外的 L3 缓存层，使处理器可用的缓存容量增加到原来的三倍。这种额外的缓存大幅降低了游戏负载中的内存延迟，这也是自 2022 年首款 Ryzen 7 5800X3D 发布以来，X3D 系列 Ryzen 处理器始终在游戏基准测试中名列前茅的原因。Intel 的 Core Ultra 品牌于 2023 年末随 Meteor Lake（第一代）推出，标志着该公司转向基于 chiplet 的设计理念，后续世代包括 Lunar Lake 和 Panther Lake（第三代，于 2026 年 CES 推出），将产品线扩展至移动端和桌面端。因此，这场对决在关键价位段上，将 AMD 久经验证的游戏缓存优势与 Intel 较新的架构方案进行了直接较量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/processors/technologies/3d-v-cache.html">AMD 3D V-Cache™ Technology</a></li>
<li><a href="https://www.digitaltrends.com/computing/what-is-amd-3d-v-cache/">What is AMD 3D V-Cache? Extra gaming performance unlocked What is 3D V-Cache? — AMD X3D Technology Explained What is AMD 3D V-Cache and why is it so special? - CORSAIR 3D V-Cache Explained: Why X3D CPUs Win at Gaming - Newegg.com What Is AMD 3D V-Cache and How Does It Work? - MUO</a></li>
<li><a href="https://en.wikipedia.org/wiki/Panther_Lake_(microprocessor)">Panther Lake (microprocessor) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cpu-comparison`, `#intel`, `#amd`, `#hardware-review`, `#benchmark`

---

<a id="item-11"></a>
## [顶尖程序员创造可自我复制的 Piet Quine GIF](https://www.tomshardware.com/software/programming/mind-bending-self-replicating-gif-code-prints-an-exact-copy-of-itself-is-both-a-program-and-its-own-visual-output-champion-coder-shows-off-piet-quine-technique) ⭐️ 5.5/10

一位顶尖程序员创造了一个「Piet Quine」——一个 GIF 图像，它同时作为一个 Piet 程序运行，并作为自身逐字节精确的视觉输出。该成果将 Piet 这种程序看起来像抽象画的神秘编程语言与 quine（自我复制程序）的概念结合在了一起。 这是神秘编程社区中的一项创意编程里程碑，展示了 Piet 语言的极端灵活性，并拓展了「既是源代码又是渲染输出」的边界。虽然它对主流软件工程没有直接的实用影响，但它展现了非常规编程范式中艺术性与创造力的可能性。 该 Piet Quine 同时作为可执行程序和 GIF 图像文件运行，在代码和视觉两个维度上实现了逐字节精确的自我复制。创作者被称为「冠军程序员」，暗示其在竞技或神秘编程圈内获得过认可，但原始材料中并未详述其具体身份、竞赛成绩或实现的技术限制。

rss · Tom's Hardware · 8月9日 11:40

**背景**: Piet 是由 David Morgan-Mar 设计的基于栈的神秘编程语言，程序以彩色方块编码，排列成类似抽象画的图案；指令由颜色之间的过渡决定，这些颜色按色相和亮度周期排列。Quine（自复制程序）是一种运行后将自身源代码作为输出（且不读取源文件）的程序，以哲学家和逻辑学家 Willard Van Orman Quine 命名，与可计算性理论中的 Kleene 不动点定理相关。将这两个概念结合，意味着创造一幅视觉艺术作品，当它作为 Piet 程序被解释时，会输出该作品本身的精确像素数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dangermouse.net/esoteric/piet.html">DM's Esoteric Programming Languages - Piet</a></li>
<li><a href="https://esolangs.org/wiki/Piet">Piet - Esolang</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quine_(computing)">Quine (computing) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#esoteric-programming`, `#quine`, `#piet`, `#creative-coding`, `#self-replicating-code`

---

<a id="item-12"></a>
## [美光对 Crucial 内存保修仅按原价赔偿，遭批评后修正方案](https://www.tomshardware.com/pc-components/ram/micron-reportedly-offers-pennies-on-the-dollar-for-crucial-ram-return-only-offers-to-reimburse-original-msrp-despite-it-being-only-37-percent-of-market-value-chipmaker-later-reverses-course-with-a-better-solution) ⭐️ 5.5/10

美光最初在处理 Crucial 内存保修退货时，仅按产品原始建议零售价（MSRP）赔偿给一位 Crucial 内存用户，而该价格仅相当于当前市场价值的 37%，但在事件引起公众关注后，美光修正方案，提供了更好的解决方案。 此事对依赖终身保修服务的 PC 装机用户和 Crucial 消费者十分重要，并在美光逐步退出消费级内存业务、转向 AI 数据中心产品的背景下，引发了人们对 RMA（退货授权）流程公平性的更广泛担忧。 赔偿金额仅为当前市场价值的 37%，意味着在美光修正方案之前，消费者在保修索赔中将承担 63%的价值损失；Crucial 内存由美光消费产品集团（Micron CPG）提供有限终身保修服务。

rss · Tom's Hardware · 8月9日 11:20

**背景**: Crucial 是美光面向消费者的内存品牌，在零售 RAM 和 SSD 市场已有近 30 年历史。2025 年 12 月，美光宣布将退出 Crucial 消费业务——包括通过零售商、电商平台和分销商的销售渠道——以重新聚焦于 AI 驱动的内存产品。Crucial 品牌内存模块享有有限终身保修服务，承诺对存在材料或工艺缺陷的产品进行维修或更换。RAM 的市场价格相对原始 MSRP 可能会有大幅波动，尤其是在供应短缺时期，这使得 37%的赔偿金额显得尤为刺眼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investors.micron.com/news-releases/news-release-details/micron-announces-exit-crucial-consumer-business">Micron Announces Exit from Crucial Consumer Business | Micron ...</a></li>
<li><a href="https://www.crucial.com/company/warranty">crucial .com/company/ warranty</a></li>
<li><a href="https://www.indmoney.com/blog/us-stocks/why-micron-is-killing-crucial-ram">Why Micron Is Killing Its Consumer Memory Business ‘Crucial’</a></li>

</ul>
</details>

**标签**: `#micron`, `#crucial`, `#ram`, `#warranty`, `#consumer-rights`

---

<a id="item-13"></a>
## [Intel 8080 原始预生产红宝石膜所有者寻求修复者](https://www.tomshardware.com/pc-components/cpus/owner-of-original-intel-8080-pre-production-layout-seeks-restorer-handcrafted-rubylith-mask-shows-5-000-transistors-and-interconnect-patterns-of-the-fabled-2-mhz-cpu) ⭐️ 5.5/10

原始 Intel 8080 微处理器预生产红宝石膜的所有者正在寻找一位技艺精湛的修复者，以保存这一具有重要历史意义的计算文物。这张手工制作的红膜掩模展示了这款 2 MHz CPU 约 5,000 个晶体管及互连图案的布局。 这一文物代表了计算史上最具影响力的微处理器之一的物理设计蓝图——8080 推动了个人电脑时代的到来，并影响了无数后续处理器架构。它的保存之所以重要，是因为早期半导体时代这种手工制作的设计文物已越来越稀少，是了解早期 CPU 工程设计方式不可替代的第一手资料。 该红宝石膜显示了约 5,000 个晶体管，与 Intel 8080 已知晶体管数量一致；其制作方法是手工切割红色半透明薄膜层并逐一剥离，以定义电路图案。这些组合后的图层随后通过照相缩小到玻璃板上，制成用于晶圆制造的光刻掩模。

rss · Tom's Hardware · 8月9日 11:00

**背景**: Intel 8080 于 1974 年发布，是一款 8 位微处理器，相比 Intel 早期的 8008 是一次重大飞跃，运行速度约为后者的十倍。它是最早能够独立运行的通用微处理器之一，为个人电脑革命奠定了基础，并对后来的 CPU 产生了直接影响。红宝石膜（Rubylith mask）是 1970 年代 IC 设计的标准方法：工程师在红色半透明的红宝石薄膜上手工切割图案，剥离选定区域以定义电路特征，然后将合并后的图层通过照相缩小到玻璃板上，制成用于硅晶圆光刻的掩模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel_8080">Intel 8080 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rubylith">Rubylith - Wikipedia</a></li>
<li><a href="https://www.computerhistory.org/revolution/story/287">Designing Integrated Circuits - CHM Revolution</a></li>

</ul>
</details>

**标签**: `#intel-8080`, `#computing-history`, `#hardware-preservation`, `#rubylith-mask`, `#cpu-design`

---

<a id="item-14"></a>
## [RTX 5090 在台湾以捆绑 8 块主板的奇葩套装出售](https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-ships-in-bizarre-8-motherboard-bundle-retailers-hold-gpus-hostage-similar-to-the-crypto-boom) ⭐️ 5.5/10

台湾电商平台 PChome24h 将 Nvidia RTX 5090 显卡与最多 8 块主板、入门到中端显卡以及其他配件打包出售，迫使消费者购买不需要的额外硬件才能买到想要的显卡。 这种捆绑销售行为表明 RTX 5090 供应严重紧张，与加密货币挖矿热潮时期的黄牛倒卖手法如出一辙，当时矿工大量扫货导致显卡供应崩溃。台湾的消费者和 PC 装机爱好者被迫为一套他们并不完全需要的整机支付高得多的费用。 RTX 5090 基于 Nvidia Blackwell 架构，配备 32GB GDDR7 显存和 512 位显存接口，于 2025 年 1 月发布，是 RTX 50 系列的旗舰产品。捆绑套装中包含入门到中端显卡及主板，这表明零售商正试图通过将滞销库存与稀缺的高端产品挂钩来清仓。

rss · Tom's Hardware · 8月8日 17:08

**背景**: 在 2017 至 2021 年的加密货币挖矿热潮期间，矿工需要大量 GPU 来挖掘以太坊等币种，导致显卡需求极其旺盛。这催生了广泛的黄牛倒卖、哄抬物价以及捆绑销售行为，零售商迫使消费者在购买稀缺显卡的同时购买不需要的配件。RTX 5090 作为 Nvidia 基于 Blackwell 架构的当前旗舰消费级显卡，同样受到游戏玩家和 AI/计算用户的高度追捧。PChome24h 是台湾最大的 B2C 电商平台之一，自 2007 年起以 24 小时到货服务闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GeForce_RTX_50_series">GeForce RTX 50 series - Wikipedia</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/geforce-rtx-5090.c4216">NVIDIA GeForce RTX 5090 Specs | TechPowerUp GPU Database</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPU_mining">GPU mining - Wikipedia</a></li>

</ul>
</details>

**标签**: `#hardware`, `#gpu`, `#nvidia`, `#rtx5090`, `#market-trends`

---