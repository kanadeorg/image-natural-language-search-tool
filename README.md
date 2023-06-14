# Search Your Images Using Natural Language

## Install Dependencies
- Optional: cuda runtime
- Python 3.6+ and Pip
- `pip install -r requirements.txt`

## Basic Usage
- Execute the script in captioning mode: `python3 main.py -mode captioning -d "<DIST DIR>"`
- Execute the script in query mode: `python3 main.py -mode query -d "<DIST DIR>" -q "<QUERY>"` eg, "Is it a document?"
- Use `-r` flag to scan your dist dir recursivly.

```
@misc{https://doi.org/10.48550/arxiv.2201.12086,
  doi = {10.48550/ARXIV.2201.12086},
  
  url = {https://arxiv.org/abs/2201.12086},
  
  author = {Li, Junnan and Li, Dongxu and Xiong, Caiming and Hoi, Steven},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation},
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {Creative Commons Attribution 4.0 International}
}
```
