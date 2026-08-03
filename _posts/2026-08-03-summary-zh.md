---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 47 条内容中筛选出 10 条重要资讯。

---

1. [伊朗涉嫌对美国 45 个市政水务系统发动网络攻击](#item-1) ⭐️ 7.5/10
2. [Dasharo v0.9.0 为 AMD AM5 平台带来首款开源固件](#item-2) ⭐️ 7.5/10
3. [中国侵入式脑机接口公司「主动科技」创纪录完成 3.3 亿元天使轮融资](#item-3) ⭐️ 7.3/10
4. [Karpathy 的鹈鹕](#item-4) ⭐️ 7.0/10
5. [AMD 即将推出的 Zen 6 处理器有望解决游戏微卡顿问题并提升 1%最低帧率——下一代 CPU 据称将具备单核热与功耗预算优化](#item-5) ⭐️ 6.5/10
6. [「幺正量子」完成数亿元 A 轮融资](#item-6) ⭐️ 6.3/10
7. [铠侠计划于 2025 年量产支持 PCIe 6.0 和 UFS 5.0 的下一代 AI NAND 产品](#item-7) ⭐️ 6.3/10
8. [Kakehashi：面向 Linux ARM 的实验性 macOS 二进制兼容层](#item-8) ⭐️ 6.0/10
9. [F*：面向形式化验证的证明式编程语言](#item-9) ⭐️ 6.0/10
10. [华硕展示搭载 Intel Panther Lake 的 NUC 16 迷你电脑家族](#item-10) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [伊朗涉嫌对美国 45 个市政水务系统发动网络攻击](https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control) ⭐️ 7.5/10

伊朗涉嫌对美国 45 个市政供水设施发动网络攻击，小型城镇为主要目标。尽管水务系统仍在运行，但多家供水企业已转为人工控制以保障供水安全。 此次事件暴露出美国关键水利基础设施在面对国家级网络威胁时的脆弱性，尤其是那些往往缺乏完善网络安全防护的小型供水企业。对水务系统的成功攻击可能扰乱重要的公共服务，影响数百万公民的生活，并削弱公众对关键基础设施安全的信心。 这些攻击与伊朗威胁组织 CyberAv3ngers 有关，该组织被广泛认为与伊朗伊斯兰革命卫队网络电子司令部（IRGC-CEC）有关联，一直以 Unitronics Vision 系列集成 HMI 的 PLC 为攻击目标。受影响的供水企业已切换到人工操作，以避免对受感染的工业系统进行远程控制的风险。

rss · Tom's Hardware · 8月2日 13:10

**背景**: 供水和污水处理企业依赖 SCADA（数据采集与监视控制系统）来监控和管理分布在广阔地理区域内的运营，这些系统通常使用远程终端单元（RTU）和可编程逻辑控制器（PLC）。CyberAv3ngers 是一个由伊朗国家支持的黑客组织，最早于 2020 年左右被发现，已发展成为全球针对工业控制系统最活跃的威胁组织之一。该组织此前的攻击利用了以色列制造的 Unitronics PLC，而这类设备在美国的水务和污水处理设施中被广泛使用，使其成为关键基础设施防御中已知的薄弱环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/cyberav3ngers-iran-hacking-water-and-gas-industrial-systems/">CyberAv3ngers: The Iranian Saboteurs Hacking Water and Gas Systems Worldwide | WIRED</a></li>
<li><a href="https://www.tenable.com/blog/what-to-know-about-cyberav3ngers-the-irgc-linked-group-targeting-critical-infrastructure">CyberAv3ngers: FAQ About Iran-Linked Threat Group Targeting U.S. Critical Infrastructure | Tenable®</a></li>
<li><a href="https://www.securityweek.com/ics-at-multiple-us-water-facilities-targeted-by-hackers-affiliated-with-iranian-government/">ICS at Multiple US Water Facilities Targeted by Hackers Affiliated...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#critical-infrastructure`, `#cyberattack`, `#iran`, `#water-utilities`

---

<a id="item-2"></a>
## [Dasharo v0.9.0 为 AMD AM5 平台带来首款开源固件](https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850) ⭐️ 7.5/10

3mdeb 正式发布了 Dasharo v0.9.0，这是 AMD AM5 平台的首款开源固件，结合了 Coreboot 和 AMD 的 openSIL，为 MSI Pro B850-P WiFi 主板上的 Zen 4 Phoenix APU 提供初步支持。 这一里程碑通过提供可审计、透明的开源固件，向安全研究人员、爱好者和维修权社区开放了 AM5 平台，打破了 AMD 在桌面平台上长期封闭固件的格局。它也是 AMD 的 openSIL 计划能够在消费级产品中实现完全开放硅初始化的首次实际验证。 该版本号为 v0.9.0，表明它仍在成熟中，尚未达到生产就绪状态，且目前支持范围仅限于 MSI Pro B850-P WiFi 这一款主板搭配 Zen 4 Phoenix APU 使用。Dasharo 本身是 3mdeb 维护的 Coreboot 下游分支，3mdeb 在开源版本之外还提供名为 Dasharo Pro Package 的商业订阅服务，包含额外功能。

rss · Tom's Hardware · 8月2日 12:10

**背景**: Coreboot（前身为 LinuxBIOS）是一个长期存在的开源项目，通过在将控制权交给操作系统之前执行最少的硬件初始化来替代专有的 BIOS/UEFI 固件。AMD openSIL 由三个可静态链接的 C 语言库组成——xSIM（x86 硅初始化库）、xPRF（x86 平台参考库）和 xUSL（x86 实用工具与服务库），用于处理 x86 主机硅初始化，可以集成到任何 x86 主机固件中。Dasharo 是 3mdeb 旗下的品牌化 Coreboot 下游分支，强调开放开发、固件弹性和平台安全透明性。AMD 的 AM5 插槽是该公司随 Ryzen 7000 系列推出的当前桌面平台，在此版本发布之前，AM5 上尚无任何开源 UEFI 固件可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850">First open-source firmware for AM5 officially launches — Dasharo v0.9.0 brings Coreboot and openSIL to Zen 4 APUs on MSI B850 | Tom's Hardware</a></li>
<li><a href="https://docs.dasharo.com/osf-trivia-list/dasharo/">Frequenty Asked Questions about Dasharo</a></li>
<li><a href="https://www.amd.com/en/blogs/2023/empowering-the-industry-with-open-system-firmware-.html">Empowering The Industry with Open System Firmware – AMD openSIL</a></li>

</ul>
</details>

**标签**: `#open-source`, `#coreboot`, `#openSIL`, `#AMD-AM5`, `#firmware`

---

<a id="item-3"></a>
## [中国侵入式脑机接口公司「主动科技」创纪录完成 3.3 亿元天使轮融资](https://36kr.com/newsflashes/3923172519374216?f=rss) ⭐️ 7.3/10

8 月 3 日，中国脑机接口（BCI）公司「主动科技」宣布完成 3.3 亿元人民币天使轮融资，刷新中国脑机接口领域天使轮融资纪录。本轮融资由中科创星领投，联想之星、九合创投、道彤投资、英诺天使基金、华大松禾生科基金、济峰资本、嘉道资本共同参投。 这是中国侵入式脑机接口领域规模最大的早期投资之一，显示投资者在全球脑机接口格局被 Neuralink 等公司重塑之际，对本土神经植入生态系统的强烈信心。该笔资金将直接推动临床转化进程——这是中国在已批准设备和人体植入数据方面仍落后于美国的关键瓶颈——有望使国内企业在下一波医疗级脑机接口应用浪潮中具备竞争能力。 3.3 亿元资金将围绕场地扩展、设备完善、临床试验推进、团队扩充四个方向部署，全部聚焦于侵入式脑机接口产品的产业化落地。投资方组合异常多元，覆盖国资背景科学基金（中科创星、华大松禾生科）、企业战略投资部门（联想之星）以及医疗专项基金，表明这是跨领域协同支持，而非单一主题押注。

rss · 36氪 · 8月3日 02:17

**背景**: 脑机接口（BCI）是一类通过记录或调控神经活动来实现大脑与外部设备直接通信的系统。侵入式脑机接口通过外科手术将电极直接植入或紧贴脑组织，相较非侵入式方案可获得显著更高的信号保真度，但需要复杂的神经外科手术流程并面临长期生物相容性挑战。脑机接口的临床转化通常耗时数年，需要神经外科、神经内科、康复医学与生物医学工程的跨学科协作，并依赖中国 NMPA 或美国 FDA 等监管通道——中国脑机接口生态系统发展迅速，但在已批准的植入式设备和人体试验数据方面仍落后于美国。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12671281/">Invasive Brain-Computer Interfaces: A Critical Assessment of Current Developments and Future Prospects - PMC</a></li>
<li><a href="https://arxiv.org/pdf/2607.07185">Clinical Translation of Brain-Computer Interface in China: A Landscape</a></li>

</ul>
</details>

**标签**: `#brain-computer-interface`, `#funding`, `#China-tech`, `#medtech`, `#neural-implant`

---

<a id="item-4"></a>
## [Karpathy 的鹈鹕](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Karpathy 的鹈鹕 SVG 挑战成为一项重要的 AI 基准测试,通过生成矢量图形代码来测试模型对物理世界的理解能力。

hackernews · delichon · 8月2日 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**标签**: `#AI`, `#LLM benchmarks`, `#SVG generation`, `#world models`, `#Karpathy`

---

<a id="item-5"></a>
## [AMD 即将推出的 Zen 6 处理器有望解决游戏微卡顿问题并提升 1%最低帧率——下一代 CPU 据称将具备单核热与功耗预算优化](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets) ⭐️ 6.5/10

据泄露的信息显示，AMD 的 Zen 6 处理器将引入单核热与功耗优化，有望减少游戏中的微卡顿现象并提升 1%最低帧率。

rss · Tom's Hardware · 8月2日 12:30

**标签**: `#AMD`, `#Zen 6`, `#CPU architecture`, `#gaming performance`, `#hardware leak`

---

<a id="item-6"></a>
## [「幺正量子」完成数亿元 A 轮融资](https://36kr.com/newsflashes/3923156103818628?f=rss) ⭐️ 6.3/10

中国量子计算初创公司幺正量子（Unitary Quantum）完成数亿元 A 轮融资，本轮融资由深圳资本领投，多家机构联合参与投资，资金将用于加速基于 QCCD 架构的囚禁离子量子计算研发，目标直指量子优越性与量子纠错。

rss · 36氪 · 8月3日 02:00

**标签**: `#quantum-computing`, `#funding`, `#QCCD`, `#trapped-ion`, `#china-tech`

---

<a id="item-7"></a>
## [铠侠计划于 2025 年量产支持 PCIe 6.0 和 UFS 5.0 的下一代 AI NAND 产品](https://36kr.com/newsflashes/3923128725646979?f=rss) ⭐️ 6.3/10

日本 NAND 闪存制造商铠侠宣布计划于今年量产其面向 AI 的下一代 NAND 闪存产品，新产品将支持尖端的 PCIe 6.0 接口和 UFS 5.0 标准。这些产品专为满足人工智能工作负载不断增长的存储需求而设计。 作为全球主要的 NAND 闪存制造商之一，铠侠的这一举措标志着整个行业向新一代接口标准的过渡，这对于处理 AI 训练和推理所需的海量数据吞吐至关重要。PCIe 6.0 和 UFS 5.0 的采用将带来显著更快的数据传输速率，惠及数据中心、边缘 AI 设备和智能手机等领域。 PCIe 6.0 通过采用新的调制方式将传输速度从 PCIe 5.0 的 32 GT/s 翻倍至 64 GT/s，主要面向数据中心互连（DCI）场景中的 AI 和机器学习应用。UFS 5.0 代表了移动闪存存储的下一代标准，继承自读取速度已达 4,200 MB/s、写入速度达 2,800 MB/s 的 UFS 4.0。

rss · 36氪 · 8月3日 01:32

**背景**: NAND 闪存是一种非易失性存储技术，广泛用于固态硬盘、智能手机及其他设备中。PCIe（外围组件互连高速标准）是用于将 SSD 等组件连接至处理器的高速接口标准，每新一代大致使带宽翻倍。UFS（通用闪存存储）是由 JEDEC 制定的移动设备闪存存储标准。AI 的快速发展对高带宽、低延迟存储提出了前所未有的需求，推动整个行业加速采用 PCIe 6.0 和 UFS 5.0 等新一代标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12VHPWR - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_Flash_Storage">Universal Flash Storage - Wikipedia</a></li>

</ul>
</details>

**标签**: `#NAND flash`, `#PCIe 6.0`, `#UFS 5.0`, `#AI hardware`, `#storage technology`

---

<a id="item-8"></a>
## [Kakehashi：面向 Linux ARM 的实验性 macOS 二进制兼容层](https://github.com/wie-project/kakehashi) ⭐️ 6.0/10

开发者 vlad_kalinkin 发布了 Kakehashi，这是一个实验性的用户空间兼容层，可在 Linux ARM 机器上原生运行 macOS 命令行二进制文件，目前已有 7-Zip、curl 和 Git 的可用原型。 该项目探索了已有工具（如 Darling）尚未覆盖的细分领域——ARM 支持，有望让 Linux ARM 用户（例如运行 Asahi Linux 的 Apple Silicon Mac 用户）无需模拟开销即可运行 macOS 专属的 CLI 工具。 7-Zip 目前运行速度比原生 Linux 慢约 5.2 倍，但开发者已制定了优化计划；curl 在 Docker 测试脚本中通过了超过 200 个自动化命令；该项目在理念上与 Wine 类似，但目标格式是 Mach-O 可执行文件和苹果的框架，而非 Windows PE 二进制文件。

hackernews · vlad_kalinkin · 8月2日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: 用户空间兼容层将一个操作系统的 API 和系统调用转换为另一个系统的调用，使为一个平台编译的二进制文件能够在另一个平台上运行。Wine 是最著名的例子，它让 Windows PE 二进制文件无需完整 CPU 级模拟即可在 Linux 上运行。macOS 使用 Mach-O 可执行格式，并依赖苹果特有的框架和动态库（例如 /usr/lib/system 中的那些），这在结构上与 Linux 的 ELF 格式和 glibc 不同。Darling 是一个现有的开源项目，在 Linux 上重新实现了足够多的 macOS 用户空间来运行 macOS 二进制文件，但它历来只面向 x86_64，缺乏 ARM 支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CrossOver_(software)">CrossOver (software) - Wikipedia</a></li>
<li><a href="https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/MachOOverview.html">Overview of the Mach - O Executable Format</a></li>
<li><a href="https://inventivehq.com/blog/executable-file-formats-guide">Understanding PE, ELF, and Mach - O : Executable File Format Deep...</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与 Wine、Proton 和 Darling 进行类比，其中一位用户建议 Kakehashi 与 Darling 已开放的 ARM64 支持 PR 合作。另一些人赞扬了项目的雄心，同时批评了"Kakehashi"这个名字，并指出项目仍处于早期阶段。一位技术评论者（derefr）提出，是否可以采用反编译式的方法——将原始二进制文件作为输入而非打包重写的库——来降低此类项目的实现难度。

**标签**: `#macOS`, `#Linux ARM`, `#compatibility-layer`, `#userspace`, `#open-source`

---

<a id="item-9"></a>
## [F*：面向形式化验证的证明式编程语言](https://fstar-lang.org/) ⭐️ 6.0/10

本次讨论重新介绍了 F*，这是一款主要由微软研究院开发的通用证明式函数式编程语言，强调了它在编写可执行代码的同时表达程序正确性证明的能力，以及将现有 C 代码库逐步迁移到 F* 的支持。 F* 代表了一种日益兴起的证明式编程范式，将形式化验证集成到开发过程中，而非事后补充，这对于正确性至关重要的高保障系统具有重要意义。 F* 将数学证明技术集成到开发流程中，允许开发者编写程序的同时附带大部分自动化的正确性证明。它与依赖类型和带副作用编程的联系，使其特别适合验证底层系统代码以及与现有 C 库进行交互。

hackernews · ducktective · 8月2日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49143925)

**背景**: 证明式编程语言将可执行代码、形式化规约和正确性证明集成到统一的开发流程中。与依赖测试和调试来确保正确性的传统语言不同，这类语言允许开发者数学化地证明其程序满足指定的性质。F* 属于这一类别，由微软研究院开发，相关的 Steel 语言用于并发分离逻辑证明。能够逐步验证和迁移 C 代码的能力使 F* 特别适用于将形式化验证引入现有工业代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fstar-lang.org/">F *: A Proof - Oriented Programming Language</a></li>
<li><a href="https://medium.com/@SakshifromKushoAI/f-a-general-purpose-proof-oriented-programming-language-2a0cf9f71915">F * : A general-purpose proof - oriented programming language</a></li>
<li><a href="https://spencerfarley.com/2022/07/22/proof-oriented-programming/">Proof - Oriented Programming | 5min Dev Essentials</a></li>

</ul>
</details>

**社区讨论**: 社区情绪较为复杂，主要批评的是 F* 官网的展示方式而非语言本身。一位评论者对首页缺乏语法示例表示不满，希望能看到语法长什么样以及为什么应该使用该语言。另一位评论者则称赞了 F* 在调用外部库的同时逐步迁移现有 C 代码库的能力。其他评论询问了 F* 是否在现实工业界有应用，并讽刺地指出讨论形式化验证的网站本身缺乏响应式设计。

**标签**: `#programming-languages`, `#formal-verification`, `#functional-programming`, `#proof-assistants`, `#type-systems`

---

<a id="item-10"></a>
## [华硕展示搭载 Intel Panther Lake 的 NUC 16 迷你电脑家族](https://www.servethehome.com/asus-showcases-nuc-16-family-powered-by-intel-panther-lake/) ⭐️ 5.5/10

在 Computex 展会上，华硕发布了搭载 Intel 即将推出的 Panther Lake 和 Wildcat Lake SoC 的 NUC 16 迷你电脑家族，将完整系统集成在 0.7 升的小巧机箱中。该产品线将提供多种配置选项，包括完整的迷你电脑版本以及不带内存、存储和操作系统的准系统套件。 这是 Intel Panther Lake 平台首次以迷你电脑形态亮相商用市场，让人们得以一窥下一代紧凑型 AI 计算设备的风貌。此举表明在小型桌面电脑市场竞争中，继承了 Intel NUC 业务的华硕继续保持强劲的市场存在感。 Panther Lake 基于 Intel 18A 制程节点打造，配备的 NPU 可提供高达 50 TOPS 的 AI 算力；而 Wildcat Lake 则面向入门级笔记本等更注重成本的设备。0.7 升的机箱体积展示了 Intel 芯片设计架构如何在不牺牲性能的前提下实现紧凑集成。

rss · ServeTheHome · 8月2日 17:00

**背景**: 华硕于 2023 年接管了 Intel 的 NUC（Next Unit of Computing）迷你电脑业务，继承了开创超紧凑桌面电脑品类的产品线。Intel 的 Panther Lake 是继 Meteor Lake、Lunar Lake 和 Arrow Lake 之后的下一代主流客户端 SoC，采用基于芯片块（tile）的设计，在 Intel 18A 制程上制造。Wildcat Lake 则是面向经济型笔记本和小型设备的低端版本。0.7 升的机箱体积使 NUC 16 成为市面上最小的 x86 商用系统之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/asus-showcases-nuc-16-family-powered-by-intel-panther-lake/">ASUS Showcases NUC 16 Family Powered By... - ServeTheHome</a></li>
<li><a href="https://www.linkedin.com/posts/thezit_aicomputing-intel18a-edgeperformance-activity-7382090653918224385-PWlv">Intel 's Panther Lake chip specs revealed: 50 TOPS NPU... | LinkedIn</a></li>
<li><a href="https://logicity.in/en/blog/dell-xps-13-vs-macbook-neo-699-wildcat-lake-takes-on-apple">Dell XPS 13 vs MacBook Neo: $699 Wildcat Lake Takes on... | Logicity</a></li>

</ul>
</details>

**标签**: `#hardware`, `#intel`, `#panther-lake`, `#nuc`, `#computex`

---