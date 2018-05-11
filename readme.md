# es-export-csv

This will perform a basic match all query within the date math specific date range (against `@timestamp` field), returning results as a CSV file. I'll probably add more later.

## Usage

```
usage: es_export_csv.py [-h] [-t TOTAL] [-e HOST] [--from RANGE_FROM]
                        [--to RANGE_TO] [-o OUTPUT] [--only-source]
                        [--no-header] [-u USERNAME] [-p PASSWORD]
                        index [fields [fields ...]]

positional arguments:
  index                 index to export
  fields                limit output to fields (if set) or return all fields
                        (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -t TOTAL, --total TOTAL
                        max docs to return (default: 500)
  -e HOST, --host HOST  cluster API (default: http://localhost:9200)
  --from RANGE_FROM     range start (default: now-1d/d)
  --to RANGE_TO         range end (default: now/d)
  -o OUTPUT, --output OUTPUT
                        output file (default: results.csv)
  --only-source         only return source fields; exclude metadata fields
                        (default: True)
  --no-header           do not write csv header (default: False)
  -u USERNAME, --username USERNAME
                        basic auth username (default: username)
  -p PASSWORD, --password PASSWORD
                        basic auth password (default: None)
```

`--range-from` and `--range-to` accept [date math](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/common-options.html#date-math) formatted strings. This should give you great flexibility in date range selection without knowing epochs.
