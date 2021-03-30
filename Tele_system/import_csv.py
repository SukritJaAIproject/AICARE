import csv

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = [str(row_index), row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                           row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20],
                           row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30],
                           row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39]
                           ]
                # columns = [str(row_index), row]
                data.append(columns)
    return data
