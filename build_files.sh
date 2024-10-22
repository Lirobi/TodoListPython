# build_files.sh
pip3 install -r requirements.txt
yes yes | python3 manage.py collectstatic 