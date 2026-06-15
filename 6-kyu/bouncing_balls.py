# Task: Bouncing Balls
# Link: https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
# Level: 6 kyu

def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        count = 1
        rebound = h * bounce
        while rebound > window:
            count += 2
            rebound = rebound * bounce
        return count
    else:
        return -1
    
testing = (3, 0.66, 1.5) #3
print(bouncing_ball(*testing))