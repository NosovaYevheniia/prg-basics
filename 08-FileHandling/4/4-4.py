company_file = "it_company.csv"

# count = 1
# while (True):
#     try:
#         with open(company_file, "r") as file:
#             for line in file:
#                 if count <= 5:
#                     print(line)
#                     count += 1

#     except:
#         if FileNotFoundError:
#             print("File not found", company_file)

with open(company_file, "r") as f:
    while True:
        lines = []
        for l in range(5):
            line = f.readline()
            if not line:  # end of file
                break
            lines.append(line.rstrip("\n"))

        if not lines:
            break

        print("\n".join(lines))
        input("Press Enter key...")