# The Track Layout Problem from a SAT-Solving Perspective

Introduction

The track layout problem is a challenge in graph theory and computational geometry. It involves arranging the vertices and edges of a graph in a linear order while minimizing the crossings and maintaining specific track constraints. This repository contains a Python implementation of a solution to the track layout problem using two different SAT methods. 

The underlying work has demonstrated that a relational view of node positions within the track layout is a more effective approach. The evaluation showed that adding an extra variable significantly reduces the number of clauses, albeit at the cost of increased evaluation time. Furthermore, as the number of nodes increases, the time required to create the clauses becomes less significant in terms of overall evaluation time.

### First Approach

To assign a node of the graph to a track, we use the variable $\sigma(v_i, t_k)$ for each pair of nodes $v_i \in V$ and track $t_k$. Additionally, we define the variable $\omega(v_i, v_j)$ for each pair of nodes $v_i, v_j \in V$. This variable evaluates to true if $v_i$ is a left neighbor of $v_j$ on any track. Note that $\omega(v_i, v_j)$ cannot be true if $i = j$, as a node cannot be its own neighbor.

We express the constraints using the following conjunctions for each disjoint pair of edges $e_{i,j}$ and $e_{u,w}$:

$$ 
\forall e_{i,j}, e_{u,w} \in E : 
( \sigma(v_i, t_x) \land \sigma(v_u, t_x) \land \sigma(v_j, t_y) \land \sigma(v_w, t_y) \land \omega(v_i, v_u) \land \omega(v_w, v_j) ) 
$$

### Second Approach

Another idea is to define a new variable that indicates whether two nodes are on the same track, regardless of which track it is. We introduce the variable $\psi(v_i, v_j)$ for all $v_i, v_j \in V$, where $\psi(v_i, v_j)$ evaluates to true if and only if $v_i$ and $v_j$ are on the same track.

Using this new variable, we can further limit the crossing clauses. We construct a conjunction for every disjoint pair of edges $e_{i,j}$ and $e_{u,w}$:

$$ 
\forall e_{i,j}, e_{u,w} \in E : 
( \psi(v_i, v_u) \land \psi(v_j, v_w) \land \omega(v_i, v_u) \land \omega(v_w, v_j) ) 
$$
