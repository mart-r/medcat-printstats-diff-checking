MODEL_PATH=$1
MCT_EXPORT=$2
OUTPUT_PATH=$3

echo "Running on model: "$MODEL_PATH
echo "And MCT export  : "$MCT_EXPORT

# currently master
TARGET="https://github.com/CogStack/MedCAT.git@76b75cc4e3558e9a48d1fe8aa43ba23621652a75"
MCT_TYPE="with-OLD-print_stats"
bash scripts/run_with_target.sh $MODEL_PATH $MCT_EXPORT $OUTPUT_PATH $TARGET $MCT_TYPE

TARGET=""https://github.com/CogStack/MedCAT.git@CU-2e77a31-improve-print_stats""
MCT_TYPE="with-NEW-print_stats"
bash scripts/run_with_target.sh $MODEL_PATH $MCT_EXPORT $OUTPUT_PATH $TARGET $MCT_TYPE
