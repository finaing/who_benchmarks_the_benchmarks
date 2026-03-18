# Who benchmarks the benchmarks? A case study of LLM evaluation in Icelandic

This repository contains materials for the LREC 2026 paper "Who benchmarks the benchmarks? A case study of LLM evaluation in Icelandic", by Finnur Ágúst Ingimundarson (University of Zürich), Steinunn Rut Friðriksdóttir (University of Iceland), Bjarki Ármannsson (University of Iceland & The Árni Magnússon Institute for Icelandic Studies), Iris Edda Nowenstein (University of Iceland) and Steinþór Steingrímsson (The Árni Magnússon Institute for Icelandic Studies).

If you find the paper, code or data useful in your research, please use the following citation:

```bibtex
@misc{ingimundarson2026benchmarksbenchmarkscasestudy,
      title={Who Benchmarks the Benchmarks? A Case Study of LLM Evaluation in Icelandic}, 
      author={Finnur Ágúst Ingimundarson and Steinunn Rut Friðriksdóttir and Bjarki Ármannsson and Iris Edda Nowenstein and Steinþór Steingrímsson},
      year={2026},
      eprint={2603.16406},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2603.16406}, 
}
```

## Scripts

We provide two scripts:

1.  [``create_datasets.py``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/create_datasets.py) to show how we created the subsamples of the benchmarks we evaluated (also included in the folder [``unannotated data``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/unannotated_data).
2. [``process_data.Rmd``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/process_data.Rmd) to show how we processed the data for analysis and to reproduce the figures included in the paper. This is done on the basis of the [``who_benchmarks_the_benchmarks_annotated_data.xlsx``](https://github.com/finaing/who_benchmarks_the_benchmarks/blob/main/who_benchmarks_the_benchmarks_annotated_data.xlsx) file.







