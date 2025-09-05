import os

os.environ["HF_HOME"] = "./cache/huggingface"


from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="stanfordnlp/imdb",
    repo_type="dataset",
    local_dir="./raw/imdb",
    cache_dir="./cache/",
)

snapshot_download(
    repo_id="McAuley-Lab/Amazon-Reviews-2023",
    repo_type="dataset",
    local_dir="./raw/amazon",
    cache_dir="./cache/",
)

snapshot_download(
    repo_id="fancyzhx/ag_news",
    repo_type="dataset",
    local_dir="./raw/ag_news",
    cache_dir="./cache/",
)

snapshot_download(
    repo_id="SetFit/bbc-news",
    repo_type="dataset",
    local_dir="./raw/bbc_news",
    cache_dir="./cache/",
)

snapshot_download(
    repo_id="tasksource/jigsaw_toxicity",
    repo_type="dataset",
    local_dir="./raw/jigsaw_toxicity",
    cache_dir="./cache/",
)
