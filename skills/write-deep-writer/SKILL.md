---
name: write-deep-writer
description: Adaptive deep writing agent that transforms any input (video interviews, speeches, articles, podcasts) into coherent, in-depth written content with logical structure. Automatically identifies writing principles, target audience, and scenarios from input. Handles spoken language, merges duplicate viewpoints, and optimizes logic while preserving the original framework. Features three-stage workflow with todo list tracking: Analysis & Planning → Structure Design → Content Writing.
---

# Write Deep Writer

Adaptive deep writing agent that transforms any input into coherent, in-depth written content.

## Overview

This agent converts spoken or fragmented content (video interviews, speeches, podcasts) into well-structured, deep written content. It automatically:
- Identifies writing principles, target audience, and scenarios from input
- Handles spoken language and removes redundancies
- Merges similar viewpoints for clarity
- Optimizes logic while preserving original structure
- Provides three-stage workflow with progress tracking

## Quick Start

```
Input: Any content (video interview transcript, speech text, article, podcast transcript)

Output: Deep, structured written content (5000-10000 words)
```

## Core Capabilities

### Eight-Layer Processing System

1. **Requirement Identification**
   - Extracts writing principles from input keywords
   - Identifies target audience based on terminology density
   - Detects writing scenario (academic/business/popular)
   - Determines core purpose (interpretation/critique/summary)

2. **Brief Document Construction**
   - Builds writing baseline document
   - Defines creator persona
   - Specifies audience profile
   - Establishes content stance
   - Lists core themes and key points

3. **Preprocessing**
   - Identifies spoken language (fillers: "um", "ah", "like")
   - Detects repetitive patterns
   - Finds fragmented viewpoints

4. **Viewpoint Extraction & Clustering**
   - Extracts all core viewpoints
   - Clusters similar viewpoints by semantic similarity
   - Merges each cluster into complete, deep arguments

5. **Logic Analysis**
   - Identifies causal relationships ("because...", "leads to...")
   - Identifies parallel relationships ("first, second...", "on the other hand...")
   - Identifies progressive relationships ("further...", "not only but also...")
   - Identifies contrast relationships ("however...", "unlike...")
   - Identifies summary relationships ("in conclusion...", "summarizing...")
   - Builds logic graph

6. **Structure Optimization**
   - Maintains core framework
   - Merges duplicates
   - Enhances logic with transitions
   - Micro-adjusts order for better flow
   - Ensures alignment with Brief

7. **Deep Writing**
   - Supplements background knowledge
   - Adds data support
   - Enriches with examples
   - Expands viewpoints
   - Enhances logic
   - Optimizes expression

8. **Quality Check**
   - Verifies duplicate merging
   - Checks spoken language handling
   - Validates logic clarity
   - Confirms content depth
   - Ensures structure preservation
   - Validates principle satisfaction

## Workflow

### Three-Stage Process with Todo Tracking

#### Stage 1: Analysis & Planning
- Step 1: Requirement Identification
- Step 1.5: Brief Document Construction
- Step 2: Preprocessing
- Step 3: Viewpoint Extraction & Clustering
- Step 4: Logic Analysis

**Output**: Brief document + Viewpoint clusters + Logic graph

#### Stage 2: Structure Design
- Step 5: Structure Optimization

**Output**: Optimized structure framework

#### Stage 3: Content Writing
- Step 6: Deep Writing
- Step 7: Quality Check

**Output**: Complete deep content

## Todo List Management

```
【待办事项】
- [pending] 第一阶段：分析与规划
- [pending] 第二阶段：结构设计
- [pending] 第三阶段：内容撰写
```

**Principles**:
- One stage in progress at a time
- Mark completed immediately upon completion
- User confirmation required between stages
- Create new tasks for blockers

## Constraints

1. **Structure不可重组**: Once structure framework is determined, strictly follow during writing
2. **Viewpoints必须合并**: All identified duplicates must be merged
3. **Logic必须清晰**: Merged and optimized content must have clear logic chains
4. **Depth要有度**: Supplemented content must be highly relevant
5. **Expression要准确**: Do not distort original core viewpoints
6. **Brief是基准**: All steps must align with Brief requirements
7. **Stages必须确认**: Must wait for user confirmation after each stage

## Example Input & Output

### Input (Interview Transcript - Spoken)
```
记者：AI会对就业有什么影响？
嘉宾：嗯，这个话题很大。首先，一些重复性的工作，比如数据录入，
      肯定会被AI取代。然后，创造性工作可能暂时不会受影响。
      但是...嗯...其实高级的分析工作也可能被AI做。
```

### Stage 1 Output: Viewpoint Clusters
```
聚类1：AI对不同工作类型的影响
  - 原观点1：重复性工作会被取代
  - 原观点2：创造性工作暂时不受影响
  - 原观点3：高级分析工作也会被取代
  合并后观点：AI对不同工作类型的影响呈现递进趋势：从重复性工作（如数据录入）到高技能分析工作（如财务分析）都会受到冲击，而创造性工作（如艺术）相对安全但边界模糊。
```

### Stage 2 Output: Structure Framework
```
一、AI对不同类型工作的影响（递进逻辑）
   1. 重复性工作：数据录入、客服
   2. 分析性工作：财务分析
   3. 创造性工作：相对安全但边界模糊
```

### Stage 3 Output: Deep Content (Excerpt)
```
# 一、AI对不同类型工作的影响

## 1. 重复性工作的危机

数据录入、客服这类重复性、规则明确的工作，将成为AI取代的首批目标。
这类工作的特点是：流程固定、可量化、不需要复杂判断。

[Deep dive continues with background, examples, data...]

## 2. 分析性工作的冲击

财务分析等高技能工作同样面临挑战。AI在数据分析、模式识别方面
已具备超越人类的能力。

[Deep dive continues with specific examples, industry cases...]

## 3. 创造性工作的相对安全与边界模糊

设计师、艺术家等创造性工作曾被认为是最难被AI取代的，但
AI绘画的突破改变了这一认知。

[Deep dive continues with analysis of human creativity, human-AI collaboration...]
```

## Brief Document Format

```
【Brief文档】

# 创作者人设
[Inferred persona from requirement identification and content style]

# 受众画像
- 年龄层次：[Identified age range]
- 知识背景：[Identified background]
- 关注点：[Identified focus areas]

# 写作场景
[Identified scenario]

# 内容立场
[Identified stance]

# 写作原则
[Identified principles]

# 核心主题
[1-3 core themes extracted from content]

# 关键金句/核心观点
[3-5 key viewpoints]

# 结构要求
- 保持原有结构：是/否
- 逻辑强度要求：[高/中/低]
- 深化程度要求：[高/中/低]
```

## Output Format

Each stage outputs clearly labeled content:

```
【阶段X完成】

---
【本阶段输出】
[Stage-specific output]

---

【待办事项状态】
- [completed] 第一阶段：分析与规划
- [completed] 第二阶段：结构设计
- [pending] 第三阶段：内容撰写

---

是否继续下一阶段？（输入"继续"进入下一阶段，或提出修改意见）
```

## Notes

- **Stage-wise confirmation**: Must wait for user confirmation after each stage
- **Strict structure adherence**: Once structure is optimized, do not change it during writing
- **Viewpoint merging**: All duplicates must be merged, no repetition allowed
- **Logic consistency**: Ensure clear logic chains in merged content
- **Brief as baseline**: Always refer back to Brief document for consistency
- **Quality check**: Perform thorough self-check before final output