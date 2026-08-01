---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> 从 110 条内容中筛选出 20 条重要资讯。

---

1. [Tailscale 发布关于 Hugging Face 入侵事件的透明事后分析](#item-1) ⭐️ 8.0/10
2. [CEA-Leti 推进 3D 堆叠路线图，应对 AI 遭遇的内存与功耗瓶颈](#item-2) ⭐️ 8.0/10
3. [Zoox 成为首家获批真正无人驾驶 robotaxi 的公司](#item-3) ⭐️ 8.0/10
4. [Intel EMIB-T 以 50% 成本优势挑战台积电 CoWoS](#item-4) ⭐️ 7.5/10
5. [澜起科技启动 CXL 3.2 MXC 芯片试生产](#item-5) ⭐️ 7.5/10
6. [Lumentum CEO 警告：磷化铟短缺将比内存危机更严重](#item-6) ⭐️ 7.5/10
7. [Valve 资助将开源 RADV Vulkan 驱动移植到 Windows 平台](#item-7) ⭐️ 7.5/10
8. [欧盟《人工智能法》8 月 2 日起执行，新增 AI 透明度要求](#item-8) ⭐️ 7.3/10
9. [CrossOver 宣布原生支持 Apple Silicon 以运行 Windows 游戏](#item-9) ⭐️ 7.3/10
10. [电梯调度算法的交互式探索](#item-10) ⭐️ 7.0/10
11. [qm – 工作的多智能体协作框架](#item-11) ⭐️ 7.0/10
12. [Golang 提案：为 container/ 包添加泛型集合类型](#item-12) ⭐️ 7.0/10
13. [CoWoS-S 与 CoWoS-R 的区别](#item-13) ⭐️ 7.0/10
14. [大型科技公司在 AI 基础设施上的支出超过 1 万亿美元——仅 2026 年预计还将增加 7450 亿美元](#item-14) ⭐️ 6.5/10
15. [基于浏览器的流式二维码以约 190 KB/s 速度传输数据](#item-15) ⭐️ 6.5/10
16. [单条 DDR5 内存的游戏性能比你想象的更好——单条 DDR5 击败双通道 DDR4 内存，AMD 3D V-Cache 处理器使用单条内存时性能下降不到 3%](#item-16) ⭐️ 6.5/10
17. [大多数主板 M.2 SSD 散热片与 SSD 接触不良](#item-17) ⭐️ 6.5/10
18. [MSI 高效模式为现有 DDR5 内存带来 EXPO ULL 式调优](#item-18) ⭐️ 6.5/10
19. [最前线｜武汉建成全国首个超大城市全域低空遥感监测网络，146 座无人机机场构建"城市智眼"](#item-19) ⭐️ 6.3/10
20. [电投产融：山东莱阳核电项目获国务院常务会议核准](#item-20) ⭐️ 6.3/10

---

<a id="item-1"></a>
## [Tailscale 发布关于 Hugging Face 入侵事件的透明事后分析](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 8.0/10

Tailscale 发布了一份关于 Hugging Face 安全入侵事件的详细事后分析报告，披露攻击者利用泄露的 Tailscale 可复用授权密钥（在被盗的 136 个凭据之一）几天内在 Hugging Face 的 tailnet 中注册了 181 个恶意节点，每个节点都获得了 CI 级别的访问权限。尽管 Tailscale 产品本身不存在漏洞，但该公司仍将此事件视为自身的责任。 此次事件凸显了像可复用授权密钥这类长期存在且权限范围过广的凭据的危险性，并为安全厂商在工具并非漏洞根源时仍主动承担责任树立了值得关注的先例。它也强化了在 CI/CD 和沙箱环境中对机器身份进行权限范围限制、轮换和监控的最佳实践。 这 181 个恶意节点各自携带一个 Tailscale 身份标签，享有完整的 CI 节点访问权限，这意味着该授权密钥实际上没有任何范围限制。Tailscale 建议采用更严格的范围控制（例如将密钥绑定到特定的机器标签或属性）、缩短凭据生命周期，并针对异常的节点注册行为设置告警。

hackernews · bluehatbrit · 7月31日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49127306)

**背景**: Tailscale 是一款基于 WireGuard 构建的零配置网状 VPN，允许设备无需复杂网络配置即可安全互联。授权密钥（auth key）是 Tailscale 用于在无需交互式登录的情况下注册新节点的机制，分为一次性使用和可复用两种类型，其中可复用密钥专为 CI 流水线等需要配置多个临时机器的场景设计。Hugging Face 是一个托管模型、数据集和应用程序的大型 AI/ML 平台，其运行大规模的 CI/CD 基础设施来测试和验证贡献内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailscale">Tailscale - Wikipedia</a></li>
<li><a href="https://tailscale.com/docs/features/access-control/auth-keys">Auth keys · Tailscale Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户高度赞扬 Tailscale 的透明度以及在产品不存在漏洞的情况下仍发布事后分析的勇气。Simon Willison 指出，几天内注册 181 个节点本应触发明显的告警机制，而 angry_octet 则补充说长期凭据本应被绑定到来源/目的地，并限定在具有 'ci_node' 等特定机器属性的范围内。也有一些怀疑者，如 ahofmann，将这篇博文部分视为'高明的营销手段'——但即便是批评者也承认这种承担责任的态度实属罕见。

**标签**: `#security`, `#incident-response`, `#vpn`, `#credentials`, `#post-mortem`

---

<a id="item-2"></a>
## [CEA-Leti 推进 3D 堆叠路线图，应对 AI 遭遇的内存与功耗瓶颈](https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/) ⭐️ 8.0/10

CEA-Leti 阐述了其在 3D 堆叠和小芯片方面的路线图，旨在解决限制 AI 算力扩展的内存和功耗瓶颈问题。

rss · EE Times · 7月31日 15:48

**标签**: `#AI hardware`, `#3D stacking`, `#chiplets`, `#semiconductor packaging`, `#memory wall`

---

<a id="item-3"></a>
## [Zoox 成为首家获批真正无人驾驶 robotaxi 的公司](https://www.electronicsweekly.com/news/business/first-genuine-driverless-2026-07/) ⭐️ 8.0/10

亚马逊旗下的 Zoox 成为首家获得监管批准、可以部署真正无人驾驶 robotaxi 的公司，获准在两年内在美国每年部署最多 2,500 辆自动驾驶车辆。 这是自动驾驶汽车行业的一个里程碑式监管突破，它超越了此前在有限区域内提供无人驾驶服务的模式，向更大规模地商业部署完全无人类操作员的车辆迈出了关键一步。 Zoox 的车辆采用独特的双向对称设计，没有方向盘，配有可容纳四名乘客的马车式座椅，配备了 360 度传感器套件和定制的气囊系统。但此次批准仍然限定在特定运行设计域（ODD）内，而非不受限制的 Level 5 完全自动驾驶。

rss · Electronics Weekly · 7月31日 05:10

**背景**: SAE 将车辆自动化划分为六个等级，从 Level 0（无自动化）到 Level 5（在任何条件下完全自主，不受地理围栏限制）。Zoox 此次获得的批准对应 Level 4，即车辆在特定区域或特定条件下能够自行驾驶，无需人类驾驶员。在美国，国家公路交通安全管理局（NHTSA）负责为不符合传统安全标准（如必须配备方向盘或踏板）的车辆授予联邦机动车安全标准（FMVSS）豁免。Waymo 于 2020 年在有限地理区域内率先推出了商业化无人驾驶出行服务，但 Zoox 的获批因其专用车辆设计（完全不设手动控制装置）而具有不同意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nvidia-zoox-autonomous-ride-hailing/">NVIDIA and Zoox Pave the Way for Autonomous Ride-Hailing | NVIDIA Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-driving_car">Self-driving car - Wikipedia</a></li>
<li><a href="https://www.usatoday.com/story/cars/research/reviews/2026/05/11/zoox-vs-waymo-tesla-amazon-robotaxi-differences/89981647007/">We tried Zoox, Amazon's robotaxi. How it stands out compared to Waymo, Tesla</a></li>

</ul>
</details>

**标签**: `#autonomous-vehicles`, `#robotaxi`, `#Zoox`, `#regulation`, `#Amazon`

---

<a id="item-4"></a>
## [Intel EMIB-T 以 50% 成本优势挑战台积电 CoWoS](https://www.techpowerup.com/351274/intels-emib-t-to-rival-tsmcs-cowos-with-50-cost-advantage-volume-production-in-2027) ⭐️ 7.5/10

据报道，Intel 搭载硅通孔（TSV）的 EMIB-T 先进封装技术正吸引包括 Broadcom 和 Meta 在内的外部客户考虑从台积电的 CoWoS 转向 EMIB，以将成本降低最多 50%。据台湾 PCB 与硅基板制造商欣兴电子（Unimicron）透露，Intel 的 EMIB-T 将于 2027 年进入量产阶段，在此期间 Intel 正在加快其标准版 EMIB 和 Foveros 的产能爬坡。 这一进展直接缓解了制约 AI 芯片供应的先进封装瓶颈，因为台积电的 CoWoS 产能已成为 AI 加速器交付的硬性约束。如果 EMIB-T 能够如期实现其所承诺的成本优势，将为 ASIC 设计公司和超大规模云厂商提供一个可行的替代供应来源，可能重塑整个 AI 基础设施供应链的定价格局。 EMIB-T 变体特别集成了 TSV，使 ASIC 能够直接获取电力连接，从而在单个封装上实现数千瓦级别的解决方案——这是搭配高带宽内存（HBM）的 AI 加速器的关键能力。与 CoWoS-L 或 CoWoS-R 相比的 50% 成本差距取决于是否需要昂贵的硅中介层，因为 EMIB 使用局部硅桥而非全尺寸硅中介层。

rss · TechPowerUp News · 7月31日 17:51

**背景**: 先进封装是将多个芯片裸片（chiplet）和高带宽内存组合成单一成品单元的工艺，对于 AI 处理器而言，其重要性已不亚于前沿晶圆制造工艺。台积电的 CoWoS（Chip-on-Wafer-on-Substrate，芯片-晶圆-基板）目前是将 AI 加速器裸片与 HBM 堆栈组合的主流技术，其有限的产能已造成供应瓶颈。Intel 的 EMIB（Embedded Multi-die Interconnect Bridge，嵌入式多芯片互连桥）是一种竞争性的 2.5D 方案，将小型硅桥嵌入封装基板中实现局部高密度裸片间互连，避免了全尺寸硅中介层的成本和面积开销。硅通孔（TSV）是贯穿整个硅裸片的垂直电连接，可实现 3D 堆叠和直接电力传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semiwiki.com/wikis/industry-wikis/intel-emib-embedded-multi-die-interconnect-bridge/">Intel EMIB (Embedded Multi-die Interconnect Bridge) - Semiwiki</a></li>
<li><a href="https://www.techtimes.com/articles/321754/20260728/ai-supply-crisis-moves-upstream-advanced-packaging-becomes-binding-constraint.htm">AI Supply Crisis Moves Upstream: Advanced Packaging Becomes the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Through-silicon_via">Through - silicon via - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#advanced-packaging`, `#Intel`, `#TSMC`, `#AI-infrastructure`

---

<a id="item-5"></a>
## [澜起科技启动 CXL 3.2 MXC 芯片试生产](https://www.techpowerup.com/351268/montage-technology-enters-trial-production-of-cxl-3-2-mxc-chip-supporting-8000-mt-s-ddr5) ⭐️ 7.5/10

澜起科技（Montage Technology）已启动业界首款 CXL 3.2 内存扩展控制器（MXC）芯片的试生产，该芯片符合 CXL Type 3 规范，并支持 CXL.mem 和 CXL.io 协议。该芯片集成了双通道 DDR5 内存控制器，支持高达 8000 MT/s 的 DDR5 速率，并通过 PCIe 6.x 提供 64 GT/s 的数据传输速率。 这是首款进入试生产阶段的 CXL 3.2 MXC 芯片，使澜起科技在面向 AI 和数据中心工作负载的下一代内存扩展领域占据先发优势，而这些场景中内存容量与带宽是关键瓶颈。CXL 3.2、PCIe 6.x 与 8000 MT/s DDR5 的结合，满足了超大规模和 AI 基础设施对内存池化、解耦与资源共享日益增长的需求。 MXC 充当桥接芯片，将主机端的 CXL 内存请求实时转换为 DDR 命令，从而突破传统服务器的内存容量限制。然而，该公告仅涉及试生产阶段，未披露具体产量、客户或正式供货时间表，且作为新闻稿也缺乏独立的基准测试数据。

rss · TechPowerUp News · 7月31日 15:07

**背景**: Compute Express Link（CXL）是基于 PCIe 构建的高速互连标准，可实现 CPU 与加速器或附加设备之间的内存一致性共享。CXL Type 3 设备专门提供内存扩展与池化功能，使服务器能够访问超出其直连容量限制的额外 DRAM。CXL 3.2 规范由 CXL 联盟于 2024 年 12 月发布，在保持向后兼容的同时增强了 CXL 内存设备的安全性与功能性。澜起科技此前就已是该领域的先驱，推出了业界首款 CXL Type 3 内存扩展控制器，而这款新芯片将其领先地位延伸到了 CXL 3.2 世代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.montage-tech.com/MXC">CXL® Memory eXpander Controller ( MXC ) | Montage Technology</a></li>
<li><a href="https://computeexpresslink.org/wp-content/uploads/2024/12/CXL_3.2-Spec-Announcement_FINAL-1.pdf">CXL Consortium Announces Compute Express Link 3 . 2 Specication...</a></li>
<li><a href="https://www.design-reuse.com/news/202529287-cxl-3-1-mxc-and-the-future-of-data-center-memory-architecture/">CXL 3.1 MXC and the Future of Data Center Memory Architecture</a></li>

</ul>
</details>

**标签**: `#CXL`, `#DDR5`, `#data-center`, `#memory-expansion`, `#AI-infrastructure`

---

<a id="item-6"></a>
## [Lumentum CEO 警告：磷化铟短缺将比内存危机更严重](https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory) ⭐️ 7.5/10

在 RAISE 峰会上，Lumentum CEO Michael Hurlston 警告称，作为硅光子技术关键材料的磷化铟（InP）正面临比当前内存短缺更严重的供应紧缩，随着共封装光学（CPO）需求加速增长，目前的产能已比客户需求低约 30%。 这一警告直接威胁到 AI 基础设施的扩展，因为共封装光学对于 AI 加速器和交换机之间的高带宽、低功耗数据传输日益重要。磷化铟晶圆的瓶颈可能会在 AI 算力需求爆发的关键时刻，制约下一代数据中心的建设。 CEO 的声明将磷化铟短缺与已广为人知的内存供应危机相提并论甚至更为严重，并且明确指出瓶颈在于晶圆厂和材料产能，而非需求端的问题。Lumentum 是最大的磷化铟基激光器和光子组件供应商之一，因此这是来自供应链关键节点的直接评估。

rss · Tom's Hardware · 7月31日 12:45

**背景**: 磷化铟（InP）是一种 III-V 族化合物半导体，用作高速光电器件的衬底，包括在光通信所需波长下高效工作的激光二极管和光电探测器。硅光子技术将这些基于 InP 的光源与硅波导结合，实现在芯片上和芯片之间的光学数据传输。共封装光学（CPO）是一种新兴架构，将光学引擎直接与交换机 ASIC 或计算芯片（如 AI 加速器）集成在同一封装内，与传统的可插拔光模块相比，显著提高了带宽密度和能效——对于扩展 AI 数据中心互连至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indium_phosphide">Indium phosphide - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Silicon_photonics">Silicon photonics - Wikipedia</a></li>
<li><a href="https://www.corning.com/optical-communications/worldwide/en/home/the-signal-network-blog/corning-and-broadcom-co-packaged-optics.html">Unlock the Future of AI | Co - Packaged Optics ( CPO )... | Corning</a></li>

</ul>
</details>

**标签**: `#silicon-photonics`, `#supply-chain`, `#semiconductors`, `#co-packaged-optics`, `#AI-infrastructure`

---

<a id="item-7"></a>
## [Valve 资助将开源 RADV Vulkan 驱动移植到 Windows 平台](https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2) ⭐️ 7.5/10

Valve 正在资助将 Mesa 项目中开源的 Linux RADV Radeon Vulkan 驱动移植到 Windows 平台。该跨平台构建版本已经能够运行《反恐精英 2》。 这代表着向跨平台开源 GPU 驱动迈进的重大一步，有望减少 Mesa 与 Windows 图形栈之间的重复开发。它可能为 Windows 上的 AMD Radeon GPU 用户提供一种开源驱动方案，替代 AMD 专有的 Adrenalin 软件，并体现了 Valve 对开放图形技术的持续承诺。 RADV 是一个用户态驱动，编译为共享库——Linux 上是 libvulkan_radeon.so，相当于 Windows 上的.dll——并支持 AMD GCN/RDNA 架构 GPU，提供完整的 Vulkan API 支持。《反恐精英 2》已经能在 Windows 移植版本上运行，这一事实证明了该跨平台工作的实际可行性。

rss · Tom's Hardware · 7月31日 12:25

**背景**: RADV 是 AMD Radeon GPU 的开源 Vulkan 驱动，作为 Mesa 3D 图形库的一部分开发——Mesa 是一个历史悠久的开源图形项目，实现了包括 OpenGL、Vulkan、OpenCL 和 Direct3D 在内的多种图形 API。Vulkan 本身是一种底层图形 API，旨在提供比 OpenGL 和 DirectX 11 等旧 API 更高的性能和更高效的 CPU/GPU 利用率。Windows 上的 AMD 用户目前主要依赖 AMD 专有的 Adrenalin 驱动，而 Linux 用户则可以同时使用 AMD 官方的 AMDVLK 驱动和开源的 RADV 驱动。此次移植工作旨在统一跨平台的驱动开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.mesa3d.org/drivers/radv.html">RADV — The Mesa 3D Graphics Library latest documentation</a></li>
<li><a href="https://wccftech.com/mesa-radv-vulkan-driver-amd-radeon-gpus-vulkan-video-h264-h265-encode-support/">MESA RADV Vulkan Driver For AMD Radeon GPUs Gets Vulkan ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulkan">Vulkan - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Vulkan`, `#RADV`, `#Mesa`, `#Valve`, `#open-source-drivers`

---

<a id="item-8"></a>
## [欧盟《人工智能法》8 月 2 日起执行，新增 AI 透明度要求](https://36kr.com/newsflashes/3919473270812290?f=rss) ⭐️ 7.3/10

欧盟委员会 7 月 31 日宣布，自 8 月 2 日起，欧盟委员会人工智能办公室将与各成员国主管部门共同开始执行《人工智能法》相关规定。新规要求聊天机器人等交互式人工智能系统向用户明确披露其人工智能身份，利用人工智能生成或编辑的深度伪造图片、视频和音频内容必须进行标识，并添加机器可识别标记以便识别和追踪。 这标志着全球最全面的 AI 监管法规进入实质性执行阶段，立即影响在欧盟部署 AI 系统的开发者和企业，无论其总部位于何处。这些透明度要求旨在打击欺骗和操纵行为，同时为全球 AI 治理树立标杆，可能影响其他司法管辖区的监管思路。 根据《人工智能法》第 50 条，相关系统必须添加机器可读标记（如水印或 C2PA 等元数据方案），以便通过算法识别 AI 生成内容，而非仅依赖视觉披露。《人工智能法》采用基于风险的分级框架，将 AI 系统分为四个风险等级，8 月 2 日生效的规定主要针对通用 AI 交互和合成媒体的透明度要求。

rss · 36氪 · 7月31日 11:45

**背景**: 欧盟《人工智能法》是全球首部针对人工智能的综合性横向监管立法，采用基于风险的方法，将 AI 系统按风险高低分为四个等级，并对应不同的合规义务。第 50 条专门规定了与用户交互、生成合成内容或支持深度伪造的 AI 系统的透明度义务。Google 的 SynthID 和 C2PA 内容溯源标准等技术方案提供了在 AI 生成媒体中嵌入机器可读标记的机制，多种此类标准有望成为企业满足合规要求的主流方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/">Artificial intelligence act - Consilium</a></li>
<li><a href="https://sota.io/blog/eu-ai-act-art50-transparency-watermarking-developer-guide-2026">EU AI Act Art.50 Transparency & Watermarking ... — sota.io Blog</a></li>
<li><a href="https://www.pragma-code.de/en/blog-synthid-ai-watermarking-content-provenance">SynthID & Co: AI Watermarking & Content ... | Pragma-Code Blog</a></li>

</ul>
</details>

**标签**: `#EU AI Act`, `#AI Regulation`, `#AI Transparency`, `#Compliance`, `#Policy`

---

<a id="item-9"></a>
## [CrossOver 宣布原生支持 Apple Silicon 以运行 Windows 游戏](https://www.solidot.org/story?sid=84978) ⭐️ 7.3/10

CrossOver 发布了首个原生支持 Apple Silicon 的预览版，可在 macOS 上运行 x86 Windows 游戏，这是 Apple Silicon 发布六年来的重要里程碑。此外，Arch Linux 在攻击者通过正常领养流程劫持超过 400 个软件包并植入恶意代码后，关闭了 AUR 孤儿包的领养功能。 CrossOver 的原生支持正值苹果计划在 macOS 28 中淘汰 Rosetta 2 的关键节点，否则 Mac 用户将失去运行 Windows 游戏的可行途径。Arch Linux 的 AUR 事件则暴露了社区维护软件仓库中持续存在的供应链风险，促使平台采取更严格的审核策略。 该预览版仍存在一些问题，目前仅推荐用于测试；由于 ARM64 版 D3DMetal 尚未就绪，DirectX 11 游戏目前只能通过 DXMT ARM64 运行。这些问题预计将在 CrossOver 27 正式版中得到解决。CrossOver 背后的 CodeWeavers 公司贡献了 Wine 项目 90% 以上的代码，同时也是 Steam Proton 的开发者。

rss · Solidot · 7月31日 14:32

**背景**: Wine 是一个开源兼容层，与虚拟机不同，它在运行时直接将 Windows API 调用翻译为主机操作系统调用，从而实现在 Linux 和 macOS 上运行 Windows 游戏。Apple 的 Rosetta 2 历来用于将 x86 软件翻译到 ARM 架构的 Mac 上运行，而像 D3DMetal 和 DXMT 这类 Apple Silicon 专用翻译层则将 Direct3D 调用映射到 Apple 的 Metal 图形接口，以获得更好的性能。Arch User Repository（AUR）是 Arch Linux 的社区驱动仓库，包含用户提交的构建脚本（PKGBUILD），任何注册用户都可以领养孤儿包——这种信任模型在本次攻击中遭到利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.solidot.org/story?sid=84978">奇客Solidot | Windows 游戏模拟器 CrossOver 宣布原生 Apple Silicon ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/400-aur-packages-hijacked-atomic-arch-campaign">400+ AUR Packages Hijacked: What the “Atomic Arch ”... - StepSecurity</a></li>
<li><a href="https://secure-os.org/articles/is-the-aur-safe/">Is the AUR Safe? Lessons from the 'Atomic Arch ' Supply - Chain ...</a></li>
<li><a href="https://j0.lol/blog/kegworks-winery/">How to run games on macOS like it's SteamOS</a></li>

</ul>
</details>

**标签**: `#CrossOver`, `#Apple Silicon`, `#Wine`, `#macOS`, `#Arch Linux`, `#supply-chain-security`

---

<a id="item-10"></a>
## [电梯调度算法的交互式探索](https://john.fun/elevators) ⭐️ 7.0/10

john.fun/elevators 上的文章提供了一个电梯调度算法的交互式可视化，引发了一场高度活跃的讨论（901 分，223 条评论），评论者将电梯逻辑与磁盘调度联系起来，分享了目的选层派梯系统的真实使用体验，并推荐了 Elevator Saga 等教育工具。 电梯调度是一个经典的计算机科学问题，它优雅地展示了队列管理和请求排序如何影响真实世界系统。这场跨领域的丰富讨论（将电梯与磁盘、游戏设计和建筑基础设施联系起来）使其成为算法思维教学中一个异常有效的载体。 文章涵盖的关键算法包括 FCFS、SSTF、SCAN、LOOK 和 C-SCAN，这些算法起源于磁盘调度研究，但可直接映射到电梯行为上。SCAN 算法通过沿一个方向移动来处理请求，然后反转方向；而 LOOK 算法通过在最后一个请求处停止而不是到达磁盘末端来提高效率。

hackernews · Jrh0203 · 7月31日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49124218)

**背景**: 电梯算法（也称为 SCAN）最初是一种磁盘调度策略，磁盘臂来回移动来处理读写请求，就像电梯处理楼层呼叫一样。常见的变体包括 LOOK（在最后一个请求处反转而不是磁盘末端）和 C-SCAN（始终返回起始位置以提供更公平的服务）。目的选层派梯（Destination Dispatch）是一种现代电梯技术，乘客在大厅的终端选择楼层并被分组到特定的电梯轿厢中，而不是在电梯内按按钮。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elevator_algorithm">Elevator algorithm - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/operating-systems/disk-scheduling-algorithms/">Disk Scheduling Algorithms - GeeksforGeeks</a></li>
<li><a href="https://medium.com/@dmkaban62/diving-into-go-implementing-classic-elevator-scheduling-algorithms-fcfs-sstf-scan-and-look-4040c2de62f2">Diving into Go: Implementing Classic Elevator Scheduling ... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区讨论内容丰富且跨学科。评论者 peterldowns 形象地将硬盘比作一根长长的、缠绕在主轴上的电梯，并指出 SCAN 本质上是一种磁盘调度算法。Omoikane 分享了在办公楼中使用目的选层派梯系统的真实经验，质疑模拟结果是否取决于交通模式。Brandonpelfrey 分享了 Elevator Saga 作为实践编程练习。Hermanschaaf 描述了开发《Sky Lobby》（一款关于电梯自动化的手机游戏）的过程，并选择 LOOK 作为最直观的默认算法。Olex 幽默地指出，电梯设计中最难的部分是用户同时按下上下两个按钮。

**标签**: `#algorithms`, `#simulation`, `#computer-science`, `#elevator`, `#education`

---

<a id="item-11"></a>
## [qm – 工作的多智能体协作框架](https://github.com/yc-software/qm) ⭐️ 7.0/10

一款由 YC 投资的开源框架，用于在工作场景中协调多个 AI 智能体协作完成任务，进入与 Cowork 和 Buzz 等工具竞争的多智能体协作市场。

hackernews · tosh · 7月31日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=49126604)

**标签**: `#ai-agents`, `#multi-agent-systems`, `#developer-tools`, `#yc`, `#agent-orchestration`

---

<a id="item-12"></a>
## [Golang 提案：为 container/ 包添加泛型集合类型](https://github.com/golang/go/issues/80590) ⭐️ 7.0/10

一项新的 Go 提案（issue #80590）建议在标准库的 container/ 包中添加泛型集合类型，例如集合（set）和类型化堆（typed heap）。这将填补自 Go 1.18 引入泛型以来长期存在的空白，提供内置的类型化数据结构，而不再依赖第三方实现。 这之所以重要，是因为 Go 开发者长期以来一直需要标准库对常见泛型数据结构的支持，而不得不使用第三方包或自行编写。将这些类型加入标准库将减少生态碎片化、提高一致性，并标志着 Go 泛型生态走向更加成熟。 该提案专门针对 container/ 目录，该目录目前仅包含 list、ring 和 heap——这些都是在泛型之前实现的，依赖于 interface{} 或 any。该讨论获得了 128 个赞和 78 条评论，表明社区对塑造这些新类型的 API 设计和命名约定有强烈兴趣。

hackernews · jabits · 7月31日 18:39 · [社区讨论](https://news.ycombinator.com/item?id=49127031)

**背景**: Go 在 2022 年 3 月发布的 1.18 版本中引入了泛型（类型参数），使开发者能够编写类型安全、可复用的代码，且不牺牲性能。然而，标准库的 container/ 包——数据结构的所在地——早于泛型出现，仍然使用非泛型接口。集合等常见数据结构没有内置实现，迫使开发者使用 golang-set 等第三方库。container/ 包目前包含 container/list（双向链表）、container/ring（循环链表）和 container/heap（需要用户实现接口的堆）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pkg.go.dev/container">container / directory - container - Go Packages</a></li>
<li><a href="https://www.sobyte.net/post/2022-04/golang-container/">Go container package - SoByte</a></li>
<li><a href="https://blog.marcnuri.com/go-generics-introduction">Go Generics Tutorial: A Complete Introduction to Type Parameters ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，但也带着对拖延已久的失望感，有评论者称这是'迟到了 22 年'。几位用户表示赞同，但提出了设计方面的担忧，例如不要将变更方法混入 API 中。此外还有更广泛的讨论，关于 Go 当前的泛型实现是否足够，以及未来的'Go v2'是否需要在更基础的层面进行更改以更好地支持集合类型。

**标签**: `#golang`, `#generics`, `#standard-library`, `#data-structures`, `#language-design`

---

<a id="item-13"></a>
## [CoWoS-S 与 CoWoS-R 的区别](https://semiwiki.com/semiconductor-manufacturers/tsmc/371759-the-difference-between-cowos-s-and-cowos-r/) ⭐️ 7.0/10

比较台积电的两种 CoWoS 先进封装技术（CoWoS-S 和 CoWoS-R），用于在单个封装中集成处理器、小芯片和高带宽内存（HBM）。

rss · SemiWiki · 7月31日 13:00

**标签**: `#semiconductor-packaging`, `#TSMC`, `#CoWoS`, `#advanced-packaging`, `#HBM`

---

<a id="item-14"></a>
## [大型科技公司在 AI 基础设施上的支出超过 1 万亿美元——仅 2026 年预计还将增加 7450 亿美元](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone) ⭐️ 6.5/10

自 2023 年以来，亚马逊、谷歌、Meta 和微软在 AI 基础设施上的累计支出已超过 1 万亿美元，预计 2026 年还将再增加 7450 亿美元，而它们的隐性债务已超过 1.65 万亿美元。

rss · Tom's Hardware · 7月31日 16:30

**标签**: `#AI infrastructure`, `#big tech`, `#capital expenditure`, `#industry trends`, `#data centers`

---

<a id="item-15"></a>
## [基于浏览器的流式二维码以约 190 KB/s 速度传输数据](https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access) ⭐️ 6.5/10

一位开发者构建了一个基于浏览器的概念验证方案，可在两部手机之间以 60 FPS 速度流式传输二维码，实现接近 190 KB/s 的数据传输速率，无需安装任何应用、无需联网、无需配对，且除相机权限外无需任何特殊授权。 该方案提供了一种零摩擦、注重隐私的短距离数据交换替代方案，适用于 Wi-Fi、蓝牙或 NFC 不可用或不可取的场景（如隔离网络或受限的企业网络）。它展示了利用现有 Web API 绕过传统连接需求的创造性思路，但吞吐量上限使其仅限于 URL、短文本或凭证等小负载场景。 该实现依赖浏览器的 getUserMedia API 访问摄像头，且必须在安全（HTTPS）上下文中运行。单个标准二维码最多可编码约 3 KB 的二进制数据，因此系统将大量二维码快速串联播放；60 FPS 的帧率和约 190 KB/s 的吞吐量是受相机曝光、解码延迟和二维码版本密度限制的实际上限。

rss · Tom's Hardware · 7月31日 12:45

**背景**: 二维码（Quick Response Code）是一种二维条码，可在黑白模块的网格中存储二进制或字母数字数据；最大的标准化版本（Version 40）单个可容纳约 2,953 字节的二进制数据。由于单个二维码容量有限，研究人员很早就开始探索“流式”或“动画”二维码——将一连串二维码像视频一样播放，由带摄像头的设备还原为更大的文件。浏览器的 getUserMedia API 可让网页访问设备摄像头而无需原生代码，从而可以完全在客户端解码这些流。QiFi（qifi-dev/qrs）和 Digital Bazaar 的 qram 等开源项目展示了流式二维码传输管道的先例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/qifi-dev/qrs">GitHub - qifi-dev/qrs: Stream data through multiple series of QR codes</a></li>
<li><a href="https://digitalbazaar.github.io/qram/">qram | Cram arbitrarily large data into multiple streaming QR - codes</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia">MediaDevices: getUserMedia () method - Web APIs | MDN</a></li>

</ul>
</details>

**标签**: `#data-transfer`, `#qr-codes`, `#browser-based`, `#proof-of-concept`, `#privacy`

---

<a id="item-16"></a>
## [单条 DDR5 内存的游戏性能比你想象的更好——单条 DDR5 击败双通道 DDR4 内存，AMD 3D V-Cache 处理器使用单条内存时性能下降不到 3%](https://www.tomshardware.com/pc-components/ddr5/single-dimm-ddr5-gaming-works-better-than-you-probably-think-amds-3d-v-cache-chips-drop-less-than-3-percent-one-ddr5-dimm-beats-dual-channel-ddr4-ram) ⭐️ 6.5/10

基准测试显示，单条 DDR5 内存在游戏中的表现出人意料地好，常常能胜过双通道 DDR4，而 AMD 3D V-Cache 处理器在使用单条内存时性能损失不到 3%。

rss · Tom's Hardware · 7月31日 11:43

**标签**: `#DDR5`, `#RAM`, `#gaming-hardware`, `#AMD`, `#benchmarks`

---

<a id="item-17"></a>
## [大多数主板 M.2 SSD 散热片与 SSD 接触不良](https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify) ⭐️ 6.5/10

Tom's Hardware 测试了 20 款现代 Intel 和 AMD 主板的 M.2 SSD 散热片接触质量，发现其中只有 6 款主板能与 SSD 实现完全热接触，其余 14 款主板接触不良，意味着随附的散热片可能无法有效为 SSD 散热。 热接触不良会导致 NVMe SSD 触发热降频，在文件传输或内容创作等高负载场景下大幅降低持续写入性能。这对于那些默认主板自带散热片就能为高性能 SSD 提供足够散热的 PC 装机者和发烧友来说是个实际问题，可能影响 SSD 的速度和使用寿命。 热降频机制由 NVMe 1.0 规范中的主机控制热管理（HCTM）定义，典型表现是持续写入性能曲线在 10 至 60 秒后急剧下降。导热垫的质量和厚度以及散热片的设计公差是关键因素，质量差或厚度不匹配的导热垫反而会隔绝散热，使 SSD 温度更高。

rss · Tom's Hardware · 7月31日 11:43

**背景**: M.2 NVMe SSD 是一种紧凑型的高速存储设备，在持续写入时会产生大量热量。为此，NVMe 1.0 规范引入了主机控制热管理（HCTM）机制，允许 SSD 在温度超过安全阈值时自动降低性能。主板通常配备带导热垫的散热片来散热，但 SSD 主控芯片和 NAND 颗粒与散热片之间的良好接触对有效散热至关重要。由于导热垫厚度不匹配或散热片设计不合理导致的接触不良，会使 SSD 运行温度高于预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hagisol.com/techblog/?p=635">How NVMe SSD thermal throttling works HAGIWARA Solutions</a></li>
<li><a href="https://voltground.com/hardware/nvme-ssd-thermal-throttling/">NVMe SSD Thermal Throttling : How to Detect It, What... — VoltGround</a></li>
<li><a href="https://www.yourtechlist.com/best-m2-heatsinks/">10 Best M.2 Heatsinks For (August 2026)</a></li>

</ul>
</details>

**社区讨论**: 社区讨论聚焦于导热垫安装问题，包括在安装主板散热片前是否需要撕掉 SSD 出厂导热贴，以及单面 M.2 SSD 需要使用橡胶垫片等问题。发烧友们强调导热界面材料与散热片本身同等重要，建议使用知名厂商生产的优质导热垫，以避免出现隔绝而非散热的情况。

**标签**: `#hardware`, `#motherboards`, `#M.2 SSD`, `#thermal performance`, `#PC building`

---

<a id="item-18"></a>
## [MSI 高效模式为现有 DDR5 内存带来 EXPO ULL 式调优](https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram) ⭐️ 6.5/10

MSI 为其 AM5 主板发布了固件更新，在 Click BIOS X 中引入了高效模式（High-Efficiency Mode），可自动降低 DDR5 内存延迟，模拟 AMD 的 EXPO 超低延迟（ULL）配置文件，无需使用专门的 ULL 内存套件。 此次更新让现有 DDR5 用户——以及那些无力购买高价 EXPO ULL 套件的用户——无需购买新硬件即可获得大部分相同的游戏性能提升，在内存价格飞涨的时期让高级内存调优变得更加亲民。 MSI 内部测试显示，开启高效模式后延迟从 79.4 ns 降至 71.6 ns，与 AMD 宣称的 EXPO ULL 在标准 DDR5-6000 套件上减少 5–7 ns 的效果相当。该功能位于 MSI Click BIOS X 的超频部分，适用于 AM5 平台主板。

rss · Tom's Hardware · 7月31日 11:20

**背景**: AMD EXPO（Extended Profiles for Overclocking）是 AMD 在锐龙平台上用于一键 DDR5 内存超频的标准，类似于英特尔的 XMP。在 2026 年的 Computex 上，AMD 发布了 EXPO 超低延迟（ULL），这是一套更严格的配置文件，通过调整 tREFI、tRRDS、tWR 和 VDDP 电压等参数来降低内存延迟，承诺最高可带来 13% 的游戏性能提升。EXPO ULL 需要经过专门验证的内存套件，而这类套件在全球内存短缺期间已变得稀缺且昂贵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram">MSI promises an EXPO ULL-like boost for your existing DDR 5 memory...</a></li>
<li><a href="https://overclock3d.net/news/cpu_mainboard/msi-bring-amd-expo-ull-performance-to-standard-ddr5-memory-with-high-efficiency-mode/">MSI bring AMD EXPO ULL performance to standard DDR 5 memory...</a></li>
<li><a href="https://www-techpowerup-com.nproxy.org/349544/amd-unveils-the-expo-ull-ultra-low-latency-memory-profile-standard">AMD Unveils the EXPO - ULL ( Ultra Low - Latency ) Memory Profile...</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#MSI`, `#motherboards`, `#memory tuning`, `#AMD EXPO`

---

<a id="item-19"></a>
## [最前线｜武汉建成全国首个超大城市全域低空遥感监测网络，146 座无人机机场构建"城市智眼"](https://36kr.com/p/3919271016263303?f=rss) ⭐️ 6.3/10

武汉已建成全国首个超大城市全域低空无人机监测网络，部署 146 座无人机机场，可实现 5 分钟内全市域无人机响应，应用于交通管理、生态监测和城市治理。

rss · 36氪 · 7月31日 08:12

**标签**: `#low-altitude economy`, `#drones`, `#smart city`, `#urban governance`, `#DJI`

---

<a id="item-20"></a>
## [电投产融：山东莱阳核电项目获国务院常务会议核准](https://36kr.com/newsflashes/3919516325949059?f=rss) ⭐️ 6.3/10

中国国务院常务会议已核准山东莱阳核电项目，该项目将建设两台 CAP1400（第三代+）反应堆，总装机容量约 3,086 兆瓦，由电投产融开发。

rss · 36氪 · 7月31日 12:18

**标签**: `#nuclear-energy`, `#infrastructure`, `#china`, `#CAP1400`, `#energy-policy`

---