# Datasets

## SemEval 2023 Task 3: Propaganda Detection ✅
https://propaganda.math.unipd.it/semeval2023task3/

- News genre categorization: given a news article, determine whether it is an opinion piece, aims at objective news reporting, or is a satire piece. This is a multi-class (single-label) task at article-level. 
- Framing detection: given a news article, identify the frames used in the article. This is a multi-label task at article-level. A frame is the perspective under which an issue or a piece of news is presented. We consider 14 frames: Economic, Capacity and resources, Morality, Fairness and equality, Legality, constitutionality and jurisprudence, Policy prescription and evaluation, Crime and punishment, Security and defense, Health and safety, Quality of life, Cultural identity, Public opinion, Political, External regulation and reputation. This taxonomy, as well as a discussion on the definitions of frame, For details on the definition of frame and the taxonomy used in our annotations, we followed (Card et al., 2015). Specifically, 
- Persuasion Techniques Detection: Given a news article, identify the persuasion techniques in each paragraph. This is a multi-label task at paragraph level. Justification, simplification, distraction, call, manipulative wording, attack on reputation.
- All multiclass classification

**Comparable to propaganda part of no_prop_overlap dataset but only multiclass though could be made multiple. Good topic fit but different length (article/paragraph instead of sentence). High fit.**

## Measuring Hate Speech Dataset ✅
https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech

- Hate speech score
- Ordinal labels sentiment, (dis)respect, insult, humiliation, inferior status, violence, dehumanization, genocide, attack/defense, hate speech benchmark
- Includes 8 target identity groups (race/ethnicity, religion, national origin/citizenship, gender, sexual orientation, age, disability, political ideology) and - 42 target identity subgroups, as well as 6 annotator demographics and 40 subgroups.
- hate_speech_score - continuous hate speech measure, where higher = more hateful and lower = less hateful. > 0.5 is approximately hate speech, < -1 is counter or supportive speech, and -1 to +0.5 is neutral or ambiguous.
- text - lightly processed text of a social media post
- comment_id - unique ID for each comment
- annotator_id - unique ID for each annotator
- sentiment - ordinal label that is combined into the continuous score
- respect - ordinal label that is combined into the continuous score
- insult - ordinal label that is combined into the continuous score
- humiliate - ordinal label that is combined into the continuous score
- status - ordinal label that is combined into the continuous score
- dehumanize - ordinal label that is combined into the continuous score
- violence - ordinal label that is combined into the continuous score
- genocide - ordinal label that is combined into the continuous score
- attack_defend - ordinal label that is combined into the continuous score
- hatespeech - ordinal label that is combined into the continuous score
- annotator_severity - annotator's estimated survey interpretation bias

**Good mix of datatypes, both techniques of speech and entity recognition, similar to IAC _bi scores and IBM WA/WA_bi parts of no_prop_overlap. High fit.**

## Comparative Agendas Project: Datasets & Codebooks ✅
https://www.comparativeagendas.net/datasets_codebooks

- Organizes government activities—such as laws, speeches, hearings, and debates—into a shared, standardized system of 21 major topics and over 220 subtopics.
- Political text coded against major topics and subtopics. CMP records position, CAP codes topic. Major/sub structure could use hierarchical task_structure. 

**High fit with CMP.**