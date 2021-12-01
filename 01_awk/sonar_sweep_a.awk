#!/usr/bin/awk -f

# begin section
BEGIN {}

# loop section
{
    if ($0 > prev) {
        count++
    }
    
    prev=$0;
}

# end section
END {
    # print the result - 1, 
    # as the first measurement should not be counted
    print count - 1;
}
