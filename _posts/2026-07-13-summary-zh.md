---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 51 条内容中筛选出 10 条重要资讯。

---

1. [台积电 2 纳米据报道已量产，谷歌成首家手机芯片客户](#item-1) ⭐️ 7.3/10
2. [Chromium 148 的 Math.tanh 函数泄露操作系统指纹](#item-2) ⭐️ 7.0/10
3. [Claude Code 在读取提示词前发送了 33k tokens；OpenCode 仅发送 7k](#item-3) ⭐️ 7.0/10
4. [2025 年爱尔兰数据中心耗电量几乎与全国家庭用电总量相当——尽管多年来受到电网限制，服务器农场仍吞噬了全国 23%的电力](#item-4) ⭐️ 6.5/10
5. [FCC 批准 Reflect Orbital 太空镜面卫星](#item-5) ⭐️ 6.5/10
6. [高盛：AI 或推高美国通胀，存储芯片价格暴涨为主因](#item-6) ⭐️ 6.3/10
7. [商业航天迎规模商用拐点，基金经理看好赛道长期配置价值](#item-7) ⭐️ 6.3/10
8. [AI 需求火热蔓延，台积电成熟制程加入涨价潮](#item-8) ⭐️ 6.3/10
9. [韩国 7 月前 10 天出口额创纪录达 298 亿美元，同比增长 53.9%](#item-9) ⭐️ 6.3/10
10. [陶哲轩分享使用 LLM 编程智能体构建应用的体验](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [台积电 2 纳米据报道已量产，谷歌成首家手机芯片客户](https://36kr.com/newsflashes/3893386117806597?f=rss) ⭐️ 7.3/10

据报道，台积电已开始量产 2 纳米（N2）芯片，谷歌成为首家采用其 2 纳米手机芯片的客户，预计将于 8 月中旬推出新机，比苹果早约一个月。 这是半导体行业的一个重要里程碑，因为 2 纳米是 3 纳米之后的下一代制程节点，有望在性能和能效方面带来显著提升。值得注意的是，谷歌取代苹果成为首发客户，打破了苹果长期以来率先采用台积电最新制程的模式。 台积电的 N2 技术采用了第一代纳米片（全栅环绕，GAA）晶体管，这是从 3 纳米所使用的 FinFET 架构的重大转变。该节点还引入了低阻抗重布线层（RDL）和超高性能金属-绝缘体-金属（MiM）电容器，以进一步提升性能并降低功耗。

rss · 36氪 · 7月13日 01:17

**背景**: 在半导体制造中，制程节点（以纳米为单位衡量）代表晶体管缩小的代际进步，每一代新节点通常都能带来更高的晶体管密度、更强的性能和更低的功耗。3 纳米节点大约在 2022 年进入量产，2 纳米是其继任者，采用了纳米片/GAA（全栅环绕）晶体管架构以实现更好的静电控制。台积电是全球最大的代工芯片制造商，为苹果、谷歌、AMD 和英伟达等公司供应处理器，其制程路线图是整个行业的风向标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://www.asiamanufacturingreview.com/news/tsmc-advances-chip-manufacturing-with-2nm-volume-production-nwid-2409.html">TSMC Advances Chip Manufacturing With 2nm Volume Production</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#TSMC`, `#2nm`, `#Google`, `#mobile-chips`

---

<a id="item-2"></a>
## [Chromium 148 的 Math.tanh 函数泄露操作系统指纹](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 7.0/10

从 Chromium 148 开始，JavaScript 的 Math.tanh 函数改为调用宿主平台的数学库（host libm），而非 V8 自带的实现，导致其输出在不同操作系统上产生差异。因此，只需对精心选择的输入进行一次 Math.tanh 调用，就可以作为可靠的操作系统特征签名，使追踪者能够将浏览器会话与底层操作系统关联起来，即使 User-Agent 请求头被伪造也无效。 这创造了一个新的、难以缓解的指纹识别向量，削弱了用户隐私，尤其是对于那些试图在不同操作系统之间统一浏览器行为的注重隐私的浏览器（如 Tor 和 Mullvad）。同时，这也使反爬虫和数据抓取服务受益，因为它们可以通过一种隐蔽的方式检测真实操作系统，而无需依赖容易被伪造的表面信号。 虽然 V8 为大多数数学函数打包了自己的实现（大部分使用 llvm-libc，sin/cos 使用基于 glibc 派生的 dbl-64 例程），但 Math.tanh 独特地通过宿主 libm 调用——macOS 上为 libsystem_m，Linux 上为 glibc，Windows 上为 UCRT——使其成为唯一泄露操作系统的 JavaScript Math 函数。Web Audio 压缩器在 Mac 上还使用了 Apple 的 vDSP，产生了类似的指纹识别向量。Firefox 在 2021 年通过将 Math.cos/sin/tan 切换到 fdlibm 来解决了密切相关的问题。

hackernews · joahnn_s · 7月12日 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 浏览器指纹识别通过组合浏览器暴露的独特属性（屏幕尺寸、字体、时区，以及软件处理计算时的细微差异）来识别用户。诸如三角函数和双曲函数等数学函数在不同的平台之间可能会有细微差异，因为不同操作系统级别的数学库（libm 实现）使用不同的舍入策略。Math.tanh（双曲正切）是一种广泛使用的机器学习激活函数，其 JavaScript 行为对于合法用途和对抗性用途都很重要。自 2017 年以来的学术研究已经证明，通过操作系统和硬件级别特征进行跨浏览器追踪是可行的，这促使浏览器标准化数学函数的实现以关闭这些侧信道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scrapfly.dev/posts/browser-math-os-fingerprint/">Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev</a></li>
<li><a href="https://groups.google.com/a/mozilla.org/g/dev-platform/c/0dxAO-JsoXI/m/eEhjM9VsAgAJ">Intent to Implement: Use fdlibm for Math.cos, Math.sin, and Math.tan to prevent math-based fingerprinting</a></li>
<li><a href="https://yinzhicao.org/TrackingFree/crossbrowsertracking_NDSS17.pdf">(Cross-)Browser Fingerprinting via OS and Hardware Level Features Yinzhi Cao</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一，且明显带有怀疑态度：多位评论者指出该文章看起来是 AI 生成的，批评者强调出版方 Scrapfly 作为从中受益的抓取服务提供商存在明显的利益冲突。一些人认为操作系统指纹识别不如浏览器版本指纹识别有趣，因为大多数用户不会伪造 User-Agent；另一些人则建议使用正确舍入的超越函数作为长期的根治方案，并指出即使 Tor 和 Mullvad 浏览器实际上也已放弃完全隐藏操作系统信息。

**标签**: `#browser-security`, `#fingerprinting`, `#chromium`, `#privacy`, `#vulnerability`

---

<a id="item-3"></a>
## [Claude Code 在读取提示词前发送了 33k tokens；OpenCode 仅发送 7k](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 7.0/10

实证比较显示，Claude Code 的工具链在读取提示词前会发送约 33k tokens，而 OpenCode 仅发送约 7k，揭示了智能体编程工具之间显著的效率差异。

hackernews · systima · 7月12日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**标签**: `#claude-code`, `#opencode`, `#token-efficiency`, `#agentic-coding`, `#developer-tools`, `#llm-cost`

---

<a id="item-4"></a>
## [2025 年爱尔兰数据中心耗电量几乎与全国家庭用电总量相当——尽管多年来受到电网限制，服务器农场仍吞噬了全国 23%的电力](https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions) ⭐️ 6.5/10

2025 年爱尔兰数据中心消耗了该国 23%的电力，同比增长 10%。尽管存在电网接入限制，其耗电量仍几乎追平全国居民用电总量。

rss · Tom's Hardware · 7月12日 15:12

**标签**: `#data-centers`, `#energy-consumption`, `#infrastructure`, `#ireland`, `#sustainability`

---

<a id="item-5"></a>
## [FCC 批准 Reflect Orbital 太空镜面卫星](https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more) ⭐️ 6.5/10

美国联邦通信委员会（FCC）已批准 Reflect Orbital 公司的实验性卫星，该卫星利用大型轨道镜面在夜间将阳光反射到地球表面。首批测试卫星计划于今年晚些时候发射，该公司展望到 2035 年将运营超过 5 万颗卫星的星座。 这标志着美国首次为轨道阳光反射器开绿灯，为商业太空应用开辟了一个全新类别。同时，这也可能引发商业太空项目与科学界之间的冲突，因为天文学家警告说反射光可能会显著降低地面天文观测的质量。 每颗卫星的反射光预计在地面的覆盖范围约为 3 英里宽。欧洲南方天文台警告说，全面部署可能会使其位于智利的望远镜设施的背景天空亮度增加 3 到 4 倍，其影响程度可与 SpaceX 的轨道数据中心和中国竞争项目等超大规模星座带来的干扰相媲美。

rss · Tom's Hardware · 7月12日 12:20

**背景**: Reflect Orbital 成立于 2021 年，总部位于加利福尼亚州霍桑市，正在开发配备大型可展开镜面的卫星，将集中的阳光反射到地球上的特定地点，为工业和应急应用提供夜间照明。太空镜面的概念历史悠久，可以追溯到 20 世纪初的科幻小说，严肃的提案在 20 世纪 90 年代初由美国国家科学院等机构提出。FCC 的管辖范围通过无线电频谱许可覆盖所有美国商业卫星运营商，无论卫星的主要功能是什么，都赋予其有效的否决权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Reflect_Orbital">Reflect Orbital - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more">FCC approves orbital space mirrors, first test satellites will launch this year — large spacecraft reflects sunlight to Earth’s surface for construction sites, search-and-rescue lighting, and more | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space_mirror">Space mirror - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 此新闻条目未附带实质性的社区评论。

**标签**: `#space-tech`, `#satellites`, `#FCC-regulation`, `#renewable-energy`, `#controversy`

---

<a id="item-6"></a>
## [高盛：AI 或推高美国通胀，存储芯片价格暴涨为主因](https://36kr.com/newsflashes/3893440881621760?f=rss) ⭐️ 6.3/10

高盛经济学家 Megan Peters 的最新研究指出，人工智能驱动的需求正导致美国核心 PCE 通胀率每年上升约 20 个基点，预计到年底这一通胀压力将增加一倍以上，达到 50 个基点，主要推手为供应受限的内存芯片和半导体。 该分析将 AI 投资热潮与宏观经济结果联系起来，表明由于美国在 AI 基础设施和芯片制造中的核心地位，可能成为 AI 引发通胀冲击最严重的国家。这凸显了技术支出可能通过新传导路径影响美联储货币政策决策。 估算聚焦于核心 PCE，这是美联储偏好的通胀指标，剔除了波动较大的食品和能源价格。一个基点等于百分之一，因此 50 个基点意味着核心 PCE 通胀率将上升 0.5 个百分点。

rss · 36氪 · 7月13日 02:12

**背景**: 核心 PCE（个人消费支出价格指数）是美联储评估潜在通胀的首选指标，因为它剔除了波动较大的食品和能源价格，能更清晰地反映长期价格趋势。美联储的长期通胀目标为 2%，按 PCE 价格指数的年度变化来衡量。内存芯片和半导体是 AI 训练和推理的核心组件，近期这些市场的供应紧张已大幅推高价格，尤其是用于 AI 加速器的高带宽内存（HBM）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/economy-at-a-glance-inflation-pce.htm">The Fed - Inflation ( PCE )</a></li>
<li><a href="https://go-pips.com/core-personal-consumption-expenditures-inflation/">Cooling Core PCE Signals Fed Easing Soon Don't Be Last To Act</a></li>
<li><a href="https://www.investopedia.com/terms/b/basispoint.asp">investopedia.com/terms/b/basispoint.asp</a></li>

</ul>
</details>

**标签**: `#AI`, `#inflation`, `#semiconductors`, `#macroeconomics`, `#Goldman Sachs`

---

<a id="item-7"></a>
## [商业航天迎规模商用拐点，基金经理看好赛道长期配置价值](https://36kr.com/newsflashes/3893363088472832?f=rss) ⭐️ 6.3/10

中国长征十号乙运载火箭完成首次海上网系回收，成功实现运载火箭一子级可控回收，基金经理看好商业航天迎来规模商用拐点。

rss · 36氪 · 7月13日 01:06

**标签**: `#商业航天`, `#可回收火箭`, `#长征十号`, `#中国航天`, `#卫星互联网`

---

<a id="item-8"></a>
## [AI 需求火热蔓延，台积电成熟制程加入涨价潮](https://36kr.com/newsflashes/3893368739674884?f=rss) ⭐️ 6.3/10

台积电在持续调高 3 纳米等先进制程报价的同时，已陆续通知多家 IC 设计业者，拟调高成熟制程价格。具体调涨幅度因各厂商和产品线而异，将于第四季敲定，预计于 2025 年 1 月正式生效。 这表明 AI 驱动的需求已不再局限于最先进芯片，而是正在对整个半导体制造链的产能和定价产生压力。尤其依赖成熟制程的汽车、物联网、消费电子和工业领域的 IC 设计公司将面临成本上升，可能向下游产品传导。 成熟制程（通常指 28 纳米及以上）广泛用于模拟芯片、电源管理、显示驱动和微控制器等产品。台积电先进制程（如 N3）此前因苹果和 AI 加速器客户的订单爆满而连续涨价；此次涨价延伸至成熟制程，表明产能紧张已波及多条产线，而不仅仅是先进制程产线。

rss · 36氪 · 7月13日 00:59

**背景**: 半导体制造中的制程节点指的是芯片制造所使用的技术世代，节点越小（如 3 纳米），晶体管密度越高、性能越强、功耗越低，而成熟制程（如 28 纳米、16 纳米或更大）则广泛用于汽车、物联网和电源管理等日常电子产品。先进制程对 AI 加速器、CPU 和旗舰移动处理器至关重要，而成熟制程对汽车电子、物联网设备和电源管理芯片同样不可或缺。台积电作为全球最大的晶圆代工厂，同时制造先进和成熟制程芯片，客户涵盖苹果、英伟达以及数千家无晶圆 IC 设计公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://randtech.com/mature-node-semiconductor-capacity-shortage/">Why Mature - Node Capacity Is Becoming a Supply Chain Risk</a></li>
<li><a href="https://semiengineering.com/knowledge_centers/manufacturing/process/nodes/">Nodes - Semiconductor Engineering</a></li>
<li><a href="https://www.anandtech.com/show/16024/tsmc-details-3nm-process-technology-details-full-node-scaling-for-2h22">TSMC Details 3 nm Process Technology: Full Node Scaling for 2H22...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#TSMC`, `#pricing`, `#AI-demand`, `#supply-chain`

---

<a id="item-9"></a>
## [韩国 7 月前 10 天出口额创纪录达 298 亿美元，同比增长 53.9%](https://36kr.com/newsflashes/3893357324942088?f=rss) ⭐️ 6.3/10

韩国 7 月前 10 天出口额达 298 亿美元，同比增长 53.9%，去年同期为 193 亿美元，创下韩国海关统计史上任何 10 天内的最高纪录。此前纪录为 6 月份创下的 286 亿美元。同期进口额同比增长 17.4%至 235 亿美元，实现贸易顺差 64 亿美元。 创纪录的出口表现凸显了韩国在存储半导体（特别是 DRAM 和 NAND）领域的统治地位，使其成为全球 AI 基础设施供应链中的关键节点。芯片驱动的出口持续增长表明 AI 相关存储产品的需求强劲、全球芯片供应紧张，这对科技公司、下游设备制造商以及宏观经济趋势都有重要影响。 韩国在全球 DRAM 市场约占 66%份额，在 NAND 市场约占 30%份额，三星电子和 SK 海力士是两大主导厂商。7 月初 53.9%的同比增长高于整体出口增速，表明半导体出口的拉动效应远超其他品类。

rss · 36氪 · 7月13日 00:57

**背景**: 韩国经济严重依赖半导体出口，2022 年半导体出口约占其总出口的 15%。韩国拥有全球两大存储芯片制造商——三星电子和 SK 海力士，它们共同供应了全球大部分用于从智能手机到 AI 数据中心的 DRAM 和 NAND 闪存产品。韩国海关每 10 天发布一次贸易统计数据，被密切关注作为全球科技需求周期的前瞻性指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://moneyoval.com/article/south-korea-posts-highest-november-exports-on-strong-chip-and-auto-demand-s1ctg7zy7h4pyhsni9erykb6">South Korea posts highest November exports on strong chip and...</a></li>
<li><a href="https://worldmetrics.org/south-korea-semiconductor-industry-statistics/">South Korea Semiconductor Industry Statistics | 2026 Edition</a></li>
<li><a href="https://economixplus.com/semiconductors/">South Korea vs Taiwan: Who Excels in Semiconductors ?</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#trade-data`, `#korea`, `#chip-industry`, `#economic-indicators`

---

<a id="item-10"></a>
## [陶哲轩分享使用 LLM 编程智能体构建应用的体验](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 6.0/10

菲尔兹奖得主陶哲轩（Terence Tao）发表了一篇博客文章，详细介绍了他使用现代基于 LLM 的编程智能体构建新应用和改造旧应用的体验。他描述了这些 AI 工具如何让他在无需深厚软件工程专业知识的情况下，创建出能辅助其数学研究的软件和交互式可视化工具。 当一位世界著名的数学家公开认可 LLM 编程智能体时，这表明这些工具已经成熟到足以让传统软件工程以外的领域专家独立创建功能性应用。这一趋势标志着能够生产软件的人群范围大幅扩大，并可能释放学术界、科学界及其他非软件领域对定制工具的潜在需求。 陶哲轩特别强调使用 LLM 智能体来为其研究论文构建交互式补充材料，同时谨慎地指出这些可视化并非关键任务，因此 LLM 生成错误的风险是可以接受的。他强调了一种平衡的使用方式：这些工具非常适合原型设计和辅助性工作，但不应在关键的、核心的软件任务中盲目信任。

hackernews · subset · 7月12日 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: LLM 编程智能体是由大语言模型驱动的 AI 系统，能够自主读取、编写和编辑整个项目文件中的代码，超越了简单的逐行代码补全功能。与早期只能建议下一行代码的 AI 编程助手不同，这些智能体可以规划多步骤任务、浏览代码库，并执行复杂的软件构建工作流。陶哲轩是当今最著名的在世数学家之一，2006 年获得菲尔兹奖，他公开使用 AI 工具在学术界和科技界都具有重大影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective AI Agents \ Anthropic</a></li>
<li><a href="https://aicoderhq.com/blog/ai-code-completion-vs-agents-ships-code">AI Code Completion vs AI Agents : Which Actually... | AI Coder HQ</a></li>

</ul>
</details>

**社区讨论**: 社区评论者普遍认同陶哲轩这一演示的重要意义，一位评论者强调了传统软件领域之外对软件的巨大潜在需求，并估计需要十年时间才能赶上现已具备的新型软件编写能力。其他人赞赏陶哲轩的平衡观点——即 LLM 编码的补充材料有用但不值得在关键任务中信任，同时有人幽默地将菲尔兹奖得主使用编程智能体比作米其林星级厨师发现微波炉晚餐。一位计算机科学教育者也分享了 LLM 如何帮助他们快速构建长期渴望的教学可视化工具，例如一个简化的 8 位计算机模拟器。

**标签**: `#LLM`, `#coding-agents`, `#AI-tools`, `#software-development`, `#Terry-Tao`

---