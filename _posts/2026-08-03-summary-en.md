---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
---

> From 47 items, 10 important content pieces were selected

---

1. [Iran Suspected of Cyberattacks on US Water Utilities Across 45 Municipalities](#item-1) ⭐️ 7.5/10
2. [Dasharo v0.9.0 brings first open-source firmware to AMD AM5 platform](#item-2) ⭐️ 7.5/10
3. [Chinese invasive BCI startup Zhidong Tech sets record with 330M RMB angel round](#item-3) ⭐️ 7.3/10
4. [Karpathy’s Pelican](#item-4) ⭐️ 7.0/10
5. [AMD's upcoming Zen 6 processors could fix microstutters and improve 1% lows in games — Next-gen CPUs tipped to feature per-core optimizations for thermal and power budgets](#item-5) ⭐️ 6.5/10
6. [“幺正量子”完成数亿元A轮融资](#item-6) ⭐️ 6.3/10
7. [Kioxia to Mass-Produce Next-Gen AI NAND Supporting PCIe 6.0 and UFS 5.0 in 2025](#item-7) ⭐️ 6.3/10
8. [Kakehashi: Experimental macOS Binary Compatibility Layer for Linux ARM](#item-8) ⭐️ 6.0/10
9. [F*: A Proof-Oriented Programming Language for Formal Verification](#item-9) ⭐️ 6.0/10
10. [ASUS Showcases NUC 16 Mini-PC Family Powered by Intel Panther Lake](#item-10) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Iran Suspected of Cyberattacks on US Water Utilities Across 45 Municipalities](https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control) ⭐️ 7.5/10

Iran is suspected of conducting cyberattacks against US water utilities in 45 municipalities, with small towns being the primary targets. While water systems remain operational, several utilities have resorted to manual control to safeguard their water supply. This incident highlights the vulnerability of America's critical water infrastructure to nation-state cyber threats, particularly small utilities that often lack robust cybersecurity defenses. A successful attack on water systems could disrupt essential public services, potentially affecting millions of citizens and undermining public trust in critical infrastructure security. The attacks are linked to the Iranian threat group CyberAv3ngers, which is widely associated with Iran's Islamic Revolutionary Guard Corps Cyber-Electronic Command (IRGC-CEC) and has been targeting Unitronics Vision series PLCs with integrated HMIs. Affected utilities have switched to manual operations rather than risking remote control of compromised industrial systems.

rss · Tom's Hardware · Aug 2, 13:10

**Background**: Water and wastewater utilities rely on SCADA (Supervisory Control and Data Acquisition) systems to monitor and control operations across large geographic areas, often using remote terminal units (RTUs) and programmable logic controllers (PLCs). CyberAv3ngers is an Iranian state-directed hacker group, first identified around 2020, that has emerged as one of the most active threat actors targeting industrial control systems worldwide. Previous attacks by this group have exploited Israeli-made Unitronics PLCs, which are commonly used in US water and wastewater facilities, making them a known weak point in critical infrastructure defenses.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/cyberav3ngers-iran-hacking-water-and-gas-industrial-systems/">CyberAv3ngers: The Iranian Saboteurs Hacking Water and Gas Systems Worldwide | WIRED</a></li>
<li><a href="https://www.tenable.com/blog/what-to-know-about-cyberav3ngers-the-irgc-linked-group-targeting-critical-infrastructure">CyberAv3ngers: FAQ About Iran-Linked Threat Group Targeting U.S. Critical Infrastructure | Tenable®</a></li>
<li><a href="https://www.securityweek.com/ics-at-multiple-us-water-facilities-targeted-by-hackers-affiliated-with-iranian-government/">ICS at Multiple US Water Facilities Targeted by Hackers Affiliated...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#critical-infrastructure`, `#cyberattack`, `#iran`, `#water-utilities`

---

<a id="item-2"></a>
## [Dasharo v0.9.0 brings first open-source firmware to AMD AM5 platform](https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850) ⭐️ 7.5/10

3mdeb officially released Dasharo v0.9.0, the first open-source firmware for AMD's AM5 platform, combining Coreboot and AMD's openSIL to provide initial support for Zen 4 Phoenix APUs on MSI's Pro B850-P WiFi motherboard. This milestone opens the AM5 platform to security researchers, enthusiasts, and the right-to-repair community by providing auditable, transparent firmware, breaking AMD's long-standing closed-firmware stance on its desktop platform. It also serves as the first real-world validation that AMD's openSIL initiative can deliver fully open silicon initialization in a consumer-facing product. The release is numbered v0.9.0, indicating it is still maturing and not yet production-ready, and support is currently limited to a single board (MSI Pro B850-P WiFi) paired with Zen 4 Phoenix APUs. Dasharo is itself a Coreboot downstream maintained by 3mdeb, and 3mdeb offers a commercial Dasharo Pro Package subscription tier with additional features on top of the open releases.

rss · Tom's Hardware · Aug 2, 12:10

**Background**: Coreboot (formerly LinuxBIOS) is a long-standing open-source project that replaces proprietary BIOS/UEFI firmware by performing minimal hardware initialization before handing control to an operating system. AMD openSIL is a set of three statically linkable C libraries — xSIM (x86 Silicon Initialization Library), xPRF (x86 Platform Reference Library) and xUSL (x86 Utilities & Services Library) — that handle x86 host silicon initialization and can be integrated into any x86 host firmware. Dasharo is 3mdeb's branded Coreboot downstream, emphasizing open development, firmware resilience, and platform security transparency. AMD's AM5 socket is the company's current desktop platform launched with the Ryzen 7000 series, and prior to this release no open-source UEFI firmware had been available for it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850">First open-source firmware for AM5 officially launches — Dasharo v0.9.0 brings Coreboot and openSIL to Zen 4 APUs on MSI B850 | Tom's Hardware</a></li>
<li><a href="https://docs.dasharo.com/osf-trivia-list/dasharo/">Frequenty Asked Questions about Dasharo</a></li>
<li><a href="https://www.amd.com/en/blogs/2023/empowering-the-industry-with-open-system-firmware-.html">Empowering The Industry with Open System Firmware – AMD openSIL</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#coreboot`, `#openSIL`, `#AMD-AM5`, `#firmware`

---

<a id="item-3"></a>
## [Chinese invasive BCI startup Zhidong Tech sets record with 330M RMB angel round](https://36kr.com/newsflashes/3923172519374216?f=rss) ⭐️ 7.3/10

On August 3, Chinese brain-computer interface company 主动科技 (Zhidong Technology) announced the closing of a 330 million RMB (~$46M) angel round, the largest angel-stage financing ever recorded in China's BCI sector. The round was led by 中科创星 (CAS Star), with participation from Lenovo Star, Jiuyhe Venture Capital, Daotong Investment, Inno Angel Fund, BGI Pine Life Sciences Fund, Jifeng Capital, and Jiadao Capital. This is one of the largest early-stage bets on invasive BCI technology in China, signaling strong investor validation of the domestic neural implant ecosystem at a moment when the field is being reshaped globally by players like Neuralink. The capital will directly accelerate clinical translation—the key bottleneck where China still trails the US in approved devices and human implant data—potentially positioning domestic firms to compete in the next wave of medical BCI applications. The 330M RMB will be deployed across four priorities: facility expansion, equipment buildout, advancing clinical trials, and team hiring—all oriented toward industrialization of invasive BCI products. The investor mix is unusually broad, combining state-affiliated science funds (中科创星, 华大松禾生科), a corporate strategic arm (联想之星), and healthcare-focused funds, which together suggest coordinated cross-sector backing rather than a single thesis-driven bet.

rss · 36氪 · Aug 3, 02:17

**Background**: Brain-computer interfaces (BCIs) are systems that record or modulate neural activity to enable direct communication between the brain and external devices. Invasive BCIs place electrodes directly in or on brain tissue through surgery, yielding much higher signal fidelity than non-invasive approaches but requiring complex neurosurgical procedures and raising long-term biocompatibility challenges. Clinical translation of BCI technology typically spans years, requiring multidisciplinary collaboration across neurosurgery, neurology, rehabilitation medicine, and biomedical engineering, and depends on regulatory pathways such as China's NMPA or the US FDA—China's BCI ecosystem has been building rapidly but still lags in approved implantable devices and human-trial data relative to the United States.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12671281/">Invasive Brain-Computer Interfaces: A Critical Assessment of Current Developments and Future Prospects - PMC</a></li>
<li><a href="https://arxiv.org/pdf/2607.07185">Clinical Translation of Brain-Computer Interface in China: A Landscape</a></li>

</ul>
</details>

**Tags**: `#brain-computer-interface`, `#funding`, `#China-tech`, `#medtech`, `#neural-implant`

---

<a id="item-4"></a>
## [Karpathy’s Pelican](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Karpathy's Pelican SVG challenge emerges as a notable AI benchmark for testing models' physical world understanding through vector graphics code generation.

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Tags**: `#AI`, `#LLM benchmarks`, `#SVG generation`, `#world models`, `#Karpathy`

---

<a id="item-5"></a>
## [AMD's upcoming Zen 6 processors could fix microstutters and improve 1% lows in games — Next-gen CPUs tipped to feature per-core optimizations for thermal and power budgets](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets) ⭐️ 6.5/10

Leaked details suggest AMD's Zen 6 processors will feature per-core thermal and power optimizations that could reduce microstutters and improve 1% lows in gaming.

rss · Tom's Hardware · Aug 2, 12:30

**Tags**: `#AMD`, `#Zen 6`, `#CPU architecture`, `#gaming performance`, `#hardware leak`

---

<a id="item-6"></a>
## [“幺正量子”完成数亿元A轮融资](https://36kr.com/newsflashes/3923156103818628?f=rss) ⭐️ 6.3/10

Chinese quantum computing startup 幺正量子 (Unitary Quantum) completed a Series A funding round worth hundreds of millions of yuan, led by Shenzhen Capital with multiple institutional co-investors, to accelerate QCCD trapped-ion quantum computing R&D targeting quantum supremacy and error correction.

rss · 36氪 · Aug 3, 02:00

**Tags**: `#quantum-computing`, `#funding`, `#QCCD`, `#trapped-ion`, `#china-tech`

---

<a id="item-7"></a>
## [Kioxia to Mass-Produce Next-Gen AI NAND Supporting PCIe 6.0 and UFS 5.0 in 2025](https://36kr.com/newsflashes/3923128725646979?f=rss) ⭐️ 6.3/10

Japanese NAND flash manufacturer Kioxia announced plans to mass-produce its next-generation AI-oriented NAND flash products this year, featuring support for the cutting-edge PCIe 6.0 interface and UFS 5.0 standard. These products are specifically designed to meet the growing storage demands driven by artificial intelligence workloads. As a major global NAND flash producer, Kioxia's move signals the industry's transition to next-generation interface standards, which are essential for handling the massive data throughput required by AI training and inference workloads. The adoption of PCIe 6.0 and UFS 5.0 will enable significantly faster data transfer rates, benefiting data centers, edge AI devices, and smartphones alike. PCIe 6.0 doubles the transmission speed of PCIe 5.0 from 32 GT/s to 64 GT/s by using a new modulation method, primarily targeting AI and machine learning applications in data center interconnect (DCI) scenarios. UFS 5.0 represents the next generation of mobile flash storage, succeeding UFS 4.0 which already achieved read speeds of 4,200 MB/s and write speeds of 2,800 MB/s.

rss · 36氪 · Aug 3, 01:32

**Background**: NAND flash is a type of non-volatile storage technology used in SSDs, smartphones, and other devices. PCIe (Peripheral Component Interconnect Express) is a high-speed interface standard for connecting components like SSDs to processors, with each new generation roughly doubling bandwidth. UFS (Universal Flash Storage) is the standard for flash storage in mobile devices, maintained by JEDEC. The rapid growth of AI has created unprecedented demand for high-bandwidth, low-latency storage, driving the industry to accelerate the adoption of next-gen standards like PCIe 6.0 and UFS 5.0.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/12VHPWR">12VHPWR - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_Flash_Storage">Universal Flash Storage - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#NAND flash`, `#PCIe 6.0`, `#UFS 5.0`, `#AI hardware`, `#storage technology`

---

<a id="item-8"></a>
## [Kakehashi: Experimental macOS Binary Compatibility Layer for Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 6.0/10

Developer vlad_kalinkin released Kakehashi, an experimental userspace compatibility layer that runs macOS command-line binaries natively on Linux ARM machines, with working prototypes for 7-Zip, curl, and Git. This project explores a niche that established tools like Darling have not addressed—ARM support—potentially benefiting Linux ARM users (such as Apple Silicon Mac owners running Asahi Linux) who want to run macOS-specific CLI tools without emulation overhead. 7-Zip currently runs roughly 5.2x slower than native Linux but the developer has mapped out an optimization plan; curl passes over 200 automated commands in a Docker test script; and the project is conceptually similar to Wine but targets the Mach-O executable format and Apple's frameworks instead of Windows PE binaries.

hackernews · vlad_kalinkin · Aug 2, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49145937)

**Background**: A userspace compatibility layer translates API and system calls from one operating system to another so that binaries compiled for one platform can run on another. Wine is the most famous example, letting Windows PE binaries run on Linux without full CPU-level emulation. macOS uses the Mach-O executable format and depends on Apple-specific frameworks and dynamic libraries (such as those in /usr/lib/system), which differ structurally from Linux's ELF format and glibc. Darling is an existing open-source project that re-implements enough of macOS's userspace on Linux to run macOS binaries, but it has historically targeted x86_64 and lacks ARM support.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CrossOver_(software)">CrossOver (software) - Wikipedia</a></li>
<li><a href="https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/MachOOverview.html">Overview of the Mach - O Executable Format</a></li>
<li><a href="https://inventivehq.com/blog/executable-file-formats-guide">Understanding PE, ELF, and Mach - O : Executable File Format Deep...</a></li>

</ul>
</details>

**Discussion**: Commenters drew parallels to Wine, Proton, and Darling, with one user suggesting Kakehashi collaborate with Darling's open ARM64 support PR. Others praised the project's ambition while criticizing the name 'Kakehashi' and noting it is still early-stage. A technical commenter (derefr) raised whether a decompilation-style approach—requiring the original binary as input rather than shipping rewritten libraries—could make a project like this more tractable.

**Tags**: `#macOS`, `#Linux ARM`, `#compatibility-layer`, `#userspace`, `#open-source`

---

<a id="item-9"></a>
## [F*: A Proof-Oriented Programming Language for Formal Verification](https://fstar-lang.org/) ⭐️ 6.0/10

The discussion revisits F*, a general-purpose proof-oriented functional programming language developed primarily at Microsoft Research, highlighting its ability to express proofs of program correctness alongside executable code and its support for incrementally migrating existing C codebases to F*. F* represents a growing paradigm of proof-oriented programming, where formal verification is integrated into the development process rather than being an afterthought, making it relevant for high-assurance systems where correctness is critical. F* integrates mathematical proof techniques into the development workflow, allowing developers to write programs together with mostly-automated correctness proofs. Its connection to dependent types and effectful programming makes it particularly suitable for verifying low-level systems code and interfacing with existing C libraries.

hackernews · ducktective · Aug 2, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49143925)

**Background**: Proof-oriented programming languages integrate executable code, formal specifications, and correctness proofs into a unified development process. Unlike traditional languages that rely on testing and debugging to ensure correctness, these languages allow developers to mathematically prove that their programs satisfy specified properties. F* falls within this category and was developed at Microsoft Research, with related work including the Steel language for concurrent separation logic proofs. The ability to incrementally verify and migrate C code makes F* particularly useful for bringing formal verification into existing industrial codebases.

<details><summary>References</summary>
<ul>
<li><a href="https://fstar-lang.org/">F *: A Proof - Oriented Programming Language</a></li>
<li><a href="https://medium.com/@SakshifromKushoAI/f-a-general-purpose-proof-oriented-programming-language-2a0cf9f71915">F * : A general-purpose proof - oriented programming language</a></li>
<li><a href="https://spencerfarley.com/2022/07/22/proof-oriented-programming/">Proof - Oriented Programming | 5min Dev Essentials</a></li>

</ul>
</details>

**Discussion**: Community sentiment was mixed and largely critical of the F* website's presentation rather than the language itself. One commenter expressed frustration at the lack of syntax examples on the homepage, wanting to see what the syntax looks like and why the language should be used. Another commenter praised F*'s ability to incrementally migrate existing C codebases while calling external libraries. Additional comments asked whether F* has real-world industry adoption and noted the irony of the website itself lacking responsive design despite discussing formal verification.

**Tags**: `#programming-languages`, `#formal-verification`, `#functional-programming`, `#proof-assistants`, `#type-systems`

---

<a id="item-10"></a>
## [ASUS Showcases NUC 16 Mini-PC Family Powered by Intel Panther Lake](https://www.servethehome.com/asus-showcases-nuc-16-family-powered-by-intel-panther-lake/) ⭐️ 5.5/10

At Computex, ASUS unveiled its NUC 16 family of mini-PCs powered by Intel's upcoming Panther Lake and Wildcat Lake SoCs, packing a full system into a compact 0.7-liter chassis. The lineup will be offered in multiple configurations, including a fully equipped mini-PC and a barebones kit without memory, storage, or operating system. This marks one of the first commercial appearances of Intel's Panther Lake platform in a mini-PC form factor, offering a glimpse into the next generation of compact AI-capable computing. It signals continued competition in the small-form-factor desktop space where ASUS, having inherited Intel's NUC business, maintains a strong presence. Panther Lake is built on Intel's 18A process node and features an NPU delivering up to 50 TOPS of AI performance, while Wildcat Lake targets more budget-oriented devices such as entry-level laptops. The 0.7L chassis demonstrates how Intel's chiplet-based architecture enables compact integration without sacrificing capability.

rss · ServeTheHome · Aug 2, 17:00

**Background**: ASUS took over Intel's NUC (Next Unit of Computing) mini-PC business in 2023, inheriting a product line that pioneered the ultra-compact desktop category. Intel's Panther Lake is the company's next major client SoC generation, following Meteor Lake, Lunar Lake, and Arrow Lake, built using a tile-based chiplet design and manufactured on the Intel 18A process. Wildcat Lake is a lower-tier sibling targeting affordable laptops and small form factors. The 0.7-liter chassis size positions the NUC 16 among the smallest commercially available x86-based systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/asus-showcases-nuc-16-family-powered-by-intel-panther-lake/">ASUS Showcases NUC 16 Family Powered By... - ServeTheHome</a></li>
<li><a href="https://www.linkedin.com/posts/thezit_aicomputing-intel18a-edgeperformance-activity-7382090653918224385-PWlv">Intel 's Panther Lake chip specs revealed: 50 TOPS NPU... | LinkedIn</a></li>
<li><a href="https://logicity.in/en/blog/dell-xps-13-vs-macbook-neo-699-wildcat-lake-takes-on-apple">Dell XPS 13 vs MacBook Neo: $699 Wildcat Lake Takes on... | Logicity</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#intel`, `#panther-lake`, `#nuc`, `#computex`

---