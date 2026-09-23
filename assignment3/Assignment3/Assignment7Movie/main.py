from models.movie import Movie

lst = []

for i in range(5):
    print("\nEnter Movie", i + 1)
    mid = int(input("Enter Movie Id: "))
    n = input("Enter Movie Name: ")
    g = input("Enter Genre: ")
    r = float(input("Enter Rating: "))
    p = float(input("Enter Ticket Price: "))
    m = Movie(mid, n, g, r, p)
    lst.append(m)

print("\nAll Movies:")
for m in lst:
    m.display()

print("\nMovies with rating greater than 8:")
for m in lst:
    if m.r > 8:
        print(m.n, m.r)

print("\nAction Movies:")
for m in lst:
    if m.g.lower() == "action":
        print(m.n)

hi = lst[0]
for m in lst:
    if m.r > hi.r:
        hi = m

print("\nHighest Rated Movie:")
print(hi.n, hi.r)

mid = int(input("\nSearch Movie Id: "))

for m in lst:
    if m.mid == mid:
        print("\nMovie Found:")
        m.display()
        break

tot = 0
for m in lst:
    tot = tot + m.r

avg = tot / len(lst)

print("\nAverage Movie Rating:")
print(round(avg, 2))

print("\nMovies with ticket price greater than 300:")
for m in lst:
    if m.p > 300:
        print(m.n, m.p)
