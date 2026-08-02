---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 43 items, 11 important content pieces were selected

---

1. [Iran Suspected of Cyberattacks on 45 US Water Utilities, Forcing Manual Operations](#item-1) ⭐️ 7.5/10
2. [Dasharo v0.9.0 brings open-source firmware to AMD AM5 platform](#item-2) ⭐️ 7.5/10
3. [Google Suspends Google Earth AI Image Generation Feature Within 48 Hours of Launch](#item-3) ⭐️ 7.3/10
4. [Go 1.27 Interactive Tour](#item-4) ⭐️ 7.0/10
5. [ByteDance Releases Seedance 2.5 with One-Take Creation](#item-5) ⭐️ 7.0/10
6. [Diátaxis](#item-6) ⭐️ 7.0/10
7. [AMD Zen 6 CPUs Rumored to Fix Microstutters with Per-Core Optimizations](#item-7) ⭐️ 6.5/10
8. [Kioxia Launches CM10 Series: PCIe Gen6 Enterprise SSDs](#item-8) ⭐️ 6.5/10
9. [近120万辆特斯拉汽车遭调查](#item-9) ⭐️ 6.3/10
10. [Chinese AI Models Sweep Top 5 on OpenRouter Weekly Rankings](#item-10) ⭐️ 6.3/10
11. [Microsoft vows to make Windows 11 fly on 8GB RAM amid memory shortage — optimizations to reduce OS memory footprint have begun](#item-11) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Iran Suspected of Cyberattacks on 45 US Water Utilities, Forcing Manual Operations](https://www.tomshardware.com/tech-industry/cyber-security/iran-suspected-of-conducting-cyberattacks-on-us-water-suppliers-in-45-municipalities-small-towns-mostly-targeted-with-utilities-switching-to-manual-control) ⭐️ 7.5/10

Several US water utilities across 45 municipalities have been hit by cyberattacks suspected to have originated from Iran. Although systems remain operational, many affected utilities—predominantly small towns—have reverted to manual control to safeguard their water supply. This incident highlights the vulnerability of US critical infrastructure to nation-state cyber threats and the potentially severe public health consequences of compromised water systems. Small municipalities are disproportionately targeted because they typically lack the cybersecurity resources and expertise that larger utilities possess. The attacks targeted SCADA (Supervisory Control and Data Acquisition) systems and Programmable Logic Controllers (PLCs) commonly used in water treatment and distribution. According to CISA advisories, Iranian-affiliated APT actors have been observed exploiting internet-exposed PLCs to manipulate HMI and SCADA displays, echoing past incidents such as the 2021 Oldsmar, Florida attack and the 2024 Texas water utility attacks.

rss · Tom's Hardware · Aug 2, 13:10

**Background**: Water utilities rely on SCADA systems and PLCs to monitor and automate treatment processes, including chemical dosing, pressure regulation, and distribution. Cyberattacks on these systems can manipulate chemical levels—as seen in the 2021 Oldsmar, Florida incident where attackers tried to increase sodium hydroxide—or cause physical damage by overflowing tanks, as happened in Texas in 2024. Iran has been identified by CISA and the FBI as a persistent cyber threat targeting US critical infrastructure, particularly industrial control devices in the energy and water sectors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a">Iranian-Affiliated Cyber Actors Exploit Programmable Logic Controllers Across US Critical Infrastructure | CISA</a></li>
<li><a href="https://www.wired.com/story/iran-linked-hackers-are-sabotaging-us-energy-and-water-infrastructure/">Iran-Linked Hackers Are Sabotaging US Energy and Water Infrastructure | WIRED</a></li>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a">Compromise of U.S. Water Treatment Facility | CISA</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#critical-infrastructure`, `#cyberattacks`, `#geopolitics`, `#water-utilities`

---

<a id="item-2"></a>
## [Dasharo v0.9.0 brings open-source firmware to AMD AM5 platform](https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850) ⭐️ 7.5/10

3mdeb has released Dasharo v0.9.0, the first open-source firmware for AMD's AM5 platform, combining Coreboot with AMD's openSIL silicon initialization library. It targets Zen 4 APUs on MSI B850 motherboards, with initial support for the MSI B850-P WiFi model. This release breaks AMD's long-standing closed firmware ecosystem for modern consumer desktop platforms, giving users firmware transparency, auditability, and freedom from vendor lock-in. It represents an important stepping stone toward broader open-source firmware adoption on Zen-based consumer hardware. As an early v0.9.0 build, support is currently limited to a single MSI B850 board, meaning broader board coverage and feature parity will require further development. Dasharo benefits from 3mdeb's mature CI/CD pipeline and its track record of deploying open-source firmware on more than half a million commercial x86 units.

rss · Tom's Hardware · Aug 2, 12:10

**Background**: Coreboot is an open-source project that provides lightweight firmware to replace proprietary BIOS/UEFI, performing only the minimal hardware initialization required to hand off to an operating system. AMD openSIL is a set of three statically linked libraries (xSIM, xPRF, xUSL) that abstract silicon initialization, allowing the same low-level code to be linked into either UEFI or Coreboot firmware. Dasharo, developed by 3mdeb, is a productized open-source firmware distribution emphasizing trustworthiness, privacy, and transparency. AMD's AM5 is the company's current consumer socket, supporting Ryzen 7000/9000 series CPUs and APUs built on the Zen 4 architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.dasharo.com/">About Dasharo - Dasharo Universe</a></li>
<li><a href="https://www.amd.com/en/blogs/2023/empowering-the-industry-with-open-system-firmware-.html">Empowering The Industry with Open System Firmware – AMD openSIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coreboot">coreboot - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#coreboot`, `#firmware`, `#AMD`, `#AM5`

---

<a id="item-3"></a>
## [Google Suspends Google Earth AI Image Generation Feature Within 48 Hours of Launch](https://36kr.com/newsflashes/3922077104664199?f=rss) ⭐️ 7.3/10

Google pulled its newly launched AI image generation feature in Google Earth less than 48 hours after rollout, after users shared AI-created images that appeared to violate company policies and experts warned the tool could be weaponized to spread misinformation by overlaying fictional scenes on real satellite imagery. This incident highlights the tension between rapid AI feature deployment and responsible safety safeguards, particularly for tools built on trusted platforms like Google Earth that journalists and researchers rely on as visual evidence sources. It also serves as a notable real-world case study in how generative AI can erode trust in established media platforms when misused. The feature, reportedly based on the Nano Banana 2 model, allowed users to anchor AI-generated images to real geographic coordinates. One widely circulated example showed a fake sinkhole digitally inserted over the Great Pyramid of Giza; some images were labeled with 'AI-GENERATED' warning banners but still demonstrated the potential for misuse.

rss · 36氪 · Aug 2, 07:51

**Background**: Google Earth is a widely used geospatial platform that provides satellite and aerial imagery, serving as a trusted reference tool for journalists, researchers, and the general public. Generative AI image models can now produce highly realistic synthetic visuals, raising concerns about 'deepfakes'—AI-generated content presented as authentic. When such synthetic imagery is combined with the credibility of real geographic coordinates, the resulting misinformation can be especially convincing and difficult to debunk.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c9349yx2ydvo">Google withdraws Earth AI tool after misinformation warnings</a></li>
<li><a href="https://www.storyboard18.com/digital/google-rolls-back-google-earth-ai-image-generation-feature-a-day-after-launch-over-policy-concerns-106286.htm">Google rolls back Google Earth AI image generation feature a day...</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/9288/google-earth-ai-fake-satellite-imagery-rollback">Google Earth : the Button That Generated Fake Satellite Images ...</a></li>

</ul>
</details>

**Discussion**: Online reactions were largely critical and sarcastic, with commentators on LinkedIn and tech forums mocking the seemingly obvious risks of deploying an AI image generator on a platform trusted for visual evidence. Many expressed concerns that even a short window of availability was enough to produce misleading imagery, and some questioned whether Google had failed to anticipate the misuse scenario before launch.

**Tags**: `#AI safety`, `#Google Earth`, `#misinformation`, `#responsible AI`, `#generative AI`

---

<a id="item-4"></a>
## [Go 1.27 Interactive Tour](https://victoriametrics.com/blog/go-1-27/index.html) ⭐️ 7.0/10

An interactive tour of Go 1.27 features including generics improvements, MTE compatibility fixes for Android, and automatic HTTP response body draining, with substantive community discussion.

hackernews · Hixon10 · Aug 2, 01:35 · [Discussion](https://news.ycombinator.com/item?id=49140218)

**Tags**: `#Go`, `#programming-languages`, `#release-notes`, `#generics`, `#runtime`

---

<a id="item-5"></a>
## [ByteDance Releases Seedance 2.5 with One-Take Creation](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ⭐️ 7.0/10

ByteDance has released Seedance 2.5, the latest version of its video generation model, featuring one-take creation that can produce up to 30-second audio-video clips in a single pass, along with flexible referencing capabilities and support for multi-round extensions. This release is significant in the rapidly evolving AI video generation space, where ByteDance leverages its TikTok-era expertise to push generation length and quality. It directly competes with models like MiniMax's H3 and signals that the gap between closed commercial models and open-weight alternatives continues to narrow. Seedance 2.5 can generate high-quality 30-second audio-video clips in a single pass and supports multiple rounds of extension. Unlike Seedance 2.0 which moved to true multi-modal control, this version emphasizes streamlined one-take workflows; community discussion notes that the model appears heavily tuned for action and high-effect text-to-video shots favored by the Chinese market.

hackernews · njaremko · Aug 1, 20:45 · [Discussion](https://news.ycombinator.com/item?id=49138302)

**Background**: Seedance is ByteDance's flagship AI video generation model family, part of the broader 'Seed' foundation model suite. Built on ByteDance's extensive experience processing billions of short-form videos through TikTok, the model family evolved from text-and-image single-shot generation in version 1.0 to true multi-modal control in 2.0. Flexible referencing allows users to upload reference images, videos, or audio to guide the generated output—a capability now standard across competing models such as MiniMax H3 and Google's Gemini Omni.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">One - take Creation, Flexible Referencing: Introducing Seedance 2.5</a></li>
<li><a href="https://seed.bytedance.com/en/seedance">Seedance</a></li>
<li><a href="https://hailuoai.video/tools/minimax-h3">MiniMax H3 Multimodal AI Video Model | Hailuo AI</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed but engaged. Several commenters praised Seedance 2.5's output quality, though one noted that ByteDance's optimization skews toward Chinese market preferences—emphasizing action and high-effect text-to-video shots rather than the v2v dialogue-heavy workflows demanded by Western filmmakers. Others raised concerns about escalating inference costs (one user reported spending over $10k generating 50k images and nearly an hour of video), while a commenter highlighted that open-weight competitor MiniMax H3 was releasing within 24 hours and could run on mid-range consumer GPUs like the 3080. A minority voice questioned the overall societal value of generative video tools.

**Tags**: `#video-generation`, `#bytedance`, `#generative-ai`, `#text-to-video`, `#ai-models`

---

<a id="item-6"></a>
## [Diátaxis](https://diataxis.fr/) ⭐️ 7.0/10

Diátaxis is a documentation framework that categorizes content into four distinct types (tutorials, how-to guides, reference, and explanation), each with its own purpose and writing style.

hackernews · ryanseys · Aug 1, 20:33 · [Discussion](https://news.ycombinator.com/item?id=49138188)

**Tags**: `#documentation`, `#technical-writing`, `#methodology`, `#knowledge-management`, `#developer-experience`

---

<a id="item-7"></a>
## [AMD Zen 6 CPUs Rumored to Fix Microstutters with Per-Core Optimizations](https://www.tomshardware.com/pc-components/cpus/amds-upcoming-zen-6-processors-could-fix-microstutters-and-improve-1-percent-lows-in-games-next-gen-cpus-tipped-to-feature-per-core-optimizations-for-thermal-and-power-budgets) ⭐️ 6.5/10

A new report suggests AMD's upcoming Zen 6 processors will introduce per-core optimizations for thermal and power budgets, which individually may seem minor but collectively could significantly reduce microstutters and improve 1% low frame rates in gaming. If accurate, these optimizations could meaningfully improve the gaming experience on AMD's next-generation platform by addressing frame pacing issues that have plagued modern CPUs, potentially giving AMD a competitive edge over Intel in gaming workloads. These improvements are based on unverified leaks rather than official AMD announcements, and per-core thermal/power management is related to addressing issues like C-states and power-saving features that have historically contributed to microstutters in games.

rss · Tom's Hardware · Aug 2, 12:30

**Background**: Microstutters are brief, irregular frame hitches that disrupt smooth gameplay, often caused by CPU power management features like C-states switching cores in and out of sleep. 1% lows refer to the average frame rate in the worst 1% of frames, a key metric for perceived smoothness beyond average FPS. AMD's Zen architecture has been the backbone of Ryzen processors since 2017, with each generation bringing improvements in instructions per clock (IPC), cache hierarchy, and power efficiency. Zen 6 is expected to succeed Zen 5 and may include up to 12-core CCDs with larger 48MB L3 caches.

<details><summary>References</summary>
<ul>
<li><a href="https://www.noobfeed.com/hardware/amd-zen6-ryzen-zen5-x3d-am5-support">AMD Zen 6 Ryzen Could Match Zen 5 X3D While... | NoobFeed</a></li>
<li><a href="https://linustechtips.com/topic/1228554-cpu-microstuttering-due-to-dxgmms2sys/">CPU microstuttering due to dxgmms2.sys - CPUs ... - Linus Tech Tips</a></li>
<li><a href="https://superuser.com/questions/1382406/experiencing-microstutters-in-all-games-after-changing-to-rtx-2070-video-card">cpu - Experiencing microstutters in all games after... - Super User</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Zen 6`, `#CPU`, `#gaming performance`, `#PC hardware`

---

<a id="item-8"></a>
## [Kioxia Launches CM10 Series: PCIe Gen6 Enterprise SSDs](https://www.servethehome.com/kioxia-cm10-series-launched-for-the-pcie-gen6-generation-of-ssds/) ⭐️ 6.5/10

Kioxia has launched the CM10 SSD series, which spans 2.5-inch and EDSFF form factors, supports both PCIe Gen5 and Gen6 interfaces, offers air-cooled and liquid-cooled variants, and is built around two different NAND generations. The CM10 series marks one of the first enterprise SSD families to natively support PCIe Gen6, signaling the beginning of the Gen6 adoption cycle in data centers. The broad combination of form factors and cooling options gives hyperscale and enterprise customers flexibility for diverse deployment scenarios, including AI workloads that demand very high storage throughput. The series covers both legacy 2.5-inch bays and the newer EDSFF (Enterprise and Datacenter Storage Form Factor), which offers better airflow, higher capacity, and easier serviceability. By supporting PCIe Gen5 alongside Gen6 in the same product family, Kioxia allows customers with current-generation platforms to adopt the drives today while preserving a migration path to Gen6 servers.

rss · ServeTheHome · Aug 1, 15:00

**Background**: PCIe Gen 6 doubles the per-lane signaling rate to 64 GT/s using PAM4 encoding, enabling roughly 128 GB/s of throughput per direction on an x16 link, which is critical for AI training and inference workloads that move massive datasets. EDSFF is a newer SSD form factor designed specifically for hyperscale and enterprise data centers, replacing older 2.5-inch designs with better thermal characteristics and higher density. Kioxia is one of the world's largest NAND flash manufacturers, and its enterprise SSD line typically competes with products from Samsung, Solidigm, and Micron.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/pcie-gen6-and-gen5-will-both-matter-for-ai-storage/">PCIe Gen 6 and Gen5 Will Both Matter for AI Storage - ServeTheHome</a></li>
<li><a href="https://www.ssstc.com/knowledge-detail/edsff-enterprise-ssd-form-factor/">EDSFF :E1/ E3 Enterprise SSD Form Factors ｜SSSTC</a></li>
<li><a href="https://www.supermicro.com/en/glossary/edsff">What Is Enterprise and Datacenter SSD Form Factor ? | Supermicro</a></li>

</ul>
</details>

**Tags**: `#SSDs`, `#PCIe Gen6`, `#Kioxia`, `#enterprise storage`, `#hardware`

---

<a id="item-9"></a>
## [近120万辆特斯拉汽车遭调查](https://36kr.com/newsflashes/3922152130653828?f=rss) ⭐️ 6.3/10

US NHTSA launches investigation into nearly 1.2 million Tesla Model 3 and Model Y vehicles over reported suspension failures that could cause loss of vehicle control.

rss · 36氪 · Aug 2, 09:30

**Tags**: `#Tesla`, `#NHTSA`, `#automotive safety`, `#electric vehicles`, `#regulatory investigation`

---

<a id="item-10"></a>
## [Chinese AI Models Sweep Top 5 on OpenRouter Weekly Rankings](https://36kr.com/newsflashes/3921989528432259?f=rss) ⭐️ 6.3/10

According to the latest weekly AI model call volume rankings released by OpenRouter, all top 5 spots were claimed by Chinese-developed models. Xiaomi's MiMo-V2.5 led the list with 10.5 trillion tokens in a single week (up 12% week-over-week), while Tencent's Hunyuan 3 — open-sourced only on July 6 — surged over 999% week-over-week to rank third, making it the fastest-growing model on the chart. This ranking signals a significant shift in the global LLM competitive landscape: Chinese models are no longer just regional contenders but are dominating real-world developer adoption on a neutral third-party platform. The rapid uptake of newly open-sourced models like Hunyuan 3 suggests that Chinese labs are closing the gap — and potentially overtaking — Western closed-source alternatives in developer mindshare. DeepSeek occupies both the #2 and #5 slots with two models that form a high-low pairing to cover different developer needs, with its flagship Pro version said to rival top overseas closed-source models on code and complex agent tasks. The fact that all five models climbed the charts shortly after release highlights how aggressive Chinese labs have become in capturing API market share.

rss · 36氪 · Aug 2, 06:14

**Background**: OpenRouter is a developer-focused AI infrastructure platform that acts as a unified API gateway to 400+ large language models from multiple providers, used by 250k+ apps and over 4.2 million users globally. Token count is the standard unit for measuring LLM usage, where tokens represent the smallest pieces of text (words, subwords, or characters) a model processes — so 10.5 trillion tokens in one week represents an enormous volume of real-world inference activity. DeepSeek is a Hangzhou-based Chinese AI company that has gained international attention for building competitive open-weight LLMs at reportedly low training and inference costs.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter ? A Guide with Practical Examples | Codecademy</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Chinese-AI`, `#OpenRouter`, `#LLM-market`, `#industry-news`

---

<a id="item-11"></a>
## [Microsoft vows to make Windows 11 fly on 8GB RAM amid memory shortage — optimizations to reduce OS memory footprint have begun](https://www.tomshardware.com/software/windows/microsoft-vows-to-make-windows-11-fly-on-8gb-ram-amid-memory-shortage-optimizations-to-reduce-os-memory-footprint-have-begun) ⭐️ 5.5/10

Microsoft is optimizing Windows 11 to reduce its memory footprint and run more smoothly on 8GB RAM systems, likely driven by ongoing memory chip shortages and the return of 8GB laptops.

rss · Tom's Hardware · Aug 1, 14:48

**Tags**: `#Windows 11`, `#Microsoft`, `#RAM optimization`, `#PC hardware`, `#operating systems`

---