Ideas
=====

Choice of Language
------------------

We want to be as fast as possible, but does that mean we need to do it in straight-up ANSI C?
To be have the ability to be as fast as possible, we obviously need a compiled language that
either does not have a runtime or has a *very* thin one.

Options on the board:
 * ANSI C
 * Objective-C
 * C++

How Genetic?
------------

Um... yeah

As genetic as possible. Whether weights or a priority list is used, the program should create a randomized, 
medium-sized (20? 50? 100?) population of individuals. After thinking more on the problem, my current genetic
approach may focus on local maxima, which a simulated annealing approach manages to avoid. Currently, the two
most-fit specimens within the gene pool are mated to produce some size pool of children. The two most-fit
children are compared to the two least-fit specimens in the current pool, and swaps are made as necessary.
The ideal "genetic" approach is to have random couples mate, producing some number of children into a pool of
children. However, this approach takes much longer than the above. To simulate this and get around the potential
of sticking at a local maxima, a random element can be introduced which chooses between:
  * Mating two most fit
  * Mating most fit and a random specimen
  * Mating a member of top 50% and a random specimen
  * Mating two random specimens
  * And potentially some other combinations.

Mutations can include:
  * Dropping a gene
  * Reordering one gene
  * Swapping two genes
  * Random ordering of full or partial genome
  * Reversing the full or partial genome

Gameplan
--------

  * Eli's code focuses on sorting the guests based using a stable sort to create a priority list, then assigning
    descending order based on an independent priority list of preferences.
  * Mutations currently include a random chance to cause some combination of the following:
    * Dropping a gene
    * Swapping two genes
    * Reversing both list orders.

  
  