def is_surviving(monsters_count, bullet_count, healths, positions):
    monsters = sorted((abs(positions[i]), healths[i]) for i in range(monsters_count))
    total_health = 0
    for distance, health in monsters:
        total_health += health
        if total_health > bullet_count * distance:
            return print("NO")
    return print("YES")


if __name__ == "__main__":
    test_cases=int(input())
    for _ in range(test_cases):
        monsters_count, bullets_count=map(int, input().split())
        healths=list(map(int, input().split()))
        positions=list(map(int, input().split()))
        is_surviving(monsters_count, bullets_count, healths, positions)
        
