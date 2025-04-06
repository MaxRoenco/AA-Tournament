def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    # First move cooperation
    if len(my_history) == 0:
        return 1
    
    # Always defect on last round of known-length games
    if rounds is not None and len(my_history) == rounds - 1:
        return 0
    
    # Pattern recognition functions
    def is_tit_for_tat(my_hist, opp_hist):
        if len(opp_hist) < 3 or opp_hist[0] != 1:
            return False
        matches = 0
        for i in range(1, len(my_hist)):
            if opp_hist[i] == my_hist[i - 1]:
                matches += 1
        # Allow for some noise (90% match is still considered tit-for-tat)
        return matches >= (len(my_hist) - 1) * 0.9
    
    def is_random_strategy(opp_hist):
        if len(opp_hist) < 20:  # Need more data to determine randomness
            return False
        ones = opp_hist.count(1)
        proportion = ones / len(opp_hist)
        # Check if close to 50/50 distribution
        return 0.4 <= proportion <= 0.6
    
    def detect_exploitation_pattern(my_hist, opp_hist):
        """Detect if opponent exploits cooperation"""
        if len(my_hist) < 10:
            return False
            
        # Calculate how often opponent defects after we cooperate
        defect_after_coop = 0
        coop_count = 0
        
        for i in range(len(my_hist) - 1):
            if my_hist[i] == 1:  # We cooperated
                coop_count += 1
                if opp_hist[i+1] == 0:  # They defected next
                    defect_after_coop += 1
        
        # If they defect more than 60% of the time after we cooperate, they're exploiting
        return coop_count > 0 and defect_after_coop / coop_count > 0.6
    
    def detect_pattern(hist, length=3):
        """Check if there's a repeating pattern of given length"""
        if len(hist) < length * 2:
            return False, None
            
        for i in range(len(hist) - length * 2 + 1):
            pattern = hist[i:i+length]
            next_seq = hist[i+length:i+length*2]
            if pattern == next_seq:
                return True, pattern
        return False, None
    
    # Strategy against tit-for-tat: always cooperate for mutual benefit
    if is_tit_for_tat(my_history, opponent_history):
        return 1
    
    # Strategy against random players: always defect
    if is_random_strategy(opponent_history):
        return 0
    
    # Detect if opponent is exploiting our cooperation
    if detect_exploitation_pattern(my_history, opponent_history):
        return 0  # Stop being exploited
    
    # Check for repeating patterns in opponent's moves
    has_pattern, pattern = detect_pattern(opponent_history, 3)
    if has_pattern and pattern:
        # Predict next move based on pattern and counter it
        next_predicted = pattern[len(my_history) % len(pattern)]
        return 1 if next_predicted == 1 else 0  # Cooperate only with cooperative patterns
    
    # Recovery from mutual defection
    if len(my_history) >= 2:
        # If both players defected in the last two rounds, try to break the cycle
        if all(move == 0 for move in my_history[-2:]) and all(move == 0 for move in opponent_history[-2:]):
            return 1
    
    # Check recent cooperation ratio from opponent
    recent_window = min(10, len(opponent_history))
    recent_coop_rate = opponent_history[-recent_window:].count(1) / recent_window
    
    # If opponent has been cooperative recently, cooperate
    if recent_coop_rate > 0.7:
        return 1
    
    # If opponent has been mostly defecting recently, defect
    if recent_coop_rate < 0.3:
        return 0
    
    # Default to modified tit-for-tat with forgiveness
    if opponent_history[-1] == 1:
        return 1  # Always reciprocate cooperation
    else:
        # 20% chance to forgive a defection to break defection cycles
        import random
        return 1 if random.random() < 0.2 else 0