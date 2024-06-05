---
permalink: /research/
title: "Research"
author_profile: true
classes: wide
---

## LLM-based SoC Design Tools (Ongoing)

LLMs with powerful imitation and learning capability can not only handle tedious and repetitve work but also address more complex work that requires expertise and experiences. SoC design that consists of a set of connected standard IPs actually become a possible task for LLMs. We investigate the use of LLM for SoC design with a top-down approach ranging from architecture design, IP integration, processor customization, accelerator generation, SoC debug and verification.

[HLSPilot](https://github.com/xcw-1010/HLSPilot.git): This is an LLM-based HLS code generation framework that is capable to select the most time-consuming computing kernels with profling and converts the selected C/C++ kernels to Xilinx HLS automatically. Meanwhile, it leverages a DSE tool to further tune the generated HLS code for more efficient accelerator generation. Essentially, this framework provides a possible approach for automatic hardware accelerator generation with high-level code and it will be a key component of the LLM-based SoC design as well.
<!-- ## Software

TBC -->

<!-- https://github.com/bhargavvader/pycobra

<iframe src="https://ghbtns.com/github-btn.html?user={{ bhargavvader }}&repo={{ pycobra }}&type=star&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>

https://github.com/astha736/PACbayesianNMF

https://cran.r-project.org/web/packages/COBRA/index.html

https://cran.r-project.org/web/packages/pacbpred/index.html

https://i-pri.org/special/Biostatistics/Software/Geneland/ -->

## Domain-Specific Accelerator Design Tools (Ongoing)
We investigate DSA design automation approaches from different perspectives including HLS template based frameworks, hardware overlays, and domain specific languages. In order to optimize the resulting DSAs, DSE tools are also explored and integrated.

[DeepBurning-MixQ](https://github.com/fffasttime/AnyPackingNet.git) [BFS Accelerator](https://github.com/Liu-Cheng/bfs_with_Intel_OpenCL.git)


## Graph Processing Accelerators and Systems (Ongoing)
Graph processing is notorously difficult because of the irregular accesses and low compute-to-I/O ratio. We mainly investigate graph processing accelerators and processing systems on new hardware such as computational storage and heterogeneous architectures to address the computing challenge. In addition, we also extend our work to more graph-based algorithms and systems such as vector retrieval and graph learning.

[TaijiGraph](https://anonymous.4open.science/r/TaijiGraph2022)

## AIoT Processors and Computing Systems (Ongoing)
Deep learning is increasingly deployed in IoT devices and has become a major workload in IoTs. Prior works mainly utilize specialized accelerators or classical computing engines like DSP and MCUs for deep learning processing on IoTs. Providing specialized accelerators for different types of workloads induces larger soc design and more chip area, which is unacceptable for cost-effective IoT devices. Classical computing engines generally fail to achieve optimized deep learning processing due to the lack of native hardware support. While deep learning is much more compute-intenvie and memory-intensive compared to classical IoT workloads such as signal processing and data analytics, reusing classical computing engines will lead to suboptimal architectures for AIoTs eventually. In this case, we seek to extend typical deep learning accelerators for more IoT workloads like signal processing and generalize the capability of dee learning accelerators such that we can reuse deep learning accelerators for accelerating other IoT workloads without compromising the performance of deep learning.


## Fault-Tolerant Deep Learning (2021-2024)
We mainly investigate the design of deep learning toolchains all the way from deep learning applications to low-level circuit designs. Specifically, we explore model-independent fault-tolerant algorithm design, model-dependent fault-tolerant algorithm design, fault-tolerant compilation, fault-tolerant architecture design, fault-tolerant circuit design, and cross-layer fault-tolerant designs. In addition, we also develop a set of fault injection tools from different perspectives to assist fault-tolerant design at different abstraction levels.

[MRFI](https://github.com/fffasttime/MR-Neural-Network-Reliability-Analysis-Toolbox)

## DeepBurning: Automatic generation of FPGA-based learning accelerators (2018-2020)
DeepBurning is an end-to-end automatic neural network accelerator design tool for specialized learning tasks. It provides a unified deep learning acceleration solution to high-level application designers without dealing with the model training and hardware accelerator tuning. You can refer to DeepBurning homepage for more details.

[DeepBurning](https://github.com/groupsada/DeepBurning)

## QuickDough: A rapid loop acceleration on closely coupled CPU-FPGA architectures (2011-2016)
QuickDough is developed to address the FPGA design productivity problem. By utilizing a soft coarse-grained reconfigurable array (SCGRA) overlay built on top of off-the-shelf FPGAs, it compiles a high-level loop to the overlay through a rapid operation scheduling first and then generates the FPGA accelerator bitstream through a rapid integration of the scheduling result and a pre-built overlay bitstream.

[QuickDough](https://github.com/Liu-Cheng/QuickDough)

<!-- ### Current -->

<!-- **Project:**      
**Period:**      
**Amount:**      
**Founder:**      
**Role:**      
**Details:**      -->


