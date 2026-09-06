---
layout: default
title: "Horizon Summary: 2026-09-06 (EN)"
date: 2026-09-06
lang: en
---

> From 41 items, 16 important content pieces were selected

---

1. [肾病患者靠移植猪肾生活九个月](#item-1) ⭐️ 7.3/10
2. [Visualizing Rust's Vtables: How dyn Trait Works in Memory](#item-2) ⭐️ 7.0/10
3. [DLSS 5 Swapper Brings Neural Rendering to Unsupported Games and Older GPUs](#item-3) ⭐️ 6.5/10
4. [Acemagic Unveils Mini-Workstation with AMD Ryzen AI Max+ PRO 495](#item-4) ⭐️ 6.5/10
5. [Stripped-down Windows 11 for AI developers demands 64GB RAM and insane 250 GB/s bandwidth — Project Zenith will debut on AMD's flagship Ryzen AI Halo platform](#item-5) ⭐️ 6.5/10
6. [Taiwan Cracks Down on Illegal Chinese-Owned Tech Firms](#item-6) ⭐️ 6.5/10
7. [Trump slaps up to 100% tariffs on imported drones and critical components in latest move against China's proliferation of  U.S. drone market, citing national security — products from allied nation face 10-15% rates](#item-7) ⭐️ 6.5/10
8. [The revolt of the reader](#item-8) ⭐️ 6.0/10
9. [Private German rocket makes history, reaches orbit from European soil](#item-9) ⭐️ 6.0/10
10. [Learn Programming with OCaml: Online Book Released](#item-10) ⭐️ 6.0/10
11. [AMD BC-250 Mining Board Repurposed as a Budget Gaming PC (2025)](#item-11) ⭐️ 6.0/10
12. [Acemagic Unveils F2A and F7A Mini PCs With Intel Panther Lake and AMD Gorgon Point](#item-12) ⭐️ 5.5/10
13. [GEEKOM's A9 Mega Mini PCs Form Local Inference Cluster at IFA 2026](#item-13) ⭐️ 5.5/10
14. [Modder gets Nvidia's DLSS 5 working on AMD's RDNA 4 GPUs — RX 9070 XT only manages 30 FPS at 1080p right now, but 5070 Ti-level performance is the eventual goal](#item-14) ⭐️ 5.5/10
15. [Tom's Hardware Benchmarks DLSS 5 in NBA 2K27 Across All RTX 50-Series GPUs](#item-15) ⭐️ 5.5/10
16. [Japan to mass-procure 3D-printed rocket-powered drone interceptor — Terra B1 capable of countering one-way attack platforms](#item-16) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [肾病患者靠移植猪肾生活九个月](https://www.solidot.org/story?sid=85295) ⭐️ 7.3/10

A kidney disease patient survived nine months with a transgenic pig kidney before receiving a human transplant, marking a milestone in xenotransplantation as a potential bridge therapy, alongside studies on meat-cancer links and quantum tests of the equivalence principle.

rss · Solidot · Sep 5, 13:35

**Tags**: `#xenotransplantation`, `#medical-breakthrough`, `#genetic-engineering`, `#transplant-medicine`, `#Solidot-news-roundup`

---

<a id="item-2"></a>
## [Visualizing Rust's Vtables: How dyn Trait Works in Memory](https://sofiabelen.github.io/projects/visualizing-rusts-vtables-how-dyn-trait-works-in-memory/) ⭐️ 7.0/10

A detailed, well-illustrated blog post by Sofía Belén was published explaining how Rust's dyn Trait and vtables are laid out in memory, covering object safety, fat pointers, and zero-sized types (ZSTs). 理解 trait object 的内存布局对于从事系统级编程、高性能库或 FFI 开发的中高级 Rust 开发者至关重要，因为它澄清了动态分派在底层的工作原理。 The post explains that trait objects are dynamically sized types (DSTs) represented by 16-byte fat pointers containing both a data pointer and a vtable pointer. It also clarifies that the term "Object Safety" has been officially renamed to "dyn compatibility" in recent Rust documentation.

hackernews · torutofu · Sep 5, 13:31 · [Discussion](https://news.ycombinator.com/item?id=49576343)

**Background**: Rust supports two forms of dispatch: static dispatch via generics and monomorphization, and dynamic dispatch via trait objects (dyn Trait). Trait objects are dynamically sized types that must be referenced through pointers, which store not only the address of the data but also a pointer to a vtable containing method implementations. Not all traits can be used as trait objects—only those that are "object safe" (now termed "dyn compatible") qualify. Zero-sized types (ZSTs) like () occupy no memory and are often used as markers or in generic contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://sofiabelen.github.io/projects/visualizing-rusts-vtables-how-dyn-trait-works-in-memory/">Visualizing Rust 's Vtables: How dyn Trait Works In Memory</a></li>
<li><a href="https://stackoverflow.com/questions/57754901/what-is-a-fat-pointer">rust - What is a "fat pointer"? - Stack Overflow Code sample</a></li>
<li><a href="https://doc.rust-lang.org/nomicon/exotic-sizes.html">Exotically Sized Types - The Rustonomicon - Learn Rust</a></li>

</ul>
</details>

**Discussion**: The post received strong community engagement with 137 upvotes and 19 comments. Discussion included a terminology clarification noting that "Object Safety" has been renamed to "dyn compatibility" in the Rust reference, a recommendation of the cheats.rs memory layout section as a related resource, praise for the blog's writing quality, and a follow-up question about reverse-engineering the internal vtable structure as a list of function pointers.

**Tags**: `#rust`, `#memory-layout`, `#vtables`, `#dyn-trait`, `#systems-programming`

---

<a id="item-3"></a>
## [DLSS 5 Swapper Brings Neural Rendering to Unsupported Games and Older GPUs](https://www.techpowerup.com/352395/new-dlss-5-swapper-tool-brings-neural-rendering-to-games-nvidia-never-supported) ⭐️ 6.5/10

Developer rakanki911 has released a GitHub tool called DLSS 5 Swapper that automates installing NVIDIA's DLSS 5 Neural Rendering into games that never received official support, using the DLSS5-Feeder mod to emulate DLSS calls and ReShade to supply depth and motion data. This community tool democratizes access to NVIDIA's latest neural rendering technology, enabling millions of RTX 20 and 30 series owners and players of legacy or emulated titles to experience AI-driven visual enhancements that NVIDIA itself has restricted to RTX 50 series hardware and a limited game catalog. The tool supports DirectX 9 through DirectX 12 titles plus emulators like PCSX2, Dolphin, and Xenia, but since it is unofficial and bundles leaked DLSS 5 DLLs with no NVIDIA endorsement, users should verify the download source to avoid tampered binaries.

rss · TechPowerUp News · Sep 5, 22:49

**Background**: NVIDIA DLSS (Deep Learning Super Sampling) is a suite of neural rendering technologies that leverages RTX Tensor Cores to upscale lower-resolution images in real time, with DLSS 5 representing the latest generation that applies neural network reprocessing to already-rendered game frames for photorealistic output. DLSS 5 was initially discovered through DLL files leaked in the NBA 2K27 pre-launch build, which modders then reverse-engineered to run on older hardware and unsupported titles. ReShade is a widely-used generic post-processing injector that can access frame color and depth information from virtually any game, making it the natural mechanism for supplying the depth buffer and motion vectors that neural rendering requires.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/352395/new-dlss-5-swapper-tool-brings-neural-rendering-to-games-nvidia-never-supported">New DLSS 5 Swapper Tool Brings Neural Rendering to Games ...</a></li>
<li><a href="https://github.com/himomohi/dlss5-feeder">GitHub - himomohi/dlss5-feeder: DLSS 5 neural rendering in ...</a></li>
<li><a href="https://reshade.me/">ReShade Home</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#dlss`, `#neural-rendering`, `#gpu-modding`, `#gaming`

---

<a id="item-4"></a>
## [Acemagic Unveils Mini-Workstation with AMD Ryzen AI Max+ PRO 495](https://www.techpowerup.com/352384/acemagic-shows-mini-workstation-with-amd-ryzen-ai-max-pro-495-gorgon-halo-apu) ⭐️ 6.5/10

At IFA 2026 in Berlin, Acemagic showcased a compact 2-liter mini-workstation powered by AMD's flagship Ryzen AI Max+ PRO 495 'Gorgon Halo' APU, featuring 16 Zen 5 cores, Radeon 8065S integrated graphics, and support for up to 192 GB of LPDDR5X memory. The 192 GB unified memory pool makes this one of the most memory-rich compact systems available, enabling local inference of very large language models (up to ~300B parameters) without a discrete GPU, directly challenging Apple's Mac Studio approach for local AI workloads. The system delivers 55 TOPS from its NPU (INT8) and ~131 TOPS total compute, includes OCuLink for external GPU expansion, and uses LPDDR5X at 8,533 MT/s. The Zen 5 CPU boosts to 5.2 GHz, while the Radeon 8065S iGPU contains 40 RDNA compute units, sharing the same memory pool.

rss · TechPowerUp News · Sep 5, 15:17

**Background**: AMD's 'Gorgon Halo' is the successor to the Strix Halo family (Ryzen AI Max+ 395), sharing the same monolithic APU design philosophy of using large pools of unified LPDDR5X memory instead of a discrete GPU. This architecture is AMD's answer to Apple Silicon for local AI inference, where memory bandwidth and capacity matter more than raw GPU compute for LLM workloads. TOPS (Tera Operations Per Second) measures peak AI inference throughput using INT8 precision, and Microsoft currently requires 40+ TOPS for Copilot+ PC certification.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/amd-pushes-ryzen-ai-max-400-to-192gb-memory-single-chip-run-300b-ai-llms-locally/">AMD Pushes Ryzen AI MAX 400 ‘ Gorgon Halo ’ to 192GB Memory...</a></li>
<li><a href="https://www.techpowerup.com/348739/amd-ryzen-ai-max-pro-495-gorgon-halo-apu-appears-with-radeon-8065s">AMD Ryzen AI Max+ PRO 495 " Gorgon Halo " APU ... | TechPowerUp</a></li>
<li><a href="https://pinggy.io/blog/best_hardware_for_self_hosting_local_llms/">Picking the Right Hardware to Run LLMs Locally in 2026 ...</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#AMD`, `#mini-workstation`, `#local-LLM`, `#IFA-2026`

---

<a id="item-5"></a>
## [Stripped-down Windows 11 for AI developers demands 64GB RAM and insane 250 GB/s bandwidth — Project Zenith will debut on AMD's flagship Ryzen AI Halo platform](https://www.tomshardware.com/software/windows/stripped-down-windows-11-for-ai-developers-demands-64gb-ram-and-insane-250-gb-s-bandwidth-project-zenith-will-debut-on-amds-flagship-ryzen-ai-halo-platform) ⭐️ 6.5/10

Microsoft's Project Zenith is a stripped-down Windows 11 for AI developers requiring 64GB RAM and 250 GB/s bandwidth, debuting on AMD's Ryzen AI Halo platform.

rss · Tom's Hardware · Sep 5, 17:18

**Tags**: `#Windows 11`, `#AI development`, `#AMD Ryzen AI`, `#Microsoft`, `#developer tools`

---

<a id="item-6"></a>
## [Taiwan Cracks Down on Illegal Chinese-Owned Tech Firms](https://www.tomshardware.com/tech-industry/policy/taiwan-cracks-down-on-tech-businesses-with-illegal-chinese-ownership-166-investigations-and-at-least-36-convictions-since-2020) ⭐️ 6.5/10

Taiwan's Ministry of Justice Investigation Bureau (MJIB) has investigated 166 tech businesses for illegal Chinese ownership since 2020, resulting in at least 36 convictions. These companies were found to have been hiring Taiwanese semiconductor experts for R&D without proper government authorization. This enforcement campaign highlights Taiwan's determination to protect its semiconductor intellectual property from Chinese industrial espionage, a critical concern given Taiwan's dominance in advanced chip manufacturing. The crackdown signals tightening cross-strait tech restrictions and could reshape how semiconductor talent and IP flow in the global supply chain. Beyond the 166 investigations, the MJIB also closed 67 trade-secret cases during this period, with court records showing approximately 190 individuals charged across roughly 60 cases. Chinese companies operating in Taiwan are required under the Cross-Strait Act to obtain government approval, and Chinese nationals are prohibited from serving as CEO of a Taiwan company in sensitive sectors.

rss · Tom's Hardware · Sep 5, 10:40

**Background**: Taiwan is home to TSMC and other semiconductor giants that produce the vast majority of the world's most advanced chips, making its tech sector a prime target for foreign espionage. Under the Cross-Strait Act and related investment regulations, Chinese companies must obtain government approval before operating in Taiwan, and Chinese investment in core technology sectors like semiconductors is regarded as a national security issue. The U.S. has also grown closer to Taiwan's semiconductor industry, with TSMC's $65 billion Arizona fab project supported in part by the CHIPS and Science Act, reflecting broader geopolitical tensions over chip supply chains.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/taiwan-ministry-ran-166-chinese-chip-talent-probes-and-67-trade-secret-cases">Taiwan Ministry Ran 166 Chinese-Chip-Talent Probes and... | AI Weekly</a></li>
<li><a href="https://restofworld.org/2026/taiwan-china-chip-investigations/">Taiwan’s six-year hunt for China’s undercover chip labs - Rest of World</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_industry_in_Taiwan">Semiconductor industry in Taiwan - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#tech-policy`, `#geopolitics`, `#supply-chain`, `#taiwan`

---

<a id="item-7"></a>
## [Trump slaps up to 100% tariffs on imported drones and critical components in latest move against China's proliferation of  U.S. drone market, citing national security — products from allied nation face 10-15% rates](https://www.tomshardware.com/tech-industry/drones/trump-slaps-up-to-100-percent-tariffs-on-imported-drones-and-critical-components-in-latest-move-against-chinas-proliferation-of-u-s-drone-market-citing-national-security-products-from-allied-nation-face-10-15-percent-rates) ⭐️ 6.5/10

The Trump administration has imposed tariffs of up to 100% on imported drones and key components to curb Chinese dominance in the U.S. drone market, while allied nations face lower 10-15% rates.

rss · Tom's Hardware · Sep 5, 10:20

**Tags**: `#drones`, `#trade-policy`, `#tariffs`, `#supply-chain`, `#china-tech`

---

<a id="item-8"></a>
## [The revolt of the reader](https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/) ⭐️ 6.0/10

Bryan Cantrill's essay exploring reader pushback against AI-generated content and the role of AI detection tools like Pangram.

hackernews · chmaynard · Sep 5, 21:37 · [Discussion](https://news.ycombinator.com/item?id=49580939)

**Tags**: `#AI`, `#LLM`, `#content-quality`, `#culture`, `#Bryan-Cantrill`

---

<a id="item-9"></a>
## [Private German rocket makes history, reaches orbit from European soil](https://www.space.com/space-exploration/launches-spacecraft/isar-aerospace-second-launch-norway-andoya-spaceport-spectrum-rocket) ⭐️ 6.0/10

Private German rocket company Isar Aerospace successfully reached orbit from European soil, marking a historic milestone for the European private space industry.

hackernews · bookmtn · Sep 5, 20:31 · [Discussion](https://news.ycombinator.com/item?id=49580369)

**Tags**: `#space-industry`, `#european-space`, `#private-rockets`, `#geopolitics`, `#commercial-space`

---

<a id="item-10"></a>
## [Learn Programming with OCaml: Online Book Released](https://usr.lmf.cnrs.fr/lpo/) ⭐️ 6.0/10

A new online book titled 'Learn Programming with OCaml' has been published at usr.lmf.cnrs.fr/lpo/, offering a structured introduction to programming through the OCaml language. The resource has attracted attention on programming forums, sparking pedagogical discussion about whether ML-family languages should be the first language taught to computer science students. The choice of first programming language has lasting effects on how students conceptualize computation, and ML-family languages emphasize functional programming, immutability, and strong type systems that can build solid theoretical foundations. This book contributes to an ongoing debate about whether functional languages should replace or complement more commonly taught languages like Python and Java in introductory CS curricula. The book is hosted by the Laboratoire de Méthodes Formelles (LMF) at CNRS, a French research institution associated with formal methods. OCaml, created in 1996 by Xavier Leroy and others at Inria, was originally developed for automated theorem proving and remains widely used in static analysis and formal verification.

hackernews · elvis70 · Sep 5, 16:45 · [Discussion](https://news.ycombinator.com/item?id=49578280)

**Background**: OCaml is a general-purpose, multi-paradigm programming language that extends the Caml dialect of ML with object-oriented features. It belongs to the ML family of strict functional languages, which evolved from Robin Milner's Meta Language developed at the University of Edinburgh in the 1970s for the LCF theorem proving system. Functional programming, the paradigm OCaml exemplifies, treats computation as the evaluation of mathematical functions and avoids mutable state. The ML family has influenced many modern languages including F#, Scala, and Haskell.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OCaml_programming_language">OCaml programming language</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML_(programming_language)">ML (programming language) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Functional_programming">Functional programming - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that an ML-family language should be the first language taught to computer scientists, though they disagree on which language to teach to non-CS students (Python, R, or Java). Several users shared personal experiences of struggling to transition from imperative languages like C to functional thinking, wondering whether learning OCaml first would have been easier. One user questioned whether learning new programming languages is still necessary given the rise of LLMs that can write code.

**Tags**: `#ocaml`, `#functional-programming`, `#programming-education`, `#computer-science`, `#pedagogy`

---

<a id="item-11"></a>
## [AMD BC-250 Mining Board Repurposed as a Budget Gaming PC (2025)](https://devquasar.com/hardware/the-60-gaming-pc-amd-bc-250/) ⭐️ 6.0/10

A guide explores building a gaming PC from an AMD BC-250 cryptocurrency mining board by flashing a modded BIOS that unlocks disabled GPU compute units (24→40) and CPU cores (6→8), based on the cut-down PS5 APU codenamed 'Oberon' / 'Cyan Skillfish'. This project demonstrates creative repurposing of surplus crypto-mining hardware during the post-mining market downturn, potentially giving hobbyists a way to build a functional gaming machine at the cost of bare components. It also illustrates how headlines about ultra-cheap PCs often omit significant hidden costs. The BC-250 is a cut-down PS5 APU, and the BIOS mod is essentially a silicon lottery — success depends on the specific board — and the build also requires an ATX PSU, NVMe drive, high-pressure fan, DP-to-HDMI adapter, and often a 3D-printed case. For AI workloads, the board offers only 12–14 GB of VRAM and a bottlenecked PCIe 2.0 x2 connection, making it unsuitable for serious LLM inference.

hackernews · networked · Sep 5, 13:36 · [Discussion](https://news.ycombinator.com/item?id=49576386)

**Background**: During the 2021–2022 cryptocurrency boom, manufacturers like AMD produced specialized 'mining' boards (such as the BC-250) that stripped down consumer chips to the bare essentials needed for hashing, disabling most display outputs and locking CPU/GPU cores. After the crypto crash, these boards flooded the second-hand market at low prices, attracting hobbyists who attempted to re-enable disabled features through custom firmware. BIOS modding on AMD GPUs and APUs involves rewriting the chip's firmware to change power limits, enable disabled execution units, and alter memory timings, but it carries risks such as bricking the hardware if done incorrectly.

<details><summary>References</summary>
<ul>
<li><a href="https://elektricm.github.io/amd-bc250-docs/hardware/specifications/">Specifications - AMD BC250 Documentation</a></li>
<li><a href="https://github.com/elektricM/amd-bc250-docs/blob/main/docs/hardware/specifications.md">amd-bc250-docs/docs/hardware/specifications.md at main ...</a></li>

</ul>
</details>

**Discussion**: The community largely dismissed the $60 premise — multiple builders reported paying $150–$300+ just for the board, with one warning that 'you are not getting one of these for less than $300' and cautioning that viral posts have spawned scams selling 3D-printed cases at inflated prices. Real-world builders confirmed the BIOS unlock works but described it as 'hacky' and silicon-lottery dependent, though those who won the lottery reported respectable gaming performance competitive with a Steam Machine. Alternative suggestions pointed to buying 'untested' Dell Optiplex office PCs for genuine budget builds.

**Tags**: `#hardware-hacking`, `#budget-pc`, `#amd`, `#bios-modding`, `#cryptocurrency-repurposing`

---

<a id="item-12"></a>
## [Acemagic Unveils F2A and F7A Mini PCs With Intel Panther Lake and AMD Gorgon Point](https://www.techpowerup.com/352386/acemagic-shows-f2a-and-f7a-mini-pcs-with-intel-panther-lake-and-amd-gorgon-point-options) ⭐️ 5.5/10

At IFA 2026, Acemagic showcased its F2A and F7A mini PCs, with the F2A available in both Intel Core Ultra X7 358H (Panther Lake) and AMD Ryzen AI 9 HX 470 (Gorgon Point) variants. Both ship with 32 GB of onboard LPDDR5X memory, but differ in storage expansion (Intel offers PCIe 5.0 x4 plus PCIe 4.0; AMD offers two PCIe 4.0 x4 interfaces). This is one of the first public demonstrations of Panther Lake silicon in a finished consumer mini PC, signaling that Intel's next-gen tile-based mobile architecture is nearing retail availability. The side-by-side offering against AMD's Gorgon Point refresh gives buyers a direct comparison of competing AI PC platforms in the same chassis. The Intel Core Ultra X7 358H is a 16-core/16-thread part reaching 4.8 GHz with Arc B390 integrated graphics and a combined AI throughput of 180 TOPS. The AMD Ryzen AI 9 HX 470 features 12 cores/24 threads with a 5.2 GHz boost, Radeon 890M iGPU on RDNA 3.5, an XDNA 2 NPU delivering up to 55 TOPS, and a platform total of 86 TOPS.

rss · TechPowerUp News · Sep 5, 15:49

**Background**: Intel Panther Lake is the company's next-generation mobile architecture after Meteor Lake and Arrow Lake, and the first to fully implement Intel's tile-based design with mixed process nodes. AMD's Gorgon Point (Ryzen AI 9 HX 470) is essentially a higher-clocked refresh of the existing Strix Point (HX 375) silicon with an updated XDNA 2 NPU for on-device AI acceleration. Both platforms are aimed at the Copilot+ PC market, where neural processing unit (NPU) TOPS ratings have become a key marketing metric for qualifying as a modern AI PC.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/343070/amd-ryzen-ai-9-hx-470-gorgon-point-apu-12c-24t-and-5-25-ghz-boost">AMD Ryzen AI 9 HX 470 "Gorgon Point" APU: 12C/24T and 5.25 GHz Boost | TechPowerUp</a></li>
<li><a href="https://acemagic.uk/blogs/buying-guide/intel-nova-lake-vs-arrow-lake-vs-panther-lake">Intel Nova Lake vs Arrow Lake vs Panther Lake : Which Mini PC CPU...</a></li>
<li><a href="https://www.amd.com/en/technologies/xdna.html">AMD XDNA™ Architecture</a></li>

</ul>
</details>

**Tags**: `#mini-pc`, `#intel-panther-lake`, `#amd-gorgon-point`, `#ifa-2026`, `#hardware`

---

<a id="item-13"></a>
## [GEEKOM's A9 Mega Mini PCs Form Local Inference Cluster at IFA 2026](https://www.techpowerup.com/352383/geekoms-a9-mega-mini-pcs-form-local-inference-cluster-at-ifa-2026) ⭐️ 5.5/10

GEEKOM demonstrated at IFA 2026 a local AI inference cluster built by interconnecting four A9 Mega mini PCs via USB4, each featuring AMD Ryzen AI Max+ 395 with up to 128GB unified memory, creating a desk-sized private supercomputer for local AI workloads.

rss · TechPowerUp News · Sep 5, 15:01

**Tags**: `#edge-ai`, `#local-inference`, `#mini-pc`, `#amd-ryzen`, `#hardware`

---

<a id="item-14"></a>
## [Modder gets Nvidia's DLSS 5 working on AMD's RDNA 4 GPUs — RX 9070 XT only manages 30 FPS at 1080p right now, but 5070 Ti-level performance is the eventual goal](https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-on-amds-rdna-4-gpus-rx-9070-xt-only-manages-30-fps-at-1080p-right-now-but-5070-ti-level-performance-is-the-eventual-goal) ⭐️ 5.5/10

A modder has gotten Nvidia's DLSS 5 upscaling working on AMD's RDNA 4 GPUs (RX 9070 XT), though current performance is limited to 30 FPS at 1080p with the eventual goal of matching RTX 5070 Ti performance.

rss · Tom's Hardware · Sep 5, 12:00

**Tags**: `#gpu`, `#dlss`, `#amd`, `#nvidia`, `#modding`

---

<a id="item-15"></a>
## [Tom's Hardware Benchmarks DLSS 5 in NBA 2K27 Across All RTX 50-Series GPUs](https://www.tomshardware.com/video-games/pc-gaming/we-tested-dlss-5-in-nba-2k27-with-every-rtx-50-series-gpu-first-official-release-comes-with-a-big-performance-hit-but-almost-every-blackwell-card-can-run-it-at-1080p) ⭐️ 5.5/10

Tom's Hardware tested Nvidia's DLSS 5 neural rendering in NBA 2K27 across the entire RTX 50-series lineup at 1080p, 1440p, and 4K. Results show a notable performance cost from enabling DLSS 5, but nearly every Blackwell GPU can still deliver playable framerates at 1080p. This is one of the first real-world performance benchmarks of DLSS 5, Nvidia's neural rendering technology, giving PC gamers practical data on whether upgrading is worthwhile. It also signals a shift in GPU workloads — neural rendering demands significant AI compute and tests the limits of even high-end Blackwell cards. DLSS 5 differs from prior DLSS versions: instead of upscaling or frame generation, it uses a large AI model to analyze faces, materials, and lighting in real time and re-shade frames, running on RTX tensor cores and optimized for RTX 50-series hardware. The RTX 50-series itself debuted in January 2025 using Nvidia's Blackwell architecture, built specifically for neural rendering workloads.

rss · Tom's Hardware · Sep 5, 11:00

**Background**: DLSS (Deep Learning Super Sampling) is Nvidia's suite of AI-driven graphics technologies, evolving from simple upscaling in DLSS 2 to frame generation in DLSS 3 and 4. DLSS 5, announced in March 2026, marks a leap to full neural rendering — where an AI model replaces or augments traditional shading to produce photorealistic lighting and materials. The RTX 50-series GPUs, powered by Nvidia's Blackwell architecture announced at CES 2025, include dedicated hardware for AI tensor operations that neural rendering requires.

<details><summary>References</summary>
<ul>
<li><a href="https://tbreak.com/nvidia-dlss-5-neural-rendering-explained/">DLSS 5 Explained: How Nvidia's Neural Renderer Actually Works</a></li>
<li><a href="https://en.wikipedia.org/wiki/GeForce_RTX_50_series">GeForce RTX 50 series - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#dlss-5`, `#rtx-50-series`, `#gpu-benchmarking`, `#pc-gaming`

---

<a id="item-16"></a>
## [Japan to mass-procure 3D-printed rocket-powered drone interceptor — Terra B1 capable of countering one-way attack platforms](https://www.tomshardware.com/tech-industry/drones/japan-to-mass-procure-3d-printed-rocket-powered-drone-interceptor-terra-b1-capable-of-countering-one-way-attack-platforms) ⭐️ 5.5/10

Japan's military is mass-procureing Terra B1, a 3D-printed rocket-powered interceptor drone based on a model already deployed by Ukraine for countering one-way attack drones.

rss · Tom's Hardware · Sep 5, 10:00

**Tags**: `#drones`, `#defense-technology`, `#3d-printing`, `#military-procurement`, `#counter-drone`

---