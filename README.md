# Automated Script Writing 

## Problem
- Films and shows are produced at high rates and Writer’s block can lead to lack of creativity
- Humans lack consistency and are error-prone, AI is here for help!
  Use AI to generate scripts based on emotions.

## Approach
Image

## Components
- Script Dataset
  - consists of 862 ﬁlm scripts from The Internet Movie Script Database (IMSDb), representing 7,400 characters, with a total of 664,000 lines of dialogue and 9,599,000 tokens (UC Santa Cruz - Baskin Engineering)
- IBM Watson Tone Analyzer
  - used for sentiment analysis to gather dataset of lines based on different emotions
  - limited to 3000 API calls
- nVidia Teslas
  - GPUs used for training large sets of texts, specifically labelled sets from tone analyzer
- OpenAI’s GPT-2 Model
  - text generating AI used to develop new scripts based on user’s input

## Architecture
 Image

## Sample
 Image

## Next steps
- Refining scripts 
 - removing repeated lines
 - format output text to a strict script structure

 - Maintaining context 
     - more coherent and better flow

 - Dialogues
   - script is mainly scenes and narration currently