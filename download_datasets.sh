from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="stanfordnlp/imdb",
    repo_type="dataset",
    local_dir="./raw/imdb"
)