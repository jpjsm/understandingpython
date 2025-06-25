from pathlib import Path
import random
from generator import SAMPLE_SIZE_MAX, SAMPLE_SIZE_MIN, Generator

sample_min_size = 10000
sample_max_size = 20000
samples_location = "/mnt/c/learning/python/generate-huge-random-data/samples"

for _ in range(3):
    print(f"{sample_min_size:,} - {sample_max_size:,}")
    destination_folder = Path(samples_location).joinpath(
        f"sample-size-{sample_min_size}-{sample_max_size}"
    )
    destination_folder.mkdir(parents=True, exist_ok=True)
    generator = Generator(
        sample_size_max=sample_max_size, sample_size_min=sample_min_size
    )
    for _ in range(20):
        socres_id = random.randint(10000, 20000)
        sample_file = destination_folder.joinpath(f"scores-{socres_id}.csv")
        with open(sample_file, "w") as csvfile:
            filelen = csvfile.write(generator.SamplesCsvStr)
            print(f"{sample_file} size: {filelen:,}")

    sample_min_size *= 10
    sample_max_size *= 10
