---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 43 条内容中筛选出 11 条重要资讯。

---

1. [伊朗涉嫌攻击美国 45 个市政供水系统，各部门被迫切换手动控制](#item-1) ⭐️ 7.5/10
2. [Dasharo v0.9.0 为 AMD AM5 平台带来开源固件](#item-2) ⭐️ 7.5/10
3. [谷歌地球 AI 生图功能上线不到 48 小时即被叫停](#item-3) ⭐️ 7.3/10
4. [Go 1.27 交互式导览](#item-4) ⭐️ 7.0/10
5. [字节跳动发布 Seedance 2.5，支持一镜到底创作](#item-5) ⭐️ 7.0/10
6. [Diátaxis](#item-6) ⭐️ 7.0/10
7. [AMD Zen 6 处理器传闻通过单核优化解决游戏微卡顿问题](#item-7) ⭐️ 6.5/10
8. [Kioxia 发布 CM10 系列：PCIe Gen6 企业级 SSD](#item-8) ⭐️ 6.5/10
9. [近 120 万辆特斯拉汽车遭调查](#item-9) ⭐️ 6.3/10
10. [中国大模型包揽 OpenRouter 周调用量榜单前五名](#item-10) ⭐️ 6.3/10
11. [微软承诺在内存短缺背景下让 Windows 11 在 8GB 内存上流畅运行——减少操作系统内存占用的优化工作已启动](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [伊朗涉嫌攻击美国 45 个市政供水系统，各部门被迫切换手动控制](https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control) ⭐️ 7.5/10

美国 45 个市政供水设施遭受疑似来自伊朗的网络攻击。尽管系统仍在运行，但许多受影响的供水部门（主要是小型城镇）已恢复手动控制以保障供水安全。 此次事件凸显了美国关键基础设施面对国家级网络威胁时的脆弱性，以及供水系统被攻陷后可能造成的严重公共健康后果。小型市政部门成为攻击的主要目标，是因为它们通常缺乏大型供水企业所拥有的网络安全资源和专业能力。 攻击目标主要针对供水处理和分配系统中常用的 SCADA（数据采集与监视控制系统）和 PLC（可编程逻辑控制器）。根据 CISA 的警告，伊朗相关的 APT 组织被发现利用互联网暴露的 PLC 来操纵 HMI 和 SCADA 显示，类似于 2021 年佛罗里达州 Oldsmar 水处理设施攻击和 2024 年德州多起供水设施攻击事件。

rss · Tom's Hardware · 8月2日 13:10

**背景**: 供水企业依赖 SCADA 系统和 PLC 来监控和自动化水处理过程，包括化学品投加、压力调节和分配。对这些系统的网络攻击可以操纵化学品剂量——正如 2021 年佛罗里达州 Oldsmar 事件中，攻击者试图增加氢氧化钠（烧碱）含量；也可能通过溢出水箱造成物理损害，如 2024 年德州发生的事件。CISA 和 FBI 已将伊朗确定为针对美国关键基础设施（特别是能源和水务领域的工业控制设备）的持续性网络威胁来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a">Iranian-Affiliated Cyber Actors Exploit Programmable Logic Controllers Across US Critical Infrastructure | CISA</a></li>
<li><a href="https://www.wired.com/story/iran-linked-hackers-are-sabotaging-us-energy-and-water-infrastructure/">Iran-Linked Hackers Are Sabotaging US Energy and Water Infrastructure | WIRED</a></li>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a">Compromise of U.S. Water Treatment Facility | CISA</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#critical-infrastructure`, `#cyberattacks`, `#geopolitics`, `#water-utilities`

---

<a id="item-2"></a>
## [Dasharo v0.9.0 为 AMD AM5 平台带来开源固件](https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850) ⭐️ 7.5/10

3mdeb 发布了 Dasharo v0.9.0，这是 AMD AM5 平台的首个开源固件，结合了 Coreboot 与 AMD 的 openSIL 硅初始化库。它面向 MSI B850 主板上的 Zen 4 APU，首批适配型号为 MSI B850-P WiFi。 这一发布打破了 AMD 在现代消费级桌面平台上长期封闭的固件生态，让用户获得固件层面的透明度、可审计性，并摆脱厂商锁定。它代表着开源固件在基于 Zen 架构的消费级硬件上更广泛采用过程中的重要一步。 作为早期 v0.9.0 版本，目前仅支持一款 MSI B850 主板，更广泛的板卡覆盖与功能完善仍需后续开发。Dasharo 依托 3mdeb 成熟的 CI/CD 流水线，以及在超过 50 万台商用 x86 设备上部署开源固件的丰富经验。

rss · Tom's Hardware · 8月2日 12:10

**背景**: Coreboot 是一个开源项目，提供轻量级固件以替代专有的 BIOS/UEFI，仅执行交给操作系统前所需的最基本硬件初始化。AMD openSIL 由三个静态链接库（xSIM、xPRF、xUSL）组成，用于抽象硅初始化流程，使同一套底层代码能够同时链接到 UEFI 或 Coreboot 固件中。Dasharo 由 3mdeb 开发，是一款产品化的开源固件分发方案，强调可信性、隐私与透明度。AMD 的 AM5 是该公司当前的消费级插槽，支持基于 Zen 4 架构的 Ryzen 7000/9000 系列 CPU 与 APU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.dasharo.com/">About Dasharo - Dasharo Universe</a></li>
<li><a href="https://www.amd.com/en/blogs/2023/empowering-the-industry-with-open-system-firmware-.html">Empowering The Industry with Open System Firmware – AMD openSIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coreboot">coreboot - Wikipedia</a></li>

</ul>
</details>

**标签**: `#open-source`, `#coreboot`, `#firmware`, `#AMD`, `#AM5`

---

<a id="item-3"></a>
## [谷歌地球 AI 生图功能上线不到 48 小时即被叫停](https://36kr.com/newsflashes/3922077104664199?f=rss) ⭐️ 7.3/10

谷歌在上线谷歌地球 AI 图像生成功能不到 48 小时后便将其紧急暂停，因为用户生成的 AI 图像违反了公司政策，且专家警告该工具可能被滥用，把虚构场景叠加在真实卫星图像上以传播虚假信息。 这一事件凸显了快速部署 AI 功能与落实安全防护之间的矛盾，尤其是在像谷歌地球这样被记者和研究人员作为视觉证据来源的可靠平台上。它也是一个典型的现实案例，展示了生成式 AI 被滥用时如何侵蚀公众对既有媒体平台的信任。 据报道该功能基于 Nano Banana 2 模型，允许用户将 AI 生成的图像锚定到真实的地理坐标上。一个被广泛传播的示例是在吉萨大金字塔上数字插入了一个虚假的天坑；部分图像虽然标注了"AI-GENERATED"（AI 生成）警示横幅，但仍显示出潜在的滥用风险。

rss · 36氪 · 8月2日 07:51

**背景**: 谷歌地球是一个广泛使用的地理空间平台，提供卫星和航空影像，是记者、研究人员和公众信赖的参考工具。当前的生成式 AI 图像模型能够生成高度逼真的合成图像，由此引发了关于"深度伪造"（deepfake）的担忧——即以真实信息面貌呈现的 AI 生成内容。当此类合成图像与真实地理坐标的可信度相结合时，所产生的虚假信息可能格外有说服力，且难以被揭穿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c9349yx2ydvo">Google withdraws Earth AI tool after misinformation warnings</a></li>
<li><a href="https://www.storyboard18.com/digital/google-rolls-back-google-earth-ai-image-generation-feature-a-day-after-launch-over-policy-concerns-106286.htm">Google rolls back Google Earth AI image generation feature a day...</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/9288/google-earth-ai-fake-satellite-imagery-rollback">Google Earth : the Button That Generated Fake Satellite Images ...</a></li>

</ul>
</details>

**社区讨论**: 网络上的反应大多是批评和讽刺，LinkedIn 和科技论坛上的评论者嘲笑谷歌在一个被视为视觉证据可靠来源的平台上部署 AI 图像生成器这一明显存在风险的做法。许多人对即使只是短暂的可用窗口也足以产生误导性图像表示担忧，还有人质疑谷歌是否在上线前未能预见到这种滥用场景。

**标签**: `#AI safety`, `#Google Earth`, `#misinformation`, `#responsible AI`, `#generative AI`

---

<a id="item-4"></a>
## [Go 1.27 交互式导览](https://victoriametrics.com/blog/go-1-27/index.html) ⭐️ 7.0/10

Go 1.27 新功能的交互式导览，包括泛型改进、Android 的 MTE 兼容性修复，以及自动的 HTTP 响应体排空处理，并附有深入的社区讨论。

hackernews · Hixon10 · 8月2日 01:35 · [社区讨论](https://news.ycombinator.com/item?id=49140218)

**标签**: `#Go`, `#programming-languages`, `#release-notes`, `#generics`, `#runtime`

---

<a id="item-5"></a>
## [字节跳动发布 Seedance 2.5，支持一镜到底创作](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ⭐️ 7.0/10

字节跳动发布了其视频生成模型的最新版本 Seedance 2.5，主打一镜到底创作能力，可在单次生成中产出长达 30 秒的音视频片段，并具备灵活的参考引用功能与多轮扩展支持。 此次发布在快速发展的 AI 视频生成领域具有重要意义，字节跳动借助其在 TikTok 时代积累的短视频经验，推动了生成时长与画质的提升。该模型与 MiniMax H3 等竞品直接竞争，也表明闭源商业模型与开源权重模型之间的差距正在持续缩小。 Seedance 2.5 可在单次生成中产出高质量的 30 秒音视频片段，并支持多轮扩展。与转向真正多模态控制的 Seedance 2.0 不同，该版本更强调精简的一镜到底工作流；社区讨论指出，该模型似乎主要针对中国市场偏好的动作与特效文本生成视频场景进行了深度优化。

hackernews · njaremko · 8月1日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=49138302)

**背景**: Seedance 是字节跳动的旗舰 AI 视频生成模型系列，属于其更广泛的 "Seed" 基础模型套件的一部分。该模型家族依托字节跳动通过 TikTok 处理数十亿条短视频所积累的丰富经验，从 1.0 版本的文本与图像单镜头生成，发展到 2.0 版本的真正多模态控制。灵活的参考引用功能允许用户上传参考图像、视频或音频来引导生成结果——这一能力现已成为 MiniMax H3 和 Google Gemini Omni 等竞品的标配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">One - take Creation, Flexible Referencing: Introducing Seedance 2.5</a></li>
<li><a href="https://seed.bytedance.com/en/seedance">Seedance</a></li>
<li><a href="https://hailuoai.video/tools/minimax-h3">MiniMax H3 Multimodal AI Video Model | Hailuo AI</a></li>

</ul>
</details>

**社区讨论**: 社区反响热烈但观点不一。多位评论者称赞 Seedance 2.5 的输出质量，不过也有人指出字节跳动的优化方向偏向中国市场需求——侧重动作和特效类文本生成视频，而非西方电影人所需的视频转视频对话密集型工作流。另一些评论者则对不断攀升的推理成本表示担忧（一位用户报告在生成 5 万张图像和近一小时视频上花费超过 1 万美元），还有评论者提到开源权重竞品 MiniMax H3 将在 24 小时内发布，且能在 3080 等中端消费级显卡上运行。少数声音对生成式视频工具的整体社会价值提出了质疑。

**标签**: `#video-generation`, `#bytedance`, `#generative-ai`, `#text-to-video`, `#ai-models`

---

<a id="item-6"></a>
## [Diátaxis](https://diataxis.fr/) ⭐️ 7.0/10

Diátaxis 是一个文档框架,将内容分为四种不同的类型(教程、操作指南、参考和阐释),每种类型都有其特定的用途和写作风格。

hackernews · ryanseys · 8月1日 20:33 · [社区讨论](https://news.ycombinator.com/item?id=49138188)

**标签**: `#documentation`, `#technical-writing`, `#methodology`, `#knowledge-management`, `#developer-experience`

---

<a id="item-7"></a>
## [AMD Zen 6 处理器传闻通过单核优化解决游戏微卡顿问题](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets) ⭐️ 6.5/10

据新报告透露，AMD 即将推出的 Zen 6 处理器将引入针对单核心的热设计与功耗预算优化，这些优化单独来看似乎并不起眼，但叠加起来有望显著减少游戏中的微卡顿并提升 1% 低帧率表现。 如果消息属实，这些优化将有效改善 AMD 下一代平台的游戏体验，解决困扰现代 CPU 的帧率波动问题，并有望让 AMD 在游戏负载场景中相较 Intel 获得竞争优势。 这些改进目前基于未经证实的爆料而非 AMD 官方公告，并且单核心热设计与功耗管理与解决 C-state 以及节能特性相关——历史上这些特性正是导致游戏微卡顿的常见原因之一。

rss · Tom's Hardware · 8月2日 12:30

**背景**: 微卡顿是指打断游戏流畅度的短暂不规则帧延迟，通常由 CPU 的功耗管理特性（如 C-state 让核心频繁进出休眠状态）引起。1% 低帧率指的是最差 1% 帧的平均帧率，是衡量玩家感知流畅度的关键指标，重要性超过平均帧率。AMD 的 Zen 架构自 2017 年以来一直是 Ryzen 处理器的基础，每一代都在 IPC（每时钟周期指令数）、缓存体系与能效方面有所提升。Zen 6 预计将接替 Zen 5，有望采用最多 12 核心的 CCD 设计与更大的 48MB L3 缓存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.noobfeed.com/hardware/amd-zen6-ryzen-zen5-x3d-am5-support">AMD Zen 6 Ryzen Could Match Zen 5 X3D While... | NoobFeed</a></li>
<li><a href="https://linustechtips.com/topic/1228554-cpu-microstuttering-due-to-dxgmms2sys/">CPU microstuttering due to dxgmms2.sys - CPUs ... - Linus Tech Tips</a></li>
<li><a href="https://superuser.com/questions/1382406/experiencing-microstutters-in-all-games-after-changing-to-rtx-2070-video-card">cpu - Experiencing microstutters in all games after... - Super User</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Zen 6`, `#CPU`, `#gaming performance`, `#PC hardware`

---

<a id="item-8"></a>
## [Kioxia 发布 CM10 系列：PCIe Gen6 企业级 SSD](https://www.servethehome.com/kioxia-cm10-series-launched-for-the-pcie-gen6-generation-of-ssds/) ⭐️ 6.5/10

Kioxia 发布了 CM10 系列 SSD，涵盖 2.5 英寸和 EDSFF 两种外形规格，同时支持 PCIe Gen5 和 Gen6 接口，提供风冷和液冷两种散热方案，并采用了两代不同的 NAND 闪存。 CM10 系列是首批原生支持 PCIe Gen6 的企业级 SSD 产品线之一，标志着数据中心 Gen6 升级周期正式开启。丰富的外形规格与散热方案组合为超大规模和企业客户在不同部署场景（包括对存储吞吐要求极高的 AI 工作负载）中提供了灵活性。 该系列同时覆盖传统的 2.5 英寸盘位和较新的 EDSFF（Enterprise and Datacenter Storage Form Factor，企业与数据中心存储外形规格），后者具备更好的散热气流、更高的容量和更便捷的可维护性。通过在同一产品家族中同时支持 PCIe Gen5 和 Gen6，Kioxia 让当前一代平台的用户可以立即部署这些 SSD，同时保留向 Gen6 服务器迁移的路径。

rss · ServeTheHome · 8月1日 15:00

**背景**: PCIe Gen 6 采用 PAM4 编码，将单通道信号速率提升至 64 GT/s，在 x16 链路上可实现约 128 GB/s 的单向吞吐量，这对需要传输海量数据的 AI 训练和推理工作负载至关重要。EDSFF 是专为超大规模和企业数据中心设计的较新 SSD 外形规格，相比传统 2.5 英寸设计具有更好的散热特性和更高的密度。Kioxia 是全球最大的 NAND 闪存制造商之一，其企业级 SSD 产品线通常与三星、Solidigm 和美光的产品竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/pcie-gen6-and-gen5-will-both-matter-for-ai-storage/">PCIe Gen 6 and Gen5 Will Both Matter for AI Storage - ServeTheHome</a></li>
<li><a href="https://www.ssstc.com/knowledge-detail/edsff-enterprise-ssd-form-factor/">EDSFF :E1/ E3 Enterprise SSD Form Factors ｜SSSTC</a></li>
<li><a href="https://www.supermicro.com/en/glossary/edsff">What Is Enterprise and Datacenter SSD Form Factor ? | Supermicro</a></li>

</ul>
</details>

**标签**: `#SSDs`, `#PCIe Gen6`, `#Kioxia`, `#enterprise storage`, `#hardware`

---

<a id="item-9"></a>
## [近 120 万辆特斯拉汽车遭调查](https://36kr.com/newsflashes/3922152130653828?f=rss) ⭐️ 6.3/10

美国国家公路交通安全管理局（NHTSA）针对近 120 万辆特斯拉 Model 3 和 Model Y 车辆展开调查，原因是这些车辆据报道存在悬挂系统故障，可能导致车辆失控。

rss · 36氪 · 8月2日 09:30

**标签**: `#Tesla`, `#NHTSA`, `#automotive safety`, `#electric vehicles`, `#regulatory investigation`

---

<a id="item-10"></a>
## [中国大模型包揽 OpenRouter 周调用量榜单前五名](https://36kr.com/newsflashes/3921989528432259?f=rss) ⭐️ 6.3/10

据全球多模型聚合平台 OpenRouter 最新发布的周度 AI 大模型调用量榜单，排名前五的产品全部由中国企业的模型包揽。小米 MiMo-V2.5 以单周 10.5 万亿 Token 的调用量登顶，环比增长 12%；腾讯混元 3 于 7 月 6 日正式开源，单周环比增幅超 999%，跃居第三，成为榜单中增长势头最猛的模型。 该榜单反映出全球大模型竞争格局的重大转变：中国模型已不再局限于区域市场，而是在中立第三方平台上主导了开发者的实际调用量。腾讯混元 3 等近期才开源的模型调用量迅速攀升，表明中国厂商正缩小差距，并有可能在开发者心智占有率上超越西方的闭源模型。 DeepSeek 凭借两款模型同时占据第二和第五名，形成高低搭配以覆盖不同开发需求，其旗舰 Pro 版本据称在代码和复杂智能体任务上可对标海外顶级闭源模型。所有上榜模型均在发布后极短时间内快速冲榜，凸显了中国厂商在抢占 API 市场份额方面的攻势之强。

rss · 36氪 · 8月2日 06:14

**背景**: OpenRouter is a developer-focused AI infrastructure platform that acts as a unified API gateway to 400+ large language models from multiple providers, used by 250k+ apps and over 4.2 million users globally. Token count is the standard unit for measuring LLM usage, where tokens represent the smallest pieces of text (words, subwords, or characters) a model processes — so 10.5 trillion tokens in one week represents an enormous volume of real-world inference activity. DeepSeek is a Hangzhou-based Chinese AI company that has gained international attention for building competitive open-weight LLMs at reportedly low training and inference costs.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter ? A Guide with Practical Examples | Codecademy</a></li>

</ul>
</details>

**标签**: `#AI`, `#Chinese-AI`, `#OpenRouter`, `#LLM-market`, `#industry-news`

---

<a id="item-11"></a>
## [微软承诺在内存短缺背景下让 Windows 11 在 8GB 内存上流畅运行——减少操作系统内存占用的优化工作已启动](https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun) ⭐️ 5.5/10

微软正在优化 Windows 11，以减少其内存占用并在 8GB 内存系统上更流畅地运行，这可能是由于持续的内存芯片短缺以及 8GB 笔记本电脑的回归所推动的。

rss · Tom's Hardware · 8月1日 14:48

**标签**: `#Windows 11`, `#Microsoft`, `#RAM optimization`, `#PC hardware`, `#operating systems`

---