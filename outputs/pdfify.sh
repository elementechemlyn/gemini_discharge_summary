#!/bin/bash

PDF_CONVERT=/usr/bin/wkhtmltopdf

for dir in */; do mkdir -p -- "$dir/pdf"; done

for i in `find . -name "*.html"`; 
do 
echo $i
OUTPUT_FOLDER="`dirname $i`/pdf"
OUTPUT_FILE="${OUTPUT_FOLDER}/`basename $i .html`.pdf"
echo $OUTPUT_FILE
$PDF_CONVERT $i $OUTPUT_FILE
done
