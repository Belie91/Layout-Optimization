import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Facility and slicing input
facilities = ['D', 'A', 'H', 'B', 'E', 'F', 'I', 'C', 'G']
slicing_directions = ['H', 'V', 'V', 'H', 'H', 'V', 'V', 'H']  # 8 cuts for 9 facilities

layout_width = 100
layout_height = 100

def recursive_slicing(x, y, width, height, facilities, cuts, cut_index=0):
    if len(facilities) == 1:
        return [(facilities[0], (x, y, width, height))]

    cut = cuts[cut_index]
    mid = len(facilities) // 2
    left = facilities[:mid]
    right = facilities[mid:]

    result = []
    if cut == 'H':
        h1 = height / 2
        result += recursive_slicing(x, y + h1, width, h1, left, cuts, cut_index + 1)
        result += recursive_slicing(x, y, width, h1, right, cuts, cut_index + 1 + len(left) - 1)
    else:  # 'V'
        w1 = width / 2
        result += recursive_slicing(x, y, w1, height, left, cuts, cut_index + 1)
        result += recursive_slicing(x + w1, y, w1, height, right, cuts, cut_index + 1 + len(left) - 1)

    return result

# Generate positions
facility_positions = recursive_slicing(0, 0, layout_width, layout_height, facilities, slicing_directions)

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
for name, (x, y, w, h) in facility_positions:
    ax.add_patch(patches.Rectangle((x, y), w, h, edgecolor='black', facecolor='skyblue'))
    ax.text(x + w / 2, y + h / 2, name, ha='center', va='center', fontsize=12, weight='bold')

ax.set_xlim(0, layout_width)
ax.set_ylim(0, layout_height)
ax.set_title("Slicing Layout for Facilities")
ax.set_aspect('equal')
plt.grid(True)
plt.show()
