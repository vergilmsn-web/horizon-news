---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 63 条内容中筛选出 17 条重要资讯。

---

1. [LG 显示器通过 Windows Update 静默安装软件且未经用户同意](#item-1) ⭐️ 8.0/10
2. [新型θ-TaN 金属热导率达铜的三倍](#item-2) ⭐️ 8.0/10
3. [台积电 A14 工艺进展超 N2 同期，吸引 AI/HPC 及智能手机客户](#item-3) ⭐️ 7.5/10
4. [月之暗面有望最快 6 个月内赴港上市](#item-4) ⭐️ 7.3/10
5. [退化型 JPEG](#item-5) ⭐️ 7.0/10
6. [TP-Link Kasa EC71 摄像头通过未认证 UDP 泄露家庭 GPS 坐标长达 6 年](#item-6) ⭐️ 7.0/10
7. [Julia Evans 分享生产环境运行 SQLite 的经验教训](#item-7) ⭐️ 7.0/10
8. [Kimi K3 以及我们仍能从鹈鹕基准测试中学到什么](#item-8) ⭐️ 7.0/10
9. [ASML 计划上调 Low-NA EUV 光刻机价格，引发台积电不满](#item-9) ⭐️ 6.5/10
10. [国家数据局：全国已建成高质量数据集 12 万个](#item-10) ⭐️ 6.3/10
11. [TSMC CoWoS 对决 Intel EMIB：客户是否正在转向英特尔的封装技术？](#item-11) ⭐️ 6.0/10
12. [PC 厂商争抢长鑫存储内存供应，小型 OEM 举步维艰](#item-12) ⭐️ 5.5/10
13. [英伟达 RTX 50 Super 显卡已就绪但因 GDDR7 价格过高而搁置](#item-13) ⭐️ 5.5/10
14. [韩国机构举办 1.44MB 游戏开发大赛致敬软盘——参赛者须将整套文件（含资源、引擎及库）压缩至极小存储格式](#item-14) ⭐️ 5.5/10
15. [40 克自主微型无人机利用汽车泊车传感器实现空中击杀蚊子](#item-15) ⭐️ 5.5/10
16. [佛州男子利用 Steam 游戏藏匿恶意软件窃取 22 万美元加密货币被捕](#item-16) ⭐️ 5.5/10
17. [AMD Instinct MI350P：144GB HBM3E PCIe AI 加速器频繁现身](#item-17) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [LG 显示器通过 Windows Update 静默安装软件且未经用户同意](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 8.0/10

LG 显示器在通过 HDMI 接口插入的瞬间，会通过 Windows Update 静默安装 LG OnScreen Control 软件，且无需任何用户提示或同意。该软件以设备元数据包的形式由 Windows 自动获取并在后台安装，跨重启持续运行，并拥有不受限制的系统权限。 这一行为代表了一次严重的供应链信任失败：硬件厂商仅凭显示器物理连接，就能向任何 Windows 机器静默部署具有完全权限的软件，模糊了驱动程序交付与未授权软件安装之间的界限。它影响到每一位购买或连接 LG 显示器的 Windows 用户，并暴露了微软 Windows Update 合作伙伴渠道可被用来绕过用户明确同意的风险。 受影响的软件包括 LG 的 OnScreen Control，它通常需要通过 USB 连接手动安装，用于屏幕分割、显示器设置和固件更新。用户可以通过组策略（计算机配置 > 管理模板 > 系统 > 设备安装：禁止自动下载与设备元数据相关联的应用程序）来阻止静默安装；在家庭版上，则可通过 sysdm.cpl > 硬件 > 设备安装设置，将「是否自动下载设备的制造商应用」选择为「否」来禁用该行为。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 通常用于交付操作系统补丁、安全修复和硬件驱动程序，但微软也允许第三方硬件厂商（IHV/OEM）通过其硬件合作伙伴仪表板发布驱动程序和元数据包，这些包会经过飞行测试和基于 Windows 遥测的渐进式推广。当系统检测到新显示器时，Windows 可以获取相关元数据并静默安装厂商随附的软件——这一机制最初是为了方便而设计的，但它同样会赋予厂商软件完整的系统权限，且没有任何沙箱隔离。LG 的 OnScreen Control 是此次被推送的具体工具，它传统上是基于 USB 的可选工具，现在却通过 Windows Update 渠道自动到达用户机器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/develop/distributing-a-driver-package">Distributing a Driver Package - Windows drivers | Microsoft Learn</a></li>
<li><a href="https://www.lg.com/us/support/help-library/lg-monitor-onscreen-control-how-to-update-monitor-software--20154710888908">[LG Monitor OnScreen Control] How to Update Monitor Software ...</a></li>
<li><a href="https://www.fingerlakes1.com/2026/07/18/lg-monitor-software-now-installs-through-windows-update-and-many-users-did-not-expect-it/">LG Monitor Software Now Installs Through Windows Update and ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应强烈，许多用户认为这种行为与恶意软件几乎没有区别，因为该软件以完整系统权限安装、每次开机都会运行，且完全无需用户交互。有用户清晰地分享了通过组策略和设备安装设置来阻止此行为的解决方案，而大量讨论的焦点则在于将责任从 LG 转向微软——因为正是 Windows 自身根据硬件元数据执行了静默安装操作。多位评论者指出，微软作为 Windows Update 的把关者，拥有拒绝此类载荷的能力和责任，应当执行更严格的准则以防止厂商捆绑无关软件。

**标签**: `#security`, `#privacy`, `#windows-update`, `#lg`, `#supply-chain`, `#hardware`

---

<a id="item-2"></a>
## [新型θ-TaN 金属热导率达铜的三倍](https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/) ⭐️ 8.0/10

研究人员成功实验制备了单晶θ相氮化钽（θ-TaN），这是一种亚稳态过渡金属氮化物，在室温下热导率约为 1100 W/m·K，接近铜（约 400 W/m·K）的三倍。该突破性成果于 2026 年 1 月 15 日发表在《Science》期刊上。 如果该材料能够实现规模化制造并集成到半导体工艺中，将有望显著改善芯片、电力电子和高性能计算系统中的散热性能——而散热正是这些领域的关键瓶颈。该材料有可能颠覆芯片散热层的设计，并在未来器件中实现更高的功率密度。 θ-TaN 是一种亚稳态相，意味着它的形成需要特定的合成条件，在实际应用中可能难以稳定存在。该材料超高热导率的理论预测最早于 2021 年发表在《Physical Review Letters》上，预测沿 a 轴和 c 轴的热导率分别为约 995 和 820 W/m·K。铜的热导率受限于固有的电子-声子散射机制，基本被限制在 400 W/m·K 左右，而θ-TaN 似乎突破了这一限制。

rss · EE Times · 7月17日 19:00

**背景**: 热导率衡量材料传导热量的能力，单位为瓦每米开尔文（W/m·K）。铜的热导率约为 400 W/m·K，长期以来一直是电子产品散热管理的标准材料，但其热导率受到固有散射机制（主要是电子-声子相互作用）的根本限制，这为所有金属导体的热导率设定了上限。氮化钽（TaN）是一种在半导体领域广为人知的化合物，尤其用作铜互连中的扩散阻挡层，它根据合成条件的不同存在多种晶体相。θ相是一种特定的亚稳态晶体结构，理论研究曾预测由于其电子和声子特性的独特组合，将具有异常高的热导率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/science.aeb1142">Metallic θ-phase tantalum nitride has a thermal conductivity ...</a></li>
<li><a href="https://link.aps.org/doi/10.1103/PhysRevLett.126.115901">Ultrahigh Thermal Conductivity of -Phase Tantalum Nitride ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tantalum_nitride">Tantalum nitride - Wikipedia</a></li>

</ul>
</details>

**标签**: `#materials-science`, `#thermal-management`, `#semiconductors`, `#chip-cooling`, `#nanotechnology`

---

<a id="item-3"></a>
## [台积电 A14 工艺进展超 N2 同期，吸引 AI/HPC 及智能手机客户](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers) ⭐️ 7.5/10

台积电确认其 A14（1.4 纳米级）工艺技术的进展速度快于 N2（2 纳米）节点在相同发展阶段的表现，在良率和性能方面均有显著提升。公司表示，来自 AI/HPC 开发者以及智能手机芯片设计商的客户兴趣浓厚，均计划采用这一新工艺节点。 A14 工艺的加速开发意味着尖端芯片制造的时间表可能提前，将惠及 AI 加速器、高性能计算系统以及下一代智能手机。多领域客户的强劲采用验证了台积电在最前沿制程的领先地位，同时也加剧了与三星和英特尔在 2 纳米以下赛道的竞争。 A14 是台积电首个采用第二代 GAAFET（环绕栅极）晶体管架构的节点，接替首次引入第一代 GAA nanosheet 设计的 N2。与 N2 相比，A14 预计可在相同功耗下提供最高 15%的性能提升，或在相同速度下降低高达 30%的功耗，目标量产时间为 2028 年。

rss · Tom's Hardware · 7月17日 15:30

**背景**: 台积电的工艺节点名称基于市场命名而非实际的物理尺寸——A14 名称对应 1.4 纳米级别的技术世代。良率是衡量制造工艺的关键指标，表示符合性能和规格要求的芯片在产出中的比例；更高的良率可降低单芯片成本并反映工艺成熟度。N2 是台积电目前进入量产的尖端节点，采用第一代 GAA nanosheet 晶体管，而 A14 将使用改进的第二代 GAAFET 架构，以在功耗、性能和面积（PPA）方面获得进一步提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A14">A14 Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/tsmc-a14-process-technology-wiki/">TSMC A14 Process Technology Wiki - Semiwiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yield_(metric)">Yield (metric) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#semiconductors`, `#process-technology`, `#A14`, `#AI-HPC`

---

<a id="item-4"></a>
## [月之暗面有望最快 6 个月内赴港上市](https://36kr.com/newsflashes/3900806713951873?f=rss) ⭐️ 7.3/10

Moonshot AI（月之暗面）正进行重组以筹备赴港 IPO，有望在 6 个月内上市，同期发布了 Kimi K3 模型，据称是全球最大的开源模型，在 Code Arena 上的表现超越了 Claude 和 GPT。

rss · 36氪 · 7月18日 07:45

**标签**: `#Moonshot AI`, `#IPO`, `#Kimi K3`, `#open-source models`, `#Chinese AI`

---

<a id="item-5"></a>
## [退化型 JPEG](https://maurycyz.com/projects/bad_jpeg/) ⭐️ 7.0/10

一个创意项目，通过操控 JPEG 系数的排序顺序来制作类似 GIF 的动画视频，使运动效果在文件逐步解码的过程中自然涌现。

hackernews · vitaut · 7月18日 03:14 · [社区讨论](https://news.ycombinator.com/item?id=48954851)

**标签**: `#jpeg`, `#image-processing`, `#creative-coding`, `#steganography`, `#codec-hacks`

---

<a id="item-6"></a>
## [TP-Link Kasa EC71 摄像头通过未认证 UDP 泄露家庭 GPS 坐标长达 6 年](https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md) ⭐️ 7.0/10

安全研究员 BadChemical 披露，TP-Link Kasa EC71 室内安防摄像头通过未认证的 UDP 流量广播其配置的家庭 GPS 坐标，这一漏洞在固件中持续了约六年。TP-Link 随后发布的固件更新据报告导致部分设备变砖，进一步引发了对厂商质量保证流程的担忧。 该披露揭示了消费级 IoT 设备通过未加密、未认证协议泄露敏感位置遥测数据的更广泛模式，且这些数据通常被发送到厂商无法控制的云端端点。对于像 TP-Link 这样大规模部署的品牌而言，这种长期存在的缺陷会削弱消费者对现成智能家居安防产品的信任。 该泄露依赖 UDP——一种无连接的协议，不提供认证或加密机制，这意味着同一局域网段上的任何设备都可以被动监听并收集 GPS 数据。社区评论者指出，实际暴露范围有限，除非摄像头被放置在路由器的 DMZ 中，因为默认情况下它无法直接从公网访问。

hackernews · BadChemical · 7月17日 21:42 · [社区讨论](https://news.ycombinator.com/item?id=48952565)

**背景**: TP-Link Kasa EC71（Kasa Spot Pan Tilt）是一款具备运动追踪、夜视和 microSD 存储功能的 1080p 室内安防摄像头，属于 TP-Link 面向消费者的 Kasa 智能家居产品线。UDP（用户数据报协议）是一种轻量级、无连接的传输层协议，常用于 DNS、NTP 和流式遥测等对时效性或低开销要求较高的通信场景，但由于缺乏认证机制，任何能够访问该网络的人都可以查询或窃听监听 UDP 端口的服务。IoT 设备上未认证的 UDP 服务历来是隐私泄露和反射型 DDoS 放大攻击的反复出现的源头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tp-link.com/us/home-networking/cloud-camera/ec71/v1/">EC71 | Kasa Spot Pan Tilt, 24/7 Recording | TP-Link</a></li>
<li><a href="https://static.tp-link.com/upload/product-overview/2024/202403/20240318/EC71+4.6_Datasheet.pdf">Kasa Spot® Pan Tilt 24/7 Recording Indoor Security Camera EC71 Motion Tracking</a></li>
<li><a href="https://www.kb.cert.org/vuls/id/417980">VU#417980 - Implementations of UDP-based application protocols are vulnerable to network loops</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：部分评论者认为这份报告是 IoT 系统性安全问题的典型体现，ericpauley 指出许多设备将数据发送到厂商无法控制的云 IP，而 gruez 认为报告看起来是 AI 生成的，且实际风险在纯局域网部署中很小，除非错误配置了 DMZ。drnick1 强调了廉价 IoT 硬件绝不应直接暴露在公网上的观点，nubinetwork 和 BobbyTables2 则分别对导致设备变砖的固件更新和漫长的披露时间表表示担忧。

**标签**: `#security`, `#iot`, `#vulnerability`, `#privacy`, `#tp-link`

---

<a id="item-7"></a>
## [Julia Evans 分享生产环境运行 SQLite 的经验教训](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) ⭐️ 7.0/10

Julia Evans 发布了一篇博客文章，详细分享了她在生产环境运行 SQLite 时学到的实践经验，涵盖性能问题、备份和运维注意事项。该文章引发了社区的强烈关注，读者们分享了工具技巧，并对她的性能假设提出了技术批评。 Julia Evans 是一位广受尊敬的技术教育者，她对生产环境 SQLite 的探索为那些不再满足于玩具项目和原型的开发者提供了宝贵的实战见解。社区讨论既带来了可直接应用的工具技巧，也对小规模下的性能假设提出了重要的反驳意见，使其成为一个关于诚实、基于经验的写作的有价值案例研究。 SQLite CLI 中的 `.expert` 模式可以根据分析的查询自动推荐索引，对于不熟悉阅读查询计划的开发者来说是一个很有用的工具。一位专注于数据库的评论者（stevoski）认为，仅 10k 行的全表扫描本应几乎是瞬时的，并怀疑慢删除问题其实是经典的 n+1 查询问题，而非 SQLite 的性能限制。

hackernews · surprisetalk · 7月17日 17:45 · [社区讨论](https://news.ycombinator.com/item?id=48950122)

**背景**: SQLite 是一个自包含、无服务器、支持事务的 SQL 数据库引擎，以进程内方式运行，非常适合嵌入式应用、移动应用，以及越来越多地被用于中小型 Web 服务。Julia Evans 以其通俗易懂的「Wizard Zines」和透明的学习风格而闻名，经常公开记录自己的学习过程。在生产环境中运行 SQLite 与 PostgreSQL 等客户端/服务器数据库不同，因为没有独立的数据库服务器进程，这会影响备份策略、并发处理方式以及可用的运维工具。

**社区讨论**: 社区反应热烈且观点多元。评论者们分享了实用的补充信息，例如 SQLite 的 `.expert` 索引推荐模式和 Simon Willison 的 `s3-credentials` 工具（用于限定范围的 AWS 访问）。一位数据库从业者（stevoski）强烈质疑 10k 行级别出现性能问题这一前提，怀疑真正的元凶是经典的 n+1 查询；另一些人则赞扬 Julia 真实的探索式写作风格，认为与过度自信的 LLM 生成内容形成了令人耳目一新的对比，但也有评论者认为该文章缺乏实质内容。

**标签**: `#sqlite`, `#databases`, `#operations`, `#performance`, `#devops`

---

<a id="item-8"></a>
## [Kimi K3 以及我们仍能从鹈鹕基准测试中学到什么](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 7.0/10

Simon Willison 对 Kimi K3 的分析以及鹈鹕基准测试的局限性，揭示了它在评估现代大语言模型方面的价值与不足，尤其是在智能体工具使用和隐藏系统提示方面。

hackernews · droidjj · 7月17日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947717)

**标签**: `#ai-benchmarks`, `#llm-evaluation`, `#kimi-k3`, `#simon-willison`, `#model-analysis`

---

<a id="item-9"></a>
## [ASML 计划上调 Low-NA EUV 光刻机价格，引发台积电不满](https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions) ⭐️ 6.5/10

据报道，ASML 正计划上调其 Low-NA EUV 光刻机的价格，理由是这些设备的生产力有所提升。此次涨价可能会让正在扩建晶圆厂产能的台积电多花费数十亿美元。 这之所以重要，是因为台积电已在其先进制程（A16 和 A14）上做出了重大战略押注——选择使用 Low-NA EUV 配合多重图形曝光技术，而非采用 High-NA EUV，这意味着它将需要更多的 Low-NA 设备，并承担任何价格上涨带来的冲击。这一财务影响可能会波及整个半导体供应链，进而影响芯片定价和先进晶圆厂建设的经济性。 ASML 的 Low-NA EUV 系统采用 0.33 数值孔径的光学元件，台积电计划利用计算光刻技术（如逆向光刻和曲率掩膜版优化）来延伸其可用分辨率，而非升级到 High-NA 设备。据报道，每台 High-NA EUV 系统的价格显著高于 Low-NA 系统，这使得采用 Low-NA 配合多重图形曝光成为台积电近期路线图中更具成本效益的路径。

rss · Tom's Hardware · 7月17日 15:57

**背景**: ASML 是全球唯一的 EUV（极紫外）光刻系统供应商，这些设备对于制造 7nm 以下的先进芯片至关重要。Low-NA EUV（数值孔径 0.33）自 2019 年前后已投入大规模量产，而 High-NA EUV（数值孔径 0.55）则是下一代技术，能提供更好的分辨率，但成本也高得多。台积电已公开表示将在其 A16（1.6nm）和 A14（1.4nm）制程中跳过 High-NA EUV，转而使用 Low-NA 配合先进的多重图形曝光技术和计算光刻技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/asml-lithograpy-roadmap-examined-from-duv-to-hyper-na">ASML's roadmap for chipmaking lithography tools examined — from DUV to Low-NA, High-NA, Hyper-NA, and beyond | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#ASML`, `#TSMC`, `#EUV-lithography`, `#chip-manufacturing`

---

<a id="item-10"></a>
## [国家数据局：全国已建成高质量数据集 12 万个](https://36kr.com/newsflashes/3900807486293892?f=rss) ⭐️ 6.3/10

国家数据局表示，全国已建成 12 万个高质量数据集，总容量达 1565PB，单季度增长 60%。目前已设立 7 个数据标注试点城市，拥有 14 万名标注从业人员，为人工智能发展提供支撑。

rss · 36氪 · 7月18日 08:00

**标签**: `#China-AI`, `#data-infrastructure`, `#AI-policy`, `#national-strategy`, `#data-annotation`

---

<a id="item-11"></a>
## [TSMC CoWoS 对决 Intel EMIB：客户是否正在转向英特尔的封装技术？](https://semiwiki.com/semiconductor-manufacturers/tsmc/371412-tsmc-cowos-versus-intel-emib-semiconductor-packaging/) ⭐️ 6.0/10

SemiWiki 报道称，在最近举行的会议上，有传闻指出部分 TSMC 的客户正将晶圆送往 Intel 进行封装，这一趋势促使 TSMC 首席执行官魏哲家在最近一次投资者电话会议上被问及 EMIB-T 时的看法。 由于 AI 加速器需求激增，CoWoS 产能严重受限，任何客户向 Intel EMIB 的迁移都将表明 TSMC 在先进封装领域的主导地位正面临竞争压力，并可能重塑 Nvidia、AMD 等芯片制造商的供应链策略。 已发布的文章只是一段截断的预告，CEO 魏哲家的实际评论被付费墙或"阅读更多"链接遮挡；可见文本中并未披露标准 EMIB 与文中提及的 EMIB-T 变体之间的精确技术差异。

rss · SemiWiki · 7月17日 15:00

**背景**: CoWoS（Chip-on-Wafer-on-Substrate，芯片上晶圆上基板）是 TSMC 的 2.5D 先进封装技术，它将多个小芯片（chiplet）放置在硅中介层上以实现高带宽通信，是 Nvidia 旗舰 AI GPU 的核心封装方案。EMIB（Embedded Multi-die Interconnect Bridge，嵌入式多芯片互连桥）是 Intel 的竞争性 2.5D 方案，它将小型硅桥嵌入有机基板中，而不是使用完整的硅中介层，因此可能更具成本效益。这两项技术都旨在解决同一核心挑战：在单个封装中集成多个小芯片，通过高密度、低延迟的互连来支撑现代 AI 和高性能计算工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://logicity.in/en/blog/tsmc-cowos-can-pack-58-dies-before-panels-take-over">TSMC : CoWoS can pack 58 dies before panels take over | Logicity</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/intel-emib-embedded-multi-die-interconnect-bridge/">Intel EMIB (Embedded Multi-die Interconnect Bridge) - SemiWiki</a></li>
<li><a href="https://semiconductorx.com/packaging-emib.html">EMIB Advanced Packaging: Embedded Multi-Die Interconnect ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#advanced-packaging`, `#TSMC`, `#Intel`, `#CoWoS`

---

<a id="item-12"></a>
## [PC 厂商争抢长鑫存储内存供应，小型 OEM 举步维艰](https://www.techpowerup.com/350853/pc-vendors-fight-for-cxmt-memory-supply-smaller-oems-struggle) ⭐️ 5.5/10

戴尔、惠普和苹果等主要 PC OEM 厂商已锁定中国内存厂商长鑫存储（CXMT）直至 2027 年的 DRAM 产能份额，而小型厂商则因 CXMT 产能有限以及三大内存厂商供应紧张而陷入困境。

rss · TechPowerUp News · 7月17日 17:56

**标签**: `#DRAM`, `#supply-chain`, `#CXMT`, `#PC-hardware`, `#semiconductors`

---

<a id="item-13"></a>
## [英伟达 RTX 50 Super 显卡已就绪但因 GDDR7 价格过高而搁置](https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb) ⭐️ 5.5/10

据报道，英伟达的 RTX 50 Super 显卡已经开发完成，但由于 3GB GDDR7 显存模块价格虚高（是标准 RTX 50 系列所采用的 2GB GDDR7 芯片价格的 2 到 3 倍），导致这些显卡的发布被迫推迟。这一价格差异预计将使 Super 版本的零售价远超英伟达设定的建议零售价目标。 这一事件的重要性在于，它凸显了显存供应链成本如何直接影响产品能否上市以及以何种价格上市，可能让游戏玩家和硬件发烧友不得不等待更长时间才能迎来一轮中端显卡更新。它同时也反映出显卡制造商在 DRAM 价格波动时期管理物料成本所面临的更广泛挑战。 Super 系列所需的 3GB GDDR7 模组相比 2GB 模组有 2 到 3 倍的价格溢价，这很可能是因为高密度显存芯片的良率较低，在市场上也更加稀缺。英伟达面临一个艰难的抉择：要么自行消化上涨的物料成本（从而侵蚀利润率），要么将其转嫁给消费者（在显卡定价已经备受关注的时期面临需求疲软的风险）。

rss · Tom's Hardware · 7月18日 13:45

**背景**: GDDR7 是最新一代的图形显存，专为 GPU 和 AI 加速器等高带宽应用而设计，它被直接焊接到显卡上，而不是作为可拆卸的内存模块来安装。现有的 RTX 50 系列使用的是 2GB GDDR7 芯片；改用 3GB 模组可以在更窄的显存位宽下实现更大的总容量（例如 24GB 或 32GB），但单颗芯片的成本更高。建议零售价（MSRP，Manufacturer's Suggested Retail Price）是英伟达官方建议的售价，但实际上零售市场的'市售价'往往会因供货情况、需求以及零售商加价等因素而与之不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GDDR7_SDRAM">GDDR7 SDRAM - Wikipedia</a></li>
<li><a href="https://semiconductor.samsung.com/dram/gddr/gddr7/">GDDR7 - DRAM | Samsung Semiconductor Global</a></li>
<li><a href="https://www.cgdirector.com/gpu-msrp-list/">GPU MSRP List - AMD, Nvidia & Intel Graphics Cards</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#gpu`, `#gddr7`, `#hardware`, `#pricing`

---

<a id="item-14"></a>
## [韩国机构举办 1.44MB 游戏开发大赛致敬软盘——参赛者须将整套文件（含资源、引擎及库）压缩至极小存储格式](https://www.tomshardware.com/software/korean-outfit-hosting-1-44mb-game-development-contest-to-honor-the-floppy-disk-entrants-must-confine-entire-fileset-including-resources-engine-and-library-to-miniscule-storage-format) ⭐️ 5.5/10

韩国某机构正在举办一场开放式游戏开发大赛，要求所有游戏文件（引擎、资源、库）均须容纳在 1.44MB 软盘容量内，前三名获奖者将获得现金奖励。

rss · Tom's Hardware · 7月18日 11:00

**标签**: `#game-development`, `#code-optimization`, `#retro-computing`, `#contest`, `#demoscene`

---

<a id="item-15"></a>
## [40 克自主微型无人机利用汽车泊车传感器实现空中击杀蚊子](https://www.tomshardware.com/tech-industry/drones/autonomous-micro-drone-achieves-first-air-to-air-insect-kill-on-the-way-towards-completely-eradicating-mosquitoes-40-gram-unit-uses-car-parking-sensors-can-eliminate-insects-at-up-to-26-feet) ⭐️ 5.5/10

一架搭载汽车超声波泊车传感器的 40 克自主微型无人机完成了首次空中击杀蚊子的测试，能够在远至 26 英尺（约 8 米）的距离上探测并消灭飞行中的昆虫。该里程碑被描述为迈向彻底消灭蚊子的目标的一步。 蚊子是疟疾、登革热和寨卡病毒等疾病的主要传播媒介，因此自主空中精准打击可以补充甚至替代传统的杀虫剂喷洒和幼虫治理。将廉价、量产的汽车传感器重新用于生物害虫防治，体现了消费级硬件向公共健康应用转化的潜力。 该无人机仅重 40 克，依赖与汽车保险杠泊车辅助系统相同的超声波近距离探测原理，即通过测量超声波回波的时间来计算与障碍物的距离。26 英尺的有效击杀距离表明超声波传感器能够在数倍于无人机自身翼展的距离上可靠识别小型快速移动的昆虫目标，但文章并未详细说明击杀机制或飞行续航的限制。

rss · Tom's Hardware · 7月18日 09:00

**背景**: 汽车泊车传感器是安装在车辆保险杠上的超声波近距离探测器，通过发射高频声波脉冲并测量回波返回时间来估算与附近物体的距离，通常用于在低速行驶时提醒驾驶员注意障碍物。20 kHz 以上的超声波频率在昆虫学领域早已用于探测昆虫，包括蛀木害虫，因为该频段的背景噪声可以忽略不计。自主微型无人机结合了微型飞控、机载传感器以及日益成熟的感知算法，能够在没有人类操控的情况下自主导航并追踪目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Parking_sensor">Parking sensor - Wikipedia</a></li>
<li><a href="https://www.bosch-mobility.com/en/solutions/sensors/ultrasonic-sensor/">Ultrasonic sensor - Bosch Mobility</a></li>
<li><a href="https://www.mdpi.com/2504-446X/9/6/442">UAV Autonomous Navigation System Based on Air–Ground ... - MDPI</a></li>

</ul>
</details>

**标签**: `#drones`, `#robotics`, `#autonomous-systems`, `#public-health`, `#sensor-technology`

---

<a id="item-16"></a>
## [佛州男子利用 Steam 游戏藏匿恶意软件窃取 22 万美元加密货币被捕](https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards) ⭐️ 5.5/10

联邦调查局逮捕了来自佛罗里达州北劳德代尔堡的 21 岁嫌疑人 Zyaire Dontaevious Zamarion Wilkins，罪名是通过隐藏在 Steam 游戏中的恶意软件窃取了价值 22 万美元的加密货币，该恶意软件感染了约 8000 台设备。联邦探员追踪到被盗比特币被用于购买 Uber Eats 礼品卡，由此锁定并逮捕了嫌疑人。 此案件凸显了通过游戏平台传播恶意软件的威胁日益严重，以及以加密货币为目标的网络犯罪的复杂性不断提高。它为游戏玩家和加密货币持有者敲响了警钟，展示了攻击者如何利用 Steam 等受信任的平台向大量受害者投递加密货币窃取程序。 加密货币窃取恶意软件（CryptoStealer）通常会在受感染的机器上搜索加密货币钱包文件、剪贴板活动和包含金融数据的浏览器 Cookie，然后将信息外传到命令与控制服务器。基于 Steam 的恶意软件分发经常利用该平台的创意工坊和模组功能，与 2025 年 9 月发现的 ModStealer 恶意软件类似，后者能够躲避杀毒软件检测，同时针对基于浏览器的加密货币钱包。

rss · Tom's Hardware · 7月17日 14:43

**背景**: Steam 是由 Valve Corporation 运营的全球最大数字游戏分发平台之一，拥有数亿活跃用户。其创意工坊功能允许用户创建和分享模组、皮肤和其他游戏自定义内容，这些功能有时会被利用来隐藏恶意代码。加密货币窃取恶意软件（称为 CryptoStealer 或信息窃取器）是一类有据可查的恶意软件，专门用于从受感染系统中定位和窃取数字钱包凭证、私钥和助记词。这些恶意软件家族通常在后台静默运行，使得在没有强大终端安全解决方案的情况下难以检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcrisk.com/removal-guides/14419-cryptostealer-trojan">CryptoStealer Trojan - Malware removal instructions (updated) Malwarebytes Threat Alert | Trojan.CryptoStealer.Go Undetectable crypto-stealing ModStealer malware targets ... New lightweight, self-propagating crypto stealing malware ... 5 Crypto-Stealing Malware Threats: How to Stay Safe and Aware Beware Bitcoin, Ether, Solana, XRP Wallets: This Virus Is ...</a></li>
<li><a href="https://www.malwarebytes.com/blog/detections/trojan-cryptostealer-go">Malwarebytes Threat Alert | Trojan.CryptoStealer.Go</a></li>
<li><a href="https://crypto.news/undetectable-crypto-stealing-modstealer-malware-targets-wallets-on-mac-and-windows/">Undetectable crypto-stealing ModStealer malware targets ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#cryptocurrency`, `#malware`, `#crime`, `#gaming`

---

<a id="item-17"></a>
## [AMD Instinct MI350P：144GB HBM3E PCIe AI 加速器频繁现身](https://www.servethehome.com/the-amd-instinct-mi350p-is-a-hbm-pcie-accelerator-that-has-been-all-over/) ⭐️ 5.5/10

AMD Instinct MI350P 是一款采用 PCIe 形态的 AI 加速器，配备 144GB HBM3E 显存和 128 个计算单元（CU），最近几周在多个场合和部署中频繁亮相。AMD 将其定位为可直接替换升级现有企业 AI 基础设施的产品。 MI350P 的重要性在于，它为企业提供了一条基于 PCIe 的大显存 AI 加速升级路径，无需改造服务器机柜以适配更新的互联拓扑。其 144GB HBM3E 容量以及宣称的 FP16/FP8 性能约比 NVIDIA H200 NVL 高 40%，使其在高端推理和训练市场中具备竞争力。 该加速卡采用 HBM3E 显存，这是一种 3D 堆叠 DRAM 技术，可提供远超传统 GDDR 显存更高的带宽和容量。PCIe 形态（而非 OAM 或专有模块）意味着它可以插入标准服务器插槽，尽管与基于专用互联的方案相比，其与主机 CPU/GPU 池之间的带宽通常较低。

rss · ServeTheHome · 7月17日 17:00

**背景**: AMD Instinct 系列是 AMD 面向数据中心 GPU 的产品线，旨在与 NVIDIA 的加速器在 AI 和高性能计算领域竞争。HBM（高带宽存储器）是一种由三星、AMD 和 SK 海力士最初联合开发的 3D 堆叠 DRAM 技术，因大语言模型同时需要高显存容量和高显存带宽而被广泛应用于现代 AI 加速器。MI350 系列是 AMD 采用 HBM3E 的最新一代产品，后缀 'P' 表示 PCIe 形态版本，区别于该系列中的其他形态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/amd-announces-mi350p-pcie-ai-accelerator-card-with-144gb-of-hbm3e-roughly-40-percent-faster-in-fp16-and-fp8-theoretical-compute-compared-to-nvidias-h200-nvl-competitor">AMD announces MI350P PCIe AI accelerator card with 144GB of ...</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi350p.html">AMD Instinct™ MI350P PCIe® Cards</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AMD`, `#AI Accelerator`, `#GPU`, `#HBM3E`, `#Hardware`

---