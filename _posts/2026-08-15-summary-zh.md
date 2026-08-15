---
layout: default
title: "Horizon Summary: 2026-08-15 (ZH)"
date: 2026-08-15
lang: zh
---

> 从 75 条内容中筛选出 20 条重要资讯。

---

1. [单条指令漏洞攻破 AMD 15h/16h 系列 CPU 硬件安全防线](#item-1) ⭐️ 8.5/10
2. [Qwen 3.8 27B](#item-2) ⭐️ 8.0/10
3. [台积电实现 0.42 纳米栅极突破，赋能二维 MoS₂晶体管](#item-3) ⭐️ 8.0/10
4. [英伟达为下一代"费曼"GPU 锁定台积电 A16 制程](#item-4) ⭐️ 7.5/10
5. [英特尔副总裁 Robert Hallock 设定 Nova Lake 预期，暗示将重返 Raptor Lake 以支持 DDR4 平台 — 完整 1 对 1 采访实录](#item-5) ⭐️ 7.5/10
6. [乌克兰声称在俄罗斯巡航导弹中发现英伟达 Jetson 芯片——S-71 "Monochrome" 武器中可能使用了 AI 技术](#item-6) ⭐️ 7.5/10
7. [走向黑暗：执法机构黑客时代的来临](#item-7) ⭐️ 7.0/10
8. [硬件安全专家发文批评 RISC-V 指令集架构设计决策](#item-8) ⭐️ 7.0/10
9. [Claude Opus 5 沟通体验下降：后期训练转向智能体优化](#item-9) ⭐️ 7.0/10
10. [谷歌推动同态加密迈向实用的隐私 AI](#item-10) ⭐️ 7.0/10
11. [RustDesk 新增对 Wayland 的真正无人值守远程访问支持](#item-11) ⭐️ 7.0/10
12. [ASML 四十年光刻霸权之路与无掩膜技术变革来临](#item-12) ⭐️ 7.0/10
13. [英特尔在 AI 驱动的内存热潮中再次面临抉择](#item-13) ⭐️ 7.0/10
14. [Google 以主要成员身份加入 OpenROAD 计划](#item-14) ⭐️ 7.0/10
15. [长江存储跻身 NAND 芯片出货量前三](#item-15) ⭐️ 7.0/10
16. [原告在法庭文件中使用 AI 提示注入被识破](#item-16) ⭐️ 6.5/10
17. [美国对外国制造无人机征收最高 100%关税，重点针对中国](#item-17) ⭐️ 6.5/10
18. [AMD 借款 47.5 亿美元用于'一般企业用途'——未透露将如何使用这笔资金](#item-18) ⭐️ 6.5/10
19. [Firefox 成为最后一个支持完整版 uBlock Origin 的主流浏览器](#item-19) ⭐️ 6.0/10
20. [推出 Toast 1](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [单条指令漏洞攻破 AMD 15h/16h 系列 CPU 硬件安全防线](https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas) ⭐️ 8.5/10

安全研究人员披露了一个影响 2015 年发布 AMD CPU（15h 和 16h 系列芯片家族）的漏洞，仅需一条指令即可绕过硬件安全边界，获取对 Platform Security Processor（PSP）、微代码（microcode）以及 System Management Interface 区域的完整硬件级访问权限。该漏洞破解了通常与用户和操作系统隔离的秘密内存区域。 这个漏洞的影响非常严重，因为它攻破的正是那些专门用于实施硬件级安全防护的组件，可能允许拥有本地代码执行权限的攻击者植入持久化的固件级恶意软件，此类恶意软件即使重装操作系统也无法清除，并且对传统杀毒软件完全不可见。尽管受影响的 CPU 来自 2015 年，但它们仍被用于遗留系统、嵌入式设备、游戏主机以及长生命周期的企业部署中。 15h 系列包括 AMD FX 系列桌面处理器和部分 Opteron 服务器芯片，而 16h 系列则包含用于 PlayStation 4 和 Xbox One 等设备中的低功耗 Jaguar 和 Puma 架构 SoC，以及部分 Athlon、Sempron 和 Opteron-X 芯片。PSP 约于 2013 年引入，目前品牌名为 AMD Secure Technology，作为可信执行环境子系统运行，因此对其未经授权的访问构成了芯片安全架构中尤为严重的入侵。

rss · Tom's Hardware · 8月14日 09:33

**背景**: AMD Platform Security Processor（PSP）是一个独立于主 x86 核心运行的嵌入式 ARM 微控制器，负责启动时认证、固件验证和加密运算等任务。它类似于 Intel 的 Management Engine，长期以来一直是安全研究和隐私讨论的对象。受影响的芯片系列——15h（基于 Bulldozer/Piledriver/Steamroller 架构的 FX 芯片）和 16h（Jaguar/Puma APU）——代表了那个时代 AMD 的主流和嵌入式产品线。能够跨越主 CPU 与安全协处理器之间边界的硬件级漏洞十分罕见，通常意味着芯片设计中的内存保护或地址映射隔离机制存在缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AMD_Platform_Security_Processor">AMD Platform Security Processor - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas">Just one instruction on AMD 's 2015-era CPUs gets... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#hardware-security`, `#cpu-vulnerability`, `#amd`, `#exploit`, `#platform-security`

---

<a id="item-2"></a>
## [Qwen 3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Qwen 发布 Qwen 3.8 27B，这是一款新的开源权重模型，因在本地硬件上具备强大的推理能力以及独特的极简思维链风格而备受关注。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**标签**: `#Qwen`, `#open-source-llm`, `#local-ai`, `#reasoning-models`, `#model-release`

---

<a id="item-3"></a>
## [台积电实现 0.42 纳米栅极突破，赋能二维 MoS₂晶体管](https://semiwiki.com/semiconductor-manufacturers/tsmc/372146-a-0-42-nanometer-breakthrough-from-tsmc-could-push-transistors-beyond-silicon/) ⭐️ 8.0/10

台积电企业研究与国立阳明交通大学的研究人员成功构建了一层厚度仅为 0.42 纳米的氧化铝界面层，在保护单层 MoS₂晶体管电子输运的同时实现了强大的栅极控制能力。该氧化铝层通过精确氧化铝金属获得，形成了一个原子级厚度的优质基底，可用于后续电介质材料的生长。 随着传统硅制程逼近物理极限，这一突破表明全球领先的代工厂正在认真布局后硅晶体管技术。如果单层 MoS₂晶体管能够走向量产，将有望推动超薄低功耗器件和柔性电子产品的持续性能提升。 这层 0.42 纳米的氧化铝薄膜是位于主栅极电介质下方的界面层，其极薄的特性得以保持二维 MoS₂沟道中电子的迁移率，避免其性能退化。该成果仍处于研究阶段，要实现大规模量产仍需克服晶圆级 MoS₂生长、缺陷控制以及与现有晶圆厂设备兼容性等方面的重大挑战。

rss · SemiWiki · 8月14日 15:00

**背景**: 硅基晶体管数十年来一直是半导体产业的基石，但当特征尺寸缩小到几纳米以下时，量子效应和漏电流使进一步微缩变得越来越困难。二维材料如二硫化钼（MoS₂）——即一层钼原子夹在两层硫原子之间——提供了原子级厚度的沟道，有望实现进一步的小型化、更高的载流子迁移率以及优异的机械柔韧性。二维晶体管设计的一个关键挑战在于栅极电介质：控制沟道的绝缘层必须极薄但同时均匀且不破坏脆弱的二维晶格。氧化铝（Al₂O₃）正是此类界面中被广泛研究的高κ电介质候选材料之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/2d-semiconductors-molybdenum-disulfide">2D Chip Breakthrough: 6,000 Transistors, 3 Atoms Thick - IEEE Spectrum</a></li>
<li><a href="https://www.nycu.edu.tw/nycu/en/app/news/view?module=headnews&id=552&serno=149da2b1-c125-4a91-a84f-1e21e369f762">NSTC, NYCU, and TSMC Break Key Barrier in 2 D Semiconductors</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11728206/">Advances in 2D Molybdenum Disulfide Transistors for Flexible and Wearable Electronics - PMC</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#TSMC`, `#transistor-technology`, `#2D-materials`, `#MoS2`

---

<a id="item-4"></a>
## [英伟达为下一代"费曼"GPU 锁定台积电 A16 制程](https://www.techpowerup.com/351607/nvidia-secures-tsmc-a16-node-for-next-generation-feynman-gpus) ⭐️ 7.5/10

英伟达正在台积电 A16 1.6 纳米制程上原型设计其 Rubin 之后的"费曼"GPU 架构，采用背面供电和先进的 3D 芯粒封装技术，目标在 2028 年下半年实现量产。

rss · TechPowerUp News · 8月14日 09:56

**标签**: `#NVIDIA`, `#TSMC`, `#GPU`, `#semiconductor-manufacturing`, `#advanced-packaging`

---

<a id="item-5"></a>
## [英特尔副总裁 Robert Hallock 设定 Nova Lake 预期，暗示将重返 Raptor Lake 以支持 DDR4 平台 — 完整 1 对 1 采访实录](https://www.tomshardware.com/pc-components/cpus/intel-vp-robert-hallock-sets-nova-lake-expectations-teases-return-to-raptor-lake-for-ddr4-platforms-our-full-1-1-interview-transcript) ⭐️ 7.5/10

Tom's Hardware 采访了英特尔副总裁 Robert Hallock，话题涉及 Nova Lake 的预期、对内存价格危机的应对策略，以及重返 Raptor Lake 以支持 DDR4 平台的战略决策。

rss · Tom's Hardware · 8月14日 11:00

**标签**: `#Intel`, `#Nova Lake`, `#Raptor Lake`, `#DDR4`, `#CPU architecture`

---

<a id="item-6"></a>
## [乌克兰声称在俄罗斯巡航导弹中发现英伟达 Jetson 芯片——S-71 "Monochrome" 武器中可能使用了 AI 技术](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-jetson-chip-found-in-russian-cruise-missile-ukraine-claims-presence-in-s-71-monochrome-weapon-may-indicate-use-of-ai-tech) ⭐️ 7.5/10

乌克兰情报部门声称俄罗斯新型 S-71 "Monochrome" 巡航导弹使用英伟达 Jetson Orin NX 模块进行基于 AI 的末端制导，这引发了人们对商业 AI 硬件用于武器系统的质疑。

rss · Tom's Hardware · 8月14日 10:30

**标签**: `#AI-hardware`, `#military-tech`, `#Nvidia`, `#export-controls`, `#autonomous-weapons`

---

<a id="item-7"></a>
## [走向黑暗：执法机构黑客时代的来临](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/) ⭐️ 7.0/10

本文由一位顶级密码学研究人员撰写，深入分析了"走向黑暗"加密辩论以及执法机构黑客时代的到来，探讨了后门、漏洞市场以及加密技术与政府访问权限之间的矛盾。

hackernews · vslira · 8月14日 20:52 · [社区讨论](https://news.ycombinator.com/item?id=49304447)

**标签**: `#cryptography`, `#encryption`, `#security-policy`, `#privacy`, `#law-enforcement`

---

<a id="item-8"></a>
## [硬件安全专家发文批评 RISC-V 指令集架构设计决策](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV) ⭐️ 7.0/10

一位受人尊敬的硬件安全研究员 Dmitry 发表了一篇详细的技术批评文章，指出尽管 RISC-V 作为一个开放、不受知识产权限制的标准具有重要价值，但其在 ISA 设计上的一些决策缺乏远见。 这一批评为广泛存在的 RISC-V 炒作提供了有价值的技术反叙事，来自领域专家的实质性技术反馈可能会影响未来 ISA 的修订和整个生态系统中的实现决策。 该批评聚焦于 ISA 层面的具体设计选择，而非质疑 RISC-V 的模块化扩展理念或开放标准的前提。在实践中，实现者通常必须扩展基线配置（例如从 RV64IMA 扩展到 RV64GC）才能启动主流 Linux 发行版，这需要额外的组件如 softfloat 库。

hackernews · kaycebasques · 8月14日 22:38 · [社区讨论](https://news.ycombinator.com/item?id=49305492)

**背景**: RISC-V 是一个基于 RISC（精简指令集计算机）原则的免费开放标准指令集架构（ISA），不同于 x86（英特尔/AMD）和 ARM 等专有 ISA。它被刻意设计为可通过众多可选扩展进行扩展，允许实现者根据从微型传感器芯片到超级计算机的应用场景选择所需功能。RISC-V 有意省略了条件码和进位标志以简化 CPU 设计，并支持多种配置如 RV32I/RV64I（基础整数）、M（整数乘除）、A（原子操作）、F/D（浮点）、C（压缩指令）以及 G（整合上述所有功能的通用组合）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC - V - Wikipedia</a></li>
<li><a href="https://www.slideshare.net/slideshow/riscv-introduction/54217700">RISC - V Introduction | PPTX</a></li>
<li><a href="https://www.eetindia.co.in/the-rise-of-risc-v-processor-designs/">The Rise of RISC - V Processor Designs - EE Times India</a></li>

</ul>
</details>

**社区讨论**: 社区回应总体上务实而理性。业余 CPU 设计者主要看重 RISC-V 的开放标准地位和主流编译器支持，认为实际局限性可以通过扩展来弥补。多位评论者指出，RISC-V 的重要性——尤其是中国大力投资的原因——源于其开放标准属性而非技术优越性，它证明了开放公共架构是可行的。一些人将其与 MIPS 类比，认为 RISC-V 的真正价值在于为开放硬件树立了先例，而实现者确认扩展 ISA 配置（例如从 RV64IMA 到 RV64GC）虽然必要但可管理，足以运行真实世界的软件。

**标签**: `#RISC-V`, `#ISA design`, `#computer architecture`, `#hardware`, `#open-source hardware`

---

<a id="item-9"></a>
## [Claude Opus 5 沟通体验下降：后期训练转向智能体优化](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 7.0/10

如果前沿模型厂商确实把后期训练优化重点从人类对话转向智能体之间的通信，这预示着整个行业向智能体工作流转型时付费用户将面临更广泛的体验风险，并可能促使客户转向对话风格更友好的竞品。 具体抱怨包括：句子绕了一大圈再把关键点当作「顿悟」抛出、频繁「坦诚」错误、以及在没有严格提示时方向飘忽不定；值得注意的是 Opus 5 保持了与 Opus 4.8 相同的每百万 token 5/25 美元定价，但部分用户认为质量反而下降了。

hackernews · numeri · 8月14日 10:12 · [社区讨论](https://news.ycombinator.com/item?id=49296740)

**背景**: 「后期训练」（post-training）是在基础语言模型预训练之后，通过 RLHF、DPO、GRPO 等技术调整模型的语气、乐于助人程度和推理行为，使其与下游目标对齐。随着 AI 智能体在工作流中的角色日益重要，行业开始讨论类似传统用户体验的「智能体体验」（Agent Experience, AX），即模型越来越多地与其他模型协作而非直接与人类用户交互。Claude Opus 5 是 Anthropic 面向高难度推理、编码和长程智能体任务的旗舰模型，拥有 100 万 token 上下文窗口和 12.8 万 token 最大输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://luwai.fr/en/resources/claude-opus-5-cout-agents-ia-pme-2026-07-26">Claude Opus 5 : Anthropic 's Most Capable AI Model in 2026</a></li>
<li><a href="https://penfriend.ai/blog/optimizing-content-for-llm">Optimizing Content For LLMs : LLMO Strategies To Rank In AI -Driven...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同新风格令人疲惫，对直接的人类使用适得其反，有几位明确表示已转向竞品模型。最具实质性的讨论推测，后期训练目标已偏离人类用户，转向智能体之间通信所用的「智能体语言」，鉴于用户难以忍受其默认行为，这一担忧引发了强烈共鸣。

**标签**: `#AI`, `#Claude`, `#LLM`, `#user-experience`, `#AI-agents`

---

<a id="item-10"></a>
## [谷歌推动同态加密迈向实用的隐私 AI](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 7.0/10

谷歌宣布致力于让同态加密在隐私保护 AI 推理中变得实用，目标是实现对加密数据的计算而无需暴露原始信息。该举措旨在弥合密码学隐私保障与现实世界 AI 部署之间长期存在的差距。 如果成功，同态加密可以让用户在不向服务提供商暴露敏感数据的前提下使用强大的云端 AI 模型，从而应对日益增长的监管和消费者隐私担忧。这一进展对任何希望在不暴露明文数据的情况下使用 AI 的个人、医疗或专有数据处理机构都至关重要。 同态加密在传统上会带来约 10^3 倍的计算开销，相比明文推理这引发了关于能耗和商业可行性的严重质疑。谷歌尚未公布具体的延迟、吞吐量或模型规模基准，以证明其已具备实际部署的成熟度。

hackernews · u1hcw9nx · 8月14日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49300314)

**背景**: 同态加密是一种密码学技术，允许直接在加密数据（密文）上执行数学运算，产生的加密结果在解密后与在明文上运算的结果相同。这使其对隐私保护机器学习非常有吸引力，服务器可以在用户的加密输入上运行模型推理，而无需看到原始数据。隐私 AI 推理广义上指在用户控制的或以保密方式保留用户数据的基础设施上运行模型，通常与将数据发送到第三方服务器的公共云 API 形成对比。其他隐私保护技术包括联邦学习、安全多方计算和差分隐私，每种技术在安全保障、准确性和计算成本之间都有不同的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.freecodecamp.org/news/homomorphic-encryption-in-plain-english/">How Homomorphic Encryption Works – Explained in Plain English</a></li>
<li><a href="https://www.wardleymaps.ai/library/privacy-preserving-ai-unlocking-the-power-of-secure-machine-learning-9509ccd5-7a28-40">Privacy - Preserving AI: Unlocking the Power of Secure Machine ...</a></li>
<li><a href="https://cloudserv.ai/private-ai-inference-clouds-why-enterprises-are-shifting-from-public-apis/">Private AI Inference Clouds: Why Enterprises Are Shifting From Public...</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体上持怀疑态度，主要围绕三个主题。在技术层面，评论者指出同态加密目前带来约 1000 倍的计算开销，使其能耗高且商业可行性未经证实。在实践层面，一些用户认为真正的隐私 AI 应该直接在本地硬件上运行，而不是依赖云服务提供商。对谷歌整体隐私实践的不信任进一步放大了怀疑情绪，批评者指出谷歌密码管理器默认未启用端到端加密，并积极阻止匿名化工具的使用。

**标签**: `#homomorphic-encryption`, `#privacy-preserving-ml`, `#google`, `#cryptography`, `#ai-security`

---

<a id="item-11"></a>
## [RustDesk 新增对 Wayland 的真正无人值守远程访问支持](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk 新增了对 Wayland 显示协议的真正无人值守远程访问支持，克服了此前在运行 Wayland 的 Linux 系统上需要用户交互才能建立远程连接的安全限制。 这一更新意义重大，因为 Wayland 在 Linux 桌面上的采用正在加速，GNOME 50 已完全转向 Wayland，这意味着缺少无人值守 Wayland 支持的远程桌面工具在服务器维护和 IT 支持场景中将越来越不实用。 该功能绕过了 Wayland 的安全模型，该模型限制屏幕捕获和输入注入以防止未授权应用访问。尽管取得了这一进展，社区成员指出，与商业替代方案相比，客户端到主机的麦克风透传和自托管部署的端到端加密仍未实现。

hackernews · rustdesk · 8月14日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=49300759)

**背景**: Wayland 是 Linux 用来取代旧版 X11 系统的现代显示协议，通过限制应用程序与显示器的交互方式，提供更好的安全性、稳定性和图形性能。无人值守远程访问意味着可以在无用户在场的情况下远程连接设备，通常通过预先安装的代理实现，这对 IT 管理和全天候服务器维护至关重要。RustDesk 是用 Rust 编写的开源远程桌面应用，定位于 TeamViewer 和 AnyDesk 等商业方案的替代品，完全支持自托管中继服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustdesk.com/">RustDesk: Open-Source Remote Desktop with Self-Hosted Server...</a></li>
<li><a href="https://github.com/rustdesk/rustdesk">GitHub - rustdesk / rustdesk : An open - source remote desktop ...</a></li>
<li><a href="https://www.baeldung.com/linux/wayland-explained">What Is Wayland in Ubuntu? | Baeldung on Linux</a></li>

</ul>
</details>

**社区讨论**: 社区反响普遍积极，长期用户表示满意，一位评论者提到在修复发布前两天就遇到了这个完全相同的限制。但也提出了关于剩余功能差距的实质性担忧：自托管加密（在 GitHub issue #3714 中跟踪）和客户端到主机的麦克风输入透传功能相比商业方案仍然缺失。

**标签**: `#rustdesk`, `#wayland`, `#remote-desktop`, `#open-source`, `#linux`

---

<a id="item-12"></a>
## [ASML 四十年光刻霸权之路与无掩膜技术变革来临](https://semiwiki.com/lithography/372177-asmls-path-to-lithography-dominance-and-the-coming-maskless-revolution/) ⭐️ 7.0/10

SemiWiki 发表了一篇深度分析文章，回顾了 ASML 如何从 1984 年的飞利浦-ASM 合资企业发展为全球光刻霸主，依靠四十年的系统工程、供应商协同以及对竞争对手认为过于昂贵的光刻技术转型进行反复战略押注。该文还探讨了可能挑战 ASML 市场地位的新兴无掩膜光刻技术。 ASML 是 EUV 光刻系统的唯一供应商，该系统对于生产 7nm 及以下最先进芯片至关重要，因此其战略地位对整个半导体供应链极为关键。任何可行的无掩膜替代方案都可能重塑价值数十亿美元的光刻设备市场，并改变先进芯片制造的经济格局。 ASML 当前的旗舰 NXE 和 EXE EUV 系统使用波长约 13.5 纳米的极紫外光来对先进芯片进行图案化，这一能力经过数十年研发才进入大规模量产阶段。相比之下，无掩膜光刻利用直接数字控制来写入图案，无需物理光掩模，既提供设计灵活性，又消除了掩模制造成本——对于小批量或快速迭代的生产来说是一个显著优势。

rss · SemiWiki · 8月14日 13:00

**背景**: 光刻是半导体制造中的核心图案化工艺，利用光将电路图案从光掩模转移到硅晶圆上，可实现小至数纳米的特征尺寸。采用 13.5 纳米波长光的 EUV 光刻代表了当前最前沿的技术，使最高制程节点芯片的大规模量产成为可能。总部位于荷兰的 ASML 是全球唯一生产商用 EUV 光刻系统的公司，这源于其与 Zeiss、Trumpf 等供应商长达数十年的投资和生态协作。目前仍局限于特定细分领域和分辨率范围的无掩膜光刻，正因能够绕过昂贵掩模组的优势而日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://en.wikipedia.org/wiki/Photolithography">Photolithography - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Maskless_lithography">Maskless lithography</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#lithography`, `#ASML`, `#chip-manufacturing`, `#industry-analysis`

---

<a id="item-13"></a>
## [英特尔在 AI 驱动的内存热潮中再次面临抉择](https://www.eetimes.com/intel-at-a-memory-crossroads-again/) ⭐️ 7.0/10

EE Times 报道，英特尔正考虑重新加大内存芯片业务投入，因为人工智能正将内存从低利润的大宗商品转变为具有战略价值的高价值资源。这是英特尔与内存之间漫长而周期性关系的最新篇章——英特尔曾在 1985 年退出 DRAM 市场，并在 1990 年代末短暂重返。 英特尔可能重返内存市场标志着在 AI 硬件热潮驱动下的重大战略转变，高带宽内存（HBM）已成为 AI 加速器的关键瓶颈。如果英特尔做出这一承诺，将加剧与三星、SK 海力士和美光等成熟内存厂商在利润丰厚的 HBM 领域的竞争，可能重塑整个内存行业格局。 英特尔与内存有着悠久的历史：公司于 1969 年推出了首款商用 SRAM（3101），1970 年推出了首款商用 DRAM（1103），但在 1985 年因来自日本竞争对手的低价冲击遭受重大亏损后退出 DRAM 市场。当前的 AI 内存热潮核心是 HBM——堆叠在处理器旁边的 DRAM——它正日益被视为限制 AI 加速器可扩展性的带宽瓶颈。

rss · EE Times · 8月14日 13:01

**背景**: 英特尔最初于 1968 年由罗伯特·诺伊斯和戈登·摩尔创立，是一家内存公司，也是商用 DRAM 的先驱。1985 年退出 DRAM 业务后，英特尔转型为 x86 CPU 的主导供应商。AI 时代对高带宽内存（HBM）产生了前所未有的需求——HBM 是一种堆叠式 DRAM 的专用形式，置于 GPU 等 AI 加速器旁边，以极高速度为其提供数据——使内存从大宗商品转变为战略瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eetimes.com/intel-at-a-memory-crossroads-again/">Intel at a Memory Crossroads, Again - EE Times</a></li>
<li><a href="https://www.indexbox.io/blog/intels-memory-comeback-from-dram-pioneer-to-ai-driven-innovation/">Intel Returns to Memory : CEO Lip-Bu Tan Hints at New... - IndexBox</a></li>
<li><a href="https://www.taskade.com/wiki/infrastructure/hbm">HBM : The Stacked Memory Beside Every AI Chip | Taskade AI</a></li>

</ul>
</details>

**标签**: `#Intel`, `#semiconductors`, `#memory-chips`, `#AI-hardware`, `#industry-analysis`

---

<a id="item-14"></a>
## [Google 以主要成员身份加入 OpenROAD 计划](https://www.electronicsweekly.com/news/design/eda-and-ip/google-joins-openroad-eda-initiative-2026-08/) ⭐️ 7.0/10

Google 已作为主要成员加入 OpenROAD 计划（ORI），以支持开源电子设计自动化（EDA）工具的开发。作为此次合作的一部分，Google 的技术项目经理 Aaron Cunningham 已加入该计划的治理机构。 Google 作为主要成员的加入为开源 EDA 生态系统带来了大量资金资源、工程人才和行业信誉——该生态自 2023 年底才开始完全自给自足。作为拥有自有 TPU 和 Tensor 硬件项目的主要芯片设计商，Google 的参与标志着开源工具在生产级半导体设计中正获得越来越多的主流认可。 OpenROAD 项目旨在提供完全自动化的端到端数字集成电路设计流程（从 RTL 到 GDSII），无需人工干预——这一能力传统上由 Cadence、Synopsys 和 Siemens EDA 等专有供应商主导。ORI 本身是一个 501(c)(3) 非营利组织，致力于开源 EDA 生态系统的长期管理和治理。

rss · Electronics Weekly · 8月14日 14:01

**背景**: 电子设计自动化（EDA）是指用于设计几乎所有现代电子设备和芯片的软件工具；没有这些工具，现代半导体的复杂性将无法手动管理。OpenROAD 项目（自主设计的开放实现）是一个重要的开源计划，提供完整的从 RTL 到 GDSII 的数字设计流程，旨在通过减少对昂贵专有工具的依赖来实现芯片设计的民主化。OpenROAD 计划（ORI）是管理和维护该生态系统的非营利组织，已于 2023 年底实现完全自给自足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openroadinitiative.org/">OpenROAD Initiative - Making chip design open and accessible</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenROAD_Project">OpenROAD Project - Wikipedia</a></li>
<li><a href="https://wiki.f-si.org/index.php?title=OpenROAD_and_The_OpenROAD_Initiative:_Foundations_for_Open_Innovation">OpenROAD and The OpenROAD Initiative : Foundations for Open ...</a></li>

</ul>
</details>

**标签**: `#EDA`, `#OpenROAD`, `#open-source`, `#semiconductors`, `#chip-design`

---

<a id="item-15"></a>
## [长江存储跻身 NAND 芯片出货量前三](https://www.electronicsweekly.com/news/business/ymtc-in-big-3-for-nand-units-2026-08/) ⭐️ 7.0/10

长江存储在第二季度超越美光和铠侠，以 14%的单位出货量市场份额夺得第三名，仅次于三星和 SK 海力士。

rss · Electronics Weekly · 8月14日 05:12

**标签**: `#semiconductors`, `#NAND-flash`, `#memory-market`, `#YMTC`, `#industry-news`

---

<a id="item-16"></a>
## [原告在法庭文件中使用 AI 提示注入被识破](https://www.tomshardware.com/tech-industry/artificial-intelligence/plaintiff-busted-trying-to-use-ai-prompt-injection-to-win-court-case-hides-text-instruction-in-filing-demands-ai-model-reviewing-the-text-should-side-with-him-rumbled-because-of-strange-white-spaces-in-text) ⭐️ 6.5/10

康涅狄格州法院一名自行代理诉讼的原告试图在其法律文件中嵌入隐藏的 AI 提示注入攻击，指示任何审查该文件的 AI 模型支持其立场。由于隐藏文本产生了可疑的空白字符，这一企图被识破并失败。 这是公开记录中首批在法律场景中尝试提示注入的案例之一，凸显了随着 AI 工具越来越多地被用于审查、总结或处理专业文档时出现的真实风险。该事件表明，被 OWASP 列为顶级 LLM 安全威胁的提示注入问题，已经从软件系统扩展到了法律、政府和行政工作流程中。 该法院禁止原告进行电子提交，要求其将打印好的纸质文件交给法院书记官，这表明原告假设 AI 系统仍会处理扫描或 OCR 后的文档。隐藏指令因打印文本中出现异常的空白模式而暴露，这是隐藏字符或零宽字符（常用于提示注入尝试）的典型迹象。

rss · Tom's Hardware · 8月14日 12:23

**背景**: 提示注入（Prompt Injection）是一种对抗性攻击，利用大语言模型（LLM）无法区分可信的系统指令和不可信的用户输入这一弱点。攻击者通过在文本中嵌入隐藏或伪装后的指令，可以操纵 LLM 使其忽略原始指令而执行被注入的内容。与越狱（Jailbreak）攻击（旨在绕过模型内置的安全过滤器）不同，提示注入针对的是构建在模型之上的应用程序行为。OWASP 已将提示注入列为基于 LLM 的应用程序面临的顶级安全风险之一，并且现实中的案例已经出现在电子邮件助手、网页摘要工具等多个领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection | OWASP Foundation</a></li>
<li><a href="https://www.evidentlyai.com/llm-guide/prompt-injection-llm">What is prompt injection ? Example attacks, defenses and testing.</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#legal tech`, `#cybersecurity`, `#AI ethics`

---

<a id="item-17"></a>
## [美国对外国制造无人机征收最高 100%关税，重点针对中国](https://www.tomshardware.com/tech-industry/drones/us-imposes-up-to-100-percent-tariffs-on-foreign-made-drones-and-components-china-remains-primary-target-as-washington-moves-to-reduce-reliance-on-overseas-suppliers) ⭐️ 6.5/10

特朗普政府对外国制造的无人机及其组件征收最高 100%的关税，中国被列为主要目标。政府表示此举是出于国家安全考虑，同时希望减少美国对海外供应商（尤其是中国供应商）的依赖。 该政策可能显著重塑全球无人机供应链，大幅提高依赖进口无人机的美国消费者和企业的成本，同时可能促进美国本土无人机制造业的发展。这也标志着美中科技贸易紧张关系的进一步升级，影响范围可能不仅限于无人机领域，还可能波及无人机以外的其他电子和硬件行业。 这些关税同时适用于整机无人机和单个组件，使得通过分别进口零部件再进行本地组装来规避关税的做法变得困难。目前依赖中国制造无人机的公司——尤其是主导全球消费级和商用无人机市场的大疆（DJI）——在美国市场将面临大幅上涨的成本。

rss · Tom's Hardware · 8月14日 11:53

**背景**: 美国无人机市场长期由中国制造商主导，大疆（DJI）在全球商用和消费级无人机市场占据最大份额。多年来，美国立法者和机构一直对中国制造的无人机提出数据安全和监控方面的担忧，导致此前已出台限制政府使用的相关措施。关税是对进口商品征收的税款，100%的关税实际上使进口商品的到岸成本翻倍。此举是美中贸易摩擦这一更广泛格局的一部分，此前已经波及半导体、电信设备和电动汽车等领域。

**标签**: `#tariffs`, `#drones`, `#trade-policy`, `#supply-chain`, `#hardware-industry`

---

<a id="item-18"></a>
## [AMD 借款 47.5 亿美元用于'一般企业用途'——未透露将如何使用这笔资金](https://www.tomshardware.com/pc-components/cpus/amd-borrows-usd4-75-billion-for-general-corporate-purposes-company-gives-no-insight-into-how-it-plans-to-spend-cash-injection) ⭐️ 6.5/10

AMD 宣布计划筹集 47.5 亿美元债务，但未披露资金用途，引发外界对其战略意图的种种猜测。

rss · Tom's Hardware · 8月14日 09:48

**标签**: `#AMD`, `#semiconductors`, `#corporate-finance`, `#industry-news`, `#hardware`

---

<a id="item-19"></a>
## [Firefox 成为最后一个支持完整版 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 6.0/10

Firefox 现在是唯一仍然支持完整版 uBlock Origin 的主流浏览器，因为 Chrome 和其他基于 Chromium 的浏览器正在完成向 Manifest V3 的迁移，而后者大幅限制了广告拦截器的功能。基于 Chromium 的浏览器现在只能使用功能被削减的 uBlock Origin Lite 版本。 这一变化实际上缩小了用户对强大广告拦截功能的选择，因为 Manifest V3 的 declarativeNetRequest API 取代了更灵活的 webRequest API，阻止扩展实时拦截和修改网络请求。注重隐私的用户和依赖精细内容过滤功能的开发者可能会被迫转向 Firefox，或在其他浏览器上接受被削弱的拦截能力。 Manifest V3 的核心变化是，将支持拦截功能的 webRequest API 替换为 declarativeNetRequest API，后者只允许扩展向浏览器声明过滤规则，而不能自行拦截请求。社区有一个非官方的移植版本（r58Playz 在 GitHub 上的 uBlock-mv3），旨在在 MV3 上恢复完整版 uBlock Origin 功能，但它仅在企业侧载配置下可用，因为 webRequestBlocking 权限受到限制。

hackernews · DemiGuru · 8月14日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49303202)

**背景**: uBlock Origin 是由 Raymond Hill 创建的一款免费、开源的内容过滤扩展，被广泛认为是目前最有效、最轻量的广告拦截工具之一。Manifest V3 是 Chrome、Edge、Opera 和 Safari 采用的最新扩展平台规范；虽然 Firefox 也计划支持 MV3，但它保留了与旧版 Manifest V2 API 的兼容性，使得完整版 uBlock Origin 等传统扩展能够继续运行。webRequest API 允许扩展观察、拦截或修改网络请求，这对高级广告拦截至关重要，而 declarativeNetRequest 则将过滤职责转移为由浏览器评估的静态规则集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://extensionworkshop.com/documentation/develop/manifest-v3-migration-guide/">Manifest V 3 migration guide | Firefox Extension Workshop</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍批评 Google 的 Manifest V3 迁移，认为这是对扩展自由的有意瓦解。评论者强调了 Firefox 对热门扩展进行安全审查的做法，提到了非官方的 uBlock Origin MV3 移植版本作为替代方案，并指出 uBlock Origin Lite 用户并未报告重大缺陷，但也有开发者表示 Manifest V3 迫使他们彻底关闭了自己的项目。

**标签**: `#browsers`, `#ad-blocking`, `#firefox`, `#chrome`, `#manifest-v3`

---

<a id="item-20"></a>
## [推出 Toast 1](https://www.mixedbread.com/blog/toast-1) ⭐️ 6.0/10

Mixedbread 推出 Toast 1，这是一款专用于搜索任务的大语言模型，引发了关于专用搜索模型与通用方法之间优劣的讨论。

hackernews · mplappert · 8月14日 15:07 · [社区讨论](https://news.ycombinator.com/item?id=49299746)

**标签**: `#llm`, `#search`, `#specialized-models`, `#mixedbread`, `#ai-infrastructure`

---