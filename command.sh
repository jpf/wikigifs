# Run these commands by hand:
#
# This is a huge file. Over 7 GiB in size.
# $ curl -O http://dumps.wikimedia.org/commonswiki/latest/commonswiki-latest-image.sql.gz
# This takes about 10 minutes
# $ zcat commonswiki-latest-image.sql.gz | sed -e 's/),/),\n/g' | grep frameCount | python process.py > found-images
# $ cat found-images | grep -v '.png' | grep -v ' ' | grep -vi masturba | grep -vi scrotum > animated-gifs
cat $0