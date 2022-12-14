from sys import stdin

index = {}

for line in stdin:

    row = line.rstrip('\n').split()

    if row[0] in index:
        index[row[0]].append(row[1])
    else:
        index[row[0]] = [row[1]]

for word in index:
    postings_list = [str(doc_id) for doc_id in index[word]]

    postings = ','.join(postings_list)
    print(f"{word}\t{postings}\t{1}")
