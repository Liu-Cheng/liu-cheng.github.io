---
pageClass: home-page
# some data for the components
name: Cheng Liu
profile: /profile.jpg

socials:
  - title: github
    icon: "/icons/github.svg"
    link: https://github.com/Liu-Cheng
  - title: linkedin
    icon: "/icons/linkedin-mono.svg"
    link: https://www.linkedin.com/feed/?trk=eml-wym-cta
  - title: googlescholar
    icon: "/icons/googlescholar.svg"
    link: https://scholar.google.com/citations?user=LVWU_VQAAAAJ&hl=en

email: liucheng (at) ict (dot) ac (dot) cn
address: Floor 5, No.6 Kexueyuan South Road, Haidian District, Beijing
---

<ProfileSection :frontmatter="$page.frontmatter" />

## About Me
I am an associate professor in State Key Laboratory of Processors (SKLP), Institute of Computing Technology (ICT), and work in IC design group led by Prof. Xiaowei Li and Prof. Huawei Li. I got my B.Eng degree and M.Eng degree from Harbin Institute of Technology in 2007 and 2009 respectively. I got my Ph.D degree from The University of Hong Kong advised by Prof. Hayden So in 2016. I also worked as a research fellow in Xtra group led by Prof. Bingsheng He in National University of Singapore from 2016 to 2018. My research interest includes domain specific architecture and system, in-storage processing, reconfigurable computing, and fault-tolerant computing.

## Vancancies
I am looking for self-motivated intern students. Students with EE and CS background are preferred. For intern students, it is possible to work fully remotely. Topics for interns are listed as follows. If you are interested in my research, contact me with email.

- LLM for DSA design automation
- AI for cross-layer chip design and optimization
- Automatic neural network accelerator customization on FPGAs 
- Light-weight neural network acceleration on the edge
- DSL-based graph processing accelerator and system
- In-storage big data processing systems (graph processing and information retriveal)
- Reliable AI toolchain development

## News

- [June 2020] Shengwen Liang and Rick Lee won the Third Prize (FPGA Track) of the 2020 IEEE Low-Power Computer Vision Challenge ([LPCVC](https://lpcv.ai/)).
- [July 2022] Haitong Huang, Erjing Luo, and Cangyuan Li in my group got the Third Place in DAC'22 SDC.
- [Jan. 2023] Our work "EnGN: A High-Throughput and Energy-Efficient Accelerator for Large Graph Neural Networks" won the Best Paper Award of TC'21.
- [Jan. 2023] Our work "S2Loop: a Lightweight Spectral-Spatio Loop Closure Detector for Resource-Constrained Platforms" is accepted by IEEE Robotics and Automation Letters.
- [Jan. 2023] Our work "MA-BERT: Towards Matrix Arithmetic-only BERT Inference by Eliminating Complex Non-linear Functions" is accepted by ICLR'23
- [Apr. 2023] Our work "Statistical Modeling of Soft Error Influence on Neural Networks" is accepted by TCAD'23.
- [May 2023] Our work "Accelerating Deformable Convolution Networks with Dynamic and Irregular Memory Accesses" is accepted by TODAES'23.
- [May 2023] Our work "Layer-Puzzle: Allocating and Scheduling Multi-Task on Multi-Core NPUs By Using Layer Heterogeneity" is accepted by DATE'23.
- [June 2023] <font color='red'> Congratulations! Haitong Huang, Erjing Luo, and Guoyu Li got the Second Place in DAC'23 SDC.
- [June 2023] <font color='red'> Our recent work about fault injection tools for neural network processing "MRFI: An Open Source Multi-Resolution Fault Injection Framework for Neural Network Processing" is accepted by CCF-CFTC'23.
- [July 2023] <font color='red'> Our recent work "DeepBurning-MixQ: An Open Source Mixed-Precision Neural Network Accelerator Design Framework for FPGAs" about HW/SW co-optimization for mixed-precision neural network accelerator design is accepted by ICCAD'23. It is also open sourced on github and you are welcome to try it.
 
## Funding
- Automatic Cross-Layer DSA Design and Optimization, 1 600 000￥, National Key Research and Development Program of China(2023-2025) 
- Intelligent In-Storage Big Data Processing System, 1 300 000￥, 1XX(2023-2024)
- Fault-tolerant Deep Learning Toolchain for COTS Devices, 300 000￥, XXX(2023)
- Elastic Fault-tolerant Deep Learning Processor Design, 570 000￥, NSFC(2022-2025)
- Customized Energy-efficient Graph Processing Acceleration on FPGAs, 300 000￥, NSFC(2020-2022)
- Fault-tolerant Deep Learning Processor Design Automation, 300 000￥, SKLCA(2021-2022)

## Talks
- 基于计算存储器的图处理系统设计, 面向复杂图计算应用的新型高能效体系结构论坛，CNCC，2022
- 容错深度学习处理器微结构设计，集成电路设计与自动化学术会议(CCF-DAC), 2021
- DeepBurning2.0: An Automatic End-to-end Neural Network Acceleration System on FPGAs, 华南理工大学，软件学院, 2019

## Services
- PC for:
  - DFT'22, FPT'22, ATS'23, FPT'23, DFT'23 
- Review for:
  - TPDS, TCAD, TC, TVLSI, JCST, TETC, JETC, IS
  - ITC'22, ITC'23, NIPS'23


## Graduate Students
- Erjing Luo (Intern from Beijing Institute of Technology, PhD candidate in University of Alberta)
- Zhiyu Zhu (Intern from Harbin Institute of Technology, CETC 47)
- Cheng Chu (Intern from Hefei University of Technology, PhD candidate in Indiana University Bloomington)
- Meng He (Intern from Hefei University of Technology, 字节跳动)
- Ziyang Zhu (Intern from Hefei University of Technology, 紫光展锐)
- Qiang Zhang (Master Student, 快手)
- Kouzi Xing (Intern from Hefei University of Technology, 商汤科技)
- Li Li (Intern from Hefei University of Technology, 京东)
- Kexin Chu (Intern from Hefei University of Technology, 百度)
- Kaijie Tu (Intern from Hefei University of Technology, 计算所)
- Chang Shi (Master student, Alibaba)
- Peibin Wu (Master student, MSRA)

<!-- Custom style for this page -->

<style lang="stylus">

.theme-container.home-page .page
  font-size 16px
  font-family "lucida grande", "lucida sans unicode", lucida, "Helvetica Neue", Helvetica, Arial, sans-serif;
  p
    margin 0 0 0.5rem
  p, ul, ol
    line-height normal
  a
    font-weight normal
  .theme-default-content:not(.custom) > h2
    margin-bottom 0.5rem
  .theme-default-content:not(.custom) > h2:first-child + p
    margin-top 0.5rem
  .theme-default-content:not(.custom) > h3
    padding-top 4rem

  /* Override */
  .md-card
    margin-top 0.5em
    .card-image
      padding 0.2rem
      img
        max-width 120px
        max-height 120px
    .card-content p
      -webkit-margin-after 0.2em

@media (max-width: 419px)
  .theme-container.home-page .page
    p, ul, ol
      line-height 1.5

    .md-card
      .card-image
        img 
          width 100%
          max-width 400px

</style>
