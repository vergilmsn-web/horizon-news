---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 39 条内容中筛选出 16 条重要资讯。

---

1. [QubesOS 通过 qvm-copy-to-vm 错误报告机制实现任意代码执行](#item-1) ⭐️ 8.0/10
2. [China's top DRAM maker CXMT sues Pentagon over its blacklisting — argues chips are standard civilian JEDEC spec, not defense hardware](#item-2) ⭐️ 7.5/10
3. [Pixel 11 取消硬件 MTE 支持；索尼和华纳起诉 Anthropic](#item-3) ⭐️ 7.3/10
4. [Omarchy Linux：任何用户进程可通过 Docker 组提权至 Root](#item-4) ⭐️ 7.0/10
5. [爬虫来袭](#item-5) ⭐️ 7.0/10
6. [欧盟委员会在"保护欧盟"战略中重提加密后门要求](#item-6) ⭐️ 7.0/10
7. [Bug 盲点](#item-7) ⭐️ 7.0/10
8. [SpaceX 将涡轮叶片制造转为内部生产，加速 AI 数据中心电力部署](#item-8) ⭐️ 6.5/10
9. [DIY 档案员用平价尼康相机和神经网络数字化 1800 本珍稀书籍](#item-9) ⭐️ 6.5/10
10. [海盗船 RM1000e（2026）评测：温感线缆防止 GPU 接口熔毁](#item-10) ⭐️ 6.5/10
11. [泄露版 DLSS 5 成功运行于 RTX 30 系显卡，但性能严重崩溃](#item-11) ⭐️ 5.5/10
12. [SteamOS 3.9.0 预览版发布，搭载 KDE 6.7.3 和 Linux 内核 7.2](#item-12) ⭐️ 5.5/10
13. [Intel 官方确认 Nova Lake-S 处理器将采用 LGA1954 插槽](#item-13) ⭐️ 5.5/10
14. [《大金刚 64》终于迎来完全原生的 C 语言 PC 移植版 —— DK64 ReKONGpiled 带来超宽屏支持、无帧率上限以及零 AI 代码](#item-14) ⭐️ 5.5/10
15. [玩家直接将电源线焊接到 RTX 5090 PCB 上以绕过烧毁的 16 针接口](#item-15) ⭐️ 5.5/10
16. [美国军方在南边境使用高能激光击落三架墨西哥贩毒集团无人机——毒贩涉嫌使用无人机进行监视和侦察以支持非法活动](#item-16) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [QubesOS 通过 qvm-copy-to-vm 错误报告机制实现任意代码执行](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 8.0/10

QubesOS 披露了一个严重的任意代码执行漏洞（QSB-118），存在于 `qvm-copy-to-vm` 工具的错误报告机制中，该机制调用了 `system()`，可被利用作为从特权域 Dom0 的反向通道。值得注意的是，VM 端的该工具变体不受影响，因为其错误报告函数未使用 `system()`。 该漏洞意义重大，因为 QubesOS 是一款以安全为核心的操作系统，被记者、活动人士和安全专业人员等高价值目标用户所依赖，他们依靠其隔离架构来保护敏感工作流。尽管 QubesOS 围绕最小化可信计算基进行设计，但一个相对普通的错误处理路径使用 `system()`，为代码执行回流到 Dom0 搭建了桥梁，动摇了核心安全假设。 该漏洞特指影响 `qvm-copy-to-vm` 在 Dom0 端的实现，其错误消息通过 `system()` 构造，允许攻击者控制的内容影响命令执行。由于 Dom0 对所有虚拟机拥有完全控制权，其内部的任何代码执行都是灾难性的；QubesOS 的最佳实践已建议不要在 Dom0 中执行日常操作，这大大限制了实际攻击面。

hackernews · vntok · 8月30日 08:51 · [社区讨论](https://news.ycombinator.com/item?id=49496918)

**背景**: QubesOS 是一款以安全为核心的操作系统，它使用基于 Xen 的虚拟化技术将不同活动隔离到独立的虚拟机（称为 qube）中。Dom0 是特权管理域，负责管理所有其他虚拟机并拥有对它们的完全访问权，是整个系统中安全敏感度最高的组件。`qvm-copy-to-vm` 工具通常用于在 qube 之间安全传输文件，其设计特性会对内容进行清理以防止数据跨隔室泄露。使用 `system()` 来格式化错误消息——这一模式早已被 OpenBSD 等注重安全的项目所摒弃——却意外地创造了代码执行的攻击路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://doc.qubes-os.org/en/latest/user/how-to-guides/how-to-copy-from-dom0.html">How to copy from dom0 — Qubes OS Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者对即使是攻击面极小的 QubesOS 也会出现此类漏洞表示惊讶，同时也指出该漏洞仅影响 Dom0 使用场景，在正常操作中这种情况应该很少见。多位用户引用了 OpenBSD 的 Theo DeRaadt 作为避免使用危险 API 的哲学先例，另一些用户则讨论了创始人 Joanna Rutkowska 的遗产以及缺乏 GPU 加速等实际局限性。尽管发生了此次披露，整体情绪仍对 QubesOS 保持积极，用户重申对其设计理念的信任。

**标签**: `#security`, `#qubesos`, `#vulnerability`, `#operating-systems`, `#exploit`

---

<a id="item-2"></a>
## [China's top DRAM maker CXMT sues Pentagon over its blacklisting — argues chips are standard civilian JEDEC spec, not defense hardware](https://www.tomshardware.com/pc-components/dram/chinas-top-dram-maker-cxmt-sues-pentagon-over-its-blacklisting-argues-chips-are-standard-civilian-jedec-spec-not-defense-hardware) ⭐️ 7.5/10

CXMT, China's leading DRAM manufacturer, is suing the Pentagon to remove itself from the Chinese military companies blacklist, arguing its chips are standard JEDEC-spec civilian hardware.

rss · Tom's Hardware · 8月30日 11:30

**标签**: `#semiconductors`, `#US-China-tech-war`, `#DRAM`, `#export-controls`, `#geopolitics`

---

<a id="item-3"></a>
## [Pixel 11 取消硬件 MTE 支持；索尼和华纳起诉 Anthropic](https://www.solidot.org/story?sid=85233) ⭐️ 7.3/10

GrapheneOS 发现 Google 的 Pixel 11 取消了对硬件 MTE（内存标记扩展）的支持，导致该项目无法支持该设备并建议用户不要购买。与此同时，索尼和华纳已对 Anthropic 提起诉讼，指控其使用数万首受版权保护的歌曲训练 Claude 模型，每部侵权作品索赔最高 15 万美元，案件最终赔偿可能高达数十亿美元。 Pixel 11 取消 MTE 是一次显著的安全倒退，尤其是在苹果 iPhone 17 默认启用内存完整性保护的情况下，这标志着两大旗舰平台在安全理念上的分歧。Anthropic 诉讼案是一项里程碑式的法律挑战，可能重塑 AI 公司处理受版权保护训练数据的方式，并对整个生成式 AI 行业产生深远影响。 Google 从 2023 年发布的 Pixel 8 起开始支持硬件 MTE，但 Android 和 Pixel OS 从未默认启用——GrapheneOS 为每个应用提供开关以启用 MTE。同时，Anthropic 诉讼指控联合创始人 Benjamin Mann 使用 BitTorrent 下载了超过 500 万本盗版书籍，Anthropic 员工从 Pirate Library Mirror 下载了超过 200 万本书，并从 MusixMatch 和 LyricFind 等授权服务抓取歌词。

rss · Solidot · 8月29日 23:44

**背景**: ARM 内存标记扩展（MTE）是 ARMv8.5-A 架构引入的硬件安全特性，通过为内存分配打标签来检测缓冲区溢出、释放后使用和其他内存安全漏洞。苹果在 iPhone 17 上推出的等效实现称为 Memory Integrity Enforcement（MIE），默认覆盖内核和超过 70 个用户态进程。GrapheneOS 是一个基于 AOSP 构建的注重隐私的开源移动操作系统，最初仅支持 Google Pixel 设备，但现在正扩展到使用高通骁龙 8 Elite Gen 5 芯片的摩托罗拉硬件，该芯片支持硬件 MTE。Anthropic 诉讼案是针对 AI 公司版权诉讼浪潮的一部分，类似于作者群体和《纽约时报》对 OpenAI 和微软提起的诉讼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://source.android.com/docs/security/test/memory-safety/arm-mte">Arm Memory Tagging Extension | Android Open Source Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://redact.dev/blog/iphone-17-memory-integrity-enforcement-explained">Memory Integrity Enforcement : iPhone 17 ’s Counter-Spyware System</a></li>

</ul>
</details>

**标签**: `#android-security`, `#mte`, `#grapheneos`, `#anthropic`, `#copyright-lawsuit`

---

<a id="item-4"></a>
## [Omarchy Linux：任何用户进程可通过 Docker 组提权至 Root](https://0xcc.io/posts/omarchy-root-creds/) ⭐️ 7.0/10

0xcc.io 发布的安全分析显示，Omarchy 的默认配置将用户加入 Docker 组，导致任何用户进程只需在容器内挂载宿主机文件系统即可轻易提权至 root。该文章还引用了此前披露的一个缺陷（commit 9285b19d），即 Omarchy 将原始 USB 描述符直接传入 shell，进一步加剧了人们对该发行版系统性安全问题的担忧。 此事值得关注，因为 Omarchy 是由 DHH（David Heinemeier Hansson）力推的、备受关注的基于 Arch 的定制发行版，在 YouTube 博主和开发者群体中引发了大量追捧。默认将用户加入 Docker 组的做法使得用户与 root 之间的权限边界形同虚设，破坏了大多数用户对桌面操作系统安全模型的预期。 Docker 组提权是一个长期被记录的经典攻击路径：属于 docker 组的用户只需执行 `docker run -v /:/mnt` 即可对宿主机的 `/etc/passwd` 和 `/etc/shadow` 进行读写操作，等同于获得 root 权限。Omarchy 此前的 USB shell 注入缺陷（将不可信的设备描述符直接传入 shell 执行）表明，问题可能不仅是单一的误配置，而反映出更广泛的输入验证不足问题。

hackernews · trap0xcc · 8月30日 15:59 · [社区讨论](https://news.ycombinator.com/item?id=49499854)

**背景**: Omarchy 是基于 Arch Linux 和 Hyprland Wayland 合成器构建的一款定制 Linux 发行版，由 DHH 于 2025 年 6 月 26 日发布，主要定位为开发者环境。所谓“vibe coding”（氛围编程）是指通过迭代式 LLM 提示词生成代码、而人工审查极少的 AI 辅助开发方式；当这种做法延伸到系统级配置时，批评者便将整个发行版称为“vibecoded”。Docker 组提权作为一个已知的权限提升路径已存在十多年，原因在于 Docker 守护进程本身需要对宿主机拥有 root 级控制能力——无 root 模式下的 Podman 等替代方案正是为了缓解这一风险而出现的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Omarchy">Omarchy - Wikipedia</a></li>
<li><a href="https://github.com/omacom/omarchy">GitHub - omacom/omarchy: Beautiful, Modern & Opinionated Linux · GitHub</a></li>
<li><a href="https://www.securitum.com/privilege_escalation_through_docker_group_membership_and_sudo_backdoor.html">privilege escalation through Docker group membership</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同将用户加入 docker 组是一个众所周知的危险配置，但用户 exitb 反驳说这并非 Omarchy 独有的问题，该错误配置在其他发行版中同样常见。mike_hearn 认为这在很大程度上只是“做样子的安全”，因为 Linux 缺乏完善的桌面沙箱机制，恶意进程无论是否被限制在 root 之外，仍能攻陷用户账户。其他人则推荐使用无 root 模式的 Podman 作为现代替代方案，并警告不要盲目采用被大肆宣传的“vibecoded”发行版，指出 CachyOS 此前也经历过类似的质疑。多位评论者建议直接使用原生 Arch 加 archinstall 安装，而不是依赖额外的定制化封装层。

**标签**: `#security`, `#linux`, `#privilege-escalation`, `#omarchy`, `#docker`

---

<a id="item-5"></a>
## [爬虫来袭](https://people.kernel.org/monsieuricon/creepy-crawlies) ⭐️ 7.0/10

本文探讨了通过 Anubis 等工作量证明系统抵御 AI 爬虫的愈演愈烈的攻防战，并援引社区专家的批评观点，指出算力强大的爬虫反而比普通用户更能轻松应对工作量证明挑战。

hackernews · zdw · 8月29日 17:49 · [社区讨论](https://news.ycombinator.com/item?id=49491791)

**标签**: `#bot-detection`, `#proof-of-work`, `#ai-scraping`, `#web-security`, `#anubis`

---

<a id="item-6"></a>
## [欧盟委员会在"保护欧盟"战略中重提加密后门要求](https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement) ⭐️ 7.0/10

欧盟委员会的"保护欧盟"战略重提强制要求加密设置后门以供执法部门访问，引发了人们对其在隐私、安全以及欧盟民主问责方面的担忧。

hackernews · nickslaughter02 · 8月30日 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49499394)

**标签**: `#encryption`, `#privacy`, `#EU-policy`, `#law-enforcement`, `#cybersecurity`

---

<a id="item-7"></a>
## [Bug 盲点](https://danluu.com/bug-blind/) ⭐️ 7.0/10

Dan Luu 的分析文章探讨了开发者和用户如何因与系统的心智模型不匹配而对 Bug "视而不见"，并以搜索引擎、效率工具及其他软件为例加以说明。

hackernews · davidmckenna · 8月30日 00:21 · [社区讨论](https://news.ycombinator.com/item?id=49494520)

**标签**: `#software-engineering`, `#ux`, `#debugging`, `#dan-luu`, `#cognitive-bias`

---

<a id="item-8"></a>
## [SpaceX 将涡轮叶片制造转为内部生产，加速 AI 数据中心电力部署](https://www.tomshardware.com/tech-industry/data-centers/spacex-starts-in-house-turbine-blade-manufacturing-to-boost-gas-powered-generator-output-for-elons-ai-data-centers-new-manufacturing-strategy-cuts-generator-delays-by-18-months) ⭐️ 6.5/10

SpaceX 已开始内部制造涡轮叶片和导叶，以应对关键的供应链瓶颈，据称此举将把其 AI 数据中心电力发电机的交付延迟缩短最多 18 个月。 这一垂直整合举措凸显了制约 AI 基础设施扩张的严峻电力供应瓶颈，也表明在 AI 算力需求激增的背景下，企业正采取非常规的制造策略来确保能源供应能力。 由于精密加工和先进材料要求，一套约 40 片先进涡轮叶片的成本可超过 60 万美元，制造周期长达 60 至 90 周，这也使全球燃气轮机行业高度集中在 GE Vernova 和西门子能源等少数厂商手中。

rss · Tom's Hardware · 8月30日 14:49

**背景**: 燃气轮机因其部署迅速、能够提供大规模可靠电力，正越来越多地被用作 AI 数据中心的备用或主要电源。AI 浪潮带来了前所未有的电力需求，为工业燃气轮机制造商创造了数十亿美元的商业机会，同时也暴露了严重的供应链瓶颈。涡轮叶片和导叶是涡轮发动机中最复杂的部件之一，需要精密铸造或增材制造、高温合金材料以及全面的质量保证。垂直整合是将此前外包的生产业务收回自营的策略，企业借此减少对外部供应商的依赖、缩短交货周期并改善质量控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.filtercoffee.co/stories/why-is-the-world-suddenly-short-on-gas-turbines">Why is the world suddenly short on gas turbines ? - Filter Coffee</a></li>
<li><a href="https://www.squaredtech.co/ai-data-centers-are-driving-a-major-gas-turbine-boom">AI Data Centers Powering The Biggest Gas Turbine Boom In Yea</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-cybersecurity-from-ground-up-part-6-gas-turbines-brendan-cronin-vzvse">AI cybersecurity from the ground up - Part 6 ' Gas Turbines '</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#manufacturing`, `#SpaceX`, `#power generation`

---

<a id="item-9"></a>
## [DIY 档案员用平价尼康相机和神经网络数字化 1800 本珍稀书籍](https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans) ⭐️ 6.5/10

一组 DIY 档案员将平价尼康相机的快门次数推至 90.2 万次，扫描了 1800 本珍稀书籍，生成了 52.6 万张扫描图像，随后用基于人工 Photoshop 编辑训练的神经网络进行处理。 该项目展示了将富有创意的 DIY 方法与定制机器学习相结合，如何以低成本实现大规模文化遗产保护，为昂贵机构数字化项目提供了一种替代方案。 相机被推至高达 90.2 万次快门的极限使用，远超普通消费级相机的寿命；神经网络专门针对 Photoshop 编辑进行训练，以自动化处理 52.6 万张扫描页面中繁重的人工后期工作。

rss · Tom's Hardware · 8月30日 12:00

**背景**: 快门次数是指相机机械快门触发的总次数；消费级相机通常额定寿命为 10 万到 30 万次快门，超过这个数字机械结构就可能失效，因此 90.2 万次快门属于极端压力测试。神经网络是一种从训练数据中学习模式的机器学习模型——在本项目中，团队向网络输入原始扫描图像及其人工 Photoshop 编辑结果的配对，让其学习自动应用校正。数字化珍稀书籍对于保护至关重要，因为实体书籍容易因老化、火灾和访问受限而受损。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://countmyshutter.com/?ref">Camera Shutter Counter | Check Your DSLR Shutter Count</a></li>
<li><a href="https://petapixel.com/camera-shutter-count/">How to Check Your Camera ’s Shutter Count | PetaPixel</a></li>

</ul>
</details>

**标签**: `#digital-preservation`, `#machine-learning`, `#computer-vision`, `#DIY-tech`, `#cultural-heritage`

---

<a id="item-10"></a>
## [海盗船 RM1000e（2026）评测：温感线缆防止 GPU 接口熔毁](https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review) ⭐️ 6.5/10

海盗船 2026 款 RM1000e 电源具备白金效率认证、500W 无风扇静音运行窗口，以及一根 ThermalProtect 12V-2x6 线缆，能够在接口过热熔毁之前自动关闭 GPU。ThermalProtect 线缆将过温保护（OTP）传感功能直接集成到线梳中，作为最后一道安全防线。 这项技术针对的是高功耗 GPU 上 12VHPWR/12V-2x6 接口熔毁这一已被广泛记录的问题，该问题已造成多起火灾并烧毁了价值数千美元的硬件。通过在线缆本身增加主动热关断保护，而非仅仅依赖接口设计的改进，海盗船提升了 GPU 供电安全的标准，并可能促使其他电源厂商跟进。 ThermalProtect 线缆有严格的安装方向要求——温度传感器必须朝向 GPU 一端连接才能正常工作，这是一个值得注意的安装注意事项。该线缆也作为独立配件单独出售，兼容任何配备原生 12V-2x6 接口的电源。

rss · Tom's Hardware · 8月30日 11:05

**背景**: 12VHPWR（12 伏高功率）接口是一种 16 针标准，专为向显卡传输高达 600W 电力而设计，用于取代高端 GPU 上的传统 8 针 PCIe 供电接口。由于接触不良、插入不均匀和制造缺陷导致接口熔毁的报告频发，业界将该标准修订为 12V-2x6，机械结构上更加耐用且更不易熔毁。然而，熔毁事故仍然时有发生，促使硬件厂商增加主动防护措施，例如温度传感器和自动关断电路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/power-supplies/corsair-rm1000e-2026-thermalprotect-power-supply-review">Corsair RM1000e (2026) ThermalProtect power... | Tom's Hardware</a></li>
<li><a href="https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/corsair-thermalprotect-technical-overview/">Technical overview of the CORSAIR ThermalProtect 12V-2x6 cable</a></li>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12 VHPWR - Wikipedia</a></li>

</ul>
</details>

**标签**: `#hardware`, `#power-supply`, `#corsair`, `#gpu-safety`, `#pc-components`

---

<a id="item-11"></a>
## [泄露版 DLSS 5 成功运行于 RTX 30 系显卡，但性能严重崩溃](https://www.techpowerup.com/352147/leaked-dlss-5-reaches-rtx-30-series-ampere-gpus-but-performance-falls-apart) ⭐️ 5.5/10

RenoDX Discord 上的 mod 社区成功将泄露版 DLSS 5 的 Neural Rendering 技术移植到官方不支持的 RTX 30 系 Ampere 显卡上，但效果几乎无法使用——RTX 3070 笔记本显卡在《天国：拯救 2》中的渲染延迟从约 29 毫秒飙升至超过 3300 毫秒；RTX 3080 在《Deep Rock Galactic》中帧率从约 130 FPS 暴跌至仅 4 FPS；RTX 3050 与 RTX 3060 Ti 在多款游戏中帧率徘徊在 1 FPS 左右。 这证实了 DLSS 5 的 Neural Rendering 严重依赖 Ampere 架构所不具备的硬件特性，表明 NVIDIA 几乎不可能官方将其回溯支持到 RTX 30 系，同时也凸显了 Blackwell 与上一代相比的性能差距——RTX 40 系尚可勉强运行，而 Ampere 则彻底崩溃。 根本原因在于 Ampere 架构缺乏原生 FP8（8 位浮点）支持，而泄露版 DLSS 5 模型依赖该精度用于 Tensor Core 运算，导致 GPU 无法高效处理 DLSS 5 所需的精度计算。官方 DLSS 5 目前仅支持 RTX 50 系 Blackwell 显卡，NVIDIA 尚未公布向 RTX 40 系添加支持的计划，更不用说更早的世代。

rss · TechPowerUp News · 8月30日 16:43

**背景**: NVIDIA DLSS（深度学习超采样）是一套由 RTX GPU 上的专用 Tensor Core 提供算力的神经渲染技术，旨在通过 AI 从低分辨率渲染重建高分辨率图像以提升帧率。DLSS 5 是 NVIDIA 在 GTC 2026 上发布的最新一代，采用 Neural Rendering 模型实时添加照片级光照和材质效果，计算负载远超前几代 DLSS 超采样技术。RTX 30 系 Ampere 架构于 2020 年发布，配备第三代 Tensor Core，不具备原生 FP8 吞吐能力，这一点与较新的 RTX 40 系 Ada Lovelace 和 RTX 50 系 Blackwell 架构不同，因此这些老显卡无法满足 DLSS 5 的算力需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ampere_(microarchitecture)">Ampere (microarchitecture) - Wikipedia</a></li>
<li><a href="https://wccftech.com/nvidia-dlss-5-neural-rendering-in-10-modern-games-the-best-unofficial-dlss-5-on-vs-off-comparisons-so-far/">NVIDIA DLSS 5 Neural Rendering In 10 Modern Games – The Best...</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#dlss-5`, `#rtx-30-series`, `#gpu`, `#modding`

---

<a id="item-12"></a>
## [SteamOS 3.9.0 预览版发布，搭载 KDE 6.7.3 和 Linux 内核 7.2](https://www.techpowerup.com/352133/steamos-3-9-0-preview-launches-with-kde-6-7-3-and-linux-kernel-7-2) ⭐️ 5.5/10

Valve 发布了 SteamOS 3.9.0 预览版，将桌面模式升级至 KDE Plasma 6.7.3（此前为 6.4.3），并将 Linux 内核更新至 7.2 版本。此次发布紧随最近的 3.8.26 测试版补丁，该补丁修复了桌面和游戏模式中的大量错误。 此次更新为 Steam Deck 和 SteamOS 用户带来了重要的组件升级，尤其是提升了 Intel Arc B390 核显性能，并引入了基于 USB4 的设备间文件共享功能。这表明 Valve 持续致力于优化 SteamOS 的桌面体验，以满足掌机和客厅娱乐两种使用场景。 KDE 6.7.3 升级带来了改进的 KRunner 搜索功能、剪贴板固定功能以及更好的数位板支持。据报道，Linux 内核 7.2 新增了 Intel USB4Stream 驱动程序，可通过 USB4 实现低延迟的设备间文件共享，并为 Intel Arc B390 核显带来显著的性能提升。同时 Valve 还对配置进行了修改，以提升日常使用体验。

rss · TechPowerUp News · 8月30日 05:14

**背景**: SteamOS 是 Valve 开发的基于 Linux 的操作系统，旨在将 Linux 的稳定性与为大屏幕和 Steam Deck 等掌机设备优化的游戏体验相结合。KDE Plasma 是一个功能丰富的桌面环境，围绕小组件构建，允许对用户界面进行广泛的自定义。KRunner 是 KDE Plasma 内置的启动器工具（可通过 Alt+Space 快捷键调用），支持快速启动应用程序、搜索和执行命令，并可通过称为"runners"的插件扩展其功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itsfoss.com/steamos/">What is SteamOS ? Everything You Need to Know</a></li>
<li><a href="https://kde.org/plasma-desktop/">Plasma is KDE 's desktop environment . Simple by default, powerful...</a></li>

</ul>
</details>

**标签**: `#SteamOS`, `#Linux`, `#KDE`, `#Valve`, `#Gaming`

---

<a id="item-13"></a>
## [Intel 官方确认 Nova Lake-S 处理器将采用 LGA1954 插槽](https://www.techpowerup.com/352121/intel-confirms-lga1954-as-the-socket-for-nova-lake-s-processors-through-internal-tools) ⭐️ 5.5/10

Intel 通过在其官网发布内部验证测试工具，正式确认即将推出的 Nova Lake-S Core Ultra 400 系列桌面处理器将采用 LGA1954 插槽。这是 Intel 首次以官方身份将 Nova Lake-S 与这一全新插槽联系在一起，新插槽替代了当前的 LGA1851。 此次确认让 PC 装机用户和硬件爱好者可以确定 Nova Lake-S 将需要全新的 Intel 900 系列主板，意味着当前的 LGA1851 主板将无法兼容下一代平台。同时这也标志着又一次插槽换代，将影响升级成本和散热器兼容性规划。 LGA1954 插槽将采用 2L-ILM（双杠杆独立加载机构）设计，在 CPU 两侧各设一个杠杆，以确保更好的接触平整度并减少 CPU 弯曲风险。根据泄露信息，Nova Lake-S 旗舰型号 SKU 可能包含最多 52 个核心，bLLC 缓存最高达 288 MB，平台预计将搭配 Z990 芯片组使用 DMI Gen 5 x4。

rss · TechPowerUp News · 8月29日 20:46

**背景**: Intel 桌面 CPU 使用 LGA（栅格阵列）插槽，针脚位于主板上而非 CPU 本身。每一代 Intel 桌面处理器通常都需要新的插槽，这反过来又需要新的主板。LGA1851 随 Arrow Lake / Core Ultra 200S 系列一同推出，Nova Lake-S 代表下一次重大架构飞跃，预计将于 2027 年第一季度发布。2L-ILM 插槽设计是对 LGA1700 平台过去出现的 CPU 弯曲和接触压力不均问题的回应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/roundup/intel-nova-lake-s/">Intel Nova Lake: Full Specs , Release Date & Lineup (Up to 52 Cores...)</a></li>
<li><a href="https://www.hwcooling.net/en/nova-lake-to-feature-new-2l-ilm-socket-to-prevent-cpu-bending/">Nova Lake to feature new 2 L - ILM socket to prevent CPU bending</a></li>

</ul>
</details>

**标签**: `#Intel`, `#Nova Lake-S`, `#LGA1954`, `#CPU`, `#hardware`

---

<a id="item-14"></a>
## [《大金刚 64》终于迎来完全原生的 C 语言 PC 移植版 —— DK64 ReKONGpiled 带来超宽屏支持、无帧率上限以及零 AI 代码](https://www.tomshardware.com/video-games/retro-gaming/donkey-kong-64-finally-gets-a-fully-native-pc-port-written-in-c-dk64-rekongpiled-brings-ultrawide-support-uncapped-framerates-and-zero-ai-code) ⭐️ 5.5/10

资深开发者打造了基于 C 语言的《大金刚 64》原生 PC 移植版，支持超宽屏和无帧率上限，值得注意的是该过程中未使用任何生成式 AI。

rss · Tom's Hardware · 8月30日 14:26

**标签**: `#retro-gaming`, `#reverse-engineering`, `#pc-port`, `#donkey-kong-64`, `#cross-platform`

---

<a id="item-15"></a>
## [玩家直接将电源线焊接到 RTX 5090 PCB 上以绕过烧毁的 16 针接口](https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling) ⭐️ 5.5/10

巴西 YouTuber TecLab 在一块裸板的影驰 HOF（名人堂）RTX 5090 显卡上直接将电源线焊接到 PCB 上，完全绕过了臭名昭著的 16 针 12VHPWR 接口，据称在压缩机冷却下该卡功耗达到 600W。 这一极端的改装方案凸显了英伟达的 16 针接口烧毁问题在历经两代显卡后依然严重且持续，也反映出社区对这一问题在新一代旗舰 RTX 5090 上仍未得到彻底解决的强烈不满。 这种改装反而可能比烧毁的接口本身带来更大的火灾风险，因为在 600W 大电流负载下手工焊接的电线连接绕过了接口所有的安全设计和接触特性。影驰 HOF 系列显卡专为超频爱好者和挑战极限性能而设计。

rss · Tom's Hardware · 8月30日 10:30

**背景**: 16 针 12VHPWR 接口随 RTX 4090 一同推出，旨在通过单根线缆为 GPU 提供更高功率，但很快因接触不良或插接不当导致的烧毁事件而臭名昭著。RTX 5090 显卡继续沿用这一接口标准，烧毁报告也延续到了新一代产品上。影驰的 HOF（Hall of Fame）名人堂系列是面向极限超频的旗舰产品，这也解释了为什么 TecLab 将焊接改装与压缩机冷却搭配使用，以维持显卡 600W 的功耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/news/rtx-4090-16-pin-connector-melted-after-one-year-of-usage">RTX 4090's 16 - Pin Connector Melted After One... | Tom's Hardware</a></li>
<li><a href="https://galax.com/en/category/graphics-cards/hall-of-fame-series/">Hall of Fame ( HOF ) - GALAX</a></li>
<li><a href="https://ww-article-cache-1.s3.amazonaws.com/en/16-pin_12VHPWR_connector">ww-article-cache-1.s3.amazonaws.com/en/ 16 - pin _ 12 VHPWR ...</a></li>

</ul>
</details>

**标签**: `#RTX 5090`, `#GPU modding`, `#hardware issues`, `#16-pin connector`, `#PC hardware`

---

<a id="item-16"></a>
## [美国军方在南边境使用高能激光击落三架墨西哥贩毒集团无人机——毒贩涉嫌使用无人机进行监视和侦察以支持非法活动](https://www.tomshardware.com/tech-industry/drones/us-military-uses-high-energy-lasers-to-shoot-down-three-mexican-cartel-drones-over-the-southern-border-narcos-suspected-of-using-uavs-for-surveillance-and-reconnaissance-to-support-illegal-activities) ⭐️ 5.5/10

美国军方使用高能激光系统，击落了三架正在南边境进行监视侦察的墨西哥贩毒集团无人机。

rss · Tom's Hardware · 8月30日 10:00

**标签**: `#directed-energy-weapons`, `#counter-UAS`, `#defense-technology`, `#drones`, `#military`

---