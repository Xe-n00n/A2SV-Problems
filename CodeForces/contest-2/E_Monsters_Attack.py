def is_surviving(monsters_count, bullet_count, healths, positions):
    monsters = sorted((abs(positions[i]), healths[i]) for i in range(monsters_count))
    lost_points=0
    for distance, health in monsters:
        lost_points+=health
        if (bullet_count * distance) < lost_points : 
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    test_cases=int(input())
    for _ in range(test_cases):
        monsters_count, bullets_count=map(int, input().split())
        healths=list(map(int, input().split()))
        positions=list(map(int, input().split()))
        is_surviving(monsters_count, bullets_count, healths, positions)
        
