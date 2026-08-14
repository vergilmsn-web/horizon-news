---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 84 items, 20 important content pieces were selected

---

1. [NVIDIA Secures TSMC A16 Node for Next-Generation "Feynman" GPUs](#item-1) ⭐️ 8.5/10
2. [TSMC Achieves 98% Yield on CoWoS-L with 5.5x Reticle Size, 14x Comes in 2029](#item-2) ⭐️ 8.5/10
3. [Just one instruction on AMD's 2015-era CPUs cracks open secret memory areas and gives full hardware-level control — exploit for 15h and 16h chip families gets you access to Platform Security Processor, microcode, and System Management Interface](#item-3) ⭐️ 8.5/10
4. [GLM-5.3: Frontier coding with emergent cyber capabilities](#item-4) ⭐️ 8.0/10
5. [Christopher Domas Releases 'skitter' DRAM Exploit Tool for AMD CPUs](#item-5) ⭐️ 8.0/10
6. [Understanding is the new bottleneck](#item-6) ⭐️ 8.0/10
7. [Nvidia Jetson Chip Found in Russian Cruise Missile: Ukraine Claims](#item-7) ⭐️ 7.5/10
8. [ShieldBreak: New Windows Zero-Day Privilege Escalation Vulnerability Disclosed](#item-8) ⭐️ 7.5/10
9. [Gemini 3.7 Flash](#item-9) ⭐️ 7.0/10
10. [Dan McKinley's 'Choose Boring Technology' Essay Still Resonates a Decade Later](#item-10) ⭐️ 7.0/10
11. [ASML’s Path to Lithography Dominance—and the Coming Maskless Revolution](#item-11) ⭐️ 7.0/10
12. [Intel at a Memory Crossroads: Considering a Return to Memory Chip Manufacturing](#item-12) ⭐️ 7.0/10
13. [All-Solid-State Batteries (ASSBs) Advance to Pilot Production in 2026](#item-13) ⭐️ 7.0/10
14. [Epic Games Launcher Coming "Soon" to Linux](#item-14) ⭐️ 6.5/10
15. [Microsoft Unifies Copilot Features Into a Super App](#item-15) ⭐️ 6.5/10
16. [US Imposes Up to 100% Tariffs on Foreign-Made Drones, Targeting China](#item-16) ⭐️ 6.5/10
17. [Intel VP Hallock on Nova Lake and DDR4 Comeback Strategy](#item-17) ⭐️ 6.5/10
18. [Prusa Research upgrades entire 3D printer lineup to second-generation '+' models for free](#item-18) ⭐️ 6.5/10
19. [Near-Packaged Optics Gains Ground as Hedge Against CPO's Growing Pains](#item-19) ⭐️ 6.5/10
20. [Microchip Showcases 160-Lane PCIe Gen6 Switch at FMS 2026](#item-20) ⭐️ 6.5/10

---

<a id="item-1"></a>
## [NVIDIA Secures TSMC A16 Node for Next-Generation "Feynman" GPUs](https://www.techpowerup.com/351607/nvidia-secures-tsmc-a16-node-for-next-generation-feynman-gpus) ⭐️ 8.5/10

NVIDIA is prototyping its post-Rubin 'Feynman' GPU architecture on TSMC's A16 (1.6nm) node with backside power delivery and 3D chiplet packaging, with mass production scheduled for H2 2028.

rss · TechPowerUp News · Aug 14, 09:56

**Tags**: `#NVIDIA`, `#TSMC`, `#semiconductors`, `#GPU architecture`, `#advanced packaging`

---

<a id="item-2"></a>
## [TSMC Achieves 98% Yield on CoWoS-L with 5.5x Reticle Size, 14x Comes in 2029](https://www.techpowerup.com/351584/tsmc-achieves-98-yield-on-cowos-l-with-5-5x-reticle-size-14x-comes-in-2029) ⭐️ 8.5/10

TSMC has achieved 98% packaging yield on CoWoS-L at 5.5x reticle size (858 mm²), enabling 4,720 mm² silicon integration, with a 14x reticle variant (~12,012 mm²) planned for 2029 alongside the A13 node.

rss · TechPowerUp News · Aug 13, 15:37

**Tags**: `#semiconductors`, `#TSMC`, `#CoWoS`, `#advanced-packaging`, `#AI-hardware`

---

<a id="item-3"></a>
## [Just one instruction on AMD's 2015-era CPUs cracks open secret memory areas and gives full hardware-level control — exploit for 15h and 16h chip families gets you access to Platform Security Processor, microcode, and System Management Interface](https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas) ⭐️ 8.5/10

A newly disclosed exploit targeting AMD's 2015-era 15h and 16h CPU families allows a single instruction to access protected memory areas, exposing the Platform Security Processor, microcode, and System Management Interface to hardware-level control.

rss · Tom's Hardware · Aug 14, 09:33

**Tags**: `#security`, `#amd`, `#cpu-vulnerability`, `#hardware-exploit`, `#platform-security`

---

<a id="item-4"></a>
## [GLM-5.3: Frontier coding with emergent cyber capabilities](https://z.ai/blog/glm-5.3) ⭐️ 8.0/10

Z.ai releases GLM-5.3, a frontier coding model with emergent cyber capabilities, already scanning OSS at scale and disclosing numerous CVEs, prompting rapid commercial adoption.

hackernews · pella · Aug 14, 05:19 · [Discussion](https://news.ycombinator.com/item?id=49294997)

**Tags**: `#ai-models`, `#cybersecurity`, `#vulnerability-disclosure`, `#code-generation`, `#frontier-ai`

---

<a id="item-5"></a>
## [Christopher Domas Releases 'skitter' DRAM Exploit Tool for AMD CPUs](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

Security researcher Christopher Domas has released a proof-of-concept tool called 'skitter-creek-bath-salts' that exploits a vulnerability in AMD's DRAM-controller configuration, allowing attackers to bypass hardware-enforced memory isolation and gain access to protected areas including the Platform Security Processor (PSP), System Management Mode (SMM), and microcode patch RAM with a single instruction on AMD 15h and 16h chip families. This research exposes a significant hardware-level attack surface on AMD processors used in gaming consoles and consumer devices, potentially enabling deep system compromise. If exploited, it could allow attackers to extract firmware secrets, install persistent implants, and break the trust roots that modern CPUs rely on for secure boot and measured computing. The attack works by flipping specific configuration bits in the memory controller to rewrite how physical addresses map onto actual DRAM cells—a process Domas describes as 'spaghettifying' memory. The exploit targets AMD's 16h (Jaguar, 2013) family by default, with partial notes for Zen 3 (different memory controller register base address), but applicability to newer CPU families remains unclear from the documentation.

hackernews · matt_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: Modern CPUs use multiple privilege levels (rings) to isolate sensitive operations from normal software; 'ring 0' provides the highest OS-level access, while negative rings (like SMM and PSP) handle even more privileged functions such as firmware, secure boot, and hardware-level trust. DRAM scrambling is a technique used by memory controllers to remap physical addresses to DRAM cells, originally designed to reduce electrical interference and improve signal integrity. AMD's Platform Security Processor (PSP) is an ARM-based coprocessor embedded in AMD CPUs that handles sensitive operations including the fTPM (firmware TPM) and firmware validation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/ skitter -creek-bath-salts: Unlocking _everything...</a></li>
<li><a href="https://gbhackers.com/new-dram-scrambling-attack-unlocks-amd-cpu-psp-smm/">New DRAM Scrambling Attack Unlocks AMD CPU PSP, SMM and...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas">Just one instruction on AMD's 2015-era CPUs gets... | Tom's Hardware</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly enthusiastic, with commenters praising Domas's track record and eagerly anticipating his Black Hat talk, linking his previous research (MoVfuscator, hardware backdoors in x86). Technical commenters raised concerns about the attack's scope on modern CPUs—specifically questioning applicability beyond AMD Jaguar 16h and whether Zen 3+ architectures are also vulnerable. Others noted the implications for gaming console security, observing that achieving ring-0 access on Xbox and PlayStation hardware would expose nearly all system secrets.

**Tags**: `#security`, `#DRAM`, `#hardware-exploitation`, `#Christopher-Domas`, `#Black-Hat`

---

<a id="item-6"></a>
## [Understanding is the new bottleneck](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck) ⭐️ 8.0/10

As LLMs automate code writing, understanding code—its purpose, model, and motivations—becomes the new critical bottleneck in software engineering workflows.

hackernews · sebg · Aug 13, 18:47 · [Discussion](https://news.ycombinator.com/item?id=49290299)

**Tags**: `#AI`, `#software-engineering`, `#LLMs`, `#code-review`, `#developer-productivity`

---

<a id="item-7"></a>
## [Nvidia Jetson Chip Found in Russian Cruise Missile: Ukraine Claims](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-jetson-chip-found-in-russian-cruise-missile-ukraine-claims-presence-in-s-71-monochrome-weapon-may-indicate-use-of-ai-tech) ⭐️ 7.5/10

Ukrainian intelligence has claimed that Russia's new S-71 'Monochrome' cruise missile incorporates Nvidia Jetson Orin NX AI modules, allegedly used to provide AI-powered terminal guidance for targeting. This revelation raises serious questions about export controls on commercial AI hardware, as the Jetson Orin NX is a widely available developer module sold globally. It highlights the dual-use nature of consumer-grade AI chips and may pressure Nvidia and regulators to tighten restrictions on chip sales to Russia and other sanctioned entities. The Jetson Orin NX delivers up to 100 TOPS of AI performance in a compact SO-DIMM form factor, making it suitable for edge AI applications including robotics and autonomous systems. Terminal guidance refers to the final phase of a missile's flight when it homes in on a target, and AI-based guidance could enable object recognition or autonomous target selection.

rss · Tom's Hardware · Aug 14, 10:30

**Background**: The Nvidia Jetson platform is a family of compact, low-power computing modules designed for embedded AI applications such as drones, robots, and IoT devices. Cruise missiles are self-propelled guided weapons that fly to a target area and use a guidance system — terminal guidance being the final phase of targeting — to increase hit accuracy. The use of commercial off-the-shelf (COTS) components in military systems is a well-established practice, but the integration of modern AI accelerators like the Jetson Orin NX represents a new escalation in the sophistication of weaponized consumer technology.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/embedded/jetson-modules">Jetson Modules , Support, Ecosystem, and Lineup | NVIDIA Developer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Missile">Missile - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI-hardware`, `#military-tech`, `#geopolitics`, `#export-controls`

---

<a id="item-8"></a>
## [ShieldBreak: New Windows Zero-Day Privilege Escalation Vulnerability Disclosed](https://www.tomshardware.com/tech-industry/cyber-security/microsofts-nemesis-drops-new-zero-day-privilege-escalation-vulnerability-attack-grants-system-level-privileges-but-it-could-already-be-patched) ⭐️ 7.5/10

Security researcher Nightmare Eclipse disclosed ShieldBreak, a new Windows zero-day privilege escalation vulnerability that exploits a flaw in Microsoft Defender's security engine to escalate a low-level user to full SYSTEM-level access. Microsoft has already deployed a Defender-side mitigation to block the exploit, and security researcher Will Dormann independently verified the reported behavior. The vulnerability is particularly concerning because it ironically requires Microsoft Defender to be enabled for the exploit to function, meaning systems relying on Defender for protection are precisely those most at risk. The disclosure highlights the ongoing cat-and-mouse game between vulnerability researchers and Microsoft's security teams, and security teams should immediately verify their Defender coverage is current. ShieldBreak specifically bypasses Microsoft's July mitigation for CVE-2026-50656, suggesting an evolving vulnerability chain targeting Defender's security engine. The fact that Microsoft was able to push a Defender-side fix quickly indicates the issue was treated as high priority, though the irony of exploiting the very software meant to protect Windows systems remains noteworthy.

rss · Tom's Hardware · Aug 13, 17:36

**Background**: A privilege escalation vulnerability allows an attacker who already has some level of access to a system to elevate their privileges to a higher tier, such as gaining SYSTEM-level access on Windows, which is the highest privilege level granting complete control over the operating system. A zero-day vulnerability is one that is exploited before the vendor has had time to release a patch, making it especially dangerous. Microsoft Defender is the built-in antivirus and security software on Windows, and flaws within it are ironic since it is designed to protect against exactly these kinds of attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.varindia.com/news/shieldbreak-vulnerability-in-microsoft-defender-may-enable-full-system-access">ShieldBreak Vulnerability in Microsoft Defender May Enable Full</a></li>
<li><a href="https://en.cryptonomist.ch/2026/08/12/windows-security-vulnerability-shieldbreak/">Windows Security Vulnerability Exposes ShieldBreak Exploit</a></li>
<li><a href="https://windowsreport.com/shieldbreak-zero-day-grants-system-access-on-fully-patched-windows/">ShieldBreak Zero-Day Grants SYSTEM Access on Fully Patched...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#windows`, `#zero-day`, `#privilege-escalation`, `#vulnerability-disclosure`

---

<a id="item-9"></a>
## [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

Google announces Gemini 3.7 Flash with new pricing structure, prompting community discussion about model versioning cadence, pricing sustainability, and practical performance comparisons against competitors.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**Tags**: `#AI`, `#LLM`, `#Google`, `#Gemini`, `#model-release`

---

<a id="item-10"></a>
## [Dan McKinley's 'Choose Boring Technology' Essay Still Resonates a Decade Later](https://mcfunley.com/choose-boring-technology) ⭐️ 7.0/10

Dan McKinley's classic 2015 essay advocating for the use of boring, proven technologies in software engineering has been re-shared and generated 392 points with 217 comments on Hacker News. The post re-introduces his influential 'innovation tokens' framework, which has become a widely adopted mental model for technology selection. The essay provides a powerful framework for engineering teams and leaders to make deliberate tradeoffs about when to adopt new tools versus proven solutions. The concept helps prevent technology choices from becoming ends in themselves, and remains highly relevant as organizations continue to grapple with the hype around new architectures like microservices and Kubernetes. The central metaphor proposes that every team has roughly three 'innovation tokens' to spend—choosing boring technologies is essentially 'free,' but each adoption of new, risky tech costs a token that should ideally be spent on areas that differentiate the product. The essay was originally published on March 30, 2015, drawing from McKinley's six years of experience as an engineer at Etsy.

hackernews · tosh · Aug 13, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49289512)

**Background**: Dan McKinley is a software engineer best known for his time at Etsy, where he observed how a highly productive engineering team often succeeded by limiting technology churn. The 'innovation tokens' concept works as a budget metaphor: when evaluating any new technology (database, language, framework), teams must weigh whether the innovation is worth spending a scarce token on. The essay was written during the height of the microservices hype, when many teams were adopting new architectures without clear justification, and it pushed back against treating 'new' as inherently 'better.'

<details><summary>References</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Dan McKinley :: Choose Boring Technology</a></li>
<li><a href="https://boringtechnology.club/?ref=alexandre.storelli.fr">Choose Boring Technology</a></li>
<li><a href="https://jonathannen.com/choose-boring-technology/">Dan McKinley 's classic advice on " choosing boring technology " is....</a></li>

</ul>
</details>

**Discussion**: Commenters overwhelmingly endorsed the innovation tokens concept, with one PM/engineering leader calling it 'one of the most useful concepts' in their career for both making and explaining tradeoffs. Concrete examples were shared: one engineer described running two bare-metal Linux servers with Postgres, HAProxy, and PHP to achieve 99.99% uptime for most business needs, while another noted how they ported an R script to LINQPad because nobody on the team had R experience, illustrating the 'optimize globally' principle. Several commenters observed that despite the essay's age, it remains relevant because newer, less experienced engineers continue to be lured into chasing fashionable architectures.

**Tags**: `#software-engineering`, `#technology-selection`, `#engineering-management`, `#architecture`, `#best-practices`

---

<a id="item-11"></a>
## [ASML’s Path to Lithography Dominance—and the Coming Maskless Revolution](https://semiwiki.com/lithography/372177-asmls-path-to-lithography-dominance-and-the-coming-maskless-revolution/) ⭐️ 7.0/10

Analysis of ASML's four-decade rise to lithography dominance through systems engineering and strategic bets, with forward-looking discussion of emerging maskless lithography technologies.

rss · SemiWiki · Aug 14, 13:00

**Tags**: `#semiconductors`, `#lithography`, `#ASML`, `#manufacturing`, `#industry-analysis`

---

<a id="item-12"></a>
## [Intel at a Memory Crossroads: Considering a Return to Memory Chip Manufacturing](https://www.eetimes.com/intel-at-a-memory-crossroads-again/) ⭐️ 7.0/10

Intel CEO Lip-Bu Tan has hinted at a potential return to the memory chip business, citing that new memory architectures—once considered a commodity market—are now strategically interesting, particularly in the context of AI-driven demand. He also hinted at innovations involving stacking memory and CPU together. This signals a major strategic shift for Intel, which has historically been a CPU specialist and exited the memory market years ago. If Intel re-enters, it could disrupt the current oligopoly dominated by SK Hynix, Samsung, and Micron, while also addressing the AI-driven memory supply crunch that has made HBM a critical resource. Intel previously attempted returns to memory via NAND and Optane products, and also explored RDRAM technology. Meanwhile, SK Hynix is investing $720 billion to triple memory fab capacity by 2034, underscoring how fierce the competition has become in the AI memory space.

rss · EE Times · Aug 14, 13:01

**Background**: Intel was historically a player in the memory business before exiting it, leaving the DRAM market dominated by three companies: Samsung, SK Hynix, and Micron. High Bandwidth Memory (HBM) is a 3D-stacked SDRAM technology that delivers faster data access with lower energy consumption—critical for AI workloads that require massive parallel processing. The AI boom has transformed memory from a low-margin commodity into a strategic resource, with the three major suppliers concentrating capacity on high-margin HBM and server DRAM, causing supply tightness in commodity DRAM segments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/intel-ceo-hints-at-return-to-the-memory-business-says-market-is-ripe-for-innovation-hints-at-stacking-memory-and-cpu">Intel CEO hints at return to the memory business — says market is...</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://economy.ac/news/2026/08/202608289721">“Alternative Amid Memory Supply Crunch” CXMT... | The Economy</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#semiconductors`, `#memory-chips`, `#AI-infrastructure`, `#industry-strategy`

---

<a id="item-13"></a>
## [All-Solid-State Batteries (ASSBs) Advance to Pilot Production in 2026](https://www.electronicsweekly.com/news/business/solid-state-auto-batteries-2026-08/) ⭐️ 7.0/10

According to TrendForce, the Technology Readiness Levels (TRLs) of all-solid-state batteries (ASSBs) have advanced significantly in 2026, with Toyota, Honda, Nissan, and Samsung leading pilot line production efforts alongside Japanese suppliers. This milestone signals that solid-state battery technology is moving from laboratory research toward near-term commercialization, which could reshape EV safety, energy density, range, and the competitive landscape of the global automotive battery supply chain. Pilot production is an intermediate stage that bridges R&D and mass manufacturing, typically used to validate manufacturing processes, yield rates, and cost models before full-scale commercialization; ASSBs replace the flammable liquid electrolyte in conventional lithium-ion cells with a solid electrolyte (polymer, oxide, or sulphide), often paired with a lithium metal anode.

rss · Electronics Weekly · Aug 14, 05:08

**Background**: All-solid-state batteries (ASSBs) are widely seen as the next-generation successor to conventional lithium-ion cells, promising higher energy density, improved safety, and longer service life by eliminating flammable liquid electrolytes. The Technology Readiness Level (TRL) framework, originally developed by NASA in the 1970s and later adopted by agencies such as the U.S. Air Force, the European Union, and the UK, provides a systematic scale—typically 1 through 9—to evaluate how mature a technology is, from basic concept to full deployment. Pilot production generally corresponds to mid-range TRLs, sitting between laboratory validation and commercial-scale manufacturing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.crugroup.com/en/communities/thought-leadership/2025/from-smartphones-to-flying-taxis-the-coming-age-of-all-solid-state-batteries/">Unlocking a new era with all - solid - state batteries - CRU Group</a></li>
<li><a href="https://www.solidenergies.com/what-is-assb">What is ASSB</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technology_readiness_level">Technology readiness level - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#solid-state-batteries`, `#ASSB`, `#automotive`, `#EV`, `#battery-technology`

---

<a id="item-14"></a>
## [Epic Games Launcher Coming "Soon" to Linux](https://www.techpowerup.com/351601/epic-games-launcher-coming-soon-to-linux) ⭐️ 6.5/10

Epic Games is reportedly preparing to launch a native Linux version of its game launcher, signaling broader Linux gaming expansion tied to Easy Anti-Cheat support improvements.

rss · TechPowerUp News · Aug 14, 05:07

**Tags**: `#linux`, `#gaming`, `#epic-games`, `#steam-deck`, `#platform-support`

---

<a id="item-15"></a>
## [Microsoft Unifies Copilot Features Into a Super App](https://www.techpowerup.com/351589/microsoft-unifies-copilot-features-into-a-super-app) ⭐️ 6.5/10

Microsoft is consolidating its various Copilot features and integrations into a single unified 'super app,' retiring some features like Deep Research, Podcasts, and Group Chat while bringing Office 365 access under one roof.

rss · TechPowerUp News · Aug 13, 17:39

**Tags**: `#Microsoft`, `#Copilot`, `#AI`, `#product-strategy`, `#software-consolidation`

---

<a id="item-16"></a>
## [US Imposes Up to 100% Tariffs on Foreign-Made Drones, Targeting China](https://www.tomshardware.com/tech-industry/drones/us-imposes-up-to-100-percent-tariffs-on-foreign-made-drones-and-components-china-remains-primary-target-as-washington-moves-to-reduce-reliance-on-overseas-suppliers) ⭐️ 6.5/10

The Trump administration has imposed tariffs of up to 100% on foreign-made drones and their components, with China identified as the primary target. The move is justified on national security grounds and aims to reduce US dependence on overseas drone suppliers. These steep tariffs could significantly reshape the global drone industry by making Chinese-made drones and components far more expensive in the US market, potentially benefiting domestic manufacturers such as Skydio. Hardware startups, component suppliers, and commercial drone operators that rely on Chinese supply chains will face major cost disruptions and may need to rapidly redesign or reshore their products. The 100% tariff rate is exceptionally high and applies not only to complete drones but also to individual components, meaning even partially Chinese-sourced products could be affected. The policy framework resembles Section 232 national security tariffs previously used on steel and aluminum, signaling a broad trade-policy tool rather than a narrowly targeted restriction.

rss · Tom's Hardware · Aug 14, 11:53

**Background**: The US drone market has long been dominated by Chinese manufacturers, particularly DJI, which holds an estimated majority share of the global commercial drone market. US lawmakers and intelligence officials have raised concerns for years about Chinese-made drones potentially transmitting sensitive geospatial and visual data back to China. Previous administrations had already placed certain Chinese drone companies on restricted entity lists, and Congress passed the American Security Drone Act to limit federal use of Chinese drones. This new tariff action represents an escalation from entity-specific restrictions to broad economic pressure across the entire foreign drone supply chain.

**Tags**: `#drones`, `#tariffs`, `#trade-policy`, `#supply-chain`, `#china-us-relations`

---

<a id="item-17"></a>
## [Intel VP Hallock on Nova Lake and DDR4 Comeback Strategy](https://www.tomshardware.com/pc-components/cpus/intel-vp-robert-hallock-sets-nova-lake-expectations-teases-return-to-raptor-lake-for-ddr4-platforms-our-full-1-1-interview-transcript) ⭐️ 6.5/10

In a 1:1 interview with Tom's Hardware, Intel VP and GM of Enthusiast Channel Business Robert Hallock discussed expectations for the upcoming Nova Lake architecture, revealed a strategy shift toward DIY builders during the ongoing memory pricing crisis, and teased a return to Raptor Lake-based CPUs for DDR4 platforms. Hallock also credited the Raptor Lake refresh with triggering a strategic paradigm shift inside Intel. This interview offers rare forward-looking commentary from a senior Intel executive on the company's next-generation desktop CPU strategy at a time when high memory prices are dampening PC-building enthusiasm. The decision to revive Raptor Lake for DDR4 users signals Intel's pragmatism in addressing current market pain points rather than pushing all customers to costly DDR5 platforms. Nova Lake is positioned as Core Ultra Series 4 desktop and mobile processors and is expected to launch in late 2026 using a new LGA 1954 socket, with a redesigned P-core and E-core layout rather than a straightforward refresh of the prior generation. Hallock's mention of bringing Raptor Lake back specifically targets DDR4 platforms, which remain widely deployed and unaffected by the current DDR5-driven 'RAMageddon' pricing surge.

rss · Tom's Hardware · Aug 14, 11:00

**Background**: Nova Lake is Intel's next-generation desktop CPU family, succeeding Arrow Lake and expected to introduce a fresh P-core/E-core design on a new LGA 1954 socket, making it incompatible with existing LGA 1851 motherboards. 'RAMageddon' refers to the 2025-2026 memory pricing crisis driven largely by AI-related demand for HBM and DRAM, which has inflated consumer DDR5 prices and pushed some PC builders toward DDR4 alternatives. Raptor Lake, the codename for 13th-generation Intel Core processors built on the Intel 7 process, used LGA 1700 and supported both DDR4 and DDR5, which is why Intel can revive it as a lower-cost DDR4 option during the current memory squeeze.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nova_Lake_(microprocessor)">Nova Lake (microprocessor) - Wikipedia</a></li>
<li><a href="https://www.techradar.com/pro/why-is-ram-so-expensive-right-now-its-more-complicated-than-you-think">DRAM shortages, AI demand, and rising prices : what... | TechRadar</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#Nova Lake`, `#CPU`, `#DDR4`, `#hardware`

---

<a id="item-18"></a>
## [Prusa Research upgrades entire 3D printer lineup to second-generation '+' models for free](https://www.tomshardware.com/3d-printing/prusa-research-xl-core-one-and-core-one-l-all-to-receive-second-generation-upgrades-all-new-orders-get-updated-model-for-free) ⭐️ 6.5/10

Prusa Research announced that its entire 3D printer lineup, including the XL, CORE One, and CORE One L, is receiving second-generation upgrades with a new '+' designation. All new orders will automatically receive the updated '+' models at no additional cost. This is a significant move by one of the most respected names in the desktop 3D printing industry, as it ensures new buyers receive the latest hardware without paying a premium during a transition period. The consumer-friendly policy also reflects competitive pressure in the 3D printer market, where manufacturers are racing to deliver better speed, reliability, and material compatibility. The upgraded models will carry a '+' suffix to distinguish them from previous generations, following a naming convention similar to the MINI+. Specific technical improvements for each model were not detailed in the announcement, but the CORE One+'s known strengths include a high-speed CoreXY architecture and an enclosed design capable of printing engineering-grade materials like PLA, PETG, ABS, ASA, PC, and Nylon.

rss · Tom's Hardware · Aug 13, 20:35

**Background**: Prusa Research, founded by Josef Průša in the Czech Republic, is one of the leading desktop FDM (Fused Deposition Modeling) 3D printer manufacturers, known for open-source designs and reliable machines. Its product lineup as of 2025 includes the MK4S, MINI+, XL, and CORE One, with the XL being a premium multi-tool printer featuring up to 5 tool heads for multi-color and multi-material printing, while the CORE One is a high-speed enclosed CoreXY printer. The company also develops PrusaSlicer, an open-source slicing software widely used across the 3D printing community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prusa_Research">Prusa Research - Wikipedia</a></li>
<li><a href="https://www.prusa3d.com/">Original Prusa 3 D printers directly from Josef Prusa</a></li>
<li><a href="https://www.dynamism.com/brands/prusa/prusa-core-one-plus-kit.html">Prusa CORE One + Kit | Dynamism</a></li>

</ul>
</details>

**Tags**: `#3d-printing`, `#prusa-research`, `#hardware-updates`, `#consumer-electronics`, `#product-announcement`

---

<a id="item-19"></a>
## [Near-Packaged Optics Gains Ground as Hedge Against CPO's Growing Pains](https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains) ⭐️ 6.5/10

Analysts report that near-packaged optics (NPO) is gaining traction as the industry hedges against implementation challenges with co-packaged optics (CPO). NPO-based silicon photonics products are expected to ship in volume through the end of the decade. This matters because AI infrastructure and hyperscale data centers are increasingly bottlenecked by the bandwidth and power efficiency limits of traditional electrical interconnects, making the choice between NPO and CPO pivotal for next-generation networking roadmaps. The shift affects chipmakers, switch ASIC vendors, and cloud operators planning multi-year capital deployments. NPO sits architecturally between traditional pluggable optics (like QSFP modules) and fully co-packaged optics, placing the optical engine in close proximity to the switching chip without the deep co-integration that CPO demands. CPO relies heavily on silicon photonics to integrate waveguides, modulators, and detectors directly onto a silicon wafer, but faces yield, thermal, and standardization headwinds that have slowed adoption.

rss · Tom's Hardware · Aug 13, 16:52

**Background**: Data center networking has traditionally relied on pluggable optical transceivers that convert electrical signals to light and back, but as AI workloads drive terabit-scale bandwidth demands, the industry is moving toward tighter integration of optics and silicon. LPO (Linear Pluggable Optics), NPO, and CPO represent three successive stages in this evolution: LPO simplifies the pluggable module, NPO brings the optical engine nearer to the switch ASIC on the same substrate or package, and CPO integrates the optics directly into the switch chip package. Silicon photonics is the enabling technology that makes NPO and CPO feasible by allowing optical components to be fabricated using standard CMOS processes.

<details><summary>References</summary>
<ul>
<li><a href="https://resources.l-p.com/glossary/what-is-near-packaged-optics-benefits-network-upgrades">Beyond Pluggables: What is NPO ( Near - Packaged Optics ) and Why...</a></li>
<li><a href="https://dev.to/aicplight/lpo-vs-npo-vs-cpo-the-evolution-of-optical-interconnects-in-ai-data-centers-33ha">LPO vs NPO vs CPO: The Evolution of Optical ... - DEV Community</a></li>
<li><a href="https://www.fibermall.com/blog/overview-of-cpo.htm">Comprehensive Overview of CPO ( Co - Packaged Optics ) | FiberMall</a></li>

</ul>
</details>

**Tags**: `#phototonics`, `#AI-infrastructure`, `#data-center`, `#silicon-photonics`, `#hardware`

---

<a id="item-20"></a>
## [Microchip Showcases 160-Lane PCIe Gen6 Switch at FMS 2026](https://www.servethehome.com/microchip-switchtec-160-lane-pcie-gen6-switch-shown-at-fms-2026-with-xpressconnect-pcie-6-retimer/) ⭐️ 6.5/10

At FMS 2026, Microchip demonstrated a 160-lane Switchtec PCIe Gen6 switch alongside its XpressConnect PCIe 6 retimer, with Everpure also making a cameo appearance. The demonstration highlighted next-generation data center connectivity hardware for AI and high-performance computing workloads. PCIe Gen6 switches with extremely high lane counts are critical for scaling AI infrastructure, where GPUs, accelerators, and high-bandwidth memory must be interconnected with minimal latency. A 160-lane fabric switch enables dense topologies such as large GPU clusters, directly supporting the build-out of AI training and inference data centers. The Switchtec family historically delivers sub-10ns hop latency, well below the PCIe Gen5 specification's roughly 60ns reference, and the Gen6 generation is positioned for AI and HPC workloads. Retimers like XpressConnect are formally defined in the PCIe specification to extend physical link reach while preserving signal integrity at the high 64 GT/s PAM4 signaling rates that Gen6 employs.

rss · ServeTheHome · Aug 13, 18:00

**Background**: PCI Express (PCIe) is the standard high-speed serial interconnect used inside servers to link CPUs, GPUs, NVMe storage, and accelerators. Each new generation roughly doubles per-lane bandwidth: PCIe Gen5 runs at 32 GT/s and Gen6 at 64 GT/s using PAM4 signaling, meaning a x16 Gen6 link delivers about 128 GB/s per direction (256 GB/s bidirectional). At these speeds, signal integrity degrades quickly over copper traces, so retimers are needed to recondition signals and extend reach, while PCIe switches fan out connectivity to many endpoints in fabric topologies typical of modern AI clusters.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/confessions-engineer-pcie-gen-6-nyquist-trap-chandra-sekhar-mallela-073fc">Confessions of an Engineer: The PCIe Gen 6 Nyquist Trap</a></li>
<li><a href="https://thevoltpost.com/microchip-switchtec-gen-6-pcie-switches/">Switchtec Gen 6 PCIe switches from Microchip for AI Workload</a></li>
<li><a href="https://www.servethehome.com/microchip-switchtec-pcie-5-0-switches-now-sampling/">Microchip Switchtec PCIe 5.0 Switches Now... - ServeTheHome</a></li>

</ul>
</details>

**Tags**: `#PCIe Gen6`, `#Microchip`, `#data center infrastructure`, `#hardware`, `#FMS 2026`

---