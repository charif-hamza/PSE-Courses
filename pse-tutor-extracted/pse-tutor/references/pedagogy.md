# Pedagogical Principles for PSE Teaching

## Core Teaching Philosophy

### First Principles Approach
- Start with fundamental axioms and build concepts from the ground up
- Never assume prerequisite knowledge without verification
- Make explicit the reasoning chain from basics to advanced concepts
- Connect mathematical abstractions to physical intuition

### Physical Intuition Development
- Always provide physical interpretation of mathematical concepts
- Use concrete examples from chemical processes
- Relate abstract concepts to observable phenomena
- Encourage visualization and mental models

### Spaced Repetition
- Review previously learned concepts at increasing intervals
- Integrate old concepts into new problem contexts
- Use cumulative problem sets that test retention
- Schedule review sessions based on progression.json tracking

## Teaching Methodology

### 1. Concept Introduction
When introducing any new concept:

1. **State the learning objective clearly**
   - What will the student be able to do after mastering this?
   - Why is this concept important in PSE?

2. **Establish prerequisites**
   - What concepts must be understood first?
   - Briefly review key prerequisite ideas

3. **Build from first principles**
   - Start with the most basic definition or axiom
   - Show how the concept emerges naturally
   - Avoid "hand-waving" or unexplained leaps

4. **Provide physical interpretation**
   - What does this mean in the real world?
   - How does it apply to chemical processes?
   - What is the intuitive understanding?

5. **Work through examples**
   - Start with simple, clear examples
   - Progress to more complex applications
   - Show common mistakes and how to avoid them

### 2. Application Exercises
After teaching each subconcept:

1. **Generate 3-5 exercises of ascending difficulty:**
   - Exercise 1: Direct application (plug and chug)
   - Exercise 2: Requires one step of reasoning
   - Exercise 3: Multi-step problem requiring integration
   - Exercise 4: Application to PSE context
   - Exercise 5: Challenge problem requiring deeper insight

2. **Exercise design principles:**
   - Each exercise should test a specific aspect of understanding
   - Include numerical problems AND conceptual questions
   - Require work to be shown in Typst format
   - Provide hints for challenging problems
   - Solutions should reinforce the learning objectives

3. **Mastery assessment:**
   - Student must complete all exercises successfully
   - Provide feedback on incorrect attempts
   - Explain why wrong approaches don't work
   - Only proceed when mastery is demonstrated

### 3. Cheat Sheet Generation
After completing all subconcepts in a concept:

1. **Structure:**
   - Title: Clear identification of the concept
   - Key definitions: Precise mathematical/physical definitions
   - Important formulas: Boxed and highlighted
   - Rules and theorems: Stated clearly
   - Common applications: Brief examples
   - Common pitfalls: What to watch out for
   - Quick reference tables: When applicable

2. **Format requirements:**
   - Use LaTeX for professional appearance
   - Use tcolorbox environments for visual organization
   - Two-column layout for compactness
   - Clear hierarchy with sections and subsections
   - Color coding: Blue for concepts, green for formulas, yellow for notes

3. **Content principles:**
   - Concise but complete
   - Focus on what students will reference frequently
   - Include both equations and physical interpretations
   - Cross-reference related concepts

### 4. Problem Set Generation
After completing all concepts in a subtier:

1. **Problem set composition:**
   - 8-12 problems covering the entire subtier
   - Mix of calculation, derivation, and conceptual problems
   - At least 2 problems integrating multiple concepts
   - 1-2 challenging problems requiring creative thinking
   - All problems should be relevant to PSE applications

2. **Problem characteristics:**
   - **Non-generic**: Avoid textbook-style plug-and-chug
   - **Intellectually stimulating**: Require genuine understanding
   - **Cumulative**: Reference earlier subtiers when appropriate
   - **Realistic**: Based on actual PSE scenarios when possible
   - **Varied difficulty**: From moderate to challenging

3. **Answer key requirements:**
   - Complete solutions with all steps shown
   - Explanation of approach and reasoning
   - Common mistakes highlighted
   - Alternative solution methods when applicable
   - Physical interpretation of results

4. **Format:**
   - Problem statements in problembox environment
   - Solutions in solutionbox environment
   - Hints in hintbox environment (when needed)
   - Clear numbering and organization
   - Professional LaTeX formatting

## Integration and Connections

### Horizontal Integration (Within Tier)
- Explicitly show connections between subtiers
- Use examples that combine concepts from different subtiers
- Remind students how concepts relate to each other

### Vertical Integration (Across Tiers)
- Problem sets in later tiers must include concepts from earlier tiers
- Show how foundational concepts enable advanced understanding
- Regularly callback to Tier 1 fundamentals

### PSE Context Integration
- Every mathematical concept should connect to PSE applications
- Use examples from: reactors, separations, control systems, optimization
- Build intuition for how mathematics serves engineering

## Assessment and Progression

### Mastery Criteria
A student has mastered a subconcept when they can:
1. Explain the concept in their own words
2. Apply it correctly to novel problems
3. Identify when the concept is relevant
4. Connect it to related concepts
5. Demonstrate physical intuition

### Progression Rules
- Never advance before mastery is demonstrated
- Use progression.json to track completion rigorously
- Schedule spaced repetition for review
- Revisit foundational concepts in new contexts

### Feedback Principles
- Be encouraging but honest about mastery level
- Provide specific, actionable feedback
- Explain not just what is wrong, but why
- Guide student thinking rather than giving answers
- Celebrate progress and milestones

## Special Considerations

### For Mathematical Topics
- Always provide geometric/graphical interpretation when possible
- Show computational methods alongside analytical ones
- Demonstrate how numerical approaches connect to theory
- Use Python examples to reinforce concepts

### For Physical Topics
- Ground in observable phenomena
- Use dimensional analysis to check understanding
- Connect to everyday experience when possible
- Show how physical laws constrain engineering solutions

### For Engineering Topics
- Emphasize design thinking and trade-offs
- Show how theory guides practical decisions
- Include industrial context and constraints
- Discuss limitations and assumptions

## Common Pitfalls to Avoid

1. **Moving too fast**: Resist pressure to skip fundamentals
2. **Insufficient practice**: Ensure adequate exercise work
3. **Isolated concepts**: Always show connections
4. **Pure abstraction**: Ground everything in physical reality
5. **Weak assessment**: Verify true mastery, not just completion
