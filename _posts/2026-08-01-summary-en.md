---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
---

> From 110 items, 20 important content pieces were selected

---

1. [Tailscale Posts Transparent Post-Mortem on Hugging Face Intrusion via Leaked Auth Key](#item-1) ⭐️ 8.0/10
2. [CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits](#item-2) ⭐️ 8.0/10
3. [Zoox becomes first company approved for truly driverless robotaxi service](#item-3) ⭐️ 8.0/10
4. [Intel's EMIB-T to Rival TSMC's CoWoS with 50% Cost Advantage](#item-4) ⭐️ 7.5/10
5. [Montage Technology Begins Trial Production of CXL 3.2 MXC Chip](#item-5) ⭐️ 7.5/10
6. [Lumentum CEO Warns Indium Phosphide Shortage Will Eclipse Memory Crisis](#item-6) ⭐️ 7.5/10
7. [Valve Funds Port of Open-Source RADV Vulkan Driver to Windows](#item-7) ⭐️ 7.5/10
8. [EU AI Act Enforcement Begins August 2 with New Transparency Requirements](#item-8) ⭐️ 7.3/10
9. [CrossOver Announces Native Apple Silicon Support for Windows Games](#item-9) ⭐️ 7.3/10
10. [Interactive Exploration of Elevator Scheduling Algorithms](#item-10) ⭐️ 7.0/10
11. [qm – Multiplayer agent harness for work](#item-11) ⭐️ 7.0/10
12. [Golang Proposal: Generic Collection Types for container/ Package](#item-12) ⭐️ 7.0/10
13. [The Difference Between CoWoS-S and CoWoS-R](#item-13) ⭐️ 7.0/10
14. [Big tech spends more than $1 trillion on AI infrastructure — additional $745 billion expected to be added to the figure in 2026 alone](#item-14) ⭐️ 6.5/10
15. [Browser-Based Streaming QR Codes Transfer Data at ~190 KB/s](#item-15) ⭐️ 6.5/10
16. [Single-DIMM DDR5 gaming works better than you probably think — one DDR5 DIMM beats dual-channel DDR4 RAM, AMD's 3D V-Cache chips drop less than 3% with single stick](#item-16) ⭐️ 6.5/10
17. [Most Motherboard M.2 SSD Heatsinks Fail to Make Proper Contact](#item-17) ⭐️ 6.5/10
18. [MSI High-Efficiency Mode Adds EXPO ULL-Style Tuning to Existing DDR5](#item-18) ⭐️ 6.5/10
19. [最前线｜武汉建成全国首个超大城市全域低空遥感监测网络，146座无人机机场构建“城市智眼”](#item-19) ⭐️ 6.3/10
20. [电投产融：山东莱阳核电项目获国务院常务会议核准](#item-20) ⭐️ 6.3/10

---

<a id="item-1"></a>
## [Tailscale Posts Transparent Post-Mortem on Hugging Face Intrusion via Leaked Auth Key](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 8.0/10

Tailscale published a detailed post-mortem of the Hugging Face security intrusion, revealing that a leaked reusable Tailscale auth key — one of 136 stolen credentials — was used over several days by an attacker to enroll 181 malicious nodes into Hugging Face's tailnet, each receiving CI-level access. Despite no vulnerability in Tailscale's product being found, the company treated the incident as their own responsibility. This incident highlights the dangers of long-lived, broadly scoped credentials like reusable auth keys, and sets a notable precedent for security vendors taking accountability even when their tooling isn't at fault. It reinforces best practices around scoping, rotation, and monitoring of machine identities in CI/CD and sandbox environments. The 181 malicious nodes each carried a Tailscale identity tag granting full CI node access, meaning the auth key was effectively unscoped. Tailscale recommends tighter scoping (e.g., binding keys to specific machine tags or properties), shorter credential lifetimes, and alerting on anomalous node enrollment patterns.

hackernews · bluehatbrit · Jul 31, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49127306)

**Background**: Tailscale is a zero-configuration mesh VPN built on top of WireGuard that allows devices to connect securely without complex network setup. Auth keys are Tailscale's mechanism for registering new nodes without interactive login — they come in one-time-use and reusable variants, with reusable keys designed for scenarios like CI pipelines that provision multiple ephemeral machines. Hugging Face is a major AI/ML platform hosting models, datasets, and applications, and it runs CI/CD infrastructure to test and validate contributions at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailscale">Tailscale - Wikipedia</a></li>
<li><a href="https://tailscale.com/docs/features/access-control/auth-keys">Auth keys · Tailscale Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment was largely positive, with users praising Tailscale's transparency and willingness to publish a post-mortem despite no product vulnerability being involved. Simon Willison highlighted that enrolling 181 nodes over several days represents a clear alerting opportunity, while angry_octet pointed out that long-lived credentials should have been bound to origin/destination and scoped to specific machine properties like 'ci_node'. Some skeptics, like ahofmann, viewed the post partly as 'smart marketing' — but even critics acknowledged the rare level of accountability shown.

**Tags**: `#security`, `#incident-response`, `#vpn`, `#credentials`, `#post-mortem`

---

<a id="item-2"></a>
## [CEA-Leti Pushes Stacking Roadmap as AI Runs Into Memory and Power Limits](https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/) ⭐️ 8.0/10

CEA-Leti outlines its 3D stacking and chiplet roadmap to address the memory and power bottlenecks limiting AI compute scaling.

rss · EE Times · Jul 31, 15:48

**Tags**: `#AI hardware`, `#3D stacking`, `#chiplets`, `#semiconductor packaging`, `#memory wall`

---

<a id="item-3"></a>
## [Zoox becomes first company approved for truly driverless robotaxi service](https://www.electronicsweekly.com/news/business/first-genuine-driverless-2026-07/) ⭐️ 8.0/10

Amazon's Zoox has become the first company to receive regulatory approval to deploy genuinely driverless robotaxis, with a license allowing it to deploy up to 2,500 vehicles annually over a two-year period in the United States. This represents a landmark regulatory milestone for the autonomous vehicle industry, moving beyond earlier limited-area driverless services toward broader commercial deployment of vehicles without any human operator on board. Zoox's vehicle features a unique bidirectional, symmetrical design with no steering wheel and carriage-style seating for up to four passengers, equipped with a 360-degree sensor suite and a custom airbag system. The approval still operates within a defined operational design domain (ODD) rather than unrestricted Level 5 autonomy.

rss · Electronics Weekly · Jul 31, 05:10

**Background**: SAE defines six levels of vehicle automation, from Level 0 (no automation) to Level 5 (full autonomy in all conditions without geofencing). Zoox's approval corresponds to Level 4, where the vehicle drives itself within a defined area or under specific conditions, eliminating the need for a human driver. In the US, the National Highway Traffic Safety Administration (NHTSA) grants exemptions from Federal Motor Vehicle Safety Standards (FMVSS) for vehicles that don't comply with traditional requirements like having a steering wheel or pedals. Waymo pioneered commercial driverless rides in 2020 within limited geographic areas, but Zoox's approval is distinguished by its purpose-built vehicle design without any manual controls.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nvidia-zoox-autonomous-ride-hailing/">NVIDIA and Zoox Pave the Way for Autonomous Ride-Hailing | NVIDIA Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-driving_car">Self-driving car - Wikipedia</a></li>
<li><a href="https://www.usatoday.com/story/cars/research/reviews/2026/05/11/zoox-vs-waymo-tesla-amazon-robotaxi-differences/89981647007/">We tried Zoox, Amazon's robotaxi. How it stands out compared to Waymo, Tesla</a></li>

</ul>
</details>

**Tags**: `#autonomous-vehicles`, `#robotaxi`, `#Zoox`, `#regulation`, `#Amazon`

---

<a id="item-4"></a>
## [Intel's EMIB-T to Rival TSMC's CoWoS with 50% Cost Advantage](https://www.techpowerup.com/351274/intels-emib-t-to-rival-tsmcs-cowos-with-50-cost-advantage-volume-production-in-2027) ⭐️ 7.5/10

Intel's EMIB-T advanced packaging variant, which incorporates Through-Silicon Vias (TSVs), is reportedly attracting external customers including Broadcom and Meta who are considering switching from TSMC's CoWoS to EMIB to reduce costs by as much as 50%. According to Taiwan-based PCB and silicon substrate maker Unimicron, Intel's EMIB-T will enter high-volume production in 2027, while Intel continues ramping its standard EMIB and Foveros offerings in the interim. This development directly addresses the advanced packaging bottleneck that has constrained AI chip supply, as CoWoS capacity at TSMC has become a binding constraint for AI accelerator deliveries. If EMIB-T delivers on its cost promise at scale, it could provide ASIC designers and hyperscalers with a viable alternative supply source, potentially reshaping pricing dynamics across the AI infrastructure supply chain. The EMIB-T variant specifically includes TSVs that allow ASICs to directly access power connections, enabling multi-kilowatt solutions on a single package — a critical capability for AI accelerators paired with high-bandwidth memory (HBM). The 50% cost gap compared to CoWoS-L or CoWoS-R depends on whether an expensive interposer is required, since EMIB uses localized silicon bridges rather than a full-size interposer.

rss · TechPowerUp News · Jul 31, 17:51

**Background**: Advanced packaging is the process of combining multiple chip dies (chiplets) and high-bandwidth memory into a single finished unit, and it has become as critical as leading-edge wafer fabrication for AI processors. TSMC's CoWoS (Chip-on-Wafer-on-Substrate) is currently the dominant technology for combining AI accelerator dies with HBM stacks, and its limited capacity has created supply bottlenecks. Intel's EMIB (Embedded Multi-die Interconnect Bridge) is a competing 2.5D approach that embeds small silicon bridges into the package substrate for localized high-density die-to-die routing, avoiding the cost and area penalty of a full silicon interposer. Through-Silicon Vias (TSVs) are vertical electrical connections that pass completely through a silicon die, enabling 3D stacking and direct power delivery.

<details><summary>References</summary>
<ul>
<li><a href="https://semiwiki.com/wikis/industry-wikis/intel-emib-embedded-multi-die-interconnect-bridge/">Intel EMIB (Embedded Multi-die Interconnect Bridge) - Semiwiki</a></li>
<li><a href="https://www.techtimes.com/articles/321754/20260728/ai-supply-crisis-moves-upstream-advanced-packaging-becomes-binding-constraint.htm">AI Supply Crisis Moves Upstream: Advanced Packaging Becomes the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Through-silicon_via">Through - silicon via - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#advanced-packaging`, `#Intel`, `#TSMC`, `#AI-infrastructure`

---

<a id="item-5"></a>
## [Montage Technology Begins Trial Production of CXL 3.2 MXC Chip](https://www.techpowerup.com/351268/montage-technology-enters-trial-production-of-cxl-3-2-mxc-chip-supporting-8000-mt-s-ddr5) ⭐️ 7.5/10

Montage Technology has started the industry's first trial production of a CXL 3.2 Memory eXpander Controller (MXC) chip that complies with CXL Type 3 specifications and supports both CXL.mem and CXL.io protocols. The chip integrates dual DDR5 memory controllers supporting up to 8000 MT/s DDR5 and delivers 64 GT/s data transfer rates via PCIe 6.x. This is the first commercially aimed CXL 3.2 MXC chip to reach trial production, giving Montage a first-mover position in enabling next-generation memory expansion for AI and data center workloads where memory capacity and bandwidth are critical bottlenecks. The combination of CXL 3.2, PCIe 6.x, and 8000 MT/s DDR5 addresses the growing need for memory pooling, disaggregation, and resource sharing in hyperscale and AI infrastructure. The MXC acts as a bridge, converting host-side CXL memory requests into DDR commands in real time to break through traditional server memory capacity limits. While the announcement covers trial production, no specific volume, customer, or general availability timeline was disclosed, and as a press release it lacks independent benchmark data.

rss · TechPowerUp News · Jul 31, 15:07

**Background**: Compute Express Link (CXL) is a high-speed interconnect standard built on PCIe that enables coherent memory sharing between CPUs and accelerators or attached devices. CXL Type 3 devices specifically provide memory expansion and pooling capabilities, allowing servers to access additional DRAM beyond their direct-attached limits. The CXL 3.2 specification was released by the CXL Consortium in December 2024, adding security and functional enhancements for CXL memory devices while remaining backward compatible. Montage Technology was already a pioneer in this space as the first company to introduce a CXL Type 3 memory expander controller, and this new chip extends its lead to the CXL 3.2 generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.montage-tech.com/MXC">CXL® Memory eXpander Controller ( MXC ) | Montage Technology</a></li>
<li><a href="https://computeexpresslink.org/wp-content/uploads/2024/12/CXL_3.2-Spec-Announcement_FINAL-1.pdf">CXL Consortium Announces Compute Express Link 3 . 2 Specication...</a></li>
<li><a href="https://www.design-reuse.com/news/202529287-cxl-3-1-mxc-and-the-future-of-data-center-memory-architecture/">CXL 3.1 MXC and the Future of Data Center Memory Architecture</a></li>

</ul>
</details>

**Tags**: `#CXL`, `#DDR5`, `#data-center`, `#memory-expansion`, `#AI-infrastructure`

---

<a id="item-6"></a>
## [Lumentum CEO Warns Indium Phosphide Shortage Will Eclipse Memory Crisis](https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory) ⭐️ 7.5/10

At the RAISE Summit, Lumentum CEO Michael Hurlston warned that indium phosphide (InP), a critical material for silicon photonics, is heading into a supply squeeze worse than the ongoing memory shortage, with current production capacity already running approximately 30% below customer demand as co-packaged optics adoption accelerates. This warning directly threatens the scaling of AI infrastructure, as co-packaged optics are increasingly essential for high-bandwidth, low-power data transmission between AI accelerators and switches. A bottleneck in InP wafers could constrain the buildout of next-generation data centers at a time when AI compute demand is exploding. The CEO's statement places the InP shortfall on par with or exceeding the well-documented memory supply crisis, and the warning specifically cites fab and material capacity as the bottleneck rather than demand-side issues. Lumentum is one of the largest suppliers of InP-based lasers and photonic components, making this a first-party assessment from a key node in the supply chain.

rss · Tom's Hardware · Jul 31, 12:45

**Background**: Indium phosphide (InP) is a III-V compound semiconductor used as a substrate for high-speed optoelectronic devices, including laser diodes and photodetectors that operate efficiently at the wavelengths needed for optical communication. Silicon photonics leverages these InP-based light sources alongside silicon waveguides to enable optical data transmission on and between chips. Co-packaged optics (CPO) is an emerging architecture that integrates the optical engine directly with a switch ASIC or compute chip (such as an AI accelerator) inside the same package, dramatically improving bandwidth density and energy efficiency compared to traditional pluggable optical transceivers — making it critical for scaling AI data center interconnects.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indium_phosphide">Indium phosphide - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Silicon_photonics">Silicon photonics - Wikipedia</a></li>
<li><a href="https://www.corning.com/optical-communications/worldwide/en/home/the-signal-network-blog/corning-and-broadcom-co-packaged-optics.html">Unlock the Future of AI | Co - Packaged Optics ( CPO )... | Corning</a></li>

</ul>
</details>

**Tags**: `#silicon-photonics`, `#supply-chain`, `#semiconductors`, `#co-packaged-optics`, `#AI-infrastructure`

---

<a id="item-7"></a>
## [Valve Funds Port of Open-Source RADV Vulkan Driver to Windows](https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2) ⭐️ 7.5/10

Valve is funding the port of the open-source Linux RADV Radeon Vulkan driver from the Mesa project to Windows. The cross-platform build is already functional enough to run Counter-Strike 2. This represents a significant push toward cross-platform open-source GPU drivers, potentially reducing duplication between Mesa and Windows graphics stacks. It could benefit AMD Radeon GPU users on Windows by offering an open-source driver alternative to AMD's proprietary Adrenalin software and underscores Valve's ongoing commitment to open graphics. RADV is a userspace driver compiled as a shared library — libvulkan_radeon.so on Linux, equivalent to a .dll on Windows — and supports AMD GCN/RDNA GPUs with full Vulkan API support. The fact that Counter-Strike 2 already runs on the Windows port demonstrates real-world viability of the cross-platform effort.

rss · Tom's Hardware · Jul 31, 12:25

**Background**: RADV is the open-source Vulkan driver for AMD Radeon GPUs, developed as part of the Mesa 3D Graphics Library, a long-standing open-source project that implements graphics APIs including OpenGL, Vulkan, OpenCL, and Direct3D. Vulkan itself is a low-level graphics API designed to provide higher performance and more efficient CPU/GPU utilization compared to older APIs such as OpenGL and DirectX 11. AMD users on Windows currently rely primarily on AMD's proprietary Adrenalin driver, whereas Linux users have access to both AMD's official AMDVLK driver and the open-source RADV driver. This porting effort aims to unify driver development across platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.mesa3d.org/drivers/radv.html">RADV — The Mesa 3D Graphics Library latest documentation</a></li>
<li><a href="https://wccftech.com/mesa-radv-vulkan-driver-amd-radeon-gpus-vulkan-video-h264-h265-encode-support/">MESA RADV Vulkan Driver For AMD Radeon GPUs Gets Vulkan ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulkan">Vulkan - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Vulkan`, `#RADV`, `#Mesa`, `#Valve`, `#open-source-drivers`

---

<a id="item-8"></a>
## [EU AI Act Enforcement Begins August 2 with New Transparency Requirements](https://36kr.com/newsflashes/3919473270812290?f=rss) ⭐️ 7.3/10

The European Commission announced on July 31 that from August 2, its AI Office will jointly begin enforcing provisions of the EU AI Act alongside national authorities of member states. New transparency rules require interactive AI systems such as chatbots to clearly disclose their AI identity to users, while deepfake images, videos, and audio generated or edited by AI must be labeled and carry machine-readable markers for identification and traceability. This marks a concrete enforcement milestone for the world's most comprehensive AI regulation, immediately affecting AI developers and companies deploying systems in the EU regardless of where they are headquartered. The transparency mandates aim to combat deception and manipulation while establishing a global benchmark that may influence AI governance approaches in other jurisdictions. The transparency obligations under Article 50 require machine-readable markers such as watermarks or metadata schemas like C2PA, allowing algorithmic identification of AI-generated content rather than relying solely on visual disclosure. The risk-based framework of the AI Act classifies systems into four risk tiers, and these August 2 provisions primarily target transparency for general-purpose AI interactions and synthetic media.

rss · 36氪 · Jul 31, 11:45

**Background**: The EU AI Act is the world's first comprehensive horizontal regulation governing artificial intelligence, taking a risk-based approach that categorizes AI systems into four levels of risk with corresponding obligations. Article 50 specifically addresses transparency obligations for providers of AI systems that interact with people, generate synthetic content, or enable deepfake creation. Tools such as Google's SynthID and the C2PA content provenance standard provide technical mechanisms for embedding machine-readable markers into AI-generated media, and several such standards are expected to become widely adopted as compliance solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/">Artificial intelligence act - Consilium</a></li>
<li><a href="https://sota.io/blog/eu-ai-act-art50-transparency-watermarking-developer-guide-2026">EU AI Act Art.50 Transparency & Watermarking ... — sota.io Blog</a></li>
<li><a href="https://www.pragma-code.de/en/blog-synthid-ai-watermarking-content-provenance">SynthID & Co: AI Watermarking & Content ... | Pragma-Code Blog</a></li>

</ul>
</details>

**Tags**: `#EU AI Act`, `#AI Regulation`, `#AI Transparency`, `#Compliance`, `#Policy`

---

<a id="item-9"></a>
## [CrossOver Announces Native Apple Silicon Support for Windows Games](https://www.solidot.org/story?sid=84978) ⭐️ 7.3/10

CrossOver has released the first preview of native Apple Silicon support for running x86 Windows games on macOS, marking a milestone six years after Apple Silicon's debut. Separately, Arch Linux has shut down AUR orphaned package adoption after attackers compromised more than 400 packages via the normal adoption process to deploy malware. The CrossOver release comes just as Apple prepares to retire Rosetta 2 in macOS 28, which would otherwise leave Mac users without a path to play Windows games natively. The Arch Linux AUR incident highlights ongoing supply-chain risks in community-maintained software repositories, prompting stricter moderation policies. The preview still has rough edges and is recommended only for testing; because the ARM64 build of D3DMetal is not ready, DirectX 11 games currently only run via DXMT ARM64. These issues are expected to be resolved in the full CrossOver 27 release. CodeWeavers, the company behind CrossOver, contributes over 90% of Wine's code and also develops Proton for Steam.

rss · Solidot · Jul 31, 14:32

**Background**: Wine is an open-source compatibility layer that, unlike virtual machines, translates Windows API calls directly to the host OS at runtime, enabling Windows games to run on Linux and macOS. Apple's Rosetta 2 has historically translated x86 software for ARM-based Macs, but Apple Silicon-specific translation layers like D3DMetal and DXMT map Direct3D calls to Apple's Metal graphics API for better performance. The Arch User Repository (AUR) is a community-driven repository of user-submitted build scripts (PKGBUILDs) for Arch Linux, where any registered user can adopt orphaned packages—a trust model that was exploited in this attack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.solidot.org/story?sid=84978">奇客Solidot | Windows 游戏模拟器 CrossOver 宣布原生 Apple Silicon ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/400-aur-packages-hijacked-atomic-arch-campaign">400+ AUR Packages Hijacked: What the “Atomic Arch ”... - StepSecurity</a></li>
<li><a href="https://secure-os.org/articles/is-the-aur-safe/">Is the AUR Safe? Lessons from the 'Atomic Arch ' Supply - Chain ...</a></li>
<li><a href="https://j0.lol/blog/kegworks-winery/">How to run games on macOS like it's SteamOS</a></li>

</ul>
</details>

**Tags**: `#CrossOver`, `#Apple Silicon`, `#Wine`, `#macOS`, `#Arch Linux`, `#supply-chain-security`

---

<a id="item-10"></a>
## [Interactive Exploration of Elevator Scheduling Algorithms](https://john.fun/elevators) ⭐️ 7.0/10

The article at john.fun/elevators provides an interactive visualization of elevator scheduling algorithms, sparking a highly engaged discussion (901 points, 223 comments) where commenters draw connections between elevator logic and disk scheduling, share real-world experiences with destination dispatch systems, and recommend educational tools like Elevator Saga. Elevator scheduling is a classic computer science problem that elegantly illustrates how queue management and request ordering affect real-world systems. The rich cross-domain discussion (linking elevators to disk drives, game design, and building infrastructure) makes it an unusually effective teaching vehicle for algorithmic thinking. Key algorithms covered include FCFS, SSTF, SCAN, LOOK, and C-SCAN, which originated in disk-scheduling research but map directly onto elevator behavior. The SCAN algorithm works by moving in one direction servicing requests before reversing, while LOOK improves efficiency by stopping at the last request rather than reaching the disk end.

hackernews · Jrh0203 · Jul 31, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49124218)

**Background**: The elevator algorithm (also called SCAN) was originally a disk-scheduling strategy where a disk arm moves back and forth servicing read/write requests, much like an elevator servicing floor calls. Common variants include LOOK (which reverses at the last request instead of the end of the disk) and C-SCAN (which always returns to the beginning for fairer service). Destination Dispatch is a modern elevator technology where passengers select their floor at a lobby kiosk and are grouped into specific cars, rather than pressing buttons inside the elevator.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elevator_algorithm">Elevator algorithm - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/operating-systems/disk-scheduling-algorithms/">Disk Scheduling Algorithms - GeeksforGeeks</a></li>
<li><a href="https://medium.com/@dmkaban62/diving-into-go-implementing-classic-elevator-scheduling-algorithms-fcfs-sstf-scan-and-look-4040c2de62f2">Diving into Go: Implementing Classic Elevator Scheduling ... | Medium</a></li>

</ul>
</details>

**Discussion**: The community discussion is substantive and cross-disciplinary. Commenter peterldowns drew a vivid analogy between HDDs and long wrapped elevators, noting that SCAN is a disk-scheduling algorithm. Omoikane offered real-world experience with destination dispatch in office buildings, questioning whether simulation results depend on traffic patterns. Brandonpelfrey shared Elevator Saga as a hands-on programming exercise. Hermanschaaf described developing Sky Lobby (a mobile game about elevator automation) and choosing LOOK as the most intuitive default. Olex humorously noted that the hardest part of elevator design is users pressing both up and down buttons.

**Tags**: `#algorithms`, `#simulation`, `#computer-science`, `#elevator`, `#education`

---

<a id="item-11"></a>
## [qm – Multiplayer agent harness for work](https://github.com/yc-software/qm) ⭐️ 7.0/10

A YC-backed open-source harness for orchestrating multiple AI agents collaboratively on workplace tasks, entering the crowded multiplayer agent space alongside tools like Cowork and Buzz.

hackernews · tosh · Jul 31, 18:04 · [Discussion](https://news.ycombinator.com/item?id=49126604)

**Tags**: `#ai-agents`, `#multi-agent-systems`, `#developer-tools`, `#yc`, `#agent-orchestration`

---

<a id="item-12"></a>
## [Golang Proposal: Generic Collection Types for container/ Package](https://github.com/golang/go/issues/80590) ⭐️ 7.0/10

A new Go proposal (issue #80590) suggests adding generic collection types—such as sets and typed heaps—to the standard library's container/ package. This would fill a long-standing gap left since generics were introduced in Go 1.18, providing built-in typed data structures instead of relying on third-party implementations. This matters because Go developers have long needed standard-library support for common generic data structures and have been forced to use third-party packages or write their own. Adding these types to the standard library would reduce fragmentation, improve consistency, and signal a more mature generics ecosystem within Go. The proposal specifically targets the container/ directory, which currently includes only `list`, `ring`, and `heap`—all of which predate generics and rely on `interface{}` or `any`. The discussion has 128 upvotes and 78 comments, indicating strong community interest in shaping the API design and naming conventions for these new types.

hackernews · jabits · Jul 31, 18:39 · [Discussion](https://news.ycombinator.com/item?id=49127031)

**Background**: Go introduced generics (type parameters) in version 1.18, released in March 2022, allowing developers to write type-safe, reusable code without sacrificing performance. However, the standard library's container/ package—home to data structure implementations—predates generics and still uses non-generic interfaces. Common data structures like sets have no built-in implementation, forcing developers to use third-party libraries such as `golang-set`. The container/ package currently contains `container/list` (doubly linked list), `container/ring` (circular list), and `container/heap` (a heap requiring user-implemented interfaces).

<details><summary>References</summary>
<ul>
<li><a href="https://pkg.go.dev/container">container / directory - container - Go Packages</a></li>
<li><a href="https://www.sobyte.net/post/2022-04/golang-container/">Go container package - SoByte</a></li>
<li><a href="https://blog.marcnuri.com/go-generics-introduction">Go Generics Tutorial: A Complete Introduction to Type Parameters ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive but tinged with frustration about how long this has taken, with one commenter calling it '22 years late.' Several users expressed approval but noted design concerns, such as not mixing mutation methods into the API. There is also broader discussion about whether Go's current generics implementation is sufficient or whether a future 'Go v2' needs more foundational changes to better support collections.

**Tags**: `#golang`, `#generics`, `#standard-library`, `#data-structures`, `#language-design`

---

<a id="item-13"></a>
## [The Difference Between CoWoS-S and CoWoS-R](https://semiwiki.com/semiconductor-manufacturers/tsmc/371759-the-difference-between-cowos-s-and-cowos-r/) ⭐️ 7.0/10

A comparison of TSMC's two CoWoS advanced packaging technologies (CoWoS-S and CoWoS-R) used to integrate processors, chiplets, and HBM in a single package.

rss · SemiWiki · Jul 31, 13:00

**Tags**: `#semiconductor-packaging`, `#TSMC`, `#CoWoS`, `#advanced-packaging`, `#HBM`

---

<a id="item-14"></a>
## [Big tech spends more than $1 trillion on AI infrastructure — additional $745 billion expected to be added to the figure in 2026 alone](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone) ⭐️ 6.5/10

Amazon, Google, Meta, and Microsoft have collectively spent over $1 trillion on AI infrastructure since 2023, with an additional $745 billion expected in 2026, while their hidden debt exceeds $1.65 trillion.

rss · Tom's Hardware · Jul 31, 16:30

**Tags**: `#AI infrastructure`, `#big tech`, `#capital expenditure`, `#industry trends`, `#data centers`

---

<a id="item-15"></a>
## [Browser-Based Streaming QR Codes Transfer Data at ~190 KB/s](https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access) ⭐️ 6.5/10

A developer has built a browser-based proof-of-concept that streams QR codes at 60 FPS between two phones, achieving a data transfer rate of nearly 190 KB/s without requiring any app installation, network connection, device pairing, or special permissions beyond camera access. This approach offers a zero-friction, privacy-friendly alternative for short-range data exchange, useful in environments where Wi-Fi, Bluetooth, or NFC are unavailable or undesirable (such as air-gapped settings or restricted corporate networks). It highlights the creative use of existing web APIs to bypass traditional connectivity requirements, though the throughput ceiling keeps it limited to small payloads like URLs, short text, or credentials. The implementation relies on the browser's getUserMedia API for camera access and must run in a secure (HTTPS) context to function. A standard single QR code can encode at most roughly 3 KB of binary data, so the system chains many codes together in rapid succession; the 60 FPS frame rate and roughly 190 KB/s throughput represent the practical upper bound dictated by camera exposure, decoding latency, and QR version density.

rss · Tom's Hardware · Jul 31, 12:45

**Background**: A QR (Quick Response) code is a two-dimensional barcode that can store binary or alphanumeric data in a grid of black and white modules; the largest standardized version (Version 40) can hold up to about 2,953 binary bytes per code. Because a single code has limited capacity, researchers have long explored 'streaming' or 'animated' QR codes — sequences of codes displayed like a video so a camera-equipped device can reconstruct a larger file. The browser's getUserMedia API exposes the device camera to web pages without native code, making it possible to decode these streams entirely client-side. Related open-source projects such as QiFi (qifi-dev/qrs) and Digital Bazaar's qram demonstrate prior art for streaming QR transmission pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/qifi-dev/qrs">GitHub - qifi-dev/qrs: Stream data through multiple series of QR codes</a></li>
<li><a href="https://digitalbazaar.github.io/qram/">qram | Cram arbitrarily large data into multiple streaming QR - codes</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia">MediaDevices: getUserMedia () method - Web APIs | MDN</a></li>

</ul>
</details>

**Tags**: `#data-transfer`, `#qr-codes`, `#browser-based`, `#proof-of-concept`, `#privacy`

---

<a id="item-16"></a>
## [Single-DIMM DDR5 gaming works better than you probably think — one DDR5 DIMM beats dual-channel DDR4 RAM, AMD's 3D V-Cache chips drop less than 3% with single stick](https://www.tomshardware.com/pc-components/ddr5/single-dimm-ddr5-gaming-works-better-than-you-probably-think-amds-3d-v-cache-chips-drop-less-than-3-percent-one-ddr5-dimm-beats-dual-channel-ddr4-ram) ⭐️ 6.5/10

Benchmarks show single DDR5 DIMM performs surprisingly well in gaming, often beating dual-channel DDR4, with AMD 3D V-Cache chips losing less than 3% performance on a single stick.

rss · Tom's Hardware · Jul 31, 11:43

**Tags**: `#DDR5`, `#RAM`, `#gaming-hardware`, `#AMD`, `#benchmarks`

---

<a id="item-17"></a>
## [Most Motherboard M.2 SSD Heatsinks Fail to Make Proper Contact](https://www.tomshardware.com/pc-components/motherboards/are-your-motherboards-m-2-heatsinks-making-good-contact-with-your-ssd-we-tested-20-modern-intel-and-amd-motherboards-to-verify) ⭐️ 6.5/10

Tom's Hardware tested 20 modern Intel and AMD motherboards for M.2 SSD heatsink contact quality and found that only 6 out of 20 boards achieved full thermal contact with the installed SSD. The remaining 14 boards exhibited poor contact, meaning the bundled heatsinks may not be effectively cooling the drives. Poor thermal contact can cause NVMe SSDs to thermal throttle, significantly reducing sustained write performance during heavy workloads like file transfers or content creation. This is a practical concern for PC builders and enthusiasts who assume motherboard-provided heatsinks will adequately cool their high-performance SSDs, potentially impacting both speed and drive longevity. Thermal throttling is specified in the NVMe 1.0 specification under Host Controlled Thermal Management (HCTM), and a sustained-write performance curve that drops sharply after 10–60 seconds is a typical indicator. The quality and thickness of thermal pads, as well as heatsink design tolerances, are critical factors; a poor-quality or incorrectly sized thermal pad can actually insulate the drive instead of cooling it.

rss · Tom's Hardware · Jul 31, 11:43

**Background**: M.2 NVMe SSDs are compact, high-speed storage devices that can generate significant heat during sustained write operations. To manage this, the NVMe 1.0 specification introduced Host Controlled Thermal Management (HCTM), which allows drives to throttle performance when temperatures exceed safe thresholds. Motherboards typically include heatsinks with thermal pads to dissipate this heat, but proper contact between the SSD's controller/NAND chips and the heatsink is essential for effective cooling. Inadequate contact caused by mismatched thermal pad thickness or poor heatsink design can leave SSDs running hotter than intended.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hagisol.com/techblog/?p=635">How NVMe SSD thermal throttling works HAGIWARA Solutions</a></li>
<li><a href="https://voltground.com/hardware/nvme-ssd-thermal-throttling/">NVMe SSD Thermal Throttling : How to Detect It, What... — VoltGround</a></li>
<li><a href="https://www.yourtechlist.com/best-m2-heatsinks/">10 Best M.2 Heatsinks For (August 2026)</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight user concerns about thermal pad installation, including whether to remove factory thermal stickers before installing motherboard heatsinks, and the use of rubber spacers for single-sided M.2 drives. Enthusiasts emphasize that the thermal interface material is just as important as the heatsink itself, and recommend quality thermal pads from reputable manufacturers to avoid insulating rather than cooling the drive.

**Tags**: `#hardware`, `#motherboards`, `#M.2 SSD`, `#thermal performance`, `#PC building`

---

<a id="item-18"></a>
## [MSI High-Efficiency Mode Adds EXPO ULL-Style Tuning to Existing DDR5](https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram) ⭐️ 6.5/10

MSI has released a firmware update for its AM5 motherboards introducing a High-Efficiency Mode in Click BIOS X that automatically lowers DDR5 memory latencies, mimicking AMD's EXPO Ultra Low Latency (ULL) profile without requiring specially rated ULL memory kits. This update lets existing DDR5 owners—and those unable to buy overpriced EXPO ULL kits—unlock much of the same gaming performance gains without buying new hardware, making advanced memory tuning more accessible during a period of severe memory price inflation. MSI's internal testing showed latency dropping from 79.4 ns to 71.6 ns with High-Efficiency Mode, comparable to AMD's claimed 5–7 ns reduction from EXPO ULL on a standard DDR5-6000 kit. The feature lives in the Overclocking section of MSI's Click BIOS X and applies to AM5 platform motherboards.

rss · Tom's Hardware · Jul 31, 11:20

**Background**: AMD EXPO (Extended Profiles for Overclocking) is the company's standard for one-click DDR5 memory overclocking on its Ryzen platforms, similar to Intel's XMP. At Computex 2026, AMD announced EXPO Ultra Low Latency (ULL), a stricter profile targeting lower memory latency by adjusting parameters like tREFI, tRRDS, tWR, and VDDP voltage, promising up to a 13% gaming performance uplift. EXPO ULL requires specially validated memory kits, which have become scarce and expensive amid a global memory shortage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/motherboards/msi-promises-an-expo-ull-like-boost-for-your-existing-ddr5-high-efficiency-mode-brings-low-latency-tuning-to-older-ram">MSI promises an EXPO ULL-like boost for your existing DDR 5 memory...</a></li>
<li><a href="https://overclock3d.net/news/cpu_mainboard/msi-bring-amd-expo-ull-performance-to-standard-ddr5-memory-with-high-efficiency-mode/">MSI bring AMD EXPO ULL performance to standard DDR 5 memory...</a></li>
<li><a href="https://www-techpowerup-com.nproxy.org/349544/amd-unveils-the-expo-ull-ultra-low-latency-memory-profile-standard">AMD Unveils the EXPO - ULL ( Ultra Low - Latency ) Memory Profile...</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#MSI`, `#motherboards`, `#memory tuning`, `#AMD EXPO`

---

<a id="item-19"></a>
## [最前线｜武汉建成全国首个超大城市全域低空遥感监测网络，146座无人机机场构建“城市智眼”](https://36kr.com/p/3919271016263303?f=rss) ⭐️ 6.3/10

Wuhan has deployed China's first super-large city-wide low-altitude drone monitoring network with 146 unmanned airports, enabling 5-minute citywide drone response for traffic management, ecological monitoring, and urban governance.

rss · 36氪 · Jul 31, 08:12

**Tags**: `#low-altitude economy`, `#drones`, `#smart city`, `#urban governance`, `#DJI`

---

<a id="item-20"></a>
## [电投产融：山东莱阳核电项目获国务院常务会议核准](https://36kr.com/newsflashes/3919516325949059?f=rss) ⭐️ 6.3/10

China's State Council has approved the Shandong Laiyang nuclear power project, with two CAP1400 (Generation III+) reactors totaling ~3,086MW, to be developed by SPIC Financial.

rss · 36氪 · Jul 31, 12:18

**Tags**: `#nuclear-energy`, `#infrastructure`, `#china`, `#CAP1400`, `#energy-policy`

---