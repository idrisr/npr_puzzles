awk -F'\t' '{print }' country.tsv | awk -F',' '{print }' | sed 's/\<[^[:space:]]*/&r/' > capitals.txt
awk -F'\t' '{print }' us_president.tsv | awk '{print }'
