---
permalink: /research/
title: "Research"
author_profile: true
classes: wide
---

## LLM-based SoC Design Tools (Ongoing)

LLMs with powerful imitation and learning capability can not only handle tedious and repetitve work but also address more complex work that requires expertise and experiences. SoC design that consists of a set of connected standard IPs actually become a possible task for LLMs. We investigate the use of LLM for SoC design with a top-down approach ranging from architecture design, IP integration, processor customization, accelerator generation, SoC debug and verification.

[HLSPilot](https://github.com/xcw-1010/HLSPilot.git): This is an LLM-based HLS code generation framework that is capable to select the most time-consuming computing kernels with profling and converts the selected C/C++ kernels to Xilinx HLS automatically. Meanwhile, it leverages a DSE tool to further tune the generated HLS code for more efficient accelerator generation. Essentially, this framework provides a possible approach for automatic hardware accelerator generation with high-level code and it will be a key component of the LLM-based SoC design as well.


## Domain-Specific Accelerator Design Tools (Ongoing)
We investigate DSA design automation approaches from different perspectives including HLS template based frameworks, hardware overlays, and domain specific languages. In order to optimize the resulting DSAs, DSE tools are also explored and integrated.

[ApproxPilot](https://anonymous.4open.science/r/840c8c57-3c32-451e-bf12-0e243562/) This work presents a Graph Neural Network (GNN) model that leverages the physical connections of arithmetic units to capture their influence on the performance, power, area (PPA), and accuracy of the accelerator. Particularly, we notice that critical path plays a key role in node feature of the GNN model and having it embedded in the feature vector greatly enhances the prediction quality of the models. On top of the prediction models, we can further explore the large design space effectively and build an end-to-end accelerator approximation framework named ApproxPilot to optimize generic hardware accelerator approximation.

[DeepBurning-MixQ](https://github.com/fffasttime/AnyPackingNet.git) This work presents a pipelined neural network accelerator design framework DeepBurning-MixQ for FPGAs. It proposes to pack multiple low bit-width operations within a single primitive DSP of FPGAs and enables efficient acceleration of mixed-precision neural network models. In addition, it integrates NAS with the hardware acceleration such that it can optimizes both model accuracy and performance. 


## Graph Processing Accelerators and Systems (Ongoing)
Graph processing is notorously difficult because of the irregular accesses and low compute-to-I/O ratio. We mainly investigate graph processing accelerators and processing systems on new hardware such as computational storage and heterogeneous architectures to address the computing challenge. In addition, we also extend our work to more graph-based algorithms and systems such as vector retrieval and graph learning.

[HisOrder](https://github.com/RecoderChris/HisOrder.git) **This is my favoriate work!** We propose a graph reordering method, HisOrder, which improves graph locality to reduce the cache misses of graph processing systems. Unlike the previous reordering algorithms which depend on static characteristics of graphs, HisOrder firstly profiles the traces of Historical graph processing (primarily the concurrent frontiers) to construct the locality metric between vertices, and then utilizes an unsupervised ML method (K-means at present) to excavate the clusters of high locality to guide graph Reordering. Furthermore, since the learned clusters of vertices are more likely to be co-activated, HisOrder also fine-tunes the load balance in parallel graph processing with the clusters. It has been demonstrated to be effective for various graph processing systems such as Ligra, GPOP, and GridGraph.


[TaijiGraph](https://anonymous.4open.science/r/TaijiGraph2022) we propose a CSD-based out-of-core graph processing system called TaijiGraph. It systematically investigates the use of computational storage devices (CSDs), which offer in-storage computing facilities with higher I/O bandwidth, to improve both the data utilization and bandwidth utilization at the same time and enhance the overall I/O efficiency of out-of-core graph processing. Specifically, with programmable CSDs, we present a graph semantic aware data organization approach at the granularity of partitions to load only active partitions for higher utilization of the fetched data. We also customize the data layout to fit the internal storage architecture for parallel accesses and improve the I/O bandwidth utilization. In addition, we capture the dynamic status of graph tasks across the iterations and partitions at runtime and dynamically assign workloads to the preference of the CSD processors with restricted computing resources but higher IO bandwidth, which further improves the IO efficiency.

[Graphitron](https://github.com/VesperalKite/Graphitron)  We develop Graphitron, a domain-specific language (DSL), which allows users to generate customized accelerators for a wide range of graph processing algorithms on FPGAs without engaging with the complexities of low-level FPGA designs. Graphitron, by defining vertices and edges as primitive data types, naturally facilitates the description of graph algorithms using edge-centric or vertex-centric programming models. The Graphitron back-end employs a suite of hardware optimization techniques including pipelining, data shuffling, and memory access optimization that are independent with the specific algorithms, supporting the creation of versatile graph processing accelerators.

[BFS Accelerator](https://github.com/Liu-Cheng/bfs_with_Intel_OpenCL.git) It presents a fully pipelined BFS accelerator design based on HLS. Particularly, it proposes an graph reordering and padding algorithm to address the on-chip operation conflicts and enahnces the pipeline efficiency significantly. The resulting BFS acceleratror achives comparable performance over prior handcrafted designs.


## AIoT Processors and Computing Systems (Ongoing)
Deep learning is increasingly deployed in IoT devices and has become a major workload in IoTs. Prior works mainly utilize specialized accelerators or classical computing engines like DSP and MCUs for deep learning processing on IoTs. Providing specialized accelerators for different types of workloads induces larger soc design and more chip area, which is unacceptable for cost-effective IoT devices. Classical computing engines generally fail to achieve optimized deep learning processing due to the lack of native hardware support. While deep learning is much more compute-intenvie and memory-intensive compared to classical IoT workloads such as signal processing and data analytics, reusing classical computing engines will lead to suboptimal architectures for AIoTs eventually. In this case, we seek to extend typical deep learning accelerators for more IoT workloads like signal processing and generalize the capability of dee learning accelerators such that we can reuse deep learning accelerators for accelerating other IoT workloads without compromising the performance of deep learning.

[SigDLA](https://liu-cheng.github.io/files/sigdla.pdf) Deep learning and signal processing are closely correlated in many IoT scenarios such as anomaly detection to empower intelligence of things. Many IoT processors utilize digital signal processors (DSPs) for signal processing and build deep learning frameworks on this basis. While deep learning is usually much more computing-intensive than signal processing, the computing efficiency of deep learning on DSPs is limited due to the lack of native hardware support. In this case, we present a contrary strategy and propose to enable signal processing on top of a classical deep learning accelerator (DLA). Specifically, we propose a programmable data shuffling fabric and have it inserted between the input buffer and computing array of DLAs such that the irregular data is reorganized and the processing is converted to be regular. With the online data shuffling, the proposed architecture, SigDLA, can adapt to various signal processing tasks without affecting the deep learning processing. 

[MCU-MixQ](https://anonymous.4open.science/r/MCU-MixQ-FCD7) We propose to pack multiple low-bitwidth arithmetic operations within a single instruction multiple data (SIMD) instructions in typical MCUs, and then develop an efficient convolution operator by exploring both the data parallelism and computing parallelism in convolution along with the proposed SIMD packing. Finally, we further leverage Neural Architecture Search (NAS) to build a HW/SW co-designed MPNN design framework, namely MCU-MixQ. This framework can optimize both the MPNN quantization and MPNN implementation efficiency, striking an optimized balance between neural network performance and accuracy. 


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


