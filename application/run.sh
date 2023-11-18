APK_PATH="./app_test/test.apk"
SERIAL="emulator-5554"
OUTPUT_DIR="out"
VENV_DIR="./R-DLD-Arduino/venv/bin/activate" 
rm -r ${OUTPUT_DIR}
mkdir ${OUTPUT_DIR}
source ${VENV_DIR}         
#dld -a ${APK_PATH} -o ${OUTPUT_DIR}/test -grant_perm -count 2250
dld -a ${APK_PATH} -o ${OUTPUT_DIR}/test -grant_perm -count 2250 -robot

