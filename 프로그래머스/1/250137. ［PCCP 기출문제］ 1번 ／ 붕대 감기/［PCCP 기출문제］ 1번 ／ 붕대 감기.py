def solution(bandage, health, attacks):
    answer = 0
    elapsed_time, heal_per_sec, additional_heal = bandage
    max_health = health
    current = 0
    continuous_heal = 0
    while attacks:
        current += 1
        attack_time, attack_damage = attacks[0]
        if attack_time == current:
            del attacks[0]
            health -= attack_damage
            continuous_heal = 0
            if health <= 0:
                return -1
            
        else:
            continuous_heal += 1
            health += heal_per_sec
            if continuous_heal == elapsed_time:
                health += additional_heal
                continuous_heal = 0
            health = min(health, max_health)
            
    return health
            
        
        
    
    return answer