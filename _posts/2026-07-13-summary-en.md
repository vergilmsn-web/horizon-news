---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 51 items, 10 important content pieces were selected

---

1. [TSMC Reportedly Begins 2nm Mass Production, Google First Mobile Customer](#item-1) ⭐️ 7.3/10
2. [Chromium 148 Math.tanh Leaks Operating System via Fingerprinting](#item-2) ⭐️ 7.0/10
3. [Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k](#item-3) ⭐️ 7.0/10
4. [Ireland’s data centers consumed nearly as much electricity as every home in the country combined in 2025 — server farms gulped 23% of national power despite years of grid restrictions](#item-4) ⭐️ 6.5/10
5. [FCC Approves Reflect Orbital's Space Mirror Satellites](#item-5) ⭐️ 6.5/10
6. [Goldman Sachs: AI May Drive US Inflation, Memory Chip Surge Is Key Driver](#item-6) ⭐️ 6.3/10
7. [商业航天迎规模商用拐点，基金经理看好赛道长期配置价值](#item-7) ⭐️ 6.3/10
8. [TSMC Extends Price Hikes to Mature Nodes Amid AI Demand Surge](#item-8) ⭐️ 6.3/10
9. [South Korea's July First 10-Day Exports Hit Record $29.8B, Up 53.9% YoY on Chip Demand](#item-9) ⭐️ 6.3/10
10. [Terry Tao Explores LLM Coding Agents for Building Apps](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [TSMC Reportedly Begins 2nm Mass Production, Google First Mobile Customer](https://36kr.com/newsflashes/3893386117806597?f=rss) ⭐️ 7.3/10

TSMC has reportedly started mass production of its 2nm (N2) chips, with Google becoming the first mobile chip customer. Google is expected to launch a new phone in mid-August, approximately one month ahead of Apple. This marks a significant milestone in the semiconductor industry, as 2nm is the next major node after 3nm and promises meaningful gains in performance and power efficiency. Notably, Google leapfrogging Apple as the lead mobile adopter breaks Apple's long-standing pattern of being first to debut new TSMC process nodes. TSMC's N2 technology uses first-generation nanosheet (gate-all-around) transistors, a shift from the FinFET architecture used at 3nm. The node also incorporates a low-resistance redistribution layer (RDL) and super high-performance metal-insulator-metal (MiM) capacitors to further boost performance and reduce power consumption.

rss · 36氪 · Jul 13, 01:17

**Background**: In semiconductor manufacturing, process nodes (measured in nanometers) represent successive generations of transistor scaling, where each new node typically delivers higher transistor density, better performance, and lower power consumption. The 3nm node entered mass production around 2022, and 2nm is its successor, featuring a shift to nanosheet/GAA transistor architecture for better electrostatic control. TSMC is the world's largest contract chipmaker and supplies processors to companies including Apple, Google, AMD, and Nvidia, making its process roadmap a bellwether for the entire industry.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://www.asiamanufacturingreview.com/news/tsmc-advances-chip-manufacturing-with-2nm-volume-production-nwid-2409.html">TSMC Advances Chip Manufacturing With 2nm Volume Production</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#TSMC`, `#2nm`, `#Google`, `#mobile-chips`

---

<a id="item-2"></a>
## [Chromium 148 Math.tanh Leaks Operating System via Fingerprinting](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 7.0/10

Starting with Chromium 148, the JavaScript Math.tanh function was changed to route through the host platform's math library (host libm) instead of V8's bundled implementation, causing its output to differ across operating systems. As a result, a single Math.tanh call on a carefully chosen input can serve as a reliable per-OS signature, enabling trackers to link a browser session to the underlying OS regardless of spoofed User-Agent headers. This creates a new, hard-to-mitigate fingerprinting vector that undermines user privacy, particularly for privacy-focused browsers like Tor and Mullvad that try to equalize browser behavior across OSes. It also benefits anti-bot and scraping services by providing a stealthy way to detect the real OS without relying on easily-spoofed surface-level signals. While V8 bundles its own math routines for most functions (llvm-libc for most, a glibc-derived dbl-64 routine for sin/cos), Math.tanh is uniquely routed through the host libm—libsystem_m on macOS, glibc on Linux, UCRT on Windows—making it the lone JavaScript Math function that leaks the OS. The Web Audio compressor additionally uses Apple's vDSP on Mac, creating a parallel fingerprinting vector. Firefox addressed a closely related issue in 2021 by switching Math.cos/sin/tan to fdlibm.

hackernews · joahnn_s · Jul 12, 21:12 · [Discussion](https://news.ycombinator.com/item?id=48884853)

**Background**: Browser fingerprinting identifies users by combining the unique attributes their browser exposes—screen size, fonts, timezone, and subtle differences in how software handles computations. Mathematical functions such as trigonometric and hyperbolic operations can vary slightly between platforms because different OS-level math libraries (libm implementations) use different rounding strategies. Math.tanh (hyperbolic tangent) is a widely used machine learning activation function, making its JavaScript behavior relevant for both legitimate and adversarial purposes. Academic research since 2017 has demonstrated that cross-browser tracking via OS- and hardware-level features is feasible, which has motivated browsers to standardize math implementations to close these side channels.

<details><summary>References</summary>
<ul>
<li><a href="https://scrapfly.dev/posts/browser-math-os-fingerprint/">Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev</a></li>
<li><a href="https://groups.google.com/a/mozilla.org/g/dev-platform/c/0dxAO-JsoXI/m/eEhjM9VsAgAJ">Intent to Implement: Use fdlibm for Math.cos, Math.sin, and Math.tan to prevent math-based fingerprinting</a></li>
<li><a href="https://yinzhicao.org/TrackingFree/crossbrowsertracking_NDSS17.pdf">(Cross-)Browser Fingerprinting via OS and Hardware Level Features Yinzhi Cao</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed and notably skeptical: multiple commenters pointed out the article appears to be AI-generated, and critics highlighted that Scrapfly, the publishing company, has a clear conflict of interest as a scraping service provider that benefits from refined fingerprinting techniques. Some argued that OS fingerprinting is less interesting than browser-version fingerprinting because most users don't spoof their User-Agent, while others proposed correctly rounded transcendental functions as the proper long-term fix and observed that even Tor and Mullvad browsers have effectively given up on fully obscuring the operating system.

**Tags**: `#browser-security`, `#fingerprinting`, `#chromium`, `#privacy`, `#vulnerability`

---

<a id="item-3"></a>
## [Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 7.0/10

Empirical comparison shows Claude Code's harness sends ~33k tokens before reading the prompt versus OpenCode's ~7k, revealing significant efficiency differences between agentic coding tools.

hackernews · systima · Jul 12, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48883275)

**Tags**: `#claude-code`, `#opencode`, `#token-efficiency`, `#agentic-coding`, `#developer-tools`, `#llm-cost`

---

<a id="item-4"></a>
## [Ireland’s data centers consumed nearly as much electricity as every home in the country combined in 2025 — server farms gulped 23% of national power despite years of grid restrictions](https://www.tomshardware.com/tech-industry/data-centers/irelands-data-centers-consumed-nearly-as-much-electricity-as-every-home-in-the-country-combined-in-2025-server-farms-gulped-23-percent-of-national-power-despite-years-of-grid-restrictions) ⭐️ 6.5/10

Ireland's data centers consumed 23% of the country's electricity in 2025—a 10% year-over-year increase—nearly matching total residential consumption despite grid connection restrictions.

rss · Tom's Hardware · Jul 12, 15:12

**Tags**: `#data-centers`, `#energy-consumption`, `#infrastructure`, `#ireland`, `#sustainability`

---

<a id="item-5"></a>
## [FCC Approves Reflect Orbital's Space Mirror Satellites](https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more) ⭐️ 6.5/10

The U.S. Federal Communications Commission has approved Reflect Orbital's experimental satellite that uses large orbital mirrors to reflect sunlight onto Earth's surface at night. The first test satellites are scheduled to launch later this year, with the company envisioning a constellation of over 50,000 satellites by 2035. This marks the first regulatory green light for orbital sunlight reflectors in the United States, opening the door for a new category of commercial space applications. It also sets up a potential conflict between commercial space ventures and the scientific community, as astronomers warn the reflected light could significantly degrade ground-based observations. The reflected light from each satellite is expected to span an area approximately 3 miles wide on the ground. The European Southern Observatory has warned that full deployment could increase background sky brightness at its Chilean telescope facilities by a factor of three to four, rivaling the disruption threatened by mega-constellations like SpaceX's Orbital Data Center and China's competing project.

rss · Tom's Hardware · Jul 12, 12:20

**Background**: Reflect Orbital, founded in 2021 and headquartered in Hawthorne, California, is developing satellites equipped with large deployable mirrors that reflect concentrated sunlight to specific points on Earth, enabling nighttime illumination for industrial and emergency applications. The concept of space mirrors has a long history dating back to early 20th-century science fiction, with serious proposals emerging from institutions like the U.S. National Academy of Sciences in the early 1990s. The FCC's jurisdiction extends to all U.S.-based commercial satellite operators through radio spectrum licensing, giving it effective veto power regardless of a satellite's primary function.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Reflect_Orbital">Reflect Orbital - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/fcc-approves-orbital-space-mirrors-first-test-satellites-will-launch-this-year-large-spacecraft-reflects-sunlight-to-earths-surface-for-construction-sites-search-and-rescue-lighting-and-more">FCC approves orbital space mirrors, first test satellites will launch this year — large spacecraft reflects sunlight to Earth’s surface for construction sites, search-and-rescue lighting, and more | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space_mirror">Space mirror - Wikipedia</a></li>

</ul>
</details>

**Discussion**: No substantive community comments were provided with this news item.

**Tags**: `#space-tech`, `#satellites`, `#FCC-regulation`, `#renewable-energy`, `#controversy`

---

<a id="item-6"></a>
## [Goldman Sachs: AI May Drive US Inflation, Memory Chip Surge Is Key Driver](https://36kr.com/newsflashes/3893440881621760?f=rss) ⭐️ 6.3/10

Goldman Sachs economists estimate that AI-driven demand is currently adding approximately 20 basis points to US core PCE inflation annually, with this pressure projected to more than double to 50 basis points by year-end, driven by supply-constrained memory chips and semiconductors. This analysis connects the AI investment boom to macroeconomic outcomes, suggesting the US may bear the brunt of AI-induced inflation because of its central role in AI infrastructure and chip manufacturing. It highlights a new transmission channel through which technology spending could complicate the Federal Reserve's monetary policy decisions. The estimate focuses on core PCE, the Federal Reserve's preferred inflation gauge, which excludes volatile food and energy prices. A basis point equals one-hundredth of one percent, so a 50-basis-point increase would raise core PCE inflation by half a percentage point.

rss · 36氪 · Jul 13, 02:12

**Background**: Core PCE (Personal Consumption Expenditures) inflation is the Federal Reserve's preferred measure for assessing underlying inflation because it excludes volatile food and energy prices, offering a clearer view of long-term price trends. The Fed targets 2% inflation over the longer run as measured by annual changes in the PCE price index. Memory chips and semiconductors are essential components for AI training and inference, and recent supply constraints in these markets have driven prices sharply higher, particularly for high-bandwidth memory used in AI accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalreserve.gov/economy-at-a-glance-inflation-pce.htm">The Fed - Inflation ( PCE )</a></li>
<li><a href="https://go-pips.com/core-personal-consumption-expenditures-inflation/">Cooling Core PCE Signals Fed Easing Soon Don't Be Last To Act</a></li>
<li><a href="https://www.investopedia.com/terms/b/basispoint.asp">investopedia.com/terms/b/basispoint.asp</a></li>

</ul>
</details>

**Tags**: `#AI`, `#inflation`, `#semiconductors`, `#macroeconomics`, `#Goldman Sachs`

---

<a id="item-7"></a>
## [商业航天迎规模商用拐点，基金经理看好赛道长期配置价值](https://36kr.com/newsflashes/3893363088472832?f=rss) ⭐️ 6.3/10

中国长征十号乙运载火箭完成首次海上网系回收，成功实现运载火箭一子级可控回收，基金经理看好商业航天迎来规模商用拐点。

rss · 36氪 · Jul 13, 01:06

**Tags**: `#商业航天`, `#可回收火箭`, `#长征十号`, `#中国航天`, `#卫星互联网`

---

<a id="item-8"></a>
## [TSMC Extends Price Hikes to Mature Nodes Amid AI Demand Surge](https://36kr.com/newsflashes/3893368739674884?f=rss) ⭐️ 6.3/10

TSMC is notifying multiple IC design companies of planned price increases on mature process nodes, following its earlier price hikes on advanced nodes such as 3nm. The specific increase will vary by manufacturer and product line, with final details to be determined in Q4 2024 and new prices expected to take effect in January 2025. This signals that AI-driven demand is no longer confined to cutting-edge chips but is now creating capacity strain and pricing pressure across the entire semiconductor manufacturing chain. IC designers, especially those serving automotive, IoT, consumer electronics, and industrial segments that rely on mature nodes, will face higher costs that may be passed on to downstream products. Mature process nodes — typically 28nm and above — are widely used in analog, power management, display drivers, and microcontroller chips. TSMC's advanced nodes (such as N3) had already seen successive price increases due to full order books from customers like Apple and AI accelerator firms; the extension to mature nodes indicates that capacity utilization is tight across multiple fab lines, not just leading-edge fabs.

rss · 36氪 · Jul 13, 00:59

**Background**: Process nodes in semiconductor manufacturing refer to the technology generation used to fabricate chips, with smaller nodes (e.g., 3nm) offering higher transistor density, better performance, and lower power consumption compared to mature nodes (e.g., 28nm, 16nm, or larger). While advanced nodes are critical for AI accelerators, CPUs, and flagship mobile processors, mature nodes remain essential for a wide range of everyday electronics including automotive components, IoT devices, and power management ICs. TSMC, the world's largest contract chipmaker, manufactures both advanced and mature nodes and supplies customers ranging from Apple and NVIDIA to thousands of fabless IC design houses.

<details><summary>References</summary>
<ul>
<li><a href="https://randtech.com/mature-node-semiconductor-capacity-shortage/">Why Mature - Node Capacity Is Becoming a Supply Chain Risk</a></li>
<li><a href="https://semiengineering.com/knowledge_centers/manufacturing/process/nodes/">Nodes - Semiconductor Engineering</a></li>
<li><a href="https://www.anandtech.com/show/16024/tsmc-details-3nm-process-technology-details-full-node-scaling-for-2h22">TSMC Details 3 nm Process Technology: Full Node Scaling for 2H22...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#TSMC`, `#pricing`, `#AI-demand`, `#supply-chain`

---

<a id="item-9"></a>
## [South Korea's July First 10-Day Exports Hit Record $29.8B, Up 53.9% YoY on Chip Demand](https://36kr.com/newsflashes/3893357324942088?f=rss) ⭐️ 6.3/10

South Korea's exports for the first 10 days of July reached $29.8 billion, up 53.9% year-over-year from $19.3 billion in the same period last year, setting a new record for any 10-day period in Korea Customs Service history. The previous record was $28.6 billion set in June. Imports grew 17.4% YoY to $23.5 billion, yielding a trade surplus of $6.4 billion. This record-breaking export performance underscores how South Korea's dominance in memory semiconductors—particularly DRAM and NAND—has made the country a critical chokepoint in the global AI infrastructure supply chain. Sustained chip-driven export growth signals robust demand for AI-related memory products and tight global chip supply, with implications for tech companies, downstream device makers, and macroeconomic trends. South Korea controls roughly 66% of the global DRAM market and 30% of the NAND market, with Samsung Electronics and SK Hynix as the dominant players. The 53.9% YoY surge in early July outpaces the broader export growth, suggesting semiconductor exports are pulling significantly above non-chip categories.

rss · 36氪 · Jul 13, 00:57

**Background**: South Korea's economy is heavily dependent on semiconductor exports, which accounted for roughly 15% of its total exports in 2022. The country hosts two of the world's largest memory chip makers—Samsung Electronics and SK Hynix—which together supply the majority of DRAM and NAND flash memory used in everything from smartphones to AI data centers. Korea Customs Service publishes frequent (every 10 days) trade statistics, which are closely watched as an early indicator of global tech demand cycles.

<details><summary>References</summary>
<ul>
<li><a href="https://moneyoval.com/article/south-korea-posts-highest-november-exports-on-strong-chip-and-auto-demand-s1ctg7zy7h4pyhsni9erykb6">South Korea posts highest November exports on strong chip and...</a></li>
<li><a href="https://worldmetrics.org/south-korea-semiconductor-industry-statistics/">South Korea Semiconductor Industry Statistics | 2026 Edition</a></li>
<li><a href="https://economixplus.com/semiconductors/">South Korea vs Taiwan: Who Excels in Semiconductors ?</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#trade-data`, `#korea`, `#chip-industry`, `#economic-indicators`

---

<a id="item-10"></a>
## [Terry Tao Explores LLM Coding Agents for Building Apps](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 6.0/10

Fields Medalist Terence Tao published a blog post detailing his experience using modern LLM-based coding agents to build new applications and revamp old ones. He described how these AI tools allowed him to create software and interactive visualizations that complement his mathematical research without requiring deep software engineering expertise. When a world-renowned mathematician publicly endorses LLM coding agents, it signals that these tools have matured enough for domain experts outside traditional software engineering to independently create functional applications. This trend points to a significant expansion of who can produce software and a potential unlocking of latent demand for custom tools across academia, science, and other non-software fields. Tao specifically highlights using LLM agents to build interactive supplements to his research papers, while carefully noting that these visualizations are not mission-critical, so the risk of LLM-generated errors is acceptable. He emphasizes a balanced approach: the tools are powerful for prototyping and supplementary work but should not be blindly trusted for core, critical software.

hackernews · subset · Jul 12, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48880170)

**Background**: LLM coding agents are AI systems powered by large language models that can autonomously read, write, and edit code across entire project files, going beyond simple line-by-line code completion. Unlike earlier AI coding assistants that only suggested the next few lines, these agents can plan multi-step tasks, navigate codebases, and execute complex software-building workflows. Terence Tao is one of the most celebrated living mathematicians, awarded the Fields Medal in 2006, and his public engagement with AI tools carries significant weight in both academic and tech communities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/building-effective-agents">Building Effective AI Agents \ Anthropic</a></li>
<li><a href="https://aicoderhq.com/blog/ai-code-completion-vs-agents-ships-code">AI Code Completion vs AI Agents : Which Actually... | AI Coder HQ</a></li>

</ul>
</details>

**Discussion**: Community commenters broadly agree on the significance of Tao's demonstration, with one highlighting the vast latent demand for software outside traditional software-focused spaces and estimating it would take a decade to catch up to the new software-writing abilities now available. Others appreciated Tao's balanced perspective that LLM-coded supplements are useful but not trustworthy for mission-critical work, while humorous comparisons likened a Fields Medalist using coding agents to a Michelin-starred chef discovering microwave dinners. A CS educator also shared how LLMs helped them quickly build long-desired teaching visualizations like a simplified 8-bit computer.

**Tags**: `#LLM`, `#coding-agents`, `#AI-tools`, `#software-development`, `#Terry-Tao`

---