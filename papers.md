---
layout: default
---

# Accepted Papers

This is the list of all accepted papers. You can find more information
about each submission by following either the *Forum* link or by visiting
our [OpenReview Workshop Website](https://openreview.net/group?id=ICLR.cc/2022/Workshop/GTRL). Please note that not all submissions are revised yet.

Congratulations to all authors!

<div style="text-align:center">
&#10086;
</div>

**A Piece-wise Polynomial Filtering Approach for Graph Neural Networks** (Spotlight presentation)<br />
Vijay Lingam &bull; Chanakya Ajit Ekbote &bull; Manan Sharma &bull; Rahul Ragesh &bull; Arun Iyer &bull; SUNDARARAJAN SELLAMANICKAM<br />
<abstract>Graph Neural Networks (GNNs) exploit signals from node features and the input graph topology to improve node classification task performance. Recently proposed GNNs work across a variety of homophilic and heterophilic graphs. Among these, models relying on polynomial graph filters have shown promise. We observe that polynomial filter models, in several practical instances, need to learn a reasonably high degree polynomials without facing any over-smoothing effects. We find that existing methods, due to their designs, either have limited efficacy or can be enhanced further. We present a spectral method to learn a bank of filters using a piece-wise polynomial approach, where each filter acts on a different subsets of the eigen spectrum. The approach requires eigendecomposition for a few eigenvalues at extremes (i.e., low and high ends of the spectrum) and offers flexibility to learn sharper and complex shaped frequency responses with low-degree polynomials. We theoretically and empirically show that our proposed model learns a better filter, thereby improving classification accuracy. Our model achieves performance gains of up to ~6% over the state-of-the-art (SOTA) models.</abstract>

[PDF](https://openreview.net/pdf?id=BFLNoVWkag5) &bull;
[Poster](https://openreview.net/attachment?id=BFLNoVWkag5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BFLNoVWkag5)

<div style="text-align:center">
&#10086;
</div>

**An extensible Benchmarking Graph-Mesh dataset for studying Steady-State Incompressible Navier-Stokes Equations** <br />
Florent Bonnet &bull; Jocelyn Ahmed Mazari &bull; Thibaut Munzer &bull; Pierre Yser &bull; patrick gallinari<br />
<abstract>Recent progress in Geometric Deep Learning (GDL) has shown its potential to provide powerful data-driven models. This gives momentum to explore new methods for learning physical systems governed by Partial Differential Equations (PDEs) from Graph-Mesh data. However, despite the efforts and recent achievements, several research directions remain unexplored and progress is still far from satisfying the physical requirements of real-world phenomena. One of the major impediments is the absence of benchmarking datasets and common physics evaluation protocols. In this paper, we propose a 2-D graph-mesh dataset to study the airflow over airfoils at high Reynolds regime (from $10^6$ and beyond). We also introduce metrics on the stress forces over the airfoil in order to evaluate GDL models on important physical quantities. Moreover, we provide extensive GDL baselines. Code: https://github.com/Extrality/ICLR_NACA_Dataset_V0 
Dataset: https://data.isir.upmc.fr/extrality/</abstract>

[PDF](https://openreview.net/pdf?id=rqUUi4-kpeq) &bull;
[Poster](https://openreview.net/attachment?id=rqUUi4-kpeq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=rqUUi4-kpeq)

<div style="text-align:center">
&#10086;
</div>

**CubeRep: Learning Relations Between Different Views of Data** <br />
Rishi Sonthalia &bull; Anna Gilbert &bull; Matthew Durham<br />
<abstract>Multi-view learning tasks typically seek an aggregate synthesis of multiple views or perspectives of a single data set. The current approach assumes that there is an ambient space $X$ in which the views are images of $X$ under certain functions and attempts to learn these functions via a neural network. Unfortunately, such an approach neglects to consider the geometry of the ambient space. Hierarchically hyperbolic spaces (HHSes) do, however, provide a natural multi-view arrangement of data; they provide geometric tools for the assembly of different views of a single data set into a coherent global space, a \emph{CAT(0) cube complex}. In this work, we provide the first step toward theoretically justifiable methods for learning embeddings of multi-view data sets into CAT(0) cube complexes. We present an algorithm which, given a finite set of finite metric spaces (views) on a finite set of points (the objects), produces the key components of an HHS structure. From this structure, we can produce a \emph{CAT(0) cube complex} that encodes the hyperbolic geometry in the data while simultaneously allowing for Euclidean features given by the detected relations among the views.</abstract>

[PDF](https://openreview.net/pdf?id=BlWfnEZJTl9) &bull;
[Forum](https://openreview.net/forum?id=BlWfnEZJTl9)

<div style="text-align:center">
&#10086;
</div>

**Cycle Representation Learning for Inductive Relation Prediction** <br />
Zuoyu Yan &bull; Tengfei Ma &bull; Liangcai Gao &bull; Zhi Tang &bull; Chao Chen<br />
<abstract>Inductive relation prediction is an important learning task for knowledge graph completion. To predict the relation between two entities, one can use the existence of rules, namely a sequence of relations. Previous works primarily focus on searching the rules between entities. The space of rules is huge, and one has to sacrifice either efficiency or accuracy. In this paper, we consider rules as cycles and show that the space of cycles has a unique structure based on the mathematics of algebraic topology. By exploring the linear structure of the cycle space, we can improve the searching efficiency of rules. We propose to collect cycle bases that span the space of cycles. We build a novel GNN framework on the collected cycles to learn the representations of cycles, and to predict the existence/non-existence of a relation. Our method achieves state-of-the-art performance on popular benchmarks.</abstract>

[PDF](https://openreview.net/pdf?id=SYUMkBZk6gq) &bull;
[Poster](https://openreview.net/attachment?id=SYUMkBZk6gq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=SYUMkBZk6gq)

<div style="text-align:center">
&#10086;
</div>

**Decoupled Graph Neural Networks based on Label Agreement Message Propagation** <br />
Zhicheng An &bull; Zhengwei Wu &bull; Binbin Hu &bull; Zhiqiang Zhang &bull; JUN ZHOU &bull; Yue Wang &bull; Shao-Lun Huang<br />
<abstract>Decoupling has become a new paradigm in Graph Neural Networks (GNNs) for its effectiveness and scalability.  However, this paradigm still faces two several restrictions: unsatisfying propagation, caused by noisy or confused edges, could greatly degrade model performance; fixed aggregation schema with the same propagation steps and the same combination weights for each node limit achieving optimal performance. To address these problems, we propose a novel decoupled graph model named LA-DGNN based on label agreement message propagation and combine the intermediate feature after each propagation step as input. In our method, we decouple the graph model which trains a base predictor based on multi-layer perceptrons with a pre-step to propagate features and a post-step to propagate labels. We utilize an auxiliary label agreement model to generate proper edge weights to promote reliable propagation. When training the base predictor, we concatenate all intermediate features after each propagation step to make the model dynamically learn information of neighbors at different distances. Extensive experiments on five real-world datasets demonstrate that our method achieves superior performance over all baseline methods in terms of node classification accuracy.</abstract>

[PDF](https://openreview.net/pdf?id=rcgRE-Jpl5) &bull;
[Poster](https://openreview.net/attachment?id=rcgRE-Jpl5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=rcgRE-Jpl5)

<div style="text-align:center">
&#10086;
</div>

**Denoising Diffusion Probabilistic Models on SO(3) for Rotational Alignment** <br />
Adam Leach &bull; Sebastian M Schmon &bull; Matteo T. Degiacomi &bull; Chris G. Willcocks<br />
<abstract>Probabilistic diffusion models are capable of modeling complex data distributions on high-dimensional Euclidean spaces for a range applications. However, many real world tasks involve more complex structures such as data distributions defined on manifolds which cannot be easily represented by diffusions on $\mathbb{R}^n$. This paper proposes denoising diffusion models for tasks involving 3D rotations leveraging diffusion processes on the Lie group $SO(3)$ in order to generate candidate solutions to rotational alignment tasks. The experimental results show the proposed $SO(3)$ diffusion process outperforms naïve approaches such as Euler angle diffusion in synthetic rotational distribution sampling and in a 3D object alignment task. </abstract>

[PDF](https://openreview.net/pdf?id=BY88eBbkpe5) &bull;
[Poster](https://openreview.net/attachment?id=BY88eBbkpe5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BY88eBbkpe5)

<div style="text-align:center">
&#10086;
</div>

**Diffusion-Based Methods for Estimating Curvature in Data** <br />
Dhananjay Bhaskar &bull; Kincaid MacDonald &bull; Dawson Thomas &bull; Sarah Zhao &bull; Kisung You &bull; Jennifer Paige &bull; Yariv Aizenbud &bull; Bastian Rieck &bull; Ian M Adelstein &bull; Smita Krishnaswamy<br />
<abstract>High-throughput high-dimensional data is now being generated in massive quantities in many fields including biology, medicine, chemistry, finance, and physics. Researchers have successfully used manifold learning in order to gain insight from such data, particularly in biomedical and single-cell data. One such technique, data diffusion geometry, has been useful in understanding manifold intrinsic distances, density, and major non-linear axes or paths through the data. However, a relatively unstudied feature of high-dimensional data is curvature. While curvature is well-defined and easy to compute in low dimensions, it poses computational and conceptual difficulties in high dimensions. Here, we present two techniques to estimate curvature from high-dimensional data starting from data diffusion probabilities. The first technique, diffusion curvature, uses the spread or conversely laziness of a random walk to estimate curvature pointwise in data. The second technique, deep diffusion curvature, trains a neural network to estimate pointwise curvature. Since these techniques are scalable, we anticipate that they can be used to describe and compare datasets as well as find points in data that represent transitional entities.</abstract>

[PDF](https://openreview.net/pdf?id=HtLfgBbyagq) &bull;
[Poster](https://openreview.net/attachment?id=HtLfgBbyagq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=HtLfgBbyagq)

<div style="text-align:center">
&#10086;
</div>

**Diversified Multiscale Graph Learning with Graph Self-Correction** <br />
Yuzhao Chen &bull; Yatao Bian &bull; Jiying Zhang &bull; Xi Xiao &bull; Tingyang Xu &bull; Yu Rong<br />
<abstract>Though the multiscale graph learning techniques have enabled advanced feature extraction frameworks, we find that the classic ensemble strategy shows inferior performance while encountering the high homogeneity of the learnt representation, which is caused by the nature of existing graph pooling methods. To cope with this issue, we propose a diversified multiscale graph learning model equipped with two core ingredients:  a graph self-correction mechanism to generate informative embedded graphs, and a diversity boosting regularizer to achieve a comprehensive characterization of the input graph. The proposed mechanism compensates the pooled graph with the lost information during the graph pooling process by feeding back the estimated residual graph, which serves as a plug-in component for popular graph pooling methods. Meanwhile, pooling methods enhanced with the self-correcting procedure encourage the discrepancy of node embeddings, and thus it contributes to the success of ensemble learning strategy. The proposed regularizer instead enhances the ensemble diversity at the graph-level embeddings by leveraging the interaction among individual classifiers. Extensive experiments on popular graph classification benchmarks show that the approaches lead to significant improvements over state-of-the-art graph pooling methods, and the ensemble multiscale graph learning models achieve superior enhancement.</abstract>

[PDF](https://openreview.net/pdf?id=S5IEoV-JTg9) &bull;
[Poster](https://openreview.net/attachment?id=S5IEoV-JTg9&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=S5IEoV-JTg9)

<div style="text-align:center">
&#10086;
</div>

**Efficient Representation Learning of Subgraphs by Subgraph-To-Node Translation** <br />
Dongkwan Kim &bull; Alice Oh<br />
<abstract>A subgraph is a data structure that can represent various real-world problems. We propose Subgraph-To-Node (S2N) translation, which is a novel formulation to efficiently learn representations of subgraphs. Specifically, given a set of subgraphs in the global graph, we construct a new graph by coarsely transforming subgraphs into nodes. We perform subgraph-level tasks as node-level tasks through this translation. By doing so, we can significantly reduce the memory and computational costs in both training and inference. We conduct experiments on four real-world datasets to evaluate performance and efficiency. Our experiments demonstrate that models with S2N translation are more efficient than state-of-the-art models without substantial performance decrease.</abstract>

[PDF](https://openreview.net/pdf?id=BgLaE-k6gc) &bull;
[Poster](https://openreview.net/attachment?id=BgLaE-k6gc&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BgLaE-k6gc)

<div style="text-align:center">
&#10086;
</div>

**EquiBind: Geometric Deep Learning for Drug Binding Structure Prediction** <br />
Hannes Stärk &bull; Octavian-Eugen Ganea &bull; Lagnajit Pattanaik &bull; Regina Barzilay &bull; Tommi S. Jaakkola<br />
<abstract>Predicting how a drug-like molecule binds to a specific protein target is a core problem in drug discovery. An extremely fast computational binding method would enable key applications such as fast virtual screening or drug engineering. Existing methods are computationally expensive as they rely on heavy candidate sampling coupled with scoring, ranking, and fine-tuning steps. We challenge this paradigm with EquiBind, an SE(3)-equivariant geometric deep learning model performing direct-shot prediction of both i) the receptor binding location (blind docking) and ii) the ligand's bound pose and orientation. EquiBind achieves significant speed-ups and better quality compared to traditional and recent baselines. Further, we show extra improvements when coupling it with existing fine-tuning techniques at the cost of increased running time. Finally, we propose a novel and fast fine-tuning model that adjusts torsion angles of a ligand's rotatable bonds based on closed-form global minima of the von Mises angular distance to a given input atomic point cloud, avoiding previous expensive differential evolution strategies for energy minimization.</abstract>

[PDF](https://openreview.net/pdf?id=Brxey2E-plq) &bull;
[Poster](https://openreview.net/attachment?id=Brxey2E-plq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=Brxey2E-plq)

<div style="text-align:center">
&#10086;
</div>

**Fiber Bundle Morphisms as a Framework for Modeling Many-to-Many Maps** <br />
Elizabeth Coda &bull; Nico Courts &bull; Colby Wight &bull; Loc Truong &bull; WoongJo Choi &bull; Charles Godfrey &bull; Tegan Emerson &bull; Keerti Kappagantula &bull; Henry Kvinge<br />
<abstract>While it is not generally reflected in the `nice' datasets used for benchmarking machine learning algorithms, the real-world is full of processes that would be best described as many-to-many. That is, a single input can potentially yield many different outputs (whether due to noise, imperfect measurement, or intrinsic stochasticity in the process) and many different inputs can yield the same output (that is, the map is not injective). For example, imagine a sentiment analysis task where, due to linguistic ambiguity, a single statement can have a range of different sentiment interpretations while at the same time many distinct statements can represent the same sentiment. When modeling such a multivalued function $f: X \rightarrow Y$, it is frequently useful to be able to model the distribution on $f(x)$ for specific input $x$ as well as the distribution on fiber $f^{-1}(y)$ for specific output $y$. Such an analysis helps the user (i) better understand the variance intrinsic to the process they are studying and (ii) understand the range of specific input $x$ that can be used to achieve output $y$. Following existing work which used a fiber bundle framework to better model many-to-one processes, we describe how morphisms of fiber bundles provide a template for building models which naturally capture the structure of many-to-many processes.</abstract>

[PDF](https://openreview.net/pdf?id=HcIgi4Zkpe9) &bull;
[Poster](https://openreview.net/attachment?id=HcIgi4Zkpe9&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=HcIgi4Zkpe9)

<div style="text-align:center">
&#10086;
</div>

**Gauge Equivariant Deep Q-Learning on Discrete Manifolds** <br />
Sourya Basu &bull; Pulkit Katdare &bull; Katherine Rose Driggs-Campbell &bull; Lav R. Varshney<br />
<abstract>Data, at any point on a manifold, can be represented on the tangent plane at that point with respect to a basis, called a gauge. But the choice of gauge is not unique for arbitrary manifolds. Hence, for agents traversing an environment embedded on a manifold, the same environment may appear differently if the choice of gauge changes or when moving to a different point that has a different gauge. This may be deleterious to an agent's learning, as compared to learning on, say, a flat grid where it is easy to choose a fixed gauge for each point. To this end, we provide a formulation of deep Q-learning that learns policies (and Q-values) that are equivariant (invariant) to changes in choice of gauge. This leads to an efficient learning algorithm independent of the choice of gauge. Our experimental results demonstrate significant improvement in learning on novel environments embedded in arbitrary manifolds such as spheres, hills, and urns, compared to naive approaches.</abstract>

[PDF](https://openreview.net/pdf?id=SY8LRVbJag5) &bull;
[Poster](https://openreview.net/attachment?id=SY8LRVbJag5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=SY8LRVbJag5)

<div style="text-align:center">
&#10086;
</div>

**Graph Anisotropic Diffusion** <br />
Ahmed A. A. Elhag &bull; Gabriele Corso &bull; Hannes Stärk &bull; Michael M. Bronstein<br />
<abstract>Traditional Graph Neural Networks (GNNs) rely on message passing, which amounts to permutation-invariant local aggregation of neighbour features. Such a process is isotropic and there is no notion of `direction' on the graph. We present a new GNN architecture called Graph Anisotropic Diffusion. Our model alternates between linear diffusion, for which a closed-form solution is available, and local anisotropic filters to obtain efficient multi-hop anisotropic kernels. We test our model on two common molecular property prediction benchmarks (ZINC and QM9) and show its competitive performance.</abstract>

[PDF](https://openreview.net/pdf?id=S9fkSb1pg5) &bull;
[Poster](https://openreview.net/attachment?id=S9fkSb1pg5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=S9fkSb1pg5)

<div style="text-align:center">
&#10086;
</div>

**Graph Neural Networks are Dynamic Programmers** <br />
Andrew Dudzik &bull; Petar Veličković<br />
<abstract>Recent advances in neural algorithmic reasoning with graph neural networks (GNNs) are propped up by the notion of algorithmic alignment. Broadly, a neural network will be better at learning to execute a reasoning task (in terms of sample complexity) if its individual components align well with the target algorithm. Specifically, GNNs are claimed to align with dynamic programming (DP), a general problem-solving strategy which expresses many polynomial-time algorithms. However, has this alignment truly been demonstrated and theoretically quantified? Here we show, using methods from category theory and abstract algebra, that there exists an intricate connection between GNNs and DP, going well beyond the initial observations over individual algorithms such as Bellman-Ford. Exposing this connection, we easily verify several prior findings in the literature, and hope it will serve as a foundation for building stronger algorithmically aligned GNNs.</abstract>

[PDF](https://openreview.net/pdf?id=rebfkS-yTx9) &bull;
[Poster](https://openreview.net/attachment?id=rebfkS-yTx9&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=rebfkS-yTx9)

<div style="text-align:center">
&#10086;
</div>

**Group Symmetry in PAC Learning** (Spotlight presentation)<br />
Bryn Elesedy<br />
<abstract>In this paper we show rigorously how learning in the PAC framework with invariant or equivariant hypotheses reduces to learning in a space of orbit representatives. Our results hold for any compact group, including infinite groups such as rotations. In addition, we show how to use these equivalences to derive generalisation bounds for invariant/equivariant models in terms of the geometry of the input and output spaces. To the best of our knowledge, our results are the most general of their kind to date.</abstract>

[PDF](https://openreview.net/pdf?id=HxeTEZJaxq) &bull;
[Poster](https://openreview.net/attachment?id=HxeTEZJaxq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=HxeTEZJaxq)

<div style="text-align:center">
&#10086;
</div>

**Heterogeneous manifolds for curvature-aware graph embedding** <br />
Francesco Di Giovanni &bull; Giulia Luise &bull; Michael M. Bronstein<br />
<abstract>The quality of graph embeddings depends on whether the geometry of the space matches that of the graph. Euclidean spaces are often a poor choice and recently hyperbolic spaces and more general manifolds, such as products of constant-curvature spaces and matrix manifolds, have resulted advantageous to better matching nodes pairwise distances. However, all these manifolds are homogeneous, implying that the curvature distribution is the same at each point, making them unsuited to match the local curvature (and related structural properties) of the graph. We study embeddings in a broader class of heterogeneous rotationally-symmetric manifolds. By adding a single radial dimension to existing homogeneous models, we can both account for heterogeneous curvature distributions on graphs and pairwise distances. We evaluate our approach on reconstruction tasks.</abstract>

[PDF](https://openreview.net/pdf?id=rtUxsN-kaxc) &bull;
[Forum](https://openreview.net/forum?id=rtUxsN-kaxc)

<div style="text-align:center">
&#10086;
</div>

**HIGH SKIP NETWORKS: A HIGHER ORDER GENERALIZATION OF SKIP CONNECTIONS** <br />
Mustafa Hajij &bull; Karthikeyan Natesan Ramamurthy &bull; Aldo Guzmán-Sáenz &bull; Ghada Za<br />
<abstract>We present High Skip Networks (HSNs), a higher order generalization of skip connection neural networks to simplicial complexes. HSNs exploit higher order structure encoded in a simplicial domain by creating multiple feed-forward paths of signals computed over the input complex. Some feed-forward paths may propagate the signal through various higher order structures; e.g., if we want to propagate signals over edges, some feed-forward paths may go from edges to triangles and then back to edges. Similar to the Euclidean skip connection networks, all paths are combined together at the end by addition or concatenation. We demonstrate the effectiveness of HSNs on synthetic and real datasets. Our preliminary results show that HSNs lead to a statistically significant improvement in the generalization error when compared to base models without high skip components.</abstract>

[PDF](https://openreview.net/pdf?id=Sc8glB-k6e9) &bull;
[Forum](https://openreview.net/forum?id=Sc8glB-k6e9)

<div style="text-align:center">
&#10086;
</div>

**Learning Weighted Product Spaces Representations for Graphs of Heterogeneous Structures** <br />
Tuc Van Nguyen &bull; Dung D. Le &bull; Anh Ta<br />
<abstract>In representation learning, it is important to learn embedding spaces whose geometry matches the underlying structure of the data. In the literature, an active research direction aims at using product spaces, which consists of Euclidean and non-Euclidean manifolds to represent data of varying curvatures. However, real-world data is usually heterogeneous and consists of a mixture of varying structures, requiring the representation learning process to flexibly select and combine the member spaces accordingly. Since previous works only consider combination of embedding spaces with equal weights, in this paper, we propose a data-driven method to learn the embeddings  in a weighted product spaces for graph data. Specifically, our model utilizes the topological information of input graph to learn the weight for each component of the product spaces. Experiments on synthetic and real-world datasets show that our models produce better representations in terms of distortion measures, and perform better on tasks such as word similarity learning.</abstract>

[PDF](https://openreview.net/pdf?id=BebMTEby6x9) &bull;
[Poster](https://openreview.net/attachment?id=BebMTEby6x9&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BebMTEby6x9)

<div style="text-align:center">
&#10086;
</div>

**Manifold-aligned Neighbor Embedding** <br />
Mohammad Tariqul Islam &bull; Jason W. Fleischer<br />
<abstract>In this paper, we introduce a neighbor embedding framework for manifold alignment. We demonstrate the efficacy of the framework using a manifold-aligned version of the uniform manifold approximation and projection algorithm. We show that our algorithm can learn an aligned manifold that is visually competitive to embedding of the whole dataset.</abstract>

[PDF](https://openreview.net/pdf?id=BFIER4-J6xc) &bull;
[Forum](https://openreview.net/forum?id=BFIER4-J6xc)

<div style="text-align:center">
&#10086;
</div>

**Message passing all the way up** (Spotlight presentation)<br />
Petar Veličković<br />
<abstract>The message passing framework is the foundation of the immense success enjoyed by graph neural networks (GNNs) in recent years. In spite of its elegance, there exist many problems it provably cannot solve over given input graphs. This has led to a surge of research on going beyond message passing, building GNNs which do not suffer from those limitations---a term which has become ubiquitous in regular discourse. However, have those methods truly moved beyond message passing? In this position paper, I argue about the dangers of using this term---especially when teaching graph representation learning to newcomers. I show that any function of interest we want to compute over graphs can, in all likelihood, be expressed using pairwise message passing -- just over a potentially modified graph, and argue how most practical implementations subtly do this kind of trick anyway. Hoping to initiate a productive discussion, I propose replacing beyond message passing with a more tame term, augmented message passing.</abstract>

[PDF](https://openreview.net/pdf?id=Bc8GiEZkTe5) &bull;
[Poster](https://openreview.net/attachment?id=Bc8GiEZkTe5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=Bc8GiEZkTe5)

<div style="text-align:center">
&#10086;
</div>

**Message Passing Neural Processes** <br />
Cătălina Cangea &bull; Ben Day &bull; Arian Rokkum Jamasb &bull; Pietro Lio<br />
<abstract>Neural Processes (NPs) are powerful and flexible models able to incorporate uncertainty when representing stochastic processes, while maintaining a linear time complexity. However, NPs produce a latent description by aggregating independent representations of context points and lack the ability to exploit relational information present in many datasets. This renders NPs ineffective in settings where the stochastic process is primarily governed by neighbourhood rules, such as cellular automata (CA), and limits performance for any task where relational information remains unused. We address this shortcoming by introducing Message Passing Neural Processes (MPNPs), the first class of NPs that explicitly makes use of relational structure within the model. Our evaluation shows that MPNPs thrive at lower sampling rates, on existing benchmarks and newly-proposed CA and Cora-Branched tasks. We further report strong generalisation over density-based CA rule-sets and significant gains in challenging arbitrary-labelling and few-shot learning setups.</abstract>

[PDF](https://openreview.net/pdf?id=r5VkH-Jax9) &bull;
[Poster](https://openreview.net/attachment?id=r5VkH-Jax9&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=r5VkH-Jax9)

<div style="text-align:center">
&#10086;
</div>

**Multi-scale Physical Representations for Approximating PDE Solutions with Graph Neural Operators** <br />
Léon Migus &bull; Yuan Yin &bull; Jocelyn Ahmed Mazari &bull; patrick gallinari<br />
<abstract>Representing physical signals at different scales is among the most challenging problems in engineering. Several multi-scale modeling tools have been developed to describe physical systems governed by Partial Differential Equations (PDEs). These tools are at the crossroad of principled physical models and numerical schema. Recently, data-driven models have been introduced to speed-up the approximation of PDE solutions compared to numerical solvers. Among these recent data-driven methods, neural integral operators are a class that learn a mapping between function spaces. These functions are discretized on graphs (meshes) which are appropriate for modeling interactions in physical phenomena. In this work, we study three multi-resolution schema with integral kernel operators that can be approximated with Message Passing Graph Neural Networks (MPGNNs). To validate our study, we make extensive MPGNNs experiments with well-chosen metrics considering steady and unsteady PDEs. Code: https://github.com/LeonMigu/multi_scale_graph_neural_operator</abstract>

[PDF](https://openreview.net/pdf?id=rx9TVZJax5) &bull;
[Poster](https://openreview.net/attachment?id=rx9TVZJax5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=rx9TVZJax5)

<div style="text-align:center">
&#10086;
</div>

**Neural Approximation of Extended Persistent Homology on Graphs** (Spotlight presentation)<br />
Zuoyu Yan &bull; Tengfei Ma &bull; Liangcai Gao &bull; Zhi Tang &bull; Yusu Wang &bull; Chao Chen<br />
<abstract>Persistent homology is a widely used theory in topological data analysis. In the context of graph learning, topological features based on persistent homology have been used to capture potentially high-order structural information so as to augment existing graph neural network methods. However, computing extended persistent homology summaries remains slow for large and dense graphs. Inspired by recent success in neural algorithmic reasoning, we propose a novel learning method to compute extended persistence diagrams on graphs. The proposed neural network aims to simulate a specific algorithm and learns to compute extended persistence diagrams for new graphs efficiently. Experiments on approximating extended persistence diagrams and several downstream graph representation learning tasks demonstrate the effectiveness of our method. Our method is also efficient; on large and dense graphs, we accelerate the computation by nearly 100 times.</abstract>

[PDF](https://openreview.net/pdf?id=H9xJHbJ6e5) &bull;
[Poster](https://openreview.net/attachment?id=H9xJHbJ6e5&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=H9xJHbJ6e5)

<div style="text-align:center">
&#10086;
</div>

**Neural Sheaf Diffusion:  A Topological Perspective on Heterophily and Oversmoothing in GNNs** (Spotlight presentation)<br />
Cristian Bodnar &bull; Francesco Di Giovanni &bull; Benjamin Paul Chamberlain &bull; Pietro Lio &bull; Michael M. Bronstein<br />
<abstract>Cellular sheaves equip graphs with ``geometrical'' structure by assigning vector spaces and linear maps to nodes and edges. Graph Neural Networks (GNNs) implicitly assume a graph with a trivial underlying sheaf. This choice is reflected in the structure of the graph Laplacian operator, the properties of the associated diffusion equation, and the characteristics of the convolutional models that discretise this equation. In this paper, we use cellular sheaf theory to show that the underlying geometry of the graph is deeply linked with the performance of GNNs in heterophilic settings and their oversmoothing behaviour. By considering a hierarchy of increasingly general sheaves, we study how the ability of the sheaf diffusion process to achieve linear separation of the classes in the infinite time limit expands. At the same time, we prove that when the sheaf is non-trivial, discretised parametric diffusion processes have greater control than GNNs over their asymptotic behaviour. On the practical side, we study how sheaves can be learned from data. The resulting sheaf diffusion models have many desirable properties that address the limitations of classical graph diffusion equations (and corresponding GNN models) and obtain state-of-the-art results in heterophilic settings. Overall, our work provides new connections between GNNs and algebraic topology and would be of interest to both fields.</abstract>

[PDF](https://openreview.net/pdf?id=HtLzqEb1aec) &bull;
[Poster](https://openreview.net/attachment?id=HtLzqEb1aec&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=HtLzqEb1aec)

<div style="text-align:center">
&#10086;
</div>

**ON RECOVERABILITY OF GRAPH NEURAL NETWORK REPRESENTATIONS** <br />
Maxim Fishman &bull; Chaim Baskin &bull; Evgenii Zheltonozhskii &bull; Ron Banner &bull; Avi Mendelson<br />
<abstract>Despite their growing popularity, graph neural networks (GNNs) still have multiple unsolved problems, 
including finding more expressive aggregation methods, propagation of information to distant nodes, and training on large-scale graphs.
Understanding and solving such problems require developing analytic tools and techniques.
In this work, we propose the notion of \textit{recoverability}, which is tightly related to information aggregation in GNNs,
and based on this concept, develop the method for GNN embedding analysis.
Through extensive experimental results on various datasets and different GNN architectures, 
we demonstrate that estimated recoverability correlates with aggregation method expressivity and graph sparsification quality.
The code to reproduce our experiments is available at \url{https://github.com/Anonymous1252022/Recoverability}.</abstract>

[PDF](https://openreview.net/pdf?id=BcU49V-1pec) &bull;
[Forum](https://openreview.net/forum?id=BcU49V-1pec)

<div style="text-align:center">
&#10086;
</div>

**On subsampling and inference for multiparameter persistence homology** <br />
Vinoth Nandakumar<br />
<abstract>In topological data analysis, multi-parameter persistence homology is a framework for extracting topological information for point cloud datasets equipped with multiple filtrations. However, existing algorithms become computationally expensive for large datasets, limiting their applicability. In the single-parameter case, subsampling algorithms have been used to reduce the time complexity of computing persistence homology. Convergence properties of the persistence barcodes have also been established in this setting. We extend these results to the multiparameter persistence homology, and develop subsampling algorithms can be used to approximate the fibered barcode in this setting. We conduct experiments on the point cloud dataset ModelNet to demonstrate the efficiency of these algorithms.</abstract>

[PDF](https://openreview.net/pdf?id=BxNa4-JTgc) &bull;
[Poster](https://openreview.net/attachment?id=BxNa4-JTgc&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BxNa4-JTgc)

<div style="text-align:center">
&#10086;
</div>

**On the Inadequacy of CKA as a Measure of Similarity in Deep Learning** <br />
MohammadReza Davari &bull; Stefan Horoi &bull; Amine Natik &bull; Guillaume Lajoie &bull; Guy Wolf &bull; Eugene Belilovsky<br />
<abstract>Comparing learned representations is a challenging problem which has been approached in different ways. The CKA similarity metric, particularly it's linear variant, has recently become a popular approach and has been widely used to compare representations of a network's different layers, of similar networks trained differently, or of models with different architectures trained on the same data. CKA results have been used to make a wide variety of claims about similarity and dissimilarity of these various representations. In this work we investigate several weaknesses of the CKA similarity metric, demonstrating situations in which it gives unexpected or counterintuitive results. We then study approaches for modifying representations to maintain functional behaviour while changing the CKA value. Indeed we illustrate in some cases the CKA value can be heavily manipulated without substantial changes to the functional behaviour.</abstract>

[PDF](https://openreview.net/pdf?id=rK841rby6xc) &bull;
[Poster](https://openreview.net/attachment?id=rK841rby6xc&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=rK841rby6xc)

<div style="text-align:center">
&#10086;
</div>

**Persistent Tor-algebra based stacking ensemble learning (PTA-SEL) for protein-protein binding affinity prediction** <br />
Xiang LIU &bull; KELIN XIA<br />
<abstract>Protein-protein interactions (PPIs) play crucial roles in almost all biological processes. Recently, Data-driven machine learning models have shown great power in the analysis of PPIs. However, efficient molecular representation and featurization are still key issues that hinder the performance of learning models. Here, we propose persistent Tor-algebra (PTA), PTA-based molecular characterization and featurization, and PTA-based stacking ensemble learning (PTA-SEL) for PPI binding affinity prediction, for the first time. More specifically, the Vietoris-Rips
complex is used to characterize the PPI structure and its persistent Tor-algebra is computed to form the molecular descriptors. These descriptors then are fed into our stacking model to make the prediction. We systematically test our model on the two most commonly used datasets, i.e., SKEMPI and AB-Bind. It has been found that our model outperforms all the existing models as far as we know, which demonstrates the great power of our model.</abstract>

[PDF](https://openreview.net/pdf?id=rl79N-1alq) &bull;
[Poster](https://openreview.net/attachment?id=rl79N-1alq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=rl79N-1alq)

<div style="text-align:center">
&#10086;
</div>

**Pre-training Molecular Graph Representation with 3D Geometry** (Spotlight presentation)<br />
Shengchao Liu &bull; Hanchen Wang &bull; Weiyang Liu &bull; Joan Lasenby &bull; Hongyu Guo &bull; Jian Tang<br />
<abstract>Molecular graph representation learning is a fundamental problem in modern drug and material discovery. Molecular graphs are typically modeled by their 2D topological structures, but it has been recently discovered that 3D geometric information plays a more vital role in predicting molecular functionalities. However, the lack of 3D information in real-world scenarios has significantly impeded the learning of geometric graph representation. To cope with this challenge, we propose the Graph Multi-View Pre-training (GraphMVP) framework where self-supervised learning (SSL) is performed by leveraging the correspondence and consistency between 2D topological structures and 3D geometric views. GraphMVP effectively learns a 2D molecular graph encoder that is enhanced by richer and more discriminative 3D geometry. We further provide theoretical insights to justify the effectiveness of GraphMVP. Finally, comprehensive experiments show that GraphMVP can consistently outperform existing graph SSL methods.</abstract>

[PDF](https://openreview.net/pdf?id=rt8MCNW1pe5) &bull;
[Forum](https://openreview.net/forum?id=rt8MCNW1pe5)

<div style="text-align:center">
&#10086;
</div>

**Random Filters for Enriching the Discriminatory Power of Topological Representations** <br />
Tegan Emerson &bull; Grayson Jorgenson &bull; Henry Kvinge &bull; Colin Olson<br />
<abstract>Topological representations of data are inherently coarse summaries which endows them with certain desirable properties like stability but also potentially inhibits their discriminatory power relative to fine-scale learned features. In this work we present a novel framework for enriching the discriminatory power of topological representations based on random filters and capturing “interference topology” rather than direct topology. We show that our random filters outperform previously explored structured image filters while requiring orders of magnitude
less computational time. The approach is demonstrated on the MNIST dataset but is broadly applicable across data sets and modalities. This work is concluded with a discussion of the mathematical intuition underlying the approach and identification of future directions to enable deeper understanding and theoretical results.</abstract>

[PDF](https://openreview.net/pdf?id=BcLe3E-kpxq) &bull;
[Poster](https://openreview.net/attachment?id=BcLe3E-kpxq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BcLe3E-kpxq)

<div style="text-align:center">
&#10086;
</div>

**Reducing Learning on Cell Complexes to Graphs** <br />
Fabian Jogl &bull; Maximilian Thiessen &bull; Thomas Gärtner<br />
<abstract>Message passing graph neural networks (GNNs) are known to have a limited expressiveness in distinguishing graphs. A recent approach tackles this problem by transforming graphs to regular cell complexes. This makes it possible to model higher-order structures and yields algorithms that are more powerful than the Weisfeiler Leman test (WL) or GNNs. However, this approach cannot easily be combined with previous graph algorithms and implementations due to their fundamental differences. We develop Cell Encoding, a novel approach of transforming regular cell complexes to graphs. We show that cell encoding combined with WL or a suitably expressive GNN is at least as expressive as Cellular Weisfeiler Leman (CWL) in distinguishing cell complexes. This means that with a simple preprocessing one can use any GNN for learning tasks on cell complexes. Additionally, we show that this approach can make GNNs more expressive and give better results on graph classification datasets.</abstract>

[PDF](https://openreview.net/pdf?id=HKUxAE-J6lq) &bull;
[Poster](https://openreview.net/attachment?id=HKUxAE-J6lq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=HKUxAE-J6lq)

<div style="text-align:center">
&#10086;
</div>

**REMuS-GNN: A Rotation-Equivariant Model for Simulating Continuum Dynamics** <br />
Mario Lino Valencia &bull; Stathi Fotiadis &bull; Anil Anthony Bharath &bull; Chris D Cantwell<br />
<abstract>Numerical simulation is an essential tool in many areas of science and engineering, but its performance often limits application in practice, or when used to explore large parameter spaces. On the other hand, surrogate deep learning models, while accelerating simulations, often exhibit poor accuracy and ability to generalise. In order to improve these two factors, we introduce REMuS-GNN, a rotation-equivariant multi-scale model for simulating continuum dynamical systems encompassing a range of length scales. REMuS-GNN is designed to predict an output vector field from an input vector field on a physical domain discredited into an unstructured set of nodes. Equivariance to rotations of the domain is a desirable inductive bias that allows the network to learn the underlying physics more efficiently, leading to improved accuracy and generalisation compared with similar architectures that lack such symmetry. We demonstrate and evaluate this method on the incompressible flow around elliptical cylinders.</abstract>

[PDF](https://openreview.net/pdf?id=SYLzn4Z16ec) &bull;
[Forum](https://openreview.net/forum?id=SYLzn4Z16ec)

<div style="text-align:center">
&#10086;
</div>

**Riemannian Neural SDE: Learning Stochastic Representations on Manifolds** <br />
Sung Woo Park &bull; Hyomin Kim &bull; Hyeseong Kim &bull; Junseok Kwon<br />
<abstract>In recent years, the neural stochastic differential equation (NSDE) has gained attention in modeling stochastic representations, while NSDE brings a great success in various types of applications. However, it typically loses the expressivity when the data representation is manifold-valued. To overcome such an issue, we suggest a principled way to express the stochastic representation with the Riemannian neural SDE (RNSDE), which extends the conventional Euclidean NSDE. Empirical results on the density estimation on manifolds show that the proposed method significantly outperforms baseline methods.</abstract>

[PDF](https://openreview.net/pdf?id=SF8lkH-J6e9) &bull;
[Poster](https://openreview.net/attachment?id=SF8lkH-J6e9&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=SF8lkH-J6e9)

<div style="text-align:center">
&#10086;
</div>

**RipsNet: a general architecture for fast and robust estimation of the persistent homology of point clouds** (Spotlight presentation)<br />
Thibault de Surrel &bull; Felix Hensel &bull; Mathieu Carrière &bull; Théo Lacombe &bull; Yuichi Ike &bull; Hiroaki Kurihara &bull; Marc Glisse &bull; Frederic Chazal<br />
<abstract>The use of topological descriptors in modern machine learning applications, such as Persistence Diagrams (PDs) arising from Topological Data Analysis (TDA), has shown great potential in various domains.
However, their practical use in applications is often hindered by two major limitations: the computational complexity required to compute such descriptors exactly, and their sensitivity to even low-level proportions of outliers. In this work, we propose to bypass these two burdens in a data-driven setting by entrusting the estimation of (vectorization of) PDs built on top of point clouds to a neural network architecture that we call RipsNet. Once trained on a given data set, RipsNet can estimate topological descriptors on test data very efficiently with generalization capacity. Furthermore, we prove that RipsNet is robust to input perturbations in terms of the 1-Wasserstein distance, a major improvement over the standard computation of PDs that only enjoys Hausdorff stability, yielding RipsNet to substantially outperform exactly-computed PDs in noisy settings. We showcase the use of RipsNet on both synthetic and real-world data. Our implementation will be made freely and publicly available as part of an open-source library.</abstract>

[PDF](https://openreview.net/pdf?id=SeZlCN-ypgq) &bull;
[Poster](https://openreview.net/attachment?id=SeZlCN-ypgq&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=SeZlCN-ypgq)

<div style="text-align:center">
&#10086;
</div>

**Sign and Basis Invariant Networks for Spectral Graph Representation Learning** <br />
Derek Lim &bull; Joshua David Robinson &bull; Lingxiao Zhao &bull; Tess Smidt &bull; Suvrit Sra &bull; Haggai Maron &bull; Stefanie Jegelka<br />
<abstract>Many machine learning tasks involve processing eigenvectors derived from data. Especially valuable are Laplacian eigenvectors, which capture useful structural information about graphs and other geometric objects. However, ambiguities arise when computing eigenvectors: for each eigenvector v, the sign flipped -v is also an eigenvector. More generally, higher dimensional eigenspaces contain infinitely many choices of eigenvector bases. In this work we introduce SignNet and BasisNet --- new neural architectures that are invariant to all requisite symmetries and hence process collections of eigenspaces in a principled manner. Our networks are universal, i.e., they can approximate any continuous function of eigenvectors with the proper invariances. They are also theoretically strong for graph representation learning --- they can provably approximate any spectral graph convolution,  spectral invariants that go beyond message passing neural networks, and other graph positional encodings. Experiments show the strength of our networks for learning spectral graph filters and learning graph positional encodings.</abstract>

[PDF](https://openreview.net/pdf?id=BlM64by6gc) &bull;
[Poster](https://openreview.net/attachment?id=BlM64by6gc&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=BlM64by6gc)

<div style="text-align:center">
&#10086;
</div>

**Simplicial Attention Networks** <br />
Christopher Wei Jin Goh &bull; Cristian Bodnar &bull; Pietro Lio<br />
<abstract>Graph representation learning methods have mostly been limited to the modelling of node-wise interactions. Recently, there has been an increased interest in understanding how higher-order structures can be utilised to further enhance the learning abilities of graph neural networks (GNNs) in combinatorial spaces. Simplicial Neural Networks (SNNs) naturally model these interactions by performing message passing on simplicial complexes, higher-dimensional generalisations of graphs. Nonetheless, the computations performed by most existent SNNs are strictly tied to the combinatorial structure of the complex. Leveraging the success of attention mechanisms in structured domains, we propose Simplicial Attention Networks (SAT), a new type of simplicial network that dynamically weighs the interactions between neighbouring simplicies and can readily adapt to novel structures. Additionally, we propose a signed attention mechanism that makes SAT orientation equivariant, a desirable property for models operating on (co)chain complexes. We demonstrate that SAT outperforms existent convolutional SNNs and GNNs in two image and trajectory classification tasks.  </abstract>

[PDF](https://openreview.net/pdf?id=ScfRNWkpec) &bull;
[Poster](https://openreview.net/attachment?id=ScfRNWkpec&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=ScfRNWkpec)

<div style="text-align:center">
&#10086;
</div>

**Sparsifying the Update Step in Graph Neural Networks** <br />
Johannes F. Lutzeyer &bull; changmin wu &bull; Michalis Vazirgiannis<br />
<abstract>Message-Passing Neural Networks (MPNNs), the most prominent Graph Neural Network (GNN) framework, celebrate much success in the analysis of graph-structured data. Concurrently, the sparsification of Neural Network models attracts a great amount of academic and industrial interest. In this paper we conduct a structured, empirical study of the effect of sparsification on the trainable part of MPNNs known as the Update step. To this end, we design a series of models to successively sparsify the linear transform in the Update step. Specifically, we propose the ExpanderGNN model with a tuneable sparsification rate and the Activation-Only GNN, which has no linear transform in the Update step. In agreement with a growing trend in the literature the sparsification paradigm is changed by initialising sparse neural network architectures rather than expensively sparsifying already trained architectures. Our novel benchmark models enable a better understanding of the influence of the Update step on model performance and outperform existing simplified benchmark models such as the Simple Graph Convolution. The ExpanderGNNs, and in some cases the Activation-Only models, achieve performance on par with their vanilla counterparts on several downstream tasks, while containing significantly fewer trainable parameters. Our code is publicly available at: https://github.com/ChangminWu/ExpanderGNN.</abstract>

[PDF](https://openreview.net/pdf?id=Bxx34b1agc) &bull;
[Poster](https://openreview.net/attachment?id=Bxx34b1agc&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=Bxx34b1agc)

<div style="text-align:center">
&#10086;
</div>

**SpeqNets: Sparsity-aware Permutation-equivariant Graph Networks** <br />
Christopher Morris &bull; Gaurav Rattan &bull; Sandra Kiefer &bull; Siamak Ravanbakhsh<br />
<abstract>While graph neural networks have clear limitations in approximating permutation-equivariant functions over graphs, more expressive, higher-order graph neural networks do not scale to large graphs. By introducing new heuristics for the graph isomorphism problem, we devise a class of universal, permutation-equivariant graph networks, which offers a fine-grained control between expressivity and scalability and adapt to the sparsity of the graph. These architectures lead to vastly reduced computation times compared to standard higher-order graph networks while significantly improving over standard graph neural network and graph kernel architectures in terms of predictive performance.</abstract>

[PDF](https://openreview.net/pdf?id=rc8x9VZJpe5) &bull;
[Forum](https://openreview.net/forum?id=rc8x9VZJpe5)

<div style="text-align:center">
&#10086;
</div>

**TopTemp: Parsing Precipitate Structure from Temper Topology** (Spotlight presentation)<br />
Tegan Emerson &bull; Lara Kassab &bull; Scott Howland &bull; Henry Kvinge &bull; Keerti Sahithi Kappagantula<br />
<abstract>Technological advances are in part enabled by the development of novel manufacturing processes that give rise to new materials or material property improvements. Development and evaluation of new manufacturing methodologies is labor-, time-, and resource-intensive expensive due to complex, poorly defined relationships between advanced manufacturing process parameters and the resulting microstructures. In this work, we present a topological representation of temper (heat-treatment) dependent material micro-structure, as captured by scanning electron microscopy, called TopTemp. We show that this topological representation is able to support temper classification of microstructures in a data limited setting, generalizes well to previously unseen samples, is robust to image perturbations, and captures domain interpretable features. The presented work outperforms conventional deep learning baselines and is a first step towards improving understanding of process parameters and resulting material properties.</abstract>

[PDF](https://openreview.net/pdf?id=Bq8z34ZkTlc) &bull;
[Poster](https://openreview.net/attachment?id=Bq8z34ZkTlc&name=Poster) &bull;
[Forum](https://openreview.net/forum?id=Bq8z34ZkTlc)

<div style="text-align:center">
&#10086;
</div>

**Two-dimensional visualization of large document libraries using t-SNE** <br />
Rita González-Márquez &bull; Philipp Berens &bull; Dmitry Kobak<br />
<abstract>We benchmarked different approaches for creating 2D visualizations of large document libraries, using the MEDLINE (PubMed) database of the entire biomedical literature as a use case (19 million scientific papers). Our optimal pipeline is based on log-scaled TF-IDF representation of the abstract text, SVD preprocessing, and t-SNE with uniform affinities, early exaggeration annealing, and extended optimization. The resulting embedding distorts local neighborhoods but shows meaningful organization and rich structure on the level of narrow academic fields.</abstract>

[PDF](https://openreview.net/pdf?id=Hebl3EZ16lq) &bull;
[Forum](https://openreview.net/forum?id=Hebl3EZ16lq)

<div style="text-align:center">
&#10086;
</div>

**WEISFEILER AND LEMAN GO INFINITE: SPECTRAL AND COMBINATORIAL PRE-COLORINGS** <br />
Or Feldman &bull; Amit Boyarski &bull; Shai Feldman &bull; Dani Kogan &bull; Avi Mendelson &bull; Chaim Baskin<br />
<abstract> Two popular alternatives for graph isomorphism testing that offer a good trade-off between expressive power and computational efficiency are combinatorial (i.e., obtained via the Weisfeiler-Leman (WL) test) and spectral invariants. While the exact power of the latter is still an open question, the former is regularly criticized for its limited power, when a standard configuration of uniform pre-coloring is used. This drawback hinders the applicability of Message Passing Graph Neural Networks (MPGNNs), whose expressive power is upper bounded by the WL test. Relaxing the assumption of uniform pre-coloring, we show that one can increase the expressive power of the WL test ad infinitum. Following that, we propose an efficient pre-coloring based on spectral features that provably increase the expressive power of the vanilla WL test.
The code to reproduce our experiments is available at \url{https://github.com/TPFI22/Spectral-and-Combinatorial}</abstract>

[PDF](https://openreview.net/pdf?id=H9IG5Eby6lc) &bull;
[Forum](https://openreview.net/forum?id=H9IG5Eby6lc)
