#!/usr/bin/awk -f

# begin section
BEGIN {}

# loop section
{   
    if (NR > 3) {
        # compare first element of previous sliding window
        # with the last element of the next sliding window
        if ($1 > prev) {
            count++;
        }

        prev = next_prev;
        next_prev = next_next_prev;
        next_next_prev = $1;
    }
    # handle first sliding window
    else if (NR == 1) prev = $1;
    else if (NR == 2) next_prev = $1;
    else if (NR == 3) next_next_prev = $1;
}

# end section
END {
    print count;
}
