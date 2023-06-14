# Search Your Images Using Natural Language

## Install Dependencies
- Optional: cuda runtime
- Python 3.6+ and Pip
- `pip install -r requirements.txt`

## Basic Usage
- Execute the script in captioning mode: `python3 main.py -mode captioning -d "<DIST DIR>"`
- Execute the script in query mode: `python3 main.py -mode query -d "<DIST DIR>" -q "<QUERY>"` eg, "Is it a document?"
- Use `-r` flag to scan your dist dir recursivly.

## References
[BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://arxiv.org/abs/2201.12086)
