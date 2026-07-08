---
layout: default
title: "Horizon Summary: 2026-07-08 (ZH)"
date: 2026-07-08
lang: zh
---

> 从 95 条内容中筛选出 20 条重要资讯。

---

1. [GitLost 漏洞：通过提示注入利用 GitHub AI 代理泄露私有仓库](#item-1) ⭐️ 8.0/10
2. [三星开始量产 PM1763 PCIe Gen 6 企业级固态硬盘](#item-2) ⭐️ 7.5/10
3. [JEDEC 发布 SPHBM4 标准以降低 AI 内存成本](#item-3) ⭐️ 7.5/10
4. [英伟达将 Vera CPU 的单线程性能作为其代理式 AI 优势进行宣传，披露下一代 "Rigel" Arm CPU 核心——将该芯片定位为"大规模下的最强单线程 CPU"，而非并行怪兽](#item-4) ⭐️ 7.5/10
5. [韩国 8800 亿美元芯片与 AI 计划面临电力和水资源挑战](#item-5) ⭐️ 7.5/10
6. [腾达固件（多个版本）含有隐藏的身份验证后门](#item-6) ⭐️ 7.0/10
7. [计算机程序的构造与解释视频讲座（1986）](#item-7) ⭐️ 7.0/10
8. [封装 PDK：共封装光学的缺失环节](#item-8) ⭐️ 7.0/10
9. [SambaNova 融资 10 亿美元，摩根大通成客户](#item-9) ⭐️ 7.0/10
10. [苹果向博通承诺超 300 亿美元采购美国本土芯片](#item-10) ⭐️ 6.5/10
11. [Xbox 裁员重创 Id Software 和 Obsidian 工作室](#item-11) ⭐️ 6.5/10
12. [SiPearl Rhea1 处理器进入实验室，欧洲首款主权 HPC 芯片问世](#item-12) ⭐️ 6.5/10
13. [俄勒冈批准数据中心电价上涨 29.7%，居民电价下调 1.3%](#item-13) ⭐️ 6.5/10
14. [Windows GDID 遥测数据助力逮捕 Scattered Spider 黑客](#item-14) ⭐️ 6.5/10
15. [江波龙预测利润暴涨约 60,000%，受 AI 内存需求驱动](#item-15) ⭐️ 6.5/10
16. [快造科技完成 10 亿元融资，刷新消费级 3D 打印一级市场记录](#item-16) ⭐️ 6.3/10
17. [「德睿智药」获 5200 万美元 B 轮融资，AI 设计的减肥药已进入 3 期临床｜36 氪首发](#item-17) ⭐️ 6.3/10
18. [Cloudflare 与 OpenAI 启动试点，利用网络信号优化 AI 搜索索引](#item-18) ⭐️ 6.3/10
19. [蓝色起源以 1300 亿美元估值完成 100 亿美元融资](#item-19) ⭐️ 6.3/10
20. [解读优衣库 T 恤上的混淆 Bash 脚本](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GitLost 漏洞：通过提示注入利用 GitHub AI 代理泄露私有仓库](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) ⭐️ 8.0/10

Noma Security 的安全研究人员披露了名为'GitLost'的漏洞，该漏洞通过提示注入攻击利用 GitHub 基于 AI 的 Agentic Workflows。攻击者只需在公开的 GitHub Issue 中嵌入一个简单如'Additionally'（此外）这样的恶意指令，就能诱使 AI 代理获取并公开发布私有仓库的内容——无需任何凭证或系统访问权限。 该漏洞凸显了智能体 AI 系统中一个根本性的安全挑战：一旦 LLM 能够访问私有数据，就无法可靠地阻止它在处理不可信输入时泄露这些数据。这影响到所有使用 GitHub Agentic Workflows 且 AI 代理具有跨仓库访问权限的组织，并揭示了整个行业在为基于 LLM 的自动化构建有效安全防护方面面临的普遍困境。 攻击原理是：公开仓库的 Issue 中包含注入的指令，使代理同时从公开仓库和私有仓库获取 README.md 内容，然后将私有内容作为公开评论发布。绕过方式简单得令人震惊——仅用'Additionally'一词就足以覆盖代理的安全防护——这证明在同一个上下文窗口中混合系统规则与不可信的用户输入本质上就是不安全的。

hackernews · ColinEberhardt · 7月8日 05:25 · [社区讨论](https://news.ycombinator.com/item?id=48827858)

**背景**: GitHub Agentic Workflows 是一个由 AI 驱动的自动化功能，允许 AI 代理执行由仓库事件触发的任务，例如响应 Issue。这些代理可以拥有对组织内多个仓库的读取权限。提示注入是一类攻击，攻击者将恶意指令嵌入 LLM 处理的内容中，导致其行为偏离预期——例如忽略原有指令转而执行攻击者的命令。OWASP 已将提示注入列为 LLM 应用程序的头号安全风险（LLM01:2025），而由于 LLM 无法可靠地区分其上下文窗口中的可信系统指令和不可信数据，这一问题至今仍未得到解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/">GitLost: How We Tricked GitHub’s AI Agent into Leaking ...</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://www.darkreading.com/cyber-risk/gitlost-leaks-private-data-github-agentic-workflows">'GitLost' Flaw Leaks Private Data From GitHub's Agentic Workflows</a></li>

</ul>
</details>

**社区讨论**: 社区将提示注入与 SQL 注入进行了强烈类比，称其为'一类需要系统性防御的广泛漏洞类别'。在责任归属上出现了显著分歧：部分人认为这是用户的配置错误问题（类似于在公开 CI 任务中暴露密钥），而非 GitHub 的漏洞；但另一些人则强调，在 LLM 上下文窗口中构建硬性安全边界从根本上是不可能的，因为模型天生会遵循最新或最持久的指令。社区还对企业在产品上仓促添加 AI 功能而未能充分考虑安全性的做法提出了更广泛的批评。

**标签**: `#security`, `#prompt-injection`, `#github`, `#ai-agents`, `#llm-vulnerabilities`

---

<a id="item-2"></a>
## [三星开始量产 PM1763 PCIe Gen 6 企业级固态硬盘](https://www.techpowerup.com/350600/samsung-begins-mass-production-of-pm1763-pcie-gen-6-ssd) ⭐️ 7.5/10

三星电子宣布开始量产 PM1763，这是一款基于 PCIe 6.0 的企业级固态硬盘（eSSD），专为下一代 AI 和高性能计算（HPC）服务器环境设计。该硬盘具备高速数据传输能力和经过优化的控制器架构，并已完成面向下一代 AI 平台的验证。 作为首批进入量产阶段的 PCIe Gen 6.0 企业级固态硬盘之一，PM1763 标志着支撑 AI 训练与推理工作负载的存储基础设施取得了重要里程碑，因为数据吞吐量正成为关键瓶颈。这使三星在存储行业向 PCIe 6.0 过渡的进程中处于领先地位，而 PCIe 6.0 正是为应对大型 AI 模型和分布式训练集群的海量数据搬运需求而设计的。 PM1763 采用 PCIe 6.0 标准，该标准使用 PAM4 信号调制和 FLIT 编码，实现每通道 64 GT/s 的传输速率，是 PCIe 5.0 单通道带宽的两倍。三星尚未公开发布具体的容量规格、外形尺寸或顺序读写速度数据，不过该硬盘定位为配备专为 AI 工作负载调优的控制器架构的 NVMe 企业级固态硬盘。

rss · TechPowerUp News · 7月8日 08:09

**背景**: PCIe（外围组件互连高速总线）是由 PCI-SIG 联盟维护的高速串行计算机扩展总线标准，用于将固态硬盘、GPU 和网卡等组件连接到系统 CPU。每一代新标准大约将单通道带宽翻倍，PCIe 6.0 作为最新的主要迭代版本，是专门为支持 AI 训练和推理等计算密集型应用而设计的。高性能计算（HPC）指的是通过聚合尖端计算能力来解决标准商用系统无法应对的复杂问题，如今越来越多地涵盖大规模 AI 模型训练。企业级固态硬盘（eSSD）是面向数据中心和服务器部署的存储设备，强调高耐用性、可靠性和持续吞吐量，而非消费级硬盘通常关注的成本优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.viavisolutions.com/en-us/resources/learning-center/what-pcie-60">The PCIe 6.0 Guide. Speed, Features and More</a></li>
<li><a href="https://www.ibm.com/think/topics/hpc">What Is High-Performance Computing (HPC)? | IBM</a></li>
<li><a href="https://www.onlogic.com/blog/your-ultimate-guide-to-understanding-pcie-6-0/">Your Ultimate Guide to Understanding PCIe 6.0 | OnLogic</a></li>

</ul>
</details>

**标签**: `#PCIe Gen 6`, `#Samsung`, `#enterprise SSD`, `#AI infrastructure`, `#storage hardware`

---

<a id="item-3"></a>
## [JEDEC 发布 SPHBM4 标准以降低 AI 内存成本](https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates) ⭐️ 7.5/10

JEDEC 于 2025 年 12 月 11 日宣布了 SPHBM4（标准封装高带宽内存 4）标准，该标准采用 512 位窄接口，搭载在标准有机基板上即可实现 HBM4 级别的吞吐量，无需使用昂贵的硅中介层和 CoWoS 类 2.5D 封装。 该标准通过可能降低 HBM 封装成本并减少对台积电 CoWoS 产能的依赖，直接缓解了 AI 内存瓶颈，而 CoWoS 产能一直是 NVIDIA GPU 等 AI 加速器的关键供应制约。更便宜、更易获取的 HBM4 级内存有望降低 AI 基础设施的总成本，并将市场拓展至高端加速器以外的领域。 SPHBM4 使用与传统 HBM4 相同的 DRAM 芯片，但搭配了重新设计的接口基座芯片，可实现 512 位宽连接，从而允许使用标准有机基板替代硅中介层。据 JEDEC 称，该规范仍在制定中，实际产品与采用时间表尚未明确。

rss · Tom's Hardware · 7月8日 15:03

**背景**: HBM（高带宽内存）是与 AI 加速器和 GPU 配套使用的堆叠 DRAM，用于以极高速率向其传输数据。当前的 HBM4 实现依赖于硅中介层——包含硅通孔（TSV）的薄硅层，用于在 GPU 芯片和 HBM 堆栈之间路由数千条信号。台积电的 CoWoS（Chip-on-Wafer-on-Substrate，芯片在晶圆上再置于基板）是此应用的主流 2.5D 封装技术，但其产能有限且成本高昂，已成为 AI 芯片供应中众所周知的瓶颈。有机基板由 ABF（味之素堆积膜）等材料制成，成本远低于硅中介层且供应更充足，但传统上无法支持 HBM 所需的高密度高速连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jedec.org/news/pressreleases/jedec®-prepares-sphbm4-standard-deliver-hbm4-level-throughput-reduced-pin-count">JEDEC® Prepares SPHBM4 Standard to Deliver HBM4-Level Throughput with Reduced Pin Count | JEDEC</a></li>
<li><a href="https://wccftech.com/jedec-approves-sphbm4-to-break-hbm-costs-retain-hbm4-speeds-standard-packages/">JEDEC Approves SPHBM4 to Break HBM's Costly Packaging Bottleneck, Retaining HBM4-level Speeds With Standard Packages</a></li>
<li><a href="https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm">CoWoS® - Taiwan Semiconductor Manufacturing Company Limited</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#memory standards`, `#HBM4`, `#JEDEC`, `#semiconductor manufacturing`

---

<a id="item-4"></a>
## [英伟达将 Vera CPU 的单线程性能作为其代理式 AI 优势进行宣传，披露下一代 "Rigel" Arm CPU 核心——将该芯片定位为"大规模下的最强单线程 CPU"，而非并行怪兽](https://www.tomshardware.com/pc-components/cpus/nvidia-touts-vera-cpus-single-threaded-performance-as-its-agentic-ai-advantage-frames-chip-as-a-max-single-threaded-cpu-at-scale-not-a-parallel-monster) ⭐️ 7.5/10

英伟达披露了其 Vera CPU 的细节，该 CPU 采用下一代 "Rigel" Arm 核心，声称在代理式 AI 工作负载中相比 x86 竞争对手具有 1.8 倍的单线程性能优势。

rss · Tom's Hardware · 7月8日 11:00

**标签**: `#Nvidia`, `#Vera CPU`, `#Arm architecture`, `#agentic AI`, `#data center hardware`

---

<a id="item-5"></a>
## [韩国 8800 亿美元芯片与 AI 计划面临电力和水资源挑战](https://www.tomshardware.com/tech-industry/power-and-water-lag-the-fabs-in-south-koreas-880-billion-chip-and-ai-plan) ⭐️ 7.5/10

韩国总额达 1,350 万亿韩元（约 8,800 亿美元）的计划——包含 5,200 亿美元的半导体项目以及 AI 数据中心和机器人投资——正面临严重的电力和水资源瓶颈，据估计单个 AI 超级集群的电力需求高达首尔全市总用电量的四分之一。 这表明仅靠资本投入不足以主导 AI 基础设施，电力网络和水资源等物理限制可能才是全球半导体和 AI 竞赛中真正的瓶颈，从而削弱韩国相对于美国、中国和台湾地区的竞争力。 1,350 万亿韩元的总额主要由企业资本支出构成，而非政府直接拨款；AI 超级集群因采用液冷系统和训练模型的高能耗，所需的电力、冷却和水量远超传统数据中心。

rss · Tom's Hardware · 7月7日 17:27

**背景**: AI 超级集群是专为训练和运行 AI 模型而设计的大规模数据中心设施，需要大量的电力、冷却、网络和物理空间。单个数据中心的用水量包括现场用水、为其供电的发电厂用水以及间接水源。国际能源署预测，到 2030 年全球数据中心用电量将大致翻倍至约 945 太瓦时，占全球总用电量的近 3%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai">Energy demand from AI – Energy and AI – Analysis - IEA</a></li>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_data_center">AI data center - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#AI infrastructure`, `#South Korea`, `#power-grid`, `#industry-policy`

---

<a id="item-6"></a>
## [腾达固件（多个版本）含有隐藏的身份验证后门](https://kb.cert.org/vuls/id/213560) ⭐️ 7.0/10

CERT.org 披露的信息显示，多个版本的腾达路由器固件中存在硬编码的身份验证后门，攻击者可以使用任意用户名和一个隐藏密码进行访问。

hackernews · miniBill · 7月8日 00:08 · [社区讨论](https://news.ycombinator.com/item?id=48825749)

**标签**: `#security`, `#vulnerability`, `#iot`, `#networking`, `#backdoor`

---

<a id="item-7"></a>
## [计算机程序的构造与解释视频讲座（1986）](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) ⭐️ 7.0/10

麻省理工学院 1986 年经典的 SICP 视频讲座，由 Sussman 和 Abelson 主讲，是一门通过 Scheme/Lisp 讲解基本编程概念的计算机科学基础课程。

hackernews · gjvc · 7月7日 23:57 · [社区讨论](https://news.ycombinator.com/item?id=48825664)

**标签**: `#SICP`, `#computer-science`, `#lisp`, `#education`, `#classic-lectures`

---

<a id="item-8"></a>
## [封装 PDK：共封装光学的缺失环节](https://semiwiki.com/3dic/370709-the-packaging-pdk-is-the-missing-layer-for-co-packaged-optics/) ⭐️ 7.0/10

SemiWiki 的一篇评论文章指出，共封装光学（CPO）行业不能仅靠光子器件性能的提升来实现规模化，亟需一套标准化的封装工艺设计套件（Packaging PDK），以打通光子器件设计与电光实现之间的鸿沟。 随着 AI 基础设施对带宽、功耗、延迟和传输距离的要求不断攀升，光学器件必须更靠近计算引擎。如果没有统一的封装 PDK，CPO 从设计到制造的流程将在晶圆厂、封测代工厂（OSAT）和光子 EDA 工具链之间碎片化，拖慢超大规模数据中心所需的部署速度。 传统晶圆厂 PDK 用于描述晶圆制造工艺，使设计师能验证可制造性；类比之下，封装 PDK 将对先进封装的组装、互连和电光集成规则进行建模。文章将 CPO 定位为一项由封装驱动的技术，而非单纯的光子器件问题，意味着决定其商用可行性的将是 3DIC 及先进封装工具链，而不仅是硅光子技术本身。

rss · SemiWiki · 7月7日 17:00

**背景**: 共封装光学（CPO）将光学收发器直接集成到与交换机 ASIC 或计算芯片相同的封装中，用以取代可插拔模块，从而大幅降低功耗并提升 AI 数据中心的带宽。工艺设计套件（PDK）是晶圆厂提供的一套标准文件和模型，使芯片设计师能够确保其版图在特定工艺节点下可制造。封装 PDK 和封装装配设计套件（Package Assembly Design Kit）将这一概念扩展到封装层面，覆盖芯片间互连、凸点布局和装配规则——这对于 3DIC 及 2.5D/3D 异构集成尤为关键。该文章的核心论点是：CPO 生态虽然在光子元件 PDK 方面已较为成熟，但缺少一套等价的标准化套件来描述共封装本身的电气、热和机械规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.corning.com/oem-solutions/worldwide/en/home/products-solutions/optical-communication-components/co-packaged-optics.html">What is Co-Packaged Optics (CPO) Technology? | Corning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Process_Design_Kit">Process design kit - Wikipedia</a></li>
<li><a href="https://www.semiconductorpackagingnews.com/uploads/2/2025_SPN_White_Paper_-_Package_Assembly_Design_Kits-The_Future_of_Advanced_Package_Design.pdf">Package Assembly Design Kits: The Future of Advanced Package ...</a></li>

</ul>
</details>

**社区讨论**: 源材料中没有提供社区评论。

**标签**: `#co-packaged optics`, `#advanced packaging`, `#3DIC`, `#semiconductor`, `#AI infrastructure`

---

<a id="item-9"></a>
## [SambaNova 融资 10 亿美元，摩根大通成客户](https://www.eetimes.com/sambanova-raises-1-billion-signs-jpmorganchase-as-a-customer/) ⭐️ 7.0/10

AI 芯片初创公司 SambaNova 在由 General Atlantic 领投的 F 轮首轮融资中筹集了 10 亿美元，估值达到 110 亿美元，并签署摩根大通（JPMorganChase）作为重要企业客户。 这笔融资和企业客户的获得标志着主要金融机构开始采用 NVIDIA 以外的 AI 芯片替代方案，验证了 SambaNova 在竞争激烈的 AI 硬件市场中的地位，也表明企业级 AI 芯片市场正在走向成熟。 本轮融资由 General Atlantic 领投，预计还将有更多投资者加入；SambaNova 的技术基于其专有的可重构数据流单元（RDU）架构，其最新的第五代 SN50 RDU 专为大规模智能体（agentic）AI 推理工作负载而设计。

rss · EE Times · 7月8日 07:45

**背景**: SambaNova Systems 是一家 AI 硬件公司，通过提供专用于 AI 推理和训练的芯片与 NVIDIA 竞争。其核心技术是可重构数据流单元（RDU），采用由高速片上交换网络互连的可重构处理和存储单元阵列，这与 NVIDIA 基于 GPU 的方案有根本性差异。该公司已历经多代芯片迭代，从 SN40L 发展到现在的 SN50 RDU，瞄准大规模智能体 AI 工作负载。本轮融资使 SambaNova 成为资金最雄厚的、挑战 NVIDIA 在数据中心 AI 加速器市场主导地位的 AI 芯片初创公司之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/">AI chip maker SambaNova raises $1B at $11B valuation, 5 ...</a></li>
<li><a href="https://sambanova.ai/products/rdu-ai-chips">RDU | Next-Gen AI Chip for Inference at Scale</a></li>
<li><a href="https://www.cnbc.com/2026/07/08/sambanova-ai-chip-funding-valuation.html">SambaNova valued at $11 billion after AI chip funding - CNBC</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#funding`, `#SambaNova`, `#enterprise AI`, `#JPMorganChase`

---

<a id="item-10"></a>
## [苹果向博通承诺超 300 亿美元采购美国本土芯片](https://www.techpowerup.com/350606/apple-to-increase-spend-with-broadcom-to-produce-billions-more-u-s-chips) ⭐️ 6.5/10

苹果宣布与博通达成新的多年期合作承诺，总金额超过 300 亿美元，用于设计和生产定制硅基组件及先进的无线连接技术，预计将生产超过 150 亿颗美国本土制造的芯片，并支持数百个美国就业岗位。 这是苹果在美国制造计划（AMP）框架下达成的最大一笔承诺，标志着美国半导体供应链回迁本土的重大进展，与减少对海外芯片制造依赖的更广泛地缘政治努力相一致。 博通将投入 15 亿美元资本支出，用于扩建和现代化其位于科罗拉多州柯林斯堡的制造工厂，在该工厂生产先进的射频组件，如 FBAR（薄膜体声波谐振器）滤波器以及用于苹果产品的先进无线连接技术。

rss · TechPowerUp News · 7月8日 10:32

**背景**: 苹果的美国制造计划（AMP）于 2025 年启动，是苹果向美国制造业承诺的 6000 亿美元四年计划的一部分，最初的合作伙伴包括康宁、Coherent、德州仪器、三星和格罗方德。博通是 AMP 的关键合作伙伴，专注于射频组件。FBAR 滤波器是一种体声波（BAW）滤波器，与传统的声表面波（SAW）滤波器相比具有更优越的性能，阻带特性更陡峭，插入损耗更低（减少 0.3 至 0.5 dB），电流消耗可降低多达 50mA——这使其成为移动设备射频前端模块的关键元件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2025/08/apple-increases-us-commitment-to-600-billion-usd-announces-ambitious-program/">Apple increases U.S. commitment to $600 billion, announces ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thin-film_bulk_acoustic_resonator">Thin-film bulk acoustic resonator - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/03/26/apple-american-manufacturing-program-trump.html">Apple expands American manufacturing program with four new ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Apple`, `#Broadcom`, `#manufacturing`, `#supply-chain`

---

<a id="item-11"></a>
## [Xbox 裁员重创 Id Software 和 Obsidian 工作室](https://www.techpowerup.com/350587/xbox-layoffs-decimate-id-software-and-obsidian) ⭐️ 6.5/10

微软 Xbox 的大规模裁员对 Id Software（约 50%员工）和 Obsidian Entertainment（约 25%员工，60 至 70 人）造成了重大影响，引发了人们对其进行中项目工作量重新分配的担忧。

rss · TechPowerUp News · 7月7日 19:42

**标签**: `#gaming-industry`, `#layoffs`, `#microsoft`, `#xbox`, `#id-software`, `#obsidian`

---

<a id="item-12"></a>
## [SiPearl Rhea1 处理器进入实验室，欧洲首款主权 HPC 芯片问世](https://www.tomshardware.com/pc-components/cpus/sipearls-long-awaited-rhea-cpu-finally-gets-in-the-lab-opening-the-door-for-europes-first-sovereign-hpc-cpu-availability-of-rhea1-is-scheduled-for-end-of-2026-sipearl-vp-says-following-long-development-process) ⭐️ 6.5/10

SiPearl 期待已久的 Rhea1 处理器——欧洲处理器计划（EPI）下开发的首款主权高性能处理器——已进入实验室阶段，SiPearl 副总裁表示正式供货计划于 2026 年底进行。 Rhea1 是欧洲推动高性能计算技术主权进程中的重要里程碑，旨在减少欧洲超级计算基础设施对美国和亚洲芯片厂商（如 Intel、AMD 和 Nvidia）的依赖。 Rhea1 旨在为 HPC 和 AI 工作负载提供高能效的计算能力，未来版本将增加核心数量和内存带宽，并加入针对欧洲百亿亿次超级计算机定制的高加速模块和 IP 模块。

rss · Tom's Hardware · 7月8日 14:44

**背景**: 欧洲处理器计划（EPI）是一个由联盟支持的项目，致力于为欧洲超级计算机开发本土 CPU 架构，资金来源于 EuroHPC 联合体——一个汇集欧盟、成员国和私人资源的公私合作伙伴关系。SiPearl 为实现设计商业化而成立，Rhea1 是其首款产品。该项目的战略意义在于欧洲希望掌控自己的计算供应链，而不是在敏感的科学、国防和研究工作负载上依赖外国处理器。EuroHPC 也在探索开源 RISC-V 架构作为实现技术主权的并行路径，这可能会影响未来欧洲 CPU 的设计方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sipearl.com/rhea1">Rhea1 first-generation CPU for HPC and AI - SiPearl</a></li>
<li><a href="https://www.techpowerup.com/338824/european-hpc-processor-rhea1-tapes-out-launch-delayed-to-2026">European HPC Processor "Rhea1" Tapes Out, Launch Delayed to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_High-Performance_Computing_Joint_Undertaking">European High-Performance Computing Joint Undertaking</a></li>

</ul>
</details>

**标签**: `#HPC`, `#European tech sovereignty`, `#SiPearl`, `#CPU architecture`, `#semiconductors`

---

<a id="item-13"></a>
## [俄勒冈批准数据中心电价上涨 29.7%，居民电价下调 1.3%](https://www.tomshardware.com/tech-industry/data-centers/power-company-hikes-data-center-bills-by-30-percent-cuts-residential-electricity-costs-by-1-3-percent-oregon-approves-change-through-power-act-pushes-developments-using-more-than-20-megawatts-of-power-to-pay-their-fair-share) ⭐️ 6.5/10

俄勒冈州公用事业委员会一致批准了波特兰通用电气公司（PGE）对用电量达 20 兆瓦及以上大型用户的 29.7%电价上调方案，该方案依据该州《电力法案》（POWER Act）针对数据中心实施。新费率于 2026 年 7 月 7 日批准后的下个星期三生效，与此同时居民电价将下调 1.3%。 这标志着政策上的重大转变——承认数据中心巨大的能源消耗，推动它们承担更公平的电网基础设施成本，而不再由居民用户交叉补贴。随着 AI 基础设施电力需求持续飙升，这一先例可能影响数据中心选址决策，并为面临类似矛盾的其他美国各州塑造能源政策。 《电力法案》于 2025 年通过，要求数据中心签订为期 10 年的合同来抵消其对电网的大量使用。PGE 是俄勒冈州最大的电力供应商，服务于该州近三分之二的商业和工业活动，其服务区域包括 Hillsboro，那里有 QTS 等主要运营商的大型设施。

rss · Tom's Hardware · 7月8日 13:56

**背景**: 《电力法案》是俄勒冈州的一项州法律，为数据中心设立了独立的电价类别，并要求它们签订为期 10 年的合同以抵消其对电网的影响。波特兰通用电气公司（PGE）是一家总部位于俄勒冈州波特兰的《财富》1000 强上市能源公司。20 兆瓦的门槛直接针对大规模运营——作为参考，一个典型的超大规模数据中心可能消耗 50 到超过 500 兆瓦的电力，因此该门槛直接打击了在该地区运营的 AI 计算基础设施和云服务提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.opb.org/article/2026/07/07/oregon-data-center-general-electric-rate-hikes/">Oregon approves PGE’s 29.7% rate hike for data centers under ...</a></li>
<li><a href="https://www.centraloregondaily.com/news/regional/oregon-hikes-data-center-electric-rates-29-in-pge-territory/article_1e7127d2-4c17-5159-9cb4-02639129ca95.html">Oregon hikes data center electric rates 29% in PGE territory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Portland_General_Electric">Portland General Electric - Wikipedia</a></li>

</ul>
</details>

**标签**: `#data-centers`, `#energy-policy`, `#infrastructure`, `#AI-economics`, `#power-consumption`

---

<a id="item-14"></a>
## [Windows GDID 遥测数据助力逮捕 Scattered Spider 黑客](https://www.tomshardware.com/tech-industry/cyber-security/arrest-and-extradition-of-scattered-spider-hacker-shines-light-on-how-windows-telemetry-gdids-can-identify-users-microsoft-device-identifier-is-just-one-digital-fingerprint-in-a-software-world-rife-with-them) ⭐️ 6.5/10

Scattered Spider 黑客组织成员 Peter Stokes 被逮捕并引渡，调查人员通过将微软 Windows 遥测数据中的 GDID（全局设备标识符）与 IP 地址、代理使用记录及服务访问日志相关联，最终在网上锁定其身份。尽管 Stokes 不断更换 IP、使用 VPN 和远程桌面连接来隐藏行踪，但与其 Windows 安装绑定的持久 GDID 始终保持不变，成为将其与攻击行为关联的关键线索。 此案表明，即便采用 VPN 和不断更换 IP 等持续性的操作安全措施，也可能被主流操作系统内置的遥测标识符所攻破。这引发了关于现代软件中设备指纹采集范围的重要隐私问题——此类标识符既可被执法部门利用，也存在被恶意行为者滥用的风险。 GDID 是嵌入在每台 Windows 安装中的唯一代码，微软将其用于诊断遥测、崩溃报告、功能使用分析和许可证验证；只有重新安装 Windows 才会生成新的 GDID。设备指纹技术更广泛地采集从屏幕分辨率到时区等数十种信号来生成持久标识符，即使清除浏览器数据后仍然有效，因此 GDID 只是当前广泛使用的众多指纹技术之一。

rss · Tom's Hardware · 7月8日 10:30

**背景**: Scattered Spider（又称 UNC3944，最近被认定为 ShinyHunters）是一个主要由居住在美国和英国的青少年组成的网络犯罪组织，以攻击大型企业及其 IT 帮助台而闻名。该组织通常使用社会工程学手段获取初始访问权限，随后部署勒索软件并窃取数据。另一方面，设备指纹技术通过汇集屏幕分辨率、时区、已安装字体和浏览器配置等数十种软硬件细节，为跨网络追踪用户生成唯一标识符。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scattered_Spider">Scattered Spider - Wikipedia</a></li>
<li><a href="https://cybernews.com/security/windows-telemetry-gdid-helps-arrest-hacker/">Windows telemetry backlash: GDID tracking exposes Scattered ...</a></li>
<li><a href="https://cybersecuritynews.com/windows-device-identifier-tracking/">Windows Device Identifier Feature Leads to Arrest of ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#privacy`, `#windows-telemetry`, `#digital-fingerprinting`, `#cybercrime`

---

<a id="item-15"></a>
## [江波龙预测利润暴涨约 60,000%，受 AI 内存需求驱动](https://www.tomshardware.com/tech-industry/chinese-memory-and-storage-firm-expected-to-post-more-than-60-000-percent-jump-in-profits-due-to-exploding-demand-lexar-owner-longsys-forecasts-nearly-usd1-5-billion-profit-for-1h26-compared-to-usd2-1-million-last-year) ⭐️ 6.5/10

中国内存与存储制造商江波龙预测 2026 年上半年利润将接近 15 亿美元，较去年同期的仅 210 万美元增长超过 60,000%，主要受 AI 相关内存与存储芯片需求爆发的推动。 这一惊人的利润预测凸显了全球 AI 驱动的内存与存储芯片短缺正在重塑内存制造商的命运，尤其是历史上角色较小的中国厂商。这表明 NAND 闪存和 DRAM 市场存在严重的供需紧张，将影响消费电子、数据中心和 AI 基础设施等领域的定价。 江波龙是一家全球性的 NAND 闪存和 DRAM 解决方案提供商，自 2017 年从美光科技收购 Lexar 品牌后一直持有该品牌。该公司为全球消费和企业市场提供存储卡、固态硬盘及嵌入式存储产品。

rss · Tom's Hardware · 7月7日 16:13

**背景**: 江波龙（深圳市江波龙电子股份有限公司）是一家总部位于深圳的内存与存储公司，专注于 NAND 闪存和 DRAM 产品。2017 年，该公司从美国半导体巨头美光科技手中收购了 Lexar 品牌，获得了知名消费存储品牌和全球分销渠道。更广泛的背景是持续的 AI 驱动内存短缺：随着 AI 训练和推理工作负载需要大量高带宽内存（HBM）和大容量存储，需求激增而供应依然紧张，推动了整个内存行业的价格和盈利能力上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/chinese-memory-and-storage-firm-expected-to-post-more-than-60-000-percent-jump-in-profits-due-to-exploding-demand-lexar-owner-longsys-forecasts-nearly-usd1-5-billion-profit-for-1h26-compared-to-usd2-1-million-last-year">Chinese memory and storage firm expected to post more than ...</a></li>
<li><a href="https://www.longsys.com/about-longsys/news/longsys-acquired-the-lexar-brand-from-micron.html">Longsys acquired the Lexar brand from Micron and that Lexar ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lexar">Lexar - Wikipedia</a></li>

</ul>
</details>

**标签**: `#memory-storage`, `#AI-demand`, `#semiconductor-industry`, `#Longsys`, `#market-forecast`

---

<a id="item-16"></a>
## [快造科技完成 10 亿元融资，刷新消费级 3D 打印一级市场记录](https://36kr.com/p/3885728813691145?f=rss) ⭐️ 6.3/10

消费级 3D 打印企业快造科技（Snapmaker）完成 10 亿元新一轮融资，由凯辉基金领投，好未来战投跟投，美团战投、美团龙珠、高瓴创投、顺为资本等现有股东大比例超额追投，高鹄资本担任独家财务顾问。这是近两年一级市场消费级 3D 打印赛道最大规模的单笔融资。 该融资标志着机构资本对消费级 3D 打印赛道的信心提升——这一品类长期局限于工程师和极客群体——同时也表明多色多材料打印技术正成为打开大众消费市场的关键突破口，有助于推动 3D 打印从专业工具向消费品跃迁。 快造科技旗舰产品 U1 采用 4 独立工具头加 SnapSwap™快速换头系统架构，相比传统单喷头方案（每次换色需抽料、进料和冲刷）声称实现 5 倍打印效率提升，耗材浪费减少约 80%。该产品在 Kickstarter 筹得 2061 万美元，超 2 万名用户支持，刷新全球 3D 打印品类众筹纪录，目前已交付超过 10 万台。

rss · 36氪 · 7月8日 00:50

**背景**: 消费级 FDM 3D 打印机长期受限于单色、单材料输出，用户群体被局限在工程师和极客中。多色多材料打印被视为行业共识突破口，但主流方案依赖单喷头反复换料（每次换色都需抽料、进料和冲刷），打印多色模型往往需要数十小时且产生大量废料，难以支持多材料混合打印。为此，拓竹、创想三维、闪铸、PRUSA 等厂商都在探索多工具头架构，快造科技 U1 正是采用这一技术路线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jlc-3dp.cn/technicalColumnsDetails/58761.html">多色3D打印全解析: 从入门双色到工业级全彩的技术路径与选型指南-嘉立...</a></li>
<li><a href="https://www.163.com/dy/article/KG8G2GU2051186GP.html">FDM多材料多喷头切换3D打印大战：拓竹、快造、纵维立方、PRUSA、LIQTR...</a></li>
<li><a href="https://patents.google.com/patent/CN206999645U/zh">CN206999645U - Fdm打印机单喷头自动换料系统 - Google Patents</a></li>

</ul>
</details>

**标签**: `#3D打印`, `#消费硬件`, `#融资`, `#Snapmaker`, `#硬件创业`

---

<a id="item-17"></a>
## [「德睿智药」获 5200 万美元 B 轮融资，AI 设计的减肥药已进入 3 期临床｜36 氪首发](https://36kr.com/p/3885479689465858?f=rss) ⭐️ 6.3/10

中国 AI 制药公司德睿智药完成 5200 万美元 B 轮融资，其 AI 设计的口服 GLP-1 小分子减肥药 MDR-001 已进入三期临床试验阶段。

rss · 36氪 · 7月8日 00:00

**标签**: `#AI drug discovery`, `#pharmaceuticals`, `#GLP-1`, `#funding`, `#China tech`

---

<a id="item-18"></a>
## [Cloudflare 与 OpenAI 启动试点，利用网络信号优化 AI 搜索索引](https://36kr.com/newsflashes/3886946347694593?f=rss) ⭐️ 6.3/10

7 月 8 日，Cloudflare 与 OpenAI 宣布启动一项研究试点项目，利用 Cloudflare 全球网络的实时信号（包括内容更新鲜度、流量质量和页面实际变动），帮助 AI 搜索引擎更高效地发现并索引开放网络上的相关内容，从而提升 AI 回答的准确性与时效性。 此次合作意义重大，因为 Cloudflare 的网络承载了全球超过五分之一网站的流量，能够为 OpenAI 提供独特的大规模实时网页内容信号。这些数据不仅有望显著提升 AI 搜索结果的相关性和时效性，还可能影响整个 AI 行业与网络基础设施提供商之间的互动方式。 该试点围绕三种信号类型展开：内容更新鲜度、流量质量和页面实际变动，所有信号均通过 Cloudflare 的 CDN 实时观测。值得注意的是，Cloudflare 于 2025 年 9 月还推出了 Content Signals Policy（内容信号策略），扩展了 robots.txt 框架，让内容发布者能够更精细地控制其内容在 AI 场景中的使用方式，这也为此次合作提供了更广泛的背景。

rss · 36氪 · 7月8日 12:06

**背景**: 传统搜索引擎依赖爬虫定期扫描网络、将网页存储在索引中，并根据关键词和链接对结果进行排序。AI 驱动的搜索引擎则有所不同，它们尝试理解上下文、处理动态内容并自主适应，而非仅仅匹配关键词。两种方法都面临着在网络规模下高效发现新鲜、高质量内容的挑战。Cloudflare 作为一家主要的 CDN 提供商，处于用户与源服务器之间，处于独特位置，能够观察跨互联网大部分区域的实时网络信号，使其数据对于改进传统和 AI 驱动的抓取策略都具有重要价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rallies.ai/news/cloudflare-launches-openai-pilot-using-signals-from-20-of-web-traffic">Cloudflare Launches OpenAI Pilot Using Signals from 20% of ...</a></li>
<li><a href="https://blog.cloudflare.com/content-signals-policy/">Giving users choice with Cloudflare’s new Content Signals Policy</a></li>
<li><a href="https://avenuez.com/blog/ai-crawlers-vs-traditional-crawlers-how-ai-indexes-the-web-differently/">AI Crawlers vs. Traditional Crawlers: How AI Indexes the Web ...</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#OpenAI`, `#AI搜索`, `#网页索引`, `#基础设施`

---

<a id="item-19"></a>
## [蓝色起源以 1300 亿美元估值完成 100 亿美元融资](https://36kr.com/newsflashes/3886944497154824?f=rss) ⭐️ 6.3/10

蓝色起源以 1300 亿美元的估值完成了 100 亿美元的融资轮，其中创始人杰夫·贝佐斯个人出资 20 亿美元。 这一巨额估值表明投资者对商业航天领域信心十足，也让蓝色起源获得了更充裕的资金，以便在与 SpaceX 的发射服务、月球着陆器项目以及长期太空基础设施布局中展开更激烈的竞争。 贝佐斯个人出资 20 亿美元是一个显著信号，表明尽管他自卸任亚马逊 CEO 以来已较少参与日常事务，仍持续在资金上给予公司有力支持。1300 亿美元的投后估值较此前公开的估值有大幅提升，凸显了投资者对后期商业航天公司的强烈兴趣。

rss · 36氪 · 7月8日 12:04

**背景**: 蓝色起源由杰夫·贝佐斯于 2000 年创立，是一家总部位于美国华盛顿州肯特的私营航天技术公司。该公司运营用于太空旅游的亚轨道火箭 New Shepard，以及用于轨道载荷的重型运载火箭 New Glenn。蓝色起源的主要竞争对手是 SpaceX，同时已获得 NASA 阿尔忒弥斯月球着陆器项目的合同。公司名称蕴含其长期愿景——让数百万人能够在太空中生活和工作，造福地球。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blue_Origin">Blue Origin - Wikipedia</a></li>
<li><a href="https://www.blueorigin.com/about-blue">About Blue Origin</a></li>
<li><a href="https://spacenexus.us/blog/spacex-blue-origin-rocket-lab-comparison-2026">SpaceX vs Blue Origin vs Rocket Lab: Launch Provider ...</a></li>

</ul>
</details>

**标签**: `#Blue Origin`, `#funding`, `#space industry`, `#Bezos`, `#venture capital`

---

<a id="item-20"></a>
## [解读优衣库 T 恤上的混淆 Bash 脚本](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/) ⭐️ 6.0/10

分析优衣库与 Akamai 联名 T 恤上印制的混淆自求值 Bash 脚本，探讨其工作原理及背后的设计决策。

hackernews · speerer · 7月8日 08:46 · [社区讨论](https://news.ycombinator.com/item?id=48829312)

**标签**: `#bash`, `#obfuscation`, `#quine`, `#hacker-news`, `#creative-coding`

---