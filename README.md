In order to use the repo, you'd need yourself a few models into the `data/models` folder.
The models I've used were as follows:
- 20230227__kch_gstt_trained_model_494c3717f637bb89.zip - SNOMED
- umls_self_train_model_e6a3660d3ba19f52.zip - UMLS
- trained_model_KCH_cn_only_23_11_27.zip - HPO

PS:
If you do want to do this with another model, you'd need to  change the model names in `scripts/run_all_tests.sh`.

Once you have the models, you can simply run:
```
bash scripts/run_all_tests.sh
```

This will run through each model and their corresponding MCT export(s) with and without the `_print_stats` changes.
It will output these into a file in `data/out` folder.
The script will then analyse the output and see if it is different.

PS:
The reason the difference checker is separate is because I need to run with two different `medcat` installs.
And that cannot (easily) be done within one runtime.
