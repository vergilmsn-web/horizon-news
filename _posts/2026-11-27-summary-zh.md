---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 107 条内容中筛选出 18 条重要资讯。

---

1. [伯恩斯坦质疑计算机辅助数学证明的绝对可靠性](#item-1) ⭐️ 9.0/10
2. [华为在 ISSCC 2027 公布定制 HBM 设计以应对内存瓶颈](#item-2) ⭐️ 9.0/10
3. [台积电推出 A14 节点 AI 设计套件](#item-3) ⭐️ 8.5/10
4. [硬件漏洞可让攻击者 20 天内暴力破解 BitLocker PIN](#item-4) ⭐️ 8.5/10
5. [热门购物网站遭利用 WebRTC 的信用卡盗刷脚本攻击](#item-5) ⭐️ 8.0/10
6. [States sue SpaceX to stop Grok from generating child sex images, revenge porn](#item-6) ⭐️ 8.0/10
7. [Beyond Lithography: The Battle for Semiconductor Manufacturing Yield](#item-7) ⭐️ 8.0/10
8. [出口管制威胁北京 AI 雄心，模型落后或达九个月](#item-8) ⭐️ 7.5/10
9. [凸性技能在用户不知情的情况下将应用创意发送至远程服务器](#item-9) ⭐️ 7.0/10
10. [迈克尔·尼尔森移除经典免费神经网络书籍](#item-10) ⭐️ 7.0/10
11. [AI 让自托管重新变得有趣](#item-11) ⭐️ 7.0/10
12. [AMD's RDNA 5 Set for Linux Kernel 7.5 Support](#item-12) ⭐️ 6.5/10
13. [Microsoft Cuts Memory Utilization in Windows 11 In Response To RAMpocalypse](#item-13) ⭐️ 6.5/10
14. [索尼申请专利：游戏内图形设置一键切换专用按钮](#item-14) ⭐️ 6.5/10
15. [铠侠发布 GP2 系列 SSD，1800 万 IOPS 高耐久](#item-15) ⭐️ 6.5/10
16. [Construct22：用于个性化互动的多智能体 AI 群聊模拟器](#item-16) ⭐️ 6.0/10
17. [NuVolta 解析 PCB 接地设计与返回路径](#item-17) ⭐️ 6.0/10
18. [(PR) Limited Demand Visibility and Growing Supply Chain Caution Heighten Risk of DRAM Contract Price Declines in 2028](#item-18) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [伯恩斯坦质疑计算机辅助数学证明的绝对可靠性](https://cr.yp.to/proofs/falseccp.html) ⭐️ 9.0/10

Daniel J. Bernstein 提出了关于计算机辅助证明可靠性的质疑，挑战了形式验证系统绝对无误的假设。此举引发了一场技术讨论，区分了孤立的声音性（soundness）漏洞与在多验证器系统中成功误导用户的更广泛目标。 这场辩论意义重大，因为形式证明辅助工具越来越多地用于关键软件开发和数学研究中，理解单一工具故障与系统性误导结果之间的差距对于建立信任至关重要。它强调了高保障验证中的权衡以及多证明器架构的重要性。 批评者指出，像 Metamath 这样的系统使用五种不同编程语言独立创建的验证器来最小化声音性风险。已知的一个利用案例涉及 DeepMind 研究人员利用证明来利用多个验证器的漏洞，凸显了真正保护这些系统的复杂性。

hackernews · _tk_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**背景**: 在证明论中，“声音性”意味着系统永远不会证明错误结论。Lean 和 Coq 等形式证明辅助工具被设计用来检查数学证明，但其底层代码可能包含漏洞。大多数现代系统通过使用多个独立的检查器来降低这种风险，只有当证明通过所有检查器时才会被接受，这使得欺骗整个系统变得更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.lavx.hu/article/broken-proofs-and-broken-provers">Broken proofs and broken provers | LavX News</a></li>
<li><a href="https://essamamdani.com/blog/lean-4-soundness-bug-14576-postmortem">Lean 4 Soundness Bug #14576: What Broke the... | Essa Mamdani</a></li>
<li><a href="https://proofassistants.stackexchange.com/questions/6615/status-of-verification-of-proof-assistants">foundations - Status of verification of proof assistants - Proof ...</a></li>

</ul>
</details>

**社区讨论**: 社区专家不同意伯恩斯坦的核心假设，他们认为在需要多个独立验证器达成一致的系统中发现单一的声音性漏洞与成功误导数学家是不同的。其他人补充说，主要系统在数十年中出现的总漏洞数量很少，且大多数容易修复。也有人质疑这些证明检查器为何如此庞大，以及能否从更小、可验证的规则集中引导生成。

**标签**: `#formal-verification`, `#computer-science`, `#mathematics`, `#proof-theory`, `#security`

---

<a id="item-2"></a>
## [华为在 ISSCC 2027 公布定制 HBM 设计以应对内存瓶颈](https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/) ⭐️ 9.0/10

华为确认将在旧金山举行的 ISSCC 2027 会议上公布其定制的高带宽内存（HBM）设计，以解决 AI 内存瓶颈。此次公布标志着该公司通过定制化内存架构增强 AI 硬件能力的战略举措。 此举对 AI 和半导体行业至关重要，因为 HBM 是受出口管制影响的 AI 基础设施关键组件。华为的解决方案有助于维持 AI 性能标准，并为全球市场提供替代性内存方案。 根据最新的议程详情，华为的定制 HBM 架构包含 64 个通道和 4,096 条数据线，是标准设计引脚数的两倍。该设计重点优化热管理和密度，以克服常见的 AI 内存限制。

rss · EE Times · 11月27日 08:56

**背景**: 高带宽内存（HBM）是由多层 DRAM 芯片组成的内存堆栈，能为大型 AI 加速器提供快速的数据传输速率，是驱动 AI 的关键。国际固态电路会议（ISSCC）是全球领先的论坛，供工程师展示集成电路设计的最新进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.isscc.org/">ISSCC - International Solid-State Circuits Conference</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#Semiconductors`, `#Huawei`, `#HBM`, `#ISSCC`

---

<a id="item-3"></a>
## [台积电推出 A14 节点 AI 设计套件](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-gives-a-sneap-peak-at-ai-design-kit-agentic-ai-with-foundry-expertise) ⭐️ 8.5/10

台积电发布了一款早期阶段的 AI 设计套件（ADK），利用代理式 AI 管理其即将推出的 A14 工艺节点中设计规则复杂度的指数级增长。该工具融合了晶圆厂的专业知识，包括金属间距和布线模式，以辅助芯片设计。 这一点之所以重要，是因为台积电客户要求将开发周期缩短 33%，而 A14 节点的设计规则数量比 N5 节点增加了 3.6 倍。AI 设计套件旨在通过自动化复杂任务来缩小这一差距，从而加速前沿芯片的上市时间。 A14 节点的设计复杂度是由于其设计规则数量相比 N5 节点增加了 3.6 倍所致。AI 设计套件包含特定工艺信息，如标准单元高度和库单元命名约定。

rss · Tom's Hardware · 11月27日 13:00

**背景**: EDA 中的代理式 AI 指的是能够编排设计工作流的自主系统，而不仅仅是响应用户查询。随着半导体节点微缩，物理和电气设计规则变得极其复杂，无法通过人工管理，因此需要 AI 驱动的自动化来维持芯片制造的效率和准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/tsmc-gives-a-sneap-peak-at-ai-design-kit-agentic-ai-with-foundry-expertise">TSMC gives a sneap peak at AI Design Kit: Agentic... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#AI`, `#Semiconductor`, `#EDA`, `#Agentic AI`

---

<a id="item-4"></a>
## [硬件漏洞可让攻击者 20 天内暴力破解 BitLocker PIN](https://www.tomshardware.com/tech-industry/cyber-security/amd-and-winbond-vulnerabilities-let-attackers-brute-force-bitlocker-pins-on-millions-of-pcs-cracking-a-six-digit-pin-drops-from-19-years-to-20-days) ⭐️ 8.5/10

研究人员在 AMD 和 Winbond 硬件中发现漏洞，允许攻击者在数百万台 PC 上暴力破解 BitLocker PIN。这些缺陷将破解六位数字 PIN 所需的时间从 19 年大幅缩短至仅 20 天。 该发现对使用 BitLocker 的 Windows 设备安全意义重大，因为它大幅降低了 PIN 保护数据的安全边际。数百万台使用 AMD 处理器或 Winbond 芯片的企业及消费级设备现在面临即时风险。 使用基于 Winbond SPI 闪存芯片的设备无法通过软件修复，必须更换硬件，而受影响的 AMD PC 可能需要更新 BIOS 文件。这些缺陷具体影响了 AMD 平台安全处理器（AMD PSP）及相关闪存存储组件。

rss · Tom's Hardware · 11月27日 12:30

**背景**: BitLocker 是微软内置的驱动器加密服务，通常使用 PIN 码在启动过程中保护数据。TPM 模块常被用于透明地管理此加密，但攻击者可能会尝试针对该 PIN 码进行暴力破解或字典攻击。这些特定的硬件漏洞削弱了底层安全机制，使得自动猜测攻击的速度显著提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="/url?opi=89978449&q=CAESiQIBxCJF184hC-_TWDsywkOdurVmBvjL5Z3QxGW3pwTA_w9gm-IVFvkDbBPD7IHlyg2T29Q8JUWPC2t9mZdxqZkInrOixOfjgx17GJ2teuCwdSMmrcOwZx4F24luZhqlStZvEPFTt23xSiQAPBJe9XiEXmuCPwGI4X0iDWpFbmARJ6BqxZEk5NkhhTCc89ZxSMZEAmPvq67_baM2CYeGPl4Y3WMHZgxWTUycj_8gcyM8Gv9hQM2J_oyZcbuKgF34cXdokOHE2_g3vo3ioK-ONF1-f8pJpHyzYSLvW_cbSKiqZc2SCS-ghFONQdv_NsqAr5oUZDa2LRYAbOTabyIamK9w28Vx6U8O_nVb&sa=U&uoh=3&ved=2ahUKEwjHpeOhkamYAxWNdjIDHcdWGokQFnoECAsQAg&usg=AOvVaw16S51XnYPe3kDZhWf2iPfS">AMD and Winbond vulnerabilities let attackers brute-force BitLocker PINs ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#vulnerability`, `#BitLocker`, `#AMD`, `#Windows`

---

<a id="item-5"></a>
## [热门购物网站遭利用 WebRTC 的信用卡盗刷脚本攻击](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 8.0/10

安全研究人员发现，许多知名电商网站上的恶意脚本利用 WebRTC 窃取信用卡信息。由于 WebRTC 通道绕过了传统的监控机制，这种技术手段比标准的 HTTP 请求更难被检测。 在“黑色星期五”等购物高峰期，此漏洞对在线支付安全构成重大威胁，使攻击者能窃取更广泛用户的金融数据。这突显了在面向消费者的网站上允许第三方脚本执行任意代码所带来的系统性风险。 WebRTC 可以绕过限制特定 HTTP 域名的严格内容安全策略（CSP），且该攻击主要被观察到针对移动设备，以更容易隐匿。其根本问题在于未对商户域名上执行的不可信第三方代码进行严格隔离，从而带来固有风险。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**背景**: WebRTC 是允许浏览器在不使用插件的情况下进行实时点对点音频、视频和数据交换的 Web 标准。网页扒窃（Web Skimming）是一种欺诈攻击，攻击者向结账页面注入恶意代码，在用户的支付信息被加密前窃取其凭据。传统的安全措施通常依赖内容安全策略来对特定的外部资源进行白名单管理，而 WebRTC 可以绕过这一限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rfxn.com/research/webrtc-skimmer-csp-bypass">WebRTC Skimmers: How Payment Thieves Bypass Content Security ...</a></li>
<li><a href="https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html">WebRTC Skimmer Bypasses CSP to Steal Payment Data from E ...</a></li>
<li><a href="https://aviatrix.ai/threat-research-center/webrtc-skimmer-bypasses-csp-to-steal-payment-data-from-e-commerce-sites/">WebRTC Skimmer Bypasses CSP to Steal Payment Data from E ...</a></li>

</ul>
</details>

**社区讨论**: 社区普遍认为，核心漏洞在于执行了不安全的第三方脚本，而非 WebRTC 的具体功能。部分用户强调广告拦截工具在阻止此类威胁方面是完全合理的，也有人指出支付行业缺乏非对称加密是架构缺陷。共识是，无论是通过 WebRTC 还是简单的 HTTP 进行跨域数据传输，如果网站自身的基础设施缺乏安全防护，就天然存在暴露风险。

**标签**: `#Cybersecurity`, `#WebRTC`, `#Payment Fraud`, `#Web Security`, `#Threat Intelligence`

---

<a id="item-6"></a>
## [States sue SpaceX to stop Grok from generating child sex images, revenge porn](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 8.0/10

Attorneys General from multiple states have filed a lawsuit against SpaceX's parent company, alleging that its AI model Grok facilitates the creation and promotion of child sexual exploitation material and non-consensual imagery.

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**标签**: `#AI-Law`, `#Regulation`, `#Content-Safety`, `#X-Twitter`, `#Legal`

---

<a id="item-7"></a>
## [Beyond Lithography: The Battle for Semiconductor Manufacturing Yield](https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/) ⭐️ 8.0/10

The article analyzes how the MATCH Act reveals strategic vulnerabilities in semiconductor manufacturing yield that go beyond lithography, impacting the broader ecosystem of manufacturing productivity technologies.

rss · EE Times · 11月27日 14:22

**标签**: `#Semiconductor Manufacturing`, `#Supply Chain`, `#Geopolitics`, `#MATCH Act`, `#Yield Optimization`

---

<a id="item-8"></a>
## [出口管制威胁北京 AI 雄心，模型落后或达九个月](https://www.tomshardware.com/tech-industry/artificial-intelligence/beijings-ai-ambitions-are-under-threat-as-models-may-fall-behind-by-up-to-nine-months-versus-competitors-chinese-ai-labs-are-under-heavy-fire-from-export-controls-maturing-chip-stacks-and-a-distillation-crackdown) ⭐️ 7.5/10

近期报告显示，关闭 GPU 租赁漏洞和打击模型蒸馏措施导致中国 AI 实验室可能比西方竞争对手落后多达九个月。这些举措加上不断成熟的芯片供应体系，给北京的 AI 开发时间表带来了巨大阻碍。 这一局面标志着中国 AI 发展的重要战略转折点，它通过凸显地缘政治、硬件可用性和软件创新之间的相互作用，以可量化的方式影响模型对等性。这种延误可能改变全球 AI 竞赛的竞争格局，影响范围不仅限于国家利益，还波及更广泛的技术生态系统。 关闭亚洲地区的 GPU 租赁漏洞和执行蒸馏限制被确定为导致所报道延误的主要原因。“九个月”的估计值作为一个具体指标，说明了硬件出口管制和软件政策打击措施在多大程度上导致了中国与西方 AI 能力的分化。

rss · Tom's Hardware · 11月27日 15:00

**背景**: AI 模型开发高度依赖于对高性能算力（主要是 GPU）的访问，而这些设备受到旨在限制特定地区先进芯片流动的国际出口管制。模型蒸馏是一种技术，其中较小的 AI 模型被训练以模仿更大、更强大的模型的输出，近期的政策打击旨在限制这种做法，以保护知识产权和技术优势。

**标签**: `#AI-Policy`, `#China`, `#Export-Controls`, `#Hardware-Supply`, `#Model-Development`

---

<a id="item-9"></a>
## [凸性技能在用户不知情的情况下将应用创意发送至远程服务器](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

Hacker News 上的讨论和 GitHub 问题揭露了 Convex 的 AI 编程技能会悄悄将用户的应用创意发送至远程服务器，引发了该公司 CEO 的回应以及关于 AI 工具中数据隐私的辩论。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**标签**: `#privacy`, `#AI-security`, `#developer-tools`, `#convex`, `#data-privacy`

---

<a id="item-10"></a>
## [迈克尔·尼尔森移除经典免费神经网络书籍](https://twitter.com/michael_nielsen/status/2126359767362748777) ⭐️ 7.0/10

迈克尔·尼尔森宣布从官方域名移除其广泛使用的免费在线书籍《神经网络与深度学习》，引发了社区对该资源进行存档的努力。 这一基础性教育资源的缺失影响了依赖经典反向传播解释的学生和开发者，而其存档状态凸显了在人工智能时代保存开放教育资源的重要性。 该书是在 PyTorch 等现代框架占据主导地位之前理解人工神经网络的主要资源，并且网页档案馆中仍有可供公众访问的存档快照。

hackernews · brandonb · 11月27日 19:31 · [社区讨论](https://news.ycombinator.com/item?id=50670757)

**背景**: 迈克尔·尼尔森是一位量子物理学家和科学作家，他于 2015 年创作了这本广受欢迎的神经网络入门读物。该书为反向传播和人工神经网络提供了数学基础，成为通往更现代深度学习概念的桥梁。它作为免费在线资源分发，并成为早期深度学习教育的标准教材。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/michael-nielsen-neural-networks-deep-learning-book-taken-down-november-2026">Michael Nielsen Removed His Deep Learning Book: Why ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对一个历史性教育里程碑的丧失表示担忧，并分享了 web.archive.org 的快照链接以保存内容。一些用户强调了该书在深度学习框架出现之前的时代——即自定义反向传播函数是标准做法时——的重要意义。

**标签**: `#neural_networks`, `#deep_learning_education`, `#resource_removal`, `#machine_learning`

---

<a id="item-11"></a>
## [AI 让自托管重新变得有趣](https://janlukas.blog/posts/ai-self-hosting) ⭐️ 7.0/10

一场热门讨论探索了 AI 智能体如何通过简化部署来重振自托管，同时也辩论了安全责任归属以及编程智力挑战降低所带来的利弊。

hackernews · jlelse · 11月26日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50660180)

**标签**: `#AI`, `#Self-Hosting`, `#Security`, `#DevOps`, `#Community-Discussion`

---

<a id="item-12"></a>
## [AMD's RDNA 5 Set for Linux Kernel 7.5 Support](https://www.techpowerup.com/355263/amds-rdna-5-set-for-linux-kernel-7-5-support) ⭐️ 6.5/10

AMD plans to merge GFX13 (RDNA 5) driver support into the Linux 7.5 kernel, signaling that the hardware release is likely approaching its second-half 2027 target date.

rss · TechPowerUp News · 11月27日 10:35

**标签**: `#AMD`, `#RDNA 5`, `#Linux Kernel`, `#GPU Drivers`, `#Graphics`

---

<a id="item-13"></a>
## [Microsoft Cuts Memory Utilization in Windows 11 In Response To RAMpocalypse](https://www.techpowerup.com/355249/microsoft-cuts-memory-utilization-in-windows-11-in-response-to-rampocalypse) ⭐️ 6.5/10

Microsoft is reducing memory utilization in Windows 11 for built-in apps and background services in response to the rising cost of RAM, a move confirmed by a Corporate VP of Core OS at an Ignite session.

rss · TechPowerUp News · 11月27日 03:00

**标签**: `#Windows`, `#Memory Management`, `#OS Updates`, `#Hardware Costs`, `#Microsoft`

---

<a id="item-14"></a>
## [索尼申请专利：游戏内图形设置一键切换专用按钮](https://www.techpowerup.com/355254/sony-patent-describes-a-controller-button-for-swapping-graphics-settings-mid-game) ⭐️ 6.5/10

索尼提交了一项专利申请，描述了一个专用的手柄按钮，该按钮允许玩家在不需要进入设置菜单的情况下，在游戏即时切换画质和性能图形预设。该系统采用平滑过渡方式，渲染参数（如抗锯齿级别）会通过中间值逐渐变化，而不是突然切换。 该专利可能会通过允许玩家根据实时需求动态调整游戏性能或视觉保真度，从而显著提升用户体验。它还暗示了索尼对下一代游戏机的高级实时渲染技术的兴趣。 该专利描述了一种自动适配系统，通过比较连续帧生成 0.0-1.0 的变化分数，对静态场景应用更大幅度的调整，而对混乱的游戏场景应用更轻的调整。该申请是 2023 年提交文件的延续，并未具体提及 PS6 或 DualSense 手柄。

rss · TechPowerUp News · 11月27日 00:36

**背景**: 在现代游戏中，“画质”和“性能”模式是平衡视觉细节与帧率稳定性的固定预设。超级采样抗锯齿（SSAA）是一种通过以更高分辨率渲染图像来平滑边缘的技术，但对硬件资源要求极高。实时渲染通常需要动态调整以维持稳定的帧率，但传统上这些由引擎自动处理或通过手动菜单设置完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supersampling">Supersampling - Wikipedia</a></li>
<li><a href="https://patentlyze.com/about/">About | Patentlyze</a></li>
<li><a href="https://www.displayninja.com/best-anti-aliasing-mode/">What Is The Best Anti - Aliasing Mode? [Simple] - Display Ninja</a></li>

</ul>
</details>

**标签**: `#Gaming Hardware`, `#Graphics Rendering`, `#Sony`, `#Patent`, `#User Experience`

---

<a id="item-15"></a>
## [铠侠发布 GP2 系列 SSD，1800 万 IOPS 高耐久](https://www.servethehome.com/kioxia-gp2-series-ssd/) ⭐️ 6.5/10

铠侠（Kioxia）宣布推出 GP2 系列 SSD，旨在作为 DRAM 与传统 TLC NAND 之间的高性能存储层级。该驱动器实现了超过 1800 万的随机读 IOPS，并具备 50 DWPD 的耐用性评级。 此次发布对企业数据中心具有重要意义，因为它提供了一种快速且高耐久性的存储选项，有助于弥合易失性内存与较慢闪存存储之间的延迟差距。通过定位 DRAM 与 TLC NAND 之间的层级，铠侠满足了需要持续高吞吐量和随机 I/O 性能的工作负载需求。 50 DWPD 的评级表明其具备企业级耐用性，意味着该驱动器在保修期内每天可以写入其完整容量的 50 次。1800 万的随机读 IOPS 数据使其跻身于当前面向高并发应用最高性能 SSD 的行列。

rss · ServeTheHome · 11月27日 04:08

**背景**: SSD 使用 NAND 闪存，分为 SLC、MLC、TLC 和 QLC 等类型，每种类型在密度、成本和速度之间存在权衡。DRAM 是主要系统内存，在 DRAM 和标准 TLC 存储之间放置专用 SSD 层级，使系统能够以更低延迟存储更多热数据。DWPD（每日驱动器写入量）是衡量 SSD 寿命的标准指标，表示驱动器每天可承受的完整容量写入次数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kingston.com/en/blog/pc-performance/difference-between-slc-mlc-tlc-3d-nand">2D vs 3D NAND : Differences Between SLC , MLC, TLC and QLC...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Flash_memory">Flash memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Storage`, `#SSD`, `#Kioxia`, `#NAND Flash`, `#Performance`

---

<a id="item-16"></a>
## [Construct22：用于个性化互动的多智能体 AI 群聊模拟器](https://construct22.com/) ⭐️ 6.0/10

Construct22 是一个模拟多个 AI 模型群聊的在线工具，它们以独特的个性互动来讨论用户的特定状况。该项目在 Hacker News 上走红，凸显了多智能体 LLM 互动的创意潜力。 该工具是 AI 社区中一个病毒式的文化时刻，展示了当前大语言模型的新兴行为和独特人格。它提供超越标准聊天机器人互动的创新用户体验，使 AI 协作更加可触及且有趣。 用户可以自定义 AI 参与者，例如将 Qwen 等本地模型与 Claude 和 Gemini 等云端模型混合使用，从而产生幽默的动态互动。该工具允许创建 AI 模型相互辩论、开玩笑甚至强制执行系统提示约束的创意场景。

hackernews · utiiiD · 11月27日 06:44 · [社区讨论](https://news.ycombinator.com/item?id=50663595)

**背景**: 多智能体系统是指多个 AI 模型相互作用以解决问题或完成任务，超越了单模型聊天。人格提示是一种通过特定指令赋予 LLM 独特性格、语气或角色的技术。该工具利用这些概念创建社交模拟环境。

**社区讨论**: 社区用户分享了幽默的会话轶事，例如 Claude 强制执行群体章程，或 Gemini 因未能遵循指示而被移除。用户还享受高端云端模型与较小本地模型之间的动态，指出 AI 如何互相调侃。

**标签**: `#LLM`, `#Multi-Agent`, `#Creativity`, `#AI-Safety`, `#Viral`

---

<a id="item-17"></a>
## [NuVolta 解析 PCB 接地设计与返回路径](https://www.eetimes.com/nuvolta-technical-sharing-pcb-grounding-design-and-return-path/) ⭐️ 6.0/10

NuVolta 在 EE Times 上发表了一篇技术深度文章，指出标准的 PCB 接地规则是不完整的，因为它们通常忽略了电流的返回路径。文章强调，当信号跨越地平面的分割时，返回电流被迫绕道而行，从而导致信号完整性问题。 解决返回路径设计对于防止高速混合信号电子系统中的电磁干扰和串扰至关重要。理解这些基本原理有助于硬件工程师避免常见的布局错误，从而防止电路板性能下降。 分割的地平面在物理上分隔了连续的铜区域，从而隔离了模拟和数字域，但这也造成了阻碍自然回流路径的间隙。文章指出，正确管理这种电流绕道对于维持信号质量至关重要。

rss · EE Times · 11月27日 14:00

**背景**: 在 PCB 设计中，信号的返回电流理想情况下应直接在走线下方流动，以抵消磁场。分割的地平面会造成一个物理屏障，中断了这条直接路径，迫使电流走一条更长、基于环路的路径。这种增加的环路面积可能像天线一样辐射电磁干扰（EMI），从而降低信号完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aivon.com/blog/pcb-design/pcb-ground-plane-splits-when-to-use-them-and-how-to-avoid-disasters/">Splitting Ground in PCB Design: Best Practices and Common ...</a></li>
<li><a href="https://www.protoexpress.com/blog/current-return-path-signal-integrity/">How to Handle Current Return Path for Better Signal Integrity</a></li>

</ul>
</details>

**标签**: `#PCB Design`, `#Hardware Engineering`, `#Signal Integrity`, `#Grounding`, `#Electronics`

---

<a id="item-18"></a>
## [(PR) Limited Demand Visibility and Growing Supply Chain Caution Heighten Risk of DRAM Contract Price Declines in 2028](https://www.techpowerup.com/355261/limited-demand-visibility-and-growing-supply-chain-caution-heighten-risk-of-dram-contract-price-declines-in-2028) ⭐️ 5.5/10

TrendForce reports that uncertainty surrounding U.S. midterm elections and geopolitical restrictions is causing DRAM supply chain participants to reassess plans, increasing the risk of contract price declines in 2028.

rss · TechPowerUp News · 11月27日 09:00

**标签**: `#DRAM`, `#Supply Chain`, `#Semiconductor Industry`, `#Market Analysis`, `#Tech Policy`

---