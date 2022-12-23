from PIL import Image
import pandas as pd
from tqdm import tqdm
import torch
import os

if __name__ == "__main__":
    pd = pd.read_csv("./dataset/train.csv")
    pd_dict = pd.to_dict(orient='list')

    file_name = []
    for i in pd_dict["id"]:
        file_name.append(f"train/{i}.png")
    pd_dict.update(dict(file_name=file_name))

    pd1 = dict(
        id=pd_dict["id"][:50000],
        attribute_ids=pd_dict["attribute_ids"][:50000],
        file_name=pd_dict["file_name"][:50000],
    )
    pd2 = dict(
        id=pd_dict["id"][50000:],
        attribute_ids=pd_dict["attribute_ids"][50000:],
        file_name=pd_dict["file_name"][50000:],
    )

    pil_image = []
    for i in tqdm(pd1["file_name"]):
        pil_image.append(Image.open(os.path.join("dataset", i)))

    pd1.update(dict(pil_image=pil_image))
    torch.save(pd1, "iMet-Collection-2019_train_0.pt")

    pil_image = []
    for i in tqdm(pd2["file_name"]):
        pil_image.append(Image.open(os.path.join("dataset", i)))

    pd2.update(dict(pil_image=pil_image))
    torch.save(pd2, "iMet-Collection-2019_train_1.pt")

