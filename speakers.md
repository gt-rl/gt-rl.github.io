---
layout: default
---

# Speakers

## Foundation talks

<div class='orgWrapper'>
<img align="left" src="https://tda-in-ml.github.io/assets/images/sk.jpg" alt="Smita Krishnaswamy" width="150">
<div class='bioWrapper'>
[**Smita Krishnaswamy**](https://www.krishnaswamylab.org) is an associated professor in the Departments of Genetics and Computer Science at the Yale University. She is also affiliated with Yale's Center for Biomedical Data Science, Cancer Center, and Applied Math Program. Her research focuses on developing representation learning methods (esp. graph signal processing and deep-learning) to denoise, impute, visualize and extract structure, patterns and relationships from big biomedical data. Her methods have been applied variety of datasets from many systems including embryoid body differentiation, EMT in breast cancer, lung cancer immunotherapy, infectious diseases, gut microbiome, and patient data. She has co-organized the Modeling of Biological Data (MOB) workshop co-located with the Design Automation Conference (DAC) in 2013, was co-chair of the technical program committee of the International Workshop on Bio-Design Automation in 2012 and has served on the technical program committee of several conferences including ICML, NeurIPS, ICLR,  Research on Computational Molecular Biology (RECOMB), ACM Conference on Bioinformatics, Computational Biology  and Health Informatics (ACMBCB), Design Automation Conference, and PSB Cancer Panomics. In addition, her lab offers a week-long bootcamp workshop on Machine Learning for Single Cell Analysis (krishnaswamylab.org/workshop) on an annual basis.
</div>
</div>

<div style="text-align:center">
&#10086;
</div>

<div class='orgWrapper'>
<img align="left" src="/assets/images/bs.jpg" alt="Bernadette Stolz" width="150">
<div class='bioWrapper'>
[**Bernadette Stolz**](https://www1.maths.ox.ac.uk/people/bernadette.stolz) is a researcher in the Centre for Topological Data Analysis at the Mathematical Institute at the University of Oxford. She is interested in applying ideas from topology to study the shape of biological data and gain novel insights into complex biological processes. Before pursuing her DPhil, Bernadette obtained an MSc in Mathematical Modelling and Scientific Computing from the University of Oxford in 2014, as well as two undergraduate degrees from the University of Bern (BSc in Mathematics, 2012) and the University of Göttingen (BSc in Molecular Medicine, 2009). As part of her degrees she also spent time studying at Charles University in Prague (2011) and conducted two short research projects at the University of Cambridge (2008 and 2009).
</div>
</div>

| **Topological Data Analysis and Geometric Anomaly Detection** |
| Topological data analysis (TDA) refers to the mathematical field that studies 'shape' of data. Research in this area has attracted a lot of interest over the last two decades with an increasing range of applications to real-world data. The most prominent method in TDA is persistent homology (PH), an algorithm that computes topological features such as connected components (dimension 0), loops (dimension 1), and voids (dimension 2) and how they change across different scales in the data. These multi-scale topological features are summarised in structures called barcodes, which can be equipped with a metric that is stable with respect to small perturbations to the data. However, this metric alone is not suitable for integration with machine learning, which has lead to the development of stable vectorisation methods such as persistence landscapes and persistence images. In this talk I will give an introduction to TDA and, in particular, PH as well as different vectorisation methods.  I will further demonstrate how we can apply local computations of PH to successfully identify non-manifold regions in two completely different data sets whose underlying spaces do not follow the manifold hypothesis and are known to admit singularities. |

## Invited talks

<div class='orgWrapper'>
<img align="left" src="/assets/images/sj.jpg" alt="Stefanie Jegelka" width="150">
<div class='bioWrapper'>
[**Stefanie Jegelka**](https://people.csail.mit.edu/stefje/)
is an Associate Professor in the Department of EECS at
MIT. Before joining MIT, she was a postdoctoral researcher at UC
Berkeley, and obtained her PhD from ETH Zurich and the Max Planck
Institute for Intelligent Systems. Stefanie has received a Sloan
Research Fellowship, an NSF CAREER Award, a DARPA Young Faculty Award,
Google research awards, a Two Sigma faculty research award, the German
Pattern Recognition Award, a Best Paper Award at ICML and an invitation
as sectional lecturer at the International Congress of Mathematicians.
She has co-organized multiple workshops on (discrete) optimization in
machine learning and graph representation learning, and serves as an
Action Editor at JMLR and a program chair of ICML 2022. Her research
interests span the theory and practice of algorithmic machine learning,
in particular, learning problems that involve combinatorial structure.
</div>
</div>

| **Sign and Basis Invariant Networks for Spectral Graph Representation Learning** |
| Many machine learning tasks involve processing eigenvectors derived from data. Especially valuable are Laplacian eigenvectors, which capture useful structural information about graphs and other geometric objects. However, ambiguities arise when computing eigenvectors: for each eigenvector v, the sign flipped version -v is also an eigenvector. More generally, higher dimensional eigenspaces contain infinitely many choices of basis eigenvectors. These ambiguities make it a challenge to process eigenvectors and eigenspaces in a consistent way. In response, we study new neural architectures that are invariant to all requisite symmetries and hence process collections of eigenspaces in a principled manner. Our networks are universal, i.e., they can approximate any continuous function of eigenvectors with the proper invariances. They are also theoretically strong for graph representation learning -- they can approximate any spectral graph convolution, can compute spectral invariants that go beyond message passing neural networks, and can provably simulate previously proposed graph positional encodings. Experiments show the strength of our networks on a variety of tasks. 

This talk is based on joint work with Derek Lim, Joshua Robinson, Lingxiao Zhao, Tess Smidt, Suvrit Sra and Haggai Maron. |

<div style="text-align:center">
&#10086;
</div>

<div class='orgWrapper'>
<img align="left" src="/assets/images/rk.png" alt="Roland Kwitt" width="150">
<div class='bioWrapper'>
[**Roland Kwitt**](https://rkwitt.github.io) is a full professor for
machine learning in the Department of Artificial Intelligence and Human
Interfaces (AIHI) at the University of Salzburg (PLUS), Austria. Prior
to that, he was part of the medical imaging and computer vision group at
Kitware Inc., North Carolina, USA. Roland's research spans multiple areas, but
mostly focusses on theoretical and practical aspects of learning methods
that allow to leverage and control structural characteristics of data.
He is also a member of the ELLIS society.
</div>
</div>

| **Topologically Densified Distributions** |
| In this talk, I am going to discuss some recent advances in the context of (topological) regularization for small sample-size learning with overparametrized neural networks. Specifically, I will shift focus from architectural properties, such as norms on the network weights, to properties of the internal representations before a linear classifier. In particular, I will advocate a topological constraint on samples drawn from the probability measure induced in that space. This provably leads to mass concentration effects around the representations of training instances, i.e., a property beneficial for generalization. Importantly, the topological constraints can be imposed in an efficient manner by leveraging results from prior work. A series of experiments on popular (vision) benchmarks provides strong empirical evidence to support the claim for better generalization in the small sample-size regime. |

<div style="text-align:center">
&#10086;
</div>

<div class='orgWrapper'>
<img align="left" src="/assets/images/ct.png" alt="Chad Topaz" width="150">
<div class='bioWrapper'>
[**Chad Topaz**](https://chadtopaz.com) (A.B. Harvard, Ph.D. Northwestern)
is an applied mathematician and data scientist. His current research
applies quantitative tools to expose and remedy social injustice, and is
based out of the Institute for the Quantitative Study of Inclusion,
Diversity, and Equity (QSIDE), which he co-founded. Chad is also
Professor of Mathematics at Williams College and, previously, at
Macalester College, where his research on complex and nonlinear systems
has been supported by the National Science Foundation from 2006 – 2021.
</div>
</div>

| **Topological Data Analysis of Collective Motion** |
| Collective behaviors abound anywhere in nature that objects or agents interact. Investigators modeling collective behavior face a variety of challenges involving data from simulation and/or experiment. These challenges include exploring large, complex data sets to understand and characterize the system, inferring the model parameters that most accurately reflect a given data set, and assessing the goodness-of-fit between experimental data sets and proposed models. Topological data analysis provides a lens through which these challenges may be addressed. I will highlight how topological techniques, sometimes in concert with machine learning, can be applied to models arising from the study of groups displaying collective motion, such as bird flocks, fish schools, and insect swarms. The key approach is to characterize a system's dynamics via the time-evolution of topological invariants called Betti numbers, accounting for persistence of topological features across multiple scales. |

## Case studies

- [Tara Chari](https://scholar.google.com/citations?user=ivMagPQAAAAJ&hl=en), California Institute of Technology<br />
  *Distortion of Single-Cell Data in Two-Dimensional Embeddings*
- [Dmitry Kobak](https://dkobak.github.io), Tübingen University
- [Jessica Moore](https://www.linkedin.com/in/jessica-moore-b0298794/), Yale University<br />
  *G2 stem cells orchestrate time-directed, long-range coordination of calcium signaling during skin epidermal regeneration*

## Panellists

- [Tara Chari](https://scholar.google.com/citations?user=ivMagPQAAAAJ&hl=en), California Institute of Technology
- [Corinna Coupette](https://people.mpi-inf.mpg.de/~coupette), Max Planck Institute for Informatics
- [Sergey Ivanov](https://nd7141.github.io/), Criteo AI Labs
- [Dmitry Kobak](https://dkobak.github.io), Tübingen University
- [Leland McInnes](https://ca.linkedin.com/in/leland-mcinnes-406233103),
  Tutte Institute for Mathematics and Computing
- [Christopher Morris](https://chrsmrrs.github.io), Mila – Quebec AI Institute \& McGill University
- [Chad Topaz](https://chadtopaz.com), Williams College

More speakers to be listed soon!
