---
layout: default
title: "Horizon Summary: 2026-11-19 (EN)"
date: 2026-11-19
lang: en
---

> From 93 items, 20 important content pieces were selected

---

1. [Nvidia launches Vera CPU for scientific discovery](#item-1) ⭐️ 10.0/10
2. [Intel 18A yields hit 70% as company signs Microsoft as EMIB customer](#item-2) ⭐️ 9.5/10
3. [Anthropic hits $2T in Nasdaq debut](#item-3) ⭐️ 9.0/10
4. [Claude solves two open problems in the physics of black holes](#item-4) ⭐️ 9.0/10
5. [Ruby2ßhell: Critical Pre-Auth RCE in Ruby Rails](#item-5) ⭐️ 9.0/10
6. [Anthropic Secures $107.3bn Funding at $1.5tn Valuation](#item-6) ⭐️ 9.0/10
7. [UK Admits Secret Order Forced Apple to Break End-to-End Encryption](#item-7) ⭐️ 8.0/10
8. [Debate over LLM discovery of Java 4 Shell vulnerability](#item-8) ⭐️ 8.0/10
9. [Souring Datacentre Sentiment](#item-9) ⭐️ 8.0/10
10. [Ukraine deploys homemade 'flying modems' in daring drone attack to destroy Crimean Bridge, ditching Elon Musk's Starlink](#item-10) ⭐️ 7.5/10
11. [Pancreatic cancer halted by virus injection in three patients](#item-11) ⭐️ 7.0/10
12. [Pete warden on local AI, open models, voice interfaces, the future of hardware](#item-12) ⭐️ 7.0/10
13. [European Commission Deploys Matrix Chat Platform to Over 40,000 Staff Members](#item-13) ⭐️ 7.0/10
14. [PHP 8.6 Introduces ZTS Performance and Type System Improvements](#item-14) ⭐️ 7.0/10
15. [Thermal and EMI challenges in high-density GaN power converters](#item-15) ⭐️ 7.0/10
16. [Three used V100 GPUs achieve 100 tokens per second on Qwen 3.6 35B](#item-16) ⭐️ 6.5/10
17. [Making 8-page foldable zines from a single A4 sheet in the browser](#item-17) ⭐️ 6.0/10
18. [ST set to double MCU revenues](#item-18) ⭐️ 6.0/10
19. [SI expects 60-80% semi growth in 2026](#item-19) ⭐️ 6.0/10
20. [AMD "Zen 6" for Desktop Reportedly Pushed to Computex 2027](#item-20) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [Nvidia launches Vera CPU for scientific discovery](https://www.electronicsweekly.com/news/business/nvidia-launches-vera-cpu-for-scientific-discovery-2026-11/) ⭐️ 10.0/10

Nvidia has announced the Vera CPU, its first fully custom datacenter processor designed for high-performance computing and scientific discovery.

rss · Electronics Weekly · Nov 19, 06:07

**Tags**: `#Nvidia`, `#CPU`, `#HPC`, `#Hardware`, `#Datacenter`

---

<a id="item-2"></a>
## [Intel 18A yields hit 70% as company signs Microsoft as EMIB customer](https://www.tomshardware.com/tech-industry/semiconductors/intel-18a-yields-hit-70-percent-as-company-signs-microsoft-as-emib-customer-the-first-company-to-publicly-commit-to-intels-new-packaging-technology) ⭐️ 9.5/10

Intel achieves 70% yields on its 18A process node and signs a major deal with Microsoft for Xeon supply and EMIB packaging technology.

rss · Tom's Hardware · Nov 19, 13:00

**Tags**: `#Intel 18A`, `#Semiconductors`, `#Microsoft`, `#EMIB`, `#Foundry`

---

<a id="item-3"></a>
## [Anthropic hits $2T in Nasdaq debut](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) ⭐️ 9.0/10

Anthropic's historic Nasdaq debut at a $2 trillion valuation sparks intense debate about the economic, environmental, and social impacts of the AI boom, with community discussions highlighting concerns over housing affordability, job displacement for engineers, and the misallocation of capital away from sectors like healthcare.

hackernews · wslh · Nov 19, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50562754)

**Tags**: `#AI`, `#Finance`, `#Market Trends`, `#Anthropic`, `#Economic Impact`

---

<a id="item-4"></a>
## [Claude solves two open problems in the physics of black holes](https://www.anthropic.com/research/claude-black-hole-physics) ⭐️ 9.0/10

Anthropic announced that their model Claude solved two open problems in black hole physics, a feat now considered significant enough to be featured in frontier model launch announcements, sparking debate on AI capabilities and scientific reproducibility.

hackernews · cybermango · Nov 19, 17:30 · [Discussion](https://news.ycombinator.com/item?id=50563148)

**Tags**: `#AI`, `#Physics`, `#Scientific Breakthrough`, `#Claude`, `#Anthropic`

---

<a id="item-5"></a>
## [Ruby2ßhell: Critical Pre-Auth RCE in Ruby Rails](https://verialabs.com/ruby2shell/) ⭐️ 9.0/10

Researchers discovered a critical pre-authentication remote code execution (RCE) vulnerability in stock Ruby on Rails, known as ruby2ßhell. This flaw is a one-byte heap buffer overflow in Ruby's string case-conversion code that allows attackers to compromise systems without credentials. This vulnerability is critical because it affects the widely used Ruby on Rails framework and enables remote code execution without authentication. It highlights the growing risk of memory-safety flaws in interpreted languages and the increasing speed at which AI-assisted tools can weaponize low-level bugs. The flaw, tracked as CVE-2026-132825, affects Ruby's case-conversion functions like upcase and downcase due to a heap overflow that can be exploited to read one byte beyond the buffer. Fixes are available in Ruby versions 3.3.14, 3.4.13, and 4.0.10, and the code dating back to Ruby 2.4.0 is vulnerable.

hackernews · jdns · Nov 19, 05:09 · [Discussion](https://news.ycombinator.com/item?id=50556287)

**Background**: Ruby on Rails is a popular web application framework built on the Ruby programming language, which is known for its dynamic typing and object-oriented syntax. While Ruby insulates developers from manual memory management, its underlying virtual machine (VM) and native extensions interact with C code, which is susceptible to memory-safety issues like buffer overflows. Pre-authentication RCE vulnerabilities are particularly dangerous because they allow unauthenticated remote attackers to gain full control of a server.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/ruby2shell-rce/">ruby2ßhell: Critical One-Byte Heap Overflow in Ruby Could ...</a></li>
<li><a href="https://orca.security/resources/blog/ruby2shell-ruby-heap-overflow-rce/">ruby2ßhell: CVE-2026-132825 Ruby Heap Overflow RCE</a></li>
<li><a href="https://www.getastra.com/blog/security-advisory/ruby2shell/">Ruby2shell (CVE-2026-132825): Critical Ruby Heap Overflow ...</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight a debate on whether AI is making it easier to convert single-byte overflows into RCEs, prompting calls for stricter memory safety across software stacks. Some users expressed frustration at the increasing frequency of 'Rails2Shell' variants, questioning if individual CVEs should still be treated as major news in the AI era. Technical interest focused on the difficulty of weaponizing a single-byte overflow for remote code execution.

**Tags**: `#Ruby`, `#Rails`, `#Security`, `#RCE`, `#MemorySafety`

---

<a id="item-6"></a>
## [Anthropic Secures $107.3bn Funding at $1.5tn Valuation](https://www.electronicsweekly.com/news/business/anthropic-raises-107bn-at-1-5trn-valuation-2026-11/) ⭐️ 9.0/10

Anthropic raised a combined $107.3 billion in a mixed offering that included a $26 billion private placement backed by Google, Nvidia, AMD, and Microsoft. The company achieved a $1.5 trillion valuation through this significant capital raise. This funding milestone signals strong industry consolidation and heavy investment in AI infrastructure by major tech firms. It positions Anthropic as a dominant player capable of competing with other leading AI labs in the global market. The capital raise was structured as a combination of an IPO and a private placement, with the latter totaling $26 billion from institutional investors. This dual approach allowed Anthropic to secure substantial funding while maintaining strategic ties with major technology companies.

rss · Electronics Weekly · Nov 19, 06:16

**Background**: An Initial Public Offering (IPO) is when a company offers shares to the public market for the first time, while a private placement involves selling securities directly to a targeted group of investors. Anthropic is an artificial intelligence company known for developing the Claude family of models, operating as a public benefit corporation dedicated to AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/ask/answers/021015/what-difference-between-ipo-and-private-placement.asp">IPO vs. Private Placement: Which Is Right for Your Company? Private Placement vs. IPO - Eqvista IPO vs. Private Placement - What's the Difference? | This vs ... Private Placement vs IPO: Which Path Is Right? Private Placement vs IPO: The Investor's Guide to Public vs ... How a Private Placement Memorandum Differs from an Initial ... IPO or Private Placement: What Does It Mean for You as an ...</a></li>
<li><a href="https://www.britannica.com/money/Anthropic-PBC">Anthropic | History, Controversies, & Claude AI | Britannica Money</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI Funding`, `#Venture Capital`, `#IPO`, `#Tech Industry`

---

<a id="item-7"></a>
## [UK Admits Secret Order Forced Apple to Break End-to-End Encryption](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) ⭐️ 8.0/10

The UK government legally acknowledged through the Investigatory Powers Tribunal that it issued a secret Technical Capability Notice to Apple under the Investigatory Powers Act. This admission confirms that governments can legally compel private companies to weaken their security infrastructure, undermining user trust in end-to-end encryption services. It raises significant privacy and national security implications for the entire tech industry. Apple responded to the order by withdrawing its most secure Advanced Data Protection service in the UK. The specific details of the encryption order remain classified, but it mandated a backdoor for law enforcement access to cloud storage.

hackernews · Terretta · Nov 19, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50562113)

**Background**: A Technical Capability Notice allows governments to force companies to modify their systems to access encrypted data. End-to-end encryption is a security model where data is only readable by the communicating parties. An encryption backdoor is a deliberate vulnerability that allows third parties, such as law enforcement, to bypass standard security measures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpolicy.press/uk-encryption-crackdown-imperils-privacy-security-free-speech/">UK Encryption Crackdown Imperils Privacy... | TechPolicy.Press</a></li>
<li><a href="https://www.ft.com/content/186a9bb6-9e62-47ce-b974-ce52a2d73e9f?syn-25a6b1a6=1">UK pressure on Apple for data access could leave the majority less safe</a></li>

</ul>
</details>

**Discussion**: The community expresses strong skepticism about Apple's shifted security assurances, highlighting the technical risk that a Key Encryption Key (KEK) compromise allows access to the actual data keys. Many users argue that the UK's overt surveillance approach warrants migrating to alternatives like GrapheneOS to maintain trust in their personal privacy.

**Tags**: `#security`, `#privacy`, `#legal`, `#apple`, `#surveillance`

---

<a id="item-8"></a>
## [Debate over LLM discovery of Java 4 Shell vulnerability](https://github.com/openjdk/jdk/pull/32781) ⭐️ 8.0/10

Security researchers at Calif disclosed Java 4 Shell, a critical RCE vulnerability in OpenJDK's Base64 decoder. A Hacker News discussion questions whether an LLM-assisted researcher independently discovered the bug or simply retrieved prior public knowledge. This incident highlights the growing role of AI in security research while raising concerns about attribution, originality, and the reliability of LLM-generated vulnerability reports. It prompts the industry to define new standards for validating AI-assisted findings. The vulnerability is tracked as CVE-2026-114938 with a CVSS 4.0 score of 9.2. The research focused on the JIT compiler, intrinsics, and widely accessible APIs, but it remains unclear if the LLM truly understood the exploitability.

hackernews · notmine1337 · Nov 19, 11:47 · [Discussion](https://news.ycombinator.com/item?id=50558906)

**Background**: Java 4 Shell is a memory corruption vulnerability in OpenJDK that allows remote code execution via malformed Base64 input. Responsible disclosure norms require researchers to coordinate with vendors like Oracle before public release to prevent immediate exploitation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sentinelone.com/blog/java4shell-vulnerability-in-openjdk-enables-rce-on-avx-512-cpus/">Defending Against Java 4 Shell : Vulnerability in OpenJDK Enables...</a></li>
<li><a href="https://www.helpnetsecurity.com/2022/05/12/publishing-cve/">How to avoid headaches when publishing a CVE - Help Net Security</a></li>

</ul>
</details>

**Discussion**: The community debates whether the LLM had prior knowledge of similar bug reports from open repositories. While some argue that understanding criticality still requires human supervision, others suspect the model simply copied details from previous PRs or issues.

**Tags**: `#Security`, `#AI/ML`, `#Java`, `#OpenSource`, `#VulnerabilityManagement`

---

<a id="item-9"></a>
## [Souring Datacentre Sentiment](https://www.electronicsweekly.com/blogs/mannerisms/dilemmas/souring-datacentre-sentiment-2026-11/) ⭐️ 8.0/10

The article explores the potential economic risks and sentiment shifts surrounding the projected $10.3 trillion global AI infrastructure investment cycle from 2025 to 2032.

rss · Electronics Weekly · Nov 19, 01:01

**Tags**: `#AI Infrastructure`, `#Data Centers`, `#Economics`, `#Hardware Supply Chain`, `#Technology Trends`

---

<a id="item-10"></a>
## [Ukraine deploys homemade 'flying modems' in daring drone attack to destroy Crimean Bridge, ditching Elon Musk's Starlink](https://www.tomshardware.com/networking/ukraine-deploys-homemade-flying-modems-in-daring-drone-attack-to-destroy-crimean-bridge-ditching-elon-musks-starlink-airborne-relay-stations-allow-pilots-to-dodge-russian-air-defences-to-deliver-1-200kg-payload) ⭐️ 7.5/10

Ukrainian forces employed a network of homemade 'flying modems' to create an airborne relay system, enabling live video feeds during an attack on the Crimean Bridge while evading Russian jamming of Starlink signals.

rss · Tom's Hardware · Nov 19, 11:11

**Tags**: `#Networking`, `#Military Technology`, `#Satellite Communications`, `#Signal Jamming`, `#Innovation`

---

<a id="item-11"></a>
## [Pancreatic cancer halted by virus injection in three patients](https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/) ⭐️ 7.0/10

A new study demonstrates that viral injections can halt pancreatic cancer in a small patient group, sparking community discussion that provides links to underlying research and critical analysis of the early-stage results.

hackernews · cybermango · Nov 19, 17:25 · [Discussion](https://news.ycombinator.com/item?id=50563066)

**Tags**: `#Medical Research`, `#Cancer`, `#Oncolytic Virus`, `#Biotechnology`, `#Clinical Trials`

---

<a id="item-12"></a>
## [Pete warden on local AI, open models, voice interfaces, the future of hardware](https://thedataexchange.media/pete-warden-moonshine/) ⭐️ 7.0/10

A discussion on Pete Warden's views regarding local AI and hardware, complemented by user reports on the feasibility and performance of running large language models on consumer GPUs.

hackernews · datascientist · Nov 19, 15:38 · [Discussion](https://news.ycombinator.com/item?id=50561508)

**Tags**: `#Local AI`, `#On-Device AI`, `#Hardware`, `#LLM`, `#Consumer Tech`

---

<a id="item-13"></a>
## [European Commission Deploys Matrix Chat Platform to Over 40,000 Staff Members](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/) ⭐️ 7.0/10

The European Commission successfully rolled out the decentralized communication protocol Matrix to more than 40,000 staff members. The deployment prompted significant internal technical adjustments, including the disabling of live presence features to mitigate server performance degradation. This large-scale deployment serves as a critical case study for the viability of open-source infrastructure in government and enterprise environments. It highlights the practical challenges of managing real-time communication protocols at scale, influencing how architects approach enterprise adoption of Matrix. The platform's end-to-end encryption capabilities remain a point of significant debate among security researchers, particularly regarding the implementation status of the MLS protocol. Performance bottlenecks in live presence tracking and the fragmented client landscape were identified as notable technical limitations.

hackernews · liotier · Nov 19, 10:58 · [Discussion](https://news.ycombinator.com/item?id=50558533)

**Background**: Matrix is an open-source protocol for secure, real-time communication that aims to be a decentralized alternative to proprietary messaging apps. It operates on a distributed server architecture, allowing entities to self-host their own homeservers and communicate across the global network.

**Discussion**: The community is divided, with users appreciating the privacy benefits of self-hosting but critical users expressing frustration over security flaws and frequent encryption errors. Some skeptics predict a high churn rate for institutional users due to the platform's current usability limitations and slow development pace.

**Tags**: `#Matrix`, `#OpenSource`, `#EnterpriseIT`, `#Security`, `#DistributedSystems`

---

<a id="item-14"></a>
## [PHP 8.6 Introduces ZTS Performance and Type System Improvements](https://www.php.net/releases/8.6/en.php) ⭐️ 7.0/10

PHP 8.6 releases several significant updates including ZTS performance improvements and enhancements to the type system. The release specifically highlights the introduction of function partials and a reduction in overhead for ZTS mode. The reduction in ZTS overhead could pave the way for native asynchronous support, enabling more efficient multithreading in PHP applications. This update is significant for web developers seeking to improve performance and security in their server-side codebases. A notable technical improvement allows for backward-compatible function arity checking, addressing a long-standing feature request to limit arguments for user-defined functions. Developers should note that recent critical vulnerabilities affect PHP 8.5 and later, meaning users on 8.3-8.4 remain safe from those specific CVEs.

hackernews · netol · Nov 19, 09:27 · [Discussion](https://news.ycombinator.com/item?id=50557870)

**Background**: PHP ZTS stands for Zend Thread Safety, a mode allowing PHP to run in multithreaded environments, though it typically incurs performance overhead compared to non-ZTS. The `parallel` extension currently offers limited concurrency, and ZTS improvements are seen as a stepping stone toward deeper native asynchronous capabilities.

**Discussion**: The community is most excited about the ZTS overhead reduction, viewing it as a potential enabler for native async support similar to the existing parallel extension. There is also disappointment regarding the lack of a simple way to limit user-defined function arguments in the type system, despite proposals for backward-compatible solutions. Users are advising those on newer PHP versions to upgrade quickly due to recent critical vulnerabilities, while noting that older versions like 8.3-8.4 are currently safe.

**Tags**: `#PHP`, `#Web Development`, `#Programming Languages`, `#Performance Optimization`

---

<a id="item-15"></a>
## [Thermal and EMI challenges in high-density GaN power converters](https://www.electronicsweekly.com/news/business/thermal-and-emi-challenges-in-high-density-gan-power-converters-2026-11/) ⭐️ 7.0/10

An article in Electronics Weekly emphasizes that maximizing the benefits of GaN design requires treating switching behavior, EMI, PCB design, and thermal management as interconnected problems. It argues that these factors cannot be addressed in isolation to achieve optimal performance in high-density applications. This guidance is critical for power electronics engineers designing next-generation high-density converters, as ignoring the interplay between thermal and EMI factors can lead to device failure or compliance issues. It highlights the complexity of moving from silicon to wide-bandgap technologies like GaN. The article notes that GaN devices exhibit high switching frequencies and low losses due to small parasitic capacitances. However, these characteristics make the system highly sensitive to electromagnetic interference and heat dissipation on the printed circuit board.

rss · Electronics Weekly · Nov 19, 12:00

**Background**: Gallium nitride is a wide-bandgap semiconductor that enables power electronics to operate at much higher frequencies and temperatures than traditional silicon devices. Because of these high frequencies, managing electromagnetic interference and preventing thermal overload in compact, high-density designs becomes significantly more complex.

<details><summary>References</summary>
<ul>
<li><a href="https://www.flywing-tech.com/blog/sic-vs-gan-comparison-2026/">SiC vs GaN : Which One Should You Choose in 2026?</a></li>
<li><a href="https://www.infineon.com/assets/row/public/documents/24/42/infineon-icl8830-high-frequency-gan-controller-for-led-lighting-applicationnotes-en.pdf">ICL8830 high - frequency GaN controller for LED</a></li>
<li><a href="https://www.geeksforgeeks.org/electronics-engineering/electromagnetic-interference/">Electromagnetic Interference - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#GaN`, `#Power Electronics`, `#Thermal Management`, `#EMI`, `#PCB Design`

---

<a id="item-16"></a>
## [Three used V100 GPUs achieve 100 tokens per second on Qwen 3.6 35B](https://www.tomshardware.com/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts) ⭐️ 6.5/10

A homelab builder demonstrated that a $1,042 rig using three decommissioned Nvidia Tesla V100 GPUs can achieve 100 tokens per second on the Qwen 3.6 35B model. This configuration outperforms the more expensive M5 Max Mac Studio at long contexts. This result proves that affordable, repurposed 'e-waste' enterprise GPUs remain a highly competitive solution for local large language model inference. It offers a practical, cost-effective alternative to high-end consumer hardware for developers and enthusiasts who need long-context performance. The Qwen 3.6 35B is a Mixture-of-Experts model released in April 2026, and this benchmark specifically highlights its performance at long contexts where traditional consumer hardware often slows down. The V100 is based on the older Volta architecture, showing its continued relevance for sustained inference tasks.

rss · Tom's Hardware · Nov 19, 11:00

**Background**: The Nvidia V100 is a data-center GPU based on the Volta architecture, originally designed for AI and high-performance computing in large-scale facilities. Qwen 3.6 35B is an advanced Large Language Model that utilizes Mixture-of-Experts (MoE) to optimize inference efficiency. Homelabbing refers to building personal hardware setups to self-host software, providing privacy and customizability.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/models/qwen3.6-35b-a3b">Qwen3.6-35B-A3B: Benchmarks, Pricing & Context Window</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/v100.md/">NVIDIA V100 | NVIDIA</a></li>
<li><a href="https://dasroot.net/posts/2026/05/qwen-3-6-35b-a3b-mtp-frozen-backbones-speedup/">Qwen 3.6 35B A3B & MTP: 7.8x Speedup with Frozen Backbones</a></li>

</ul>
</details>

**Tags**: `#homelab`, `#LLM-inference`, `#used-GPU`, `#Qwen`, `#nvidia`

---

<a id="item-17"></a>
## [Making 8-page foldable zines from a single A4 sheet in the browser](https://krthr.co/paper-folds-and-whats-new-in-fanzines-app/) ⭐️ 6.0/10

A Hacker News discussion about a tool for generating foldable 8-page zines from a single A4 sheet, featuring community insights on paper imposition, historical folding techniques, and related software tools.

hackernews · krthr · Nov 19, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50559719)

**Tags**: `#PrintMedia`, `#WebDevelopment`, `#CreativeTools`, `#PaperFolding`, `#Impositioning`

---

<a id="item-18"></a>
## [ST set to double MCU revenues](https://www.electronicsweekly.com/news/business/st-to-double-stm32-revenues-2026-11/) ⭐️ 6.0/10

STMicroelectronics expects to double its microcontroller revenues between 2005 and 2028, according to its president.

rss · Electronics Weekly · Nov 19, 06:15

**Tags**: `#STMicroelectronics`, `#Microcontrollers`, `#Semiconductor Industry`, `#Business News`

---

<a id="item-19"></a>
## [SI expects 60-80% semi growth in 2026](https://www.electronicsweekly.com/news/business/si-expecting-60-80-semi-growth-in-2026-2026-11/) ⭐️ 6.0/10

Semiconductor Intelligence forecasts 60-80% global market growth for 2026 in a newsletter from Bill Jewell's retirement.

rss · Electronics Weekly · Nov 19, 06:14

**Tags**: `#Semiconductor Market`, `#Industry Forecast`, `#Business`, `#Tech Trends`

---

<a id="item-20"></a>
## [AMD "Zen 6" for Desktop Reportedly Pushed to Computex 2027](https://www.techpowerup.com/355030/amd-zen-6-for-desktop-reportedly-pushed-to-computex-2027) ⭐️ 5.5/10

AMD's desktop 'Zen 6' (Olympic Ridge) processors are reportedly delayed to Computex 2027 to utilize TSMC's N2X node for higher clock speeds, while EPYC lines stick to the standard N2 node.

rss · TechPowerUp News · Nov 19, 17:22

**Tags**: `#AMD`, `#CPU`, `#TSMC`, `#Hardware`, `#Roadmap`

---