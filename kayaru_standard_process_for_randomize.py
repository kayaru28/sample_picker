import random
import kayaru_standard_process as kstd


def get_val_int(start,end):
    
    if not ( kstd.is_int(start) ):
        message = "start is not int"
        kstd.echo_error_occured(message)
        return None
    elif not ( kstd.is_int(end) ):
        message = "end is not int"
        kstd.echo_error_occured(message)
        return None

    if (start > end):
        message = "start is bigger than end"
        kstd.echo_error_occured(message)
        return None

    step    = 1
    end     = end + 1
    val_int = random.randrange(start,end,step)
    return val_int

def get_val_even_int(start,end):
    
    if not ( kstd.is_even_number(start) ):
        message = "start is not even number"
        kstd.echo_error_occured(message)
        return None
    elif not ( kstd.is_even_number(end) ):
        message = "end is not even number"
        kstd.echo_error_occured(message)
        return None

    if (start > end):
        message = "start is bigger than end"
        kstd.echo_error_occured(message)
        return None

    step = 2
    val_even_number = random.randrange(start,end,step)
    return val_even_number



