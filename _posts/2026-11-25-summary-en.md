---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 118 items, 20 important content pieces were selected

---

1. [The matrix multiplication exponent is nine fourths (pdf)](#item-1) ⭐️ 10.0/10
2. [1Password Security Incident](#item-2) ⭐️ 9.0/10
3. [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](#item-3) ⭐️ 9.0/10
4. [Google releases Cogentic papers on integer factorization, discrete logs and more](#item-4) ⭐️ 9.0/10
5. [Lean Formal Verification Audits and Uncovers Bugs in Clojure Core](#item-5) ⭐️ 8.0/10
6. [Netherlands May Defy US MATCH Act Amid China Diplomacy](#item-6) ⭐️ 8.0/10
7. [Seoul Semiconductor launches mass production of WICOP Pixel LCD backlight](#item-7) ⭐️ 7.5/10
8. [AMD Introduces RT-MLAS for Optimizing Large-Scale Ray Traced World Performance](#item-8) ⭐️ 7.5/10
9. [Intel Core Ultra 4000 "Nova Lake-S" Preliminary Specs Leaked](#item-9) ⭐️ 7.5/10
10. [Windows Loudness Equalization, reverse-engineered and ported to PipeWire](#item-10) ⭐️ 7.0/10
11. [Cuts to Chinese CSP Demand Weigh on Price Outlook, Slowing Memory Industry Revenue Growth in 2027, Says TrendForce](#item-11) ⭐️ 7.0/10
12. [Lawsuit alleges Trump strong-armed Intel](#item-12) ⭐️ 6.5/10
13. [Frontier Supercomputer Maintenance and Claude's Bioinformatics Performance](#item-13) ⭐️ 6.3/10
14. [Keysight ADS certified for Tower Semiconductor PH18 silicon photonics process](#item-14) ⭐️ 6.0/10
15. [Siemens Extends Eigen AI Agent to Process Industries via SIMATIC PCS 7](#item-15) ⭐️ 6.0/10
16. [Vishay Launches LoRa-based M2M Module for Industrial Sensors](#item-16) ⭐️ 6.0/10
17. [dToF sensor with ranging capability beyond 8m](#item-17) ⭐️ 6.0/10
18. [(PR) Kioxia to Showcase XL-FLASH Generation 3 Technology, the Next-Generation Low-Latency, High-Performance Flash Memory for AI](#item-18) ⭐️ 5.5/10
19. [7 new Intel Nova Lake-S Core Ultra 4000-series CPUs detailed in new leak](#item-19) ⭐️ 5.5/10
20. [New CPU benchmark tool promises 40 years of compatibility, with support as far back as i386, Windows 95](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [The matrix multiplication exponent is nine fourths (pdf)](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 10.0/10

A new OpenAI paper proves the matrix multiplication exponent is 9/4, refuting a major conjecture and resolving several top-tier open problems in mathematics and computer science.

hackernews · E-Reverance · Nov 25, 01:19 · [Discussion](https://news.ycombinator.com/item?id=50637220)

**Tags**: `#math`, `#algorithms`, `#complexity-theory`, `#openai`, `#research`

---

<a id="item-2"></a>
## [1Password Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 9.0/10

1Password discloses a security incident where malicious code was pushed to backend services, prompting a high-level analysis from the community regarding the effectiveness of their security measures and the risks of insider threats in SaaS environments.

hackernews · lxhrstn · Nov 25, 17:18 · [Discussion](https://news.ycombinator.com/item?id=50644817)

**Tags**: `#Security`, `#1Password`, `#SaaS`, `#Supply Chain Attack`, `#Incident Response`

---

<a id="item-3"></a>
## [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) ⭐️ 9.0/10

Scott Aaronson expresses excitement about recent advances in AI solving hard math problems, sparking community debate on whether this marks the beginning of an AI singularity contained to verifiable tasks.

hackernews · Kotlopou · Nov 25, 19:11 · [Discussion](https://news.ycombinator.com/item?id=50646108)

**Tags**: `#AI`, `#Mathematics`, `#LLM`, `#Automated Theorem Proving`, `#Scott Aaronson`

---

<a id="item-4"></a>
## [Google releases Cogentic papers on integer factorization, discrete logs and more](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 9.0/10

Google has released research papers on 'cogentic' methods for solving complex mathematical problems such as integer factorization and discrete logs, sparking significant community discussion about the impact on mathematics and computer science.

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**Tags**: `#AI`, `#Cryptography`, `#Mathematics`, `#Google Research`, `#Breakthrough`

---

<a id="item-5"></a>
## [Lean Formal Verification Audits and Uncovers Bugs in Clojure Core](https://s.conao3.com/blog/2026/e4f733) ⭐️ 8.0/10

A researcher used Lean to formally verify Clojure's core library, uncovering several unreported bugs in the process. This audit demonstrates the practical utility of dependent type theory in discovering hidden flaws in real-world, mainstream production code, elevating formal verification from abstract theory to industrial application. A community member noted that some of the identified issues, such as type coercion in `(get "abc" 1.9)` and byte array index handling, are actually expected language behaviors rather than fundamental bugs, highlighting a nuance in how Lean interacts with Clojure's dynamic type system.

hackernews · encyclopedism · Nov 25, 14:56 · [Discussion](https://news.ycombinator.com/item?id=50642939)

**Background**: Clojure is a modern, functional programming language that runs on the Java Virtual Machine (JVM). Lean is a dependently typed programming language and proof assistant used for formalizing mathematics and verifying program correctness. In Lean's type system, dependent types allow the specification of complex invariants that standard type systems cannot express, making it a powerful tool for rigorous code auditing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted nuances in the reported findings, such as type coercion in strings versus byte arrays, and shared links to similar audits of Common Lisp implementations. Additionally, the community discussed the growing trend of using Lean over Rocq (formerly Coq) for automated theorem proving tasks.

**Tags**: `#Formal Verification`, `#Lean`, `#Clojure`, `#Programming Languages`, `#Bugs`

---

<a id="item-6"></a>
## [Netherlands May Defy US MATCH Act Amid China Diplomacy](https://www.electronicsweekly.com/news/business/dutch-may-resist-us-match-act-2026-11/) ⭐️ 8.0/10

The Netherlands may choose to resist the implementation of the US MATCH Act, a decision that could be swayed by Dutch Foreign Minister Tom Berendsen's recent diplomatic visit to China. This geopolitical friction between The Hague and Washington threatens the global semiconductor supply chain and tests the limits of US export control enforcement on its European allies. The bipartisan MATCH Act targets the export of semiconductor manufacturing equipment, which would directly affect the operations of Dutch company ASML and increase US-China tensions.

rss · Electronics Weekly · Nov 25, 06:10

**Background**: The US MATCH Act (Multilateral Alignment of Technology Controls on Hardware) was introduced by Senators Risch, Ricketts, and Kim to impose stricter export restrictions on semiconductor manufacturing equipment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.govinfo.gov/app/details/BILLS-119hr8170ih">H.R. 8170 (IH) - Multilateral Alignment of Technology ...</a></li>
<li><a href="https://www.govinfo.gov/app/details/BILLS-119s4281is">S. 4281 (IS) - Multilateral Alignment of Technology Controls ...</a></li>
<li><a href="https://www.foreign.senate.gov/press/rep/release/risch-ricketts-kim-introduce-match-act-level-the-global-playing-field-for-us-tech">[2026-04-08] Risch, Ricketts, Kim Introduce MATCH Act; Level ...</a></li>

</ul>
</details>

**Tags**: `#Geopolitics`, `#Export Controls`, `#Semiconductors`, `#Supply Chain`, `#Netherlands`

---

<a id="item-7"></a>
## [Seoul Semiconductor launches mass production of WICOP Pixel LCD backlight](https://www.techpowerup.com/355205/seoul-semiconductor-enables-beyond-oled-picture-quality-with-lcd) ⭐️ 7.5/10

Seoul Semiconductor has announced the full-scale mass production of WICOP Pixel, a package-free RGB backlight technology for LCDs that achieves 100% DCI-P3 color gamut and over three times the brightness of OLED displays. The company plans to convert existing white backlight capacity to produce these ultra-fine pitch RGB chips and expand supply to global TV manufacturers. This development offers a cost-effective alternative to OLEDs for high-end displays, enabling LCDs to rival or exceed OLEDs in brightness while maintaining superior color accuracy for professional and film-industry applications. It represents a significant shift in the display industry, potentially revitalizing LCD technology through advanced backlighting rather than replacing it with OLED panels. The WICOP Pixel technology, developed by subsidiary Seoul Viosys, uses wireless, lens-free, and package-free RGB micro-LEDs stacked vertically at ultra-fine pitches of several tens of micrometers. Seoul Semiconductor plans to generate additional revenue through a global patent licensing program and invest those royalties into R&D for biotechnology, 3D printing, and AI data communications.

rss · TechPowerUp News · Nov 25, 14:51

**Background**: DCI-P3 is a color gamut standard widely used in the film industry, offering a broader range of colors than the standard sRGB used in most web content. While OLED displays are known for deep blacks and high contrast, they are typically limited in peak brightness compared to new backlight technologies. Mini-LED and Micro-LED backlights are emerging as ways to upgrade LCD panels to compete with OLEDs by improving color volume and dynamic range.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androidauthority.com/color-gamuts-guide-3035782/">Color gamuts explained: sRGB, DCI - P 3 , Rec 2020 - Android Authority</a></li>
<li><a href="http://www.qianlin-led.com/4857">Seoul Viosys – Single-Chip Micro-LED Display Technology – GAINER...</a></li>
<li><a href="https://www.seoulsemicon.com/en/media/newsroom/175">Seoul Semiconductor and Seoul Viosys Introduce Four ...</a></li>

</ul>
</details>

**Tags**: `#Display Technology`, `#Semiconductors`, `#LCD`, `#Optoelectronics`, `#Hardware`

---

<a id="item-8"></a>
## [AMD Introduces RT-MLAS for Optimizing Large-Scale Ray Traced World Performance](https://www.techpowerup.com/355194/amd-wants-to-ray-trace-large-dynamic-worlds-with-reusable-parts) ⭐️ 7.5/10

AMD introduced Ray Tracing Multi-Level Acceleration Structures (RT-MLAS), a new approach that adds up to two Mid-Level Acceleration Structures (MDLAS) within a hierarchy to improve memory efficiency and build times. This extension has been formally included in Vulkan via the VK_AMDX_multi_level_acceleration_structure proposal, enabling reusable geometries in large environments. RT-MLAS addresses a critical bottleneck in modern game development where traditional two-level ray tracing becomes increasingly expensive to rebuild and update as open-world environments grow in scale and complexity. This technology is particularly significant for developers creating heavily animated scenes, such as vast forests or sprawling cities, as it allows independent sections of a world to be updated without rebuilding the entire hierarchy. The technology allows developers to organize repeated scene components, such as building parts (walls, windows, roofs), into shared MDLAS rather than registering each individually in a massive Top-Level Acceleration Structure. By isolating different areas of a scene into independently manageable structures, developers can rebuild only the specific sections that need updating when objects move or change level of detail.

rss · TechPowerUp News · Nov 25, 13:52

**Background**: In modern hardware ray tracing, developers typically use a two-level hierarchy consisting of Bottom-Level Acceleration Structures (BLAS) that contain individual geometry, and a Top-Level Acceleration Structure (TLAS) that manages the instances of that geometry in a scene. As open worlds grow to contain thousands or millions of moving objects, the TLAS becomes a massive computational resource that must be constantly rebuilt every frame. AMD's RT-MLAS introduces Mid-Level Acceleration Structures to act as reusable, intermediate layers that group related objects, making large-scale updates more manageable.

<details><summary>References</summary>
<ul>
<li><a href="https://gpuopen.com/learn/amd-rt-mlas-vulkan/">Ray tracing large, dynamic worlds with RT - MLAS - AMD GPUOpen</a></li>
<li><a href="https://www.phoronix.com/news/Vulkan-AMDX-Ray-Tracing-Struct">Vulkan 1.4.369 Introduces New AMD Extension For... - Phoronix</a></li>
<li><a href="https://docs.vulkan.org/features/latest/features/proposals/VK_AMDX_multi_level_acceleration_structure.html">VK_AMDX_multi_level_acceleration_structure - docs.vulkan.org</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Ray Tracing`, `#Graphics`, `#Game Development`, `#Hardware`

---

<a id="item-9"></a>
## [Intel Core Ultra 4000 "Nova Lake-S" Preliminary Specs Leaked](https://www.techpowerup.com/355195/intel-core-ultra-4000-nova-lake-s-preliminary-specs-leaked) ⭐️ 7.5/10

Leaked documentation reveals preliminary specs for the upcoming Intel Core Ultra 4000 'Nova Lake-S' desktop CPU lineup, including a flagship chip with 28 cores and 5.5 GHz boost clocks.

rss · TechPowerUp News · Nov 25, 12:36

**Tags**: `#Intel`, `#CPU`, `#Hardware`, `#Leak`, `#Nova Lake`

---

<a id="item-10"></a>
## [Windows Loudness Equalization, reverse-engineered and ported to PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

A GitHub project that reverse-engineers Windows' Loudness Equalization and ports it to PipeWire, sparking technical debate about audio processing algorithms and the ethics of reverse engineering.

hackernews · ThrowNotAway · Nov 25, 11:34 · [Discussion](https://news.ycombinator.com/item?id=50641171)

**Tags**: `#audio-engineering`, `#linux`, `#pipewire`, `#reverse-engineering`, `#windows`

---

<a id="item-11"></a>
## [Cuts to Chinese CSP Demand Weigh on Price Outlook, Slowing Memory Industry Revenue Growth in 2027, Says TrendForce](https://www.dramexchange.com/WeeklyResearch/Post/2/12900.html) ⭐️ 7.0/10

TrendForce reports that reduced memory orders from Chinese CSPs are slowing projected revenue growth in the memory industry for 2027 and pressuring pricing outlooks.

rss · DRAMeXchange (TrendForce) · Nov 25, 16:24

**Tags**: `#Memory Industry`, `#Supply Chain`, `#China`, `#CSP`, `#Market Analysis`

---

<a id="item-12"></a>
## [Lawsuit alleges Trump strong-armed Intel](https://www.tomshardware.com/tech-industry/policy/lawsuit-reveals-trumps-alleged-strong-arming-of-intel-troubled-chipmaker-allegedly-forced-to-give-white-house-10-percent-stake-for-release-of-chips-act-funds) ⭐️ 6.5/10

A lawsuit alleges that the White House pressured Intel into accepting a 10% government stake as a condition for releasing CHIPS Act funding.

rss · Tom's Hardware · Nov 25, 16:39

**Tags**: `#Intel`, `#CHIPS Act`, `#Policy`, `#Semiconductors`, `#Politics`

---

<a id="item-13"></a>
## [Frontier Supercomputer Maintenance and Claude's Bioinformatics Performance](https://www.solidot.org/story?sid=85989) ⭐️ 6.3/10

OAK Ridge National Lab highlighted how Frontier's high memory density leads to daily uncorrectable HBM errors and how GPU performance mismatches can stall large-scale simulations. Meanwhile, a researcher found that Anthropic's Claude outperforms specialized tools in predicting unknown bacterial protein sequences. The Frontier maintenance details provide critical insights for engineers scaling large AI and HPC systems, while the Claude results suggest general LLMs are catching up to dedicated scientific AI tools. Frontier's HBM error rate is 1.5 per day compared to one per two weeks on Summit due to a 16x increase in memory capacity. Claude outperformed other models and specialized protein tools in the test, sparking debate about the future of general vs. specialized AI models.

rss · Solidot · Nov 25, 14:18

**Background**: Frontier and Summit are top-tier supercomputers that rely on checkpointing to save progress and avoid restarting long simulations after hardware failures. High-Bandwidth Memory (HBM) is critical for AI performance but can suffer from 'uncorrectable' bit errors that require restarting jobs. The study on bacteria involved general language models like Claude being prompted to predict protein sequences, a task traditionally handled by specialized deep learning tools.

<details><summary>References</summary>
<ul>
<li><a href="https://www.computer.org/csdl/proceedings-article/dsn-s/2026/324600a156/2joOOnhW7Ju">HBM Errors at Scale: An Industrial Study - computer.org</a></li>
<li><a href="https://www.researchgate.net/publication/322760706_CHECKPOINTING_FAULT_TOLERANCE_MECHANISM">(PDF) checkpointing : fault tolerance mechanism</a></li>
<li><a href="https://www.gamesindustry.biz/ea-sports-fc-27-adds-ai-recreated-voice-of-late-commentator-john-motson">EA Sports FC 27 adds AI-recreated voice of late commentator ...</a></li>

</ul>
</details>

**Tags**: `#High-Performance Computing`, `#Bioinformatics`, `#LLM`, `#Hardware Maintenance`

---

<a id="item-14"></a>
## [Keysight ADS certified for Tower Semiconductor PH18 silicon photonics process](https://semiwiki.com/eda/keysight-eda/376442-keysight-unites-rf-and-photonic-design-for-tower-semiconductor/) ⭐️ 6.0/10

Keysight has certified its Advanced Design System (ADS) Photonic Designer for Tower Semiconductor's PH18 silicon photonics process design kits. This integration, announced in November, enables engineers to perform unified electronic and photonic circuit design within a single software environment. This certification bridges the gap between RF/microwave design and emerging silicon photonics, allowing developers to simulate electrical-optical-electrical signal paths before fabrication. It accelerates the development of next-generation datacom components by unifying disparate design workflows. The integration extends a partnership spanning more than a decade in RF semiconductor design into the silicon photonics domain. It specifically supports Tower's PH18 platform, which is currently in high-volume production, alongside their newer 300mm process options.

rss · SemiWiki · Nov 25, 16:00

**Background**: Silicon photonics uses silicon-based waveguides to transmit light for data communication, replacing or complementing traditional electrical signals. Keysight ADS is a leading EDA suite used for simulating high-frequency and photonic circuits. Tower Semiconductor PH18 is a foundry process specifically optimized for manufacturing silicon photonic components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businesswire.com/news/home/20261109345043/en/Keysight-Brings-Radio-Frequency-and-Photonic-Design-Together-for-Tower-Semiconductor">Keysight Brings Radio Frequency and Photonic Design Together for...</a></li>
<li><a href="https://towersemi.com/technology/rf-and-hpa/silicon-photonics-rf/">Silicon Photonics (SiPho) - Tower Semiconductor</a></li>
<li><a href="https://convergedigest.com/keysight-tower-ph18-rf-photonic-design-ads/">Keysight Integrates RF and Photonic Design for Tower’s SiPh</a></li>

</ul>
</details>

**Tags**: `#Silicon Photonics`, `#EDA`, `#Keysight`, `#Tower Semiconductor`, `#RF Design`

---

<a id="item-15"></a>
## [Siemens Extends Eigen AI Agent to Process Industries via SIMATIC PCS 7](https://www.electronicsweekly.com/news/business/siemens-expands-eigen-to-process-industries-2026-11/) ⭐️ 6.0/10

Siemens is expanding its Eigen Engineering Agent to the process industries by integrating it with the SIMATIC PCS 7 distributed control system. This new offering allows the AI agent to support project execution in continuous process environments. This expansion brings AI-powered automation to the process industries, which are traditionally complex and heavily reliant on manual engineering. It positions Siemens as a leader in industrial AI by reducing repetitive workload for engineers. The agent specifically targets SIMATIC PCS 7 systems, which are used in continuous process industries like power generation and chemical processing. It is designed to improve consistency and accelerate project execution through AI assistance.

rss · Electronics Weekly · Nov 25, 06:05

**Background**: Eigen Engineering Agent is an industrial AI solution that originally connected to TIA Portal to assist in electrical and mechanical engineering tasks. SIMATIC PCS 7 is a widely used distributed control system (DCS) for managing complex continuous processes in industries where 24/7 operation is required.

<details><summary>References</summary>
<ul>
<li><a href="https://www.siemens.com/en-us/products/tia-portal/eigen-engineering-agent/">Eigen Engineering Agent - Siemens</a></li>
<li><a href="https://www.siemens.com/en-us/products/process-control/simatic-pcs-7/eigen-engineering-agent-process-industries/">Eigen Engineering Agent for Process Industries - Siemens</a></li>
<li><a href="https://industrialmonitordirect.com/blogs/knowledgebase/selecting-siemens-pcs-7-for-power-plant-dcs-projects">Siemens PCS 7 DCS architecture for power plant selection | IMD</a></li>

</ul>
</details>

**Tags**: `#Siemens`, `#Industrial Automation`, `#AI Agents`, `#Process Industries`, `#SCADA`

---

<a id="item-16"></a>
## [Vishay Launches LoRa-based M2M Module for Industrial Sensors](https://www.electronicsweekly.com/news/business/vishay-launches-2026-11/) ⭐️ 6.0/10

Vishay Intertechnology has launched a new LoRa-based machine-to-machine (M2M) wireless module designed for the remote monitoring of analog precision sensors in industrial settings. The device operates in the 2.4 GHz ISM band and supports worldwide frequency allocations. This module simplifies the integration of precision sensors into industrial IoT networks by providing a long-range, low-power communication solution that eliminates the need for complex wired infrastructure. It enables real-time data transfer for remote asset monitoring and maintenance, which is critical for improving industrial automation and operational efficiency. The module specifically targets analog precision sensors, allowing for the transfer of continuous position data without the latency and bandwidth demands of high-speed video or audio. Operating in the 2.4 GHz ISM band means it shares frequency space with Wi-Fi and Bluetooth, requiring careful frequency planning to avoid interference in dense industrial environments.

rss · Electronics Weekly · Nov 25, 06:04

**Background**: LoRa (Long Range) is a Low-Power Wide-Area Network (LPWAN) protocol that enables battery-powered devices to communicate over several kilometers. In the industrial sector, it is frequently used as an alternative to Wi-Fi or cellular networks when high data rates are not required but long-range and low-power consumption are critical. The 2.4 GHz ISM (Industrial, Scientific, and Medical) band is a globally unlicensed frequency range that allows such devices to operate without specific regulatory permissions, although it is prone to congestion from other wireless technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRaWAN">LoRaWAN - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ISM_radio_band">ISM radio band - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#IoT`, `#LoRa`, `#Industrial Automation`, `#Wireless Communication`, `#Sensor Technology`

---

<a id="item-17"></a>
## [dToF sensor with ranging capability beyond 8m](https://www.electronicsweekly.com/news/business/dtof-sensor-with-ranging-capability-beyond-8m-2026-11/) ⭐️ 6.0/10

STMicroelectronics is sampling the FlightSense VL53LB, a direct Time-of-Flight sensor that extends ranging capability beyond 8 meters for use in compact consumer electronics.

rss · Electronics Weekly · Nov 25, 06:02

**Tags**: `#sensors`, `#dToF`, `#STMicroelectronics`, `#hardware`, `#consumer-electronics`

---

<a id="item-18"></a>
## [(PR) Kioxia to Showcase XL-FLASH Generation 3 Technology, the Next-Generation Low-Latency, High-Performance Flash Memory for AI](https://www.techpowerup.com/355197/kioxia-to-showcase-xl-flash-generation-3-technology-the-next-generation-low-latency-high-performance-flash-memory-for-ai) ⭐️ 5.5/10

Kioxia announced it will showcase its next-generation XL-FLASH Gen 3 memory, designed for low-latency AI applications, at a forum in November 2026.

rss · TechPowerUp News · Nov 25, 13:17

**Tags**: `#Hardware`, `#Storage`, `#AI`, `#Flash Memory`, `#Kioxia`

---

<a id="item-19"></a>
## [7 new Intel Nova Lake-S Core Ultra 4000-series CPUs detailed in new leak](https://www.tomshardware.com/pc-components/cpus/7-new-intel-nova-lake-s-core-ultra-4000-series-cpus-detailed-in-new-leak-lineup-includes-5-5ghz-ultra-9-4970k-bfc-ahead-of-the-expected-february-2027-release) ⭐️ 5.5/10

A leak details seven upcoming Intel Core Ultra 4000-series desktop CPUs, including the Ultra 9 4970K with a 5.5 GHz boost, ahead of a potential February 2027 launch event.

rss · Tom's Hardware · Nov 25, 15:30

**Tags**: `#Intel`, `#CPU`, `#Hardware Leak`, `#Nova Lake`, `#Desktop Processor`

---

<a id="item-20"></a>
## [New CPU benchmark tool promises 40 years of compatibility, with support as far back as i386, Windows 95](https://www.tomshardware.com/pc-components/cpus/new-cpu-benchmark-tool-promises-40-years-of-compatibility-with-support-as-far-back-as-i386-windows-95-crystalmark-cpuix-tested-on-nec-pc-98-21bs-pentium-100-and-more) ⭐️ 5.5/10

A new CPU benchmark tool named CrystalMark CPUix has been released, featuring compatibility spanning 40 years of hardware from i386 and Windows 95 to modern processors.

rss · Tom's Hardware · Nov 25, 10:00

**Tags**: `#Hardware`, `#CPU`, `#Benchmarking`, `#Retrocomputing`, `#Tom's Hardware`

---