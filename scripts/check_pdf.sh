#!/bin/bash

for file in /tmp/SampTA_Main_*.pdf; do
  paper_number=$(basename "$file" | grep -oE '[0-9]+')
  creator=$(pdfinfo "$file" | grep "Creator" | sed 's/Creator://' | sed -r 's/^\s+//g' )
  pages=$(pdfinfo "$file" | grep "Pages" | sed 's/Pages://' | sed -r 's/^\s+//g' )
  echo "Paper: $paper_number - ($pages p.) - Creator: $creator"
done
