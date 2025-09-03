from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="stanfordnlp/imdb", repo_type="dataset", local_dir="./raw/imdb"
)

snapshot_download(
    repo_id="McAuley-Lab/Amazon-Reviews-2023",
    repo_type="dataset",
    local_dir="./raw/amazon",
)
