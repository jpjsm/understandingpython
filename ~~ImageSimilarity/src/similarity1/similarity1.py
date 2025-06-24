"""Identify visually similar images using hashing.

:source: https://practicaldatascience.co.uk/data-science/how-to-use-image-hashing-to-identify-visually-similar-or-duplicate-images
:author: Matt Clarke (https://practicaldatascience.co.uk/about)
"""
import json
from datetime import datetime, timezone
from os import walk
from pathlib import Path

from annoy import AnnoyIndex
import imagehash
import pandas as pd
from PIL import Image

ALGORITHMS = [
    "Average",
    "Perceptual",
    "Difference",
    "Wavelet",
    "HSV_color",
    "cropresistant",
]

IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp", ".heif", ".svg"}

# number of bytes used in the image hash for all algorithms, except colorhash
HASH_SIZE = 16
# The number of bits used per bin in color hash
BINBITS = 6


photoslocation = r"C:\SamplePictures"
hashlocation = r"C:\SamplePicturesHash"

image_paths = []
for (dir_path, _, file_names) in walk(photoslocation):
    _dir_path = Path(dir_path)
    image_paths.extend(
        [
            str(_dir_path.joinpath(file_name))
            for file_name in file_names
            if Path(file_name).suffix in IMAGE_TYPES
        ]
    )

image_count = len(image_paths)

columns = ["image"] + ALGORITHMS
for algorithm in ALGORITHMS:
    columns += [algorithm]
    if algorithm != "cropresistant":
        columns += [algorithm + "_array"]

df = pd.DataFrame(columns=columns)

duplicates = {h: {} for h in ALGORITHMS}

hashing = {
    "Average": lambda image: imagehash.average_hash(image, HASH_SIZE),
    "Perceptual": lambda image: imagehash.phash(image, HASH_SIZE),
    "Difference": lambda image: imagehash.dhash(image, HASH_SIZE),
    "Wavelet": lambda image: imagehash.whash(image, HASH_SIZE),
    "HSV_color": lambda image: imagehash.colorhash(image, BINBITS),
    "cropresistant": lambda image: imagehash.crop_resistant_hash(
        image, hash_func=imagehash.phash
    ),
}

for image_path in image_paths:
    print(f"processing image: {image_path}")
    image = Image.open(image_path)

    data = {
        "image": image_path,
    }

    for algorithm in ALGORITHMS:
        hash = hashing[algorithm](image)

        data[algorithm] = hash

        if algorithm != "cropresistant":
            data[algorithm + "_array"] = hash.hash.astype("int").flatten()

        hex_value = str(hash)
        if hex_value not in duplicates[algorithm]:
            duplicates[algorithm][hex_value] = []

        duplicates[algorithm][hex_value] += [image_path]

    df = df.append(data, ignore_index=True)

print(df)

# Find exact hash duplicates
# --> Remove non-duplicates
for algorithm in ALGORITHMS:
    hex_values = list(duplicates[algorithm].keys())
    for hex_value in hex_values:
        if len(duplicates[algorithm][hex_value]) == 1:
            del duplicates[algorithm][hex_value]

    print(f"listing duplicates for '{algorithm}' algorithm.")
    if len(duplicates[algorithm]) > 0:
        for hex_value in duplicates[algorithm]:
            print(f"    {hex_value}: {duplicates[algorithm][hex_value]}")
            dup_images = []
            canvas = Image.new("RGB", (1800, 600))
            for image_path in duplicates[algorithm][hex_value]:
                dup_images.append(Image.open(image_path))

            tiles = len(dup_images)
            tile_width = 1800 // tiles
            tile_height = 600

            tile_index = 0
            for dup_image in dup_images:
                width, height = dup_image.size
                resize_factor = 1.0
                if width > tile_width:
                    resize_factor = tile_width / width

                if height * resize_factor > tile_height:
                    resize_factor = tile_height / (height * resize_factor)

                resize_value = (int(width * resize_factor), int(height * resize_factor))
                canvas.paste(
                    dup_image.resize(resize_value),
                    (tile_index * tile_width, 0),
                )

                tile_index += 1

            print(f"Saving duplicates for '{algorithm}', group: {hex_value}")
            now = datetime.now(timezone.utc).astimezone()
            name_prefix = f"{algorithm}_{hex_value}_{now.strftime('%Y%m%d_%H%M%S')}"
            dup_path = Path(hashlocation).joinpath(name_prefix + ".png")
            canvas_name = str(dup_path)
            canvas.save(canvas_name, format="png")
            dup_metadata = {
                "algorithm": algorithm,
                "group": hex_value,
                "images": duplicates[algorithm][hex_value],
            }

            json_path = str(Path(hashlocation).joinpath(name_prefix + ".json"))
            with open(json_path, "w") as outfile:
                json.dump(dup_metadata, outfile, indent=4)

        print()
    else:
        print("    --- no duplicates ---")


dist_function = "hamming"
imageSimilarityNearestNeighbors_db = {}

for algorithm in [a for a in ALGORITHMS if a != "cropresistant"]:
    print(f"Create nearest neighbors 'DB' using: {algorithm}")
    _array = df[algorithm + "_array"]
    vector_length = _array[0].shape[0]
    imageSimilarityNearestNeighbors_db[algorithm] = AnnoyIndex(
        vector_length, dist_function
    )
    for i in len(_array):
        imageSimilarityNearestNeighbors_db[algorithm].add_item(i, _array[i])

    imageSimilarityNearestNeighbors_db[algorithm].build(image_paths // 5)

print("Finding the 5 Nearest Neighbors of each image by algorithm.")
max_neighbors = 5
for algorithm in [a for a in ALGORITHMS if a != "cropresistant"]:
    for index in range(image_paths):
        nns = imageSimilarityNearestNeighbors_db[algorithm].get_nns_by_item(
            index, max_neighbors, include_distances=True
        )
        print(nns)
