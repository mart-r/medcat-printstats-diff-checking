#!/bin/bash

MODEL_FOLDER="data/model_packs/"
DS_FOLDER="data/mct_export/"
OUT_FOLDER="data/out/"

# Define models
models=(
  "20230227__kch_gstt_trained_model_494c3717f637bb89.zip"
  "umls_self_train_model_e6a3660d3ba19f52.zip"
  "umls_self_train_model_e6a3660d3ba19f52.zip"
  "trained_model_KCH_cn_only_23_11_27.zip"
)

# Define MCT export datasets corresponding to each model
datasets=(
  "Keggle_MCT_export.json"
  "trainer_export.json"
  "MedCAT_Export.json"
  "MedCAT_Export_With_Text_2023-10-13_14_22_51.json"
)

# Iterate over models and their corresponding datasets
for ((i = 0; i < ${#models[@]}; i++)); do
  model=${models[i]}
  dataset=${datasets[i]}

  MFP="$MODEL_FOLDER""$model"
  DSFP="$DS_FOLDER""$dataset"

  target_file="$OUT_FOLDER""${model}_${dataset}.out"
  echo "Running test... ""$model"" and ""$dataset"" -> ""$target_file"
  bash scripts/run_tests.sh $MFP $DSFP $target_file
  echo "Comparing!"
  python src/find_difference.py $target_file
done
