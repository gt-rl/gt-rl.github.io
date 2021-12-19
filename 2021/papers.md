---
layout: default
navigation: "2021"
---

# Accepted Papers

This is the list of all accepted papers. You can find more information
about each submission by following either the *Forum* link or by visiting
the [OpenReview Workshop Website](https://openreview.net/group?id=ICLR.cc/2021/Workshop/GTRL).

# Statistics

We received 39 submissions, of which we accepted 5 spotlight
presentations and 22 posters.

# Spotlight Presentations

**Directional Graph Networks** (Spotlight presentation)<br />
Dominique Beaini &bull; Saro Passaro &bull; Vincent Létourneau &bull; William L. Hamilton &bull; Gabriele Corso &bull; Pietro Liò<br />
<abstract>The lack of anisotropic kernels in graph neural networks (GNNs) strongly limits their expressiveness, contributing to well-known issues such as over-smoothing. To overcome this limitation, we propose the first globally consistent anisotropic kernels for GNNs, allowing for graph convolutions that are defined according to topologicaly-derived directional flows.
First, by defining a vector field in the graph, we develop a method of applying directional derivatives and smoothing by projecting node-specific messages into the field. 
Then, we propose the use of the Laplacian eigenvectors as such vector field.
We show that the method generalizes CNNs on an $n$-dimensional grid and is provably more discriminative than standard GNNs regarding the Weisfeiler-Lehman 1-WL test.
We evaluate our method on different standard benchmarks and see a relative error reduction of 8% on the CIFAR10 graph dataset and 11% to 32% on the molecular ZINC dataset, and a relative increase in precision of 1.6% on the MolPCBA dataset. 
An important outcome of this work is that it enables graph networks to embed directions in an unsupervised way, thus allowing a better representation of the anisotropic features in different physical or biological problems. </abstract>

[PDF](https://openreview.net/pdf?id=cH3lcayWoCm) &bull;
[Forum](https://openreview.net/forum?id=cH3lcayWoCm)

<div style="text-align:center">
&#10086;
</div>

**Don't stack layers in graph neural networks, wire them randomly** (Spotlight presentation)<br />
Diego Valsesia &bull; Giulia Fracastoro &bull; Enrico Magli<br />
<abstract>Several results suggest an inherent difficulty of graph neural networks in extracting better performance by increasing the number of layers. Recent works attribute this to a phenomenon peculiar to the extraction of node features in graph-based tasks, i.e., the need to consider multiple neighborhood sizes at the same time and adaptively tune them. In this paper, we investigate the recently proposed randomly wired architectures in the context of graph neural networks. Instead of building deeper networks by stacking many layers, we prove that employing a randomly-wired architecture can be a more effective way to increase the capacity of the network and obtain richer representations. We show that such architectures behave like an ensemble of paths, which are able to merge contributions from receptive fields of varied size. Moreover, these receptive fields can also be modulated to be wider or narrower through the trainable weights over the paths.</abstract>

[PDF](https://openreview.net/pdf?id=xFH_wIFy1Je) &bull;
[Forum](https://openreview.net/forum?id=xFH_wIFy1Je)

<div style="text-align:center">
&#10086;
</div>

**Geometry encoding for numerical simulations** (Spotlight presentation)<br />
Amir Maleki &bull; Jan Heyse &bull; Rishikesh Ranade &bull; Haiyang He &bull; Priya Kasimbeg &bull; Jay Pathak<br />
<abstract>We present a notion of geometry encoding suitable for machine learning-based numerical simulation. In particular, we delineate how this notion of encoding is different than other encoding algorithms commonly used in other disciplines such as computer vision and computer graphics. We also present a model comprised of multiple neural networks including a processor, a compressor and an evaluator. These parts each satisfy a particular requirement of our encoding. We compare our encoding model with the analogous models in the literature.</abstract>

[PDF](https://openreview.net/pdf?id=ONnNXBPg41h) &bull;
[Forum](https://openreview.net/forum?id=ONnNXBPg41h)

<div style="text-align:center">
&#10086;
</div>

**On Linear Interpolation in the Latent Space of Deep Generative Models** (Spotlight presentation)<br />
Mike Yan Michelis &bull; Quentin Becker<br />
<abstract>The underlying geometrical structure of the latent space in deep generative models is in most cases not Euclidean, which may lead to biases when comparing interpolation capabilities of two models. Smoothness and plausibility of linear interpolations in latent space are associated with the quality of the underlying generative model. In this paper, we show that not all such interpolations are comparable as they can deviate arbitrarily from the shortest interpolation curve given by the geodesic. This deviation is revealed by computing curve lengths with the pull-back metric of the generative model, finding shorter curves than the straight line between endpoints, and measuring a non-zero relative length improvement on this straight line. This leads to a strategy to compare linear interpolations across two generative models. We also show the effect and importance of choosing an appropriate output space for computing shorter curves. For this computation we derive an extension of the pull-back metric.</abstract>

[PDF](https://openreview.net/pdf?id=SL9w_9M-kSj) &bull;
[Forum](https://openreview.net/forum?id=SL9w_9M-kSj)

<div style="text-align:center">
&#10086;
</div>

**Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks** (Spotlight presentation)<br />
Cristian Bodnar &bull; Fabrizio Frasca &bull; Yu Guang Wang &bull; Nina Otter &bull; Guido Montufar &bull; Pietro Liò &bull; Michael M. Bronstein<br />
<abstract>The pairwise interaction paradigm of graph machine learning has predominantly governed the modelling of relational systems. However, graphs alone cannot capture the multi-level interactions present in many complex systems and the expressive power of such schemes was proven to be limited. To overcome these limitations, we propose Message Passing Simplicial Networks (MPSNs), a class of models that perform message passing on simplicial complexes (SCs) -- topological objects generalising graphs to higher dimensions. To theoretically analyse the expressivity of our model we introduce a Simplicial Weisfeiler-Lehman (SWL) colouring procedure for distinguishing non-isomorphic SCs. We relate the power of SWL to the problem of distinguishing non-isomorphic graphs and show that SWL and MPSNs are strictly more powerful than the WL test and not less powerful than the 3-WL test. We deepen the analysis by comparing our model with traditional graph neural networks with ReLU activations in terms of the number of linear regions of the functions they can represent. We empirically support our theoretical claims by showing that MPSNs can distinguish challenging strongly regular graphs for which GNNs fail and, when equipped with orientation equivariant layers, they can improve classification accuracy in oriented SCs compared to a GNN baseline. Additionally, we implement a library for message passing on simplicial complexes that we envision to release in due course.</abstract>

[PDF](https://openreview.net/pdf?id=RZgbB-O3w6Z) &bull;
[Forum](https://openreview.net/forum?id=RZgbB-O3w6Z)

# Poster Presentations

**A Geometry-Aware Algorithm to Learn Hierarchical Embeddings in Hyperbolic Space** <br />
Zhangyu Wang &bull; Lantian Xu &bull; Zhifeng Kong &bull; Weilong Wang &bull; Xuyu Peng &bull; Enyang Zheng<br />
<abstract>Hyperbolic embeddings are a class of representation learning methods that offer competitive performances when data can be abstracted as a tree-like graph. However, in practice, learning hyperbolic embeddings of hierarchical data is difficult due to the different geometry between hyperbolic space and the Euclidean space. To address such difficulties, we first categorize three kinds of illness that harm the performance of the embeddings. Then, we develop a geometry-aware algorithm to tackle the above illnesses. Specifically, we introduce the dilation operation, the transitive closure regularization, and an improved negative sampling strategy to build our algorithm. We empirically validate these techniques and present a theoretical analysis of the mechanism behind the dilation operation. Experiments on synthetic and real-world datasets reveal superior performances of our algorithm.</abstract>

[PDF](https://openreview.net/pdf?id=RcBGlCmmDnU) &bull;
[Forum](https://openreview.net/forum?id=RcBGlCmmDnU)

<div style="text-align:center">
&#10086;
</div>

**Attend to connect: GNN for predicting brain functional connectivity** <br />
Usman Mahmood &bull; Zening Fu &bull; Vince Calhoun &bull; Sergey Plis<br />
<abstract>Functional connectivity (FC) studies have demonstrated the benefits of investigating the brain and its disorders through the undirected weighted graph of fMRI correlation matrix. Most of the work with the FC, however, depends on the way the connectivity is computed and further depends on the manual post-hoc analysis of the FC matrices. In this work, we propose a deep learning architecture (BrainGNN) that learns the connectivity structure while learning to classify subjects. It simultaneously trains a graphical neural network on this graph and learns to select a sparse subset of brain regions important to the prediction task. We demonstrate the model's state-of-the-art classification performance on a schizophrenia fMRI dataset and show how introspection leads to disorder-relevant findings. The graphs learned by the model exhibit strong class discrimination, and the identified sparse subset of relevant regions is consistent with the schizophrenia literature.</abstract>

[PDF](https://openreview.net/pdf?id=v7Bct24zeft) &bull;
[Forum](https://openreview.net/forum?id=v7Bct24zeft)

<div style="text-align:center">
&#10086;
</div>

**AutoGL: A Library for Automated Graph Learning** <br />
Chaoyu Guan &bull; Ziwei Zhang &bull; Haoyang Li &bull; Heng Chang &bull; Zeyang Zhang &bull; Yijian Qin &bull; Jiyan Jiang &bull; Xin Wang &bull; Wenwu Zhu<br />
<abstract>Recent years have witnessed an upsurge of research interests and applications of machine learning on graphs. Automated machine learning (AutoML) on graphs is on the horizon to automatically design the optimal machine learning algorithm for a given graph task. However, all current libraries cannot support AutoML on graphs. To tackle this problem, we present Automated Graph Learning (AutoGL), the first library for automated machine learning on graphs. AutoGL is open-source, easy to use, and flexible to be extended. Specifically, We propose an automated machine learning pipeline for graph data containing four modules: auto feature engineering, model training, hyper-parameter optimization, and auto ensemble. For each module, we provide numerous state-of-the-art methods and flexible base classes and APIs, which allow easy customization. We further provide experimental results to showcase the usage of our AutoGL library.</abstract>

[PDF](https://openreview.net/pdf?id=0yHwpLeInDn) &bull;
[Forum](https://openreview.net/forum?id=0yHwpLeInDn)

<div style="text-align:center">
&#10086;
</div>

**Bermuda Triangles: GNNs Fail to Detect Simple Topological Structures** <br />
Arseny Tolmachev &bull; akira sakai &bull; Masaru Todoriki &bull; Koji Maruhashi<br />
<abstract>Most graph neural network architectures work by message-passing node vector embeddings over the adjacency matrix, and it is assumed that they capture graph topology by doing that. We design two synthetic tasks, focusing purely on topological problems -- triangle detection and clique distance -- on which graph neural networks perform surprisingly badly, failing to detect those "bermuda" triangles. We plan to make the datasets and their generation scripts publicly available.</abstract>

[PDF](https://openreview.net/pdf?id=Vz_Nl9MSQnu) &bull;
[Forum](https://openreview.net/forum?id=Vz_Nl9MSQnu)

<div style="text-align:center">
&#10086;
</div>

**Bootstrapped Representation Learning on Graphs** <br />
Shantanu Thakoor &bull; Corentin Tallec &bull; Mohammad Gheshlaghi Azar &bull; Remi Munos &bull; Petar Veličković &bull; Michal Valko<br />
<abstract>Current state-of-the-art self-supervised learning methods for graph neural networks are based on contrastive learning. As such, they heavily depend on the construction of augmentations and negative examples. Increasing the number of negative pairs improves performance, thereby requiring quadratic computation and memory cost to achieve peak performance. Inspired by BYOL, a recently introduced method for self-supervised learning that does not require negative pairs, we present Bootstrapped Graph Latents, BGRL, a self-supervised graph representation method that gets rid of this potentially quadratic bottleneck. BGRL outperforms or matches the previous unsupervised state-of-the-art results on several established benchmarks. Moreover, it enables the effective usage of graph attentional (GAT) encoders, allowing us to further improve the state of the art, in particular achieving 70.49% Micro-F1 on the PPI dataset using the linear evaluation protocol.</abstract>

[PDF](https://openreview.net/pdf?id=QrzVRAA49Ud) &bull;
[Forum](https://openreview.net/forum?id=QrzVRAA49Ud)

<div style="text-align:center">
&#10086;
</div>

**Chemistry-informed Macromolecule Graph Representation for Similarity Computation and Supervised Learning** <br />
Somesh Mohapatra &bull; Joyce An &bull; Rafael Gomez-Bombarelli<br />
<abstract>Macromolecules are large, complex molecules composed of covalently bonded monomer units, existing in different stereochemical configurations and topologies. As a result of such chemical diversity, representing, comparing, and learning over macromolecules emerge as critical challenges. To address this, we developed a macromolecule graph representation, with monomers and bonds as nodes and edges, respectively. We captured the inherent chemistry of the macromolecule by using molecular fingerprints for node and edge attributes. For the first time, we demonstrated computation of chemical similarity between 2 macromolecules of varying chemistry and topology, using exact graph edit distances and graph kernels. We also trained graph neural networks for a variety of glycan classification tasks, achieving state-of-the-art results. Our work has two-fold implications – it provides a general framework for representation, comparison, and learning of macromolecules; and enables quantitative chemistry-informed decision-making and iterative design in the macromolecular chemical space.</abstract>

[PDF](https://openreview.net/pdf?id=CIV88aSy8m8) &bull;
[Forum](https://openreview.net/forum?id=CIV88aSy8m8)

<div style="text-align:center">
&#10086;
</div>

**Exploring epithelial-cell calcium signaling with geometric and topological data analysis** <br />
Feng Gao &bull; Jessica Moore &bull; Bastian Rieck &bull; Valentina Greco &bull; Smita Krishnaswamy<br />
<abstract>Spatio-temporal calcium imaging is widely used to study neuronal activity. However the function of calcium signaling in epithelial cells is not well understood. We thus explore the underlying fluorescence patterns using a combination of data geometry and topology. We model the epithelial tissue as a graph and use a variant of geometric scattering transform (a multi-level wavelet transform on a graph) to describe the signaling at each time point. We then embed these discriptors using the manifold learning method PHATE in order to  capture the entire time-trajectory of calcium signaling. Finally, we use persistent homology computed on the PHATE embedding to quantitatively characterize the trajectory.  We demonstrate that scattering coefficients can effectively learn time point embeddings while PHATE can represent relationships between time points. Persistent homology provides a way to quantify differences between signaling dynamics as evidenced by the differences in dynamics between wild type cells and cells that are stalled in a particular cell cycle phase.</abstract>

[PDF](https://openreview.net/pdf?id=8V6vm_yuwEv) &bull;
[Forum](https://openreview.net/forum?id=8V6vm_yuwEv)

<div style="text-align:center">
&#10086;
</div>

**Fast GRL with Unique Optimal Solutions** <br />
Sami Abu-El-Haija &bull; Valentino Crespi &bull; Greg Ver Steeg &bull; Aram Galstyan<br />
<abstract>We consider two popular Graph Representation Learning (GRL) methods: message passing for node classification and network embedding for link prediction. For each, we pick a popular model that we:
(i) *linearize* and (ii) and switch its training objective to *Frobenius norm error minimization*. These simplifications can cast the training into finding the optimal parameters in closed-form. We program in TensorFlow a functional form of Truncated Singular Value Decomposition (SVD), such that, we could decompose a dense matrix $\mathbf{M}$, without explicitly computing $\mathbf{M}$.
We achieve competitive performance on popular GRL tasks while providing orders of magnitude speedup. We open-source our code at http://anonymous/url/for/review</abstract>

[PDF](https://openreview.net/pdf?id=YIloSPZFeGe) &bull;
[Forum](https://openreview.net/forum?id=YIloSPZFeGe)

<div style="text-align:center">
&#10086;
</div>

**GLAM: Graph Learning by Modeling Affinity to Labeled Nodes for Graph Neural Networks** <br />
Vijay Lingam &bull; Arun Iyer &bull; Rahul Ragesh<br />
<abstract>We propose GLAM, a semi-supervised graph learning method for cases when there are no graphs available. This approach learns a graph as a convex combination of the unsupervised k-Nearest Neighbor graph and a supervised label-affinity graph. The latter graph directly captures all the nodes' label-affinity with the labeled nodes, i.e., how likely a node has the same label as the labeled nodes. Our experiments show that GLAM gives close to or better performance (up to $\sim$1.5\%), while being simpler and faster (up to 70x) to train, than state-of-the-art graph learning methods. We also demonstrate the importance of individual components and contrast them with the state-of-the-art methods.</abstract>

[PDF](https://openreview.net/pdf?id=zyRPy5KrN6) &bull;
[Forum](https://openreview.net/forum?id=zyRPy5KrN6)

<div style="text-align:center">
&#10086;
</div>

**Grassmann Graph Embedding** <br />
Bingxin Zhou &bull; Xuebin Zheng &bull; Yu Guang Wang &bull; Ming Li &bull; Junbin Gao<br />
<abstract>Geometric deep learning that employs the geometric and topological features of data has attracted increasing attention in deep neural networks. Learning the intrinsic structure property of data is a crucial step for dimensionality reduction and effective feature extraction. This paper develops Grassmann graph embedding, which combines graph convolutions to capture the main components within graphs' hidden representations. Each set of featured graph nodes is mapped to a point on a Grassmann matrix manifold through Singular Value Decomposition, which is then embedded into a symmetric matrix space that approximates denoised second-order feature information. The view of treating nodes as a set could inspire many potential applications. In particular, we propose Grassmann (global graph) pooling that can connect with any graph convolution for graph neural networks. The Grassmann pooling achieves state-of-the-art performance on a variety of graph prediction benchmarks.</abstract>

[PDF](https://openreview.net/pdf?id=ELsrI4NgvS-) &bull;
[Forum](https://openreview.net/forum?id=ELsrI4NgvS-)

<div style="text-align:center">
&#10086;
</div>

**LDLE: Low Distortion Local Eigenmaps** <br />
Dhruv Kohli &bull; Alex Cloninger &bull; Gal Mishne<br />
<abstract>We present Low Distortion Local Eigenmaps (LDLE), a manifold learning technique which constructs a set of low distortion local views of a dataset in lower dimension and registers them to obtain a global embedding. The local views are constructed using the global eigenvectors of the graph Laplacian and are registered using Procrustes analysis. The choice of these eigenvectors may vary across the regions. In contrast to existing techniques, LDLE is more geometric and can embed manifolds without boundary as well as non-orientable manifolds into their intrinsic dimension.</abstract>

[PDF](https://openreview.net/pdf?id=jJs5OndwQ_z) &bull;
[Forum](https://openreview.net/forum?id=jJs5OndwQ_z)

<div style="text-align:center">
&#10086;
</div>

**LIDL: Local Intrinsic Dimension estimation using Likelihood** <br />
Piotr Tempczyk &bull; Adam Golinski &bull; Przemysław Spurek &bull; Jacek Tabor<br />
<abstract>We investigate the problem of local intrinsic dimension (LID) estimation. LID of the data is the minimal number of coordinates which are necessary to describe the data point and its neighborhood without the significant information loss. Existing methods for LID estimation do not scale well to high dimensional data because they rely on estimating the LID based on nearest neighbors structure, which may cause problems due to the curse of dimensionality. We propose a new method for Local Intrinsic Dimension estimation using Likelihood (LIDL), which yields more accurate LID estimates thanks to the recent progress in likelihood estimation in high dimensions, such as normalizing flows (NF). We show our method yields more accurate estimates than previous state-of-the-art algorithms for LID estimation on standard benchmarks for this problem, and that unlike other methods, it scales well to problems with thousands of dimensions. We anticipate this new approach to open a way to accurate LID estimation for real-world, high dimensional datasets and expect it to improve further with advances in the NF literature.</abstract>

[PDF](https://openreview.net/pdf?id=ij1aPkDZBYV) &bull;
[Forum](https://openreview.net/forum?id=ij1aPkDZBYV)

<div style="text-align:center">
&#10086;
</div>

**Low-rank projections of GCNs Laplacian** <br />
Nathan Grinsztajn &bull; Philippe Preux &bull; Edouard Oyallon<br />
<abstract>In this work, we study the behavior of standard models for community detection under spectral manipulations. Through various ablation experiments, we evaluate the impact of bandpass filtering on the numerical performances of a GCN: we empirically show that most of the necessary and used information for nodes classification is contained in the low-frequency domain, and thus contrary to images,  high-frequencies are less crucial to community detection. In particular, it is sometimes possible to obtain accuracies at a state-of-the-art level with simple classifiers that rely only on a few low frequencies.</abstract>

[PDF](https://openreview.net/pdf?id=DnlDTxsQ8Uz) &bull;
[Forum](https://openreview.net/forum?id=DnlDTxsQ8Uz)

<div style="text-align:center">
&#10086;
</div>

**On the Stability of Graph Convolutional Neural Networks under Edge Rewiring** <br />
Henry Kenlay &bull; Dorina Thanou &bull; Xiaowen Dong<br />
<abstract>Graph neural networks are experiencing a surge of popularity within the machine learning community due to their ability to adapt to non-Euclidean domains and instil inductive biases. Despite this, their stability, i.e., their robustness to small perturbations in the input, is not yet well understood. Although there exists some results showing the stability of graph neural networks, most take the form of an upper bound on the magnitude of change due to a perturbation in the graph topology. However, the change in the graph topology captured in existing bounds tend not to be expressed in terms of structural properties, limiting our understanding of the model robustness properties. In this work, we develop an interpretable upper bound elucidating that graph neural networks are stable to rewiring between high degree nodes. This bound and further research in bounds of similar type provide further understanding of the stability properties of graph neural networks.</abstract>

[PDF](https://openreview.net/pdf?id=NG7Eb2_zR6K) &bull;
[Forum](https://openreview.net/forum?id=NG7Eb2_zR6K)

<div style="text-align:center">
&#10086;
</div>

**Online High-Dimensional Change-Point Detection using Topological Data Analysis** <br />
Xiaojun Zheng &bull; Simon Mak &bull; Yao Xie<br />
<abstract>Topological Data Analysis (TDA) is a rapidly growing field, which studies methods for learning underlying topological structures present in complex data representations. TDA methods have found recent success in extracting useful geometric structures for a wide range of applications, including protein classification, neuroscience, and time-series analysis. However, in many such applications, one is also interested in sequentially detecting changes in this topological structure. We propose a new method called Persistence Diagram based Change-Point (PD-CP), which tackles this problem by integrating the widely-used persistence diagrams in TDA with recent developments in nonparametric change-point detection. The key novelty in PD-CP is that it leverages the distribution of points on persistence diagrams for online detection of topological changes. We demonstrate the effectiveness of PD-CP in an application to solar flare monitoring.</abstract>

[PDF](https://openreview.net/pdf?id=ZMdN2FEi14R) &bull;
[Forum](https://openreview.net/forum?id=ZMdN2FEi14R)

<div style="text-align:center">
&#10086;
</div>

**Persistent Message Passing** <br />
Heiko Strathmann &bull; Mohammadamin Barekatain &bull; Charles Blundell &bull; Petar Veličković<br />
<abstract>Graph neural networks (GNNs) are a powerful inductive bias for modelling algorithmic reasoning procedures and data structures. Their prowess was mainly demonstrated on tasks featuring Markovian dynamics, where querying any associated data structure depends only on its latest state. For many tasks of interest, however, it may be highly beneficial to support efficient data structure queries dependent on previous states. This requires tracking the data structure's evolution through time, placing significant pressure on the GNN's latent representations. We introduce Persistent Message Passing (PMP), a mechanism which endows GNNs with capability of querying past state by explicitly persisting it: rather than overwriting node representations, it creates new nodes whenever required. PMP generalises out-of-distribution to more than 2$\times$ larger test inputs on dynamic temporal range queries, significantly outperforming GNNs which overwrite states.</abstract>

[PDF](https://openreview.net/pdf?id=HhOJZT--N23) &bull;
[Forum](https://openreview.net/forum?id=HhOJZT--N23)

<div style="text-align:center">
&#10086;
</div>

**Recovering Barabási-Albert Parameters of Graphs through Disentanglement** <br />
Cristina Guzmán &bull; Daphna Keidar &bull; Tristan Meynier &bull; Andreas Opedal &bull; Niklas Stoehr<br />
<abstract>Classical graph modeling approaches such as Erdős-Rényi random graphs (ER graphs) or Barabási Albert graphs (BA graphs), here referred to as stylized models, aim to reproduce properties of real-world graphs in an interpretable way. While useful, graph generation with stylized models requires domain knowledge and iterative trial and error simulation. Stoehr et al. (2019) suggest addressing these issues by learning the generation process from graph data, using a disentanglement-focused deep autoencoding framework, more specifically, a $\beta$-Variational Autoencoder ($\beta$-VAE). While they successfully recover the generative parameters of ER graphs through the model's latent variables, their model performs badly on sequentially generated graphs such as BA graphs, due to their oversimplified decoder. We focus on recovering the generative parameters of BA graphs by replacing the decoder in Stoehr et al. (2019)'s $\beta$-VAE with a sequential one. We first learn the generative BA parameters in a supervised fashion using a Graph Neural Network (GNN) and a Random Forest Regressor, by minimizing the squared loss between the true generative parameters and the latent variables. Next, we train a $\beta$-VAE model, combining the GNN encoder from the previous step with an LSTM-based decoder with a customized loss.</abstract>

[PDF](https://openreview.net/pdf?id=ln6AzgMbKBC) &bull;
[Forum](https://openreview.net/forum?id=ln6AzgMbKBC)

<div style="text-align:center">
&#10086;
</div>

**Sanity Check for Persistence Diagrams** <br />
Chen Cai<br />
<abstract>Recently many efforts have been made to incorporate persistence diagrams, one of major tools in topological data analysis (TDA), into machine learning pipelines. To better understand the power and limitation of persistence diagrams, we carry out a range of experiments on both graph and shape data, aiming to decouple and inspect the effects of different factors involved. To this end, we propose a sanity check for persistence diagrams to delineate critical values and pairings of critical values (structure of persistence module). For graph classification tasks, we note that while persistence pairing yields consistent improvement over various benchmark datasets, it appears that for various filtration functions tested, most discriminative power comes from critical values. For shape segmentation and classification, however, we note that persistence pairing shows significant power on most of the benchmark datasets, and improves over summaries based on merely critical values. Our results help provide insights on when persistence diagram based summaries could be more suitable.</abstract>

[PDF](https://openreview.net/pdf?id=lygeqKLv6Ec) &bull;
[Forum](https://openreview.net/forum?id=lygeqKLv6Ec)

<div style="text-align:center">
&#10086;
</div>

**Scaling Up Graph Homomorphism Features with Efficient Data Structures** <br />
Paul Beaujean &bull; Florian Sikora &bull; Florian Yger<br />
<abstract>Typical datasets used in graph classification tasks only contain a few thousand graphs which rarely exceed hundreds of nodes. Graph homomorphism densities are permutation-invariant features that can be directly computed from graph data, and their approximation scales naturally to large graphs. We propose the use of efficient data structures for approximate set membership in the context of a sampling algorithm for graph homomorphism density which enables the use of large-scale datasets containing larger graphs. To validate our findings, we compare this method with existing approaches used for graph homomorphism features in synthetic experiments.</abstract>

[PDF](https://openreview.net/pdf?id=EwT8NpZIth8) &bull;
[Forum](https://openreview.net/forum?id=EwT8NpZIth8)

<div style="text-align:center">
&#10086;
</div>

**Self-supervised representation learning on manifolds** <br />
Eric O Korman<br />
<abstract>We explore the use of a topological manifold, represented as a collection of charts, as the target space of neural network based representation learning tasks. This is achieved by a simple adjustment to the output of an encoder's network architecture plus the addition of a maximal mean discrepancy based loss function for regularization. Most algorithms in representation learning are easily adaptable to our framework and we demonstrate its effectiveness by adjusting SimCLR to have a manifold encoding space. Our experiments show that we obtain a substantial performance boost over the baseline for low dimensional encodings.</abstract>

[PDF](https://openreview.net/pdf?id=EofGDIGAhvR) &bull;
[Forum](https://openreview.net/forum?id=EofGDIGAhvR)

<div style="text-align:center">
&#10086;
</div>

**Simplicial Regularization** <br />
Jose Gallego-Posada &bull; Patrick Forré<br />
<abstract>Inspired by the fuzzy topological representation employed in UMAP (McInnes et al., 2018), we propose a regularization principle based on the preservation of the simplicial complex structure of the data. We analyze the behavior of our proposal in contrast with the common mixup (Zhang et al., 2018) framework on dimensionality reduction and supervised learning tasks, and show how simplicial regularization alleviates some of the shortcomings of state-of-the art methods for regularization based on data augmentation.</abstract>

[PDF](https://openreview.net/pdf?id=x9xn6HKgefz) &bull;
[Forum](https://openreview.net/forum?id=x9xn6HKgefz)

<div style="text-align:center">
&#10086;
</div>

**Unsupervised Geometric Disentanglement via CFAN-VAE** <br />
Norman Joseph Tatro &bull; Stefan C Schonsheck &bull; Rongjie Lai<br />
<abstract>Geometric disentanglement, the separation of latent codes for intrinsic (i.e. identity) and extrinsic (i.e. pose) geometry, is a prominent task for generative models of non-Euclidean data such as 3D deformable models. It provides greater interpretability of the latent space, and leads to more control in generation. This work introduces a mesh feature, the conformal factor and normal feature (CFAN), for use in mesh convolutional autoencoders. We further propose CFAN-VAE, a novel architecture that disentangles identity and pose using the CFAN feature. Requiring no label information on the identity or pose during training, CFAN-VAE achieves geometric disentanglement in an unsupervised way. Our comprehensive experiments, including reconstruction, interpolation, generation, and identity/pose transfer, demonstrate CFAN-VAE achieves state-of-the-art performance on unsupervised geometric disentanglement. </abstract>

[PDF](https://openreview.net/pdf?id=shaSYHQSEVf) &bull;
[Forum](https://openreview.net/forum?id=shaSYHQSEVf)
