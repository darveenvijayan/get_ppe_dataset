# TO DOWNLOAD FILES FROM GOOGLE DRIVE USING WGET

# In the above command change the FILEID by above id extracted and rename FILENAME for your own simple use.

# SAMPLE:
# wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=FILEID" -O FILENAME && rm -rf /tmp/cookies.txt





wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1rGY-M2LNUZ9lLaiyeLqrAFQVoGn9KauY' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1rGY-M2LNUZ9lLaiyeLqrAFQVoGn9KauY" -O instances_train2017.json && rm -rf /tmp/cookies.txt




# LINK: https://drive.google.com/file/d/1rGY-M2LNUZ9lLaiyeLqrAFQVoGn9KauY/view?usp=sharing


