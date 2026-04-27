# Stable-Baselines3 Atari Mini Project

**Course Project Window:** April 7, 2026 - April 26, 2026

**Final Submission Due:** Sunday, April 26, 2026, by 11:59 PM

**Presentations:** Tuesday, April 28, 2026, and Thursday, April 30, 2026

**Team Size:** 1-3 students

## Overview

In this compressed graduate mini-project, teams will use Stable-Baselines3 to explore reinforcement learning in Atari domains. Each team will train and compare **DQN** with **one or two additional Stable-Baselines3 algorithms** on **one to three Atari environments**. Teams must save models at multiple checkpoints, resume training from saved models, test trained agents, generate gameplay videos, and summarize experimental findings with tables, plots, and discussion.

## Purpose

This mini-project is designed as a focused experimental study rather than a large semester-long build. The emphasis is on carrying out a manageable but meaningful reinforcement learning investigation under a short timeline. Your team should compare algorithms, hyperparameters, and training progress across checkpoints while documenting both quantitative and qualitative behavior.

## Required Project Elements

1. Use **DQN** as a required baseline.
2. Use **1 or 2 additional Stable-Baselines3 algorithms**.
3. Work with **1 to 3 Atari domains**.
4. Explore **multiple hyperparameter settings**.
5. Save models at **multiple training levels**.
6. Demonstrate **restarting training from saved checkpoints**.
7. Test trained models using a consistent evaluation process.
8. Generate gameplay videos from representative checkpoints and final models.
9. Provide summary data and a short analysis of findings.

## Recommended Scope

Because this is a compressed mini-project, keep the scope realistic and manageable.

- **1 Atari domain** is appropriate for smaller teams or deeper experimentation.
- **2 Atari domains** is a strong target for most teams.
- **3 Atari domains** is appropriate only if the team keeps the hyperparameter study modest.
- **DQN + 1 additional algorithm** is the standard target.
- **DQN + 2 additional algorithms** is optional for ambitious teams.

## Suggested Algorithm Choices

Good comparison choices in Stable-Baselines3 include:

- A2C
- PPO

Each team should think carefully about which algorithms are practical for the selected domains and available compute time.

## Examples of Hyperparameters to Explore

- learning rate
- batch size
- buffer size
- discount factor (gamma)
- target update interval
- training frequency
- exploration schedule or epsilon-related settings for DQN
- number of parallel environments for actor-critic methods
- network architecture choices, if feasible

## Required Deliverables

### 1. Code Submission

Submit code or notebooks that show training, checkpoint saving, checkpoint loading, resumed training, evaluation, and video generation.

### 2. Results Summary

Submit a concise experiment summary including environments used, algorithms used, hyperparameters explored, saved checkpoints, evaluation scores, and short observations.

### 3. Mini Report

Submit a **3-5 page report** that includes:

- project setup
- algorithms and domains
- hyperparameter variations
- checkpoint and resumed-training evidence
- evaluation summary
- interpretation of results

### 4. Presentation

Give a **10-minute presentation** on **April 28** or **April 30**.

The presentation should include the project goal, selected domains and algorithms, key hyperparameter experiments, checkpoint and resume workflow, performance summary, gameplay clips or screenshots, and major conclusions.

### 5. Videos

Provide gameplay videos showing at least:

- one earlier checkpoint
- one later checkpoint
- one final or best model

## Minimum Technical Expectations

- successful training of at least one DQN Atari agent
- comparison with at least one additional SB3 algorithm
- hyperparameter variation beyond defaults
- checkpoint saving at multiple levels
- checkpoint reload and resumed training
- model evaluation on held-out episodes
- gameplay video generation
- summary of results in tables or figures

## Recommended Analysis Questions

- Which algorithm performed best on each environment?
- Which hyperparameters seemed most important?
- Did resumed training recover smoothly, or were there issues?
- Did some environments appear more stable than others?
- Were the best quantitative models also the most convincing qualitatively in videos?
- How sensitive were results to early training instability?

## Grading

|Category|Points|
|---|---|
|Experimental design and scope|20|
|Working implementation|30|
|Checkpointing and resumed training|20|
|Evaluation and summary data|25|
|Report quality and interpretation|25|
|Presentation|20|
|Video evidence and overall completeness|10|
|Total|150|

## Project Policies

### Collaboration

Students may work only within their assigned team of 1-3. Teams should clearly document each member's contributions.

### Use of AI Tools

AI tools may be used for debugging, coding assistance, and writing support, but teams remain responsible for the correctness of all code, experiments, analysis, and writing. Significant use of AI tools should be disclosed.

### Academic Integrity

Do not fabricate results, fake videos, or misrepresent resumed training as uninterrupted training. Experimental claims should be supported by submitted evidence.

### Reproducibility

Code and notebooks should be organized so that another student can follow the main workflow for training, evaluation, and video generation.

## Due Dates

- **Project opens:** Tuesday, April 7, 2026
- **Final submission due:** Sunday, April 26, 2026, by 11:59 PM
- **Presentation dates:** Tuesday, April 28, 2026, and Thursday, April 30, 2026