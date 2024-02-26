t = int(input())  # Number of test cases
for _ in range(t):
    n, k = map(int, input().split())  # Number of monsters and bullets per second
    health = list(map(int, input().split()))  # Health of each monster
    positions = list(map(int, input().split()))  # Position of each monster

    # Pairing health with position and sorting by absolute position
    monsters = sorted(zip(health, positions), key=lambda x: abs(x[1]))

    total_bullets_needed = 0  # Total bullets needed to kill all monsters before they reach the character
    can_survive = True  # Initial assumption

    # Iterate over each monster, from nearest to farthest
    for health, position in monsters:
        distance = abs(position)  # Distance from the player
        # Bullets needed to kill this monster
        total_bullets_needed += health

        # Maximum bullets that can be used until this monster reaches the player
        max_bullets_until_reach = distance * k

        # If the total bullets needed so far exceed what we can use, we can't survive
        if total_bullets_needed > max_bullets_until_reach:
            can_survive = False
            break

    print("YES" if can_survive else "NO")
