
---
title: 'Desalination and brine treatment systems integrated modelling framework: simulation and evaluation of water and resource recovery'
tags:
  - Python
  - Desalination
  - Brine treatment
  - resource recovery
  - Techno-economic assessment 

authors:
  - name: Rodoula Ktori
    affiliation: 1 
  - name: Fabrizio Vassallo
    affiliation: 2
  - name: Giovanni Virruso
    affiliation: 2
  - name: Carmelo Morgante
    affiliation: 2
  - name: Andrea Culcasi
    affiliation: 2
  - name: Dionysia Diamantidou
    affiliation: 3
  - name: Niels Van Linden
    affiliation: 3
  - name: Alessandro Trezzi
    affiliation: 4
  - name: Adithya Krishnan
    affiliation: 5
  - name: Andrea Cipollina
    affiliation: 2
  - name: Giorgio Micale
    affiliation: 2
  - name: Mark C.M. van Loosdrecht
    affiliation: 1
  - name: Dimitrios Xevgenos
    affiliation: 6

affiliations:
 - name:  Department of Biotechnology, Delft University of Technology, Van der Maasweg 9, 2629 HZ, Delft, The Netherland
   index: 1
- name: Dipartimento di Ingegneria, Università degli Studi di Palermo - viale delle Scienze Ed.6, 90128 Palermo, Italy
   index: 2
- name: Lenntech BV, Distributieweg 3, 2645 EG Delfgauw, The Netherlands
   index: 3
- name: Sofinter S.p.A, Piazza Francesco Buffoni, 3, 21013 Gallarate VA, Italy
   index: 4
- name: Water & Energy Intelligence BV, the Netherlands
   index: 5
- name: Department of Engineering Systems and Services, Delft University of Technology, Jaffalaan 5, 2628 BX Delft, The Netherlands
   index: 6
  
bibliography: paper.bib
---

# Summary 

Desalination plays a crucial role in addressing the growing challenges of water scarcity. In recent years, the integration of desalination and brine treatment technologies has been increasingly studied, aiming to develop sustainable solutions for resource recovery from seawater. However, designing treatment chains and optimizing these processes for maximum efficiency, sustainability, and cost-effectiveness are complex tasks that require data, sophisticated analysis and decision-making strategies.
Our software offers a comprehensive modelling framework for simulating desalination and minerals recovery systems. Integrating technical process models with economic and environmental analysis provides valuable insights into the integration of these technologies and their impact on production efficiency, energy consumption, and environmental performance.
Through our software's simulations, researchers, engineers, and policymakers gain the power to evaluate the resource recovery potential, economics, and greenhouse gas emissions associated with different configuration combinations. This empowerment with crucial information for early-stage design and strategic planning is a significant step toward fostering more sustainable water management practices.

# Statement of need
Traditionally, simulation models were developed to evaluate the influence of certain parameters on the characteristics of the recovered products and the performance of the technology in terms of energy, chemicals, and water consumption. In the desalination field, there is a lack of open-access simulation models. While commercial software programs, like WAVE (Dupont, 2024), exist for membranes, and numerous publications discuss techno-economic models for desalination (El-Dessouky and Ettouney, 2002) and brine treatment technologies (Xevgenos et al., 2015; Micari et al., 2020; Chen et al., 2021; Panagopoulos, 2021; Morgante et al., 2022; Poirier, Al Mhanna and Patchigolla, 2022), there is a noticeable absence of open-access simulation tools in the literature. With the shift towards circular systems and integrated desalination and brine treatment technologies for resource recovery, there is a need for a unified tool that integrates simulation models for each technology. 
Simulation and evaluation are essential for informing future design and decision-making processes. An open-access simulation tool is essential in the field of desalination to improve the credibility of evaluations, facilitate study repeatability, support validation efforts, and enable comparisons.
Therefore, while the modelling of desalination and brine treatment processes has been extensively studied in the literature, our software offers an integrated platform for integrating these models and facilitating seamless data exchange. Based on this need, we provide, for the first time, open-source software that brings together a range of technical processes and economic models developed over the last decades. By making these models accessible and transparent, our software aims to advance research, engineering, and decision-making in the field of desalination and resource recovery.
The proposed software provides a variety of examples to help modellers design and evaluate different technical configurations. 

# Limitations 
The proposed software is not intended to be a substitute for sophisticated physical models or a system dynamics approach. In cases requiring detailed process representations, the process model may need to be enhanced to provide more detailed results and optimization opportunities. This work highlights that the proposed software is particularly valuable for evaluating the integration of different processes and preliminary designs, capturing the technical, economic, and environmental impacts of technology integration. 

# Acknowledgements 
The software was developed by Rodoula Ktori, with theoretical support from all co-authors. Technological experts conducted the validation of each simulation model for the respective technology: Nanofiltration: Dionysia Diamantidou, Niels van Linden; Multi-effect Distillation: Alessandro Trezzi; MF-PFR: Fabrizio Vassallo, Carmelo Morgante, Andrea Cipollina; EDBM: Giovanni Virruso, Andrea Culcasi; EFC: Marcos Rodriguez Pascual.

The development of technical process models was influenced by Xevgenos et al., (2023) and the following literature (Nayar et al., 2019; Morgante et al., 2022; Cassaro et al., 2023). The development of economic models was influenced by (Peters, Timmerhaus and West, 2003; Abraham and Luthra, 2011; Bilton et al., 2011; Kesieme et al., 2013; Choi et al., 2015). The analysis and comparison were developed based on (Ktori et al., 2024) and Ktori et., (under review). 
This work was supported by the EU within the WATER MINING (Next generation water-smart management systems: large scale demonstrations for a circular economy and society) - Horizon 2020 research and innovation programme under grant agreement No 869474.

# References 
Abraham, T. and Luthra, A. (2011) ‘Socio-economic & technical assessment of photovoltaic powered membrane desalination processes for India’, Desalination, 268(1–3), pp. 238–248. doi: 10.1016/j.desal.2010.10.035.
Bilton, A. M. et al. (2011) ‘On the feasibility of community-scale photovoltaic-powered reverse osmosis desalination systems for remote locations’, Renewable Energy, 36(12), pp. 3246–3256. doi: 10.1016/j.renene.2011.03.040.
Cassaro, C. et al. (2023) ‘Electrodialysis with Bipolar Membranes for the Sustainable Production of Chemicals from Seawater Brines at Pilot Plant Scale’, ACS Sustainable Chemistry and Engineering, 11(7). doi: 10.1021/acssuschemeng.2c06636.
Chen, Q. et al. (2021) ‘A zero liquid discharge system integrating multi-effect distillation and evaporative crystallization for desalination brine treatment’, Desalination, 502, p. 114928. doi: 10.1016/J.DESAL.2020.114928.
Choi, Y. et al. (2015) ‘Economic evaluation of a hybrid desalination system combining forward and reverse osmosis’, Membranes, 6(1). doi: 10.3390/membranes6010003.
El-Dessouky, H. T. and Ettouney, H. M. (2002) Fundamentals of Salt Water Desalination. First edit. Edited by Elsevier.
Kesieme, U. K. et al. (2013) ‘Economic analysis of desalination technologies in the context of carbon pricing , and opportunities for membrane distillation’, DES, 323, pp. 66–74. doi: 10.1016/j.desal.2013.03.033.
Ktori, R. et al. (2024) ‘Sustainability assessment framework for integrated desalination and resource recovery: a participatory approach’, TechRxiv. doi: 10.36227/techrxiv.170595103.36689587/v1.
Micari, M. et al. (2020) ‘Techno-economic analysis of integrated processes for the treatment and valorisation of neutral coal mine effluents’, Journal of Cleaner Production, 270, p. 122472. doi: 10.1016/J.JCLEPRO.2020.122472.
Morgante, C. et al. (2022) ‘Valorisation of SWRO brines in a remote island through a circular approach: Techno-economic analysis and perspectives’, Desalination, 542(August), p. 116005. doi: 10.1016/j.desal.2022.116005.
Nayar, K. G. et al. (2019) ‘Cost and energy requirements of hybrid RO and ED brine concentration systems for salt production’, Desalination, 456, pp. 97–120. doi: 10.1016/J.DESAL.2018.11.018.
Panagopoulos, A. (2021) ‘Beneficiation of saline effluents from seawater desalination plants: Fostering the zero liquid discharge (ZLD) approach - A techno-economic evaluation’, Journal of Environmental Chemical Engineering. doi: 10.1016/j.jece.2021.105338.
Peters, M. ., Timmerhaus, K. D. and West, R. E. (2003) Plant Design and Economics for Chemical Engineers. Fifth. New York: McGraw-hill.
Poirier, K., Al Mhanna, N. and Patchigolla, K. (2022) ‘Techno-Economic Analysis of Brine Treatment by Multi-Crystallization Separation Process for Zero Liquid Discharge’, Separations, 9(10). doi: 10.3390/separations9100295.
Xevgenos, D. et al. (2015) ‘Design of an innovative vacuum evaporator system for brine concentration assisted by software tool simulation’, Desalination and Water Treatment, 53(12), pp. 3407–3417. doi: 10.1080/19443994.2014.948660.
Xevgenos, D. et al. (2023) Deliverable 3.1 Report on the design procedure including bench-scale tests for CS1 and CS2.