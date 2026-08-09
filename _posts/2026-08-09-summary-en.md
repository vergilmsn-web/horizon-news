---
layout: default
title: "Horizon Summary: 2026-08-09 (EN)"
date: 2026-08-09
lang: en
---

> From 29 items, 14 important content pieces were selected

---

1. [FCC moves to ban LiDAR-equipped foreign drones from US — classifies the technology as "military-grade" in a proposal that could also hit thermal models and the swarms used in drone light shows](#item-1) ⭐️ 7.5/10
2. [Amazon’s new 7.65GW Texas AI data center power plant could become the largest source of CO₂ pollution in the US — custom 35-turbine gas plant authorized to emit 33 million tons of annual greenhouse gases](#item-2) ⭐️ 7.5/10
3. [Phantom Drive: Open-Source USB Hides Encrypted Partition Behind Decoy](#item-3) ⭐️ 7.5/10
4. [Shopify replaced Redis with MySQL for inventory reservations–and it scaled](#item-4) ⭐️ 7.0/10
5. [Amazon uses 45-year-old rules to bypass Gilroy community vote for AI data center](#item-5) ⭐️ 6.5/10
6. [Delta GoCool-150 150kW Liquid-to-Air CDU Targets NVIDIA VR NVL72](#item-6) ⭐️ 6.5/10
7. [UK Study: E-Scooters More Dangerous Than Motorcycles; DeepMind AI Predicts Hurricane Melissa Early](#item-7) ⭐️ 6.3/10
8. [Nvidia RTX Spark Geekbench Leak Reveals 20-core and 18-core Variants](#item-8) ⭐️ 5.5/10
9. [Kansas Town Ends Public Comment, Goes Virtual After AI Data Center Death Threats](#item-9) ⭐️ 5.5/10
10. [Intel Core Ultra 7 270K Plus vs AMD Ryzen 7 7700X3D Faceoff](#item-10) ⭐️ 5.5/10
11. [Champion Coder Creates Self-Replicating Piet Quine as GIF](#item-11) ⭐️ 5.5/10
12. [Micron Offers Pennies for Crucial RAM Warranty Returns, Then Reverses](#item-12) ⭐️ 5.5/10
13. [Owner of Original Intel 8080 Pre-Production Rubylith Mask Seeks Restorer](#item-13) ⭐️ 5.5/10
14. [RTX 5090 Sold in 8-Motherboard Bundles in Taiwan](#item-14) ⭐️ 5.5/10

---

<a id="item-1"></a>
## [FCC moves to ban LiDAR-equipped foreign drones from US — classifies the technology as "military-grade" in a proposal that could also hit thermal models and the swarms used in drone light shows](https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows) ⭐️ 7.5/10

The FCC is proposing a retroactive sales ban on foreign-made drones with LiDAR and other 'military-grade' features, potentially removing popular DJI models from US stores.

rss · Tom's Hardware · Aug 9, 13:00

**Tags**: `#drones`, `#FCC`, `#regulation`, `#DJI`, `#LiDAR`

---

<a id="item-2"></a>
## [Amazon’s new 7.65GW Texas AI data center power plant could become the largest source of CO₂ pollution in the US — custom 35-turbine gas plant authorized to emit 33 million tons of annual greenhouse gases](https://www.tomshardware.com/tech-industry/data-centers/amazons-new-7-65gw-texas-ai-data-center-power-plant-could-become-the-largest-source-of-co2-pollution-in-the-us-custom-35-turbine-gas-plant-authorized-to-emit-33-million-tons-of-annual-greenhouse-gases) ⭐️ 7.5/10

Amazon is building a 7.65GW natural gas power plant in Texas for an AI data center, permitted to emit 33 million tons of CO2 annually—potentially making it the largest single source of US CO2 emissions.

rss · Tom's Hardware · Aug 9, 12:40

**Tags**: `#AI infrastructure`, `#data centers`, `#environmental impact`, `#energy policy`, `#Amazon`

---

<a id="item-3"></a>
## [Phantom Drive: Open-Source USB Hides Encrypted Partition Behind Decoy](https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data) ⭐️ 7.5/10

A new open-source project called 'Phantom Drive' creates a USB flash drive that appears as a standard 8GB device but hides an encrypted partition accessible only by creating a text file containing the password. The custom firmware intercepts the password during write operations and processes it directly in the microcontroller's SRAM, so the password itself is never written to flash storage. This project offers a hardware-level approach to plausible deniability for personal storage, complementing software-based solutions like VeraCrypt's hidden volumes. Privacy-conscious users, journalists, activists, and anyone facing device seizure or forensic inspection could benefit from a USB that leaves no cryptographic trace of a hidden volume on the device itself. The password never touches flash memory — custom firmware intercepts it and copies it into the microcontroller's SRAM only during the hashing operation, and SRAM is volatile so the credential disappears at power-off. Because the hidden partition and its authentication artifacts exist outside the visible 8GB storage area, forensic analysis of the decoy drive reveals nothing about the secret volume's existence.

rss · Tom's Hardware · Aug 9, 12:00

**Background**: Plausible deniability in encryption refers to the ability to deny that hidden encrypted data exists because its presence cannot be proven — typically by nesting one encrypted volume inside another so that disclosing the outer password exposes only innocuous content. Software tools like VeraCrypt implement this by hiding an inner volume within an outer volume at the filesystem level. 'Phantom Drive' moves the same idea down to the hardware/firmware layer by using a custom USB controller firmware, so the hidden partition is invisible not just at the filesystem layer but also in the raw storage layout, and the password itself never persists to non-volatile flash memory. SRAM (Static Random-Access Memory) is volatile memory inside the microcontroller that loses its contents when power is removed, making it suitable for transient password processing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.comparitech.com/blog/information-security/plausible-deniability-encryption/">What is plausible deniability (in encryption ) and does it work?</a></li>
<li><a href="https://stealthcloud.ai/cryptography/plausible-deniability-encryption/">Plausible Deniability in Encryption : VeraCrypt and Hidden</a></li>
<li><a href="https://en.wikipedia.org/wiki/Firmware">Firmware - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#open-source`, `#encryption`, `#hardware`, `#privacy`

---

<a id="item-4"></a>
## [Shopify replaced Redis with MySQL for inventory reservations–and it scaled](https://shopify.engineering/scaling-inventory-reservations) ⭐️ 7.0/10

Shopify details how they replaced Redis with MySQL for inventory reservations at scale, using a bounded pool of rows per item/location instead of quantity columns.

hackernews · adletbalzhanov · Aug 8, 22:32 · [Discussion](https://news.ycombinator.com/item?id=49226536)

**Tags**: `#shopify`, `#mysql`, `#redis`, `#scalability`, `#distributed-systems`

---

<a id="item-5"></a>
## [Amazon uses 45-year-old rules to bypass Gilroy community vote for AI data center](https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window) ⭐️ 6.5/10

Amazon secretly circumvented a community vote and public comment period in Gilroy, California by using 45-year-old zoning regulations to begin construction on a massive AI data center. Project negotiations began in 2020 with public comments open until 2024, but residents were caught unaware when construction commenced without their direct input. This incident highlights significant tensions between the rapid expansion of AI infrastructure required for technological advancement and local democratic processes. It raises broader questions about accountability and transparency in how tech giants build critical AI infrastructure in residential communities, potentially setting precedents for similar projects elsewhere. The project is reportedly valued at approximately $2 billion, with construction having proceeded under zoning rules designed long before the AI era. The legacy regulations allowed Amazon to avoid the public hearings that would normally apply to a development of this scale within city limits.

rss · Tom's Hardware · Aug 8, 13:51

**Background**: AI data centers differ significantly from traditional data centers in that they require far greater computational power, higher bandwidth, low-latency networking, and substantially more electricity to support GPU-intensive workloads. As the demand for AI-driven services grows, large tech firms have aggressively pursued land and permits across the United States, sometimes in rural or suburban communities. California legislators, including State Sen. Steve Padilla, have introduced bills aimed at regulating data center construction amid growing public concern about environmental, health, and economic impacts. The Gilroy case exemplifies how zoning ordinances drafted before the AI boom are being leveraged to approve modern infrastructure projects without adequate public oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/data-centers/amazon-secretly-circumvents-community-vote-for-massive-ai-data-center-45-year-old-rules-lock-gilroy-residents-out-of-public-comment-window">Amazon secretly circumvents community vote for massive AI ...</a></li>
<li><a href="https://www.gadgetreview.com/no-votes-no-hearings-how-amazon-built-a-2-billion-data-center-that-no-one-noticed">No Votes, No Hearings: How Amazon Built a $2 Billion Data ...</a></li>
<li><a href="https://calmatters.org/environment/2026/06/imperial-county-data-center/">Imperial County approved a massive data center. Then it ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#corporate accountability`, `#community impact`, `#Amazon`

---

<a id="item-6"></a>
## [Delta GoCool-150 150kW Liquid-to-Air CDU Targets NVIDIA VR NVL72](https://www.servethehome.com/deltas-gocool-150-goes-big-to-enable-150kw-liquid-to-air-cooling-for-asrock-racks-vr-nvl72/) ⭐️ 6.5/10

Delta has launched the GoCool-150, a 150kW liquid-to-air Coolant Distribution Unit (CDU) engineered to dissipate heat from ASRock Rack's NVIDIA VR NVL72 and other high-density AI racks. The unit acts as a large-scale heat exchanger to handle the extreme thermal loads generated by next-generation rack-scale AI systems. As AI accelerators push rack power densities beyond 100kW, air cooling is no longer viable, making high-capacity CDUs critical infrastructure. Delta's 150kW liquid-to-air CDU enables data centers to deploy liquid-cooled racks even without facility water connections, broadening the practical deployment scenarios for NVIDIA's Vera Rubin platform. The GoCool-150 uses a liquid-to-air topology, meaning it rejects heat to the ambient environment rather than to a facility water loop, which simplifies retrofits. With a 150kW capacity, a single unit can handle the thermal output of an entire NVL72-class rack, which integrates 72 Rubin GPUs and 36 Vera CPUs.

rss · ServeTheHome · Aug 8, 15:05

**Background**: A Coolant Distribution Unit (CDU) conditions, circulates, and distributes liquid coolant to IT equipment in data centers, bridging facility-level and rack-level cooling loops. NVIDIA's VR NVL72 is a rack-scale AI supercomputer combining 72 Rubin GPUs and 36 Vera CPUs with NVLink 6 interconnect, using a fully liquid-cooled, cableless tray design. As GPU power consumption per rack has grown from ~10kW in earlier generations to well over 100kW today, liquid cooling has transitioned from a niche HPC technology to a mainstream AI infrastructure requirement.

<details><summary>References</summary>
<ul>
<li><a href="https://nautilusdt.com/blog/what-is-a-coolant-distribution-unit-cdu/">What Is a Coolant Distribution Unit ( CDU )? - Nautilus Data ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72</a></li>
<li><a href="https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack">NVIDIA Launches Vera Rubin Architecture at CES 2026: The VR NVL72 Rack - StorageReview.com</a></li>

</ul>
</details>

**Tags**: `#liquid-cooling`, `#AI-infrastructure`, `#data-center`, `#NVIDIA-NVL72`, `#CDU`

---

<a id="item-7"></a>
## [UK Study: E-Scooters More Dangerous Than Motorcycles; DeepMind AI Predicts Hurricane Melissa Early](https://www.solidot.org/story?sid=85039) ⭐️ 6.3/10

An analysis of England and Wales trauma data (2020–2022) found adult e-scooter riders face 3.5× higher risk of traumatic brain injury than motorcyclists, while only 5.9% wore helmets. Meanwhile, Google DeepMind's WeatherNext AI model predicted Hurricane Melissa's Category 5 landfall in Jamaica five days in advance with 80% confidence, according to a Nature paper demonstrating one extra day of warning over conventional forecasting models. These findings highlight urgent public-safety concerns about e-scooter regulations and helmet compliance, while the WeatherNext breakthrough demonstrates how machine learning is reshaping life-saving disaster preparedness. The AI model's extra day of lead time can be the difference between life and death for communities in a hurricane's path. The trauma dataset covers 15,247 patients across 18 English/Welsh cities, including 580 e-scooter, 7,027 motorcycle, and 7,640 bicycle riders; female riders reported 2.1× higher likelihood of serious injury, likely because most e-scooters are designed for male body proportions. WeatherNext, developed jointly by Google DeepMind and Google Research, was trained on broad weather data to specialize in tropical cyclone prediction despite limited cyclone examples, and will be open-sourced.

rss · Solidot · Aug 8, 13:52

**Background**: E-scooters have proliferated in urban areas worldwide as convenient micro-mobility vehicles, but their safety profile has been widely debated as regulations struggle to keep pace with adoption. Hurricane Melissa struck Jamaica in October 2025, causing catastrophic flooding and landslides. Traditional weather forecasting relies on physics-based numerical models requiring enormous computational resources, while AI-based approaches like WeatherNext learn patterns directly from historical weather data to produce faster, cheaper, and sometimes more accurate predictions.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/">AI model achieves breakthrough in forecasting cyclones</a></li>
<li><a href="https://www.techtimes.com/articles/323617/20260808/weathernext-publishes-proof-cyclone-ai-gave-nhc-extra-day-warning-hurricane-melissa.htm">WeatherNext Publishes Proof: Cyclone AI Gave NHC Extra Day of...</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/weathernext-2/">WeatherNext 2: Google DeepMind’s most advanced forecasting model</a></li>

</ul>
</details>

**Tags**: `#public-safety`, `#e-scooter`, `#Google-DeepMind`, `#AI-weather-forecasting`, `#hurricane-prediction`

---

<a id="item-8"></a>
## [Nvidia RTX Spark Geekbench Leak Reveals 20-core and 18-core Variants](https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests) ⭐️ 5.5/10

Two variants of Nvidia's RTX Spark have appeared on Geekbench: a full 20-core SKU scoring 2,570 in single-core and 23,126 in multi-core, and a cut-down 18-core variant scoring 2,541 single-core and 21,776 multi-core. Both outperform most x86 mobile chips in both single- and multi-threaded workloads. These leaks suggest Nvidia is preparing both a flagship and a lower-tier RTX Spark for compact AI workstations and slim laptops, giving the Windows-on-Arm ecosystem a serious performance contender. The competitive multi-core numbers indicate the Grace Arm CPU is now mature enough to challenge established x86 mobile offerings in general-purpose workloads, not just AI acceleration. The 20-core SKU matches the previously announced GB10 Grace Blackwell Superchip configuration used in the DGX Spark, which pairs the Arm-based Grace CPU with a Blackwell GPU and up to 128GB of coherent unified LPDDR5x memory. The 18-core cut-down variant was not previously announced and likely targets a lower price point while retaining most of the multi-core throughput (only ~6% lower than the full chip).

rss · Tom's Hardware · Aug 9, 13:20

**Background**: The RTX Spark is the consumer-facing brand for Nvidia's GB10 Grace Blackwell Superchip, which combines an Arm-based Nvidia Grace CPU with a Blackwell-generation GPU on a single package connected via NVLink-C2C. It is positioned as a personal AI supercomputer capable of running large language models up to 200 billion parameters locally, delivering up to 1 petaFLOP of FP4 AI performance. The chip is the foundation of the DGX Spark desktop and is expected to extend to slimmer laptops and small-form-factor PCs running Windows on Arm.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/products/rtx-spark/">Slim Laptops & Small Desktops | NVIDIA RTX Spark</a></li>
<li><a href="https://dam-cdn.nvd.orangelogic.com/AssetLink/3lhuar5pc56pn7se4c7ahsskw20xw8h5.pdf">NVIDIA DGX Spark | NVIDIA</a></li>
<li><a href="https://www.linkedin.com/pulse/nvidia-rtx-spark-could-big-push-windows-arm-has-been-david-altavilla-mo37f">NVIDIA RTX Spark Could Be The Big Push Windows On Arm Has...</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#rtx-spark`, `#geekbench`, `#hardware-benchmarks`, `#gb10`

---

<a id="item-9"></a>
## [Kansas Town Ends Public Comment, Goes Virtual After AI Data Center Death Threats](https://www.tomshardware.com/tech-industry/data-centers/kansas-town-silences-public-comment-on-gigawatt-ai-data-center-after-receiving-death-threats-moves-to-virtual-meetings-shift-follows-physics-teachers-arrest-for-clapping-at-data-center-hearing) ⭐️ 5.5/10

Emporia, Kansas, eliminated public comment at city council meetings and switched entirely to virtual sessions after death threats against city leaders intensified over a proposed gigawatt-scale AI data center. The escalation follows the arrest of a physics teacher who was detained for clapping at a data center hearing. This case illustrates how the AI infrastructure boom is generating intense local opposition in small American communities, with civic backlash severe enough to suppress normal democratic participation. As hyperscale AI campuses increasingly require gigawatt-level power capacity—on par with the needs of small cities—such confrontations between tech-driven energy demand and local residents are likely to become more common. A gigawatt-scale data center consumes roughly 10x more power per rack than traditional facilities, drawing electricity comparable to that of a small city. The decision to end in-person public comment also affects residents who want to raise unrelated concerns, not just data center opponents, which has raised additional procedural questions.

rss · Tom's Hardware · Aug 9, 12:20

**Background**: AI data centers have rapidly scaled from tens of megawatts to gigawatt-class campuses as demand surges for training and serving large language models and other generative AI workloads. Companies like Meta have announced multi-billion-dollar, 1 GW facilities, highlighting how these projects dwarf traditional cloud data centers in both footprint and energy consumption. Small cities such as Emporia are now hosting or being considered for such projects because land and grid access are available, but the sudden arrival of industrial-scale infrastructure often clashes with local expectations.

<details><summary>References</summary>
<ul>
<li><a href="https://techplustrends.com/power-requirements-ai-data-centers/">Power Requirements for AI Data Centers (2026): Complete Guide</a></li>
<li><a href="https://www.novaedgedigitallabs.in/Blog/meta-10-billion-ai-data-center-indiana-2026">Meta's $10B AI Data Center : 1 Gigawatt Power (2026) | NovaEdge...</a></li>
<li><a href="https://inforcapital.com/news/africa-needs-grid-scale-energy-to-power-ai-data-centres/">Africa's AI Data Centers Need Gigawatt Power Overhaul</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#community impact`, `#civic engagement`, `#tech policy`

---

<a id="item-10"></a>
## [Intel Core Ultra 7 270K Plus vs AMD Ryzen 7 7700X3D Faceoff](https://www.tomshardware.com/pc-components/cpus/intel-core-ultra-7-270k-plus-vs-amd-ryzen-7-7700x3d-faceoff) ⭐️ 5.5/10

Tom's Hardware published a faceoff comparison pitting the Intel Core Ultra 7 270K Plus against the AMD Ryzen 7 7700X3D, evaluating both processors across gaming, productivity, power consumption, and overall value. This comparison targets consumers shopping in the upper mid-range CPU segment, where AMD's 3D V-Cache technology has historically dominated gaming benchmarks and Intel's latest Core Ultra architecture is attempting to reclaim ground. The AMD Ryzen 7 7700X3D leverages stacked 3D V-Cache technology to dramatically expand L3 cache capacity for gaming, while the Intel Core Ultra 7 270K Plus represents Intel's newer chiplet-based desktop architecture with revised efficiency and feature targets.

rss · Tom's Hardware · Aug 9, 12:05

**Background**: AMD's 3D V-Cache is a packaging technology that stacks an additional layer of L3 cache on top of the CPU die, effectively tripling the cache capacity available to the processor. This extra cache drastically reduces memory latency for gaming workloads, which is why X3D-branded Ryzen chips have consistently topped gaming benchmark charts since the original Ryzen 7 5800X3D launched in 2022. Intel's Core Ultra branding, introduced with Meteor Lake (Series 1) in late 2023, marks the company's shift to a chiplet-based design philosophy, with successive generations including Lunar Lake and Panther Lake (Series 3, launched at CES 2026) extending the lineup across mobile and desktop segments. The faceoff therefore pits AMD's proven gaming-centric cache advantage against Intel's newer architectural approach in a key price bracket.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/processors/technologies/3d-v-cache.html">AMD 3D V-Cache™ Technology</a></li>
<li><a href="https://www.digitaltrends.com/computing/what-is-amd-3d-v-cache/">What is AMD 3D V-Cache? Extra gaming performance unlocked What is 3D V-Cache? — AMD X3D Technology Explained What is AMD 3D V-Cache and why is it so special? - CORSAIR 3D V-Cache Explained: Why X3D CPUs Win at Gaming - Newegg.com What Is AMD 3D V-Cache and How Does It Work? - MUO</a></li>
<li><a href="https://en.wikipedia.org/wiki/Panther_Lake_(microprocessor)">Panther Lake (microprocessor) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#cpu-comparison`, `#intel`, `#amd`, `#hardware-review`, `#benchmark`

---

<a id="item-11"></a>
## [Champion Coder Creates Self-Replicating Piet Quine as GIF](https://www.tomshardware.com/software/programming/mind-bending-self-replicating-gif-code-prints-an-exact-copy-of-itself-is-both-a-program-and-its-own-visual-output-champion-coder-shows-off-piet-quine-technique) ⭐️ 5.5/10

A champion coder has created a 'Piet Quine' — a GIF image that functions simultaneously as a Piet program and as its own byte-for-byte visual output. The achievement merges the esoteric Piet language, whose programs resemble abstract paintings, with the concept of a quine, a self-reproducing program. This is a creative coding milestone in the esoteric programming community, demonstrating the extreme flexibility of the Piet language and pushing the boundaries of what counts as both source code and rendered output. While it has no direct practical impact on mainstream software engineering, it showcases the artistry and ingenuity possible in unconventional programming paradigms. The Piet Quine operates as both an executable program and a GIF image file, achieving byte-perfect self-replication across both the code and visual domains. The creator is described as a 'champion coder,' suggesting recognition within competitive or esoteric programming circles, though specific identity, competition placement, or technical constraints of the implementation are not detailed in the source material.

rss · Tom's Hardware · Aug 9, 11:40

**Background**: Piet is a stack-based esoteric programming language designed by David Morgan-Mar, in which programs are encoded as colored blocks arranged to resemble abstract paintings; commands are determined by transitions between colors arranged in hue and lightness cycles. A quine is a program that, when run, produces its own source code as output without reading its source file — a concept named after philosopher and logician Willard Van Orman Quine and connected to Kleene's recursion theorem in computability theory. Combining these two ideas means producing a visual artwork that, when interpreted as a Piet program, prints the exact pixel data of the artwork itself.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dangermouse.net/esoteric/piet.html">DM's Esoteric Programming Languages - Piet</a></li>
<li><a href="https://esolangs.org/wiki/Piet">Piet - Esolang</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quine_(computing)">Quine (computing) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#esoteric-programming`, `#quine`, `#piet`, `#creative-coding`, `#self-replicating-code`

---

<a id="item-12"></a>
## [Micron Offers Pennies for Crucial RAM Warranty Returns, Then Reverses](https://www.tomshardware.com/pc-components/ram/micron-reportedly-offers-pennies-on-the-dollar-for-crucial-ram-return-only-offers-to-reimburse-original-msrp-despite-it-being-only-37-percent-of-market-value-chipmaker-later-reverses-course-with-a-better-solution) ⭐️ 5.5/10

Micron initially offered to reimburse a Crucial memory owner at the product's original MSRP—which amounted to only 37% of current market value—when processing a warranty return for Crucial RAM, but later reversed course with a better solution after the story drew public attention. This matters to PC builders and Crucial customers who rely on lifetime warranty coverage, and it raises broader concerns about RMA fairness at a time when Micron is winding down its consumer memory business to focus on AI-driven data center products. 赔偿金额仅为当前市场价值的37%，意味着在美光修正方案之前，消费者在保修索赔中将承担63%的价值损失；Crucial内存由美光消费产品集团（Micron CPG）提供有限终身保修服务。

rss · Tom's Hardware · Aug 9, 11:20

**Background**: Crucial is Micron's consumer-facing memory brand that has sold retail RAM and SSDs for nearly 30 years. In December 2025, Micron announced it would exit the Crucial consumer business—including sales through retailers, e-tailers, and distributors—to refocus on AI-driven memory products. Crucial-branded memory modules are covered by a limited lifetime warranty that promises repair or replacement of products with defects in materials or workmanship. RAM market prices can fluctuate significantly from original MSRPs, particularly during supply shortages, which is what made the 37% reimbursement figure so stark.

<details><summary>References</summary>
<ul>
<li><a href="https://investors.micron.com/news-releases/news-release-details/micron-announces-exit-crucial-consumer-business">Micron Announces Exit from Crucial Consumer Business | Micron ...</a></li>
<li><a href="https://www.crucial.com/company/warranty">crucial .com/company/ warranty</a></li>
<li><a href="https://www.indmoney.com/blog/us-stocks/why-micron-is-killing-crucial-ram">Why Micron Is Killing Its Consumer Memory Business ‘Crucial’</a></li>

</ul>
</details>

**Tags**: `#micron`, `#crucial`, `#ram`, `#warranty`, `#consumer-rights`

---

<a id="item-13"></a>
## [Owner of Original Intel 8080 Pre-Production Rubylith Mask Seeks Restorer](https://www.tomshardware.com/pc-components/cpus/owner-of-original-intel-8080-pre-production-layout-seeks-restorer-handcrafted-rubylith-mask-shows-5-000-transistors-and-interconnect-patterns-of-the-fabled-2-mhz-cpu) ⭐️ 5.5/10

The owner of an original pre-production rubylith mask for the Intel 8080 microprocessor is seeking a skilled restorer to preserve this historically significant computing artifact. The handcrafted red film mask displays the layout of approximately 5,000 transistors and interconnect patterns of the 2 MHz CPU. This artifact represents the physical design blueprint of one of the most influential microprocessors in computing history — the 8080 helped launch the personal computer era and influenced countless successor architectures. Its preservation matters because such handcrafted design artifacts from the early semiconductor era are increasingly rare and serve as irreplaceable primary sources for understanding how pioneering CPUs were engineered. The rubylith mask shows approximately 5,000 transistors, consistent with the Intel 8080's known transistor count, and was produced by a hand-cut process where red translucent film layers were manually peeled away to define circuit patterns. These composite layers were then photographically reduced onto glass plates to produce photolithographic masks used in wafer fabrication.

rss · Tom's Hardware · Aug 9, 11:00

**Background**: The Intel 8080, released in 1974, was an 8-bit microprocessor and a major advancement over Intel's earlier 8008, running approximately ten times faster. It was among the first general-purpose microprocessors capable of operating independently, making it foundational to the personal computer revolution and a direct influence on later CPUs. Rubylith masks were the standard method for IC design in the 1970s: engineers hand-cut patterns into layers of red translucent rubylith film, peeled away selected areas to define circuit features, and then photographically reduced the combined layers onto glass plates to create photolithographic masks for silicon wafer fabrication.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel_8080">Intel 8080 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rubylith">Rubylith - Wikipedia</a></li>
<li><a href="https://www.computerhistory.org/revolution/story/287">Designing Integrated Circuits - CHM Revolution</a></li>

</ul>
</details>

**Tags**: `#intel-8080`, `#computing-history`, `#hardware-preservation`, `#rubylith-mask`, `#cpu-design`

---

<a id="item-14"></a>
## [RTX 5090 Sold in 8-Motherboard Bundles in Taiwan](https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090-ships-in-bizarre-8-motherboard-bundle-retailers-hold-gpus-hostage-similar-to-the-crypto-boom) ⭐️ 5.5/10

Taiwanese ecommerce platform PChome24h is selling Nvidia RTX 5090 graphics cards bundled with up to 8 motherboards, entry-to-mid-range GPUs, and other components, forcing buyers to purchase unwanted extra hardware to get the GPU they want. This bundling practice signals severe RTX 5090 supply constraints and mirrors scalping tactics seen during the cryptocurrency mining boom, when GPU availability was crippled by miners buying out stock. Consumers and PC builders in Taiwan are being forced to pay significantly more for a complete package they don't fully need. The RTX 5090 is built on Nvidia's Blackwell architecture with 32 GB of GDDR7 memory on a 512-bit interface, launched in January 2025 as the flagship of the RTX 50 series. The bundles include entry-to-mid-range GPUs alongside motherboards, suggesting retailers are offloading slow-moving inventory by tying it to scarce high-end products.

rss · Tom's Hardware · Aug 8, 17:08

**Background**: During the 2017–2021 cryptocurrency mining boom, GPUs were in extremely high demand from miners who needed them to mine coins like Ethereum. This led to widespread scalping, price gouging, and bundling tactics where retailers forced customers to buy unwanted components alongside scarce graphics cards. The RTX 5090, as Nvidia's current top-end consumer GPU based on the Blackwell architecture, is similarly in high demand from both gamers and AI/compute users. PChome24h is one of Taiwan's largest B2C ecommerce platforms, known for its 24-hour delivery service since 2007.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GeForce_RTX_50_series">GeForce RTX 50 series - Wikipedia</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/geforce-rtx-5090.c4216">NVIDIA GeForce RTX 5090 Specs | TechPowerUp GPU Database</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPU_mining">GPU mining - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#gpu`, `#nvidia`, `#rtx5090`, `#market-trends`

---