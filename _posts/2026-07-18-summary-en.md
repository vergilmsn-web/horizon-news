---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 63 items, 17 important content pieces were selected

---

1. [LG Monitors Silently Install Software via Windows Update Without Consent](#item-1) ⭐️ 8.0/10
2. [New θ-TaN Metal Achieves 3× Copper's Thermal Conductivity](#item-2) ⭐️ 8.0/10
3. [TSMC A14 process advances faster than N2, attracting AI/HPC and smartphone customers](#item-3) ⭐️ 7.5/10
4. [月之暗面有望最快6个月内赴港上市](#item-4) ⭐️ 7.3/10
5. [Regressive JPEGs](#item-5) ⭐️ 7.0/10
6. [TP-Link Kasa EC71 Cameras Leaked Home GPS via Unauthenticated UDP for 6 Years](#item-6) ⭐️ 7.0/10
7. [Julia Evans Shares Lessons from Running SQLite in Production](#item-7) ⭐️ 7.0/10
8. [Kimi K3, and what we can still learn from the pelican benchmark](#item-8) ⭐️ 7.0/10
9. [ASML Plans Low-NA EUV Price Hikes, Frustrating TSMC](#item-9) ⭐️ 6.5/10
10. [国家数据局：全国已建成高质量数据集12万个](#item-10) ⭐️ 6.3/10
11. [TSMC CoWoS vs Intel EMIB: Are Customers Switching Packaging Suppliers?](#item-11) ⭐️ 6.0/10
12. [PC Vendors "Fight" for CXMT Memory Supply, Smaller OEMs Struggle](#item-12) ⭐️ 5.5/10
13. [Nvidia RTX 50 Super GPUs Ready but Delayed by High GDDR7 Prices](#item-13) ⭐️ 5.5/10
14. [Korean outfit hosting 1.44MB game development contest to honor the floppy disk — entrants must confine entire fileset, including resources, engine, and library, to miniscule storage format](#item-14) ⭐️ 5.5/10
15. [40g Autonomous Micro-Drone Uses Car Parking Sensors to Kill Mosquitoes Mid-Air](#item-15) ⭐️ 5.5/10
16. [Florida man arrested for $220K crypto theft via Steam malware](#item-16) ⭐️ 5.5/10
17. [AMD Instinct MI350P: 144GB HBM3E PCIe AI Accelerator Spotted Widely](#item-17) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [LG Monitors Silently Install Software via Windows Update Without Consent](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 8.0/10

LG monitors are silently installing LG OnScreen Control software through Windows Update with full system privileges the moment they are plugged in via HDMI, without any user prompt or consent. The software is delivered as a device metadata package that Windows automatically fetches and installs in the background, persists across reboots, and runs with unrestricted system access. This behavior represents a serious supply-chain trust failure: a hardware vendor can silently deploy full-privilege software to any Windows machine simply by having its monitor physically connected, blurring the line between driver delivery and unauthorized software installation. It affects every Windows user who buys or connects an LG display, and it highlights how Microsoft's Windows Update partner pipeline can be abused to bypass explicit user consent. Affected software includes LG's OnScreen Control, which typically handles screen splitting, monitor settings, and firmware updates and is normally installed manually via USB cable. Users can disable the behavior via Group Policy (Computer Configuration > Administrative Templates > System > Device Installation: 'Prevent automatic download of applications associated with device metadata') or, on Home editions, via sysdm.cpl > Hardware > Device Installation Settings by selecting 'No' for automatic manufacturer app downloads.

hackernews · baranul · Jul 18, 10:21 · [Discussion](https://news.ycombinator.com/item?id=48956688)

**Background**: Windows Update normally delivers operating system patches, security fixes, and hardware drivers, but Microsoft also allows third-party hardware vendors (IHVs/OEMs) to publish driver and metadata packages through its Hardware Partner dashboard, where they undergo flighting and gradual rollout via Windows telemetry. When a new display is detected, Windows can fetch associated metadata and silently install companion software from the vendor, a mechanism originally designed for convenience but one that also grants the vendor's software full system privileges with no sandboxing. LG's OnScreen Control is the specific utility being pushed this way, traditionally a USB-based optional tool but now arriving automatically over the Windows Update channel.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/develop/distributing-a-driver-package">Distributing a Driver Package - Windows drivers | Microsoft Learn</a></li>
<li><a href="https://www.lg.com/us/support/help-library/lg-monitor-onscreen-control-how-to-update-monitor-software--20154710888908">[LG Monitor OnScreen Control] How to Update Monitor Software ...</a></li>
<li><a href="https://www.fingerlakes1.com/2026/07/18/lg-monitor-software-now-installs-through-windows-update-and-many-users-did-not-expect-it/">LG Monitor Software Now Installs Through Windows Update and ...</a></li>

</ul>
</details>

**Discussion**: The community reacted with strong alarm, with users calling this behavior effectively indistinguishable from malware because the software installs with full system access, runs on every boot, and requires no user interaction. A clear workaround was shared via Group Policy and Device Installation Settings, while much of the debate centered on shifting blame from LG to Microsoft, since Windows itself is the channel performing the silent installation based on hardware metadata. Several commenters noted that Microsoft, as the gatekeeper of Windows Update, has the power and responsibility to refuse such payloads and should enforce stricter guidelines against unrelated bundled software.

**Tags**: `#security`, `#privacy`, `#windows-update`, `#lg`, `#supply-chain`, `#hardware`

---

<a id="item-2"></a>
## [New θ-TaN Metal Achieves 3× Copper's Thermal Conductivity](https://www.eetimes.com/new-material-beats-coppers-thermal-conductivity/) ⭐️ 8.0/10

Researchers have experimentally realized single-crystalline θ-phase tantalum nitride (θ-TaN), a metastable transition metal nitride that exhibits a room-temperature thermal conductivity of approximately 1100 W/m·K — nearly three times that of copper (~400 W/m·K). The breakthrough was reported in Science on January 15, 2026. If this material can be manufactured at scale and integrated into semiconductor processes, it could dramatically improve heat dissipation in chips, power electronics, and high-performance computing systems where thermal management is a key bottleneck. It has the potential to upend chip cooling layer design and enable higher power densities in future devices. θ-TaN is a metastable phase, meaning it requires specific synthesis conditions to form and may be challenging to stabilize in practical applications. The theoretical prediction for this material's ultrahigh thermal conductivity was first published in Physical Review Letters in 2021, with predicted values of ~995 and ~820 W/m·K along the a and c crystal axes respectively. Copper's thermal conductivity is fundamentally capped near 400 W/m·K by intrinsic electron-phonon scattering mechanisms that θ-TaN appears to overcome.

rss · EE Times · Jul 17, 19:00

**Background**: Thermal conductivity measures a material's ability to conduct heat, measured in watts per meter-kelvin (W/m·K). Copper, at approximately 400 W/m·K, has long been the standard for thermal management in electronics, but its conductivity is fundamentally limited by intrinsic scattering mechanisms — primarily electron-phonon interactions — that create a ceiling for all metallic conductors. Tantalum nitride (TaN) is a well-known compound used in semiconductors, particularly as a diffusion barrier in copper interconnects, and it exists in multiple crystal phases depending on synthesis conditions. The θ-phase is a specific metastable crystal structure that theoretical work had predicted would have exceptionally high thermal conductivity due to its unusual combination of electronic and phononic properties.

<details><summary>References</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/science.aeb1142">Metallic θ-phase tantalum nitride has a thermal conductivity ...</a></li>
<li><a href="https://link.aps.org/doi/10.1103/PhysRevLett.126.115901">Ultrahigh Thermal Conductivity of -Phase Tantalum Nitride ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tantalum_nitride">Tantalum nitride - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#materials-science`, `#thermal-management`, `#semiconductors`, `#chip-cooling`, `#nanotechnology`

---

<a id="item-3"></a>
## [TSMC A14 process advances faster than N2, attracting AI/HPC and smartphone customers](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers) ⭐️ 7.5/10

TSMC has confirmed that its A14 (1.4nm-class) process technology is advancing faster than the N2 (2nm) node did at a comparable stage of development, with significant improvements in both yield and performance. The company reported strong customer interest from both AI/HPC developers and smartphone chip designers planning to adopt the new node. The accelerated development of A14 signals a faster timeline for cutting-edge chip manufacturing, which could benefit AI accelerators, high-performance computing systems, and next-generation smartphones. Strong customer adoption across multiple sectors validates TSMC's leadership at the leading edge and intensifies competition with Samsung and Intel in the sub-2nm race. A14 is TSMC's first node to use 2nd Generation GAAFET (Gate-All-Around) transistor architecture, succeeding N2 which introduced the first-generation GAA nanosheet design. Compared with N2, A14 is projected to deliver up to 15% higher performance at the same power level, or up to 30% lower power consumption at the same speed, with high-volume manufacturing targeted for 2028.

rss · Tom's Hardware · Jul 17, 15:30

**Background**: TSMC's process nodes are named based on marketing designations rather than literal physical measurements — the A14 designation corresponds to a 1.4nm-class technology generation. Yield rate is a critical manufacturing metric representing the proportion of fabricated chips that meet performance and quality specifications; higher yields reduce per-chip costs and indicate process maturity. N2, TSMC's current leading-edge node entering mass production, uses first-generation GAA nanosheet transistors, while A14 will employ an improved second-generation GAAFET architecture for further power, performance, and area (PPA) gains.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A14">A14 Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/tsmc-a14-process-technology-wiki/">TSMC A14 Process Technology Wiki - Semiwiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yield_(metric)">Yield (metric) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#TSMC`, `#semiconductors`, `#process-technology`, `#A14`, `#AI-HPC`

---

<a id="item-4"></a>
## [月之暗面有望最快6个月内赴港上市](https://36kr.com/newsflashes/3900806713951873?f=rss) ⭐️ 7.3/10

Moonshot AI is restructuring for a potential Hong Kong IPO within 6 months while releasing Kimi K3, reportedly the world's largest open-source model that surpasses Claude and GPT on Code Arena.

rss · 36氪 · Jul 18, 07:45

**Tags**: `#Moonshot AI`, `#IPO`, `#Kimi K3`, `#open-source models`, `#Chinese AI`

---

<a id="item-5"></a>
## [Regressive JPEGs](https://maurycyz.com/projects/bad_jpeg/) ⭐️ 7.0/10

A creative project that creates animated GIF-like videos by manipulating JPEG coefficient ordering, causing motion to emerge as the progressive decode advances through the file.

hackernews · vitaut · Jul 18, 03:14 · [Discussion](https://news.ycombinator.com/item?id=48954851)

**Tags**: `#jpeg`, `#image-processing`, `#creative-coding`, `#steganography`, `#codec-hacks`

---

<a id="item-6"></a>
## [TP-Link Kasa EC71 Cameras Leaked Home GPS via Unauthenticated UDP for 6 Years](https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md) ⭐️ 7.0/10

Security researcher BadChemical disclosed that TP-Link Kasa EC71 indoor security cameras broadcast their configured home GPS coordinates over unauthenticated UDP traffic, a flaw that persisted in the firmware for approximately six years. The accompanying firmware update released by TP-Link reportedly bricked some devices, raising further concerns about the vendor's quality assurance. The disclosure highlights a broader pattern of consumer IoT devices leaking sensitive location telemetry over unencrypted, unauthenticated protocols, often to cloud endpoints not controlled by the manufacturer. For a widely deployed brand like TP-Link, such long-lived flaws erode consumer trust in off-the-shelf smart home security products. The leak relies on UDP, a connectionless protocol that transmits packets without authentication or encryption, meaning any device on the same LAN segment can passively listen and harvest GPS data. Community commenters note that the practical exposure is limited unless the camera is placed in a router DMZ, since it is not directly reachable from the public internet by default.

hackernews · BadChemical · Jul 17, 21:42 · [Discussion](https://news.ycombinator.com/item?id=48952565)

**Background**: The TP-Link Kasa EC71 (Kasa Spot Pan Tilt) is a 1080p indoor security camera with motion tracking, night vision, and microSD storage, sold as part of TP-Link's consumer Kasa smart home line. UDP (User Datagram Protocol) is a lightweight, connectionless transport-layer protocol commonly used for time-sensitive or low-overhead communications such as DNS, NTP, and streaming telemetry, but because it lacks authentication, any service listening on a UDP port can be queried or eavesdropped by anyone who can reach the network. Unauthenticated UDP services on IoT devices have historically been a recurring source of privacy and amplification-DDoS vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tp-link.com/us/home-networking/cloud-camera/ec71/v1/">EC71 | Kasa Spot Pan Tilt, 24/7 Recording | TP-Link</a></li>
<li><a href="https://static.tp-link.com/upload/product-overview/2024/202403/20240318/EC71+4.6_Datasheet.pdf">Kasa Spot® Pan Tilt 24/7 Recording Indoor Security Camera EC71 Motion Tracking</a></li>
<li><a href="https://www.kb.cert.org/vuls/id/417980">VU#417980 - Implementations of UDP-based application protocols are vulnerable to network loops</a></li>

</ul>
</details>

**Discussion**: Sentiment is split: several commenters see the report as emblematic of systemic IoT insecurity, with ericpauley noting that many devices ship data to cloud IPs not controlled by the vendor, while gruez argues the report appears AI-generated and that the practical risk is minimal for LAN-only setups unless DMZ is misconfigured. drnick1 reinforces the view that cheap IoT hardware should never face the public internet, and nubinetwork and BobbyTables2 express concern about the bricking firmware update and the lengthy disclosure timeline respectively.

**Tags**: `#security`, `#iot`, `#vulnerability`, `#privacy`, `#tp-link`

---

<a id="item-7"></a>
## [Julia Evans Shares Lessons from Running SQLite in Production](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) ⭐️ 7.0/10

Julia Evans published a blog post detailing practical lessons she learned from running SQLite in production, covering performance issues, backups, and operational concerns. The post attracted strong community engagement, with readers sharing tooling tips and offering technical critique of her performance assumptions. Julia Evans is a widely respected technical educator, and her explorations of SQLite in production provide valuable real-world insights for developers moving beyond toy projects and prototypes. The community discussion highlighted both actionable tooling tips and important pushback on performance assumptions at small scale, making it a useful case study in honest, experience-based writing. SQLite's `.expert` mode in the CLI can automatically recommend indexes based on analyzed queries, a useful tool for developers unfamiliar with reading query plans. A database-focused commenter (stevoski) argued that full table scans on only 10k rows should be near-instant and suspected the slow-delete issue was a classic n+1 query problem rather than a SQLite limitation.

hackernews · surprisetalk · Jul 17, 17:45 · [Discussion](https://news.ycombinator.com/item?id=48950122)

**Background**: SQLite is a self-contained, serverless, transactional SQL database engine that runs in-process, making it a natural fit for embedded applications, mobile apps, and increasingly small-to-medium web services. Julia Evans, known for her approachable 'Wizard Zines' and transparent learning style, frequently documents her learning process publicly. Running SQLite in production differs from client/server databases like PostgreSQL because there is no separate database server process, which affects backup strategies, concurrency handling, and which operational tools are applicable.

**Discussion**: The community response was engaged and mixed. Commenters shared practical add-ons such as SQLite's `.expert` mode for index recommendations and Simon Willison's `s3-credentials` tool for scoped AWS access. A database practitioner (stevoski) pushed back hard on the premise of performance problems at 10k rows, suspecting classic n+1 queries were the real culprit; others praised Julia's authentic exploratory writing as a refreshing contrast to overconfident LLM-generated content, while one commenter dismissed the article as lacking substance.

**Tags**: `#sqlite`, `#databases`, `#operations`, `#performance`, `#devops`

---

<a id="item-8"></a>
## [Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 7.0/10

Simon Willison's analysis of Kimi K3 and the limitations of the pelican benchmark, highlighting what it reveals (and misses) about modern LLMs, particularly regarding agentic tool use and hidden system prompts.

hackernews · droidjj · Jul 17, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48947717)

**Tags**: `#ai-benchmarks`, `#llm-evaluation`, `#kimi-k3`, `#simon-willison`, `#model-analysis`

---

<a id="item-9"></a>
## [ASML Plans Low-NA EUV Price Hikes, Frustrating TSMC](https://www.tomshardware.com/tech-industry/semiconductors/asmls-planned-low-na-euv-machine-price-hikes-reportedly-frustrate-tsmc-lithography-machine-maker-comes-knocking-to-make-bank-on-tsmcs-profitable-fabs-potentially-costing-the-taiwanese-chipmaker-billions) ⭐️ 6.5/10

ASML is reportedly planning to raise prices on its Low-NA EUV lithography machines, citing increased productivity of the tools as justification. The price hike could cost TSMC billions of dollars as the foundry expands its fab capacity. This matters because TSMC has made a major strategic bet on Low-NA EUV with multi-patterning for its advanced nodes (A16 and A14), rather than adopting High-NA EUV, meaning it will need even more Low-NA machines and bear the brunt of any price increases. The financial impact could ripple through the entire semiconductor supply chain, potentially affecting chip pricing and the economics of leading-edge fab construction. ASML's Low-NA EUV systems feature 0.33 numerical aperture optics, and TSMC plans to use computational lithography techniques like inverse lithography and curvilinear mask optimization to extend their usable resolution rather than upgrading to High-NA tools. Each High-NA EUV system reportedly costs significantly more than Low-NA systems, making Low-NA with multi-patterning the more cost-effective path for TSMC's near-term roadmap.

rss · Tom's Hardware · Jul 17, 15:57

**Background**: ASML是全球唯一的EUV光刻系统供应商，这些设备对于制造7nm以下的先进芯片至关重要。Low-NA EUV（数值孔径0.33）自2019年前后已投入大规模量产，而High-NA EUV（数值孔径0.55）则代表着下一代技术，能提供更好的分辨率，但成本也高得多。台积电已公开表示将在其A16（1.6nm）和A14（1.4nm）制程中跳过High-NA EUV，转而使用Low-NA配合先进的多重图形曝光和计算光刻技术。

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/asml-lithograpy-roadmap-examined-from-duv-to-hyper-na">ASML's roadmap for chipmaking lithography tools examined — from DUV to Low-NA, High-NA, Hyper-NA, and beyond | Tom's Hardware</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">EUV lithography - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#ASML`, `#TSMC`, `#EUV-lithography`, `#chip-manufacturing`

---

<a id="item-10"></a>
## [国家数据局：全国已建成高质量数据集12万个](https://36kr.com/newsflashes/3900807486293892?f=rss) ⭐️ 6.3/10

China's National Data Bureau reports 120,000 high-quality datasets totaling 1565 PB have been built, growing 60% in one quarter, with 7 data annotation pilot cities and 140,000 annotation workers supporting AI development.

rss · 36氪 · Jul 18, 08:00

**Tags**: `#China-AI`, `#data-infrastructure`, `#AI-policy`, `#national-strategy`, `#data-annotation`

---

<a id="item-11"></a>
## [TSMC CoWoS vs Intel EMIB: Are Customers Switching Packaging Suppliers?](https://semiwiki.com/semiconductor-manufacturers/tsmc/371412-tsmc-cowos-versus-intel-emib-semiconductor-packaging/) ⭐️ 6.0/10

SemiWiki reports that industry chatter at recent conferences suggests some TSMC customers are sending wafers to Intel for packaging, prompting TSMC CEO CC Wei to address the trend during a recent investor call when asked about EMIB-T. With CoWoS capacity severely constrained due to surging AI accelerator demand, any customer migration toward Intel's EMIB would signal competitive pressure on TSMC's advanced packaging monopoly and could reshape supply chain strategies for chipmakers like Nvidia and AMD. The published article is only a truncated teaser, so the actual commentary from CEO CC Wei is locked behind a paywall or read-more link; the precise technical distinction between standard EMIB and the mentioned EMIB-T variant is not disclosed in the visible text.

rss · SemiWiki · Jul 17, 15:00

**Background**: CoWoS (Chip-on-Wafer-on-Substrate) is TSMC's 2.5D advanced packaging technology that places multiple chiplets on a silicon interposer for high-bandwidth communication, and it is the backbone of Nvidia's flagship AI GPUs. EMIB (Embedded Multi-die Interconnect Bridge) is Intel's competing 2.5D approach that embeds small silicon bridges into an organic substrate instead of using a full silicon interposer, making it potentially more cost-effective. Both technologies address the same fundamental challenge: integrating multiple chiplets into a single package with high-density, low-latency interconnects to power modern AI and high-performance computing workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://logicity.in/en/blog/tsmc-cowos-can-pack-58-dies-before-panels-take-over">TSMC : CoWoS can pack 58 dies before panels take over | Logicity</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/intel-emib-embedded-multi-die-interconnect-bridge/">Intel EMIB (Embedded Multi-die Interconnect Bridge) - SemiWiki</a></li>
<li><a href="https://semiconductorx.com/packaging-emib.html">EMIB Advanced Packaging: Embedded Multi-Die Interconnect ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#advanced-packaging`, `#TSMC`, `#Intel`, `#CoWoS`

---

<a id="item-12"></a>
## [PC Vendors "Fight" for CXMT Memory Supply, Smaller OEMs Struggle](https://www.techpowerup.com/350853/pc-vendors-fight-for-cxmt-memory-supply-smaller-oems-struggle) ⭐️ 5.5/10

Major PC OEMs like Dell, HP, and Apple are securing DRAM allocations from Chinese memory maker CXMT through 2027, while smaller vendors struggle due to CXMT's limited capacity and the big three memory makers' depleted supply.

rss · TechPowerUp News · Jul 17, 17:56

**Tags**: `#DRAM`, `#supply-chain`, `#CXMT`, `#PC-hardware`, `#semiconductors`

---

<a id="item-13"></a>
## [Nvidia RTX 50 Super GPUs Ready but Delayed by High GDDR7 Prices](https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-50-super-gpus-are-reportedly-ready-but-stuck-in-limbo-due-to-excessive-gddr7-pricing-3gb-gddr7-module-costs-triple-the-price-of-2gb) ⭐️ 5.5/10

According to reports, Nvidia's RTX 50 Super GPUs are fully developed but have been held back from release due to inflated pricing on 3GB GDDR7 memory modules, which cost two to three times as much as the 2GB GDDR7 chips used on standard RTX 50-series cards. This pricing disparity is expected to push the retail prices of the Super variants well beyond Nvidia's target MSRPs. This matters because it highlights how memory supply-chain costs can directly determine whether a product reaches consumers and at what price point, potentially leaving gamers and hardware enthusiasts waiting longer for a mid-cycle GPU refresh. It also underscores the broader challenge GPU manufacturers face in managing bill-of-materials costs amid volatile DRAM pricing. The 3GB GDDR7 modules reportedly needed for the Super series command a 2–3x price premium over 2GB modules, likely because higher-density memory dies have lower manufacturing yields and are scarcer on the market. Nvidia faces a tough choice: absorb the elevated BOM cost (eroding margins) or pass it on to consumers (risking weaker demand at a time when GPU pricing is already under scrutiny).

rss · Tom's Hardware · Jul 18, 13:45

**Background**: GDDR7 is the latest generation of graphics DRAM, designed for high-bandwidth applications such as GPUs and AI accelerators, and is soldered directly onto the graphics card rather than installed as removable modules. The current RTX 50 series uses 2GB GDDR7 chips; moving to 3GB modules would allow higher total memory capacities (such as 24GB or 32GB) on a narrower memory bus, but at a higher per-chip cost. MSRP, or Manufacturer's Suggested Retail Price, is the official price Nvidia recommends, though actual 'street prices' in retail often differ due to supply constraints, demand, and retailer markups.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GDDR7_SDRAM">GDDR7 SDRAM - Wikipedia</a></li>
<li><a href="https://semiconductor.samsung.com/dram/gddr/gddr7/">GDDR7 - DRAM | Samsung Semiconductor Global</a></li>
<li><a href="https://www.cgdirector.com/gpu-msrp-list/">GPU MSRP List - AMD, Nvidia & Intel Graphics Cards</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#gpu`, `#gddr7`, `#hardware`, `#pricing`

---

<a id="item-14"></a>
## [Korean outfit hosting 1.44MB game development contest to honor the floppy disk — entrants must confine entire fileset, including resources, engine, and library, to miniscule storage format](https://www.tomshardware.com/software/korean-outfit-hosting-1-44mb-game-development-contest-to-honor-the-floppy-disk-entrants-must-confine-entire-fileset-including-resources-engine-and-library-to-miniscule-storage-format) ⭐️ 5.5/10

A Korean organization is hosting an open game development contest requiring all game files (engine, resources, libraries) to fit within a 1.44MB floppy disk size, with cash prizes for top three submissions.

rss · Tom's Hardware · Jul 18, 11:00

**Tags**: `#game-development`, `#code-optimization`, `#retro-computing`, `#contest`, `#demoscene`

---

<a id="item-15"></a>
## [40g Autonomous Micro-Drone Uses Car Parking Sensors to Kill Mosquitoes Mid-Air](https://www.tomshardware.com/tech-industry/drones/autonomous-micro-drone-achieves-first-air-to-air-insect-kill-on-the-way-towards-completely-eradicating-mosquitoes-40-gram-unit-uses-car-parking-sensors-can-eliminate-insects-at-up-to-26-feet) ⭐️ 5.5/10

A 40-gram autonomous micro-drone equipped with automotive ultrasonic parking sensors has recorded its first air-to-air mosquito kill, demonstrating the ability to detect and eliminate flying insects at distances of up to 26 feet (approximately 8 meters). The milestone is described as a step toward the goal of completely eradicating mosquitoes. Mosquitoes are major vectors for diseases such as malaria, dengue, and Zika, so autonomous aerial targeting could complement or replace traditional methods like insecticide spraying and larviciding. Repurposing inexpensive, mass-produced automotive sensors for biological pest control highlights how consumer-grade hardware can be redirected toward public health applications. The drone weighs only 40 grams and relies on the same ultrasonic proximity-detection principle used in car bumper parking aids, which measure distance to obstacles by timing ultrasonic echoes. An effective kill range of 26 feet suggests the ultrasonic sensors can reliably resolve small, fast-moving insect targets at a distance several times the drone's own wingspan, though the article provides limited detail on the kill mechanism or flight-time limitations.

rss · Tom's Hardware · Jul 18, 09:00

**Background**: Automotive parking sensors are ultrasonic proximity detectors mounted in vehicle bumpers that emit high-frequency sound pulses and measure the echo return time to estimate distances to nearby objects, typically alerting drivers to obstacles during low-speed maneuvering. Ultrasonic frequencies above 20 kHz have long been used in entomology to detect insects, including wood-boring pests, because background noise is negligible at those frequencies. Autonomous micro-drones combine miniaturized flight controllers, onboard sensors, and increasingly sophisticated perception algorithms to navigate and track targets without human piloting.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Parking_sensor">Parking sensor - Wikipedia</a></li>
<li><a href="https://www.bosch-mobility.com/en/solutions/sensors/ultrasonic-sensor/">Ultrasonic sensor - Bosch Mobility</a></li>
<li><a href="https://www.mdpi.com/2504-446X/9/6/442">UAV Autonomous Navigation System Based on Air–Ground ... - MDPI</a></li>

</ul>
</details>

**Tags**: `#drones`, `#robotics`, `#autonomous-systems`, `#public-health`, `#sensor-technology`

---

<a id="item-16"></a>
## [Florida man arrested for $220K crypto theft via Steam malware](https://www.tomshardware.com/tech-industry/cyber-security/fbi-arrests-florida-man-in-steam-malware-investigaton-after-tracing-stolen-bitcoin-to-uber-eats-gift-cards) ⭐️ 5.5/10

The FBI arrested 21-year-old Zyaire Dontaevious Zamarion Wilkins of North Lauderdale, Florida, for allegedly stealing $220,000 in cryptocurrency through malware hidden in Steam games that infected approximately 8,000 devices. Federal agents traced the stolen Bitcoin to purchases of Uber Eats gift cards, which led to the suspect's identification and arrest. This case highlights the growing threat of malware distribution through gaming platforms and the increasing sophistication of cryptocurrency-focused cybercrime. It serves as a cautionary tale for gamers and cryptocurrency holders, demonstrating how attackers exploit trusted platforms like Steam to deliver crypto-stealing payloads to a large number of victims. CryptoStealer malware typically searches infected machines for cryptocurrency wallet files, clipboard activity, and browser cookies containing financial data, then exfiltrates the information to a command-and-control server. Steam-based malware distribution often exploits the platform's Workshop and mod features, similar to the ModStealer malware discovered in September 2025 that evaded antivirus detection while targeting browser-based crypto wallets.

rss · Tom's Hardware · Jul 17, 14:43

**Background**: Steam is one of the world's largest digital game distribution platforms, operated by Valve Corporation, with hundreds of millions of active users. Its Workshop feature allows users to create and share mods, skins, and other game customizations, which can sometimes be exploited to hide malicious code. Cryptocurrency-stealing malware, known as CryptoStealers or infostealers, are a well-documented category of malware designed specifically to locate and exfiltrate digital wallet credentials, private keys, and seed phrases from compromised systems. These malware families often operate silently in the background, making detection difficult without robust endpoint security solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcrisk.com/removal-guides/14419-cryptostealer-trojan">CryptoStealer Trojan - Malware removal instructions (updated) Malwarebytes Threat Alert | Trojan.CryptoStealer.Go Undetectable crypto-stealing ModStealer malware targets ... New lightweight, self-propagating crypto stealing malware ... 5 Crypto-Stealing Malware Threats: How to Stay Safe and Aware Beware Bitcoin, Ether, Solana, XRP Wallets: This Virus Is ...</a></li>
<li><a href="https://www.malwarebytes.com/blog/detections/trojan-cryptostealer-go">Malwarebytes Threat Alert | Trojan.CryptoStealer.Go</a></li>
<li><a href="https://crypto.news/undetectable-crypto-stealing-modstealer-malware-targets-wallets-on-mac-and-windows/">Undetectable crypto-stealing ModStealer malware targets ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#cryptocurrency`, `#malware`, `#crime`, `#gaming`

---

<a id="item-17"></a>
## [AMD Instinct MI350P: 144GB HBM3E PCIe AI Accelerator Spotted Widely](https://www.servethehome.com/the-amd-instinct-mi350p-is-a-hbm-pcie-accelerator-that-has-been-all-over/) ⭐️ 5.5/10

The AMD Instinct MI350P, a PCIe-form-factor AI accelerator equipped with 144GB of HBM3E memory and 128 Compute Units, has been appearing across multiple venues and deployments in recent weeks. AMD officially positions it as a drop-in upgrade for existing enterprise AI infrastructure. The MI350P matters because it gives enterprises a PCIe-based path to large-memory AI acceleration without needing to overhaul their server racks to accommodate newer fabric topologies. Its 144GB HBM3E capacity and claimed FP16/FP8 performance roughly 40% above NVIDIA's H200 NVL position it as a competitive option in the high-end inference and training market. The card uses HBM3E, a 3D-stacked DRAM technology that delivers significantly higher bandwidth and capacity than traditional GDDR memory. The PCIe form factor, as opposed to an OAM or proprietary module, means it can slot into standard server slots, though it typically offers less bandwidth to the host CPU/GPU pool than fabric-based alternatives.

rss · ServeTheHome · Jul 17, 17:00

**Background**: AMD's Instinct line is the company's family of data-center GPUs designed to compete with NVIDIA's accelerators in AI and HPC workloads. HBM (High Bandwidth Memory) is a 3D-stacked DRAM technology originally co-developed by Samsung, AMD, and SK Hynix, widely used in modern AI accelerators because large language models demand both high memory capacity and high memory bandwidth. The MI350 series represents AMD's latest generation using HBM3E, and the 'P' suffix denotes the PCIe card variant, distinguishing it from other form factors in the lineup.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/amd-announces-mi350p-pcie-ai-accelerator-card-with-144gb-of-hbm3e-roughly-40-percent-faster-in-fp16-and-fp8-theoretical-compute-compared-to-nvidias-h200-nvl-competitor">AMD announces MI350P PCIe AI accelerator card with 144GB of ...</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi350p.html">AMD Instinct™ MI350P PCIe® Cards</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#AI Accelerator`, `#GPU`, `#HBM3E`, `#Hardware`

---