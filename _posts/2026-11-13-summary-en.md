---
layout: default
title: "Horizon Summary: 2026-11-13 (EN)"
date: 2026-11-13
lang: en
---

> From 94 items, 20 important content pieces were selected

---

1. [NVIDIA CEO Jensen Huang Resigns Amid Export and Misconduct Allegations](#item-1) ⭐️ 10.0/10
2. [Rust 1.100 release features custom allocators and never type stabilization](#item-2) ⭐️ 9.0/10
3. [Apple releases Foundation Models framework for on-device LLMs on iOS](#item-3) ⭐️ 8.0/10
4. [Apex Compute Unveils Neural Rendering to Challenge NVIDIA DLSS](#item-4) ⭐️ 7.5/10
5. [Google reworks TPU silicon into specialized systems for agents and security](#item-5) ⭐️ 7.5/10
6. [Gemini 4 Hydrogen and Orchestrator](#item-6) ⭐️ 7.0/10
7. [Edge0-145B: Frontier AI Capabilities on Your Own Computer](#item-7) ⭐️ 7.0/10
8. [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](#item-8) ⭐️ 7.0/10
9. [Nvidia Employees Petition to Reinstate Jensen Huang](#item-9) ⭐️ 7.0/10
10. [Open-source project enables 16B LLMs on sub-1GB devices](#item-10) ⭐️ 7.0/10
11. [Hyperspectral Imaging Advances Early Soybean Disease Detection](#item-11) ⭐️ 7.0/10
12. [Vicinity Technologies Links AI to Physical World via SDR](#item-12) ⭐️ 7.0/10
13. [Keychron Announces Open-Source MKF Firmware for Magnetic Keyboards](#item-13) ⭐️ 6.5/10
14. [AMD Cuts Gaming GPU Supply in China by Up to 50%](#item-14) ⭐️ 6.5/10
15. [Techie uses voltage glitching hack to turn $2,500 Nvidia 8GB cryptomining GPU into a full-fat $20,000 A100 with 80GB of VRAM](#item-15) ⭐️ 6.5/10
16. [Hobbyist turns $45 USB-C hub into a working Nintendo Switch 2 dock by patching its firmware](#item-16) ⭐️ 6.5/10
17. [Service degradation on Microsoft 365](#item-17) ⭐️ 6.0/10
18. [Design Smarter – Energy Harvesting for Battery-Free and Low-Maintenance Devices in Safety & Security applications](#item-18) ⭐️ 6.0/10
19. [AMD Siren Halo APU Rumored with Hybrid GDDR7 and LPDDR Memory](#item-19) ⭐️ 5.5/10
20. [Noctua Launches Carbice Carbon Nanotube Thermal Pad for AM5](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [NVIDIA CEO Jensen Huang Resigns Amid Export and Misconduct Allegations](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f) ⭐️ 10.0/10

NVIDIA CEO Jensen Huang has announced his resignation following reports of personal misconduct and allegations that he skirted US export restrictions. This announcement triggers a major leadership transition at the world's leading AI chipmaker. The departure of Jensen Huang, the central figure of the current AI boom, could significantly disrupt the semiconductor industry's trajectory. The allegations of violating export controls raise major geopolitical and national security concerns for the US. The resignation is reportedly linked to allegations of skirting export bans, a national security issue, and personal misconduct involving connections to Chinese government officials. The exact details and official rationale remain partially unclear pending corporate statements.

hackernews · lldb · Nov 12, 13:52 · [Discussion](https://news.ycombinator.com/item?id=50467087)

**Background**: Jensen Huang has led NVIDIA for decades, driving its transition into the leading provider of AI accelerators. US export restrictions limit the sale of advanced AI chips to China, making NVIDIA a focal point of geopolitical tensions.

**Discussion**: Community discussion is divided, with some arguing that the real reason is skirting export bans rather than personal affairs. Others theorize that the resignation is a preemptive move by competitors or a PR spectacle to benefit specific parties.

**Tags**: `#NVIDIA`, `#Jensen Huang`, `#AI Industry`, `#Geopolitics`, `#Leadership`

---

<a id="item-2"></a>
## [Rust 1.100 release features custom allocators and never type stabilization](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/) ⭐️ 9.0/10

Rust 1.100.0 is a milestone release that stabilizes the never type and introduces stable custom allocators. The version also includes enhanced Cargo features such as minimum publish age configurations for dependency management and unused dependency warnings. This release is monumental for the Rust ecosystem because it finally lands long-pending architectural features, significantly expanding the language's utility for complex systems programming and AI workloads. It improves supply chain security and code hygiene through stricter dependency management and tooling updates. Cargo now reports unused dependencies by default, and the minimum publish age feature (RFC 3923) allows resolvers to ignore recently published versions to prevent dependency cooldown attacks. Additionally, minor stable API additions like bool::toggle() and Box::map() were included but omitted from the primary blog post.

hackernews · mbStavola · Nov 12, 18:39 · [Discussion](https://news.ycombinator.com/item?id=50472038)

**Background**: Rust is a systems programming language known for memory safety and performance. The 'never type' (!) represents computations that never complete, while 'custom allocators' allow developers to control memory allocation beyond the default global allocator. These features address core limitations in writing high-performance and domain-specific memory management applications.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/">Announcing Rust 1.100.0 | Rust Blog</a></li>
<li><a href="https://doc.rust-lang.org/std/primitive.never.html">never - Rust</a></li>
<li><a href="https://iifx.dev/en/articles/457134612/from-c-pmr-to-rust-s-generics-understanding-custom-memory-management">From C++ PMR to Rust 's Generics: Understanding Custom Memory...</a></li>

</ul>
</details>

**Discussion**: Community reaction is highly positive, with core team member Steve Klabnik calling it a 'monostal' release. Users highlight the never type and dependency cooldowns as personal favorites, while also noting the release's impact on AI code generation. However, some users point out that useful new standard library functions were not mentioned in the official blog post.

**Tags**: `#Rust`, `#Programming Language`, `#Release`, `#Cargo`, `#Systems Programming`

---

<a id="item-3"></a>
## [Apple releases Foundation Models framework for on-device LLMs on iOS](https://developer.apple.com/foundation-models-framework/) ⭐️ 8.0/10

Apple has officially unveiled its Foundation Models framework, providing developers with a Swift API to integrate on-device large language models into iOS applications. This framework enables local AI processing powered by Apple Intelligence without requiring cloud API calls. This release is a significant milestone for mobile AI, allowing developers to create privacy-centric applications where data never leaves the user's device. It solidifies Apple's position in local computing by lowering the barrier for on-device AI integration. The framework specifically targets the on-device model powering Apple Intelligence, which runs on the Apple Neural Engine and is available on iOS 26 and later. Additionally, developers enrolled in specific programs can access Private Cloud Compute features at no extra cost.

hackernews · kermatt · Nov 12, 21:13 · [Discussion](https://news.ycombinator.com/item?id=50474361)

**Background**: On-device AI refers to running machine learning models directly on a user's hardware, such as smartphones, rather than sending data to external servers. Apple Intelligence is Apple's integrated AI system that leverages on-device models for language understanding and task execution within the iOS ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/foundationmodels">Foundation Models | Apple Developer Documentation</a></li>
<li><a href="https://medium.com/@yenatlij/getting-started-with-apples-foundation-models-framework-22255113de24">Getting Started with Apple ’s Foundation Models Framework | Medium</a></li>
<li><a href="https://ztabs.co/blog/on-device-llms-mobile-2026">On - Device LLMs for Mobile (2026): Apple Intelligence... | ZTABS</a></li>

</ul>
</details>

**Discussion**: Community members highlighted several related developments, noting that Apple's CoreAI project is adapting open-weight models to run natively in Swift. Users also shared practical examples of local AI on low-memory Macs and mentioned Anthropic's Claude App Attest support for iOS.

**Tags**: `#Apple`, `#On-Device AI`, `#LLM`, `#iOS Development`, `#Privacy`

---

<a id="item-4"></a>
## [Apex Compute Unveils Neural Rendering to Challenge NVIDIA DLSS](https://www.techpowerup.com/354727/apex-neural-rendering-beats-nvidia-dlss-in-both-image-quality-and-performance) ⭐️ 7.5/10

Apex Compute has introduced Apex Neural Rendering (ANR), a new framework that claims to outperform NVIDIA DLSS in both latency and GPU memory efficiency. It offers a 1.01 ms frame generation latency and utilizes only 214 MB of memory on an RTX 5090, compared to DLSS's 1.26 ms and 562 MB. By achieving lower latency and significantly less memory consumption than the industry-leading DLSS, ANR provides a more efficient alternative for real-time AI-accelerated rendering. This breakthrough is particularly valuable for gamers and developers seeking to optimize high-end gaming hardware. ANR is currently a beta injector that relies on NVIDIA OptiScaler, allowing it to function seamlessly in any game that supports NVIDIA DLSS Frame Generation. Its neural network weights are highly efficient, requiring only 0.17 MB of space.

rss · TechPowerUp News · Nov 12, 09:19

**Background**: NVIDIA DLSS is a widely adopted AI-driven upscaling and frame generation technology for PC gaming that heavily impacts GPU performance. Apex Neural Rendering operates on a similar conceptual level but uses a different software implementation to achieve comparable or better results. Because the technology runs as an injector over OptiScaler, it bypasses the need for developers to explicitly add ANR support to their games.

<details><summary>References</summary>
<ul>
<li><a href="https://apexcompute.com/neural-rendering">ANR: Apex Neural Rendering | Apex Compute</a></li>
<li><a href="https://www.gamingonlinux.com/2026/11/apex-compute-revealed-apex-neural-rendering-anr-their-cross-platform-answer-to-nvidia-dlss/">Apex Compute revealed Apex Neural Rendering ... | GamingOnLinux</a></li>
<li><a href="https://github.com/apex-compute/ANR">GitHub - apex - compute /ANR: Apex Neural Rendering (ANR) by...</a></li>

</ul>
</details>

**Tags**: `#neural-rendering`, `#DLSS`, `#GPU-optimization`, `#computer-graphics`, `#AI-acceleration`

---

<a id="item-5"></a>
## [Google reworks TPU silicon into specialized systems for agents and security](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-adds-two-new-specialized-chips-for-ai-agents-and-security-to-8th-gen-tpu-lineup-tpu-8i-max-puts-two-chips-on-one-package-for-long-context-work-tpu-8tx-swaps-arm-hosts-for-amd-epyc) ⭐️ 7.5/10

Google has introduced two new specialized TPU systems, TPU 8i Max for long-context agent workloads and TPU 8tx for confidential inference using AMD EPYC hosts.

rss · Tom's Hardware · Nov 12, 11:00

**Tags**: `#Google TPU`, `#AI Hardware`, `#AI Agents`, `#Silicon Design`, `#Inference Security`

---

<a id="item-6"></a>
## [Gemini 4 Hydrogen and Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/) ⭐️ 7.0/10

Google Antigravity announces Gemini 4 Hydrogen and an Orchestrator mode, which community members discuss in terms of performance comparisons to existing models and the technical implications of multi-model pipeline caching.

hackernews · jonbaer · Nov 12, 18:52 · [Discussion](https://news.ycombinator.com/item?id=50472260)

**Tags**: `#Gemini`, `#LLM`, `#Model Orchestration`, `#Google AI`, `#Developer Tools`

---

<a id="item-7"></a>
## [Edge0-145B: Frontier AI Capabilities on Your Own Computer](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer) ⭐️ 7.0/10

Edge0-145B is introduced as a 145B-parameter AI model designed for local inference on consumer hardware, achieving low memory footprints through expert matrix sharing and demonstrating advanced tool-use capabilities.

hackernews · sroussey · Nov 12, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50475713)

**Tags**: `#AI/ML`, `#Edge Computing`, `#Large Language Models`, `#Model Compression`, `#Local Inference`

---

<a id="item-8"></a>
## [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](https://github.com/simpsoka/zigzag) ⭐️ 7.0/10

A developer built a custom app for their $300 embroidery machine to avoid a subscription fee, showcasing the practical use of LLMs in automating niche hardware.

hackernews · simpsoka · Nov 12, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50470488)

**Tags**: `#hardware`, `#AI-Tools`, `#IOT`, `#OpenSource`, `#HackerNews`

---

<a id="item-9"></a>
## [Nvidia Employees Petition to Reinstate Jensen Huang](https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/) ⭐️ 7.0/10

Nvidia employees have launched an internal petition calling for the reinstatement of former CEO Jensen Huang following his departure. The move has triggered a polarized debate across corporate and online communities regarding his ethical lapses. This event signals a significant corporate governance crisis, highlighting the friction between a leader's operational success and their compliance failures under strict international export control laws. It raises critical questions about board accountability and risk management. Critics highlight that Huang's alleged conduct extends beyond standard personal mistakes to a systemic pattern, involving relationships with foreign entities attempting to evade ITAR restrictions. Supporters argue for his exceptional leadership capabilities and right to a second chance.

hackernews · lavendermon · Nov 13, 02:16 · [Discussion](https://news.ycombinator.com/item?id=50477231)

**Background**: Jensen Huang recently stepped down as the Chief Executive Officer of Nvidia, a move that is still unfolding in terms of public details. ITAR is a United States federal regulation that strictly limits the export of defense-related items, and facilitating their evasion by foreign entities carries severe legal implications.

**Discussion**: The community is deeply divided; while some defend Jensen citing his past successes, others argue that his interactions with entities evading export controls reveal a reckless pattern of behavior. Many express concern over potential corporate vulnerabilities and the board's failure to address these risks.

**Tags**: `#Nvidia`, `#Corporate Governance`, `#Jensen Huang`, `#Ethics`, `#Tech Leadership`

---

<a id="item-10"></a>
## [Open-source project enables 16B LLMs on sub-1GB devices](https://github.com/hyperionaidev/smolmaxxing/) ⭐️ 7.0/10

An open-source initiative has successfully enabled 16B parameter LLMs to run on extremely constrained devices, such as the first-generation iPad Air and Xiaomi TV boxes, which have less than 1GB of usable memory. The project achieves this through optimized inference kernels, model modifications, and shared resources on Hugging Face. This breakthrough significantly expands the accessibility of large language models to legacy and low-power hardware, proving that edge AI does not require high-end resources. It aligns with broader industry trends aimed at reducing the computational footprint of inference engines, fostering a more inclusive and distributed AI ecosystem. The project relies on custom-developed kernels and modified model weights to bypass traditional memory bottlenecks. While it achieves "decent speeds" given the hardware limits, the primary challenge in deploying such systems remains the availability of physical hardware rather than the computational logic itself, which reduces to basic operations like multiplication.

hackernews · mrashad74 · Nov 12, 15:23 · [Discussion](https://news.ycombinator.com/item?id=50468888)

**Background**: Large language models typically require significant memory (often measured in gigabytes) to store model parameters during inference. Running them on devices with less than 1GB of RAM requires aggressive techniques like model quantization, which reduces the numerical precision of weights, and custom inference kernels that optimize CPU memory access. These modifications allow the entire computation to fit within the constrained memory limits of legacy mobile and TV hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://cast.ai/blog/demystifying-quantizations-llms/">LLM Quantization Methods: GPTQ, AWQ, GGUF - Cast AI</a></li>
<li><a href="https://www.linkedin.com/posts/martinuke0_optimizing-local-inference-a-guide-to-running-activity-7459953891997249536-cg5R">Optimizing 100B Parameter Models on Edge Hardware | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Community members express enthusiasm for the project and share parallel achievements, such as running LLMs on retro Dreamcast hardware via Windows CE. The discussion highlights how modern inference engines are primarily bottlenecked by memory and basic compute, making the availability of hardware the new barrier to entry rather than algorithmic complexity.

**Tags**: `#LLM`, `#Edge AI`, `#Hardware Optimization`, `#Open Source`, `#Inference`

---

<a id="item-11"></a>
## [Hyperspectral Imaging Advances Early Soybean Disease Detection](https://www.eetimes.com/can-machines-see-a-sick-plant-before-a-farmer-can/) ⭐️ 7.0/10

Soybean disease research highlights the use of hyperspectral imaging for early detection of plant ailments. Semiconductor advances are now enabling chip-scale spectral sensing systems to become affordable for widespread farming use. Early detection of crop diseases can significantly reduce yield losses and optimize resource use in agriculture. Making this technology affordable is crucial for democratizing precision agriculture and improving global food security. Practical application of hyperspectral sensors in field and greenhouse conditions for precision farming remains a challenge. Emerging technologies focus on CMOS-integrated, low-cost multispectral and polarization sensing.

rss · EE Times · Nov 12, 13:00

**Background**: Hyperspectral imaging captures detailed spectral data across many narrow bands, allowing it to detect subtle plant health changes invisible to the human eye. Machine learning algorithms process this data to identify specific disease symptoms early.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iis.fraunhofer.de/en/ff/sse/sensor-solutions/optnanostruktcmos.html">nanoSPECTRAL: Multispectral and Polarization Sensors</a></li>
<li><a href="https://www.mdpi.com/2073-4395/12/6/1451">Hyperspectral Sensing of Plant Diseases: Principle and Methods</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8983301/">A review of hyperspectral image analysis techniques for plant ...</a></li>

</ul>
</details>

**Tags**: `#Hyperspectral Imaging`, `#Precision Agriculture`, `#Sensors`, `#Semiconductors`

---

<a id="item-12"></a>
## [Vicinity Technologies Links AI to Physical World via SDR](https://www.eetimes.com/connecting-ai-to-the-physical-world/) ⭐️ 7.0/10

An article by the CEO of Vicinity Technologies argues that specialized wireless devices and SDR IP are critical for connecting AI to the physical world. The piece highlights how these components are essential for the next generation of intelligent machines. This perspective is significant because it bridges the gap between digital AI and physical reality, identifying specialized hardware as the necessary conduit for intelligent systems. It highlights a key dependency for the deployment of advanced IoT and autonomous systems. The author represents Vicinity Technologies, indicating the content serves as thought leadership or industry analysis with a specific commercial angle. The analysis focuses on the role of SDR software IP rather than just hardware, emphasizing software-defined flexibility.

rss · EE Times · Nov 12, 10:20

**Background**: Software-Defined Radio (SDR) replaces traditional analog hardware components with software on embedded systems, allowing for programmable and flexible radio communication. By integrating AI with SDR, machines can dynamically sense, analyze, and respond to physical spectral conditions, which is crucial for modern IoT environments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio - Wikipedia</a></li>
<li><a href="https://ieeexplore.ieee.org/abstract/document/11456026">Artificial Intelligence in Software Defined Radio: A Survey</a></li>

</ul>
</details>

**Tags**: `#AI`, `#IoT`, `#SDR`, `#Hardware`, `#Wireless`

---

<a id="item-13"></a>
## [Keychron Announces Open-Source MKF Firmware for Magnetic Keyboards](https://www.techpowerup.com/354759/keychron-launches-open-source-magnetic-keyboard-firmware) ⭐️ 6.5/10

Keychron has announced MKF, an open-source firmware project for TMR and Hall effect gaming keyboards that outlines features like 8kHz polling, Rapid Trigger, and controller emulation. The project is currently just a landing page without any public code contributions. Open-sourcing magnetic keyboard firmware aligns with the broader open-hardware movement, allowing enthusiasts to customize features like custom response curves and PDO. It provides a community-driven foundation that could rival closed firmware in high-end gaming peripherals. Initial support is planned for wired connectivity only, but the firmware will include advanced features like PDO, which sends more keypresses based on how deeply a key is held. The project explicitly invites community contributions for features outside of competitive gaming.

rss · TechPowerUp News · Nov 12, 21:34

**Background**: Magnetic keyboards use TMR or Hall effect sensors to detect switch position, allowing for adjustable actuation and rapid trigger. Rapid Trigger resets a key when released, while SOCD (Simultaneous Opposing Cardinal Directions) helps resolve conflicts when opposing directions are pressed at once. These features are critical for competitive FPS gaming.

<details><summary>References</summary>
<ul>
<li><a href="https://unikeyboards.com/blogs/weekeebpedia/tmr-vs-hall-effect">TMR vs Hall Effect: Which Magnetic Keyboard Technology Is ...</a></li>
<li><a href="https://gameperipherals.com/blogs/all-posts/rapid-trigger-adjustable-actuation-and-socd-explained">Rapid Trigger, Adjustable Actuation and SOCD Explained</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#firmware`, `#open-source`, `#keyboards`, `#input-devices`

---

<a id="item-14"></a>
## [AMD Cuts Gaming GPU Supply in China by Up to 50%](https://www.techpowerup.com/354757/amd-reportedly-cuts-gaming-gpu-supply-in-china-by-up-to-50) ⭐️ 6.5/10

AMD has reportedly reduced gaming GPU supply in China by at least 20% to 50% since the start of the fourth quarter, leading to tighter allocations and rising prices for Radeon cards. These changes are expected to persist until January as supply chains continue to shrink. This supply contraction significantly impacts gamers and PC builders in China by increasing the difficulty of obtaining affordable Radeon graphics cards. The rising prices and limited availability reflect broader memory and GPU cost pressures across the global hardware industry. AMD is expected to keep raising the prices of GPU and GDDR6 kits, while competitors like NVIDIA are also facing supply limits on high-end models. The market is seeing graphics cards sell on average 44% above their MSRP, making new releases significantly more expensive for consumers.

rss · TechPowerUp News · Nov 12, 21:14

**Background**: Graphics card manufacturers work with add-in board (AIB) partners to produce retail products, and fluctuations in supply directly affect these distributors. GDDR6 is a type of memory used in modern GPUs, and its cost is a major factor in the final retail price of gaming hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://hwbusters.com/news/amd-reportedly-plans-another-radeon-price-increase-for-november-as-gddr6-keeps-climbing/">AMD Reportedly Plans Another Radeon Price Increase for November...</a></li>
<li><a href="https://grokipedia.com/page/Add-in_board">Add-in board — Grokipedia</a></li>
<li><a href="https://pcbstore.com.bd/glossary/aib-partner-card">What is AIB Partner Card? Custom GPU Basics Explained</a></li>

</ul>
</details>

**Tags**: `#Hardware`, `#Supply Chain`, `#AMD`, `#GPU`, `#China`

---

<a id="item-15"></a>
## [Techie uses voltage glitching hack to turn $2,500 Nvidia 8GB cryptomining GPU into a full-fat $20,000 A100 with 80GB of VRAM](https://www.tomshardware.com/pc-components/gpus/techie-turns-usd2-500-cmp-170hx-8gb-mining-card-into-a-full-fat-a100-80gb-with-voltage-glitching-carefully-blowing-onboard-fuses-to-unlock-entire-vram-and-shader-modules) ⭐️ 6.5/10

A technician used voltage glitching techniques to disable fuses on an Nvidia CMP-170HX mining card, effectively unlocking its full 80GB VRAM and shader capabilities to create a high-performance equivalent of an A100 GPU.

rss · Tom's Hardware · Nov 12, 10:30

**Tags**: `#GPU`, `#Hardware Mod`, `#AI Hardware`, `#Nvidia`, `#Cryptocurrency Mining`

---

<a id="item-16"></a>
## [Hobbyist turns $45 USB-C hub into a working Nintendo Switch 2 dock by patching its firmware](https://www.tomshardware.com/video-games/nintendo/hobbyist-turns-usd45-usb-c-hub-into-a-working-nintendo-switch-2-dock-by-patching-its-firmware-consoles-proprietary-handshake-needs-about-540-bytes-of-code-to-answer) ⭐️ 6.5/10

A hobbyist successfully patched the firmware of a $45 USB-C hub to function as a Nintendo Switch 2 dock, enabling TV mode and HDR support by emulating the proprietary handshake.

rss · Tom's Hardware · Nov 12, 09:00

**Tags**: `#Hardware Hacking`, `#Nintendo Switch`, `#Firmware`, `#Reverse Engineering`, `#USB-C`

---

<a id="item-17"></a>
## [Service degradation on Microsoft 365](https://status.cloud.microsoft/) ⭐️ 6.0/10

A major service degradation affecting Microsoft 365 worldwide, with community members sharing real-time updates on status page issues, mitigation steps, and the impact on enterprise email and communication tools.

hackernews · dkpk · Nov 12, 18:20 · [Discussion](https://news.ycombinator.com/item?id=50471731)

**Tags**: `#Microsoft 365`, `#Outage`, `#IT Operations`, `#Cloud Services`, `#Reliability`

---

<a id="item-18"></a>
## [Design Smarter – Energy Harvesting for Battery-Free and Low-Maintenance Devices in Safety & Security applications](https://www.eetimes.com/design-smarter-energy-harvesting-for-battery-free-and-low-maintenance-devices-in-safety-security-applications/) ⭐️ 6.0/10

A design guide explaining how to implement energy harvesting in safety and security devices to eliminate the need for manual battery maintenance.

rss · EE Times · Nov 12, 15:00

**Tags**: `#Energy Harvesting`, `#Hardware Design`, `#IoT`, `#Embedded Systems`, `#Power Management`

---

<a id="item-19"></a>
## [AMD Siren Halo APU Rumored with Hybrid GDDR7 and LPDDR Memory](https://www.techpowerup.com/354765/amd-siren-halo-apu-rumored-to-pair-dedicated-gddr7-with-lpddr-memory) ⭐️ 5.5/10

A leak from X suggests that AMD's next-generation 'Siren Halo' APU will feature a hybrid memory architecture pairing dedicated GDDR7 VRAM with standard LPDDR system memory. The leaker also claimed that Siren Halo will follow the Medusa Halo design and that Siren Point is essentially a Medusa refresh. This hybrid design would mark a significant departure from AMD's current unified-memory APUs, potentially boosting iGPU gaming performance by providing higher memory bandwidth while keeping separate system memory for AI and general workloads. It signals AMD's continued evolution of high-performance integrated graphics. No specific details regarding memory capacities, bus widths, or launch timing for the Siren Halo have been disclosed in this leak. The APU is rumored to be linked to AMD's Project Magnus, which is associated with Microsoft's Project Helix console hardware.

rss · TechPowerUp News · Nov 13, 00:37

**Background**: AMD's current high-end APUs, like the Strix Halo, use a shared pool of LPDDR5X memory for both the CPU and iGPU, a design popular for local LLMs. GDDR7 is a newer, high-bandwidth memory standard recently adopted in discrete GPUs, and AMD has already added GDDR7 driver support in preparation for its RDNA 5 GPU architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/354765/amd-siren-halo-apu-rumored-to-pair-dedicated-gddr7-with-lpddr-memory">AMD "Siren Halo" APU Rumored to Pair Dedicated GDDR7 With ...</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#APU`, `#GDDR7`, `#Hardware Rumor`, `#GPU Architecture`

---

<a id="item-20"></a>
## [Noctua Launches Carbice Carbon Nanotube Thermal Pad for AM5](https://www.techpowerup.com/354729/noctua-introduces-nt-cp1-carbice-carbon-nanotube-thermal-pad-for-am5) ⭐️ 5.5/10

Noctua has released the NT-CP1, a premium carbon nanotube thermal pad designed for AMD AM5 and AM4 processors. Utilizing Carbice technology, the pad claims to improve heat transfer performance over hundreds to thousands of thermal cycles rather than degrading like traditional thermal pastes. This product addresses a critical reliability concern in high-performance computing by eliminating the maintenance cycle of reapplying thermal paste. It offers enthusiasts a durable, 'set-and-forget' solution that prevents performance degradation due to pump-out and delamination. The NT-CP1 uses a sturdy aluminum backbone and a phase-change polymer coating to ensure ease of installation and electrical non-conductivity on contact surfaces. Once the initial activation phase of conforming to surface microstructures is complete, it maintains stable performance for years.

rss · TechPowerUp News · Nov 12, 10:25

**Background**: Thermal pads are solid thermal interface materials used to bridge the gap between a processor's Integrated Heat Spreader (IHS) and a cooler. Traditional thermal pastes often suffer from 'pump-out,' where thermal cycling forces the fluid material to migrate away from the interface, increasing thermal resistance. Carbon nanotube technology is increasingly being adopted to create more stable, long-lasting thermal interfaces.

<details><summary>References</summary>
<ul>
<li><a href="https://www.noctua.at/en/news/noctua-introduces-nt-cp1-carbon-nanotube-thermal-pad-for-am5">Noctua introduces NT-CP1 Carbice ® carbon nanotube thermal pad ...</a></li>
<li><a href="https://carbice.com/technology/how-it-works">How Carbice Works | Carbice</a></li>
<li><a href="https://www.lenecold.com/resources/thermal-pad-pump-out.html">What Is TIM Pump-Out? Why Thermal Grease Fails in Cycling ...</a></li>

</ul>
</details>

**Tags**: `#Hardware`, `#Thermal Management`, `#AMD`, `#PC Cooling`, `#Product Release`

---