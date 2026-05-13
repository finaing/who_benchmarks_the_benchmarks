# Who benchmarks the benchmarks? A case study of LLM evaluation in Icelandic

This repository contains materials for the LREC 2026 paper "Who benchmarks the benchmarks? A case study of LLM evaluation in Icelandic", by Finnur Ágúst Ingimundarson (University of Zürich), Steinunn Rut Friðriksdóttir (University of Iceland), Bjarki Ármannsson (University of Iceland & The Árni Magnússon Institute for Icelandic Studies), Iris Edda Nowenstein (University of Iceland) and Steinþór Steingrímsson (The Árni Magnússon Institute for Icelandic Studies).

If you find the paper, code or data useful in your research, please use the following citation:

```bibtex
@inproceedings{ingimundarson-etal-2026-who,
  title = {Who Benchmarks the Benchmarks? A Case Study of LLM Evaluation in Icelandic},
  author = {Ingimundarson, Finnur Ágúst and Friðriksdóttir, Steinunn Rut and Ármannsson, Bjarki and Nowenstein, Iris and Steingrímsson, Steinþór},
  booktitle = {Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)},
  month = {May},
  year = {2026},
  pages = {4702--4715},
  address = {Palma, Mallorca, Spain},
  publisher = {European Language Resources Association (ELRA)},
  editor = {Piperidis, Stelios and Bel, Núria and van den Heuvel, Henk and Ide, Nancy and Krek, Simon and Toral, Antonio},
  doi = {10.63317/5nxcp3zw7vdz},
  abstract = {This paper evaluates current Large Language Model (LLM) benchmarking for Icelandic, identifies problems, and calls for improved evaluation methods in low/medium-resource languages in particular. We show that benchmarks that include synthetic or machine-translated data that have not been verified in any way, commonly contain severely flawed test examples that are likely to skew the results and undermine the tests’ validity. We warn against the use of such methods without verification in low/medium-resource settings as the translation quality can, at best, only be as good as MT quality for a given language at any given time. Indeed, the results of our quantitative error analysis on existing benchmarks for Icelandic show clear differences between human-authored/-translated benchmarks vs. synthetic or machine-translated benchmarks.}
}
```

## Scripts

We provide two scripts:

1.  [``create_datasets.py``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/create_datasets.py) to show how we created the subsamples of the benchmarks we evaluated (also included in the folder [``unannotated data``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/unannotated_data).
2. [``process_data.Rmd``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/process_data.Rmd) to show how we processed the data for analysis and to reproduce the figures included in the paper. This is done on the basis of the [``who_benchmarks_the_benchmarks_annotated_data.xlsx``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/who_benchmarks_the_benchmarks_annotated_data.xlsx) file.







