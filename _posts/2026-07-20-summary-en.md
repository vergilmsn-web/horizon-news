---
layout: default
title: "Horizon Summary: 2026-07-20 (EN)"
date: 2026-07-20
lang: en
---

> From 53 items, 18 important content pieces were selected

---

1. [SRE Replaces $120K Bowling Scoring System with $1,600 in ESP32s](#item-1) ⭐️ 8.0/10
2. [ESP32 Dongle Blocks 537K Ad Domains Using Only 50KB RAM](#item-2) ⭐️ 7.5/10
3. [我国人形机器人整机产品超全球半数](#item-3) ⭐️ 7.3/10
4. [Meshy完成近4亿美元B轮融资](#item-4) ⭐️ 7.3/10
5. [Claude Code Rewritten from Zig to Rust, Now Uses Bun](#item-5) ⭐️ 7.0/10
6. [Minecraft Java Edition Migrates from SDL2 to SDL3 in Latest Snapshot](#item-6) ⭐️ 7.0/10
7. [Alibaba Announces Qwen 3.8: 2.4T Parameter Open-Weights LLM](#item-7) ⭐️ 7.0/10
8. [Tencent Cloud ADP 4.0 Goes Global with Enterprise Agent Platform](#item-8) ⭐️ 6.3/10
9. [8点1氪丨长鑫科技中签号出炉：共约770.22万个；西班牙1-0战胜阿根廷，夺得本届世界杯冠军；月之暗面有望最快6个月内赴港上市](#item-9) ⭐️ 6.3/10
10. [工信部：将加快出台人工智能+软件行动方案](#item-10) ⭐️ 6.3/10
11. [工信部：将印发算力标准体系建设指南，推动建立算力市场化定价等标准](#item-11) ⭐️ 6.3/10
12. [China's intelligent computing power reaches 2185 EFLOPS](#item-12) ⭐️ 6.3/10
13. [What I learned selling 2,500 MIDI recorders: Hardware is not so hard](#item-13) ⭐️ 6.0/10
14. [AMD Medusa Point 10-Core APU Leaks New Geekbench Record](#item-14) ⭐️ 5.5/10
15. [Zilog Z80 turns 50 as an open-source replacement heads to drop-in DIP40 silicon — iconic 8-bit CPU launched in July 1976 and was discontinued in 2024](#item-15) ⭐️ 5.5/10
16. [Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’](#item-16) ⭐️ 5.5/10
17. [Russian drones spotted using screwed-on magnetic compasses as navigation aids — the on-board camera can occasionally tilt down to check bearings if satellite comms are lost](#item-17) ⭐️ 5.5/10
18. [MSI Previews Liquid-Cooled AMD EPYC Venice Dual-Socket Server at Computex](#item-18) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [SRE Replaces $120K Bowling Scoring System with $1,600 in ESP32s](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

An SRE who bought an abandoned 8-lane bowling center built OpenLaneLink, a DIY scoring and control system using ESP32 microcontrollers, ESPNow mesh networking, RS485 fallback, and a Raspberry Pi running Redis as middleware — replacing a 2008-era commercial system that originally cost six figures. This is a striking real-world example of how cheap modern embedded hardware and open-source software can displace overpriced legacy industrial systems with vendor lock-in, potentially saving small business owners enormous capital costs while giving them full data ownership and customization freedom. The system uses ESP32 nodes wired to relays, optocouplers, and IR break-beam sensors in a star-topology mesh reporting via UART to a Raspberry Pi; total cost is roughly $200 per lane-pair ($400 with extras) versus $4,000 per pair for vendor replacement parts, and a full lane swap takes under 10 minutes — the author plans to open-source the entire stack.

hackernews · section33 · Jul 19, 14:41

**Background**: Bowling centers rely on automated pinsetters — often decades-old mechanical machines — controlled by electronic scoring systems that detect pins via cameras, track ball speed, run foul detection, drive overhead monitors, and animate the scoreboard. The ESP32 is a low-cost Wi-Fi/Bluetooth microcontroller from Espressif Systems popular in IoT and embedded projects. ESPNow is a connectionless Espressif protocol that lets ESP32 chips communicate peer-to-peer without a Wi-Fi router, useful for simple mesh setups, while RS485 is a robust wired industrial bus standard often used as a noise-resistant fallback.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>
<li><a href="https://www.espressif.com/en/products/socs/esp32">ESP32 Wi-Fi & Bluetooth SoC | Espressif Systems</a></li>

</ul>
</details>

**Discussion**: The community reaction was highly supportive and domain-rich: another bowling lane owner with a 1970-era Intel D8749H-based scoring system confirmed the relay-control pattern; an embedded retrofitter shared parallels retrofitting old machine tools; a commenter who grew up around bowling machines validated the mechanical reality; and the author outlined future plans for DMX lighting control, LED chase animations, and self-service kiosk payment.

**Tags**: `#ESP32`, `#embedded-systems`, `#retrofit`, `#hardware-hacking`, `#Show-HN`

---

<a id="item-2"></a>
## [ESP32 Dongle Blocks 537K Ad Domains Using Only 50KB RAM](https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds) ⭐️ 7.5/10

A hardware hacker has designed firmware for a $5 ESP32 dongle that stores and queries a blocklist of 537,000 advertising and tracking domains using only ~50KB of RAM and 4MB of flash, answering DNS lookups for blocked domains in about 10 milliseconds. It demonstrates that network-wide ad blocking does not require expensive single-board computers like Raspberry Pi, making privacy and ad-blocking accessible on extremely cheap, low-power embedded hardware for DIY home networking and security enthusiasts. The trick relies on a space-efficient hashing scheme (likely a Bloom filter variant) to compress domain membership data so the entire 537K-domain list fits in just 4MB of flash and queries resolve in ~10ms; the approach trades perfect accuracy for extreme memory efficiency, and the total hardware cost is around $5 per unit.

rss · Tom's Hardware · Jul 19, 10:00

**Background**: The ESP32 is a low-cost, Wi-Fi- and Bluetooth-enabled microcontroller family made by Espressif Systems, commonly used in IoT projects. Traditional network-wide ad blockers like Pi-hole run on Linux-capable boards and need tens or hundreds of megabytes of RAM. To compress a 537,000-entry domain blocklist into a device with only ~50KB of RAM, the project almost certainly leverages a Bloom filter — a probabilistic data structure invented by Burton Bloom in 1970 that tests set membership using multiple hash functions and very little memory, at the cost of occasional false positives (blocking a domain that is not on the list).

<details><summary>References</summary>
<ul>
<li><a href="https://www.espressif.com/en/products/socs/esp32">ESP 32 Wi-Fi & Bluetooth SoC | Espressif Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bloom_filter">Bloom filter - Wikipedia</a></li>
<li><a href="https://www.digikey.com/es/maker/blogs/2024/a-guide-for-the-esp32-microcontroller-series">A Guide for the ESP 32 Microcontroller Series</a></li>

</ul>
</details>

**Tags**: `#embedded-systems`, `#ESP32`, `#ad-blocking`, `#DNS`, `#hardware-hacking`

---

<a id="item-3"></a>
## [我国人形机器人整机产品超全球半数](https://36kr.com/newsflashes/3903383107110785?f=rss) ⭐️ 7.3/10

China's MIIT reports the country produces over half of global humanoid robot products (400+ models) and ~70% of global quadruped robot sales, highlighting rapid growth in China's robotics industry.

rss · 36氪 · Jul 20, 02:46

**Tags**: `#humanoid-robots`, `#robotics`, `#china-tech`, `#industry-stats`, `#MIIT`

---

<a id="item-4"></a>
## [Meshy完成近4亿美元B轮融资](https://36kr.com/newsflashes/3903365138270088?f=rss) ⭐️ 7.3/10

AI 3D generation company Meshy raises ~$400M in a record-breaking Series B round, reaching a $1.4B+ valuation, with funds earmarked for multimodal model R&D and global expansion.

rss · 36氪 · Jul 20, 02:28

**Tags**: `#AI`, `#3D generation`, `#funding`, `#multimodal models`, `#venture capital`

---

<a id="item-5"></a>
## [Claude Code Rewritten from Zig to Rust, Now Uses Bun](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/) ⭐️ 7.0/10

Anthropic has rewritten Claude Code's runtime from Zig to Rust, and the new build ships with Bun v1.4.0 — a version ahead of the latest public release (v1.3.14) — indicating Anthropic is shipping a preview fork following its acquisition of the Bun project. This decision highlights real-world tradeoffs between systems-level languages for production agentic tooling and raises open-source governance concerns about Bun's future as an independent FOSS project now that it is owned by Anthropic. Bun itself is written in Rust and uses Safari's JavaScriptCore engine, unlike Node.js and Deno which use V8. The core engineering motivation was that Rust's automatic memory management eliminates an entire class of bugs the team encountered with Zig's manual memory lifecycle tracking.

hackernews · tosh · Jul 19, 10:03 · [Discussion](https://news.ycombinator.com/item?id=48966569)

**Background**: Claude Code is Anthropic's agentic coding tool that lives in the terminal and helps developers edit code, run commands, and manage git workflows. Bun is a fast all-in-one JavaScript runtime, package manager, and test runner designed as a drop-in replacement for Node.js, originally created by Jarred Sumner. Zig is a low-level systems language similar to C that requires developers to manually manage and explicitly free memory, while Rust enforces memory safety automatically through its ownership and borrow checker at compile time.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test ...</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some endorse the Rust switch, noting it removes manual memory management bugs that plagued the Zig implementation, while others sharply criticize the communication around the Bun acquisition and worry the open-source Bun project is effectively dying. A recurring thread questions why a terminal UI (TUI) needs to run on React/JavaScript via Bun at all, with skeptics arguing a fully native rewrite would have been cheaper and simpler.

**Tags**: `#claude-code`, `#rust`, `#bun`, `#anthropic`, `#engineering-decisions`

---

<a id="item-6"></a>
## [Minecraft Java Edition Migrates from SDL2 to SDL3 in Latest Snapshot](https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4) ⭐️ 7.0/10

Minecraft Java Edition snapshot 25w03 (26-3 snapshot 4) has migrated its underlying multimedia layer from SDL2 to SDL3 via updated LWJGL3 bindings. The release notes acknowledge known issues, including crashes when entering exclusive fullscreen mode on Windows (especially with multiple monitors) and on Wayland. SDL3 brings modernized APIs, improved platform support (including native Wayland handling), and better performance characteristics that could benefit Minecraft's long-term maintainability and cross-platform stability. Because Minecraft is one of the most widely played Java applications in the world, this migration serves as a notable real-world validation of SDL3 and LWJGL3 maturity. The LWJGL3 bindings that enabled the migration were authored by a contributor from the GTNH (GregTech: New Horizons) modpack team, continuing the tradition of modding ecosystem improvements flowing back into vanilla Minecraft. The community flagged the exclusive fullscreen bugs as potential blockers for final release.

hackernews · ObviouslyFlamer · Jul 19, 11:48 · [Discussion](https://news.ycombinator.com/item?id=48967256)

**Background**: SDL (Simple DirectMedia Layer) is a cross-platform C library that abstracts access to graphics (OpenGL, Direct3D, Vulkan, Metal), audio, and input hardware; SDL3, released as v3.2.0 in January 2025, is its latest major version. LWJGL (Lightweight Java Game Library) provides Java bindings to native libraries such as OpenGL, Vulkan, and SDL, and is the bridge Minecraft Java Edition uses to interact with low-level system APIs. The migration was made possible by the official SDL3 support in LWJGL3, which lets Java programs access SDL3's modernized feature set.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer">Simple DirectMedia Layer - Wikipedia</a></li>
<li><a href="https://www.lwjgl.org/">LWJGL - Lightweight Java Game Library</a></li>
<li><a href="https://en.wikipedia.org/wiki/LWJGL">LWJGL - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment was largely positive about the milestone but concerned about the unresolved fullscreen crashes. Commenters highlighted the circular contribution flow between the modding community and vanilla (the LWJGL3 SDL3 bindings came from a GTNH modpack team member), shared Ryan 'Icculus' Gordon's video on porting Doom to SDL3 as relevant context, and noted that Minecraft is increasingly functioning as a general-purpose game engine rather than just a game.

**Tags**: `#minecraft`, `#sdl3`, `#game-development`, `#graphics`, `#lwjgl`

---

<a id="item-7"></a>
## [Alibaba Announces Qwen 3.8: 2.4T Parameter Open-Weights LLM](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) ⭐️ 7.0/10

Alibaba has announced Qwen 3.8, a 2.4-trillion-parameter large language model with open weights, seemingly in direct response to Moonshot AI's recent release of the 2.8T-parameter Kimi K3. The announcement itself consists only of a link to Qwen Cloud pricing pages, with full architecture details and benchmarks yet to be published. This release intensifies the fierce competition among Chinese AI labs to produce the largest open-weight frontier models, with both Alibaba and Moonshot AI now offering trillion-parameter-scale models that rival top U.S. systems from OpenAI and Anthropic. Open-weight releases at this scale democratize access to cutting-edge AI capabilities, benefiting researchers, developers, and enterprises worldwide who can fine-tune and self-host the models. The announcement is notably thin—only a pricing link is shared—leaving model architecture, benchmark results, and an exact release timeline unclear. Notably, developer Simon Willison reports being unable to pay Alibaba Cloud due to his email address being flagged, highlighting potential payment and access friction for international users of the commercial API.

hackernews · nh43215rgb · Jul 19, 08:44 · [Discussion](https://news.ycombinator.com/item?id=48966120)

**Background**: Qwen is Alibaba's family of large language models, with the Qwen3 series introducing hybrid 'thinking' and 'non-thinking' modes that allow users to toggle between reasoning-intensive and fast-response outputs. 'Open weights' means the trained model parameters are released publicly for inference and fine-tuning, but this is distinct from fully open source—training data and code are typically not included. Moonshot AI's Kimi K3, released in July 2026, is a 2.8T-parameter natively multimodal model with a 1M-token context window, and Qwen 3.8 appears positioned as a direct competitor in the same trillion-parameter class.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html">China's Moonshot AI unveils Kimi K3 that rivals OpenAI, Anthropic China’s Moonshot AI releases Kimi K3, the largest open-source ... Kimi K3: Moonshot AI’s 2.8T Open-Weight Model — Release ... Moonshot AI Kimi K3 Release: Specs, Pricing, API & When to Switch China's Moonshot AI claims Kimi K3 can rival OpenAI and ... Kimi K3: Moonshot AI's Open-Source Flagship, Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models: Open Source vs Open Weights vs ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is engaged but mixed. Users widely recognize the competitive dynamic between Alibaba and Moonshot AI, with one commenter noting 'from this competition in LLMs, we win.' However, quality concerns persist—one developer reports Qwen 3.7 Pro as 'totally unusable' for software engineering tasks compared to DeepSeek, citing wasted time and high cost. Local-deployment enthusiasts hope Alibaba will release smaller variants, while Simon Willison flagged that Alibaba Cloud blocked him from paying for access.

**Tags**: `#llm`, `#qwen`, `#alibaba`, `#open-weights`, `#ai-competition`

---

<a id="item-8"></a>
## [Tencent Cloud ADP 4.0 Goes Global with Enterprise Agent Platform](https://36kr.com/p/3901396207584902?f=rss) ⭐️ 6.3/10

On July 18, 2026, at the World Artificial Intelligence Conference (WAIC), Tencent Cloud officially launched the overseas edition of its Agent Development Platform (ADP) 4.0, upgrading its Intelligent Workbench, Claw Mode, and Skill Marketplace with international adaptations including LINE and Telegram channel support, multi-language auto-response, and integrations with Google Workspace, Confluence, and Jira. This launch marks Tencent Cloud's first major push of its enterprise-grade AgentOps platform into international markets, shifting competition from the token/pricing layer up to the application layer. The company's emphasis on trust, controllability, full-chain auditability, and role-based permissions positions ADP as an enterprise alternative to personal AI assistants, targeting Southeast Asian markets like Indonesia where it already has private deployment projects. A key architectural innovation is Agent-Workflow bidirectional orchestration, where open-ended tasks are handled by Agents while deterministic processes run as Workflows to reduce token consumption. Wu Yunsheng (吴运声), Tencent Cloud's lead on the product, noted that ADP's customer count at least doubled year-over-year, driven by stronger Agent Loop capabilities and lower customer education costs, with benchmark cases showing 50% efficiency gains at a medical group and 70%+ development efficiency improvements at a telecom operator.

rss · 36氪 · Jul 20, 01:30

**Background**: ADP stands for Agent Development Platform, an enterprise-grade AgentOps platform covering the full lifecycle of AI agents — building, distribution, and governance. AgentOps is an emerging discipline focused on running AI agents in production environments, emphasizing governance, observability, tool control, human oversight, and cost management. The Claw mode mentioned in the article is a feature of ADP that allows agents to be deployed across multiple channels. Wu Yunsheng also clarified that WorkBuddy (Tencent's personal AI assistant) and ADP serve different use cases — WorkBuddy is like a personal assistant invisible to enterprise management, while ADP provides transparent, auditable agents for team use.

<details><summary>References</summary>
<ul>
<li><a href="https://news.aibase.com/news/28683">Tencent Cloud ADP 4.0 Launch: Claw Mode Enables Agents to Be...</a></li>
<li><a href="https://eu.36kr.com/en/p/3846786158086665">Tencent 's Determination to Regain Ground in the Agent Field</a></li>
<li><a href="https://www.uipath.com/blog/ai/agent-ops-operationalizing-ai-agents-for-enterprise">AgentOps and operationalizing AI agents for the enterprise ...</a></li>

</ul>
</details>

**Tags**: `#Tencent Cloud`, `#enterprise AI`, `#agent platform`, `#ADP`, `#WAIC 2026`

---

<a id="item-9"></a>
## [8点1氪丨长鑫科技中签号出炉：共约770.22万个；西班牙1-0战胜阿根廷，夺得本届世界杯冠军；月之暗面有望最快6个月内赴港上市](https://36kr.com/p/3903220264404608?f=rss) ⭐️ 6.3/10

A daily Chinese tech/business news roundup highlighting Moonshot AI's potential Hong Kong IPO, CXMT's IPO lottery results, a World Cup final result, and other miscellaneous business and economic news.

rss · 36氪 · Jul 20, 00:05

**Tags**: `#Moonshot AI`, `#IPO`, `#CXMT`, `#semiconductors`, `#China tech`

---

<a id="item-10"></a>
## [工信部：将加快出台人工智能+软件行动方案](https://36kr.com/newsflashes/3903399623542657?f=rss) ⭐️ 6.3/10

China's MIIT announces plans to accelerate an 'AI + Software' action plan promoting intelligent software development, AI-driven software products/services, and AI agent software ecosystems.

rss · 36氪 · Jul 20, 03:03

**Tags**: `#China policy`, `#AI policy`, `#software development`, `#AI agents`, `#government announcement`

---

<a id="item-11"></a>
## [工信部：将印发算力标准体系建设指南，推动建立算力市场化定价等标准](https://36kr.com/newsflashes/3903384861771649?f=rss) ⭐️ 6.3/10

China's MIIT announces plans to issue computing power standard体系建设 guidelines, promoting market-based pricing standards and optimizing compute infrastructure deployment amid surging AI demand.

rss · 36氪 · Jul 20, 02:48

**Tags**: `#China`, `#compute infrastructure`, `#AI policy`, `#regulation`, `#smart computing`

---

<a id="item-12"></a>
## [China's intelligent computing power reaches 2185 EFLOPS](https://36kr.com/newsflashes/3903375424522113?f=rss) ⭐️ 6.3/10

On July 20, 2025, at a State Council Information Office press conference, Xie Cun, Director of the Information and Communications Administration Bureau under the Ministry of Industry and Information Technology (MIIT), announced that China's intelligent computing power had reached 2185 EFLOPS by the end of June 2025, with an overall rack utilization rate (上架率) of 71.4% across national compute facilities. Over 70 compute corridors have been built around national hub nodes in the past two years, improving inter-node network performance by 10%. This data point offers one of the clearest official measurements yet of China's rapidly scaling AI compute capacity, reinforcing its position as a global leader in AI infrastructure investment. The 71.4% utilization rate suggests that a significant share of deployed hardware is already productive, signaling effective demand matching supply rather than idle overbuilding. One EFLOPS equals 10^18 (one quintillion) floating-point operations per second, making 2185 EFLOPS an exascale-class figure. The 71.4% "rack utilization rate" (上架率) refers to the proportion of physically installed servers that have been commissioned and are serving workloads. The 70+ compute corridors are part of the national backbone linking eight approved hub nodes under the "East Data West Computing" (东数西算) initiative.

rss · 36氪 · Jul 20, 02:38

**Background**: EFLOPS (Exa Floating-point Operations Per Second) is a standard unit for measuring supercomputing performance, where 1 EFLOPS equals one quintillion (10^18) floating-point operations per second. "Intelligent computing power" (智能算力) refers specifically to compute resources optimized for AI workloads such as model training and inference, as distinct from general-purpose compute. China's "East Data West Computing" (东数西算) project, formally launched in February 2022, designates eight national hub nodes (in the Beijing-Tianjin-Hebei region, the Yangtze River Delta, the Guangdong-Hong Kong-Macao Greater Bay Area, Chengdu-Chongqing, Inner Mongolia, Guizhou, Gansu, and Ningxia) and ten national data center clusters, designed to channel data-intensive workloads from eastern demand centers to western regions with cheaper land, cooler climates, and more abundant energy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Floating_point_operations_per_second">Floating point operations per second - Wikipedia</a></li>
<li><a href="https://www.gov.cn/zhengce/zhengceku/202401/content_6924596.htm">关于深入实施“东数西算”工程加快构建全国一体化算力网的实施意见_国务...</a></li>
<li><a href="https://www.iii.tsinghua.edu.cn/info/1121/2978.htm">“东数西算”工程正式全面启动，一图读懂 “东数西算”工程核心要点</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#China tech`, `#compute capacity`, `#government policy`, `#data centers`

---

<a id="item-13"></a>
## [What I learned selling 2,500 MIDI recorders: Hardware is not so hard](https://chipweinberger.com/articles/20260719-hardware-is-not-so-hard) ⭐️ 6.0/10

A hardware entrepreneur shares lessons learned from selling 2,500 MIDI recorders (JamCorders), arguing hardware is more accessible than commonly believed, though community discussion pushes back on this simplification.

hackernews · chipweinberger · Jul 19, 10:34 · [Discussion](https://news.ycombinator.com/item?id=48966713)

**Tags**: `#hardware`, `#entrepreneurship`, `#startup`, `#maker`, `#product-development`

---

<a id="item-14"></a>
## [AMD Medusa Point 10-Core APU Leaks New Geekbench Record](https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test) ⭐️ 5.5/10

A leaked Geekbench result for AMD's upcoming 10-core Medusa Point mobile APU shows the chip posting its highest score yet, reportedly outperforming every other x86 mobile processor in the single-core test. The benchmark marks the third time this particular SKU has surfaced, with each leak showing progressively better scores compared to earlier Gorgon Point and Strix Point parts. If these leaked results hold up in shipping silicon, Medusa Point would represent AMD's most significant mobile performance leap in recent generations, potentially reshaping the competitive landscape against Intel's x86 mobile lineup. For laptop buyers and OEMs, it signals that high single-core performance for thin-and-light and mainstream notebooks is set to take a major step forward in the next product cycle. The leaked part is a 10-core SKU from the Ryzen AI 500 (Medusa Point) family, based on Zen 6 architecture, using the FP10 socket and available in 28 W and 45 W TDP variants. Medusa Point is said to feature a hybrid core design with trimmed-down integrated graphics, and it succeeds the Gorgon Point (Ryzen AI 400) generation, which itself was largely a refresh of Strix Point and Krackan Point silicon.

rss · Tom's Hardware · Jul 19, 14:35

**Background**: An APU (Accelerated Processing Unit) is AMD's term for a processor that combines a CPU and an integrated GPU on a single die, commonly used in laptops and budget desktops. Medusa Point is the codename for AMD's next-generation mobile APU lineup (Ryzen AI 500 series), built on the Zen 6 architecture and succeeding the Strix Point and Gorgon Point families. Geekbench is a widely used cross-platform benchmarking tool that measures single-core and multi-core CPU performance, though its results from pre-release hardware are unofficial and depend on drivers, cooling, and power configurations that may differ from retail units.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/cpus/amds-next-gen-10-core-medusa-point-apu-shows-up-on-geekbench-again-with-its-best-score-yet-leaked-sku-outpaces-every-other-x86-mobile-chip-in-the-single-core-test">AMD's next-gen 10-core 'Medusa Point' APU shows up on ...</a></li>
<li><a href="https://www.techpowerup.com/343682/amd-zen-6-based-medusa-point-apu-comes-in-28-w-and-45-w-tdps">AMD Zen 6-Based "Medusa Point" APU Comes in 28 W and 45 W ...</a></li>
<li><a href="https://videocardz.com/newz/amd-next-gen-medusa-point-zen6-apu-with-high-and-low-tdp-settings-spotted-in-shipping-manifest">AMD next-gen "Medusa Point" Zen6 APU with High and Low TDP ...</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#CPUs`, `#benchmarks`, `#mobile-computing`, `#leaks`

---

<a id="item-15"></a>
## [Zilog Z80 turns 50 as an open-source replacement heads to drop-in DIP40 silicon — iconic 8-bit CPU launched in July 1976 and was discontinued in 2024](https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon) ⭐️ 5.5/10

Zilog Z80 celebrates its 50th anniversary while an open-source drop-in replacement heads to DIP40 silicon.

rss · Tom's Hardware · Jul 19, 14:12

**Tags**: `#retro-computing`, `#open-source-hardware`, `#Z80`, `#computing-history`, `#CPU`

---

<a id="item-16"></a>
## [Memory chip boss admits RAM prices are 'abnormally high' — SK Group chairman considering building a semiconductor plant in the US to expand supply, calm ‘chipflation’](https://www.tomshardware.com/tech-industry/policy/memory-chip-boss-admits-ram-prices-are-abnormally-high-sk-group-chairman-considering-building-a-semiconductor-plant-in-the-us-to-expand-supply-calm-chipflation) ⭐️ 5.5/10

SK Group chairman acknowledges abnormally high RAM prices and considers building a US semiconductor plant to increase supply and stabilize the memory market.

rss · Tom's Hardware · Jul 19, 13:55

**Tags**: `#semiconductors`, `#RAM`, `#supply-chain`, `#hardware`, `#industry-news`

---

<a id="item-17"></a>
## [Russian drones spotted using screwed-on magnetic compasses as navigation aids — the on-board camera can occasionally tilt down to check bearings if satellite comms are lost](https://www.tomshardware.com/tech-industry/drones/russian-drones-spotted-using-screwed-on-magnetic-compasses-as-navigation-aids-the-on-board-camera-can-occasionally-tilt-down-to-check-bearings-if-satellite-comms-are-lost) ⭐️ 5.5/10

Russian drones have been observed using cheap magnetic compasses as backup navigation aids, with cameras tilting down to verify bearings when satellite communications are lost.

rss · Tom's Hardware · Jul 19, 12:05

**Tags**: `#drones`, `#navigation`, `#electronic-warfare`, `#GPS-denied-environment`, `#military-technology`

---

<a id="item-18"></a>
## [MSI Previews Liquid-Cooled AMD EPYC Venice Dual-Socket Server at Computex](https://www.servethehome.com/msi-slyly-shows-off-an-upcoming-dlc-amd-epyc-venice-platform-with-cd182-s6091-x2-servers-and-racks/) ⭐️ 5.5/10

At Computex, MSI quietly displayed its upcoming CD182-S6091-X2 (DLC), a direct liquid-cooled dual-socket server node in a 1OU2N form factor, built on AMD's next-generation EPYC Venice platform. This is one of the earliest public showings of a server OEM's Venice-based platform, signaling that AMD's Zen 6-based server silicon is nearing readiness for hyperscale and enterprise deployment. The combination of dual-socket density and direct liquid cooling points to where high-core-count server design is heading for AI and cloud workloads. The 1OU2N form factor packs two compute nodes into a single 1U enclosure, maximizing rack density, while the DLC (direct liquid cooling) design suggests the platform is engineered to handle the higher thermal envelopes expected from Venice's increased core counts. No detailed specs on core counts, memory channels, or power draw were disclosed at the show.

rss · ServeTheHome · Jul 19, 18:00

**Background**: AMD EPYC Venice is the codename for AMD's next-generation server processors based on the Zen 6 architecture, manufactured on TSMC's N2 (2nm-class) process, with configurations reportedly scaling up to 256 cores. It will use new SP7 and SP8 socket platforms supporting up to 16-channel memory and 128 PCIe 6.0 lanes. Direct liquid cooling (DLC) is rapidly becoming the standard for high-density data center servers because air cooling cannot adequately dissipate the heat generated by modern multi-hundred-watt CPUs and accelerators. The 1OU2N form factor refers to a 1 Open U chassis housing two independent server nodes, a design popularized in hyperscale environments to maximize compute density per rack unit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/newsroom/press-releases/2026-5-20-amd-announces-production-ramp-of-next-generation-a.html">AMD Announces Production Ramp of Next-Generation AMD EPYC ...</a></li>
<li><a href="https://wccftech.com/amd-sp7-sp8-platforms-epyc-venice-verano-cpus-12800-mtps-16-channel-memory-128-pcie-6-0-lanes/">AMD SP7 & SP8 Platforms For Next-Gen EPYC “Venice” & “Verano ...</a></li>
<li><a href="https://www.computacenter.com/en-us/who-we-are/blogs/direct-liquid-cooling--the-new-gold-standard-for-data-centers">Direct Liquid Cooling: The new gold standard for data centers</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#EPYC`, `#servers`, `#data-center`, `#hardware`

---