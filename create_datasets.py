import os
import requests
import pandas as pd
from ast import literal_eval
from datasets import load_dataset

length_rows = []


def save_random_sample(df: pd.DataFrame, output_path: str, sep: str = ","):
    """Sample a fraction of the dataframe and save it to CSV."""

    original_len = len(df)
    frac = 0.1
    if len(df) > 2500:
        n = 250
        df = df.sample(n=n, random_state=1944).reset_index(drop=True)
    else:
        df = df.sample(frac=frac, random_state=1944).reset_index(drop=True)
    sampled_len = len(df)
    length_rows.append(
        [os.path.basename(output_path), original_len, sampled_len])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, sep=sep)
    print(f"Created {os.path.basename(output_path)}")


def process_hf_dataset(repo_id: str, output_file: str, split="train", name=None,
                       token=False, sep=",", trust_remote_code=False):
    """Load HF dataset → sample → save as CSV."""
    dataset = load_dataset(repo_id, name=name, split=split,
                           token=token, trust_remote_code=trust_remote_code)
    df = dataset.to_pandas()

    # only join rows that have an answer for NQiI dataset as empty answers are meant
    # as negative samples for model
    if "NQiI" in repo_id:
        has_answer: pd.Series = df.answers.map(
            lambda dct: len(dct["text"]) > 0 and dct["text"][0] != ""
        )
        df: pd.DataFrame = df.loc[has_answer]

    save_random_sample(df, output_file, sep=sep)


def main():
    # Hugging Face datasets
    process_hf_dataset("alexandrainst/m_arc",
                       "unannotated_data/arc_is_random_sample.csv", name="is", token=True)
    process_hf_dataset("alexandrainst/scala",
                       "unannotated_data/scala_is_random_sample.csv", name="is", sep=";")
    process_hf_dataset("mideind/icelandic-error-corpus-IceEC",
                       "unannotated_data/iceEC_random_sample.csv", name="category")
    process_hf_dataset("vesteinn/icelandic-qa-NQiI",
                       "unannotated_data/nqii_random_sample.csv", token=True, trust_remote_code=True)
    process_hf_dataset("mideind/icelandic_qa_scandeval",
                       "unannotated_data/icelandic_qa_random_sample.csv", token=True)
    process_hf_dataset("facebook/belebele", "unannotated_data/belebele_is_random_sample.csv",
                       name="isl_Latn", split="test", token=True)
    process_hf_dataset("alexandrainst/multi-wiki-qa",
                       "unannotated_data/multiwikiqa_is_random_sample.csv", name="is")
    process_hf_dataset("mideind/icelandic-arc-challenge",
                       "unannotated_data/arc_challenge_is_random_sample.csv", token=True)
    process_hf_dataset("alexandrainst/m_mmlu",
                       "unannotated_data/mmlu_is_random_sample.csv", name="is", token=True)
    process_hf_dataset("mideind/icelandic-winogrande",
                       "unannotated_data/winogrande_is_random_sample.csv")
    process_hf_dataset("alexandrainst/m_hellaswag",
                       "unannotated_data/hellaswag_is_random_sample.csv", name="is", split="val", token=True)
    process_hf_dataset("mideind/icelandic-sentences-gec",
                       "unannotated_data/ged_is_random_sample.csv", token=True)

    # Save lengths of original and sampled datasets
    length_df = pd.DataFrame(length_rows, columns=[
                             "dataset", "original_length", "sampled_length"])
    length_df.to_csv("unannotated_data/dataset_lengths.csv", index=False)


if __name__ == "__main__":
    main()
