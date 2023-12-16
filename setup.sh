#!/bin/sh

# preproccess
THIS_FILE_DIR=$(dirname "$0")
cd "$THIS_FILE_DIR" || (echo "failure change directory ${THIS_FILE_DIR}" && exit 1)

# setting .env
SAMPLE_ENV="work/.env.sample"
ENV_FILE="work/.env"

printf "prease input jupyter notebook password > "
read -rs PASSWORD
printf "\n"
PASSWORD=$(printf "%s" "$PASSWORD" | sed 's@/@\\/@')
cat "$ENV_FILE" > .env.bak
cat "$SAMPLE_ENV" | sed "s/<Your Password for Jupyter Notebook>/${PASSWORD}/" > "$ENV_FILE"

# unzip pkl.zip
unzip -n work/input/LSWMD_25519.pkl.zip -d work/input/ || echo 'cancel unzip because already exists.'

# result
printf "\033[32mdone\033[m"
