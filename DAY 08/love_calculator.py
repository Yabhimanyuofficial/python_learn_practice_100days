def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    t_count = combined_names.count('t')
    r_count = combined_names.count('r')
    u_count = combined_names.count('u')
    e_count_true = combined_names.count('e')
    true_score = t_count + r_count + u_count + e_count_true
    
    l_count = combined_names.count('l')
    o_count = combined_names.count('o')
    v_count = combined_names.count('v')
    e_count_love = combined_names.count('e')
    love_score = l_count + o_count + v_count + e_count_love
    
    final_score_str = str(true_score) + str(love_score)
    print(final_score_str)

calculate_love_score("Kanye West", "Kim Kardashian")