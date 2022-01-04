def tickets(people):
        
        if people[0] != 25:
            return 'NO'
        
        notes_25 = 1
        notes_50 = 0
                        
        for note in people[1:]:
            if note == 25:
                notes_25 += 1
                
            if note == 50:
                if not notes_25:
                    return 'NO'
                else:
                    notes_50 += 1
                    notes_25 -= 1
            
            if note == 100:
                if not notes_25:
                    return 'NO'
                elif not notes_50 and notes_25 <= 2:
                    return 'NO'
                elif not notes_50:
                    notes_25 -=3
                else:
                    notes_50 -= 1
                    notes_25 -= 1
                    
        return 'YES'