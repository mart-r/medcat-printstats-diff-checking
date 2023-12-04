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


## Current Results

Currently, all but one of the model-dataset combinations are identical.

The one that returns different results is `data/model_packs/umls_self_train_model_e6a3660d3ba19f52.zip` along with `data/mct_export/trainer_export.json`.
The results themselves are not different in themselves, they are just shown somewhat differently due to the random order of elements in sets. That is because some CUIs apparently don't have a preferred name, and this case the "first" of any name for the CUI is shown for false positives and false negatives. And because the CUI names are in a set (the "order" of which is different in each run) a different name is selected in different runs.

Currently, the only differences are:
```
Docs with false positives: 1605; 1687

Docs with false negatives: 1605; 1687



False Positives

investigation                                                          - C0220825             -         10
one~daily                                                              - C1170480             -          8
liquid                                                                 - C0302908             -          7
noted                                                                  - C4288581             -          7
ruled                                                                  - C1446409             -          6
aspiration                                                             - C0349707             -          6
penetrated                                                             - C0205321             -          5
cup~physical~object                                                    - C3853579             -          4
treatment                                                              - C1522326             -          4
deny                                                                   - C2700401             -          3


False Negatives

uti~urinary~tract~infection                                            - C0042029             -          4
non~insulin~dependent~diabetes~mellitus                                - C0011860             -          3
hld~hyperlipidaemia                                                    - C0020473             -          3
ami~acute~myocardial~infarction                                        - C0155626             -          2
gastresophageal~reflux~disease                                         - C0017168             -          1
bp~hypertension                                                        - C0020538             -          1
stroke                                                                 - C0038454             -          1
tia~transient~ischaemic~attack                                         - C0007787             -          1
chd~coronary~heart~disease                                             - C0010068             -          1
cardiomyopathy                                                         - C0878544             -          1


True Positives

bp~hypertension                                                        - C0020538             -          3
skin~lesion                                                            - C0037284             -          1
cardiovascular~disorder                                                - C0007222             -          1
myocardial~infarction                                                  - C0027051             -          1
joint~inflammation                                                     
```
vs
```
Docs with false positives: 1687; 1605

Docs with false negatives: 1687; 1605



False Positives

assessment                                                             - C0220825             -         10
one~daily                                                              - C1170480             -          8
fluid                                                                  - C0302908             -          7
noted                                                                  - C4288581             -          7
ruled                                                                  - C1446409             -          6
removal~by~suction                                                     - C0349707             -          6
penetration                                                            - C0205321             -          5
cups                                                                   - C3853579             -          4
treating                                                               - C1522326             -          4
deny                                                                   - C2700401             -          3


False Negatives

uti~urinary~tract~infection                                            - C0042029             -          4
type~ii~diabetes~mellitus                                              - C0011860             -          3
hyperlipidaemia                                                        - C0020473             -          3
ami~acute~myocardial~infarction                                        - C0155626             -          2
gastro~esophageal~reflux~disease                                       - C0017168             -          1
high~blood~pressure~disorder                                           - C0020538             -          1
stroke                                                                 - C0038454             -          1
transient~ischaemic~attack                                             - C0007787             -          1
coronary~heart~disease                                                 - C0010068             -          1
cardiomyopathy                                                         - C0878544             -          1


True Positives

high~blood~pressure~disorder                                           - C0020538             -          3
skin~lesion                                                            - C0037284             -          1
cardiovascular~disorder                                                - C0007222             -          1
myocardial~infarct                                                     - C0027051             -          1
inflammatory~arthritis 
```

PS:
There is also a difference in the order of documents. But that's also due to the same reason.
