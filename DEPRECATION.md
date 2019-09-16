# Deprecation Policy Proposal

As Rectifai matures we will inevitably need to deprecate old models, interfaces and features. This document provides guidelines that attempt to minimize churn. Reducing churn helps users build next generation models with tools they've already mastered.

### Terminology note

We _deprecate_ some component to communicate that a preferred alternative exists. A _deprecated_ component does not necessarily have to be _removed_ from the library.

### Goals

1. Promote backward compatibility.
2. Describe code-level and release process for both deprecation and removal.

### Non-goals

1. Eliminate all deprecation and removal.
2. Legislate. Good judgment by Rectifai developers is much preferred.
