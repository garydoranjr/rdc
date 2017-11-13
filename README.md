RDC: Randomized Dependence Coefficient
======================================

*Algorithm by:* David Lopez-Paz, Philipp Hennig, and Bernhard Schoelkopf

*Code by:* Gary Doran

## Installation Instructions

To install, run:

    $ [sudo] python setup.py install

## Algorithm Description

The RDC is a measure of nonlinear dependence between two (possibly
multidimensional) variables. A full description of the algorithm is given in
the [2013 paper](https://papers.nips.cc/paper/5138-the-randomized-dependence-coefficient.pdf)
by David Lopez-Paz, Philipp Hennig, and Bernhard Schoelkopf.

## Usage

Given two NumPy arrays, `x` and `y`, the measure can be invoked as follows:

    >>> from rdc import rdc
    >>> print rdc(x, y)

If `x` and `y` are univariate, then they should be 1-D NumPy arrays; otherwise,
then should be `n`-by-`k` arrays, where `k` is the number of dimensions and `n`
is the number of examples. The two variables must have the same number of
examples, but can have different numbers of features.

There are additional keyword parameters for `rdc` that correspond to parameters
described in the paper. One new parameter is `n`, which is the number of times
the RDC is computed with different random seeds to reduce variance in the
estimation of the statistic. The median value across these `n` runs is returned.
