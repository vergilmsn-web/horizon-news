---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 79 条内容中筛选出 20 条重要资讯。

---

1. [英伟达向联发科投资 35 亿美元，拓展 NVLink Fusion 生态](#item-1) ⭐️ 8.5/10
2. [Intel 14A 制程缺陷密度优于目标，22nm 以来最佳](#item-2) ⭐️ 8.0/10
3. [Linux 内核补丁为 Apple Silicon SoC 添加 USB4/Thunderbolt 支持](#item-3) ⭐️ 7.5/10
4. [MacBook Neo SSD 写入循环消耗速度惊人](#item-4) ⭐️ 7.5/10
5. [CXMT 启动 HBM3E 内存风险量产](#item-5) ⭐️ 7.5/10
6. [无电机弹热制冷系统利用余热实现冷却](#item-6) ⭐️ 7.5/10
7. [Unimicron 涉嫌 PCB 产地洗白遭调查](#item-7) ⭐️ 7.5/10
8. [长鑫存储率先量产 LPDDR6，小米手机首发搭载](#item-8) ⭐️ 7.5/10
9. [面向芯片验证的高性价比智能体 AI 策略](#item-9) ⭐️ 7.0/10
10. [长鑫存储起诉五角大楼](#item-10) ⭐️ 7.0/10
11. [SK hynix 考虑采用 Intel Foundry 代工 HBM4E 基础芯片](#item-11) ⭐️ 6.5/10
12. [AMD 在 Linux 7.3 中启动 Zen 6 桌面处理器支持](#item-12) ⭐️ 6.5/10
13. [人类何时失去了食用昆虫的习惯？](#item-13) ⭐️ 6.3/10
14. [利用 BirdNet-Go 将安防摄像头改造为自动鸟类识别系统](#item-14) ⭐️ 6.0/10
15. [美军军营超市冷柜疑似遭远程操控](#item-15) ⭐️ 6.0/10
16. [ChatGPT 智能体工具与技能参考指南](#item-16) ⭐️ 6.0/10
17. [先进冷却技术应对汽车散热挑战](#item-17) ⭐️ 6.0/10
18. [中国芯片公司上半年业绩亮眼](#item-18) ⭐️ 6.0/10
19. [Steam Deck 已认证与可玩游戏突破 30,000 款](#item-19) ⭐️ 5.5/10
20. [改装者打造经济实惠的开源霍尔效应分体人体工学键盘](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [英伟达向联发科投资 35 亿美元，拓展 NVLink Fusion 生态](https://www.techpowerup.com/352174/nvidia-invests-usd-3-5-billion-in-mediatek-partners-on-nvlink-fusion) ⭐️ 8.5/10

英伟达宣布向联发科投资 35 亿美元，并通过 NVLink Fusion 生态系统深化合作，使联发科能够向包括谷歌在内的 ASIC 客户提供 NVLink Fusion IP，使其定制 XPU 可通过 NVLink-C2C 互连和 NVHBM 内存接入英伟达的数据中心架构。 这笔交易模糊了英伟达专有 GPU 架构与第三方加速器之间的界限，使竞争对手的 ASIC（如谷歌 TPU）能够接入英伟达的互联栈，可能重塑 AI 数据中心的构建方式。此举抗衡了博通、AMD 和超算联盟的替代纵向扩展架构，同时将已是主要 ASIC 设计者的联发科更紧密地绑入英伟达的体系。 NVLink Fusion 是在英伟达以色列研究中心开发的 IP/Chiplet 框架，这是英伟达首次将其授权给第三方芯片制造商。英伟达还披露了 NVHBM，它将内存控制器集成到 3D HBM 堆栈中，相比 HBM4E 可提供高达 30%的更高带宽、15%的 HBM 功耗降低以及多达 25%的可用计算芯片面积；NVLink-C2C 本身可提供 900 GB/s 的双向芯片间带宽。

rss · TechPowerUp News · 8月31日 13:55

**背景**: NVLink 是英伟达专有的高带宽互连技术，用于在机柜级系统中连接 GPU，以及后来的 CPU。NVLink-C2C 将此概念扩展到芯片间的链路，最初在 Grace Hopper 超级芯片中引入，以消除 CPU 与 GPU 之间的 PCIe 瓶颈。NVLink Fusion 更进一步：英伟达不再只销售完整的英伟达系统，而是将其互连 IP 授权出去，使定制的"XPU"——业界对非英伟达 AI 加速器（如谷歌 TPU、AWS Trainium 或基于博通的 ASIC）的统称——可以使用相同的网络语言。联发科虽然以移动 SoC 著称，但已悄然成为服务于谷歌等超大规模客户的主要 ASIC 设计公司，因此成为英伟达触及这些客户的重要战略门户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techinasia.com/news/nvidia-unveils-ai-chip-communication-tech-nvlink-fusion">Tech in Asia - Connecting Asia's startup ecosystem</a></li>
<li><a href="https://www.leviathansystems.co/glossary/nvlink-c2c">What Is NVLink - C 2 C ? | Leviathan Systems</a></li>
<li><a href="https://www.servethehome.com/arm-joins-the-nvidia-nvlink-fusion-ecosystem-vera/">Arm Joins the NVIDIA NVLink Fusion Ecosystem - ServeTheHome</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#MediaTek`, `#NVLink-Fusion`, `#semiconductors`, `#data-center`, `#AI-infrastructure`

---

<a id="item-2"></a>
## [Intel 14A 制程缺陷密度优于目标，22nm 以来最佳](https://semiwiki.com/semiconductor-manufacturers/intel/372866-intels-14a-is-winning-the-race-against-defects/) ⭐️ 8.0/10

Intel 的 14A 制程展现出异常强劲的早期进展，缺陷密度下降速度快于公司内部目标。首席财务官 David Zinsner 在德意志银行 2026 年技术会议上表示，这是 Intel 自 22nm 节点以来发展最为顺利的一次制程迭代。 这一里程碑增强了人们对 Intel 制造路线图及其吸引 Apple、Nvidia 等外部代工客户的信心。同时恰逢有报道称 Intel 考虑将代工业务重心从 18A 转向 14A，这将重塑 Intel 与台积电、三星之间的竞争格局。 缺陷密度是先进半导体制造中决定晶圆良率、产品性能和单颗芯片成本的核心指标。节点早期阶段的缺陷下降速度快于预期，通常意味着该节点能够加速进入大规模量产并具备有竞争力的经济性。

rss · SemiWiki · 8月31日 21:00

**背景**: 制程节点（如 Intel 的 14A）代表半导体制程技术的逐代演进，每一代通常意味着更小的晶体管、更优的功耗表现和更高的晶体管密度。Intel 的代工战略旨在为外部客户制造芯片，直接与台积电和三星代工业务竞争。公司原本计划以 18A 节点作为吸引大型代工客户的主力，但据报道目前正将这一重心转向 14A。缺陷密度衡量单位晶圆面积上的制造缺陷数量，缺陷密度越低，良率越高，单颗芯片成本越低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kad8.com/hardware/intel-14a-node-beats-internal-targets-in-best-progress-since-22nm/">Intel 14 A Node Beats Internal Targets in Best Progress Since 22nm</a></li>
<li><a href="https://www.techtimes.com/articles/325890/20260828/intel-14a-defect-drop-rivals-22nm-era-customers-now-asking-capacity-not-data.htm">Intel 14 A Defect Drop Rivals 22nm Era: Customers Now Asking for...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/intel-might-axe-the-18a-process-node-for-foundry-customers-essentially-leaving-tsmc-with-no-rival-intel-reportedly-to-focus-on-14a">Intel might axe the 18 A process node for foundry... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Intel`, `#manufacturing`, `#14A-node`, `#foundry`

---

<a id="item-3"></a>
## [Linux 内核补丁为 Apple Silicon SoC 添加 USB4/Thunderbolt 支持](https://www.techpowerup.com/352199/linux-kernel-patch-expands-usb4-support-for-apple-silicon-socs) ⭐️ 7.5/10

Asahi Linux 开发者 Sven Peter 提交了上游 Linux 内核补丁，为 Apple Silicon M1、M2 和 M3 SoC 添加了初步的 USB4 和 Thunderbolt 支持，扩展了在 Linux 系统上运行的 MacBook 的外设兼容性。 这对 Asahi Linux 项目来说是一个重要的里程碑，因为 USB4/Thunderbolt 是现代 Apple Silicon Mac 上的主要扩展接口。没有它，用户在 Linux 上连接高速外设、外接显卡、显示器和扩展坞的能力一直受到限制。 Apple Silicon Mac 上每个支持 USB4 的 Type-C 接口都包含一个 ACIO 块，其中有一个 Cortex-M3 协处理器来管理 USB4 路由器。这些补丁目前正通过 LKML 邮件列表发送到主线 Linux 内核。

rss · TechPowerUp News · 8月31日 23:52

**背景**: Asahi Linux 项目旨在为使用 Apple 自研 ARM 架构芯片（自 2020 年 M1 起）的 Mac 带来完善的 Linux 体验。USB4 是一种基于 Thunderbolt 的连接标准，可通过单个 USB-C 接口实现高带宽数据传输、显示输出和 PCIe 隧道。Thunderbolt 最初是由 Apple 与 Intel 合作开发的。支持这些功能进入主线 Linux 内核意味着用户将获得官方的、经过充分测试的驱动，而不必依赖于主线之外的补丁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://asahilinux.org/">Asahi Linux</a></li>
<li><a href="https://en.wikipedia.org/wiki/USB4">USB4 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Linux`, `#Apple Silicon`, `#USB4`, `#Thunderbolt`, `#Asahi Linux`

---

<a id="item-4"></a>
## [MacBook Neo SSD 写入循环消耗速度惊人](https://www.techpowerup.com/352178/macbook-neo-burns-through-ssd-cycles-at-an-alarming-rate) ⭐️ 7.5/10

测试显示，苹果入门级 MacBook Neo 仅配备 8GB 内存，因大量使用交换空间导致 SSD 写入循环消耗极快，256GB 型号预估使用寿命仅约 414TB。

rss · TechPowerUp News · 8月31日 15:43

**标签**: `#Apple`, `#MacBook Neo`, `#SSD`, `#hardware`, `#consumer-tech`

---

<a id="item-5"></a>
## [CXMT 启动 HBM3E 内存风险量产](https://www.techpowerup.com/352175/cxmt-starts-risk-production-of-hbm3e-memory) ⭐️ 7.5/10

据报道，中国存储厂商长鑫存储（CXMT）已开始 HBM3E 内存的风险量产，标志着中国在面向 AI 加速器的高带宽内存国产化方面取得了重要进展。尽管如此，CXMT 仍比韩国竞争对手 SK 海力士和三星落后约两代，后者已在向 HBM4E 过渡。 HBM3E 对大型 AI 模型的训练和推理至关重要，全球供应由韩国和美国厂商主导，这为中国 AI 硬件带来了战略性供应链风险。即使 CXMT 仍处于追赶状态，其进展仍是中国在美国先进 AI 芯片出口管制背景下推动半导体自主可控的关键指标。 风险量产是指使用量产工艺设备验证工程样片的低产量阶段，在全面量产之前进行，而 CXMT 历史上通常只需数周即可从风险量产过渡到大规模量产。JEDEC 的 HBM3E 规范（JESD238）要求 1024 位接口、单引脚速率 9.2–12.4 Gbps（通常为 9.6 Gbps）、单堆栈带宽约 1.2 TB/s，容量为 24 GB（8-Hi 堆叠）或 36 GB（12-Hi 堆叠）。

rss · TechPowerUp News · 8月31日 14:30

**背景**: 高带宽内存（HBM）是一种通过硅通孔（TSV）堆叠 DRAM 并以宽接口连接的存储类型，提供远超传统 DDR 内存的带宽，因此已成为 NVIDIA、AMD 等 AI GPU 和加速器的关键组件。HBM3E 是第五代 HBM 标准（HBM3 的扩展版本），目前由 SK 海力士、三星和美光主导供应。长鑫存储（CXMT）是中国领先的 DRAM 厂商，其推进到 HBM3E 风险量产标志着中国首次正式进入 AI 级内存市场，尽管美国对先进半导体设备的出口管制仍在限制中国在尖端制程上的跨越能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Risk_production_semiconductors">Risk production (semiconductors) — Grokipedia</a></li>
<li><a href="https://blogs.sw.siemens.com/semiconductor-packaging/2026/04/24/hbm3e-hbm4-ic-design-guide/">HBM3e and HBM4: IC design guide for next-generation high ...</a></li>

</ul>
</details>

**标签**: `#HBM3E`, `#semiconductors`, `#CXMT`, `#memory-technology`, `#AI-hardware`

---

<a id="item-6"></a>
## [无电机弹热制冷系统利用余热实现冷却](https://www.tomshardware.com/tech-industry/manufacturing/motorless-solid-state-cooler-uses-heat-to-cool-itself-could-recycle-processor-heat-into-cooling-shape-memory-alloy-films-could-turn-data-center-exhaust-into-refrigeration) ⭐️ 7.5/10

德国和日本的研究人员展示了一种无电机的固态弹热制冷系统，该系统利用形状记忆合金薄膜将余热转化为制冷效果。该技术有望将数据中心处理器的废热回收转化为有效的冷却能力。 通过消除压缩机和电机，该技术可以显著提升数据中心和建筑的能源效率，同时解决余热问题，在全球气温上升和计算需求激增的背景下，为可持续制冷提供了一条潜在路径。 该系统利用了弹热效应——对形状记忆合金施加机械应力会触发马氏体相变，从而吸收或释放热量。与蒸汽压缩制冷不同，它作为固态设备运行且无电机，但其可扩展性、循环寿命以及在数据中心实际环境中的性能尚未得到验证。

rss · Tom's Hardware · 8月31日 15:40

**背景**: 弹热制冷是一种新兴的固态制冷方法，基于弹热效应：即对特定合金施加机械应力（拉伸、压缩或弯曲）时，材料会从周围环境吸收热量（产生制冷）或释放热量（产生制热）。镍钛（Nitinol）等形状记忆合金经历的马氏体相变会产生这种热效应，可用于热泵应用。传统空调和制冷依赖使用制冷剂的蒸汽压缩循环，而许多制冷剂是强效温室气体，这推动了替代性固态制冷技术的研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elastocaloric_materials">Elastocaloric materials - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0140700724001117">Elastocaloric cooling: A pathway towards future cooling technology - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#elastocaloric cooling`, `#waste-heat recovery`, `#shape-memory alloys`, `#solid-state refrigeration`, `#data centers`

---

<a id="item-7"></a>
## [Unimicron 涉嫌 PCB 产地洗白遭调查](https://www.tomshardware.com/tech-industry/big-tech/key-nvidia-and-intel-supplier-raided-over-alleged-china-origin-fraud-unimicron-faces-probe-over-pcb-origin-washing-risk-of-40-percent-u-s-tariff-penalty) ⭐️ 7.5/10

台湾检方正调查 Unimicron 涉嫌将中国制造的 PCB 运回台湾后重新标注为台湾产品的行为。据报道，如果这些指控成立，该 PCB 及芯片基板供应商可能面临 40%的美国关税处罚。 有关机构仍在调查这项涉嫌违规行为，尚未公布违法结论。报道所称的 40%关税风险凸显了可核实原产地记录以及可审计生产和运输文件对 Unimicron 及其客户的重要性。

rss · Tom's Hardware · 8月31日 11:55

**背景**: PCB 是带有导电线路的薄型绝缘板，用于固定电子元件并实现电气连接。芯片基板用于半导体封装，而产地洗白则通过虚假标示商品的实际生产地来获取更有利的关税待遇。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jlcpcb.com/blog/simple-guide-to-printed-circuit-boards">PCBs Explained: A Simple Guide to Printed Circuit Boards</a></li>
<li><a href="https://pcbmake.com/substrate-semiconductor-packaging/">Substrate Semiconductor Packaging : Materials and Processes</a></li>
<li><a href="https://www.lexology.com/library/detail.aspx?g=0cbef432-1739-4a4a-9012-80c0f9722832">Side effects of the ‘tariff war’: Risks and realities of ‘origin washing’ in the ASEAN region - Lexology</a></li>

</ul>
</details>

**标签**: `#supply-chain`, `#semiconductors`, `#trade-policy`, `#nvidia`, `#intel`

---

<a id="item-8"></a>
## [长鑫存储率先量产 LPDDR6，小米手机首发搭载](https://www.tomshardware.com/pc-components/dram/chinas-cxmt-beats-western-chipmakers-to-announcement-of-lpddr6-mass-production-xiaomi-smartphones-to-debut-industrys-first-lpddr6-chips) ⭐️ 7.5/10

长鑫存储（CXMT）宣布成为首家量产 LPDDR6 内存的 DRAM 厂商，领先于三星、SK 海力士和美光。小米智能手机将成为首批搭载 LPDDR6 芯片的设备。 这一里程碑事件展现了中国在 DRAM 技术领域不断增强的竞争力，也标志着三星、SK 海力士和美光在先进内存领域的传统优势正在被削弱。同时，这代表内存行业时间表的一次显著转变——一家中国企业在下一代标准的量产上走到了前面。 CXMT 的 LPDDR6 首批应用据报道仅限于一款特定的小米设备，属于小规模首发而非广泛的行业普及。LPDDR6 引入了双子通道架构，数据总线宽度扩展至 24 位（从 LPDDR5 的 16 位提升），以改善移动设备性能与能效。

rss · Tom's Hardware · 8月31日 10:30

**背景**: 长鑫存储（CXMT）成立于 2016 年，前身为 Innotron Memory（合肥长鑫/合肥睿力集成电路制造），被广泛认为是中国唯一一家实现规模量产的本土 DRAM 制造商。LPDDR（低功耗双倍数据速率）内存专为移动和功耗受限场景打造，每一代标准均由半导体标准组织 JEDEC 制定。LPDDR6 标准（JEDEC 正式编号 JESD209-6）引入了双子通道架构，并增强了 RAS 功能，如 PRAC 和元数据支持，代表了相较 LPDDR5 的一次重大架构飞跃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.jedec.org/standards-documents/docs/jesd209-6">LPDDR6 Standard | JEDEC</a></li>
<li><a href="https://www.ofzenandcomputing.com/lpddr6/">What is LPDDR6? Complete August 2026 Guide to Next-Gen Mobile ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#LPDDR6`, `#China-tech`, `#memory`

---

<a id="item-9"></a>
## [面向芯片验证的高性价比智能体 AI 策略](https://semiwiki.com/artificial-intelligence/372524-exploiting-agentic-automation-cost-effectively-innovation-in-verification/) ⭐️ 7.0/10

来自 Cadence 的验证事业部总经理 Paul Cunningham 和前 Synopsys CTO Raúl Camposano 等行业专家，就如何在半导体验证中经济高效地部署智能体 AI 展开讨论，提出将 Claude 等强大的前沿模型与本地开源权重模型混合使用的方案，以应对高 token 带来的成本压力。 随着智能体 AI 在 EDA（电子设计自动化）工作流中的日益普及，对大型验证任务运行前沿模型的成本可能变得难以承受。来自主要 EDA 供应商的此番观点，预示着行业正转向混合 AI 架构，有望使自主验证智能体在整个半导体行业中大规模落地。 讨论强调，Claude 等前沿模型虽然能力强大，但在验证工作流常见的海量 token 调用场景下成本高昂。开源权重模型虽然不如完全开源模型那样透明，但可以部署在本地 GPU 基础设施上运行，为 EDA 团队在成本、延迟和数据隐私方面提供了不同的权衡选择。

rss · SemiWiki · 8月31日 13:00

**背景**: 智能体 AI 是指能够自主规划、调用工具并以最少人工干预完成多步骤任务的 AI 系统，正越来越多地应用于半导体验证——即在芯片流片前严格检查其设计是否符合规格的过程。Anthropic 的 Claude 等前沿模型具备顶级的推理能力，但按 token 计费，对于长时间运行、频繁调用工具的验证智能体来说成本高昂。开源权重模型（如 Meta 的 Llama 或 DeepSeek 系列）公开发布其训练后的模型参数（不同于完全开源项目还会公开训练数据和训练流程），允许企业在自有硬件上自行部署，从而降低成本并确保专有的设计数据保留在本地。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iankhan.com/insights/data/what-is-agentic-ai/">What is agentic AI ? - Ian Khan | AI Keynote Speaker for Hire</a></li>
<li><a href="https://www.fastcompany.com/91594272/what-is-the-difference-between-proprietary-open-weight-open-source-ai-llm-openai-anthropic-llama-deepseek">Which AI model is best: proprietary, open - weight , or open source ?</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#semiconductor-verification`, `#eda`, `#llm-cost-optimization`, `#open-weight-models`

---

<a id="item-10"></a>
## [长鑫存储起诉五角大楼](https://www.electronicsweekly.com/news/business/cxmt-sues-the-pentagon-2026-08/) ⭐️ 7.0/10

中国最大的 DRAM 制造商长鑫存储正就其被认定为协助中国军方的公司一事起诉美国国防部。

rss · Electronics Weekly · 8月31日 05:18

**标签**: `#semiconductors`, `#DRAM`, `#US-China relations`, `#geopolitics`, `#trade policy`

---

<a id="item-11"></a>
## [SK hynix 考虑采用 Intel Foundry 代工 HBM4E 基础芯片](https://www.techpowerup.com/352169/sk-hynix-eyes-intel-foundry-for-hbm4e-base-die-manufacturing) ⭐️ 6.5/10

据《韩国先驱报》报道，SK hynix 正在考虑将 Intel Foundry 与 TSMC 一道作为其 HBM4E 存储产品的基础芯片代工厂，从此前仅依赖 TSMC 的单一来源策略转向双源采购模式。 如果 Intel Foundry 拿下相当份额的合同，这将是对 Intel 代工能力的重要认可，也会挑战 TSMC 在先进封装相关领域的主导地位，同时重塑 AI 加速器市场的供应链格局。 HBM4E 的基础芯片可集成内存控制器和 PHY 等定制逻辑，从而释放计算芯片的面积并降低 AI 加速器的延迟；在 HBM3E 之前，SK hynix 使用自有的 10nm 级制程制造基础芯片，但客户现在要求更先进的工艺技术。

rss · TechPowerUp News · 8月31日 13:16

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，最初由三星、AMD 和 SK hynix 共同开发，可提供 TB/s 级数据带宽，是 AI 训练和推理工作负载的基石。基础芯片位于 DRAM 堆叠之下，从 HBM4 起可以承载内存控制器等定制逻辑，将原本集中在主计算芯片上的功能转移到此处。Intel Foundry（IFS）是 Intel 的外部代工服务部门，是前 CEO Pat Gelsinger 于 2021 年宣布的 IDM 2.0 战略的核心组成部分，旨在与 TSMC 在先进制程代工领域竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/foundry/overview.html">Semiconductor Manufacturing Company for the AI Era - Intel</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiengineering.com/hbm-options-increase-as-ai-demand-soars/">HBM Options Increase As AI Demand Soars</a></li>

</ul>
</details>

**标签**: `#HBM4E`, `#Intel Foundry`, `#SK hynix`, `#semiconductor manufacturing`, `#AI hardware`

---

<a id="item-12"></a>
## [AMD 在 Linux 7.3 中启动 Zen 6 桌面处理器支持](https://www.techpowerup.com/352155/amd-starts-zen-6-desktop-enablement-in-linux-7-3) ⭐️ 6.5/10

AMD 已开始在其即将推出的 Zen 6 桌面处理器（代号 Olympic Ridge）的 Linux 内核 7.3 上游支持工作，包括更新 HSMP 内核模块以加入协议版本 7（针对 Family 1Ah Model 80H），以及新增 AMD PMF 平台驱动功能，新增了用于设备指标的 ioctl 接口。 上游内核支持是 Zen 6 桌面处理器即将发布的最明确信号之一，因为 Linux 支持对于早期采用者、服务器工作负载以及开源兼容性至关重要。据报道单 CCD 核心数提升至 12 核（实现旗舰 24 核产品）表明 AMD 继续在主流桌面市场推动更高核心数量，加剧了与英特尔在高端消费市场的竞争。 据报道，Zen 6 桌面双 CCD 产品线从 12 核起步，依次覆盖 16 核和 20 核，最高端为 24 核旗舰型号。单 CCD 核心数的提升得益于台积电 N2（2 纳米）制程节点，相较前几代 Zen 所使用的工艺提供了更优的晶体管密度。PMF 驱动（Platform Management Framework，平台管理框架）正是用于在现代 AMD 笔记本上根据用户环境和行为自适应调节功耗与体验的同一模块。

rss · TechPowerUp News · 8月31日 11:58

**背景**: AMD 现代锐龙处理器采用基于 chiplet（小芯片）的设计，将多个 Core Complex Die（CCD，核心复合芯片）与单独的 I/O 芯片组合在一起；每个 CCD 通常包含最多 8 个 CPU 核心及共享缓存，组合两个 CCD 即是 AMD 实现主流桌面级核心数（如 8、12 或 16 核）的方式。Host System Management Port（HSMP，主机系统管理端口）是 AMD 固件中定义的接口，通过 mailbox 寄存器让操作系统查询和控制电源、热与性能状态等系统管理功能，每代新 CPU 通常都会引入新的 HSMP 协议版本。AMD PMF（Platform Management Framework，平台管理框架）驱动是 Linux x86 平台驱动，用于帮助 AMD 系统根据用户行为和外部环境自适应调整功耗和性能，最初主要应用于笔记本平台，如今正逐步扩展到桌面端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.kernel.org/arch/x86/amd_hsmp.html">20. AMD HSMP interface — The Linux Kernel documentation</a></li>
<li><a href="https://www.kernelconfig.io/config_amd_pmf">config_amd_pmf - kernelconfig.io</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Zen 6`, `#Linux kernel`, `#hardware`, `#processors`

---

<a id="item-13"></a>
## [人类何时失去了食用昆虫的习惯？](https://www.solidot.org/story?sid=85240) ⭐️ 6.3/10

研究人员分析了最早可追溯至 3.3 万年前的 745 份牙结石样本，发现欧亚大陆北部的人类在大约 9000 年前失去了消化昆虫外骨骼主要成分——几丁质的能力，这一时间点恰好与农业的兴起相吻合。相比之下，尼安德特人的牙结石中含有大量昆虫 DNA，尤其是双翅目（苍蝇和蚊子），表明他们经常食用昆虫。 该研究提供了罕见的基因组证据，将特定基因突变与新石器时代革命期间的饮食转变联系起来，揭示了从狩猎采集到农业的过渡如何重塑了人类生理。它还支持了关于尼安德特人谋生方式的假说，包括食用带蛆动物尸体以及将猎物储存在沼泽环境中。 研究团队检测了几丁质酶基因——编码分解切丁质的酶——并在欧亚北部人群中发现了使该基因失活的突变，这一模式已持续约 9000 年。尼安德特人牙结石中蚊子的 DNA 含量尤其丰富，支持了猎物尸体有时被存放在池塘或沼泽中、蚊子在这些地方繁殖的观点。

rss · Solidot · 8月31日 08:13

**背景**: 牙结石是已知最丰富的古代生物分子来源之一，能够保存数万年的食物 DNA，从而实现详细的饮食重建。几丁质是构成昆虫外骨骼的坚韧结构多糖；以昆虫为食的动物通常会产生几丁质酶来分解它。大约 1 万年前发生的新石器时代转型——以肥沃月弯及更广泛地区采纳农业为标志——从根本上改变了人类饮食，并且正如本研究所示，在我们的基因组中留下了可检测的痕迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chitinase">Chitinase - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Calculus_(dental)">Calculus ( dental ) - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7055813/">Ancient DNA analysis of food remains in human dental calculus from...</a></li>

</ul>
</details>

**标签**: `#archaeogenomics`, `#ancient-DNA`, `#human-evolution`, `#OpenShot`, `#tech-policy`

---

<a id="item-14"></a>
## [利用 BirdNet-Go 将安防摄像头改造为自动鸟类识别系统](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 6.0/10

一篇爱好者博客文章展示了如何将现有的安防摄像头加以改造——将其 RTSP 音频流接入 BirdNet-Go——从而在自托管的树莓派上实现全天候自动识别鸟类物种。作者还将识别结果集成到 Home Assistant 仪表板中，实现实时鸟类监测。 这是一个将边缘机器学习应用于家庭自动化实际场景的典型案例，证明复杂的音频分类模型可以在无需云端依赖的情况下，在廉价硬件上本地运行。它展示了如何将现成的消费设备与开源 AI 工具以富有创意的方式组合，降低了爱好者构建自有野生动物监测系统的门槛。 BirdNet-Go 是基于康奈尔大学和开姆尼茨工业大学的 BirdNET 模型构建的自托管实时声景分析器，可在树莓派上运行。一位评论者指出了一个硬件限制：像 Aqara 门铃这类消费级摄像头仅支持 16kHz 音频采样，而 BirdNET 期望 48kHz 输入，因此需要外接 USB 麦克风才能获得可靠的分类效果。

hackernews · speckx · 8月31日 16:47 · [社区讨论](https://news.ycombinator.com/item?id=49511856)

**背景**: BirdNET 是一个开源研究项目，利用神经网络从音频录音中识别鸟类物种，其训练数据来自大规模的鸟类鸣声数据集。BirdNet-Go 将该模型封装为一个可自托管、7×24 小时运行的声景分析器，能够接入声卡输入或网络音频流。边缘机器学习（Edge ML）指的是直接在本地设备（如树莓派开发板、物联网传感器或微控制器）上运行机器学习推理，而非将数据发送至云端，这样可以降低延迟、保护隐私并避免持续的云服务费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/birdnet-go: Self-hosted realtime soundscape ...</a></li>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.geeksforgeeks.org/machine-learning/what-is-edge-machine-learning/">What is edge machine learning? - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 评论者们热情地分享了各自的实现方案，其中一位通过 RTSP 将 BirdNet-Go 接入 Unifi 门铃，并计划添加电子墨水屏来显示鸟类的'木刻'风格图像；另一位则在 RPi3A+ 上外接麦克风完成了详细部署并撰写了博客。讨论中浮现出一些实际硬件挑战——尤其是 16kHz 与 48kHz 采样率不匹配的问题，以及内置麦克风缺乏防风罩导致的风噪问题，并推荐了康奈尔大学 Merlin Bird ID 应用作为替代方案。此外，还有一个旁支话题讨论了以模仿能力著称的北方嘲鸫是否具有独特叫声。

**标签**: `#bird-identification`, `#audio-classification`, `#edge-ml`, `#raspberry-pi`, `#home-automation`

---

<a id="item-15"></a>
## [美军军营超市冷柜疑似遭远程操控](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) ⭐️ 6.0/10

发表在 Substack 通讯 "Signal and Silence" 上的一篇调查文章推测，美国军方一家军营超市（commissary）的冷柜可能遭到远程操控，引发了对军方运营技术（OT）系统安全漏洞的关注。作者并未确认是黑客行为，而只是将其作为一种可能性提出，并指出多台冷柜出现了有规律的故障。 如果情况属实，此事件将暴露军方后勤基础设施中 OT 安全的重大缺陷——冷柜一旦被入侵，可能影响食品供应，并对关岛、夏威夷等偏远基地周边的当地经济产生连锁影响。即便根本原因是配置失误或固件更新出错，这一案例也凸显了连接军方网络的遗留 ICS/PLC 系统更广泛的脆弱性。 原文将冷柜故障视为一种工作假设，而非已确认的入侵事件。社区评论者列举了 ICS 领域众所周知的弱点——例如 Siemens S7-1500 等设备使用默认的 admin/admin 凭据、过时的 GUI 框架、缺乏网络分段以及不安全的远程访问——以此说明无论此具体事件是否为恶意攻击，这类系统都长期处于风险之中。

hackernews · jcurbo · 8月31日 11:45 · [社区讨论](https://news.ycombinator.com/item?id=49508506)

**背景**: 美军军营超市（commissary）是设在军事基地内的免税杂货店，为军人及其家属提供服务。运营技术（OT）是指直接监控和控制物理过程（如工业冷柜）的硬件和软件，与处理数据的传统信息技术（IT）有所不同。工业控制系统（ICS），包括可编程逻辑控制器（PLC），是 OT 的核心组成部分，通常通过遗留网络连接，存在身份验证薄弱、软件过时、网络分段有限等问题，既容易因配置失误出现故障，也容易成为蓄意网络攻击的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.todaysmilitary.com/life-in-the-military/life-on-base/amenities">U.S. Military Base Amenities | Today’s Military</a></li>
<li><a href="https://www.ibm.com/think/topics/operational-technology">What is operational technology (OT)? - IBM</a></li>
<li><a href="https://ms.codes/en-gb/blogs/cybersecurity/common-cybersecurity-vulnerabilities-in-industrial-control-systems">Common Cybersecurity Vulnerabilities In Industrial Control Systems</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对"遭黑客入侵"的说法持怀疑态度：一位拥有 20 年军方 IT 经验的资深人士认为这更可能是配置失误或固件更新失败，但他同时对事件发生的时机表示担忧，并指出关岛、夏威夷等偏远海外基地才是此类攻击的高价值目标。其他参与者分享了关于 Siemens S7-1500 PLC 仍在使用默认凭据的真实见闻；还有一位评论者引用了 2014 年 Hank Paulson 书中的段落，描述了部署在 Fort Stewart 等地点的非电动制冷设备内置的"免费实时监控"功能。总体情绪是：该指控虽有可能但尚未证实，且无论此次事件是否为恶意攻击，遗留 OT 系统的不安全性都是一个系统性问题。

**标签**: `#cybersecurity`, `#industrial-control-systems`, `#military-logistics`, `#OT-security`, `#incident-analysis`

---

<a id="item-16"></a>
## [ChatGPT 智能体工具与技能参考指南](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 6.0/10

Simon Willison 发布了一份参考指南，记录了 ChatGPT 智能体能力中可用的工具和技能，其中包括 control-browser 技能如何通过 ChatGPT 的 Node.js REPL 启动 Playwright 实例，以编程方式获取浏览器自动化文档。 这份参考资料帮助开发者和高级用户了解 ChatGPT 智能体模式下确切可用的能力，揭示了浏览器自动化、代码执行等技能的实际工作原理——这些信息通常隐藏在模型的系统提示中，外界无从知晓。 control-browser 技能指示 ChatGPT 调用 nodeRepl.write(await browser.documentation())，该方法会返回使用浏览器的完整文本说明。Playwright 是微软开发的 token 高效型浏览器自动化框架，避免将大型工具架构和无障碍树加载到模型上下文中，因而非常适合编码智能体使用。

hackernews · ijidak · 8月31日 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49510000)

**背景**: ChatGPT 的智能体能力面向付费订阅用户开放，允许模型在网站上执行多步骤任务并与外部工具交互。OpenAI Codex 最初于 2021 年作为针对代码微调的 GPT-3 变体发布，现已发展为支持多种工具的更广泛的编码智能体平台。Playwright 由微软团队创建（前身为谷歌 Puppeteer 团队），因相比 MCP 等替代方案具有更高的 token 效率，现已被 Claude Code 和 GitHub Copilot 等 AI 编码智能体广泛用于浏览器自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps | Playwright</a></li>
<li><a href="https://github.com/microsoft/playwright">GitHub - microsoft/ playwright : Playwright is a framework for Web...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 重点介绍了 control-browser 技能，并链接到一条解释创建提示的背景评论。用户 satvikpendem 质疑如果两者提供相同功能，这与 OpenAI 的 Codex 产品有何区别。darepublic 对这些工作工具造成的 token 消耗和速度减慢提出了实际担忧。用户 enraged_camel 发表了一个偏离主题的观察，指出 AI 生成的网站呈现出统一的视觉风格，让人联想到 Bootstrap 时代。

**标签**: `#chatgpt`, `#codex`, `#agentic-ai`, `#playwright`, `#developer-tools`

---

<a id="item-17"></a>
## [先进冷却技术应对汽车散热挑战](https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/) ⭐️ 6.0/10

EE Times 报道了正在涌现的先进冷却技术，这些技术旨在应对现代汽车中电驱动系统、AI 处理器和自动驾驶系统所产生的日益增长的热流密度。 随着车辆集成更强大的 AI 芯片和电气化动力总成，传统风冷已越来越不够用，热管理正成为影响汽车性能、安全性和可靠性的关键瓶颈。 文章指出行业正朝着液冷和两相浸没式冷却方向发展，这些技术已在数据中心得到验证，目前正被改造用于高密度汽车电子设备和功率模块。

rss · EE Times · 8月31日 07:46

**背景**: 现代电动汽车从多个子系统产生大量热量，包括电池、电动机、功率电子设备，以及越来越多地来自用于自动驾驶和 ADAS 的车载 AI 处理器。传统风冷难以应对如此高的热流密度，促使汽车行业采用液冷、热泵系统和集成式热管理方案。两相浸没式冷却（液体沸腾以吸收大量热量）正被探索用作下一代功率电子和高性能汽车处理器的更高效替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eetimes.com/advanced-cooling-technologies-address-the-automotive-heat-challenge/">Advanced Cooling Technologies Tackle Automotive Heat - EE Times</a></li>
<li><a href="https://www.heatsinksmfg.com/automotive-ai-liquid-cooling.html">Automotive AI & Liquid Cooling: The Future of Smart Vehicle ...</a></li>
<li><a href="https://docs.nlr.gov/docs/fy23osti/83645.pdf">Automotive Power Electronics Cooling Technology Research at NREL</a></li>

</ul>
</details>

**标签**: `#automotive`, `#thermal-management`, `#electric-vehicles`, `#AI-hardware`, `#cooling-technologies`

---

<a id="item-18"></a>
## [中国芯片公司上半年业绩亮眼](https://www.electronicsweekly.com/news/business/a-solid-h1-for-china-chips-2026-08/) ⭐️ 6.0/10

根据中国国家发展[改革委]的数据，截至上周四已公布第二季度业绩的中国芯片公司，上半年营收同比增长 12.8%，利润惊人地增长了 99%。 这一强劲的财务表现突显了中国国内半导体行业日益加速的增长势头。在美国持续实施出口管制以及中国大力推动芯片技术自主的背景下，该行业具有重要的战略意义。 99%的利润飙升尤为引人注目，远远超过 12.8%的营收增长，表明利润率大幅扩张。这些数据基于截至截止日期已公布第二季度业绩的公司，由中国国家发展部门汇总编制。

rss · Electronics Weekly · 8月31日 05:15

**背景**: 中国半导体行业一直是中美科技竞争的焦点，美国已陆续实施多轮出口管制，针对先进芯片制造设备和 AI 芯片。作为回应，中国投入大量国家资金建设涵盖设计、制造和设备的国内半导体能力。国家发展和改革委员会（NDRC）是负责中国经济规划和产业政策的关键政府机构，其数据发布是行业健康状况的重要信号。

**标签**: `#semiconductors`, `#China`, `#industry-news`, `#financial-report`, `#chip-market`

---

<a id="item-19"></a>
## [Steam Deck 已认证与可玩游戏突破 30,000 款](https://www.techpowerup.com/352197/steam-tops-30-000-steam-deck-playable-and-verified-games) ⭐️ 5.5/10

根据 SteamDB 的数据，Steam 上官方标记为 Steam Deck 或 SteamOS「已认证（Verified）」或「可玩（Playable）」的游戏数量已达到 30,023 款；ProtonDB 的统计略低，为 29,988 款。 这一里程碑彰显了 Valve 的 Proton 兼容层以及 Steam Deck 的成功，将 Linux 从小众游戏平台转变为可行的主流选择，也促使发行商更有动力原生支持 Linux。 ProtonDB 的指标显示，按同时在线玩家数排名的 Steam 当前 Top 10 游戏中，有 40% 获得了「已认证」或「可玩」标签；Top 100 中这一比例上升至 46%，说明即使是头部大作也越来越兼容这款掌机。

rss · TechPowerUp News · 8月31日 22:57

**背景**: Steam Deck 是 Valve 推出的掌上游玩 PC，搭载基于 Linux 的 SteamOS 操作系统。由于绝大多数 PC 游戏都是为 Windows 开发的，Valve 开发了 Proton——一个基于开源 Wine 项目的兼容层，用于将 Windows 游戏的调用转换为 Linux 可执行的内容。Steam Deck 上的游戏会获得 Valve 颁发的两类兼容性徽章之一：「已认证（Verified）」意味着游戏经过完整测试，开箱即用且手柄与显示适配良好；「可玩（Playable）」则意味着游戏可能需要用户进行一些手动调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proton_(software)">Proton (software) - Wikipedia</a></li>
<li><a href="https://www.hlplanet.com/verified-vs-playable-steam-deck/">Verified vs Playable Game Status for Steam Deck</a></li>

</ul>
</details>

**标签**: `#Steam Deck`, `#Linux Gaming`, `#Valve`, `#Proton`, `#Gaming Industry`

---

<a id="item-20"></a>
## [改装者打造经济实惠的开源霍尔效应分体人体工学键盘](https://www.techpowerup.com/352195/modder-creates-affordable-open-source-hall-effect-split-ergonomic-keyboard) ⭐️ 5.5/10

一位开源改装者打造了 Silakka54 HE 键盘的霍尔效应开关版本，这是热门分体人体工学键盘的经济实惠之选，为玩家提供了除昂贵替代品之外的第三种选择。

rss · TechPowerUp News · 8月31日 22:40

**标签**: `#hardware`, `#open-source`, `#mechanical-keyboards`, `#ergonomics`, `#hall-effect`

---