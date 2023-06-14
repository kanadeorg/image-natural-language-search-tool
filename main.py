import os
import sys
import csv
import argparse
import torch
from PIL import Image
from rich.progress import track
from rich.console import Console
from transformers import AutoProcessor, BlipForQuestionAnswering, BlipForConditionalGeneration

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "true"
csv_fields = ['File Path', 'Result']

console = Console()

def recursive_scan(dist, model, processor, mode, query, device, dry_run):
    prompt = query if mode == "query" else "A picture of"
    with open("results.csv", "w") as index:
        results = []
        for root, _, files in track(os.walk(dist), description="Scanning image folder..."):
            for name in files:
                if name.lower().endswith(('.jpg', '.png', '.jpeg', 'bmp')):
                    img_path = os.path.join(root, name)
                    img = Image.open(img_path)
                    inputs = processor(images=img, text=prompt, return_tensors="pt").to(device)
                    outputs = model.generate(**inputs, max_new_tokens=50)
                    generation = processor.decode(outputs[0], skip_special_tokens=True)
                    results.append([img_path, generation])
        if not dry_run:
            write = csv.writer(index)
            write.writerow(csv_fields)
            write.writerows(results)

def scan(dist, model, processor, mode, query, device, dry_run):
    prompt = query if mode == "query" else "A picture of"
    with open("results.csv", "w") as index:
        results = []
        for name in track(os.listdir(dist), description="Scanning image folder..."):
            if name.lower().endswith(('.jpg', '.png', '.jpeg', 'bmp')):
                img_path = os.path.join(dist, name)
                img = Image.open(img_path)
                inputs = processor(images=img, text=prompt, return_tensors="pt").to(device)
                outputs = model.generate(**inputs, max_new_tokens=50)
                generation = processor.decode(outputs[0], skip_special_tokens=True)
                results.append([img_path, generation])
        if not dry_run:
            write = csv.writer(index)
            write.writerow(csv_fields)
            write.writerows(results)

def main():
    parser = argparse.ArgumentParser(description='Execute program in captioning mode or input a custom query')
    parser.add_argument("-m", "--mode", choices=['captioning', 'query'], default='captioning')
    parser.add_argument("-r", "--recursive", help="Scan images recursivly in the dist folder", action="store_true")
    parser.add_argument("-d", "--dist", type=str, required=True, help="Dist folder")
    parser.add_argument("--dry-run", help="If False, then it will not save index to file")
    parser.add_argument("-q", "--query", help="Search query in natural language", required='query' in sys.argv)
    args = parser.parse_args()

    console.log(f"Scanning image folder({args.dist}) in {args.mode} mode.")
    console.log("Loading model.")
    model = None
    processor = None
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    console.log(f"Running on device: {device}.")
    if (args.mode == "query"):
        model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base").to(device)
        processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-base")
    else:
        processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

    if (args.recursive):
        recursive_scan(args.dist, model, processor, args.mode, args.query, device, args.dry_run)
    else:
        scan(args.dist, model, processor, args.mode, args.query, device, args.dry_run)

if __name__ == "__main__":
    main()