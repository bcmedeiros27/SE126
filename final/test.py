def purchase()        
    if seatrow >= 0 and seatrow < len(rows):
            if seat in seat_map:
                if seat_map[seat][seatrow] == "#":
                    if seatrow < 6:
                        print("Seat purchased for $200.00")
                        purchase += 200.00
                    elif seatrow < 11:
                        print("Seat purchased for $175.00")
                        purchase += 175.00
                    else:
                        print("Seat purchased for $150.00")
                        purchase += 150.00
                    print("Seat purchased")
                    seat_map[seat][seatrow] = "*"
                else:
                    print("Seat not available")
            else:
                print("Invalid seat letter")
        else:
            print("Invalid row number")
        for i in range(len(rows)):
            print(f"{rows[i]:2} {' '.join(seat_map[letter][i] for letter in seat_map)}")
        stop = input(f"Do you want to purchase another seat? (y/n): {purchase}").lower()