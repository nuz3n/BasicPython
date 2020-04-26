scores = {
    'john': 1200,
    'bobby': 2000,
    'janny': 4200
}

print(scores)
print(scores['bobby'])

scores['roger'] = 3200

print(scores)

points = {}

points['mr_a'] = 35.1
points['mr_b'] = 25.1
points['mr_c'] = 14.5

print(points)

for k, v in scores.items():
    print(k, v)
