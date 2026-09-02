---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> 从 97 条内容中筛选出 20 条重要资讯。

---

1. [Anthropic 发布 Claude Fable 5.1 和 Claude Mythos 5.1，大幅降价](#item-1) ⭐️ 9.0/10
2. [Nvidia 通过可转换债券向 MediaTek 投资 35 亿美元](#item-2) ⭐️ 9.0/10
3. [Hot Chips 2026：三星公布三阶段 HBM 路线图，将逻辑与计算融入内存——zHBM 最终将 DRAM 直接堆叠在处理器上](#item-3) ⭐️ 8.5/10
4. [华硕和微星在 NVIDIA RTX Spark 笔记本上市前售罄首批库存](#item-4) ⭐️ 7.5/10
5. [索尼法律上辩称数字游戏所有权并不成立](#item-5) ⭐️ 7.5/10
6. [NVIDIA DLSS 5 现可在单张 RTX 50 显卡上运行，速度较三月提升 5 倍](#item-6) ⭐️ 7.5/10
7. [NVIDIA 重启 Rubin CPX GPU，搭载 HBM4 内存，弃用 GDDR7](#item-7) ⭐️ 7.5/10
8. [NVIDIA GPU 帧插值功能通过 Vulkan API 集成至 FFmpeg](#item-8) ⭐️ 7.5/10
9. [Nvidia 颇具争议的 DLSS 5 将于 9 月 3 日随 NBA2K27 一同发布，公司分享首批基准测试成绩——支持所有 RTX 50 系列 GPU、笔记本及 GeForce NOW](#item-9) ⭐️ 7.5/10
10. [中国法院冻结安世半导体 3.18 亿美元资产，闻泰科技力图夺回控制权——荷兰芯片商称查封不影响日常运营](#item-10) ⭐️ 7.5/10
11. [消息称长鑫存储启动 HBM3E 内存风险试产，实现中国 DRAM 产业突破——公司有望 2027 年实现量产](#item-11) ⭐️ 7.5/10
12. [Linux 内核每版本漏洞逼近 2000 个纪录，AI 漏洞猎人扫描 4000 万行代码——维护者称被 CVE 发现“完全压垮”](#item-12) ⭐️ 7.5/10
13. [新型 iPSJ GaN-on-Si 晶体管击穿电压接近 4kV](#item-13) ⭐️ 7.5/10
14. [Softaculous 遭遇长达 33 小时的 BGP 路由劫持](#item-14) ⭐️ 7.3/10
15. [Dan Luu 严格审视 Ed Zitron 的 AI 怀疑论预测](#item-15) ⭐️ 7.0/10
16. [Show HN：在 48GB Mac 上以约 12 tok/s 的速度运行 104GB 的 Qwen3.8-Flash-Next 模型](#item-16) ⭐️ 7.0/10
17. [前五大企业级 SSD 厂商 2026 年第二季度营收逼近 375.9 亿美元](#item-17) ⭐️ 7.0/10
18. [John Ternus 正式出任苹果新任 CEO](#item-18) ⭐️ 6.5/10
19. [NVIDIA 在 Hot Chips 2026 展示 CUDA 支持 RISC-V 及 NVLink Fusion 集成](#item-19) ⭐️ 6.5/10
20. [评论文章力陈 Firefox 对浏览器引擎多样性的必要性](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Fable 5.1 和 Claude Mythos 5.1，大幅降价](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1，进行大幅降价（缓存读取价格从 $1/M 降至 $0.25/M），写作质量得到提升，科学能力也有所增强。Claude Mythos 5.1 与 Fable 5.1 技术上完全相同，但对从事网络安全和生命科学工作的受认证机构提供了更宽松的安全限制。 缓存读取价格降低 75% 为整个 LLM 行业的定价设置了新的上限，并使顶级 AI 能力在长上下文应用中变得更加容易获取。作为高于 Opus 的旗舰模型级别，Fable 5.1 在长时间智能体任务和编程方面的改进可能会重塑主要 AI 实验室之间的竞争格局。 Claude Mythos 5.1 由于对网络安全和生命科学工作提供了更宽松的安全限制，仅限通过受信任的访问项目获取。一些用户指出，移除可视化思维链降低了提示调试能力，且在 Terminal-Bench-Science 0.1 等科学专项测试之外的基准测试改进似乎不太显著。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**背景**: Claude 是 Anthropic 的旗舰大语言模型家族，按能力分为不同等级：Haiku（小型）、Sonnet（中型）、Opus（大型）和 Fable/Mythos（最强，面向智能体任务）。Fable 5 于 2026 年 6 月发布，Fable 5.1 大约三个月后作为增量更新推出。Mythos 版本专为需要访问通常因安全原因而受限能力的受认证机构设计，主要应用于网络安全和生命科学领域。"缓存读取"是一种成本优化技术，通过缓存重复的提示前缀来避免重复计算，是长上下文应用中常见的定价机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://kie.ai/blog/what-is-claude-fable-5-1">What Is Claude Fable 5 . 1 ? Mythos -Class Claude Explained</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一。一位 Anthropic 员工强调写作风格和科学能力方面的提升是突出亮点，Simon Willison 则提供了详细的技术分析，包括用鹈鹕主题的 SVG 渲染器来衡量不同思考力度等级（低、中、高、超高）。批评者质疑基准测试是否显示出有意义的实际改进，指出移除可视化思维链会影响调试工作流，并认为大幅降价意味着 Anthropic 在原价上难以销售 Fable，暗示前沿 LLM 定价存在市场上限。

**标签**: `#anthropic`, `#claude`, `#llm-release`, `#ai-models`, `#pricing`

---

<a id="item-2"></a>
## [Nvidia 通过可转换债券向 MediaTek 投资 35 亿美元](https://www.electronicsweekly.com/news/business/nvidia-2-2026-09/) ⭐️ 9.0/10

Nvidia 将购买 MediaTek 价值 35 亿美元的可转换债券，两家公司承诺将彼此的产品整合进各自的生态系统中。作为扩展合作的一部分，MediaTek 将向设计定制 XPU 的客户开放 Nvidia 的 NVLink Fusion 平台，同时 Nvidia 的网络生态系统也将纳入 MediaTek 的供应链。 该交易是近年来规模最大的战略半导体投资之一，表明 Nvidia 正大力推动将其专有的互联技术（NVLink Fusion）深度嵌入定制 AI 加速器市场，从而更难被竞争对手取代。这笔交易显著强化了 MediaTek 在 AI 基础设施、边缘计算和汽车平台领域的地位，同时也为 Nvidia 在传统代工/无晶圆厂模式之外争取到一位利益深度绑定的合作伙伴。 该投资以可转换债券而非直接股权的形式进行，使 Nvidia 通过固定利息支付获得下行保护，同时保留通过转换为 MediaTek 股票获得上行收益的潜力。NVLink Fusion 是一项半定制 AI 基础设施技术，允许合作伙伴使用 MGX 机架级架构，将其定制的 XPU 和 CPU 集成到 Nvidia 的纵向扩展（scale-up）与横向扩展（scale-out）技术栈中。

rss · Electronics Weekly · 9月1日 05:16

**背景**: Nvidia 的 NVLink 是一种高带宽互联技术，可将 GPU（如今也包括其他加速器）连接成统一的计算 fabric，而 NVLink Fusion 则将此 IP 扩展给第三方芯片设计者，使其定制的 XPU 能够接入 Nvidia 的 AI 平台。XPU 是定制 AI 加速器芯片——不同于通用的 CPU 和 GPU——由超大规模云厂商和无晶圆厂设计商针对特定 AI 工作负载打造。可转换债券是一种混合金融工具：它支付常规债券利息，但可按约定比例转换为发行方的普通股，使投资者在获得类似债券的风险保护的同时享有类似股权的上行收益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-and-mediatek-deepen-long-standing-partnership-to-build-ai-edge-to-cloud-computing-platforms">NVIDIA and MediaTek Deepen Long-Standing... | NVIDIA Newsroom</a></li>
<li><a href="https://www.investopedia.com/terms/c/convertiblebond.asp">Understanding Convertible Bonds: Definition, Examples, and Key Benefits</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#MediaTek`, `#semiconductors`, `#strategic-investment`, `#networking`

---

<a id="item-3"></a>
## [Hot Chips 2026：三星公布三阶段 HBM 路线图，将逻辑与计算融入内存——zHBM 最终将 DRAM 直接堆叠在处理器上](https://www.tomshardware.com/tech-industry/semiconductors/hot-chips-2026-samsung-reveals-a-three-phase-hbm-roadmap-that-puts-logic-and-compute-inside-memory-zhbm-ultimately-stacks-dram-directly-on-top-of-the-processor) ⭐️ 8.5/10

三星在 Hot Chips 2026 上公布三阶段 HBM 路线图，逐步将逻辑集成到基底裸片，最终通过 zHBM 把 DRAM 直接堆叠在处理器上。

rss · Tom's Hardware · 9月1日 11:06

**标签**: `#HBM`, `#Samsung`, `#semiconductors`, `#memory-architecture`, `#HotChips2026`

---

<a id="item-4"></a>
## [华硕和微星在 NVIDIA RTX Spark 笔记本上市前售罄首批库存](https://www.techpowerup.com/352237/taiwanese-hardware-manufacturers-sell-out-nvidia-rtx-spark-laptop-stock-ahead-of-launch) ⭐️ 7.5/10

华硕和微星在正式上市前便售罄了首批共 10 万台搭载 NVIDIA RTX Spark（采用与联发科联合研发的 N1/N1x ARM SoC）的笔记本电脑，据报道 NVIDIA 计划将下一批产量提升至 30 万至 50 万台，预计起售价约为 3,500 美元。 仅两家 OEM 便在上市前售罄 10 万台，表明渠道对 NVIDIA ARM 笔记本平台的需求强劲，验证了其相对于高通骁龙 X Elite 的竞争定位。将产量扩大至 30 万至 50 万台的计划则显示 NVIDIA 认真投入高端 ARM 笔记本市场的商业决心。 RTX Spark 笔记本将 NVIDIA Blackwell GPU 与联发科的高能效 SoC 设计相结合，面向高端用户，支持本地大语言模型推理等设备端 AI 工作负载。台湾市场约 3,500 美元的起售价可能会限制其向主流市场普及，而戴尔、惠普、联想和微软等其他首发合作伙伴获得的芯片配额尚未披露。

rss · TechPowerUp News · 9月1日 19:12

**背景**: ARM 处理器采用精简指令集，专为能效优化而设计，这也是它们在移动设备中占据主导、并越来越多地出现在追求长续航的笔记本中的原因。片上系统（SoC）将 CPU、GPU 及其他关键组件集成在单一芯片上，从而降低功耗并缩小物理尺寸。NVIDIA 与联发科在既有合作的基础上进一步深化，将 NVIDIA 的加速计算、AI 和图形平台与联发科在定制芯片和高能效 SoC 设计方面的专长相结合，打造出为 RTX Spark 笔记本提供算力的 N1/N1x 芯片。该平台进入了一个目前由高通骁龙 X Elite 主导的高端 Windows-on-ARM 细分市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/352237/taiwanese-hardware-manufacturers-sell-out-nvidia-rtx-spark-laptop-stock-ahead-of-launch">Taiwanese Hardware Manufacturers Sell Out NVIDIA ... | TechPowerUp</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-and-mediatek-deepen-long-standing-partnership-to-build-ai-edge-to-cloud-computing-platforms">NVIDIA and MediaTek Deepen Long-Standing... | NVIDIA Newsroom</a></li>
<li><a href="https://www.lenovo.com/us/en/glossary/what-is-arm-architecture/">What Is ARM Architecture | ARM Processor Architecture | Lenovo US</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#ARM-laptops`, `#MediaTek`, `#hardware-launch`, `#PC-market`

---

<a id="item-5"></a>
## [索尼法律上辩称数字游戏所有权并不成立](https://www.techpowerup.com/352232/sony-legally-argues-that-digital-game-ownership-is-not-plausible) ⭐️ 7.5/10

在一项集体诉讼中，索尼援引其许可协议辩称，消费者不应期望真正拥有以数字方式购买的游戏，以此回应一起涉及加州信息披露法的投诉。

rss · TechPowerUp News · 9月1日 18:19

**标签**: `#digital-rights`, `#legal`, `#gaming`, `#consumer-protection`, `#software-licensing`

---

<a id="item-6"></a>
## [NVIDIA DLSS 5 现可在单张 RTX 50 显卡上运行，速度较三月提升 5 倍](https://www.techpowerup.com/352225/dlss-5-no-longer-needs-two-rtx-5090s-nvidia-says-model-is-5x-faster-since-march) ⭐️ 7.5/10

NVIDIA 在 DLSS 5 于 9 月 3 日随《NBA 2K27》正式上线前公布了其官方性能数据，展示了该神经渲染模型相比 3 月 GTC 首次亮相时速度提升达 5 倍——当时运行需要两块 RTX 5090 显卡。如今该技术已可在单张显卡上运行，覆盖从 RTX 5060 到 RTX 5090 的整个 RTX 50 系列。 在短短六个月内实现的这一快速优化，证明了实时神经渲染在消费级硬件上的可行性，是迈向 AI 驱动图形渲染管道的关键一步。它将直接影响正在评估 RTX 50 系列产品的玩家和开发者，并标志着 NVIDIA 在将神经网络整合到核心渲染技术栈中的领先优势正在加速扩大。 在《NBA 2K27》的 4K Ultra 画质（开启光线追踪与多帧生成）下，RTX 5090 达到约 370 FPS，RTX 5080 约 233 FPS；在 1440p 下 RTX 5090 接近 600 FPS，RTX 5070 也保持在 260 FPS 以上。尽管速度提升达 5 倍，DLSS 5 相比原生渲染仍会产生显著的性能开销——这与早期 DLSS 版本通常提升性能的做法形成明显反差——而且 NVIDIA 并未公布用于对比的原生渲染基准数据。

rss · TechPowerUp News · 9月1日 17:10

**背景**: DLSS 5 引入了实时神经渲染技术，神经网络直接在图形渲染管线内部运行（而非作为后期处理升频步骤），通过 RTX Neural Shaders 在 Blackwell Tensor Core 上的着色器程序内执行神经网络。该技术为 NVIDIA RTX 50 系列（Blackwell）显卡独占，这些显卡于 2025 年 1 月发布。DLSS 5 于 2026 年 3 月在 GTC 大会上首次公开，并将于 9 月 3 日在《NBA 2K27》中独家首发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/geforce/news/dlss5-breakthrough-in-visual-fidelity-for-games/">NVIDIA DLSS 5 Delivers AI-Powered Breakthrough In Visual Fidelity For Games</a></li>
<li><a href="https://en.wikipedia.org/wiki/GeForce_RTX_50_series">GeForce RTX 50 series - Wikipedia</a></li>
<li><a href="https://wccftech.com/nvidia-dlss-5-neural-rendering-in-10-modern-games-the-best-unofficial-dlss-5-on-vs-off-comparisons-so-far/">NVIDIA DLSS 5 Neural Rendering In 10 Modern Games – The Best Unofficial DLSS 5 ON vs OFF Comparisons So Far</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#DLSS-5`, `#neural-rendering`, `#RTX-50-series`, `#GPU-technology`

---

<a id="item-7"></a>
## [NVIDIA 重启 Rubin CPX GPU，搭载 HBM4 内存，弃用 GDDR7](https://www.techpowerup.com/352213/nvidias-rubin-cpx-gpu-reborn-with-hbm4-memory-no-more-gddr7) ⭐️ 7.5/10

据供应链分析师郭明錤报道，NVIDIA 重新启动了此前暂停的"Rubin CPX"AI 加速器项目，将其重新设计为搭载 168GB HBM4 内存，而非最初计划的 128GB GDDR7。该芯片面向大规模智能体 AI（agentic AI）工作负载，将部署于容纳 64 至 256 颗独立 CPX GPU 的机架中。 从 GDDR7 到 HBM4 的架构转变表明 NVIDIA 认识到智能体 AI 工作负载需要远超最初预期的高内存带宽，这可能重塑 AI 基础设施规划及 HBM 供应链格局。将预填充（prefill）与解码（decode）任务分配给不同 GPU 型号，反映了在机架规模上优化大语言模型推理流水线的新范式。 每个搭载 8 颗 CPX GPU 的机架托盘可利用 HBM4 处理 1.34TB 的长上下文预填充及相关 KV 缓存。由于原本基于 GDDR7 的设计不需要集成 HBM4，NVIDIA 不得不重新设计封装方案，很可能采用台积电的 CoWoS-S 或 CoWoS-L 先进封装技术。

rss · TechPowerUp News · 9月1日 12:38

**背景**: 智能体 AI（Agentic AI）是指能以最少人工干预自主执行复杂目标驱动任务的 AI 系统，需要海量上下文窗口和极高的内存带宽。高带宽内存（HBM）是一种 3D 堆叠的 DRAM 技术，通过宽接口和垂直堆叠的芯片提供远高于 GDDR7 等传统内存的带宽，但代价是更高的复杂度和成本。在大语言模型推理中，"预填充"（prefill）阶段并行处理输入提示，而"解码"（decode）阶段则顺序生成输出 token；这两个阶段的计算和内存特征截然不同，这也是 NVIDIA 决定为它们分别配备专用硬件的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://intuitionlabs.ai/articles/hbm-vs-ddr-memory-comparison">HBM vs. DDR: Key Differences in Memory Technology Explained</a></li>
<li><a href="https://www.wevolver.com/article/high-bandwidth-memory">High Bandwidth Memory : Concepts, Architecture, and Applications</a></li>
<li><a href="https://www.klaviyo.com/sg/solutions/ai/what-is-agentic-ai">What is agentic AI ? - Klaviyo SG</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI accelerators`, `#HBM4`, `#GPU architecture`, `#agentic AI`

---

<a id="item-8"></a>
## [NVIDIA GPU 帧插值功能通过 Vulkan API 集成至 FFmpeg](https://www.techpowerup.com/352206/nvidia-gpu-frame-interpolation-support-lands-in-ffmpeg) ⭐️ 7.5/10

NVIDIA 基于 GPU 加速的帧插值功能已通过 Vulkan API 合并至 FFmpeg，该功能利用 GeForce RTX GPU 上的光流加速器（NVOFA）。此次集成实现了引擎辅助帧率上转换（FRUC），允许用户通过 AI 生成中间帧来提升视频帧率，无需调用传统的图形渲染管线。 FFmpeg 是全球使用最广泛的多媒体处理工具之一，为 YouTube 等众多平台和服务提供底层支持。将硬件加速的 AI 帧插值功能添加到 FFmpeg 中，可为庞大的视频编辑、内容创作者和媒体处理流水线用户带来高效、高质量的帧率上转换能力。 该实现利用 NVENC 获取编码器端的帧数据，再借助 NVOFA 硬件生成描述帧间物体运动的光流矢量，进而合成中间帧。新的基于 Vulkan 的方案避免了专有软件的依赖问题，而这一限制正是 2023 年早期补丁未能合并至 FFmpeg 主代码库的原因。

rss · TechPowerUp News · 9月1日 07:21

**背景**: 光流（Optical Flow）是一种计算机视觉技术，通过计算像素在连续帧之间的移动来分析视频中的运动。NVIDIA 的 NVOFA 是从 Turing 架构 GPU 开始配备的专用硬件加速器，可独立于图形核心和 CUDA 核心来计算光流和立体视差。Vulkan 是由 Khronos Group 维护的开放标准、跨厂商 GPU API，为现代 GPU 提供高效的图形和计算访问能力，因此成为 FFmpeg 以非专有方式访问 NVIDIA 光流硬件的理想接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/NVIDIAOpticalFlowSDK">GitHub - NVIDIA /NVIDIAOpticalFlowSDK: Optical Flow SDK exposes...</a></li>
<li><a href="https://developer.nvidia.com/vulkan">Vulkan Open Standard Modern GPU API | NVIDIA Developer</a></li>
<li><a href="https://docs.nvidia.com/video-technologies/optical-flow-sdk/pdf/NVOFA_Application_Note.pdf">Nvidia optical flow SDK</a></li>

</ul>
</details>

**标签**: `#FFmpeg`, `#NVIDIA`, `#GPU-acceleration`, `#Vulkan`, `#video-processing`

---

<a id="item-9"></a>
## [Nvidia 颇具争议的 DLSS 5 将于 9 月 3 日随 NBA2K27 一同发布，公司分享首批基准测试成绩——支持所有 RTX 50 系列 GPU、笔记本及 GeForce NOW](https://www.tomshardware.com/pc-components/gpus/nvidias-controversial-dlss-5-will-launch-september-3-with-nba2k27-available-on-all-rtx-50-series-gpus-laptops-and-geforce-now) ⭐️ 7.5/10

Nvidia 宣布 DLSS 5 将于 9 月 3 日随 NBA2K27 一同推出，支持所有 RTX 50 系列 GPU、笔记本电脑以及 GeForce NOW 平台，并分享了首批基准测试数据。

rss · Tom's Hardware · 9月1日 13:00

**标签**: `#nvidia`, `#dlss`, `#gpu`, `#ray-tracing`, `#ai-upscaling`

---

<a id="item-10"></a>
## [中国法院冻结安世半导体 3.18 亿美元资产，闻泰科技力图夺回控制权——荷兰芯片商称查封不影响日常运营](https://www.tomshardware.com/tech-industry/chinese-court-freezes-318-million-in-nexperia-assets-as-wingtech-presses-to-regain-control) ⭐️ 7.5/10

中国法院冻结了安世半导体价值 3.18 亿美元的资产，其母公司闻泰科技正寻求重新取得控制权。尽管如此，安世半导体表示这些措施不会影响日常运营。

rss · Tom's Hardware · 9月1日 11:57

**标签**: `#Semiconductors`, `#Nexperia`, `#Wingtech`, `#Corporate Governance`, `#Supply Chain`

---

<a id="item-11"></a>
## [消息称长鑫存储启动 HBM3E 内存风险试产，实现中国 DRAM 产业突破——公司有望 2027 年实现量产](https://www.tomshardware.com/pc-components/dram/cxmt-reportedly-begins-risk-production-of-hbm3e-memory-in-breakthrough-for-chinese-dram-production-company-could-be-in-mass-production-in-2027) ⭐️ 7.5/10

消息称长鑫存储已开始 HBM3E 内存风险试产，并向阿里巴巴平头哥和寒武纪送样测试，这标志着中国国产 DRAM 和 AI 硬件供应链可能取得重大突破，目标 2027 年实现量产。

rss · Tom's Hardware · 9月1日 10:30

**标签**: `#semiconductors`, `#HBM3E`, `#China-tech`, `#DRAM`, `#AI-hardware`

---

<a id="item-12"></a>
## [Linux 内核每版本漏洞逼近 2000 个纪录，AI 漏洞猎人扫描 4000 万行代码——维护者称被 CVE 发现“完全压垮”](https://www.tomshardware.com/software/linux/linux-kernel-nears-2-000-cves-per-release-as-ai-bug-hunters-scour-40-million-lines-of-code-maintainers-say-they-are-completely-overwhelmed) ⭐️ 7.5/10

AI 辅助漏洞挖掘正推动 Linux 内核每版本 CVE 数量逼近 2000 个，海量真实缺陷与低优先级噪声令维护者不堪重负。

rss · Tom's Hardware · 9月1日 09:30

**标签**: `#linux-kernel`, `#cybersecurity`, `#AI-security`, `#open-source`, `#CVE`

---

<a id="item-13"></a>
## [新型 iPSJ GaN-on-Si 晶体管击穿电压接近 4kV](https://www.electronicsweekly.com/news/business/new-transistor-withstands-nearly-4kv-before-breakdown-2026-09/) ⭐️ 7.5/10

EPFL POWERlab 的研究人员发明了一种基于 GaN-on-Si 的本征极化超结（iPSJ）晶体管，据报道其击穿电压接近 4 kV。该设计利用 III 族氮化物异质结构中的本征极化场，无需有意掺杂即可形成电荷平衡的超结，相关成果已发表于 Nature Electronics。 如果该技术得到验证，可能使 GaN-on-Si 器件进入传统上由碳化硅（SiC）主导的高压应用领域，从而为电动汽车、电网和工业应用提供更紧凑、更高效的高压电源转换器。相比 SiC 方案，使用 GaN-on-Si 还有望降低制造成本。 该突破依赖于 GaN 异质结构中的本征极化电荷而非传统掺杂来形成超结，这一直是 GaN 高压器件的瓶颈。该器件在硅衬底上制造，论文题为《Intrinsic polarization superjunctions in III-nitride heterostructures for efficient power electronics》（Nature Electronics, 2026，DOI: 10.1038/s41928-026-01691-4）。

rss · Electronics Weekly · 9月1日 05:17

**背景**: GaN-on-Si 晶体管被普遍视为下一代功率开关的有力候选，因为 GaN 的开关损耗低于硅，且硅衬底比 SiC 更便宜。然而，传统 GaN 器件难以达到非常高的击穿电压，因为电场集中限制了其可扩展性。超结技术最初是为硅基 MOSFET 开发的，通过交替的 p 型和 n 型区域平衡电场，但在 GaN 中通过掺杂实现这种结构一直很困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.electronicsweekly.com/news/business/new-transistor-withstands-nearly-4kv-before-breakdown-2026-09/">New GaN-on-Si transistor withstands nearly 4kV before breakdown...</a></li>
<li><a href="https://www.nature.com/articles/s41928-026-01691-4?error=cookies_not_supported&code=d78c386e-053c-408b-9e0b-f20c7f005cbe">Intrinsic polarization superjunctions in III-nitride... | Nature Electronics</a></li>
<li><a href="https://www.msn.com/en-us/news/other/new-transistor-brings-high-voltage-to-microchip-scale/ar-AA2b7Y2F">New transistor brings high voltage to microchip scale</a></li>

</ul>
</details>

**标签**: `#GaN`, `#Power Electronics`, `#Semiconductors`, `#Transistors`, `#High-Voltage Devices`

---

<a id="item-14"></a>
## [Softaculous 遭遇长达 33 小时的 BGP 路由劫持](https://www.solidot.org/story?sid=85256) ⭐️ 7.3/10

8 月 28 日 20:57 UTC 左右，一个不相关网络通过 BGP 通告了 Softaculous 使用的 Hetzner IP 段，将流量重定向至攻击者控制的服务器，劫持持续约 33 小时。攻击者利用此次劫持从 Let's Encrypt 获取了有效的 TLS 证书，并向少数虚拟机管理程序服务器推送了恶意的 Virtualizor 更新包。 该事件展示了 BGP 劫持如何绕过域名验证机制，从而对软件更新基础设施实施供应链攻击。使用 Virtualizor 的托管服务商、VPS 运营商及下游客户面临凭证泄露风险，凸显了互联网基础设施层面路由安全的脆弱性。 劫持分两个阶段：首次劫持从 8 月 28 日 20:57 UTC 开始，Softaculous 于 8 月 29 日 08:50 UTC 向 Hetzner 报告，随后 8 月 29 日 20:00 UTC 再次发生持续 10 小时的劫持，最终于 8 月 30 日 05:50-06:10 UTC 停止。Let's Encrypt 的自动域名验证（可能是 ACME HTTP-01 质询）被绕过，因为验证流量本身被重定向到攻击者的 IP，从而成功签发了合法证书。

rss · Solidot · 9月1日 14:35

**背景**: BGP（边界网关协议）是互联网上用于在不同自治系统之间路由流量的协议。BGP 路由劫持是指未经授权的网络通告其并不合法拥有的 IP 前缀，导致发往这些 IP 的流量被重路由至攻击者的网络。Softaculous 是一款商业自动安装程序库，被 Web 托管服务商用于部署 WordPress、Joomla 等应用程序；Virtualizor 是由 Softaculous 开发维护的基于 Web 的 VPS 管理面板。Let's Encrypt 是一个免费、自动化的证书颁发机构，通过 ACME 协议验证域名所有权，通常做法是检查请求服务器能否响应特定 HTTP 路径——而如果发往该服务器的流量正遭到劫持，这种验证就形同虚设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/virtualizor-compromise/">BGP Hijack Diverts Softaculous Traffic to Deliver Malicious Virtualizor ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Softaculous">Softaculous</a></li>
<li><a href="https://www.thousandeyes.com/learning/glossary/bgp-route-hijacking">What is BGP Hijacking ? Internet & IP Route Hijacking</a></li>

</ul>
</details>

**标签**: `#BGP-hijacking`, `#cybersecurity`, `#supply-chain-attack`, `#Hetzner`, `#Virtualizor`

---

<a id="item-15"></a>
## [Dan Luu 严格审视 Ed Zitron 的 AI 怀疑论预测](https://danluu.com/zitron/) ⭐️ 7.0/10

工程师兼博主 Dan Luu 发表了一篇系统分析文章，逐条评估了知名 AI 怀疑论者 Ed Zitron 对 AI 行业的预测与现实结果的吻合程度，对 Zitron 的具体主张进行了核查并评估其兑现情况。 这种严格的预测核查在 AI 讨论中非常罕见，因为该领域通常充斥着缺乏问责的炒作或末日论调。本文有助于读者校准对 AI 泡沫的讨论，并为评估怀疑论者和乐观主义者的激进主张提供了一个参考框架。 文章重点揭示了超大规模云厂商（Google、Meta、Microsoft）向 OpenAI 和 Anthropic 注资换取股权、再将估值增长计入'其他收入'以推高报告营收和利润的做法。文章还指出，Zitron 的怀疑论已演变为一种政治立场，这可能会阻碍其诚实地修正自身观点。

hackernews · jatins · 9月1日 18:35 · [社区讨论](https://news.ycombinator.com/item?id=49526069)

**背景**: Ed Zitron 是一位英国公关从业者转型的科技批评家，他已成为警告生成式 AI 热潮是不可持续泡沫的最知名声音之一，认为 AI 公司的支出远远超过其能够回收的金额。Dan Luu 是一位知名的软件工程师和博主，以其对科技行业主张的严谨数据分析而闻名。AI 泡沫辩论在 2024 至 2025 年间愈演愈烈，因为 OpenAI 和 Anthropic 等公司以空前估值进行巨额融资，同时承担着巨大的算力成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ed_Zitron">Ed Zitron - Wikipedia</a></li>
<li><a href="https://www.vanityfair.com/story/ed-zitron-ai-skeptic-openai">Ed Zitron Is Sounding the Alarm About the AI Bubble. | Vanity Fair</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了实质性的观点：多人呼吁对 Sam Altman 和 Dario Amodei 等 AI 乐观主义者进行类似的预测审计，指出行业领袖同样容易夸大其词。还有人强调，超大规模云厂商通过将 AI 实验室的股权计入'其他收入'来推高报告盈利。批评者认为，AI 怀疑论变成一种政治立场后会形成固化的受众群体，使 Zitron 无法承认自己可能犯错，从而损害长期预测质量。一位评论者观察到，读者往往将自己的预测投射到 Zitron 的言论上，而非认真审视其字面主张。

**标签**: `#AI skepticism`, `#AI bubble`, `#Dan Luu`, `#industry analysis`, `#predictions`

---

<a id="item-16"></a>
## [Show HN：在 48GB Mac 上以约 12 tok/s 的速度运行 104GB 的 Qwen3.8-Flash-Next 模型](https://github.com/carloslfu/slotstream) ⭐️ 7.0/10

Slotstream 通过专家卸载和 SSD 流式传输（基于 MLX），使在仅 16GB 内存的 Mac 上以约 12 tok/s 的速度运行 104GB 的 Qwen3.8-Flash-Next 混合专家（MoE）模型成为可能。

hackernews · carloslfu · 9月1日 16:42 · [社区讨论](https://news.ycombinator.com/item?id=49524447)

**标签**: `#LLM`, `#Apple Silicon`, `#MLX`, `#MoE`, `#model-quantization`

---

<a id="item-17"></a>
## [前五大企业级 SSD 厂商 2026 年第二季度营收逼近 375.9 亿美元](https://www.dramexchange.com/WeeklyResearch/Post/2/12818.html) ⭐️ 7.0/10

据 TrendForce 报道，受价格上涨和出货量增加的推动，前五大企业级 SSD 厂商在 2026 年第二季度的合并营收有望达到约 375.9 亿美元；NAND Flash 供应商正通过扩展企业级 SSD 产品线来提升利润。 这一趋势表明，由 AI 和数据中心需求驱动的企业级存储市场正在强劲回暖，同时也凸显出 NAND Flash 供应商正战略性从大宗闪存产品向高利润企业级产品转型，这一转变可能重塑厂商之间的竞争格局。 375.9 亿美元这一数字代表了前五大企业级 SSD 供应商的合并营收，反映了出货量增长和平均售价（ASP）上升的双重驱动；TrendForce 将此增长归因于供应商积极优化和多样化其企业级 SSD 产品线以获取更高利润。

rss · DRAMeXchange (TrendForce) · 9月1日 14:42

**背景**: 企业级 SSD 是为数据中心和服务器设计的高性能、高可靠性固态硬盘，与消费级 SSD 的区别在于具备掉电保护等特性以及更高的耐久度（以每日写入量 DWPD 衡量）。NAND Flash 是底层非易失性存储技术，数据存储于电荷俘获单元中，NAND Flash 市场与企业级存储需求紧密相关。TrendForce 是一家知名的市场研究机构，定期发布存储和内存细分领域的价格与出货量预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.longsys.com/about-longsys/news/what-is-an-enterprise-ssd.html">An overview of what is an enterprise SSD .</a></li>
<li><a href="https://www.servnetuk.com/computing-components/ssd-nvme">Enterprise SSD & NVMe Guide UK | DWPD & PCIe Gen5 | Servnet UK</a></li>
<li><a href="https://recoverit.wondershare.com/flashdrive-recovery/what-is-nand-flash-memory.html">What is NAND Flash Memory ? - Definition, Features, Types and More</a></li>

</ul>
</details>

**标签**: `#Enterprise SSD`, `#NAND Flash`, `#Semiconductor Market`, `#Storage Hardware`, `#TrendForce`

---

<a id="item-18"></a>
## [John Ternus 正式出任苹果新任 CEO](https://www.techpowerup.com/352222/john-ternus-takes-the-helm-as-apples-new-ceo) ⭐️ 6.5/10

John Ternus（苹果前硬件工程高级副总裁）已正式接任首席执行官一职，取代此前于四月宣布即将卸任的 Tim Cook。Ternus 于 2001 年加入苹果，2013 年起领导硬件部门，曾主导 iPhone、iPad、Mac 产品线、AirPods 以及 Vision Pro 的研发工作。 此次领导层交接标志着这家全球市值最高的科技公司之一正转向以硬件为核心的战略方向。Ternus 深厚的工程背景及其过往业绩——尤其是成功推动从 Intel 向 Apple Silicon 的转型——预示着苹果未来的产品将更加注重定制芯片和一体化硬件设计。 Ternus 最显著的成就是主导苹果 MacBook 从基于 Intel x86 的设计转向自研 ARM 架构 Apple Silicon SoC 的过渡，这一多年项目于 2020 年末以 M1 芯片为起点。在过去几个月中，Ternus 与 Cook 密切协作，确保苹果长期战略目标的延续性。

rss · TechPowerUp News · 9月1日 16:23

**背景**: Apple Silicon 是苹果自研的 ARM 架构处理器系列，从 2020 年末的 M1 芯片开始，逐步取代了 Mac 产品线中的 Intel 芯片。这一转型被广泛视为计算行业的里程碑式转变——苹果的 M 系列芯片在性能和能效上均超越了 Intel 的 x86 处理器，并促使亚马逊、谷歌等其他科技巨头也转向 Arm 架构。苹果硬件工程高级副总裁负责公司核心产品的设计，历来是 CEO 之下最具影响力的职位之一，因此 Ternus 的上任对于一家日益以垂直整合硬件和芯片战略为核心的公司来说，是顺理成章的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/en-us/116943">Mac computers with Apple silicon - Apple Support</a></li>
<li><a href="https://www.zdnet.com/article/the-fall-of-intel-how-gen-ai-helped-dethrone-a-giant-and-transform-computing-as-we-know-it/">The fall of Intel : How gen AI helped dethrone a giant and... - ZDNET</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mac_(computer)">Mac (computer) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#leadership`, `#CEO-transition`, `#corporate-news`, `#tech-industry`

---

<a id="item-19"></a>
## [NVIDIA 在 Hot Chips 2026 展示 CUDA 支持 RISC-V 及 NVLink Fusion 集成](https://www.servethehome.com/nvidia-risc-v-for-nvidia-gpus-at-hot-chips-2026/) ⭐️ 6.5/10

在 Hot Chips 2026 上，NVIDIA 展示了将 CUDA 支持扩展到 RISC-V 指令集架构，并讨论了如何将 RISC-V 处理器集成到其 NVLink Fusion 系统架构中。此次演讲标志着 NVIDIA 在其专有 GPU 和互连技术之外，正日益深入地参与开源 RISC-V 生态系统。 这一进展之所以重要，是因为 CUDA 是 NVIDIA 核心的软件护城河，将其扩展到 RISC-V 将显著拓宽 GPU 加速计算可用的硬件范围，使其不再局限于 x86 和 Arm 平台。结合 NVLink Fusion 将非 NVIDIA 芯片接入 NVIDIA 高带宽 Fabric 的能力，NVIDIA 正从纯粹的垂直整合芯片厂商转变为生态系统的赋能者。 NVLink Fusion 被定位为高频同步 Fabric，而非像 PCIe 那样的简单 I/O 互连，可实现定制芯片与 NVIDIA GPU 之间的紧耦合。NVIDIA 公开讨论 CUDA 在 RISC-V 上的运行，表明其正在持续投入工程资源，但目前可获取的 Hot Chips 报道内容较为简略，缺乏详细的性能数据和时间线信息。

rss · ServeTheHome · 9月1日 19:00

**背景**: RISC-V 是一种基于精简指令集（RISC）原则的开源标准指令集架构（ISA），允许任何人在无需支付授权费的情况下设计和制造兼容处理器。CUDA 是 NVIDIA 的并行计算平台和编程模型，已成为 AI 和高性能计算领域 GPU 加速工作负载的主导框架。NVLink Fusion 是 NVIDIA 的互连技术，将其专有的 NVLink 协议扩展到允许第三方 CPU 和加速器接入 NVIDIA 的高带宽一致性 Fabric，从而实现将定制芯片与 NVIDIA GPU 组合的异构计算系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/interconnect-computer-why-nvidias-nvlink-fusion-most-trojan-kannan-yoiec">The Interconnect Is the Computer: Why Nvidia ’s NVLink Fusion is the...</a></li>
<li><a href="https://digestibly.beehiiv.com/p/nvidia-goes-full-matrix">NVIDIA Goes Full Matrix</a></li>
<li><a href="https://tech.yahoo.com/computing/articles/nvidias-jen-hsun-huang-boasts-132554200.html">Nvidia 's Jen-Hsun Huang boasts that one spine of its new NVLink ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#RISC-V`, `#CUDA`, `#Hot Chips`, `#GPU`

---

<a id="item-20"></a>
## [评论文章力陈 Firefox 对浏览器引擎多样性的必要性](https://www.newsonaut.com/articles/hang-on-to-your-firefox) ⭐️ 6.0/10

一篇评论文章主张 Firefox 对于维持浏览器引擎多样性仍然至关重要，理由是如果没有 Firefox，整个网络将完全被 Chromium（Blink）和 WebKit 所主导。文章将 Firefox 的重要性置于其功能集之外，强调它作为生态系统中最后一个主要独立引擎的角色。 如果 Chromium 不受制约地继续吞噬市场份额，Google 将获得对 Web 标准、渲染行为以及影响每个站点和开发者的事实政策决策的超大影响力。Firefox 的 Gecko 引擎是主要的制衡力量，但其不断萎缩的用户基数引发了人们对 Mozilla 还能维持多久独立引擎开发的质疑。 Mozilla 因涉足广告技术收购以及与 Firefox 隐私定位相矛盾的数据收集行为而遭到批评，这使得"只用 Firefox"的论点变得复杂。社区评论者还指出，Chrome 的分支浏览器（Edge、Brave、Opera、Vivaldi）并不构成引擎多样性，因为它们都共享 Blink，无法真正与上游分叉。

hackernews · speckx · 9月1日 20:30 · [社区讨论](https://news.ycombinator.com/item?id=49527748)

**背景**: 浏览器引擎是将 HTML、CSS 和 JavaScript 渲染成可见网页的软件；当今主流的引擎包括 Blink（被 Chrome 及大多数基于 Chromium 的浏览器使用）、WebKit（被 Safari 和所有 iOS 浏览器使用，因为 Apple 强制要求）以及 Gecko（被 Firefox 使用）。从历史上看，浏览器引擎多样性之所以重要，是因为单一引擎垄断会让一家供应商成为事实上的标准制定者，就像当年 Internet Explorer 对抗 Netscape 的时期一样。搜索结果解释称，Chromium 的主导地位赋予了 Google 对网站构建和测试方式的巨大影响力，而像 Gecko 这样的差异化引擎即使在性能上有所牺牲，也更注重标准合规性和隐私保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://css-tricks.com/browser-engine-diversity/">css-tricks.com/ browser - engine - diversity</a></li>
<li><a href="https://www.sigmabrowser.com/blog/what-is-a-browser-engine-chromium-blink-webkit-gecko-explained">What Is a Browser Engine ? Chromium , Blink , WebKit & Gecko ...</a></li>
<li><a href="https://bkardell.com/blog/EcosystemHealth.html">Web Engine Diversity and Ecosystem Health</a></li>

</ul>
</details>

**社区讨论**: 评论者大致认同文章的前提——Firefox 对引擎多样性很重要，但也补充了更细致的观点：有人指出广告拦截支持仍然是 Firefox 一个独特的强项卖点；有人认为 Web 开发者难辞其咎，因为他们默认"在 Chrome 中测试"就够了，并且优先实现 Chrome 已支持的功能；还有人站在构建联盟的立场上辩护说，支持 Firefox 并不意味着要认同 Mozilla 的每一个决策。一位评论者还提到了 Servo 和 Ladybird 等新兴替代方案，并介绍了一个可视化跨引擎 Web 平台测试结果（WPT）结果的工具。

**标签**: `#firefox`, `#browser-diversity`, `#mozilla`, `#web-ecosystem`, `#opinion`

---