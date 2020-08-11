---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Wave Packets (WIP)"
subtitle: ""
summary: ""
authors: [Rodrigo de Souza]
tags: ["physics", "quantum mechanics"]
categories: []
date: 2020-08-10T23:36:52+02:00
lastmod: 2020-08-10T23:36:52+02:00
featured: false
draft: false
math: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

## Introduction

These are my notes regarging my studies on trying to acquire a bit more knowledge on the grounds of the quantum mechanics.

In order to embody both particle and wave features in quantum mechanics, we must rely on a mathematical scheme called wave packets.

In classical physics, particles have defined position and velocity. In quantum mechanics, it describes a material particle by a *wave function* corresponding  to the matter wave associated with the particle (de Broglie's conjecture). But wave functions depend on the whole space, they *can not be localized*. The trick is trying to get a wave function that vanishes everywhere except in the neighbourhood of the "classical trajectory", meaning the amplitude being large in that region and zero outside it. This matter wave must be localized around the region of space which the particle is confined. This sort of wave function is called *wave packet*.

A wave packet consists  of a group of waves of slightly different wavelengths, whith phases and amplitudes chosen in order that they interfere constructively over a small region of space (the particle classical region) and destructively elsewhere. They represent a unifying mathematical tool that can cope with and embody nature's particle-like behavior.


## Localized Wave Packets

Localized wave packets can be constructed via superposition of waves with sligthly different wavelenghts with phases and amplitudes chosen to make the superposition constructive in the desired region and destructive outside it. Mathematically, it can be achieved by means of *Fourier Transforms*.

Considering a one dimensional wave packet $\psi(x, t)$ (particle moving along the *x-axis*), it can be constructed by superposing plane waves of different frequencies (or wavelengths):

\begin{equation}
  \psi(x, t)  =   \frac{1}{\sqrt{2 \pi}} \int_{- \infty}^{+ \infty} \phi(k) e^{i(kx - \omega t)} dk,
  \label{eq:psi}
\end{equation}

with $\psi(k)$ being the amplitude of the wave packet.


We want to look at the form of the packet at a given time; choosing this time to be $t=0$ and abbreviating  $\psi(x, 0)$ by $\psi_0(x)$, the previous equation can be reduced to

\begin{equation}
  \psi_0(x)  =   \frac{1}{\sqrt{2 \pi}} \int_{- \infty}^{+ \infty} \phi(k) e^{ikx} dk,
  \label{eq:psi_0}
\end{equation}

where $\phi(k)$ is the Fourier transform of $\psi_0(x)$,

\begin{equation}
  \phi(k)  =   \frac{1}{\sqrt{2 \pi}} \int_{- \infty}^{+ \infty} \psi_0(x) e^{-ikx} dx,
  \label{eq:phi}
\end{equation}


The relations \eqref{eq:psi_0} and \eqref{eq:phi} show that $\phi(k)$ determines $\psi_0(x)$ and vice-versa. The localized packet \eqref{eq:psi_0} whose form is determined by the x-dependence of $\psi_0(x)$ have the required property of localization: $\mid \psi_0(x)\mid$ peaks at $x=0$ and vanishes far away from $x=0$. Let us analyse this statement:

* As $x \rightarrow 0$ we have $e^{ikx} \rightarrow 1$, which means that the $\phi(k)$ waves of different frequencies will interfere constructively because of the various k-integrations in \eqref{eq:phi}.
* Far away from $x=0$ ($\mid x \mid \gg 0$), the phase $e^{ikx}$ goes through many periods leading to violent oscillations, thereby yielding destructive interference (the various k-integrations add up to zero).



## References


Zettili, Nouredine: Quantum Mechanics: Concepts and Applications, 2nd ed, 2009.
