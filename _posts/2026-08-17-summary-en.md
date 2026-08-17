---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 34 items, 15 important content pieces were selected

---

1. [Critical macOS Screen Sharing Flaw Exploited for Root Access and Monero Mining](#item-1) ⭐️ 9.5/10
2. [Stripe to Acquire OpenRouter for Over $7 Billion in AI Push](#item-2) ⭐️ 8.0/10
3. [Google Reportedly Taps AMD for Next-Gen TPU with On-Package CPU Cores](#item-3) ⭐️ 7.5/10
4. [Ukrainian drone regiment decimates U.S. armored brigade in war games](#item-4) ⭐️ 7.5/10
5. [Third-World Engineer Defends RISC-V's Value in Embedded Systems](#item-5) ⭐️ 7.0/10
6. [Anthropic Publishes Claude System Prompts with Community Tracking Tools](#item-6) ⭐️ 7.0/10
7. [Cloudflare silently injects JS analytics beacon into sites after nameserver switch](#item-7) ⭐️ 7.0/10
8. [3D-Printed Ultrasonic Resonators Power Silent Micro-Drone Flight](#item-8) ⭐️ 6.5/10
9. [St Lucie Nuclear Reactor Unit 1 manually shutdown, 3 control rods drop into core](#item-9) ⭐️ 6.0/10
10. [Maker compresses 2.9MB song 1000x with Meta's AI codec and encodes as QR codes](#item-10) ⭐️ 5.5/10
11. [Ukraine's MICH 2000 drone, a $48K Chinese clone, destroys Russian Tu-95 bomber](#item-11) ⭐️ 5.5/10
12. [Intel to Launch New Core Architecture on Desktop First with Nova Lake](#item-12) ⭐️ 5.5/10
13. [Modern OLEDs are just as vulnerable to burn-in as 2017 panels in 10,000-hour test — twice the brightness and 27% efficiency gains offer crucial headroom](#item-13) ⭐️ 5.5/10
14. [Ex-farm bureau chief invites AI data center developers to buy his land —argues blocked $6.3B project will just move to willing neighbors, defies 500-jurisdiction moratorium wave and 70% public opposition](#item-14) ⭐️ 5.5/10
15. [ADT R27A-BK3 EDSFF E1.S/E3.S to PCIe Gen5 Adapter Review](#item-15) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Critical macOS Screen Sharing Flaw Exploited for Root Access and Monero Mining](https://www.tomshardware.com/tech-industry/cyber-security/macos-screen-sharing-flaw-exploited-to-root-macs-and-plant-monero-miners) ⭐️ 9.5/10

A critical authentication bypass vulnerability (CVE-2026-65400) in macOS Screen Sharing is being actively exploited by attackers to gain root access and install Monero cryptocurrency miners, according to the Dutch National Cyber Security Centre (NCSC-NL). CISA has rated this vulnerability at a near-maximum severity of 9.8 out of 10, meaning any Mac with Screen Sharing enabled is potentially exposed to remote root compromise without requiring valid credentials. The flaw is an authentication bypass that lets attackers skip credential checks entirely, granting root-level control without valid login details; Monero is favored by cryptojackers because its privacy-focused features make mining transactions difficult to trace.

rss · Tom's Hardware · Aug 16, 13:00

**Background**: macOS Screen Sharing is built on the VNC (Virtual Network Computing) protocol, an open standard that allows remote desktop access and control across multiple platforms. An authentication bypass vulnerability enables an unauthenticated attacker to escalate privileges on a device or application without presenting valid credentials, effectively tricking the system into believing the attacker is already authenticated. Cryptojacking is an attack technique in which malicious actors install mining scripts on compromised machines to secretly generate cryptocurrency, with Monero being a common target due to its anonymity-focused design.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lifewire.com/how-to-enable-mac-screen-sharing-2260830">Mac Screen Sharing</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/identity-security/authentication-bypass/">What Is Authentication Bypass? Techniques & Examples - SentinelOne</a></li>
<li><a href="https://d2lvhbqifib4zm.cloudfront.net/blog/what-is-cryptojacking/">What is cryptojacking ? Definition, detection, and prevention guide</a></li>

</ul>
</details>

**Tags**: `#macOS`, `#security`, `#vulnerability`, `#cryptojacking`, `#CVE-2026-65400`

---

<a id="item-2"></a>
## [Stripe to Acquire OpenRouter for Over $7 Billion in AI Push](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 8.0/10

Stripe is reportedly finalizing an acquisition of OpenRouter, a leading LLM routing and AI model marketplace, for more than $7 billion. The deal would bring OpenRouter's unified API platform—which connects developers to over 400 AI models from 60+ providers—under Stripe's ownership. This acquisition signals Stripe's strategic expansion from payment processing into core AI infrastructure, leveraging its expertise in high-volume, low-latency API services to own the financial and routing rails of the AI economy. It positions Stripe at the center of a rapidly growing market where tokens and model usage are becoming as critical as traditional payment flows. OpenRouter had previously raised funding at a $1.3 billion valuation just months before this deal, meaning the $7B+ price represents roughly a 5x markup for early investors. The platform serves as a meta-layer that abstracts away the complexity of managing multiple LLM provider integrations, consolidating billing and authentication into a single endpoint with an OpenAI-compatible API.

hackernews · zacharyozer · Aug 16, 20:31 · [Discussion](https://news.ycombinator.com/item?id=49323381)

**Background**: OpenRouter is a unified API gateway and marketplace that routes requests across hundreds of large language models from providers including OpenAI, Anthropic, Mistral, and Google. LLM routing, the core technique OpenRouter employs, involves automatically selecting the most appropriate model for a given query based on factors like cost, speed, and reliability—similar to how an air traffic controller directs flights. Stripe, founded by the Collison brothers, is one of the world's largest payment processing platforms, handling trillions of dollars in annual volume and known for building highly reliable, developer-friendly financial APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/about">About - The Unified Interface For LLMs | OpenRouter</a></li>
<li><a href="https://www.codecademy.com/article/what-is-openrouter">What is OpenRouter? A Guide with Practical Examples</a></li>
<li><a href="https://research.ibm.com/blog/LLM-routers">LLM routing for quality, low-cost responses - IBM Research</a></li>

</ul>
</details>

**Discussion**: Commenters are divided on strategic rationale: some view the acquisition as a natural extension of Stripe's API expertise into LLM infrastructure, while others question the high valuation given OpenRouter's role as a middleman. A key insight raised is that OpenRouter and OpenAI together represent roughly $100B in payment volume—about 5% of Stripe's total—making owning that volume directly strategically important. Several commenters noted the rapid valuation jump from $1.3B to $7B+ as an extraordinary return for investors.

**Tags**: `#stripe`, `#openrouter`, `#acquisition`, `#ai-infrastructure`, `#llm-routing`

---

<a id="item-3"></a>
## [Google Reportedly Taps AMD for Next-Gen TPU with On-Package CPU Cores](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning) ⭐️ 7.5/10

A rumor suggests Google is partnering with AMD to design next-generation TPUs that integrate on-package CPU cores specifically optimized for agentic and reinforcement learning workloads, representing a potential shift toward hybrid AI ASIC designs. If confirmed, this collaboration would introduce a new competitor into the custom AI silicon space dominated by NVIDIA and signal Google's recognition that reinforcement learning and agentic AI workloads require different hardware characteristics than the pure matrix multiplication workloads current TPUs are optimized for. The proposed 'hybrid AI ASIC' would reportedly combine AMD's CPU core IP (likely Zen-based) with Google's TPU matrix compute capabilities on a single package using chiplet-based heterogeneous integration, targeting the low-latency inference and tight decision loops required for RL training rather than pure tensor throughput.

rss · Tom's Hardware · Aug 16, 12:40

**Background**: Google's Tensor Processing Units (TPUs) are custom ASICs designed for neural network workloads, using systolic array architectures that efficiently process matrix multiplications by streaming data through thousands of ALUs. TPUs currently power both training and inference of large language and other deep learning models in Google Cloud. AMD is a major CPU and GPU designer whose Zen CPU architectures and CDNA GPU accelerators compete across the broader compute market. Recently, a new class of 'agentic' AI workloads — where models perform multi-step reasoning, planning, and decision-making — has emerged, often leveraging reinforcement learning techniques that require tight coupling between compute-heavy tensor operations and fast sequential decision logic traditionally handled by CPUs. Heterogeneous integration via chiplets allows different silicon dies to be combined in a single package, enabling tighter data exchange and better performance-per-watt than separate chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.cadence.com/en_US/home/resources/white-papers/chiplets-and-heterogeneous-packaging-are-changing-system-design-and-analysis-wp.html">Chiplets and Heterogeneous Packaging Are Changing System Design and Analysis White Paper | Cadence</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Google TPU`, `#AMD`, `#reinforcement learning`, `#ASIC design`

---

<a id="item-4"></a>
## [Ukrainian drone regiment decimates U.S. armored brigade in war games](https://www.tomshardware.com/tech-industry/drones/ukrainian-drone-regiment-decimates-3-500-strong-u-s-armored-brigade-combat-team-in-war-game-reveals-shortcomings-in-american-response-as-drones-easily-spotted-and-destroyed-tanks-and-heavy-armored-vehicles) ⭐️ 7.5/10

A Ukrainian drone regiment decisively defeated the U.S. Army's 3rd Brigade Combat Team (3rd BCT) of the 1st Cavalry Division during military war games, with drones easily spotting and destroying American tanks and armored vehicles despite the brigade fielding anti-drone units. This exercise reveals critical vulnerabilities in U.S. military doctrine and equipment against modern drone warfare, potentially forcing a fundamental rethink of armored force structure, counter-drone capabilities, and tactical doctrine as drone threats continue to evolve on battlefields worldwide. The high drone kill-rate forced continuous 'respawns' of the U.S. force, indicating that even dedicated anti-drone units were insufficient to neutralize the threat. The 3rd BCT is a roughly 4,400-4,700-strong armored formation whose tanks and heavy vehicles proved easy targets for the Ukrainian drone operators.

rss · Tom's Hardware · Aug 16, 10:00

**Background**: A Brigade Combat Team (BCT) is the basic deployable maneuver unit of the U.S. Army, typically consisting of about 4,400 to 4,700 personnel depending on variant, with armored BCTs equipped with main battle tanks and heavy armored vehicles. War games employ an Opposing Force (OPFOR) to realistically simulate enemy tactics and stress-test friendly forces. Counter-UAS (C-UAS) capabilities—including jamming systems, directed-energy weapons, and retrofitted kinetic solutions—have become an increasing focus for the U.S. military, yet the Army's doctrine states that counter-UAS is 'not a stand-alone effort or the sole responsibility of any warfighting function,' and no dedicated Military Occupational Specialty (MOS) exists for the role.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brigade_Combat_Team">Brigade Combat Team - Wikipedia</a></li>
<li><a href="https://www.cbo.gov/sites/default/files/114th-congress-2015-2016/reports/51535-fsprimerbreakoutchapter2.pdf">The U.S. Militarys Force Structure : A Primer</a></li>
<li><a href="https://www.congress.gov/crs-product/R48477">Department of Defense Counter Unmanned Aircraft Systems: Background and Issues for Congress | Congress.gov | Library of Congress</a></li>

</ul>
</details>

**Tags**: `#military-tech`, `#drone-warfare`, `#defense-strategy`, `#ukraine-conflict`, `#war-games`

---

<a id="item-5"></a>
## [Third-World Engineer Defends RISC-V's Value in Embedded Systems](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

An embedded engineer from a developing country published a blog post responding to earlier criticism of RISC-V, arguing that the ISA's true strength lies in embedded applications where cost, accessibility, and customizability are more important than raw compute performance compared to ARM64 or x86. This perspective highlights a dimension often missing from mainstream RISC-V discourse, which tends to focus on competition with ARM and x86 in high-performance computing. It spotlights how open ISA economics matter for engineers in regions with supply-chain and cost constraints, potentially influencing RISC-V adoption strategy in emerging markets. The author's argument centers on the practical reality that in his country, a $1 chip can cost $60–$200 to ship, making the price difference between a 10-cent RISC-V part and a $1 ARM part highly significant. He acknowledges RISC-V's fragmentation and performance trade-offs but contends these are acceptable trade-offs for custom embedded silicon where binary distribution is less critical.

hackernews · Narishma · Aug 16, 17:01 · [Discussion](https://news.ycombinator.com/item?id=49321717)

**Background**: RISC-V is an open-standard instruction set architecture (ISA) based on reduced instruction set computing principles, designed to be simple, modular, and freely licensable. Unlike proprietary ISAs such as ARM or x86, RISC-V allows anyone to design and manufacture compatible processors without licensing fees. This makes it particularly attractive for embedded systems, IoT devices, and custom silicon, though it competes against more mature ecosystems in mobile and server computing.

<details><summary>References</summary>
<ul>
<li><a href="https://lucaberton.com/blog/risc-v-vs-arm-vs-x86-isa-comparison/">RISC - V vs ARM vs x 86 : How the Open ISA Compares</a></li>
<li><a href="https://www.linkedin.com/learning/getting-started-with-risc-v/what-is-risc-v">What is RISC - V ? - Raspberry Pi Video Tutorial | LinkedIn Learning...</a></li>
<li><a href="https://picockpit.com/raspberry-pi/arm-vs-risc-v-vs-x86/">A Simple Guide to ARM vs . RISC - V vs . x 86 | PiCockpit</a></li>

</ul>
</details>

**Discussion**: 社区评论者看法不一。一些人称赞这一视角丰富了RISC-V的讨论，但也有评论者指出成本论证中的逻辑矛盾——作者一方面抱怨1美元的芯片运费高达60至200美元，另一方面却声称RISC-V让零件价格降至十分之一；如果运费占主导成本，这种说法似乎自相矛盾。还有人援引历史先例，指出x86最终在原始性能上超越了MIPS、SPARC和Alpha等RISC架构，表明RISC-V的性能差距有可能随时间缩小。

**Tags**: `#risc-v`, `#embedded-systems`, `#hardware-architecture`, `#developing-world-tech`, `#isa-design`

---

<a id="item-6"></a>
## [Anthropic Publishes Claude System Prompts with Community Tracking Tools](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 7.0/10

Anthropic has published the official system prompts used by its Claude models on its platform documentation site, making the hidden instructions that shape model behavior publicly accessible. Developer Simon Willison has built a Git-based tool that archives these prompts as a commit history, enabling easy diff comparison across versions such as the Opus 4.8 to Opus 5 transition. System prompts define a model's role, tone, and behavioral boundaries, and seeing them publicly is rare and valuable for AI transparency. This resource helps prompt engineers understand how leading AI labs structure their internal instructions and gives the community a baseline for comparing model behavior across vendors. The published prompts include detailed behavioral rules such as instructing Claude to verify whether an image is actually present before responding to image-related queries, rather than assuming one based on the prompt text. Version diffs reveal additions referencing internal codenames like 'Claude Fable 5' and 'Claude Mythos 5,' hinting at Anthropic's product roadmap or internal naming conventions.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Background**: A system prompt is a set of hidden instructions provided to a large language model before any user message, defining the model's persona, constraints, and response style. It takes precedence over user inputs and shapes all subsequent interactions. Prompt engineering is the practice of crafting these instructions and user queries to elicit optimal model behavior. Transparency around system prompts is uncommon among major AI vendors, making Anthropic's publication noteworthy for the research and developer community.

<details><summary>References</summary>
<ul>
<li><a href="https://promptengineering.org/system-prompts-in-large-language-models/">System Prompts in Large Language Models</a></li>
<li><a href="https://www.kern-it.be/en/definitions/system-prompt/">System prompt: the hidden instruction that frames your LLM | KERN-IT</a></li>

</ul>
</details>

**Discussion**: Community members expressed mixed views: Simon Willison contributed a valuable version-tracking tool, while SwellJoe questioned why the system prompts are so lengthy given recent industry advice favoring shorter, more focused context files. ololobus noted surprise that basic common-sense checks (like verifying image presence) are still enforced via system prompt rather than being inherent to the model's capabilities, a sentiment echoed for newer models like Fable 5. Separately, user quaintdev raised concerns about community forum moderation regarding AI-critical content.

**Tags**: `#claude`, `#anthropic`, `#prompt-engineering`, `#ai-transparency`, `#llm`

---

<a id="item-7"></a>
## [Cloudflare silently injects JS analytics beacon into sites after nameserver switch](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

A user on Hacker News reported that Cloudflare silently injects a JavaScript analytics beacon (static.cloudflareinsights.com/beacon.min.js) into HTML-only, JavaScript-free websites when their nameservers are pointed at Cloudflare, even before the site owner explicitly enables analytics in the dashboard. The injection is opt-out rather than opt-in, meaning users must actively navigate to the Analytics dashboard and disable a snippet that was never requested. This is a significant privacy and trust concern because site operators who deliberately maintain JavaScript-free or privacy-respecting websites are unknowingly having third-party tracking scripts injected without their consent. Because Cloudflare is one of the largest internet infrastructure providers, the default-on behavior affects potentially millions of proxied domains and raises broader questions about transparency from infrastructure vendors. The injected beacon loads from static.cloudflareinsights.com/beacon.min.js with version "2024.11.0" and embeds a unique token in its data-cf-beacon attribute. Injection only happens when traffic is proxied through Cloudflare (the orange-cloud DNS setting), not for DNS-only setups, because HTML modification requires terminating HTTPS connections. Workarounds include disabling the snippet via the Web Analytics dashboard or using a Content-Security-Policy header with a strict script-src directive.

hackernews · stagas · Aug 16, 17:49

**Background**: Cloudflare provides a layered set of services: DNS hosting, reverse-proxy/CDN, object storage (R2), and Web Analytics. Web Analytics operates in two distinct modes: edge analytics, which Cloudflare measures directly at its network edge without touching page content, and a RUM (Real User Monitoring) beacon, which is a JavaScript snippet injected into pages to collect browser-side performance metrics. The controversy here centers on the RUM beacon appearing to be automatically activated for newly proxied sites, rather than requiring an explicit opt-in from the site owner, which contradicts the expectation of users who select Cloudflare solely for DNS or R2 access.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/speed/observatory/rum-beacon/">RUM beacon for Web Analytics · Cloudflare Speed docs</a></li>
<li><a href="https://cloudflare-docs.cloudflare-docs.workers.dev/web-analytics/faq/">Answers to common questions about Cloudflare Web Analytics .</a></li>
<li><a href="https://developers.cloudflare.com/r2/">Overview · Cloudflare R 2 docs</a></li>

</ul>
</details>

**Discussion**: Community members confirmed the behavior on their own sites, sharing identical beacon.min.js snippets, and proposed workarounds such as a Content-Security-Policy meta tag restricting script-src to 'self'. Several commenters clarified that the injection only occurs when Cloudflare terminates HTTPS as a proxy (orange-cloud), not for DNS-only setups, which another user verified by checking DNS-only domains and finding no analytics enabled. The thread also referenced Cloudflare's own blog post about enabling web analytics, suggesting the behavior is documented but not surfaced clearly to users configuring DNS for services like R2.

**Tags**: `#cloudflare`, `#privacy`, `#web-infrastructure`, `#analytics`, `#security`

---

<a id="item-8"></a>
## [3D-Printed Ultrasonic Resonators Power Silent Micro-Drone Flight](https://www.tomshardware.com/3d-printing/3d-printed-sound-powered-jet-engines-propel-micro-drones-fliers-are-completely-silent-researchers-use-ultrasonic-frequencies-to-drive-12-000-rpm-silent-hovering-fliers) ⭐️ 6.5/10

Researchers have demonstrated 3D-printed resonators that, when excited at specific ultrasonic frequencies, generate thrust via acoustic streaming, enabling a silent flier to hover while spinning its propulsion rotors at over 12,000 RPM. Silent propulsion could enable new applications in surveillance, indoor monitoring, and stealth operations where conventional rotor noise is a limitation. It also points to a low-cost, 3D-printable pathway for manufacturing micro aerial vehicles that could complement or replace existing MEMS-based micro-propulsion approaches. The propulsion relies on acoustic streaming — a nonlinear phenomenon where high-amplitude sound waves drive a steady fluid flow — rather than conventional spinning blades. Because the driving frequencies are ultrasonic (above ~20 kHz), they are inaudible to humans, though current prototypes do not yet produce thrust sufficient for practical payloads or flight endurance.

rss · Tom's Hardware · Aug 16, 11:50

**Background**: Acoustic streaming was first described by Lord Rayleigh in 1884 and refers to the steady flow generated in a fluid when it absorbs high-amplitude acoustic oscillations; it is widely used in microscale acoustofluidic devices. Micro air vehicles are generally defined as ultra-lightweight flying platforms with a maximum wingspan of about 15 cm and a weight under 20 grams, where conventional propellers are difficult to miniaturize efficiently. Ultrasonic frequencies fall above the human hearing range (~20 kHz), which is what allows these devices to operate almost inaudibly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Acoustic_streaming">Acoustic streaming - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/3d-printing/3d-printed-sound-powered-jet-engines-propel-micro-drones-fliers-are-completely-silent-researchers-use-ultrasonic-frequencies-to-drive-12-000-rpm-silent-hovering-fliers">3 D - printed sound-powered jet engines propel micro... | Tom's Hardware</a></li>
<li><a href="https://www.researchgate.net/publication/295277075_Design_and_Development_of_Ultrasonic_Jet_Array_UJA_for_Micro_Propulsion">Design and Development of Ultrasonic Jet Array (UJA) for Micro ...</a></li>

</ul>
</details>

**Tags**: `#drones`, `#3D-printing`, `#acoustics`, `#micro-robotics`, `#research`

---

<a id="item-9"></a>
## [St Lucie Nuclear Reactor Unit 1 manually shutdown, 3 control rods drop into core](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core) ⭐️ 6.0/10

St Lucie Nuclear Reactor Unit 1 manually shut down after 3 control rods dropped into the core, with community discussion explaining this as a designed fail-safe mechanism in pressurized water reactors.

hackernews · toomuchtodo · Aug 16, 15:16 · [Discussion](https://news.ycombinator.com/item?id=49320856)

**Tags**: `#nuclear-safety`, `#safety-critical-systems`, `#fail-safe-design`, `#reactor-physics`, `#incident-report`

---

<a id="item-10"></a>
## [Maker compresses 2.9MB song 1000x with Meta's AI codec and encodes as QR codes](https://www.tomshardware.com/tech-industry/maker-compresses-a-2-9mb-song-1000-times-with-metas-ai-codec-and-prints-it-on-paper-as-eight-qr-codes) ⭐️ 5.5/10

A maker used Meta's open-source EnCodec neural audio codec to compress a 2.9MB song down to approximately 21KB — roughly 1000 times smaller — and then encoded the compressed data into eight QR codes printable on paper. Playback requires a neural network decoder to reconstruct the two-minute audio from the compressed discrete tokens. This project demonstrates the extreme compression capabilities of modern neural audio codecs and creatively showcases a physical medium (paper) for storing audio data. It highlights how AI-based compression can dramatically reduce storage and transmission costs for audio, though it also illustrates the trade-off that playback depends on specialized neural network software rather than standard media players. EnCodec was released by Meta in 2022 as an open-source neural audio codec supporting stereophonic audio at 48 kHz with bitrates of 3, 6, 12, and 24 kbps. The codec uses an encoder-quantizer-decoder pipeline with residual vector quantization to convert waveforms into discrete tokens, which is what enables such extreme compression ratios compared to traditional formats like MP3 or AAC.

rss · Tom's Hardware · Aug 16, 14:22

**Background**: Neural audio codecs are AI-based systems that compress audio into discrete tokens using deep learning, enabling high-fidelity reconstruction at much lower bitrates than traditional codecs like MP3 or AAC. Meta's EnCodec was among the first neural codecs to support high-quality stereo 48 kHz audio. Unlike traditional compression, which relies on hand-crafted mathematical algorithms, neural codecs learn statistical patterns from data and require a trained neural network for both encoding and decoding. This means files compressed with EnCodec are not playable on standard media players — they need the corresponding neural model to decode the tokens back into a listenable waveform.

<details><summary>References</summary>
<ul>
<li><a href="https://audiocraft.metademolab.com/encodec.html">EnCodec</a></li>
<li><a href="https://github.com/facebookresearch/encodec">GitHub - facebookresearch/ encodec : State-of-the-art deep learning...</a></li>
<li><a href="https://www.forasoft.com/learn/audio-for-video/glossary/terms-audio/encodec">EnCodec</a></li>

</ul>
</details>

**Tags**: `#audio-compression`, `#neural-codecs`, `#Meta-EnCodec`, `#creative-projects`, `#maker`

---

<a id="item-11"></a>
## [Ukraine's MICH 2000 drone, a $48K Chinese clone, destroys Russian Tu-95 bomber](https://www.tomshardware.com/tech-industry/drones/ukraine-destroys-tu-95-bomber-using-48000-chinese-drone-clone) ⭐️ 5.5/10

Ukraine's MICH 2000 long-range strike drone, reverse-engineered from a Chinese civilian flying-wing airframe (ZTK-150) after covert factory photography, successfully destroyed a Russian Tu-95MS strategic bomber at the Engels-2 air base. The drone costs approximately $48,000 per unit, has a 2,000 km range, carries up to 60 kg of explosives, and is now produced at a rate of 6,000 units per year with 85% Ukrainian domestic content. This event demonstrates how rapid industrial reverse-engineering combined with distributed manufacturing can produce cost-effective deep-strike capabilities against high-value strategic assets. The destruction of a Tu-95MS is especially significant because only about 60 remain in Russia's Long-Range Aviation, and each is irreplaceable since the bomber has not been produced in decades. The MICH 2000 was developed by Ukraine's SBU Alfa unit starting from a Chinese civilian airframe purchased in 2023; two years of work localized engines, warheads, fuselages, and rocket boosters across dozens of Ukrainian suppliers. Its flying-wing configuration provides aerodynamic efficiency for long endurance, and the entire weapon system costs less than 1% of the value of a strategic bomber it can destroy.

rss · Tom's Hardware · Aug 16, 13:20

**Background**: The Tupolev Tu-95 'Bear' is a Soviet-era turboprop strategic bomber that first flew in 1952 and has been a cornerstone of Russia's nuclear-capable long-range aviation for decades. The Tu-95MS variant carries cruise missiles and remains one of the few platforms capable of striking targets across the Northern Hemisphere. Flying-wing UAV designs eliminate the fuselage and tail, reducing drag and radar cross-section, which makes them attractive for long-range strike missions. Ukraine's approach—cloning an existing Chinese airframe and localizing production—mirrors a broader trend of asymmetric warfare where inexpensive mass-produced drones are used to attrit expensive legacy platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/drones/ukraine-destroys-tu-95-bomber-using-48000-chinese-drone-clone">Ukraine built a $48,000 long-range drone after... | Tom's Hardware</a></li>
<li><a href="https://defence-blog.com/ukraine-converts-chinese-drone-into-mich-2000-deep-striker/">Ukraine converts Chinese drone into MICH 2000 deep striker</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tupolev_Tu-95">Tupolev Tu - 95 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#drones`, `#military-tech`, `#reverse-engineering`, `#ukraine-conflict`, `#hardware`

---

<a id="item-12"></a>
## [Intel to Launch New Core Architecture on Desktop First with Nova Lake](https://www.tomshardware.com/pc-components/cpus/intel-says-it-will-launch-new-core-with-nova-lake-on-desktop-first-not-in-data-center-vp-robert-hallock-hopes-enthusiasts-do-the-math-compared-to-amd) ⭐️ 5.5/10

Intel VP Robert Hallock announced that the company's new core architecture, debuting with Nova Lake, will be released in consumer desktop processors before appearing in data center products — a reversal of Intel's typical launch order. Hallock encouraged enthusiasts to compare the new architecture's performance against AMD's offerings. This launch order reversal indicates Intel is under competitive pressure from AMD in the consumer desktop market and is prioritizing enthusiast mindshare to regain ground. It also signals that Intel sees the new core architecture as a critical differentiator it needs to showcase in the most visible segment first. Nova Lake is expected to launch in late 2026 and will require the new LGA 1954 socket, representing a full architectural rebuild rather than a refresh of the existing Arrow Lake platform. Intel's promotional framing encourages direct performance comparisons with AMD's competing desktop processors.

rss · Tom's Hardware · Aug 16, 12:10

**Background**: Intel has historically launched new core architectures in the data center (Xeon) segment first, then trickled them down to desktop platforms. Nova Lake is the codename for Intel's Core Ultra Series 4 processors, succeeding the current Arrow Lake generation. Intel's core architecture refers to the foundational design of the CPU's execution pipelines and logic, distinct from process node improvements. The competitive context is Intel's ongoing battle with AMD, whose Ryzen processors have gained significant desktop market share in recent years.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nova_Lake_(microprocessor)">Nova Lake (microprocessor) - Wikipedia</a></li>
<li><a href="https://bottleneckcalculator.us.com/knowledge-base/hardware-guides/intel-nova-lake-architecture-the-new-desktop-king/">Intel vs AMD 2026: Nova Lake Desktop Performance Guide</a></li>
<li><a href="https://acemagic.eu/blogs/einkaufsfuehrer/intel-nova-lake-vs-arrow-lake-vs-panther-lake">Intel Nova Lake vs Arrow Lake vs Panther Lake : Should You Buy...</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#Nova Lake`, `#CPU architecture`, `#AMD competition`, `#desktop processors`

---

<a id="item-13"></a>
## [Modern OLEDs are just as vulnerable to burn-in as 2017 panels in 10,000-hour test — twice the brightness and 27% efficiency gains offer crucial headroom](https://www.tomshardware.com/monitors/modern-oled-tvs-are-just-as-susceptible-to-burn-in-as-older-models-but-theyre-much-brighter-longevity-test-highlights-luminance-headroom-and-efficiency-as-mitigations) ⭐️ 5.5/10

Rtings.com's 10,000-hour accelerated longevity test finds modern OLED TVs are equally susceptible to burn-in as 2017 models, though they offer significantly higher brightness and 27% better power efficiency as mitigations.

rss · Tom's Hardware · Aug 16, 11:10

**Tags**: `#oled`, `#display-technology`, `#hardware`, `#consumer-electronics`, `#burn-in`

---

<a id="item-14"></a>
## [Ex-farm bureau chief invites AI data center developers to buy his land —argues blocked $6.3B project will just move to willing neighbors, defies 500-jurisdiction moratorium wave and 70% public opposition](https://www.tomshardware.com/tech-industry/data-centers/former-missouri-farm-bureau-president-offers-his-farm-for-a-data-center) ⭐️ 5.5/10

Former Missouri Farm Bureau president Blake Hurst is publicly offering his land for AI data center development, defying a wave of local moratoriums and public opposition to a $6.3B project.

rss · Tom's Hardware · Aug 16, 10:30

**Tags**: `#ai-infrastructure`, `#data-centers`, `#policy`, `#land-use`, `#nimby`

---

<a id="item-15"></a>
## [ADT R27A-BK3 EDSFF E1.S/E3.S to PCIe Gen5 Adapter Review](https://www.servethehome.com/adt-r27a-bk3-edsff-e1-s-and-e3-s-to-pcie-slot-review/) ⭐️ 5.5/10

ServeTheHome has published a review of the ADT R27A-BK3, an adapter card that lets users mount a PCIe Gen5 E1.S or E3.S EDSFF SSD into a standard PCIe card slot, enabling these newer data center form factor drives to be tested or deployed in conventional PCIe-equipped systems. As EDSFF form factors like E1.S and E3.S become more common in data center and AI server deployments, adapters that bridge them to legacy PCIe slots become useful for lab validation, benchmarking, and incremental integration without redesigning whole systems. The adapter supports PCIe Gen5 bandwidth and accommodates both the smaller E1.S and the larger, higher-capacity E3.S EDSFF drives, making it flexible for testing enterprise-class NVMe SSDs in workstations or server chassis that lack native EDSFF backplanes.

rss · ServeTheHome · Aug 16, 19:00

**Background**: EDSFF, or the Enterprise and Data Center Standard Form Factor, was developed by a group of 15 companies under SNIA to standardize NVMe SSD hardware for data centers. The E1.S variant offers better thermal dissipation and higher power delivery than M.2, while the E3.S family is larger and supports higher-density deployments—a 2U server can hold up to 46 E3.S drives, making it well suited for AI and enterprise database workloads. As these form factors proliferate in hyperscale and AI infrastructure, adapters like the R27A-BK3 help bridge the gap to systems built around conventional PCIe slots.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enterprise_and_Data_Center_Standard_Form_Factor">Enterprise and Data Center Standard Form Factor - Wikipedia</a></li>
<li><a href="https://nvmexpress.org/how-edsff-is-making-nvme-technology-even-cooler/">How EDSFF is Making NVMe® Technology Even Cooler - NVM Express</a></li>
<li><a href="https://www.serverstor.com/evolution-and-trends-of-edsff-hardware-form-factor-standards/">Enterprise-class SSD design specification EDSFF : Evolution from...</a></li>

</ul>
</details>

**Tags**: `#EDSFF`, `#E1.S`, `#E3.S`, `#PCIe Gen5`, `#hardware review`

---