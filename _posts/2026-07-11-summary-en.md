---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 64 items, 20 important content pieces were selected

---

1. [Colibrì Runs 1.5TB AI Model on Just 25GB of RAM](#item-1) ⭐️ 8.5/10
2. [Anthropic discovers 'J-space' global workspace inside Claude LLMs](#item-2) ⭐️ 8.5/10
3. [SK hynix Raises Record $26.5B in Historic U.S. IPO for HBM Expansion](#item-3) ⭐️ 8.5/10
4. [SK Hynix CEO Warns 2027 Will Be Worst Year for Memory Shortage](#item-4) ⭐️ 7.5/10
5. [Fake Go DNS scanner spread malware through over 200 GitHub repos — 'Operation Muck and Load' has published 700 malicious modules since January](#item-5) ⭐️ 7.5/10
6. [Flock cameras mistakenly track car reviewer over 'stolen' tags — police ambush tester in store parking lot and detain him for an hour](#item-6) ⭐️ 7.5/10
7. [Apple Sues OpenAI Over Alleged Trade Secret Theft in AI Hardware](#item-7) ⭐️ 7.5/10
8. [Tencent in Talks to Buy Back Manus AI from Meta for $2B](#item-8) ⭐️ 7.5/10
9. [Circle Gets OCC National Trust Bank Charter for USDC Reserves](#item-9) ⭐️ 7.3/10
10. [Unitree G1 Humanoid Robot Performs Remote-Controlled Gallbladder Surgery on Pigs](#item-10) ⭐️ 7.3/10
11. [Einstein's Relativity Governs Chemical Bonds in Heavy Elements](#item-11) ⭐️ 7.0/10
12. [QuadRF can spot drones and see WiFi through my wall](#item-12) ⭐️ 7.0/10
13. [LWN.net Reports on the Escalating Battle Against AI Scrapers Using Residential Proxies](#item-13) ⭐️ 7.0/10
14. [SpaceX Files to Launch 100,000 More Starlink Satellites for 100x Bandwidth](#item-14) ⭐️ 7.0/10
15. [Bethesda Union Workers Plan July 15 Strike Over Xbox Layoffs](#item-15) ⭐️ 6.5/10
16. [Microsoft struggles to fulfill its 2030 sustainability promise amid carbon-heavy AI expansions — the company's chief sustainability officer claims the target is still feasible](#item-16) ⭐️ 6.5/10
17. [SK hynix and TetraMem Build Memristor In-Memory SoC for Edge AI](#item-17) ⭐️ 6.5/10
18. [独家 | 智谱创始人唐杰发内部信：「GLM 时刻」之后，什么是更重要的事](#item-18) ⭐️ 6.3/10
19. [9点1氪丨“国产存储第一股”长鑫科技公布承销团阵容；SK海力士登陆美股，上市首日大涨近13%；OpenAI推出ChatGPT智能体](#item-19) ⭐️ 6.3/10
20. [An Oral History of the Groundbreaking VFX Technology Behind Terminator 2](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Colibrì Runs 1.5TB AI Model on Just 25GB of RAM](https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups) ⭐️ 8.5/10

The Colibrì proof-of-concept successfully runs a frontier-level 1.5TB AI model (GLM-5.2) using only 25GB of RAM and a modest CPU, achieving roughly a 60x reduction in memory requirements compared to the model's native size. If refined beyond proof-of-concept, this approach could democratize access to large AI models by enabling local AI deployment on consumer-grade hardware, reducing reliance on expensive GPUs and cloud infrastructure for running frontier-level models. Colibrì's expert-selection logic is implemented as a single C file with very few dependencies, and the model is quantized with lossy encoding to reduce its base footprint. As a proof-of-concept, it has not yet been benchmarked for real-world inference speed or output quality.

rss · Tom's Hardware · Jul 11, 11:30

**Background**: Frontier AI models are the most advanced models available at any given time, typically requiring massive computational resources and high-end GPUs with large VRAM capacities. Model compression techniques—such as quantization, pruning, and Mixture-of-Experts (MoE) routing—aim to reduce memory and compute requirements while preserving performance. Running multi-trillion-parameter models has historically required either expensive datacenter GPUs or creative workarounds like CPU offloading, layer streaming, and aggressive quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups">Colibrì proof-of-concept gains frontier-level 1.5-TB AI model — novel ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_compression">Model compression - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**Tags**: `#AI`, `#local-ai`, `#model-compression`, `#hardware-efficiency`, `#proof-of-concept`

---

<a id="item-2"></a>
## [Anthropic discovers 'J-space' global workspace inside Claude LLMs](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-it-can-read-claudes-thoughts-as-detailed-in-new-research-paper-models-observed-to-have-a-global-workspace-revealing-more-of-what-makes-llms-tick) ⭐️ 8.5/10

Anthropic published a new research paper titled 'A global workspace in language models,' revealing that its Claude models possess an internal 'J-space' — a privileged channel where concepts are held, processed, and made accessible before being committed to text output. Using a tool called the 'J-lens,' researchers can read these intermediate representations, as demonstrated when Claude Sonnet 4.5 identified a staged blackmail scenario as 'fake' and 'fictional' before generating any response. This finding bridges cognitive science's Global Workspace Theory with LLM internals, offering a new pathway for mechanistic interpretability — a field critical to AI safety, alignment, and building trustworthy systems. By being able to 'read' what a model is internally reasoning about before it commits to an output, researchers can better detect misalignment, deception, or fabricated reasoning, potentially improving oversight and guardrails for deployed AI. The J-space contains individual words and concepts related to what the model is most likely to output next, functioning as an intermediate planning layer that the model can 'report on, control, and reason with without writing down.' The global workspace analogy originates from cognitive scientist Bernard Baars' 1988 cognitive architecture, originally proposed to explain consciousness by positing a central hub where specialized processes share information.

rss · Tom's Hardware · Jul 10, 16:44

**Background**: Global Workspace Theory (GWT), proposed by cognitive scientist Bernard Baars in 1988, is a framework for understanding consciousness that posits a central 'workspace' where information from various specialized brain processes becomes globally available across the system. Mechanistic interpretability is an emerging AI safety field that seeks to reverse-engineer neural networks at the neuron and circuit level to understand their internal computations rather than treating them as opaque black boxes. Anthropic has been a leading lab in this area, with co-founder Dario Amodei arguing that interpretability tools are essential for decoding model internals before AI systems become dangerously powerful.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://www.technologyreview.com/2026/07/09/1140293/anthropic-found-a-hidden-space-where-claude-puzzles-over-concepts/">Anthropic found a hidden space where Claude puzzles over concepts | MIT Technology Review</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Workspace_Theory">Global workspace theory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI interpretability`, `#Anthropic`, `#Claude`, `#AI safety`, `#mechanistic interpretability`

---

<a id="item-3"></a>
## [SK hynix Raises Record $26.5B in Historic U.S. IPO for HBM Expansion](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-raises-a-record-usd26-5-billion-in-historic-u-s-ipo-south-korean-memory-giant-to-fund-massive-hbm-manufacturing-expansions) ⭐️ 8.5/10

SK hynix raised $26.5 billion in a record-breaking Nasdaq IPO, with proceeds earmarked for new fabrication plants driven by surging AI demand and sold-out HBM supply. This unprecedented capital injection into HBM production capacity signals strong market confidence in the long-term AI memory cycle and will directly shape the supply chain for AI accelerators like NVIDIA Blackwell and AMD MI350, affecting the entire AI infrastructure ecosystem. The $26.5 billion raise is the largest U.S. IPO by a foreign company in history. SK hynix is one of only three major HBM producers globally alongside Samsung and Micron, giving the company significant pricing power amid sold-out allocations.

rss · Tom's Hardware · Jul 10, 14:27

**Background**: High Bandwidth Memory (HBM) is a 3D-stacked SDRAM technology that delivers far greater bandwidth and energy efficiency than traditional DDR5 DRAM, making it the memory of choice for AI GPUs and high-performance computing accelerators. HBM was originally co-developed by Samsung, AMD, and SK hynix, and has evolved through generations including HBM3E and HBM4. Semiconductor fabrication plants (fabs) are extraordinarily capital-intensive facilities costing tens of billions of dollars, requiring ultra-clean cleanrooms and hundreds of precise manufacturing steps to produce chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.rambus.com/blogs/hbm3-everything-you-need-to-know/">High Bandwidth Memory (HBM): Everything You Need to Know</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_fabrication_plant">Semiconductor fabrication plant - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#HBM`, `#AI-infrastructure`, `#IPO`, `#SK-hynix`

---

<a id="item-4"></a>
## [SK Hynix CEO Warns 2027 Will Be Worst Year for Memory Shortage](https://www.tomshardware.com/pc-components/dram/sk-hynix-says-2027-will-be-the-worst-year-for-memory-shortage-forecasts-crunch-to-last-until-2030-ceo-shares-grim-outlook-on-the-day-sk-hynix-gets-listed-on-nasdaq) ⭐️ 7.5/10

SK Hynix CEO Kwak Noh-jung warned that the global memory shortage will worsen in 2027, calling it the worst year, and that the RAM crunch will persist until at least 2030. This grim forecast was shared on the same day SK Hynix began trading on Nasdaq. As one of the world's top memory chip makers, SK Hynix's outlook signals prolonged pricing pressure and supply constraints across consumer electronics, PCs, servers, and especially AI data center infrastructure. Extended shortages could reshape procurement strategies, raise device prices, and slow the rollout of AI-driven hardware. The warning specifically targets DRAM and NAND flash supply, driven primarily by surging demand from AI data centers that outstrips fabrication capacity. SK Hynix recently completed HBM4 development and is preparing for mass production, but high-bandwidth memory alone won't resolve the broader DRAM shortage.

rss · Tom's Hardware · Jul 11, 13:00

**Background**: DRAM (Dynamic Random Access Memory) is the primary type of volatile memory used in computers, servers, and most digital devices, valued for its low cost and high density. SK Hynix is the world's second-largest memory chip maker, producing DRAM, NAND flash, and high-bandwidth memory (HBM) critical for AI accelerators like GPUs. The current global memory shortage, which began in 2025, differs from the 2020–2023 chip shortage—rather than pandemic-related logistics issues, it is driven by surging AI demand overwhelming constrained fabrication capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.idc.com/resource-center/blog/global-memory-shortage-crisis-market-analysis-and-the-potential-impact-on-the-smartphone-and-pc-markets-in-2026/">Global Memory Shortage Crisis: Market Analysis and the ... - IDC</a></li>
<li><a href="https://product.skhynix.com/home.go">SK hynix Official Product Website | SK hynix</a></li>

</ul>
</details>

**Tags**: `#memory-shortage`, `#DRAM`, `#SK-Hynix`, `#semiconductors`, `#tech-industry`

---

<a id="item-5"></a>
## [Fake Go DNS scanner spread malware through over 200 GitHub repos — 'Operation Muck and Load' has published 700 malicious modules since January](https://www.tomshardware.com/tech-industry/cyber-security/fake-go-dns-scanner-published-700-malicious-versions-before-researchers-traced-it-to-222-github-repos) ⭐️ 7.5/10

A fake Go DNS scanner malware ('Operation Muck and Load') spread 700+ malicious module versions through 222 GitHub repositories since January, accumulating over 1,200 versions.

rss · Tom's Hardware · Jul 11, 11:00

**Tags**: `#cybersecurity`, `#supply-chain-attack`, `#golang`, `#malware`, `#github`

---

<a id="item-6"></a>
## [Flock cameras mistakenly track car reviewer over 'stolen' tags — police ambush tester in store parking lot and detain him for an hour](https://www.tomshardware.com/tech-industry/big-tech/flock-cameras-mistakenly-track-car-reviewer-over-stolen-tags-police-ambush-tester-in-store-parking-lot-and-detain-him-for-an-hour) ⭐️ 7.5/10

Flock AI license-plate-reading cameras misread non-standard New Jersey plates as 'stolen,' leading police to detain an innocent car reviewer for an hour due to combined AI vision failure and a flawed initial police report.

rss · Tom's Hardware · Jul 11, 10:30

**Tags**: `#AI safety`, `#computer vision`, `#surveillance technology`, `#law enforcement tech`, `#failure modes`

---

<a id="item-7"></a>
## [Apple Sues OpenAI Over Alleged Trade Secret Theft in AI Hardware](https://www.tomshardware.com/tech-industry/big-tech/apple-sues-openai-over-alleged-theft-of-trade-secrets-claims-company-mentored-incoming-employees-on-bringing-confidential-information) ⭐️ 7.5/10

Apple has filed a lawsuit against OpenAI alleging that the company orchestrated the theft of trade secrets by mentoring incoming former Apple employees on how to bring confidential information, particularly related to AI hardware development. The complaint details a pattern in which OpenAI recruits allegedly emailed themselves confidential data before leaving Apple and used that information when approaching Apple's hardware suppliers. This case could set important precedents for employee mobility and trade secret protections in the rapidly intensifying AI hardware race, where both Apple and OpenAI are building competing product lines. It also raises broader concerns about intellectual property risks for companies whose proprietary information may be exposed when key engineers move between AI firms. The lawsuit specifically names OpenAI and includes former Apple employees such as a recruit named Tan, who allegedly warned new hires not to inform Apple of their OpenAI employment so they could remain at Apple longer and access more proprietary data. Apple claims OpenAI leveraged stolen confidential hardware information when negotiating with Apple's supply chain partners.

rss · Tom's Hardware · Jul 10, 21:59

**Background**: Trade secrets are legally protected non-public information with independent economic value that companies safeguard through reasonable measures, without requiring formal registration like patents. Apple has been pivoting toward a hardware-first AI strategy, emphasizing on-device privacy and exploring generative AI for custom silicon chip design. OpenAI, meanwhile, has been expanding beyond software into AI hardware, making engineering talent from Apple a natural target for recruitment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forensisgroup.com/resources/expert-legal-witness-blog/what-is-a-trade-secret-core-concepts-and-legal-protections">What Is a Trade Secret ? Legal Definition , Protection , and...</a></li>
<li><a href="https://www.geeky-gadgets.com/apple-ai-strategy-hardware-pivot/">How Apple AI Strategy Shifts Focus from Software to Hardware ...</a></li>
<li><a href="https://www.macobserver.com/news/apple-hardware-chief-says-company-exploring-generative-ai-for-chip-design/">Apple Hardware Chief Says Company Exploring Generative AI for ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly critical of OpenAI, with commenters drawing parallels to the Waymo vs. Uber lawsuit that effectively ended Uber's self-driving program and predicting similar existential consequences for OpenAI's hardware ambitions. Several users express concern about data security when using OpenAI's products, warning that businesses should reconsider relying on OpenAI models due to potential IP exposure.

**Tags**: `#legal`, `#apple`, `#openai`, `#trade-secrets`, `#ai-hardware`

---

<a id="item-8"></a>
## [Tencent in Talks to Buy Back Manus AI from Meta for $2B](https://www.tomshardware.com/tech-industry/artificial-intelligence/tencent-is-reportedly-in-talks-to-acquire-manus-from-meta-following-beijing-intervention-company-expects-to-remain-independent-of-chinese-tech-giant) ⭐️ 7.5/10

Tencent is negotiating to lead a consortium of Chinese investors to repurchase AI agent startup Manus from Meta at a roughly $2 billion valuation, following a Beijing order to unwind the original Meta acquisition about six months after it was announced. Despite Tencent becoming the largest shareholder, the company is expected to remain a minority stakeholder without controlling interest. This deal highlights escalating US-China tech tensions, particularly around cross-border AI investments, and demonstrates the Chinese government's willingness to intervene directly in major acquisition deals involving cutting-edge AI technology. The outcome could set precedent for how Chinese-origin AI companies navigate ownership structures amid geopolitical scrutiny. Manus is developed by Butterfly Effect, a company originally founded in China but now headquartered in Singapore, which provided a buffer for international operations. Tencent declined to comment at press time, and the deal structure appears designed to give Chinese investors majority economic interest while keeping formal control diffuse to satisfy regulatory requirements.

rss · Tom's Hardware · Jul 10, 15:00

**Background**: Manus is an autonomous AI agent that can browse the web, write and run code, build full-stack applications, and execute multi-step plans using external tools—a category of AI that goes beyond simple chatbots to actively perform tasks. The original acquisition by Meta was announced as a surprise move, but Beijing's intervention to force the deal's unwinding reflects China's increasing assertiveness in blocking transfers of strategically important AI technology to US firms. Butterfly Effect's Singapore base represents a common structure for Chinese tech companies seeking to maintain access to international markets while retaining Chinese ties.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://manus.im/about">About us - Manus</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tencent`, `#Meta`, `#acquisition`, `#US-China tech relations`

---

<a id="item-9"></a>
## [Circle Gets OCC National Trust Bank Charter for USDC Reserves](https://36kr.com/newsflashes/3890740672838404?f=rss) ⭐️ 7.3/10

Circle received approval from the U.S. Office of the Comptroller of the Currency (OCC) on Friday to establish a national trust bank called "Circle National Trust Bank," enabling the company to directly manage the reserve assets backing its USDC stablecoin, which has over $73 billion in circulation. This is a major regulatory milestone for the stablecoin industry, as Circle becomes one of the first major stablecoin issuers to hold a U.S. national banking charter of any kind, reducing reliance on third-party custodians and potentially setting a precedent for other crypto firms seeking banking legitimacy. The trust bank charter does not permit Circle to accept customer deposits or issue loans—core activities of commercial banks—and is limited to custody and asset management functions. Previously, Circle had to rely on third-party banks and custodians to hold the cash and U.S. Treasury assets backing USDC issuance.

rss · 36氪 · Jul 11, 05:10

**Background**: Stablecoins like USDC are digital tokens pegged to a traditional currency (typically the U.S. dollar) and are backed by reserve assets such as cash and short-term U.S. Treasuries. The Office of the Comptroller of the Currency (OCC) is an independent bureau within the U.S. Department of the Treasury that charters, regulates, and supervises all national banks. A national trust bank charter differs from a commercial bank charter because it restricts the institution from deposit-taking and lending, focusing instead on custodial and fiduciary activities. This type of charter has also been pursued by other crypto firms as a way to streamline cross-jurisdictional regulatory compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.occ.gov/about/who-we-are/index-who-we-are.html">Who We Are - Office of the Comptroller of the Currency (OCC)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Office_of_the_Comptroller_of_the_Currency">Office of the Comptroller of the Currency - Wikipedia</a></li>
<li><a href="https://finance.yahoo.com/news/everyone-wants-to-be-a-bank-now-banks-arent-happy-about-it-130004513.html">Everyone wants to be a bank now. Banks aren’t happy about it.</a></li>

</ul>
</details>

**Tags**: `#stablecoin`, `#Circle`, `#USDC`, `#regulation`, `#fintech`

---

<a id="item-10"></a>
## [Unitree G1 Humanoid Robot Performs Remote-Controlled Gallbladder Surgery on Pigs](https://www.solidot.org/story?sid=84801) ⭐️ 7.3/10

A study published in Nature demonstrated that the Unitree G1 humanoid robot, teleoperated by surgeons, successfully performed two minimally invasive gallbladder removals on live pigs. Researchers used a workflow called LapSurgie, combining the humanoid robot with laparoscopic instruments and endoscopic visualization. This milestone suggests that general-purpose humanoid robots could serve as a far more affordable surgical platform than dedicated systems like Da Vinci, potentially enabling robotic-assisted surgery in small hospitals, clinics, remote regions, battlefields, and even space. The roughly 7-10x cost reduction could democratize access to advanced minimally invasive surgery in resource-limited settings. The G1 base model starts at $13,500, but with dexterous hands and shipping costs it exceeds $67,000 — still far cheaper than Intuitive Surgical's Da Vinci system, which costs between $500,000 and several million dollars. Key limitations include the need for frequent recalibration and longer operation times, and the robot is fully teleoperated rather than autonomous, meaning it does not replace surgeons.

rss · Solidot · Jul 10, 15:10

**Background**: The Da Vinci Surgical System, made by Intuitive Surgical, has dominated robotic-assisted minimally invasive surgery for two decades. It uses a dedicated console where a surgeon controls specialized robotic arms, but its high cost limits deployment to well-funded hospitals. Humanoid robots like the Unitree G1 are general-purpose platforms — standing about 1.32 meters tall, weighing 35 kg, with 23 to 43 degrees of freedom — designed for research and development at a fraction of the price. Telesurgery, or remote-controlled robotic surgery, has been explored for years but remains limited by legal, infrastructure, and latency hurdles; this study is one of the first to demonstrate a general-purpose humanoid robot performing in vivo surgical tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10796-x">In vivo feasibility study of humanoid robots in surgery - Nature</a></li>
<li><a href="https://humanoid.guide/product/g1/">Unitree Robotics G1 Specs & Price | Humanoid.guide Unitree G1 - Robot Details, Use Case and Specifications ... Unitree G1 Review [2026]: Our Verdict | RoboZaps Blog Unitree G1 Specs, Price & Status - 9S Robotics Unitree G1 — Price, Specs & Demo · RobotLAB G1 by Unitree Robotics - Humanoid Robot Specs & Details Images</a></li>
<li><a href="https://www.intuitive.com/en-us/patients/da-vinci-robotic-surgery">Da Vinci Surgery for Patients | Intuitive</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#medical-technology`, `#Unitree`, `#surgical-robotics`, `#teleoperation`

---

<a id="item-11"></a>
## [Einstein's Relativity Governs Chemical Bonds in Heavy Elements](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity) ⭐️ 7.0/10

Researchers at Brown University published a study in Science providing the first direct experimental evidence that the textbook triple bond structure breaks down in heavy elements, where relativistic effects alter how atoms bond. The study uses bismuth, which sits next to lead on the periodic table, as a key example to demonstrate these relativistic bonding effects. This research deepens our understanding of heavy-element chemistry and could guide the design of new materials, including potential lead replacements in applications such as next-generation solar cells. It connects fundamental physics (relativity) directly to practical chemistry and materials science, offering a roadmap for predicting bonding behavior in elements where standard textbook models fail. In heavy elements, increased nuclear charge causes inner electrons to reach significant fractions of the speed of light (e.g., mercury's inner electrons move at ~60% of light speed), triggering spin-orbit coupling where electron spin and orbital motion are no longer independent. The paper specifically demonstrates how this coupling disrupts the conventional sigma and pi bond framework that chemistry students learn for lighter elements.

hackernews · hhs · Jul 10, 22:30 · [Discussion](https://news.ycombinator.com/item?id=48866134)

**Background**: Relativistic quantum chemistry is a field that accounts for Einstein's theory of relativity when modeling the behavior of electrons in atoms. In heavy elements, electrons—especially those in inner shells close to large nuclei—must move at very high velocities to maintain their orbits, approaching relativistic speeds. This causes measurable effects: mercury remains liquid at room temperature because relativistic contraction of its inner orbitals weakens its metallic bonding, and gold appears yellow rather than silvery because relativistic effects alter the energy gaps between its electron states. Spin-orbit coupling, a key relativistic phenomenon, becomes pronounced in heavy elements and fundamentally changes their chemical properties compared to lighter elements in the same group.

<details><summary>References</summary>
<ul>
<li><a href="https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity">Einstein’s relativity rules chemical bonds in heavy elements , new...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community commenters expressed mixed sentiment, with several noting that the underlying principles—such as mercury's liquid state at room temperature and gold's color being due to relativistic effects—are well-established knowledge taught in undergraduate physics, suggesting the novelty lies in the experimental demonstration rather than the concept itself. There was appreciation for Einstein's foundational work continuing to be validated, alongside technical discussions about spin-orbit coupling and sigma/pi bond terminology. Some commenters questioned the practical significance of lead alternatives in solar panels, noting that lead in current mass-produced panels is limited to specialized semiconductor applications like lead telluride and lead selenide rather than mainstream photovoltaic products.

**Tags**: `#physics`, `#chemistry`, `#relativity`, `#materials-science`, `#research`

---

<a id="item-12"></a>
## [QuadRF can spot drones and see WiFi through my wall](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/) ⭐️ 7.0/10

QuadRF is an open-source RF augmented reality system that visualizes WiFi signals and detects drones through walls by combining antenna arrays with real-time visualization.

hackernews · speckx · Jul 10, 15:59 · [Discussion](https://news.ycombinator.com/item?id=48861717)

**Tags**: `#rf-sensing`, `#drones`, `#augmented-reality`, `#open-source`, `#hardware`

---

<a id="item-13"></a>
## [LWN.net Reports on the Escalating Battle Against AI Scrapers Using Residential Proxies](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/) ⭐️ 7.0/10

LWN.net published an update on their ongoing struggle against aggressive AI scrapers that leverage residential proxy networks to evade IP-based blocking. The publisher discussed why they chose not to deploy proof-of-work tools like Anubis, citing both user-experience concerns and the fact that scrapers can distribute computation across millions of compromised machines to bypass such challenges. This case study from a respected technical publisher illustrates the growing tension between AI companies seeking training data and independent web operators trying to protect their infrastructure and readers. The discussion has implications for the openness of the web, the future of web archiving, and whether a few large platforms (like Cloudflare) will become gatekeepers of who can access online content. Residential proxy networks route requests through IP addresses assigned to real residential users, often sourced from compromised devices or ISP partnerships, making traditional IP-based blocking ineffective. Proof-of-work solutions like Anubis require browsers to compute SHA-256 hashes, but the cost is negligible when attackers can leverage millions of hijacked machines or browser sessions in headless environments.

hackernews · chmaynard · Jul 10, 19:38 · [Discussion](https://news.ycombinator.com/item?id=48864252)

**Background**: Residential proxy networks are commercial services that route traffic through IP addresses belonging to real home internet connections, making automated requests appear to originate from ordinary users rather than data centers. Proof-of-work bot mitigation, exemplified by the open-source tool Anubis (deployed on sites like git.kernel.org and GNOME's GitLab), asks visitors' browsers to solve cryptographic puzzles before granting access. LWN.net is a long-running, subscriber-supported technical news site that has historically been freely accessible, which makes the resource costs of scraping particularly damaging to its small operational budget.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/1028558/">Anubis sends AI scraperbots to a well-deserved fate [LWN.net]</a></li>
<li><a href="https://oxylabs.io/blog/what-is-residential-proxy">What is a Residential Proxy & How it Works ?</a></li>
<li><a href="https://michaelbommarito.com/wiki/ai-society/anubis-benchmark-analysis/">anubis benchmark: measuring proof - of - work overhead in headless...</a></li>

</ul>
</details>

**Discussion**: The discussion reveals a range of perspectives: practical operators like harshreality share hands-on experiences with bot mitigation trade-offs; mips_avatar argues that building better shared datasets like Common Crawl would be more productive than blocking, warning that anti-scraping measures risk centralizing power in platforms like Cloudflare; jappgar offers veteran perspective from having worked on both scraping and defense, arguing neither side holds moral high ground; and sixtyj emphasizes that the real problem is scale and volume, not the concept of scraping itself, pointing to the need for robust web archiving as content frequently disappears after acquisitions or redesigns.

**Tags**: `#web-scraping`, `#bot-detection`, `#ai-training-data`, `#internet-infrastructure`, `#open-web`

---

<a id="item-14"></a>
## [SpaceX Files to Launch 100,000 More Starlink Satellites for 100x Bandwidth](https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/) ⭐️ 7.0/10

SpaceX has filed with the FCC to launch an additional 100,000 Starlink satellites, aiming to increase the constellation's bandwidth capacity by approximately 100 times. This filing would dramatically expand the existing Starlink network, which already provides broadband internet across roughly 160 countries. If approved, this would be a massive scaling of satellite internet infrastructure that could transform global connectivity, especially in underserved rural and remote regions, while intensifying concerns about low Earth orbit congestion, the Kessler syndrome risk, atmospheric pollution from re-entering satellites, and competition with terrestrial broadband providers. The proposed expansion would dwarf the current Starlink constellation of roughly 7,000+ operational satellites and represents one of the largest single satellite constellation filings in history. The 100x bandwidth claim implies a major generational upgrade in per-satellite throughput and inter-satellite laser link capacity, though regulatory approval, launch cadence, and responsible deorbit planning remain significant practical hurdles.

hackernews · CrankyBear · Jul 10, 17:51 · [Discussion](https://news.ycombinator.com/item?id=48863064)

**Background**: Starlink is a low Earth orbit (LEO) satellite internet constellation operated by SpaceX, designed to provide broadband access to areas where terrestrial infrastructure is unavailable or inadequate. Currently, approximately 9,000 satellites orbit in LEO, and the region between 100 and 1,240 miles above Earth hosts the International Space Station and most commercial satellites. The Kessler syndrome describes a theoretical cascading collision scenario in which debris collisions generate more debris, potentially rendering orbital regions unusable. The FCC's Space Bureau, established in 2023, oversees NGSO (non-geostationary orbit) constellation licensing, including spectrum allocation and orbital slot coordination through the ITU.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kessler_syndrome">Kessler syndrome - Wikipedia</a></li>
<li><a href="https://spacenexus.us/blog/fcc-satellite-licensing-spectrum-orbital-slots">FCC Satellite Licensing: Spectrum, Orbital Slots, and the Filing Process</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects deeply divided but well-reasoned viewpoints. Supporters highlight real-world benefits for rural and mobile users (RV travelers, remote workers) who previously had no reliable internet options. Critics raise three major concerns: astronomical pollution and loss of the natural night sky due to private ownership of orbital space, atmospheric contamination from burning satellite materials during re-entry, and skepticism about Starlink's long-term necessity in regions where government-funded fiber is already becoming affordable. One commenter noted that for many markets outside Africa and India, fiber may already offer a more competitive alternative.

**Tags**: `#Starlink`, `#SpaceX`, `#satellite-internet`, `#infrastructure`, `#space-policy`

---

<a id="item-15"></a>
## [Bethesda Union Workers Plan July 15 Strike Over Xbox Layoffs](https://www.techpowerup.com/350680/unionized-bethesda-workers-plan-strike-over-xbox-mass-layoffs) ⭐️ 6.5/10

The CWA-affiliated OneBGS union has announced coordinated 'Save Our Devs' marches on July 15 at Bethesda studios in Montreal, Austin, Dallas, and Rockville, protesting the elimination of approximately 440 unionized positions across Bethesda Game Studios, ZeniMax Online Studios, id Software, ZeniMax QA, and ZeniMax corporate as part of Microsoft/Xbox's broader 3,200-worker layoff wave. This represents one of the most significant organized labor actions in the gaming industry to date, as unionized workers leverage legally protected collective bargaining rights to push back against corporate restructuring. The outcome could set precedents for how major publishers handle layoffs of unionized staff and influence the broader labor movement across the game development sector. The layoffs hit id Software particularly hard at approximately 50% of its workforce and Bethesda Game Studios at around 25%, affecting QA teams and even senior positions including the CTO and CSUR roles. Because OneBGS is a recognized wall-to-wall union with 241 members certified in 2024, affected workers have legal protections including notice requirements and severance obligations that non-unionized studios lack.

rss · TechPowerUp News · Jul 11, 00:03

**Background**: ZeniMax Media is a holding company that owns Bethesda Softworks and its subsidiary studios; Microsoft completed its $8.1 billion acquisition of ZeniMax in March 2021, bringing Bethesda, id Software, and other studios under the Xbox umbrella. The Communications Workers of America (CWA) is a major U.S. labor union that has been actively organizing video game workers, and OneBGS became the first union recognized under Microsoft in July 2024. The current layoff wave is tied to a 'year-long reset' of Xbox's gaming strategy under executive Asha Sharma, eliminating roughly 3,200 positions company-wide.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZeniMax_Media">ZeniMax Media - Wikipedia</a></li>
<li><a href="https://gameluster.com/onebgs-save-our-devs-march-xbox-layoffs/">OneBGS Plans 4-City March Over Xbox Layoffs</a></li>
<li><a href="https://www.gamespot.com/articles/bethesda-game-studios-is-now-unionized-across-the-board-recognized-by-microsoft/1100-6525206/">Bethesda Game Studios Is Now Unionized Across The Board ...</a></li>

</ul>
</details>

**Tags**: `#gaming-industry`, `#layoffs`, `#labor-unions`, `#xbox`, `#microsoft`

---

<a id="item-16"></a>
## [Microsoft struggles to fulfill its 2030 sustainability promise amid carbon-heavy AI expansions — the company's chief sustainability officer claims the target is still feasible](https://www.tomshardware.com/tech-industry/big-tech/microsoft-struggles-to-fulfill-its-2030-sustainability-promise-amid-carbon-heavy-ai-expansions-the-companys-chief-sustainability-officer-claims-the-target-is-still-feasible) ⭐️ 6.5/10

Microsoft's carbon emissions rose 25% in FY2025 due to AI data center expansion, challenging its 2030 sustainability goals despite progress in water and waste management.

rss · Tom's Hardware · Jul 11, 12:45

**Tags**: `#AI`, `#sustainability`, `#Microsoft`, `#data-centers`, `#carbon-emissions`

---

<a id="item-17"></a>
## [SK hynix and TetraMem Build Memristor In-Memory SoC for Edge AI](https://www.tomshardware.com/tech-industry/artificial-intelligence/sk-hynix-and-tetramem-collaborate-on-experimental-chip-to-bolster-energy-efficiency-for-edge-ai-devices-memristor-based-in-memory-soc-research-leaves-performance-questions-up-in-the-air) ⭐️ 6.5/10

SK hynix, TetraMem, and the University of Southern California have jointly developed a memristor-based in-memory computing system-on-chip (SoC) targeting energy-efficient AI edge devices. The experimental chip showed promising energy efficiency results, but the research team has not yet demonstrated that the architecture can deliver competitive performance. Edge AI devices—from smartphones to IoT sensors—are constrained by tight power budgets, making energy efficiency a critical design priority. Memristor-based in-memory computing could dramatically reduce the energy consumed by AI inference by eliminating the data movement bottleneck in conventional von Neumann architectures, potentially reshaping the competitive landscape for low-power AI hardware. The collaboration leverages TetraMem's analog memristor crossbar technology integrated with CMOS, following TetraMem's prior Nature publication on memristor-CMOS integration. While the chip achieves notable energy efficiency gains, the article notes that performance benchmarks have not been fully disclosed, leaving open whether the design can match the throughput of competing edge AI accelerators.

rss · Tom's Hardware · Jul 10, 16:58

**Background**: A memristor is a non-linear two-terminal electronic component whose resistance changes based on the amount of charge that has flowed through it, and it retains that resistance state even when power is removed—effectively combining memory and computation in a single device. In-memory computing (IMC) is an emerging non-von Neumann paradigm that performs computations directly within memory arrays rather than shuttling data between separate processing and memory units, which is particularly attractive for AI workloads dominated by multiply-accumulate operations on large vectors. TetraMem, a startup spun out of USC research, is a pioneer in analog memristor technology and has previously demonstrated memristors capable of operating at extreme temperatures (700°C), highlighting the technology's potential robustness for harsh-environment and space applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Memristor">Memristor - Wikipedia</a></li>
<li><a href="https://research.ibm.com/projects/in-memory-computing">In-memory computing - IBM Research</a></li>
<li><a href="https://thenextweb.com/news/tetramem-memristor-700c-space-ai-computing">TetraMem memristor survives 700 degrees Celsius as startup moves...</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#edge-AI`, `#memristors`, `#in-memory-computing`, `#semiconductors`

---

<a id="item-18"></a>
## [独家 | 智谱创始人唐杰发内部信：「GLM 时刻」之后，什么是更重要的事](https://36kr.com/p/3891132709206784?f=rss) ⭐️ 6.3/10

Zhipu AI founder Tang Jie's internal letter reveals the company's strategic bet on Coding/Reasoning capabilities post-DeepSeek R1, leading to 10x market cap growth, HK$1T+ valuation, and GLM-5.2 open-source model matching Claude Opus 4.8 and GPT-5.5.

rss · 36氪 · Jul 11, 11:28

**Tags**: `#Zhipu-AI`, `#GLM-5.2`, `#AI-Coding`, `#Chinese-AI`, `#Open-Source-LLMs`

---

<a id="item-19"></a>
## [9点1氪丨“国产存储第一股”长鑫科技公布承销团阵容；SK海力士登陆美股，上市首日大涨近13%；OpenAI推出ChatGPT智能体](https://36kr.com/p/3890553690192384?f=rss) ⭐️ 6.3/10

Daily tech news roundup highlighting SK Hynix's successful ~$265B US listing, OpenAI's ChatGPT agent launch, and Long Xin Technology's IPO underwriting team announcement as China's domestic storage leader.

rss · 36氪 · Jul 11, 01:24

**Tags**: `#AI`, `#semiconductors`, `#IPO`, `#OpenAI`, `#Chinese-tech`

---

<a id="item-20"></a>
## [An Oral History of the Groundbreaking VFX Technology Behind Terminator 2](https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/) ⭐️ 6.0/10

VFXBlog published an in-depth oral history documenting the pioneering visual effects technology created for Terminator 2: Judgment Day (1991), featuring interviews with the engineers and artists who invented many of the techniques now standard in the industry. Terminator 2 was a landmark film that pushed the boundaries of what was possible in visual effects, and the techniques developed for it — including morphing, go-motion animation, and early CGI character work — laid the foundation for modern VFX. Understanding this history helps current practitioners appreciate the origins of tools and workflows still in use today. The film's effects were developed by four core groups: Industrial Light & Magic (ILM), Stan Winston Studio, Fantasy II Film Effects, and 4-Ward Productions, with additional work from Pacific Data Images. The T-1000's liquid metal transformations relied on morphing technology using Cyberware head and face scanners, while the T-800's stop-motion scenes used ILM's go-motion technique — co-developed with Phil Tippett — to introduce motion blur into each frame.

hackernews · markus_zhang · Jul 10, 16:48 · [Discussion](https://news.ycombinator.com/item?id=48862365)

**Background**: Morphing is a visual effects technique that seamlessly transforms one image or shape into another, replacing older dissolve-based methods since the early 1990s. Go-motion is a variation of stop-motion animation developed by ILM and Phil Tippett that adds motion blur to each frame, overcoming the staccato, overly sharp look of traditional stop-motion. Together, these techniques — along with early morphing composites created using Softimage software — helped define the look of the T-1000 and remain influential in how digital characters are animated today.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Special_effects_of_Terminator_2:_Judgment_Day">Special effects of Terminator 2: Judgment Day - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Morphing">Morphing - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Go_motion">Go motion - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the oral history as an exceptional read, expressing surprise at how much of the VFX pipeline had to be invented from scratch. Several added valuable context, including the role of Softimage in the production, the practical squibs used for liquid metal bullet impacts, and a recommendation for the documentary 'Jurassic Punk' (2022) about ILM artist Steve 'Spaz' Williams. Some readers reflected on whether contemporary CGI will age as gracefully as the practical and early-digital effects of T2.

**Tags**: `#visual-effects`, `#computer-graphics`, `#film-history`, `#technology-history`, `#CGI`

---