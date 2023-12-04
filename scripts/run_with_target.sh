MODEL_PATH=$1
MCT_EXPORT=$2
OUTPUT_PATH=$3
TARGET=$4
MEDCAT_TYPE=$5

echo "Installing medcat from "$TARGET" ($MEDCAT_TYPE)"
# uninstall old just in case
pip uninstall -y medcat >& /dev/null
# install target version
pip install git+$TARGET >& /dev/null
# check whether or not we have the new print stats functionaltiy
python -c "import medcat.stats.stats" >& /dev/null
exit_status=$?
if [ $exit_status -eq 0 ]; then
    echo "Has medcat.stats.stats."
else
    echo "Does NOT have medcat.stats.stats"
fi

echo "Done with medcat install"

echo "===========================================" >> $OUTPUT_PATH

echo "Running test and writing output to "$OUTPUT_PATH

python src/run_test.py $MODEL_PATH $MCT_EXPORT >> $OUTPUT_PATH

echo "===========================================" >> $OUTPUT_PATH

echo "Done with this target"