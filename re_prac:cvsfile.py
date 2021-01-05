def makecvs():
    ret = []
    count = 0
    for i in range(1880, 2020):
        file_name = "names/yob%d.txt" % i
        with open(file_name, 'r') as f:
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':
                    line_data = d[:-1]
                count += int(line_data.split(',')[2])
        ret.append((i, count))
    return ret


result = makecvs()
with open('birth_by_year_re.csv', 'w') as f:
    for year, birth in result:
        data = '%s,%s\n' % (year, birth)
        print(data)
        f.write(data)
