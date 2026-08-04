---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 107 条内容中筛选出 20 条重要资讯。

---

1. [AMD 发布 Helios：搭载 72 颗 MI455X 的首个机架级 AI 平台](#item-1) ⭐️ 8.5/10
2. [神经网络在轨自主控制卫星平台](#item-2) ⭐️ 8.0/10
3. [闪迪与 SK 海力士发布高带宽闪存首个 OCP 技术规范](#item-3) ⭐️ 7.5/10
4. [台积电目标到 2026 年底实现每月 10 万片 N2 晶圆产能](#item-4) ⭐️ 7.5/10
5. [AI 爱好者用 Claude Code 绕过 BIOS RSA-2048 签名验证，解锁 55 项隐藏设置](#item-5) ⭐️ 7.5/10
6. [共封装光学（CPO）代工厂路线图——解析台积电、英特尔、三星和格芯在下一代纵向扩展连接方面的策略](#item-6) ⭐️ 7.5/10
7. [AI 自动化大幅削减客服岗位](#item-7) ⭐️ 7.3/10
8. [LLMs reward expertise](#item-8) ⭐️ 7.0/10
9. [数学与理论计算机科学领域的十项进展](#item-9) ⭐️ 7.0/10
10. [Cloudflare 使用 FP8 KV 缓存量化高效部署 Kimi 和 GLM 模型](#item-10) ⭐️ 7.0/10
11. [MiniMax H3 在 ComfyUI 的零日支持：开放权重、原生音频与 2K 视频](#item-11) ⭐️ 7.0/10
12. [Andy Pavlo 加入 ClickHouse 成立 ClickHouse Labs](#item-12) ⭐️ 7.0/10
13. [瑞萨电子以 MRDIMM 更新攻克内存瓶颈](#item-13) ⭐️ 7.0/10
14. [视频访谈：ChipAgents CEO 谈智能体 AI 在 EDA 领域的最新融资](#item-14) ⭐️ 7.0/10
15. [台积电 1.4 纳米晶圆厂建设提前推进，投资 490 亿美元](#item-15) ⭐️ 7.0/10
16. [NVIDIA RTX 50 系列显卡在韩国面临 20-30% 涨价](#item-16) ⭐️ 6.5/10
17. [铠侠发布 GP1 系列 PCIe 6.0 NVMe SSD，瞄准 AI 工作负载](#item-17) ⭐️ 6.5/10
18. [长鑫存储(CXMT)据报道计划在北京建设第二座晶圆厂以提升 DRAM 产能](#item-18) ⭐️ 6.5/10
19. [AI 公司大幅下调 token 价格，应对中国模型的激烈竞争](#item-19) ⭐️ 6.5/10
20. [2026 年用 4GB 显存的 Radeon RX 6500 XT 和 GTX 1650 Super 玩游戏——升频技术让低端 GPU 胜任电竞和网吧需求](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [AMD 发布 Helios：搭载 72 颗 MI455X 的首个机架级 AI 平台](https://www.servethehome.com/amd-helios-architecture-deep-dive-amd-broadcom-hardware-combined/) ⭐️ 8.5/10

AMD 在 Advancing AI 2026 大会上发布了其 Helios 机架级架构，将 72 颗 Instinct MI455X 加速器整合为一个统一系统——这是 AMD 首个机架级 AI 数据中心平台。该设计围绕 AI 工作负载的数据流转路径，将 AMD 的 CPU、GPU 和网络进行了紧密协同设计。 Helios 代表了 AMD 对 NVIDIA NVL72 级机架系统的正面挑战，标志着 AMD 作为全栈 AI 基础设施有力竞争者的崛起。通过采用基于以太网的开放 UALink 标准而非专有互连协议，AMD 将 Helios 定位为厂商中立的替代方案，有望重塑超大规模云厂商的采购策略。 MI455X 搭载 HBM4 显存，72 颗加速器通过以太网上的 UALink 进行通信——这与 NVIDIA 的专有 NVLink 方案形成鲜明对比。Helios 已进入量产阶段，机架交付定于 2026 年第三季度，平台面向 64 位 Linux 环境。

rss · ServeTheHome · 8月3日 19:00

**背景**: 机架级架构将整个服务器机架（计算、内存、存储和网络）视为一个统一的整体系统，而非简单组装独立服务器。NVIDIA 以 NVL72 系统开创了这一先河，该系统使用专有的 NVLink 技术连接 72 颗 GPU。UALink（Ultra Accelerator Link）是由行业支持的开放互连标准，旨在实现跨厂商加速器之间高速、厂商中立的通信。MI455X 是 AMD 面向下一代数据中心推出的 GPU，定位是与 NVIDIA 的 Rubin 系列竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">AMD Helios Rackscale Solution – Powering Frontier AI</a></li>
<li><a href="https://www.amd.com/en/blogs/2026/amd-launches-helios-the-highest-performing-rackscale-ai-infrastructure-solution.html">AMD Launches Helios™: The Highest Performing Rackscale AI Infrastructure Solution</a></li>
<li><a href="https://www.networkworld.com/article/4204533/amd-unveils-ai-gpu-to-challenge-nvidias-rubin.html">AMD unveils AI GPU to challenge Nvidia’s Rubin | Network World</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Helios`, `#rackscale`, `#MI455X`, `#AI-infrastructure`

---

<a id="item-2"></a>
## [神经网络在轨自主控制卫星平台](https://www.electronicsweekly.com/news/neural-network-controls-satellite-bus-in-orbit-2026-08/) ⭐️ 8.0/10

美国空军研究实验室(AFRL)已在轨演示了使用神经网络对卫星平台进行自主控制，实验室将其描述为迈向 AI 驱动航天器运营的一次关键性转变。 此次演示标志着星载 AI 领域的重要里程碑，对国防、自主太空运营以及在实时地面干预不可行的资源受限轨道环境中部署边缘 AI 都具有深远意义。 原始文章内容被截断，未披露神经网络的架构、具体的任务参数或故障模式，限制了对该项目的深入技术评估。AFRL 的演示与 Open Cosmos 的 HAMMER 和 Φ-Sat-2 任务以及 EDGX 的星载边缘 AI 计算平台等其他在轨 AI 项目处于同一发展方向。

rss · Electronics Weekly · 8月3日 09:08

**背景**: 卫星平台(Satellite bus)是航天器的主体结构，用于承载有效载荷和科学仪器，通常负责管理电力、推进、热控和航天器内部通信。长期以来，卫星在很大程度上扮演着"弯管"(bent pipe)的角色——采集原始数据后将其下行传输至地面站进行处理。轨道边缘 AI(Orbital Edge AI)颠覆了这一模式，直接在航天器上运行神经网络，实现自主决策、更快的响应速度，并减少对地面控制的依赖——这些能力对国防和灾害响应等时间敏感型应用越来越关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Satellite_bus">Satellite bus - Wikipedia</a></li>
<li><a href="https://blacknightspacelabs.com/blog/orbital-edge-ai-onboard-satellite-processing-cognisat-space-ai-vpu-inference-bent-pipe-bottleneck">Orbital Edge AI & On - Board Satellite ... | BlacKnight Space Labs</a></li>

</ul>
</details>

**标签**: `#neural-networks`, `#satellite`, `#autonomous-systems`, `#space-tech`, `#edge-AI`

---

<a id="item-3"></a>
## [闪迪与 SK 海力士发布高带宽闪存首个 OCP 技术规范](https://www.techpowerup.com/351335/sandisk-and-sk-hynix-advance-global-standardization-of-high-bandwidth-flash-with-release-of-first-ocp-technical-specification) ⭐️ 7.5/10

闪迪与 SK 海力士联合 Google 和 Tenstorrent 发布了高带宽闪存（HBF）的首个 OCP 技术规范，距该联盟于 2025 年 2 月启动工作仅过去六个月。该规范定义了两种容量配置（分别采用 8 层和 16 层 NAND 堆叠，最高支持 512GB），并按三个等级（Grade 1~3）设定带宽标准，数据传输能力覆盖约 0.4TB/s 至 3.0TB/s。 HBF 定位为介于 HBM 和固态硬盘之间的新型存储层级，在接近 HBM 带宽水平的同时提供 NAND 闪存的高密度特性，这对于需要大规模内存容量的 AI 推理工作负载至关重要。在 OCP 框架下获得 Google 和 Tenstorrent 等主要厂商支持的标准化工作，标志着行业已形成真正的发展势头，有望加速生态采用，缓解 AI 加速器中 HBM 面临的成本和供应压力。 HBF 基于闪迪的低成本、高密度 CBA 架构 NAND 核心技术构建，并采用 3D 堆叠封装，据称性能可达无限容量 HBM 的约 2.2%以内，同时显著提升容量。该规范主要面向 AI 推理场景，在需要更大近计算内存容量和更高带宽的应用中改善功耗、性能和总拥有成本。

rss · TechPowerUp News · 8月4日 01:46

**背景**: 开放计算项目（OCP）是一个非营利组织，致力于创建开源数据中心硬件规范，推动行业协作、降低成本并加速创新。高带宽内存（HBM）是当前高性能 AI 加速器的标准，但由于采用 DRAM，成本高昂且容量有限。高带宽闪存（HBF）是一类新型 NAND 闪存，采用先进封装和接口技术，提供与 HBM 相当的带宽，同时具备更高的容量和更低的每 GB 成本——特别适合通常需要大模型和上下文存储的 AI 推理场景，而非以 HBM 为核心的极致带宽训练场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sandisk.com/company/newsroom/blogs/2025/scaling-beyond-the-wall-inside-sandisks-high-bandwidth-flash-for-ai">Scaling the Memory Wall: Behind Sandisk’s High Bandwidth Flash for AI Inferencing | Sandisk</a></li>
<li><a href="https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf">HIGH BANDWIDTH FLASH</a></li>
<li><a href="https://www.emergentmind.com/topics/high-bandwidth-flash-hbf">High Bandwidth Flash (HBF) Overview</a></li>
<li><a href="https://www.gigabyte.com/glossary/ocp">What Is OCP and How Does It Work? - GIGABYTE Global</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#memory technology`, `#OCP`, `#HBF`, `#industry standardization`

---

<a id="item-4"></a>
## [台积电目标到 2026 年底实现每月 10 万片 N2 晶圆产能](https://www.techpowerup.com/351326/tsmc-targets-100-000-n2-wafers-per-month-by-the-end-of-2026) ⭐️ 7.5/10

台积电计划在 2026 年底前将 2 纳米 N2 晶圆月产量从 2 万片提升至 10 万片，使该制程的收入占比从 3%增至 10%以上。

rss · TechPowerUp News · 8月3日 17:12

**标签**: `#semiconductors`, `#TSMC`, `#manufacturing`, `#2nm`, `#chip-industry`

---

<a id="item-5"></a>
## [AI 爱好者用 Claude Code 绕过 BIOS RSA-2048 签名验证，解锁 55 项隐藏设置](https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings) ⭐️ 7.5/10

一位 Reddit 用户使用 Anthropic 的 Claude Code 对自己惠普笔记本的 BIOS 固件进行逆向工程，绕过了 RSA-2048 DXE-FV 签名验证，并在自己的硬件上解锁了 55 个隐藏设置项以及四个高级 BIOS 配置菜单。 这一案例表明，当前的 AI 编程智能体已经能够在固件逆向工程和二进制分析等底层任务中提供实质性帮助——而这些任务此前需要高度专业化的技术能力。它同时也引发了关于 AI 工具将如何重塑攻防安全研究及行业固件防护策略的更广泛讨论。 整个过程涉及三层补丁：绕过 DXE 固件卷阶段的 RSA-2048 签名检查、暴露 55 个隐藏设置项，以及揭示更多 BIOS 配置选项。关键在于，RSA-2048 加密算法本身并未被破解——被绕过的是固件中具体的签名验证例程，这是一个重要的区别。

rss · Tom's Hardware · 8月3日 11:55

**背景**: BIOS 是 PC 上在操作系统加载之前初始化硬件的低层固件，通常包含制造商限制仅向企业用户开放的隐藏设置（如高级电源、虚拟化或诊断选项）。RSA-2048 是一种使用 2048 位密钥的非对称加密算法，广泛用于对固件进行数字签名，使设备仅运行制造商认证的代码。Claude Code 是 Anthropic 推出的代理式编程工具，运行在终端中，可以读取代码库并执行命令，非常适合拆解二进制文件和生成补丁脚本等多步骤任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings">AI enthusiast unlocks and mods BIOS with Claude Code — AI defeats RSA-2048 signature checks and unlocks 55 hidden settings | Tom's Hardware</a></li>
<li><a href="https://x.com/cyber_razz/status/2079834248794493194">Abdulkadir | Cybersecurity on X: "A Reddit user gave Claude Code their HP laptop's BIOS dump. Asked it to unlock the firmware. Claude disassembled the signature-check code. Found the RSA-2048 verification function. Then wrote a Python script to bypass it. The user modified the BIOS. Flashed it back. Got https://t.co/VmpMQVbOjS" / X</a></li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude Code`, `#BIOS hacking`, `#reverse engineering`, `#security`

---

<a id="item-6"></a>
## [共封装光学（CPO）代工厂路线图——解析台积电、英特尔、三星和格芯在下一代纵向扩展连接方面的策略](https://www.tomshardware.com/tech-industry/artificial-intelligence/co-packaged-optics-cpo-foundry-roadmaps-breaking-down-tsmc-intel-samsung-and-globalfoundries-approach-to-next-generation-scale-up-connectivity) ⭐️ 7.5/10

分析台积电、英特尔、三星代工和格芯如何各自采取不同的共封装光学策略，以实现面向 AI 纵向扩展系统的下一代光连接。

rss · Tom's Hardware · 8月3日 11:45

**标签**: `#co-packaged-optics`, `#semiconductors`, `#AI-infrastructure`, `#foundry-roadmaps`, `#photonics`

---

<a id="item-7"></a>
## [AI 自动化大幅削减客服岗位](https://www.solidot.org/story?sid=84994) ⭐️ 7.3/10

微软、澳大利亚联邦银行（CBA）、Uber 和凯悦酒店等大公司正通过 AI 驱动的自动化大幅削减客服人员。微软将客服团队从约 5 万人缩减至 4 万人，每年节省约 7.5 亿美元；凯悦裁掉了美洲地区三成的内部客服；Uber 裁减了 10% 的客服岗位。 分析师估计到 2030 年近半客服岗位将受到影响，这一趋势将冲击美国、印度和菲律宾等雇佣了数百万呼叫中心从业者的国家——这些国家过去因西方公司外包英语客服而受益。AI 带来的岗位流失可能重塑全球劳动力市场，并动摇长期存在的离岸客服外包商业模式。 微软销售和服务运营负责人 Judson Althoff 表示，复杂问题仍需人工支持，但公司正不断扩大自动化处理的范围。CBA 裁减了数百名客服，每年预计节省数千万美元。这一转变既源于生成式 AI 技术能力的提升，也来自高管层拥抱新技术以降低成本的压力。

rss · Solidot · 8月3日 14:22

**背景**: 呼叫中心行业是全球重要的就业领域，菲律宾和印度等国因拥有大量英语劳动力而成为主要的外包目的地。如今生成式 AI 工具（包括大语言模型和对话式 AI 平台）已能够自动化处理以前需要人工完成的聊天和电话客服工作。Zendesk 等平台已构建以 AI 为先的客服工作流，可在多个渠道上无需人工介入即可解决问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zendesk.com/">AI -Powered Service Platform | Zendesk</a></li>

</ul>
</details>

**标签**: `#AI`, `#automation`, `#customer-service`, `#labor-market`, `#industry-trends`

---

<a id="item-8"></a>
## [LLMs reward expertise](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 7.0/10

Article arguing that LLMs produce significantly better outputs for users with domain expertise, as experts can craft better prompts, provide better context, and critically evaluate responses, effectively making LLMs an 'amplifying mirror' of user capability.

hackernews · MaxMussio · 8月3日 21:13 · [社区讨论](https://news.ycombinator.com/item?id=49161518)

**标签**: `#LLMs`, `#AI`, `#prompt-engineering`, `#expertise`, `#human-AI-interaction`

---

<a id="item-9"></a>
## [数学与理论计算机科学领域的十项进展](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 7.0/10

OpenAI 公布了 AI 模型在数学与理论计算机科学领域（包括猜想与证明）做出的十项贡献，社区正在就此对未来数学研究的影响展开讨论。

hackernews · milkshakes · 8月3日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49157930)

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#reasoning`

---

<a id="item-10"></a>
## [Cloudflare 使用 FP8 KV 缓存量化高效部署 Kimi 和 GLM 模型](https://blog.cloudflare.com/smaller-faster-safer-models/) ⭐️ 7.0/10

Cloudflare 发布了一篇技术深度文章，详细介绍了如何在大规模场景下高效部署开源模型 Kimi（由 Moonshot AI 开发）和 GLM（由 Zhipu AI 开发），重点采用了 FP8 KV 缓存量化及其他推理优化手段，以降低显存占用并提升吞吐量。 随着开源中国模型在全球获得越来越多关注，Cloudflare 等主要基础设施提供商在部署策略上的选择，直接影响到基于这些模型构建应用的开发者在延迟、成本和质量方面的体验。FP8 KV 缓存量化是在有限 GPU 显存中容纳大模型的关键手段，Cloudflare 公开讨论这一实践，为业界提供了许多提供商默默使用而鲜有披露的稀缺透明度。 FP8 KV 缓存量化将缓存的 Key 和 Value 张量以 8 位浮点而非 FP16/BF16 存储，可使注意力缓存的显存占用减少约一半，并且可以与权重量化独立启用（vLLM 和 TensorRT Edge-LLM 文档中均有说明）。文章还涉及其他优化手段，用于将 GLM-4.5/GLM-5 等大型 MoE 架构模型装入通用 GPU。

hackernews · ascorbic · 8月3日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=49158581)

**背景**: KV 缓存是 Transformer 中每个请求的内存结构，用于存储之前计算的 Key 和 Value 投影，从而在自回归生成过程中无需对完整上下文重新计算注意力。当上下文长度增长到数十万 token 时，KV 缓存通常会成为 GPU 显存的主要占用者，因此对缓存本身进行量化是一项高回报的优化。Kimi 是中国初创公司 Moonshot AI 的长上下文大模型系列，GLM 则是 Zhipu AI 的开源旗舰模型线，包括采用混合专家架构的 GLM-4.5 和 GLM-5（约 7450 亿总参数，激活参数 440 亿）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-academy.dev/kv-cache-quant/">KV Cache Quantization Explained... | LLM Academy</a></li>
<li><a href="https://docs.vllm.ai/projects/llm-compressor/en/0.9.0/examples/quantization_kv_cache/">fp 8 Weight, Activation, and KV Cache Quantization - LLM ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论观点不一：部分评论者赞扬 Cloudflare 对 KV 缓存量化的透明度，指出许多提供商在宣传未量化权重的同时默默使用此类优化，并希望看到跨模型家族的更全面评估。另一些评论者则对 Cloudflare 推理服务缺乏零数据保留（ZDR）机制提出隐私和信任方面的担忧，质疑选择 int4 而非 nf4 的原因，抱怨定价不透明，并询问招聘信息。

**标签**: `#LLM inference`, `#quantization`, `#model serving`, `#Cloudflare`, `#KV cache`

---

<a id="item-11"></a>
## [MiniMax H3 在 ComfyUI 的零日支持：开放权重、原生音频与 2K 视频](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 7.0/10

一款支持原生音频、2K 分辨率，并具备显著权重剪枝优化的开放权重视频生成模型发布，同时提供即时的 ComfyUI 集成支持。

hackernews · vblanco · 8月3日 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49155629)

**标签**: `#video-generation`, `#open-weights`, `#comfyui`, `#multimodal-ai`, `#model-compression`

---

<a id="item-12"></a>
## [Andy Pavlo 加入 ClickHouse 成立 ClickHouse Labs](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 7.0/10

著名卡内基梅隆大学数据库研究员 Andy Pavlo 加入 ClickHouse，创立 ClickHouse Labs，标志着公司对基础数据库系统研究的重视。

hackernews · nikolay_sivko · 8月3日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49156011)

**标签**: `#database-systems`, `#clickhouse`, `#industry-news`, `#research`, `#olap`

---

<a id="item-13"></a>
## [瑞萨电子以 MRDIMM 更新攻克内存瓶颈](https://www.eetimes.com/renesas-tackles-memory-bottleneck-with-mrdimm-update/) ⭐️ 7.0/10

瑞萨电子推出第三代 DDR5 MRDIMM，提供高达 16,000 MT/s 的带宽，旨在解决 AI 工作负载中的内存瓶颈问题，且无需进行平台重新设计。

rss · EE Times · 8月3日 19:00

**标签**: `#MRDIMM`, `#DDR5`, `#memory-bandwidth`, `#AI-infrastructure`, `#Renesas`

---

<a id="item-14"></a>
## [视频访谈：ChipAgents CEO 谈智能体 AI 在 EDA 领域的最新融资](https://www.eetimes.com/video-interview-chipagents-ceo-on-latest-funding-for-agentic-ai-in-eda/) ⭐️ 7.0/10

ChipAgents 融资 6000 万美元，用于开发面向芯片设计自动化的自主智能体 AI，与传统的副驾式 EDA 工具形成竞争格局。

rss · EE Times · 8月3日 14:07

**标签**: `#agentic-ai`, `#eda`, `#chip-design`, `#funding`, `#ai-agents`

---

<a id="item-15"></a>
## [台积电 1.4 纳米晶圆厂建设提前推进，投资 490 亿美元](https://www.electronicsweekly.com/news/business/tsmc-ahead-of-schedule-with-1-4nm-fab-2026-08/) ⭐️ 7.0/10

据《工商时报》报道，台积电位于台中中央台湾科学园区的 1.4 纳米晶圆厂建设进度超前，该工厂总投资达 490 亿美元，并于 2025 年 11 月正式动工。 作为全球最先进的半导体制造设施之一，1.4 纳米（A14）工艺节点能否如期甚至提前投产，对下一代 AI 加速器、高性能计算及消费级芯片至关重要。490 亿美元的投资规模也反映出尖端制程不断攀升的资本需求，以及台积电维持其相对于三星和英特尔工艺领先地位的决心。 台积电将 1.4 纳米节点正式命名为"A14"，预计将在 2027 至 2028 年左右进入大规模量产阶段。该工艺严重依赖极紫外光刻（EUV）技术，并将在 2025 年底量产的 N2（2 纳米）节点之后接棒。

rss · Electronics Weekly · 8月3日 05:15

**背景**: 在半导体制造中，像 1.4 纳米这样的"节点"名称已不再对应任何实际的晶体管物理尺寸，而是代表每一代晶体管密度和性能提升的营销标签。台积电的工艺路线图为 N3（3 纳米）→ N2（2 纳米）→ A14（1.4 纳米），每一代节点都会在能效、晶体管密度和性能上带来提升。尖端晶圆厂的建设资本极其密集，往往需要数百亿美元的投资，其中很大一部分来自 ASML 的极紫外光刻（EUV）设备，单台成本就超过 2 亿美元。A14 工艺预计将对 AI 工作负载尤为重要，因为这些应用对计算密度和能效的要求极高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phonearena.com/news/tsmc-says-what-follows-2nm-node_id153534">For the first time, TSMC reveals what will follow the 2 nm node</a></li>
<li><a href="https://electrazine.com/the-next-leap-in-semiconductors-the-1-4nm-process-node/">The Next Leap in Semiconductors : The 1 . 4 nm Process Node ...</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#semiconductors`, `#1.4nm`, `#fabrication`, `#industry-news`

---

<a id="item-16"></a>
## [NVIDIA RTX 50 系列显卡在韩国面临 20-30% 涨价](https://www.techpowerup.com/351329/nvidia-geforce-rtx-50-series-faces-30-price-increase-in-south-korea) ⭐️ 6.5/10

据传闻，NVIDIA 的 GeForce RTX 50 系列显卡在韩国可能面临 20-30% 的价格上涨，原因是供应商的 GDDR7 内存成本快速上升。韩国进口商和分销商已通知供应链即将进行的涨价，其中部分型号涨幅可能高达 30%。 此次涨价波及整个 RTX 50 产品线，高端型号受影响最大，可能使 RTX 5090 在韩国的售价超过 5,100 美元。尽管韩国拥有 SK hynix 和三星等主要 DRAM 生产商，但任何人都无法免受这些成本上涨的影响，这预示着 GPU 定价压力可能蔓延至其他市场。 NVIDIA 将 GDDR7 内存与 GPU 芯片作为套件提供给 AIB 合作伙伴，因此任何内存成本的上涨都会直接影响板卡厂商和消费者。以每 2GB GDDR7 模组售价 20 多美元计算，RTX 5090 需要 16 个模组，仅 GDDR7 内存成本就至少 320 美元，这还未计入 GPU 芯片、研发和 AIB 利润。

rss · TechPowerUp News · 8月3日 18:47

**背景**: GDDR7 是最新的图形双倍数据速率内存（graphics double data rate memory），相比 GDDR6 和 GDDR6X 提供更高的带宽，适用于高性能 GPU。Add-in Board（AIB）合作伙伴是指华硕、微星和技嘉等公司，它们从 NVIDIA 购买 GPU 芯片和组件来生产零售显卡。RTX 50 系列是 NVIDIA 最新的消费级 GPU 产品线，其中 RTX 5090 是旗舰型号，配备 32GB GDDR7 内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/in-a-troubling-sign-nvidia-rtx-50-series-prices-jump-up-to-30-percent-in-south-korea-tsmc-wafer-hikes-and-usd20-gddr7-modules-push-rtx-5090-past-usd5-100">In a troubling sign, Nvidia RTX 50 series prices jump... | Tom's Hardware</a></li>
<li><a href="https://grokipedia.com/page/Add-in_board">Add - in board</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#RTX-50-series`, `#GPU-pricing`, `#GDDR7-memory`, `#hardware-news`

---

<a id="item-17"></a>
## [铠侠发布 GP1 系列 PCIe 6.0 NVMe SSD，瞄准 AI 工作负载](https://www.techpowerup.com/351318/kioxia-announces-gp1-series-super-high-iops-ssds-for-ai-applications) ⭐️ 6.5/10

铠侠发布了 GP1 系列，这是其首款采用 XL-FLASH 第二代低延迟闪存的 PCIe 6.0 NVMe SSD，可实现高达 1000 万随机读取 IOPS，旨在作为基于闪存的存储层级来扩展 HBM，以满足 AI 系统的需求。评估样品将于 2026 年底向特定客户提供，并将在圣克拉拉举行的 FMS 2026 上公开展示。 GP1 瞄准的是 AI 基础设施中的关键瓶颈——GPU 内存容量。通过提供一个介于 HBM4 与传统 NAND 之间的高 IOPS 闪存层级，它承诺以远低于增加 HBM 的成本来扩展 GPU 可用的有效内存池，直接缓解大上下文和检索密集型 AI 工作负载的经济性问题。 关键规格包括 PCIe 6.0 接口、支持 GPU 直连访问、1000 万随机读取 IOPS，以及使用铠侠 XL-FLASH 第二代（基于低延迟 NAND 的存储级内存）。该产品定位为 HBM 扩展层级而非通用 SSD，并且要到 2026 年底才会向评估客户提供。

rss · TechPowerUp News · 8月3日 14:47

**背景**: XL-FLASH 是铠侠基于低延迟 NAND 的存储级内存（SCM），定位于 DRAM 与传统 NAND 之间的存储层级，访问速度远快于普通 SSD。高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，用于 GPU 和 AI 加速器，其中 HBM4 是最新一代，将用于 NVIDIA Rubin 等下一代芯片。内存分层（结合 HBM、SCM 类闪存和大容量 NAND）对于工作集超过 GPU 板载内存的 AI 工作负载越来越重要，而 PCIe 6.0 的每通道带宽是 PCIe 5.0 的两倍，这是让闪存层级在 AI 系统所需的 IOPS 水平下保持数据供给所必需的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.storagereview.com/news/kioxia-gp1-series-hits-10-million-random-read-iops-on-xl-flash-gen-2">KIOXIA GP1 Series Hits 10 Million Random Read IOPS on XL - FLASH ...</a></li>
<li><a href="https://blog-us.kioxia.com/post/2026/05/06/storage-class-memory-scm-explained-the-next-leap-in-memory-technology">Storage Class Memory (SCM) Explained – The Next... | KIOXIA Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SSD`, `#PCIe 6.0`, `#AI infrastructure`, `#storage`, `#Kioxia`

---

<a id="item-18"></a>
## [长鑫存储(CXMT)据报道计划在北京建设第二座晶圆厂以提升 DRAM 产能](https://www.techpowerup.com/351308/cxmt-reportedly-plans-second-fab-in-beijing-to-boost-dram-output) ⭐️ 6.5/10

中国 DRAM 制造商长鑫存储(CXMT)据报道正计划在北京建设第二座晶圆厂，将其晶圆月产能扩大三倍至 60 万片(WPM)，并获得地方政府资金支持。

rss · TechPowerUp News · 8月3日 09:45

**标签**: `#semiconductors`, `#DRAM`, `#memory`, `#China`, `#manufacturing`

---

<a id="item-19"></a>
## [AI 公司大幅下调 token 价格，应对中国模型的激烈竞争](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-now-racing-to-the-bottom-crashing-token-prices-and-competitive-models-push-companies-to-cut-costs) ⭐️ 6.5/10

所有主流 AI 开发商都在大幅下调 token 价格，以应对中国 AI 公司推出高效模型带来的竞争压力，这进一步压缩了本已微薄的利润率。据 CNBC 援引 OpenRouter 的数据，中国 AI 模型目前处理着美国企业 30%-46%的 API token 流量，而一年前这一比例仅为 4.5%；Coinbase 等公司通过将流量迁移至 DeepSeek，将其 AI 账单削减了一半。 这场价格战威胁着 AI 公司承诺的利润率以及投资者的回报预期，而正是这些承诺支撑着大量资本源源不断地涌入该行业。随着商品化进程加速、效率成为首要差异化因素，整个生成式 AI 的经济模式可能从高端软件利润率转向类似公用事业的定价模式。 AI 服务通常按每百万 token 计费，输入（提示）和输出（补全）采用不同费率，输出 token 的费用通常是输入 token 的数倍。竞争压力主要来自 DeepSeek 等中国开源权重模型，它们以极低的推理成本实现了相当甚至更优的性能，迫使西方厂商不得不通过价格而非纯能力来参与竞争。

rss · Tom's Hardware · 8月3日 16:26

**背景**: Token 是语言模型处理的基本单位，大致对应词片段、短词或标点符号，AI 服务根据 API 调用中消耗的 token 数量向用户收费。OpenAI、Anthropic 和 Google 等主要 AI 实验室的商业模式基于一个假设：先进的 AI 能力将享有溢价定价，这一假设在 2024 至 2025 年吸引了创纪录的投资。然而，高效的中国开源模型的出现打破了这个假设，它们证明了顶级性能可以以极低的成本交付，使得价格竞争不可避免。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing/">Models & Pricing | DeepSeek API Docs</a></li>
<li><a href="https://spoonai.me/posts/2026-07-11-chinese-ai-models-30-46pct-us-enterprise-tokens-cnbc-jul2026-en">Chinese AI Ate 30-46% of US Enterprise API Traffic... | spoonai</a></li>
<li><a href="https://agenticschool.dev/fundamentals/what-are-tokens.md">agenticschool.dev/fundamentals/ what - are - tokens .md</a></li>

</ul>
</details>

**标签**: `#ai-industry`, `#pricing`, `#market-dynamics`, `#competition`, `#china-tech`

---

<a id="item-20"></a>
## [2026 年用 4GB 显存的 Radeon RX 6500 XT 和 GTX 1650 Super 玩游戏——升频技术让低端 GPU 胜任电竞和网吧需求](https://www.tomshardware.com/pc-components/gpus/gaming-on-the-4gb-radeon-rx-6500-xt-and-gtx-1650-super-in-2026) ⭐️ 6.5/10

Tom's Hardware 测试了 2020 年发布的 4GB 显存显卡在 2026 年借助现代升频技术是否仍可用于游戏，背景是 AMD 颇具争议的 RX 9050 4GB 版本发布。

rss · Tom's Hardware · 8月3日 12:30

**标签**: `#gpu`, `#vram`, `#amd`, `#upscaling`, `#budget-gaming`

---